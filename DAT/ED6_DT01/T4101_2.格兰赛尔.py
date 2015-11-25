from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AF",           # 01, 1
        "Function_2_1BF7",         # 02, 2
        "Function_3_282D",         # 03, 3
        "Function_4_2A85",         # 04, 4
        "Function_5_2B80",         # 05, 5
        "Function_6_4089",         # 06, 6
        "Function_7_57CF",         # 07, 7
        "Function_8_5D27",         # 08, 8
        "Function_9_62C0",         # 09, 9
        "Function_10_694A",        # 0A, 10
        "Function_11_6D57",        # 0B, 11
        "Function_12_70F2",        # 0C, 12
        "Function_13_7E5B",        # 0D, 13
        "Function_14_84AB",        # 0E, 14
        "Function_15_8E27",        # 0F, 15
        "Function_16_9129",        # 10, 16
        "Function_17_9326",        # 11, 17
        "Function_18_9E24",        # 12, 18
        "Function_19_A121",        # 13, 19
        "Function_20_A87B",        # 14, 20
        "Function_21_B030",        # 15, 21
        "Function_22_B4BE",        # 16, 22
        "Function_23_B731",        # 17, 23
        "Function_24_BA08",        # 18, 24
        "Function_25_BCCB",        # 19, 25
        "Function_26_BD7E",        # 1A, 26
        "Function_27_BE69",        # 1B, 27
        "Function_28_BFE1",        # 1C, 28
        "Function_29_C024",        # 1D, 29
        "Function_30_C083",        # 1E, 30
        "Function_31_C0C0",        # 1F, 31
        "Function_32_C105",        # 20, 32
        "Function_33_C179",        # 21, 33
        "Function_34_C1A5",        # 22, 34
        "Function_35_C1FB",        # 23, 35
        "Function_36_C225",        # 24, 36
        "Function_37_C25C",        # 25, 37
        "Function_38_C30D",        # 26, 38
        "Function_39_C381",        # 27, 39
        "Function_40_C3CF",        # 28, 40
        "Function_41_C43D",        # 29, 41
        "Function_42_C489",        # 2A, 42
        "Function_43_C4B3",        # 2B, 43
        "Function_44_C56D",        # 2C, 44
        "Function_45_C5FA",        # 2D, 45
        "Function_46_C6B5",        # 2E, 46
        "Function_47_C6F1",        # 2F, 47
        "Function_48_C742",        # 30, 48
        "Function_49_C796",        # 31, 49
        "Function_50_C7EA",        # 32, 50
        "Function_51_C852",        # 33, 51
        "Function_52_C930",        # 34, 52
        "Function_53_C959",        # 35, 53
        "Function_54_C9A0",        # 36, 54
        "Function_55_CA52",        # 37, 55
        "Function_56_CAD8",        # 38, 56
        "Function_57_CB28",        # 39, 57
        "Function_58_CB4F",        # 3A, 58
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Call(2, 1)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B17")
    OP_A2(0x61A)
    OP_28(0x47, 0x1, 0x4)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(108440, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x108, 107670, 1250, 24030, 135)
    SetChrPos(0x101, 107510, 1250, 23130, 90)
    SetChrPos(0x102, 107680, 1250, 22250, 45)
    SetChrPos(0x104, 106450, 1250, 22690, 90)
    TurnDirection(0xA, 0x108, 0)
    OP_0D()

    ChrTalk(
        0x108,
        "#070FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4POh, Zane! Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4PDo you feel ready for\x01",
            "the next match at noon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071FI do. And I'd like to\x01",
            "finish my registration,\x01",
            "if I may.\x02\x03",
            "Can you help me with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4PAbsolutely, I can!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4PWhen I first heard the news, I'd\x01",
            "thought to myself, how is he going\x01",
            "to fight all by himself...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "...Hey, wait a minute...\x01",
            "Aren't you the ones...\x01",
            "from yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008FHeh. How's it going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'd like to register for\x01",
            "the tournament, as auxiliary\x01",
            "members of Zane's team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Would you, now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Then we'll need you to fill\x01",
            "out these forms, please.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle, Joshua and Olivier filled out the required paperwork. Next to his\x01",
            "signature, Olivier detailed a red rose-- for 'flavor.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "So, you two are members\x01",
            "of the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But...according to your \x01",
            "profile, sir...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "'Wandering lyric, troubadour\x01",
            "extraordinaire.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "'Ambassador of peace and\x01",
            "hearts most faire.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...And there's a note under\x01",
            "it: 'Trill the extra e, and\x01",
            "don't spare the spittle'...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa ha ha! My dear, you need\x01",
            "not bother with that post-script;\x01",
            "your diction sings!\x02\x03",
            "#030FIf you wish to know more, however,\x01",
            "I'd be happy to teach you the proper\x01",
            "reading...perhaps, over tea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509FYeeeeah... That's enough of that,\x01",
            "thanks. You can just burn that\x01",
            "application. With fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FNot literally, of course.\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You're very...welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've finalized your team \x01",
            "register for the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I list Zane as team captain, with 3 auxiliary\x01",
            "members: Estelle, Joshua and Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please remember there can be\x01",
            "no changes or substitutions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FFeels like it's all about\x01",
            "to break loose, doesn't it?\x02\x03",
            "Oh yeah. Do we know who our\x01",
            "opponents are going to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We have already determined the pairings, but to\x01",
            "discourage wagering, we do not announce them\x01",
            "until just before the match is to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You can guess your opponents just prior\x01",
            "to the match, though, by taking note of\x01",
            "who else is sharing your ready room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAh, so opposing teams are\x01",
            "kept in opposing rooms,\x01",
            "I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Here. This is for you\x01",
            "and your teammates.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x372, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "You received the \x01\x07\x02",
            "Registry Card\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "Please show that to\x01",
            "the staff before you \x01",
            "enter the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, that should just about cover\x01",
            "everything. Best of luck to you\x01",
            "all! Knock 'em dead!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1BF3")

    label("loc_B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 2)), scpexpr(EXPR_END)), "loc_C04")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 107600, 1250, 23440, 90)
    SetChrPos(0x102, 107500, 1250, 22630, 90)
    TurnDirection(0xA, 0x101, 0)
    OP_6C(90000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Welcome to the Grand Arena. \x01",
            "Would you like a ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Tickets are 1000 mira per pair.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1030")

    label("loc_C04")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 107600, 1250, 23440, 90)
    SetChrPos(0x102, 107500, 1250, 22630, 90)
    TurnDirection(0xA, 0x101, 0)
    OP_6C(90000, 0)
    OP_0D()
    OP_A2(0x672)

    ChrTalk(
        0xA,
        (
            "Welcome to the Grand Arena. \x01",
            "Would you like a ticket?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(
        0x101,
        "#006FYes. Two please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFF")

    label("loc_CE3")


    ChrTalk(
        0x102,
        "#010FThank you, ma'am.\x02",
    )

    CloseMessageWindow()

    label("loc_CFF")


    ChrTalk(
        0xA,
        (
            "Preliminaries are in progress right now,\x01",
            "but the main event will last for three\x01",
            "days, starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For which day would you\x01",
            "like your ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUhh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FActually, we were hoping to catch\x01",
            "the preliminary matches, if we\x01",
            "could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, all right, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They're already more than\x01",
            "halfway finished, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Will that be a problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FNope, no problem at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Okay. Bad value, but\x01",
            "hey, not my money!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That'll be 1000 mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FWow. That's a lot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FI had heard that there was\x01",
            "some kind of discount for\x01",
            "the birthday celebration...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm sorry, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This year there have been some...\x01",
            "complications...that have made it\x01",
            "impossible for us to offer discounts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FOh, okay. That's pretty sucky.\x01",
            "But, what can you do?\x02\x03",
            "Let's see... 900, 950...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1030")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Pay 1000 mira]\x01",      # 0
            "[Don't pay]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_109D"),
        (1, "loc_1209"),
        (SWITCH_DEFAULT, "loc_1242"),
    )


    label("loc_109D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B7")
    OP_22(0x14, 0x0, 0x64)
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0xA,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Here are your tickets.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received two \x07\x02",
            "Grand Arena Tickets\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36B, 2)
    OP_A2(0x60C)
    OP_A2(0x60C)
    OP_28(0x45, 0x1, 0x800)

    ChrTalk(
        0xA,
        (
            "The entrance to the arena is\x01",
            "directly to your left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Show your tickets at the gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1204")

    label("loc_11B7")


    ChrTalk(
        0x101,
        "#004F(Crap...I don't have enough.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F(We'll have to come back.)\x02",
    )

    CloseMessageWindow()

    label("loc_1204")

    EventEnd(0x0)
    Jump("loc_1242")

    label("loc_1209")


    ChrTalk(
        0xA,
        (
            "Thank you. We look forward\x01",
            "to your next visit.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1242")

    label("loc_1242")

    Jump("loc_1BF3")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_12C6")

    ChrTalk(
        0xA,
        (
            "Everyone looks so happy\x01",
            "out on the streets today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The queen's charisma is quite\x01",
            "a positive influence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1381")

    label("loc_12C6")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        (
            "I'm so glad the birthday\x01",
            "celebration is off to such\x01",
            "a great start!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone looks so happy\x01",
            "out on the streets today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The queen's charisma is quite\x01",
            "a positive influence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1381")

    Jump("loc_1BF3")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1407")
    TurnDirection(0xA, 0x108, 400)

    ChrTalk(
        0xA,
        (
            "Well, if it isn't Joshua and\x01",
            "Zane!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...What's the matter? You two\x01",
            "look troubled. Something on\x01",
            "your mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1491")

    ChrTalk(
        0xA,
        (
            "Well, the Martial Arts Competition went off\x01",
            "without a hitch, but I'm still a bit worried\x01",
            "about the birthday celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(
        0xA,
        (
            "Congratulations on your stunning\x01",
            "victory! Goooo team!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hope you enjoy the dinner\x01",
            "party-- it promises some\x01",
            "serious deliciousness!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160E")

    label("loc_152C")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        (
            "Congratulations on your stunning\x01",
            "victory! Goooo team!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wasn't able to see your match,\x01",
            "but I heard it was a heck of a\x01",
            "thing to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hope you enjoy the dinner\x01",
            "party-- it promises some\x01",
            "serious deliciousness!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160E")

    Jump("loc_1BF3")

    label("loc_1611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_16A4")

    ChrTalk(
        0xA,
        (
            "It's almost time for the\x01",
            "championship match to start.\x01",
            "Are you nervous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When you're ready, please\x01",
            "proceed to the entrance gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_16A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_179E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1707")

    ChrTalk(
        0xA,
        (
            "*giggle* It seems you've\x01",
            "amassed quite a following!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Good luck tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_179B")

    label("loc_1707")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        (
            "Well, you guys, tomorrow is\x01",
            "the final match! You nervous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*giggle* It seems you've\x01",
            "amassed quite a following!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Good luck tomorrow.\x02",
    )

    CloseMessageWindow()

    label("loc_179B")

    Jump("loc_1BF3")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_180E")
    TurnDirection(0xA, 0x108, 400)

    ChrTalk(
        0xA,
        "Zane, it's time for Round 2.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When you're ready, please\x01",
            "proceed to the entrance gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(
        0xA,
        (
            "Congratulations on clearing\x01",
            "Round 1!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tomorrow's match is in the\x01",
            "afternoon as well, so please\x01",
            "make sure you arrive early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(
        0xA,
        (
            "If you show your Registry\x01",
            "Card at the entrance, the\x01",
            "staff will show you in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That should cover everything.\x01",
            "Luck be with you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_192B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_19FB")

    ChrTalk(
        0xA,
        (
            "The first round of the \x01",
            "competition will begin\x01",
            "tomorrow afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There are no reserved seats, so please take\x01",
            "the first available seat you find, for the\x01",
            "convenience of the other patrons.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_19FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(
        0xA,
        (
            "The entrance to the arena is\x01",
            "directly to your left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Show your tickets at the gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_1ABE")

    ChrTalk(
        0xA,
        (
            "If you have your ticket, \x01",
            "please make your way to\x01",
            "the front entrance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1B4B")

    ChrTalk(
        0xA,
        (
            "There's still some time before\x01",
            "the match begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please feel free to wait in line\x01",
            "with the other spectators if you\x01",
            "wish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1B4B")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        "Welcome to the Grand Arena. \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's still some time before\x01",
            "the match begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please feel free to wait in line\x01",
            "with the other spectators if you\x01",
            "wish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF3")

    TalkEnd(0xA)
    Return()

    # Function_1_AF end

    def Function_2_1BF7(): pass

    label("Function_2_1BF7")

    TalkBegin(0xB)
    OP_8C(0xB, 270, 0)
    SetChrSubChip(0xB, 0)
    EventBegin(0x0)
    Fade(1500)

    def lambda_1C13():
        OP_6D(108230, 1250, 32820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C13)

    def lambda_1C2B():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C2B)
    SetChrPos(0x101, 107830, 1250, 33580, 90)
    SetChrPos(0x102, 107750, 1250, 32470, 90)
    OP_8C(0xB, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C7D")
    SetChrPos(0x108, 106450, 1250, 32450, 90)

    label("loc_1C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C9C")
    SetChrPos(0x104, 106450, 1250, 33600, 90)

    label("loc_1C9C")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3B")

    ChrTalk(
        0xB,
        (
            "Welcome, everyone, \x01",
            "to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please note that tournament participants\x01",
            "are asked to remain within the arena's\x01",
            "walls until the end of the day's matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Have you made all the necessary\x01",
            "preparations for a day of hot,\x01",
            "hot action?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Bring it on!]\x01",       # 0
            "[Not quite yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E15"),
        (1, "loc_1EB1"),
        (SWITCH_DEFAULT, "loc_1F38"),
    )


    label("loc_1E15")

    OP_A2(0x631)
    OP_28(0x49, 0x1, 0x4)

    ChrTalk(
        0xB,
        "Excellent, excellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your waiting room is the 'Blue\x01",
            "Team Room,' just inside the hall\x01",
            "on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Fight well!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x3F5)
    NewScene("ED6_DT01/T4136   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_1F38")

    label("loc_1EB1")


    ChrTalk(
        0xB,
        (
            "I understand. These things\x01",
            "take time, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And there IS still time before\x01",
            "the match begins...so try to\x01",
            "relax, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F38")

    label("loc_1F38")

    Jump("loc_2827")

    label("loc_1F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D7")

    ChrTalk(
        0xB,
        (
            "Master Zane! Welcome\x01",
            "to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please note that tournament participants\x01",
            "are asked to remain within the arena's\x01",
            "walls until the end of the day's matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Have you made all the necessary\x01",
            "preparations for a day of hot,\x01",
            "hot action?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Bring it on!]\x01",       # 0
            "[Not quite yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20B4"),
        (1, "loc_214D"),
        (SWITCH_DEFAULT, "loc_21D4"),
    )


    label("loc_20B4")

    OP_A2(0x623)
    OP_28(0x48, 0x1, 0x4)

    ChrTalk(
        0xB,
        "Excellent, excellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your waiting room is the 'Blue\x01",
            "Team Room,' just inside the hall\x01",
            "on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Fight well!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21D4")

    label("loc_214D")


    ChrTalk(
        0xB,
        (
            "I understand. These things\x01",
            "take time, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And there IS still time before\x01",
            "the match begins...so try to\x01",
            "relax, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_21D4")

    Jump("loc_2827")

    label("loc_21D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2482")

    ChrTalk(
        0xB,
        (
            "Your card, please... Ah, part\x01",
            "of the tournament, I see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please note that tournament participants\x01",
            "are asked to remain within the arena's\x01",
            "walls until the end of the day's matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Have you made all the necessary\x01",
            "preparations for a day of hot,\x01",
            "hot action?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Bring it on!]\x01",       # 0
            "[Not quite yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_235F"),
        (1, "loc_23F8"),
        (SWITCH_DEFAULT, "loc_247F"),
    )


    label("loc_235F")

    OP_A2(0x61B)
    OP_28(0x47, 0x1, 0x8)

    ChrTalk(
        0xB,
        "Excellent, excellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your waiting room is the 'Blue\x01",
            "Team Room,' just inside the hall\x01",
            "on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Fight well!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_247F")

    label("loc_23F8")


    ChrTalk(
        0xB,
        (
            "I understand. These things\x01",
            "take time, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And there IS still time before\x01",
            "the match begins...so try to\x01",
            "relax, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_247F")

    Jump("loc_2827")

    label("loc_2482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2576")

    ChrTalk(
        0xB,
        (
            "Currently at the arena\x01",
            "we're holding the royal\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you would like to\x01",
            "participate, you'll\x01",
            "need to register first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Registration is being handled\x01",
            "at the ticket counter on the\x01",
            "right-hand side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2827")

    label("loc_2576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2783")

    ChrTalk(
        0xB,
        (
            "Currently at the arena we're\x01",
            "holding the preliminary matches\x01",
            "of the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "May I see your tickets?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Show tickets]\x01",      # 0
            "[Don't show]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_266F"),
        (1, "loc_2733"),
        (SWITCH_DEFAULT, "loc_2780"),
    )


    label("loc_266F")

    OP_A2(0x60D)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "Grand Arena Tickets\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x36B, 2)

    ChrTalk(
        0xB,
        (
            "Thanks! Everything seems to be\x01",
            "in order. You may enter at your\x01",
            "discretion.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2780")

    label("loc_2733")


    ChrTalk(
        0xB,
        "Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This ticket is only usable\x01",
            "for today's matches...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_2780")

    Jump("loc_2827")

    label("loc_2783")


    ChrTalk(
        0xB,
        (
            "Currently at the arena we're\x01",
            "holding the preliminary matches\x01",
            "of the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "May I see your tickets?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Ticket sales are to the right.\x02",
    )

    CloseMessageWindow()

    label("loc_2827")

    EventEnd(0x0)
    TalkEnd(0xB)
    Return()

    # Function_2_1BF7 end

    def Function_3_282D(): pass

    label("Function_3_282D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_283A")
    Jump("loc_2A81")

    label("loc_283A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2844")
    Jump("loc_2A81")

    label("loc_2844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_284E")
    Jump("loc_2A81")

    label("loc_284E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2858")
    Jump("loc_2A81")

    label("loc_2858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2862")
    Jump("loc_2A81")

    label("loc_2862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_286C")
    Jump("loc_2A81")

    label("loc_286C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2876")
    Jump("loc_2A81")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_295A")

    ChrTalk(
        0xFE,
        (
            "#819FThis morning at work I got\x01",
            "all tangled up with group of\x01",
            "army guys. What a mess...\x02\x03",
            "All because the terrorists were posing as\x01",
            "Bracer Guild members! Hard to believe all\x01",
            "the backlash that stunt caused...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A63")

    label("loc_295A")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#810FThis morning I had to go out\x01",
            "near the Erbe Royal Villa\x01",
            "for work...\x02\x03",
            "#819FAnd as soon as they recognized\x01",
            "us as bracers, they were all\x01",
            "over us. It was terrible!\x02\x03",
            "Hard to believe all the backlash\x01",
            "those terrorists caused by posing\x01",
            "as Bracer Guild members.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A63")

    Jump("loc_2A81")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2A70")
    Jump("loc_2A81")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2A7A")
    Jump("loc_2A81")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2A81")

    label("loc_2A81")

    TalkEnd(0xFE)
    Return()

    # Function_3_282D end

    def Function_4_2A85(): pass

    label("Function_4_2A85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2A92")
    Jump("loc_2B7C")

    label("loc_2A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A9C")
    Jump("loc_2B7C")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2AA6")
    Jump("loc_2B7C")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2AB0")
    Jump("loc_2B7C")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2ABA")
    Jump("loc_2B7C")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2B4D")

    ChrTalk(
        0xFE,
        (
            "I want to get good seats for\x01",
            "my wife and I, so I'm camping\x01",
            "out at the front of the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm such a lovestruck son-of-a-gun...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2B57")
    Jump("loc_2B7C")

    label("loc_2B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B61")
    Jump("loc_2B7C")

    label("loc_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2B6B")
    Jump("loc_2B7C")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2B75")
    Jump("loc_2B7C")

    label("loc_2B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2B7C")

    label("loc_2B7C")

    TalkEnd(0xFE)
    Return()

    # Function_4_2A85 end

    def Function_5_2B80(): pass

    label("Function_5_2B80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2E64")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2C2D")

    ChrTalk(
        0xFE,
        (
            "The Erebonian embassy is just\x01",
            "up ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E61")

    label("loc_2C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D11")

    ChrTalk(
        0xFE,
        (
            "Leave it to the Queen's Birthday\x01",
            "Celebration to bring out all the\x01",
            "crazies, weirdos and heroes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And this is still just a small fraction\x01",
            "of the people you'll find in the Empire's\x01",
            "capital city. Crazy, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E61")

    label("loc_2D11")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Leave it to the Queen's Birthday\x01",
            "Celebration to bring out all the\x01",
            "crazies, weirdos and heroes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And this is still just a small fraction\x01",
            "of the people you'll find in the Empire's\x01",
            "capital city. Crazy, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just can't imagine so many people\x01",
            "milling about, every single day. How\x01",
            "can a city like that even function?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E61")

    Jump("loc_4085")

    label("loc_2E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2FCE")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2F0B")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCB")

    label("loc_2F0B")


    ChrTalk(
        0xFE,
        (
            "Seems all the other guardsmen\x01",
            "have withdrawn from the embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I haven't gotten any direct\x01",
            "orders to leave my post...so\x01",
            "here I shall stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That is my sworn duty, after all!\x02",
    )

    CloseMessageWindow()

    label("loc_2FCB")

    Jump("loc_4085")

    label("loc_2FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3122")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3075")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311F")

    label("loc_3075")


    ChrTalk(
        0xFE,
        (
            "I've been instructed to keep\x01",
            "Olivier from leaving the\x01",
            "embassy premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would probably refrain from\x01",
            "acting on his behalf, too...\x01",
            "at least for the time being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311F")

    Jump("loc_4085")

    label("loc_3122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3393")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_31C9")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3390")

    label("loc_31C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_327C")

    ChrTalk(
        0xFE,
        (
            "Mueller is the most recent\x01",
            "Imperial officer in residence\x01",
            "at the Erebonian embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's young, but he's a senior\x01",
            "officer with quite a bit of\x01",
            "rank and decorum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3390")

    label("loc_327C")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Mueller is the most recent\x01",
            "Imperial officer in residence\x01",
            "at the Erebonian embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's young, but he's a senior\x01",
            "officer with quite a bit of\x01",
            "rank and decorum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Olivier is, hopefully, behaving\x01",
            "himself at the embassy right now.\x01",
            "If he knows what's good for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3390")

    Jump("loc_4085")

    label("loc_3393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3612")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_343A")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360F")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_350F")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "Olivier, you know that no one is\x01",
            "covering for you and all these\x01",
            "little 'walks' of yours, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been ordered to report \x01",
            "you in the event of you doing\x01",
            "anything particularly asinine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360F")

    label("loc_350F")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "'Stepping out' again today,\x01",
            "are we, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Olivier, you know that no one is\x01",
            "covering for you and all these\x01",
            "little 'walks' of yours, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been ordered to report \x01",
            "you in the event of you doing\x01",
            "anything particularly asinine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360F")

    Jump("loc_4085")

    label("loc_3612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3776")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_36B9")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3773")

    label("loc_36B9")


    ChrTalk(
        0xFE,
        (
            "I wish they'd keep people like Olivier and\x01",
            "all those embassy folks under lock and key,\x01",
            "so we could all breathe a little easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How does he keep getting out,\x01",
            "anyway? Honestly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3773")

    Jump("loc_4085")

    label("loc_3776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_39C1")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_381D")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BE")

    label("loc_381D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38D8")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "Olivier, please try to stop\x01",
            "doing things we have to issue\x01",
            "formal apologies for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of the others at your \x01",
            "embassy at least TRY to be a\x01",
            "little conscientious...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BE")

    label("loc_38D8")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "'Stepping out' again today,\x01",
            "are we, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Olivier, please try to stop\x01",
            "doing things we have to issue\x01",
            "formal apologies for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of the others at your \x01",
            "embassy at least TRY to be a\x01",
            "little conscientious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BE")

    Jump("loc_4085")

    label("loc_39C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3B04")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3A68")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B01")

    label("loc_3A68")


    ChrTalk(
        0xFE,
        (
            "As a Royal Army private, being in\x01",
            "the Martial Arts Competition would\x01",
            "be a tremendous honor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only I were given the chance \x01",
            "to participate...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B01")

    Jump("loc_4085")

    label("loc_3B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3DD2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3BAB")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DCF")

    label("loc_3BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3C3B")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "Olivier... Please try to show\x01",
            "a little restraint out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sick of getting pulled into\x01",
            "your filth all the time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DCF")

    label("loc_3C3B")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "Olivier, are you headed\x01",
            "back to the embassy now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FHmph. Don't be absurd!\x02\x03",
            "Look around you, at these decorated\x01",
            "villas! These smiling visages! These\x01",
            "enticing...victuals!\x02\x03",
            "#030FIt would be a crime fouler\x01",
            "than murder were I not to go\x01",
            "and partake in the merriment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yes, well, please try to\x01",
            "show a little restraint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sick of getting pulled into\x01",
            "your filth all the time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DCF")

    Jump("loc_4085")

    label("loc_3DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3FEA")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3E79")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE7")

    label("loc_3E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F05")

    ChrTalk(
        0xFE,
        (
            "The people at the Erebonian\x01",
            "embassy are all very upscale,\x01",
            "upstanding people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With one...notable exception,\x01",
            "of course...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE7")

    label("loc_3F05")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "The people at the Erebonian\x01",
            "embassy are all very upscale,\x01",
            "upstanding people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With one...notable exception,\x01",
            "of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every time he goes and causes\x01",
            "trouble, the parties involved\x01",
            "all come complaining to ME.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE7")

    Jump("loc_4085")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4085")

    ChrTalk(
        0xFE,
        (
            "Just ahead is the Erebonian\x01",
            "embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The general public is prohibited\x01",
            "from passing beyond this point.\x01",
            "Official business only, I'm afraid!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4085")

    TalkEnd(0xFE)
    Return()

    # Function_5_2B80 end

    def Function_6_4089(): pass

    label("Function_6_4089")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4836")
    EventBegin(0x0)
    OP_69(0x23, 0x3E8)
    OP_A2(0x612)
    OP_28(0x46, 0x1, 0x8)
    OP_28(0x46, 0x1, 0x10)

    ChrTalk(
        0x23,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "What's your business here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWe're looking for a person\x01",
            "named Zane...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FMay we see him, please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Oh, you're here to see Zane,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Have you actually met the man?\x01",
            "First time I did, I almost peed\x01",
            "myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "I was like, holy crap! He\x01",
            "ain't a man, he's a grizzly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FHeh. He is a pretty big fella,\x01",
            "that's for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "But he's real friendly once\x01",
            "you start talking with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "He even gave me a meat-bun \x01",
            "when I told him I was hungry\x01",
            "during my shift one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FYeah, he's the kind of guy\x01",
            "you can really count on.\x01",
            "Like a big brother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F*ahem* Indeed.\x02\x03",
            "#010FSo, may we see him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "Oh, yes, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "He actually stepped out again shortly\x01",
            "after returning. Said he had some\x01",
            "business to take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Looking for a place to 'meditate and \x01",
            "prepare for the tournament,' or some\x01",
            "such thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FMeditate, huh? Man, he's\x01",
            "not kidding around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWhere do you think such a\x01",
            "place might be found?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Well, when he left here,\x01",
            "he was headed for the Erbe\x01",
            "Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "That old forest path has a feeling to it\x01",
            "not unlike a park...and it being monster-\x01",
            "infested makes it a good training ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThe Erbe Scenic Route? Okay,\x01",
            "got it. Come on, Estelle,\x01",
            "let's go find him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Hang on. If you're going to\x01",
            "the Erbe Scenic Route, there's\x01",
            "one thing you need to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "There's a place nearby called\x01",
            "the Erbe Royal Villa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FOh, we heard about that place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F...I assume you're going to tell us that\x01",
            "it's been commandeered for the anti-terror\x01",
            "division, so it's totally locked down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "...Good guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "They can raise quite a ruckus\x01",
            "over there. Watch your backs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Or better yet, just avoid it\x01",
            "altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FSo they're strict, huh? Strict\x01",
            "is starting to get real old...\x02\x03",
            "#501FAvoidance sounds good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThank you for the information.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_57CB")

    label("loc_4836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_498B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_48C5")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4988")

    label("loc_48C5")


    ChrTalk(
        0xFE,
        (
            "I swear, more people turn out\x01",
            "for the festivities every year.\x01",
            "It's crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In crowds like this I have to really\x01",
            "keep an eye out for mischief-makers,\x01",
            "and shake the fun-lovin' out of 'em.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4988")

    Jump("loc_57CB")

    label("loc_498B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AEE")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A1A")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEB")

    label("loc_4A1A")


    ChrTalk(
        0xFE,
        (
            "All of the regular troops have \x01",
            "been ordered out and replaced\x01",
            "with Special Ops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of them but me, that is. I'm staying\x01",
            "here until I'm directly ordered to with-\x01",
            "draw. Because that's what heroes do!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEB")

    Jump("loc_57CB")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4C4D")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4B7D")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C4A")

    label("loc_4B7D")


    ChrTalk(
        0xFE,
        (
            "What'll I be doing for the queen's\x01",
            "Birthday Celebration, you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sadly, I can't say. The ambassador can't\x01",
            "decide on his schedule, and until he does,\x01",
            "I've got to keep mine open as well. Le sigh!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C4A")

    Jump("loc_57CB")

    label("loc_4C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4EF4")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4CDC")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF1")

    label("loc_4CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D66")
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        "Congratulations, Zane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was rooting for you, but even\x01",
            "I couldn't have predicted you'd \x01",
            "end up winning it all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF1")

    label("loc_4D66")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        "Congratulations, Zane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was rooting for you, but even\x01",
            "I couldn't have predicted you'd \x01",
            "end up winning it all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've made us all very proud\x01",
            "here at the embassy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FThank you. I actually have\x01",
            "some news for the ambassador..\x02\x03",
            "Tonight I've been invited to\x01",
            "stay at the castle, so I won't\x01",
            "be back until tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll pass along the message.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Enjoy yourself!\x02",
    )

    CloseMessageWindow()

    label("loc_4EF1")

    Jump("loc_57CB")

    label("loc_4EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4FE2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4F83")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FDF")

    label("loc_4F83")


    ChrTalk(
        0xFE,
        "Final round today. At long last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe in you guys. Knock\x01",
            "'em dead out there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FDF")

    Jump("loc_57CB")

    label("loc_4FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5103")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5071")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5100")

    label("loc_5071")


    ChrTalk(
        0xFE,
        (
            "If I didn't have to work,\x01",
            "I'd've loved to participate\x01",
            "in the tournament with Zane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So you guys'll have to fight\x01",
            "extra hard...for me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5100")

    Jump("loc_57CB")

    label("loc_5103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5223")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5192")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5220")

    label("loc_5192")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        (
            "Zane, congratulations on \x01",
            "making it to day two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be cheering the loudest\x01",
            "for you, big guy, so show 'em\x01",
            "all what you got!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5220")

    Jump("loc_57CB")

    label("loc_5223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_537A")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_52B2")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5377")

    label("loc_52B2")


    ChrTalk(
        0xFE,
        (
            "Zane's such a lovable bear of\x01",
            "a man, he's become something of\x01",
            "an icon at the embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he's got one weakness, though,\x01",
            "its his chivalry. He kinda goes\x01",
            "a bit overboard with it sometimes!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5377")

    Jump("loc_57CB")

    label("loc_537A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_55C2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5409")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BF")

    label("loc_5409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_549D")
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        (
            "So, the tournament's finally\x01",
            "starting today, eh Zane?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't go watch, sadly, but\x01",
            "I'll be cheering you on from\x01",
            "my post!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BF")

    label("loc_549D")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        (
            "So, the tournament's finally\x01",
            "starting today, eh Zane?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't go watch, sadly, but\x01",
            "I'll be cheering you on from\x01",
            "my post!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FMuch obliged. With all the\x01",
            "helping hands I've got, I aim\x01",
            "to come out on top.\x02\x03",
            "But regardless of the outcome,\x01",
            "I shall fight without regret!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55BF")

    Jump("loc_57CB")

    label("loc_55C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5748")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5651")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5745")

    label("loc_5651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_END)), "loc_56C9")

    ChrTalk(
        0xFE,
        (
            "I think Zane went out to the\x01",
            "Erbe Scenic Route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you go, be careful to\x01",
            "avoid the Royal Villa!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5745")

    label("loc_56C9")


    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5745")

    Jump("loc_57CB")

    label("loc_5748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_57CB")

    ChrTalk(
        0xFE,
        (
            "This is the embassy for the \x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but only those who are here\x01",
            "on official business may enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CB")

    TalkEnd(0xFE)
    Return()

    # Function_6_4089 end

    def Function_7_57CF(): pass

    label("Function_7_57CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5828")

    ChrTalk(
        0xFE,
        (
            "Princess Klaudia looks\x01",
            "so beautiful today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish I could be her!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5895")

    ChrTalk(
        0xFE,
        (
            "Those soldiers in black sure\x01",
            "seem to be all over the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is there some kind of drill?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5920")

    ChrTalk(
        0xFE,
        (
            "Hurray! Now that the Martial\x01",
            "Arts Competition is over, the\x01",
            "birthday festivities can begin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's going to be super-fun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_59C9")

    ChrTalk(
        0xFE,
        (
            "I cheered so much, my throat's\x01",
            "all sore and bloody! Gross,\x01",
            "but AWESOME! ...Ow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The tournament is just SO exciting!\x01",
            "I can't wait for next year's now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_59C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5A4D")

    ChrTalk(
        0xFE,
        (
            "Yay! The final round! Who will\x01",
            "win, and who will lose? I don't\x01",
            "even really care-- just YAAAY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Violence is cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5AD8")

    ChrTalk(
        0xFE,
        (
            "Wow, I didn't think we'd see\x01",
            "a dark horse entry make it all\x01",
            "the way to the championship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can hardly believe my eyes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5B5E")

    ChrTalk(
        0xFE,
        (
            "No matter who's fighting whom, both matches\x01",
            "today are sure to be must-sees. Have I died\x01",
            "and gone to gladiator heaven?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5BAE")

    ChrTalk(
        0xFE,
        (
            "All the matches today have been\x01",
            "must-sees. It's so invigorating!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5C37")

    ChrTalk(
        0xFE,
        (
            "I'm going to cheer so hard my voice will\x01",
            "ride out on the hoarse it rode in on! Makes\x01",
            "no sense? I don't care! Just YAAAAY!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5CAD")

    ChrTalk(
        0xFE,
        (
            "After watching the prelims, I'm totally\x01",
            "thinking that team of bracers has this\x01",
            "competition in the bag!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5D23")

    ChrTalk(
        0xFE,
        (
            "So, let's see... Who should I cheer for\x01",
            "this year? Maybe I'll just cheer for\x01",
            "blood! Doesn't matter whose!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D23")

    TalkEnd(0xFE)
    Return()

    # Function_7_57CF end

    def Function_8_5D27(): pass

    label("Function_8_5D27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5D34")
    Jump("loc_62BC")

    label("loc_5D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5D3E")
    Jump("loc_62BC")

    label("loc_5D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5DC1")

    ChrTalk(
        0xFE,
        (
            "Ugh. I drank way too much\x01",
            "yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't even remember who\x01",
            "I was drinking with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooooh, my head...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_5DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5DCB")
    Jump("loc_62BC")

    label("loc_5DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5E9D")

    ChrTalk(
        0xFE,
        (
            "Look at all these people! I got up\x01",
            "early specifically to avoid the\x01",
            "crowds... Lot of good THAT did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These are the final match-ups,\x01",
            "though, so I guess I shouldn't\x01",
            "be surprised by the turnout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_5E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F3E")

    ChrTalk(
        0xFE,
        (
            "I don't think there were too\x01",
            "many people cheering for that\x01",
            "team of Sky Bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have to admit, though, they\x01",
            "put up a heck of a fight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6080")

    label("loc_5F3E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "I don't think there were too\x01",
            "many people cheering for that\x01",
            "team of Sky Bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Plenty of people cheering\x01",
            "AGAINST them, though, judging\x01",
            "by the din when they lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have to admit, though, they\x01",
            "put up a heck of a fight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here's hoping they rethink\x01",
            "their lives a bit, 'cause\x01",
            "they could really go places!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6080")

    Jump("loc_62BC")

    label("loc_6083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_60CF")

    ChrTalk(
        0xFE,
        "The finals continue today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder who'll make it...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_60CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6168")

    ChrTalk(
        0xFE,
        (
            "There's something...unsettling\x01",
            "about the Sky Bandit team\x01",
            "beating the Royal Army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really wanted to see them\x01",
            "get a little farther!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_6168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_61E7")

    ChrTalk(
        0xFE,
        "When's it gonna start, already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The real matches are always\x01",
            "so much more exciting than\x01",
            "the preliminaries!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_61E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_625F")

    ChrTalk(
        0xFE,
        (
            "Are they seriously doing\x01",
            "TEAM battles this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've always preferred one-on-\x01",
            "one matches, myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_625F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_62BC")

    ChrTalk(
        0xFE,
        (
            "If looks like they changed\x01",
            "around a lot of the rules\x01",
            "this year, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BC")

    TalkEnd(0xFE)
    Return()

    # Function_8_5D27 end

    def Function_9_62C0(): pass

    label("Function_9_62C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_62CD")
    Jump("loc_6946")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_62D7")
    Jump("loc_6946")

    label("loc_62D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_62E1")
    Jump("loc_6946")

    label("loc_62E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_62EB")
    Jump("loc_6946")

    label("loc_62EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6420")

    ChrTalk(
        0xFE,
        "That tears it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm cheering for that big\x01",
            "guy from the Republic, Zane!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Though that Special Ops\x01",
            "team is nothing to sneeze\x01",
            "at, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or maybe the bracers, as a team, have what\x01",
            "it takes. I'm just not sure! Maybe I'll just\x01",
            "cheer for the Specia...racer...ane! Yeah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_652D")

    label("loc_6420")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "Hmm... Who shall I cheer for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that whoever I end\x01",
            "up cheering for always loses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, maybe I should cheer for\x01",
            "the team I DON'T want to win!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good ol' reverse psychology... You\x01",
            "haven't failed me yet! Er...I mean,\x01",
            "you have! You TOTALLY have!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_652D")

    Jump("loc_6946")

    label("loc_6530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_659C")

    ChrTalk(
        0xFE,
        (
            "Aww, man! The team I was\x01",
            "cheering for lost again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must be cursed or something!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6653")

    label("loc_659C")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Aww, man! The team I was\x01",
            "cheering for lost again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must be cursed or something!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...There sure are a lot of\x01",
            "soldiers walking the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()

    label("loc_6653")

    Jump("loc_6946")

    label("loc_6656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_673F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_66A8")

    ChrTalk(
        0xFE,
        (
            "Today I'm going to cheer for\x01",
            "that bracer team from Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673C")

    label("loc_66A8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Today I'm going to cheer for\x01",
            "that bracer team from Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I keep betting on losers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But today'll be different!\x01",
            "I can feel it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_673C")

    Jump("loc_6946")

    label("loc_673F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_678A")

    ChrTalk(
        0xFE,
        "Awww, the Ravens lost, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All my teams are losing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6946")

    label("loc_678A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6875")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_67EA")

    ChrTalk(
        0xFE,
        (
            "The tournament is so much\x01",
            "more exciting when you pick\x01",
            "a team to root for!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6872")

    label("loc_67EA")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "When I was younger I acted like\x01",
            "a big-shot punk all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So maybe I'll cheer for the \x01",
            "Ravens...or that nameless\x01",
            "team.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6872")

    Jump("loc_6946")

    label("loc_6875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_68FB")

    ChrTalk(
        0xFE,
        (
            "The border garrison team I'd \x01",
            "been cheering for lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe General\x01",
            "Morgan's not participating\x01",
            "in this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6946")

    label("loc_68FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6946")

    ChrTalk(
        0xFE,
        (
            "The border garrison team is\x01",
            "totally gonna win again\x01",
            "this year!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6946")

    TalkEnd(0xFE)
    Return()

    # Function_9_62C0 end

    def Function_10_694A(): pass

    label("Function_10_694A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_698D")

    ChrTalk(
        0xFE,
        (
            "I wonder what it's like to live\x01",
            "in the castle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_698D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6997")
    Jump("loc_6D53")

    label("loc_6997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_69A1")
    Jump("loc_6D53")

    label("loc_69A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_69AB")
    Jump("loc_6D53")

    label("loc_69AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6A64")

    ChrTalk(
        0xFE,
        (
            "I keep thinking about all\x01",
            "the different teams...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "And I've decided that, in the\x01",
            "end, I'm just going to cheer\x01",
            "for Joshua! My one and only!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6AFB")

    ChrTalk(
        0xFE,
        (
            "That silky black hair and cool\x01",
            "gaze of his... It totally melts\x01",
            "my heart! He's simply DARLING!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want to hug him tight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B9D")

    label("loc_6AFB")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "Isn't that black-haired boy\x01",
            "out there amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's cute, but he has this\x01",
            "cool composure about him too,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want to hug him tight!\x02",
    )

    CloseMessageWindow()

    label("loc_6B9D")

    Jump("loc_6D53")

    label("loc_6BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6BDD")

    ChrTalk(
        0xFE,
        (
            "Yeah, this is all that \x01",
            "DUKE's fault, I hear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6C0C")

    ChrTalk(
        0xFE,
        "Yeah, Red Mask Man is DREAMY...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6C56")

    ChrTalk(
        0xFE,
        (
            "Wow, those guys in the black\x01",
            "armor look pretty tough, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6CDC")

    ChrTalk(
        0xFE,
        (
            "That Zane guy looks like an\x01",
            "immovable iron weight out\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's fighting alone? What a\x01",
            "hulking specimen of man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6D53")

    ChrTalk(
        0xFE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen aren't fighting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to see Lieutenant\x01",
            "Schwarz do her thing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D53")

    TalkEnd(0xFE)
    Return()

    # Function_10_694A end

    def Function_11_6D57(): pass

    label("Function_11_6D57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6DB1")

    ChrTalk(
        0xFE,
        "I dunno...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumors might be rumors, but\x01",
            "it still sounds good to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6DBB")
    Jump("loc_70EE")

    label("loc_6DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6DC5")
    Jump("loc_70EE")

    label("loc_6DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6DCF")
    Jump("loc_70EE")

    label("loc_6DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6E15")

    ChrTalk(
        0xFE,
        (
            "What? Why are you going to \x01",
            "cheer for just one person?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6ED8")

    ChrTalk(
        0xFE,
        (
            "Isn't Phoebe just AWFUL? I guess I'm \x01",
            "not one to talk, though, as I feel the\x01",
            "same way about that black-haired boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That boy seriously looks like\x01",
            "he needs some of mama's love.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6F1D")

    ChrTalk(
        0xFE,
        (
            "But, aren't those Sky Bandit\x01",
            "guys just the creepiest?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6FB2")

    ChrTalk(
        0xFE,
        (
            "That guy in the red mask? \x01",
            "Doesn't he just have the\x01",
            "SEXIEST set of lips?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "His arms aren't bad either.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7038")

    ChrTalk(
        0xFE,
        (
            "Yeah, those Royal Special...\x01",
            "Army Ops dudes, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That matching black on black is\x01",
            "SO not doing them any favors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_7038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_70B2")

    ChrTalk(
        0xFE,
        (
            "I guess he looks ripped \x01",
            "enough, but he's...\x01",
            "He's OLD!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You gotta have the look\x01",
            "to go with the skills.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_70B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_70EE")

    ChrTalk(
        0xFE,
        (
            "Why did I even bother buying\x01",
            "an advance ticket?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70EE")

    TalkEnd(0xFE)
    Return()

    # Function_11_6D57 end

    def Function_12_70F2(): pass

    label("Function_12_70F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_715A")

    ChrTalk(
        0xFE,
        (
            "Everyone looks like they're\x01",
            "having so much fun at the\x01",
            "Queen's Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_715A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_71BD")

    ChrTalk(
        0xFE,
        (
            "Ricky acts like such a slacker\x01",
            "sometimes. Doesn't he have\x01",
            "any kind of drive at all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_71BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7241")

    ChrTalk(
        0xFE,
        (
            "Someone like Ricky would never\x01",
            "be able to understand the passion\x01",
            "that wells deep within me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Somebody save me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_73F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_73BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7297")

    ChrTalk(
        0xFE,
        (
            "He's going to sap all the \x01",
            "motivation out of me again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73BC")

    label("loc_7297")


    ChrTalk(
        0xFE,
        (
            "I just tried talking \x01",
            "to that pretty girl who \x01",
            "kept walking by here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You know what she said?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She told me that 'a leering\x01",
            "scumbag like me would never\x01",
            "stand a chance' with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was like, wow. You could\x01",
            "have just said no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just want to go curl up\x01",
            "somewhere and die...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BC")

    Jump("loc_73F5")

    label("loc_73BF")


    ChrTalk(
        0xFE,
        "Ugh. Another uneventful day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My life sucks.\x02",
    )

    CloseMessageWindow()

    label("loc_73F5")

    Jump("loc_7E57")

    label("loc_73F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_7443")

    ChrTalk(
        0xFE,
        (
            "All right, I am so going to\x01",
            "talk to that lady today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_7443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_75B7")
    OP_A2(0x6EB)

    ChrTalk(
        0xFE,
        (
            "YES! That makes three! I've\x01",
            "seen her three times now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I need to\x01",
            "thank someone upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you! Thank you Goddess!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you too, you guys!\x01",
            "Here, take this! As a token\x01",
            "of my appreciation!\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x21C, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Carnelia - Finale\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "All right! Time to man up\x01",
            "and say something to her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_75B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_766E")

    ChrTalk(
        0xFE,
        "One more time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I see that girl one more\x01",
            "time, I'll say hello to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's like a goddess to me...\x01",
            "celestial and untenable, but\x01",
            "captivating in her beauty!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_766E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7775")

    ChrTalk(
        0xFE,
        (
            "Heh heh, that girl just\x01",
            "walked by here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Two more times...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that girl walks by \x01",
            "here two more times, it \x01",
            "means she's the one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, what if she doesn't\x01",
            "walk by again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, man...will she? Won't she?\x01",
            "Will she? Won't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_7775")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "There's this beautiful girl\x01",
            "who walks by here all the\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some days, counting how many times I see her\x01",
            "is the only way I can keep myself sane...\x01",
            "IF YOU CAN CALL THAT SANE. Ha...haha...ha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that girl walks by here\x01",
            "three times today, I'm going\x01",
            "to go up to her and say hi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I just need that book, so I can pretend to be\x01",
            "reading it while I wait for her...because girls\x01",
            "like smart, bookish men, right? RIGHT? RIIIGHT?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7943")

    Jump("loc_7E57")

    label("loc_7946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7A05")

    ChrTalk(
        0xFE,
        (
            "Everyplace I go around here, they're\x01",
            "all caught up in the festival, and no\x01",
            "one's even thinking about hiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's a sign from above\x01",
            "telling me not to work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B06")

    label("loc_7A05")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "And I went to all the trouble of\x01",
            "coming out here to search for a\x01",
            "job, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyplace I go around here, they're\x01",
            "all caught up in the festival, and no\x01",
            "one's even thinking about hiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's a sign from above\x01",
            "telling me not to work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B06")

    Jump("loc_7E57")

    label("loc_7B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7B57")

    ChrTalk(
        0xFE,
        (
            "I don't get how Ricky can\x01",
            "be so laid-back all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE7")

    label("loc_7B57")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "I've been feeling oddly\x01",
            "motivated these last couple\x01",
            "of days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a matter of fact, I'm about\x01",
            "to go out and start looking\x01",
            "for a job!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE7")

    Jump("loc_7E57")

    label("loc_7BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7C8B")

    ChrTalk(
        0xFE,
        (
            "Another day of doing nothing,\x01",
            "gone like dust in the wind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know everything'll change\x01",
            "if I can just find a good\x01",
            "job...but where do I look?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7D05")

    ChrTalk(
        0xFE,
        (
            "*sigh* Another day of doing\x01",
            "nothing at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate I'm never going\x01",
            "to go anywhere with my life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7DB1")

    ChrTalk(
        0xFE,
        (
            "Aaaaand, there's another day\x01",
            "of my life completely wasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just don't want to DO anything\x01",
            "anymore... All I want to do is\x01",
            "stay home and waste my time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7E57")

    ChrTalk(
        0xFE,
        (
            "At least if I had a girlfriend,\x01",
            "I might go to the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...There's this beautiful girl\x01",
            "who comes by here all the time. \x01",
            "She's totally my type.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E57")

    TalkEnd(0xFE)
    Return()

    # Function_12_70F2 end

    def Function_13_7E5B(): pass

    label("Function_13_7E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7EE9")

    ChrTalk(
        0xFE,
        "Whoa, sure is busy out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't look like I'll get that\x01",
            "nap I've been wanting; may as\x01",
            "well just hang out instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_7EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7F65")

    ChrTalk(
        0xFE,
        "What do I want to do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well...I guess it'd be cool \x01",
            "to have a nap in Grancel\x01",
            "Castle's Garden Terrace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_7F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7FDD")

    ChrTalk(
        0xFE,
        (
            "Right now, Anton's not talking\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, we all go through patches\x01",
            "like this sometimes, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_7FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_803D")

    ChrTalk(
        0xFE,
        (
            "...Watching Anton over there\x01",
            "never gets old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hm... What to do now...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8074")

    label("loc_803D")


    ChrTalk(
        0xFE,
        (
            "Man, I'm good with just not\x01",
            "doing ANYTHING today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8074")

    Jump("loc_84A7")

    label("loc_8077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_81B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_80F6")

    ChrTalk(
        0xFE,
        (
            "I think Anton's a pretty happy\x01",
            "guy, sort of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't figure out what's got\x01",
            "him so stoked, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B6")

    label("loc_80F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_813D")

    ChrTalk(
        0xFE,
        (
            "Anton gets some weird ideas\x01",
            "in his head sometimes, man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B6")

    label("loc_813D")


    ChrTalk(
        0xFE,
        (
            "The final round of the tournament?\x01",
            "Was that today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all good to me, man. I'll\x01",
            "just be hanging out here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81B6")

    Jump("loc_84A7")

    label("loc_81B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_824C")

    ChrTalk(
        0xFE,
        (
            "Anton's starting up his old\x01",
            "habits again, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He says he's looking for work...\x01",
            "but what he's actually looking\x01",
            "for is HIMSELF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_824C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_827F")

    ChrTalk(
        0xFE,
        "Maaaaan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nice weather today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_827F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8307")

    ChrTalk(
        0xFE,
        (
            "My buddy's got something\x01",
            "on his mind again, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he ain't gonna find\x01",
            "purpose in life just\x01",
            "by scoring some work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_8307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_83B6")

    ChrTalk(
        0xFE,
        (
            "Man, Anton's got himself all\x01",
            "worked up over something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he's got something on his mind,\x01",
            "he should take action, rather than\x01",
            "just stewing over it all day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_83B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8405")

    ChrTalk(
        0xFE,
        (
            "Better go get some food before\x01",
            "it gets too crowded around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_8405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_84A7")

    ChrTalk(
        0xFE,
        (
            "Man, I ain't interested in\x01",
            "the tournament. Not at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that stuff just happens,\x01",
            "man. It happens and it ends.\x01",
            "And the world keeps on turnin'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84A7")

    TalkEnd(0xFE)
    Return()

    # Function_13_7E5B end

    def Function_14_84AB(): pass

    label("Function_14_84AB")

    TalkBegin(0xFE)
    OP_A3(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_84BB")
    Jump("loc_8537")

    label("loc_84BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_84C8")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_84D5")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_84E2")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_84EF")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_84FC")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8506")
    Jump("loc_8537")

    label("loc_8506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8513")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_8513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8520")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_8520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_852D")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_852D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8537")
    OP_A2(0x19)

    label("loc_8537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_85AC")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859B")
    OP_0D()
    OP_A9(0x74)
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_859B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85AC")
    TalkEnd(0xFE)
    Return()

    label("loc_85AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_85F3")

    ChrTalk(
        0xFE,
        (
            "Busy, busy, busy! Just as I\x01",
            "assumed it would be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8646")

    label("loc_85F3")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "One double chocolate mint,\x01",
            "coming right up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you very much!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_8646")

    Jump("loc_8E23")

    label("loc_8649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_86A9")

    ChrTalk(
        0xFE,
        (
            "All these soldiers sure seem\x01",
            "busy with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_86A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_870A")

    ChrTalk(
        0xFE,
        (
            "What ever happened to those\x01",
            "Royal Guardsmen people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have you heard anything?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_870A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_88F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_87E9")

    ChrTalk(
        0xFE,
        (
            "Today's special is our \x01",
            "chocolate, strawberry, mint\x01",
            "and lemon sundae.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Each scoop represents one of our champions:\x01",
            "Zane is chocolate, Estelle is strawberry,\x01",
            "Joshua is mint...and Olivier's a lemon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88F3")

    label("loc_87E9")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "Hello! Would you like to\x01",
            "try our special sundae?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's one scoop each of \x01",
            "chocolate, strawberry, mint\x01",
            "and lemon ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Each scoop represents one of our champions:\x01",
            "Zane is chocolate, Estelle is strawberry,\x01",
            "Joshua is mint...and Olivier's a lemon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88F3")

    Jump("loc_8E23")

    label("loc_88F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_898A")

    ChrTalk(
        0xFE,
        "Welcome! Step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, after the final match,\x01",
            "I'll be selling my special \x01",
            "championship sundae!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come buy one later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_898A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_89EF")

    ChrTalk(
        0xFE,
        "So, tomorrow's the championship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm already planning a \x01",
            "special edition sundae.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_89EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8A87")

    ChrTalk(
        0xFE,
        (
            "During the tournament and the\x01",
            "Birthday Celebration, we're \x01",
            "running a special discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Deal of a lifetime, so don't\x01",
            "miss it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B2E")

    label("loc_8A87")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "Welcome! Step right up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During the tournament and the\x01",
            "Birthday Celebration, we're \x01",
            "running a special discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Deal of a lifetime, so don't\x01",
            "miss it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B2E")

    Jump("loc_8E23")

    label("loc_8B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8BB3")

    ChrTalk(
        0xFE,
        (
            "My store doesn't have tons\x01",
            "of flavors, but they're\x01",
            "all home-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Step on up and try one out for size!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C40")

    label("loc_8BB3")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "Coooome and get it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My store doesn't have tons\x01",
            "of flavors, but they're\x01",
            "all home-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Step on up and try one out for size!\x02",
    )

    CloseMessageWindow()

    label("loc_8C40")

    Jump("loc_8E23")

    label("loc_8C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8D5D")

    ChrTalk(
        0xFE,
        (
            "I hear the nobles associated with the royal\x01",
            "family are fans of my ice cream...but it's\x01",
            "probably just a rumor. Although...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*giggle* Nobles are always sneaking into town\x01",
            "incognito, and if Princess Klaudia has done the\x01",
            "same, maybe she's tried some of my ice cream!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_8D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8DCA")

    ChrTalk(
        0xFE,
        (
            "You look tired from \x01",
            "all that cheering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know what'll freshen\x01",
            "you up? Some ice cream!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_8DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8E23")

    ChrTalk(
        0xFE,
        "Coooome and get it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who wants some cold and\x01",
            "creamy home-made ice cream?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E23")

    TalkEnd(0xFE)
    Return()

    # Function_14_84AB end

    def Function_15_8E27(): pass

    label("Function_15_8E27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8EE2")

    ChrTalk(
        0xFE,
        (
            "Working from home means,\x01",
            "ironically enough, I can't \x01",
            "spend time with my kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, she seems to understand.\x01",
            "And it's not like I can't make\x01",
            "time, if the need arises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_8EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8F8E")

    ChrTalk(
        0xFE,
        (
            "We're here in the capital for the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'm worried about being so\x01",
            "far from home, with the airships\x01",
            "being held up so often.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_8F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8FB9")

    ChrTalk(
        0xFE,
        "Boys are so full of energy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_8FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9060")

    ChrTalk(
        0xFE,
        (
            "This woman is an attendant\x01",
            "for one of the airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're both working mothers, so\x01",
            "we hit it off pretty quickly,\x01",
            "comparing 'war stories' and such.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_9060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_90EC")

    ChrTalk(
        0xFE,
        (
            "The ice cream they sell\x01",
            "here is really good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll bet it's probably one \x01",
            "of the more famous stores\x01",
            "here in the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_90EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_90F6")
    Jump("loc_9125")

    label("loc_90F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9100")
    Jump("loc_9125")

    label("loc_9100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_910A")
    Jump("loc_9125")

    label("loc_910A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9114")
    Jump("loc_9125")

    label("loc_9114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_911E")
    Jump("loc_9125")

    label("loc_911E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9125")

    label("loc_9125")

    TalkEnd(0xFE)
    Return()

    # Function_15_8E27 end

    def Function_16_9129(): pass

    label("Function_16_9129")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9190")

    ChrTalk(
        0xFE,
        (
            "Mommy said she'd buy me more\x01",
            "ice cream if I would leave\x01",
            "her alone to talk some more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_9190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_91B6")

    ChrTalk(
        0xFE,
        "I want more ice cream!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_91B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_925B")

    ChrTalk(
        0xFE,
        (
            "I come from a village by the\x01",
            "sea, where there are lots and\x01",
            "lots of pretty white flowers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And my best friend Polly and\x01",
            "all my friends live there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_925B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_92AD")

    ChrTalk(
        0xFE,
        "I want to go see the castle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But they said I'm not allowed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_92AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_92E9")

    ChrTalk(
        0xFE,
        "I love ice cream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mommy bought me some.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_92E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_92F3")
    Jump("loc_9322")

    label("loc_92F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_92FD")
    Jump("loc_9322")

    label("loc_92FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9307")
    Jump("loc_9322")

    label("loc_9307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9311")
    Jump("loc_9322")

    label("loc_9311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_931B")
    Jump("loc_9322")

    label("loc_931B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9322")

    label("loc_9322")

    TalkEnd(0xFE)
    Return()

    # Function_16_9129 end

    def Function_17_9326(): pass

    label("Function_17_9326")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_956A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_941F")

    ChrTalk(
        0xFE,
        (
            "I didn't have work today, so\x01",
            "I got to play with my kid and\x01",
            "meet some lovely new people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's sad, though, is I keep thinking about\x01",
            "work. I figured this would be a much-needed\x01",
            "break, but I just can't get away from it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9567")

    label("loc_941F")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "I've got to catch a flight\x01",
            "on the next Cecilia. Off-duty,\x01",
            "of course-- the ONLY way to fly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't have work today, so\x01",
            "I got to play with my kid and\x01",
            "meet some lovely new people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's sad, though, is I keep thinking about\x01",
            "work. I figured this would be a much-needed\x01",
            "break, but I just can't get away from it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9567")

    Jump("loc_9E20")

    label("loc_956A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9633")

    ChrTalk(
        0xFE,
        (
            "I was supposed to work today,\x01",
            "but the boarding platform\x01",
            "was closed and locked down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might be an anti-terrorist\x01",
            "thing... I have no idea. There's\x01",
            "just been so much of that lately!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_9633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_967E")

    ChrTalk(
        0xFE,
        (
            "Seeing Carla's daughter makes\x01",
            "me really want one of my own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_967E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_97CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9700")

    ChrTalk(
        0xFE,
        (
            "This woman here works at\x01",
            "an inn, with her husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sounds like harder work\x01",
            "than you might expect...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97C9")

    label("loc_9700")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "When your kids become friends,\x01",
            "you wind up becoming friends\x01",
            "with their parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This woman here works at\x01",
            "an inn, with her husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sounds like harder work\x01",
            "than you might expect...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97C9")

    Jump("loc_9E20")

    label("loc_97CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_98A6")

    ChrTalk(
        0xFE,
        (
            "This ice cream is pretty\x01",
            "popular throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a big rumor that Princess Klaudia snuck\x01",
            "here and ate some, and then her attendants came\x01",
            "to get her, and made a whole scene out of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_98A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9939")

    ChrTalk(
        0xFE,
        (
            "Before we go home I think \x01",
            "we'll stop in the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could use a rest; it's been\x01",
            "a while since I played that\x01",
            "long with my kid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_9939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_99A4")

    ChrTalk(
        0xFE,
        (
            "He's just crazy about the\x01",
            "Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boys will be boys, though...right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_99A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9A75")

    ChrTalk(
        0xFE,
        (
            "Sure was a shocker, I must admit...\x01",
            "To think the Sky Bandits who kid-\x01",
            "napped us were out in the arena!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it was a good show\x01",
            "for everyone else, but it\x01",
            "made me...uncomfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7A")

    label("loc_9A75")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Sure was a shocker, I must admit... Why\x01",
            "would the Sky Bandits who kidnapped us be\x01",
            "allowed to fight in the competition?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What in the world was Duke\x01",
            "Dunan thinking?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it was a good show\x01",
            "for everyone else, but it\x01",
            "made me...uncomfortable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B7A")

    Jump("loc_9E20")

    label("loc_9B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9BFC")

    ChrTalk(
        0xFE,
        (
            "We're going to the tournament\x01",
            "today, but only because my\x01",
            "boy begged me to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope I'm not spoiling him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_9BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_9D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9C8A")

    ChrTalk(
        0xFE,
        (
            "People are coming from all \x01",
            "over to see the tournament; \x01",
            "the airships must be packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope the company's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D64")

    label("loc_9C8A")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "People are coming from all \x01",
            "over to see the tournament; \x01",
            "the airships must be packed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Getting a vacation at times like\x01",
            "this is almost more of a hassle\x01",
            "than anything else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope the company's okay...\x02",
    )

    CloseMessageWindow()

    label("loc_9D64")

    Jump("loc_9E20")

    label("loc_9D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9E20")

    ChrTalk(
        0xFE,
        (
            "Since I was locked up during the Sky\x01",
            "Bandit incident, the company gave me\x01",
            "a long paid vacation as compensation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm grateful to be able to spend\x01",
            "this time with my son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E20")

    TalkEnd(0xFE)
    Return()

    # Function_17_9326 end

    def Function_18_9E24(): pass

    label("Function_18_9E24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9E76")

    ChrTalk(
        0xFE,
        "This ice cream is the best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mint chocolate is my favorite.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9EA1")

    ChrTalk(
        0xFE,
        "How long is Mom gonna talk?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9ECD")

    ChrTalk(
        0xFE,
        "I wanna go to Lucia's house!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9F1C")

    ChrTalk(
        0xFE,
        (
            "Heh, you know what? I've been\x01",
            "inside the castle before! Really!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_9F66")

    ChrTalk(
        0xFE,
        "Ice cream?! Luuucky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That ice cream is really good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9FA6")

    ChrTalk(
        0xFE,
        "Mom sure gets tired quick!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's so lazy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9FD4")

    ChrTalk(
        0xFE,
        "I'm going to watch the fights!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A038")

    ChrTalk(
        0xFE,
        "That fight was AWESOME!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was so surprised, I jumped\x01",
            "THIS high out of my chair!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_A038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A07B")

    ChrTalk(
        0xFE,
        (
            "I get to go and see the fights\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Jealous?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_A07B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A0DD")

    ChrTalk(
        0xFE,
        "Mom is always on the airships.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I grow up, I wanna \x01",
            "work on airships too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_A0DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A11D")

    ChrTalk(
        0xFE,
        (
            "Today Mom said she's gonna\x01",
            "play with me aaaall day!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A11D")

    TalkEnd(0xFE)
    Return()

    # Function_18_9E24 end

    def Function_19_A121(): pass

    label("Function_19_A121")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_A18E")

    ChrTalk(
        0xFE,
        (
            "I trusted them. I was so sure\x01",
            "the Royal Guardsmen would \x01",
            "never betray Her Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A242")

    label("loc_A18E")

    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "I trusted them. I was so sure\x01",
            "the Royal Guardsmen would \x01",
            "never betray Her Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And then Colonel Richard \x01",
            "staged a coup d'etat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just don't understand it.\x02",
    )

    CloseMessageWindow()

    label("loc_A242")

    Jump("loc_A877")

    label("loc_A245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A2AD")

    ChrTalk(
        0xFE,
        (
            "The Royal Garrison have all\x01",
            "pulled back in a real hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That does not bode well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A35D")

    ChrTalk(
        0xFE,
        (
            "The Birthday Celebration is only\x01",
            "a few days away, but there's been\x01",
            "no word from the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how the Royal Guard's\x01",
            "investigation is coming along...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A41B")

    ChrTalk(
        0xFE,
        (
            "I assumed Colonel Richard and Lt.\x01",
            "Schwarz working together meant that\x01",
            "we'd be safe, pretty much forevermore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But...I never thought they'd be \x01",
            "working together like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A4D1")

    ChrTalk(
        0xFE,
        (
            "I don't care that those Special Ops guys are\x01",
            "Colonel Richard's troops. I don't trust them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That we would even HAVE \x01",
            "stormtroopers like that,\x01",
            "serving in Liberl...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A565")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, 1st Lt.\x01",
            "Schwarz was always a very\x01",
            "devout member of the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw her there numerous times\x01",
            "during mass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A60A")

    ChrTalk(
        0xFE,
        (
            "You used to see 1st Lt. Schwarz\x01",
            "patrolling this area quite\x01",
            "often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was so friendly. She even\x01",
            "made small talk, asking about\x01",
            "my sore back once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A69E")

    ChrTalk(
        0xFE,
        (
            "The Arseille is being held\x01",
            "in port by the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the Royal Guard are still\x01",
            "showing up in Zeiss, and\x01",
            "attacking the capital...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A758")

    ChrTalk(
        0xFE,
        (
            "The Royal Guard used to be\x01",
            "quite popular with the common\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every year, they'd participate in the\x01",
            "Martial Arts Competition, and the\x01",
            "Birthday Celebration as well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A82A")

    ChrTalk(
        0xFE,
        (
            "The terrorists' actions are all the\x01",
            "more shocking when you consider the\x01",
            "season. It's the queen's birthday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You would think that they'd\x01",
            "show at least some respect,\x01",
            "even if they're rebelling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A877")

    ChrTalk(
        0xFE,
        "Oh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you here to watch the\x01",
            "Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A877")

    TalkEnd(0xFE)
    Return()

    # Function_19_A121 end

    def Function_20_A87B(): pass

    label("Function_20_A87B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A90F")

    ChrTalk(
        0xFE,
        (
            "The queen imprisoned, the\x01",
            "princess kidnapped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care about the ends;\x01",
            "the means Colonel Richard \x01",
            "used are disgusting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_A90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A9B5")

    ChrTalk(
        0xFE,
        (
            "I'm supposed to be shopping,\x01",
            "but something feels...off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's too quiet, even with all\x01",
            "these people around. And all \x01",
            "these guards make me nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_A9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_AA2C")

    ChrTalk(
        0xFE,
        (
            "The castle is still closed\x01",
            "to visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel bad for the people who\x01",
            "came all this way to see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AA2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_AAED")

    ChrTalk(
        0xFE,
        (
            "Hey, aren't you the guys who\x01",
            "won the championship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Congratulations! That was an\x01",
            "absolutely incredible match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm so glad you won it instead\x01",
            "of that Special Ops team...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AAED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_AE50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_AB4E")

    ChrTalk(
        0xFE,
        (
            "Standing around all day,\x01",
            "ogling people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's just rude, you know?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_AB4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_ABA8")

    ChrTalk(
        0xFE,
        (
            "Standing around all day,\x01",
            "ogling people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's just rude, you know?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_ABA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_ACC5")
    OP_63(0x31)

    ChrTalk(
        0xFE,
        (
            "That guy over there is staring\x01",
            "at me. I can feel his eyes on\x01",
            "me, all the time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just so creepy... I don't\x01",
            "want to get anywhere near him!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x31, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, are you bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a relief! I feel a lot\x01",
            "safer with bracers around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x15)
    OP_4B(0x31, 255)
    Jump("loc_AE4D")

    label("loc_ACC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AD53")

    ChrTalk(
        0xFE,
        (
            "I saw that guy over there\x01",
            "looking at me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*shudder* Maybe I'll find \x01",
            "another route to take for\x01",
            "running my errands...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_AD53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_ADE1")

    ChrTalk(
        0xFE,
        (
            "That guy standing in front of\x01",
            "the market has been staring at\x01",
            "me for quite some time now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Makes me VERY uncomfortable...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_ADE1")


    ChrTalk(
        0xFE,
        (
            "All these soldiers showed\x01",
            "up in town yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if they found those\x01",
            "Royal Guardsmen yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE4D")

    Jump("loc_B02C")

    label("loc_AE50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_AEE8")

    ChrTalk(
        0xFE,
        (
            "The Royal Guardsmen were chased\x01",
            "out of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll just bet it was because\x01",
            "Duke Dunan was getting jealous\x01",
            "of their popularity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AEE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AF40")

    ChrTalk(
        0xFE,
        "Mmmm... What a nice morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sun feels so wonderful\x01",
            "on my skin!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AF40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AF76")

    ChrTalk(
        0xFE,
        (
            "I wonder how the day's matches\x01",
            "went...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AF76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_AF9A")

    ChrTalk(
        0xFE,
        "Today's the big day!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AF9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_AFD2")

    ChrTalk(
        0xFE,
        (
            "The city sure is full of life\x01",
            "today, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AFD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B02C")

    ChrTalk(
        0xFE,
        (
            "There's this ice cream shop\x01",
            "here in the East Block that\x01",
            "is simply to DIE for!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B02C")

    TalkEnd(0xFE)
    Return()

    # Function_20_A87B end

    def Function_21_B030(): pass

    label("Function_21_B030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B078")

    ChrTalk(
        0xFE,
        (
            "I was so happy to finally\x01",
            "see the queen's face again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B0E1")

    ChrTalk(
        0xFE,
        (
            "Haven't seen the usual soldiers\x01",
            "around lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did something happen at the\x01",
            "castle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B0E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B182")

    ChrTalk(
        0xFE,
        (
            "The Birthday Celebration isn't\x01",
            "quite the same with Duke Dunan\x01",
            "instead of the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she gets better by the\x01",
            "time it officially starts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B1F7")

    ChrTalk(
        0xFE,
        (
            "That was some match, wasn't it?\x01",
            "Had me all aflutter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, time to go home and get\x01",
            "dinner ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B269")

    ChrTalk(
        0xFE,
        (
            "Saw this nun I'd never seen before\x01",
            "at the cathedral recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder when she started...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B2C2")

    ChrTalk(
        0xFE,
        (
            "I want to get some shopping\x01",
            "done at Edel's, then get the\x01",
            "heck outta here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B337")

    ChrTalk(
        0xFE,
        (
            "Some good matches this afternoon. I really\x01",
            "want to make sure I get everything done\x01",
            "before they start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B387")

    ChrTalk(
        0xFE,
        (
            "Ahhh... Nothin' like a tourney\x01",
            "to soothe one's shattered nerves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B3FA")

    ChrTalk(
        0xFE,
        (
            "Today's match-ups should set\x01",
            "a few new records, yesiree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This afteroon can't come soon\x01",
            "enough!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B45C")

    ChrTalk(
        0xFE,
        (
            "Heh heh. There've been a lot\x01",
            "of good matches this year,\x01",
            "even in the preliminaries!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B4BA")

    ChrTalk(
        0xFE,
        (
            "Everyone in the city always looks\x01",
            "forward to the annual Martial Arts\x01",
            "Competition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4BA")

    TalkEnd(0xFE)
    Return()

    # Function_21_B030 end

    def Function_22_B4BE(): pass

    label("Function_22_B4BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B540")

    ChrTalk(
        0xFE,
        (
            "During the Birthday Celebration,\x01",
            "nobody really comes here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we still need to stand guard,\x01",
            "just in case!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B54A")
    Jump("loc_B72D")

    label("loc_B54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B58D")

    ChrTalk(
        0xFE,
        (
            "After the tournament, this\x01",
            "place gets pretty quiet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B642")

    ChrTalk(
        0xFE,
        "So...the bracers won it, I hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kind of thought the Special\x01",
            "Ops Team'd have an edge..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh well. The bracers won, fair\x01",
            "and square. No getting around\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B69C")

    ChrTalk(
        0xFE,
        "So, the championship's today, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I look forward to a quiet shift.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B6FE")

    ChrTalk(
        0xFE,
        (
            "It's tough being on guard duty\x01",
            "during the tournament, what\x01",
            "with people EVERYWHERE.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B708")
    Jump("loc_B72D")

    label("loc_B708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B712")
    Jump("loc_B72D")

    label("loc_B712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B71C")
    Jump("loc_B72D")

    label("loc_B71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B726")
    Jump("loc_B72D")

    label("loc_B726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B72D")

    label("loc_B72D")

    TalkEnd(0xFE)
    Return()

    # Function_22_B4BE end

    def Function_23_B731(): pass

    label("Function_23_B731")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B7C5")

    ChrTalk(
        0xFE,
        (
            "Word is they're going to start\x01",
            "restructuring the royal military's\x01",
            "chain of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they put the right\x01",
            "people on top!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B7CF")
    Jump("loc_BA04")

    label("loc_B7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B86D")

    ChrTalk(
        0xFE,
        (
            "Those terrorists still\x01",
            "haven't been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's probably why I'm\x01",
            "still standing guard here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But we're all...frankly,\x01",
            "exhausted!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B907")

    ChrTalk(
        0xFE,
        (
            "I was up late last night on\x01",
            "patrol, so I need to get\x01",
            "some proper rest tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the tournament over,\x01",
            "I hope I can get some leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B960")

    ChrTalk(
        0xFE,
        (
            "I was up late last night,\x01",
            "on patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So I didn't get a lot of sleep.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B9D5")

    ChrTalk(
        0xFE,
        (
            "We've got to really keep a close\x01",
            "eye on the city, to ensure there\x01",
            "are no further terrorist incidents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B9DF")
    Jump("loc_BA04")

    label("loc_B9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B9E9")
    Jump("loc_BA04")

    label("loc_B9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B9F3")
    Jump("loc_BA04")

    label("loc_B9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B9FD")
    Jump("loc_BA04")

    label("loc_B9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BA04")

    label("loc_BA04")

    TalkEnd(0xFE)
    Return()

    # Function_23_B731 end

    def Function_24_BA08(): pass

    label("Function_24_BA08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BAAA")

    ChrTalk(
        0xFE,
        (
            "Word is they're going to start\x01",
            "restructuring the royal military's\x01",
            "chain of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they put someone with\x01",
            "some brains in command...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BAAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BAB4")
    Jump("loc_BCC7")

    label("loc_BAB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BB3E")

    ChrTalk(
        0xFE,
        (
            "We're patrolling endlessly, and\x01",
            "keeping all the access gates shut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finding those terrorists is\x01",
            "just a matter of time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BB3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BB9C")

    ChrTalk(
        0xFE,
        (
            "I'll be patrolling inside the\x01",
            "department store later. That's\x01",
            "my favorite beat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BB9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BC07")

    ChrTalk(
        0xFE,
        (
            "If you see any Royal Guardsmen,\x01",
            "or anyone else who seems suspi-\x01",
            "cious, please, let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BC07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BC98")

    ChrTalk(
        0xFE,
        (
            "I can't believe the Sky Bandits\x01",
            "got permission to fight in the\x01",
            "competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What the hell is going through\x01",
            "the duke's head?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BC98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BCA2")
    Jump("loc_BCC7")

    label("loc_BCA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BCAC")
    Jump("loc_BCC7")

    label("loc_BCAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BCB6")
    Jump("loc_BCC7")

    label("loc_BCB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BCC0")
    Jump("loc_BCC7")

    label("loc_BCC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BCC7")

    label("loc_BCC7")

    TalkEnd(0xFE)
    Return()

    # Function_24_BA08 end

    def Function_25_BCCB(): pass

    label("Function_25_BCCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BCD8")
    Jump("loc_BD7A")

    label("loc_BCD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BD23")

    ChrTalk(
        0xFE,
        "Yeah? What do you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Stop makin' googly-eyes at me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD7A")

    label("loc_BD23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BD2D")
    Jump("loc_BD7A")

    label("loc_BD2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BD37")
    Jump("loc_BD7A")

    label("loc_BD37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BD41")
    Jump("loc_BD7A")

    label("loc_BD41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BD4B")
    Jump("loc_BD7A")

    label("loc_BD4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BD55")
    Jump("loc_BD7A")

    label("loc_BD55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BD5F")
    Jump("loc_BD7A")

    label("loc_BD5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BD69")
    Jump("loc_BD7A")

    label("loc_BD69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BD73")
    Jump("loc_BD7A")

    label("loc_BD73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BD7A")

    label("loc_BD7A")

    TalkEnd(0xFE)
    Return()

    # Function_25_BCCB end

    def Function_26_BD7E(): pass

    label("Function_26_BD7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BD8B")
    Jump("loc_BE65")

    label("loc_BD8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BE0E")

    ChrTalk(
        0xFE,
        (
            "People haven't seen Colonel\x01",
            "Richard anywhere-- not even\x01",
            "inside the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Where the heck could he have gone?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE65")

    label("loc_BE0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BE18")
    Jump("loc_BE65")

    label("loc_BE18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BE22")
    Jump("loc_BE65")

    label("loc_BE22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BE2C")
    Jump("loc_BE65")

    label("loc_BE2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BE36")
    Jump("loc_BE65")

    label("loc_BE36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BE40")
    Jump("loc_BE65")

    label("loc_BE40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BE4A")
    Jump("loc_BE65")

    label("loc_BE4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BE54")
    Jump("loc_BE65")

    label("loc_BE54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BE5E")
    Jump("loc_BE65")

    label("loc_BE5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BE65")

    label("loc_BE65")

    TalkEnd(0xFE)
    Return()

    # Function_26_BD7E end

    def Function_27_BE69(): pass

    label("Function_27_BE69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BE76")
    Jump("loc_BFDD")

    label("loc_BE76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BF86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_BEEC")

    ChrTalk(
        0xFE,
        (
            "Commander Lorence really\x01",
            "fought hard in the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a real force to be\x01",
            "reckoned with!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF83")

    label("loc_BEEC")

    OP_A2(0x17)

    ChrTalk(
        0xFE,
        (
            "You guys really earned\x01",
            "that championship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commander Lorence really\x01",
            "fought hard in the finals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a real force to be\x01",
            "reckoned with!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF83")

    Jump("loc_BFDD")

    label("loc_BF86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BF90")
    Jump("loc_BFDD")

    label("loc_BF90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BF9A")
    Jump("loc_BFDD")

    label("loc_BF9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BFA4")
    Jump("loc_BFDD")

    label("loc_BFA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BFAE")
    Jump("loc_BFDD")

    label("loc_BFAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BFB8")
    Jump("loc_BFDD")

    label("loc_BFB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BFC2")
    Jump("loc_BFDD")

    label("loc_BFC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BFCC")
    Jump("loc_BFDD")

    label("loc_BFCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BFD6")
    Jump("loc_BFDD")

    label("loc_BFD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BFDD")

    label("loc_BFDD")

    TalkEnd(0xFE)
    Return()

    # Function_27_BE69 end

    def Function_28_BFE1(): pass

    label("Function_28_BFE1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Allllllll right, time to hit\x01",
            "up that department store!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_BFE1 end

    def Function_29_C024(): pass

    label("Function_29_C024")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "May as well pick up some of\x01",
            "the latest fashions after\x01",
            "coming all this way, y'know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_C024 end

    def Function_30_C083(): pass

    label("Function_30_C083")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Will you look at this line?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's it for?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_C083 end

    def Function_31_C0C0(): pass

    label("Function_31_C0C0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Who do you think I am, a kid?\x01",
            "I'm not going to eat that!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_C0C0 end

    def Function_32_C105(): pass

    label("Function_32_C105")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh, you're not, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, then I guess you don't\x01",
            "mind your old man eating it.\x01",
            "Ha ha ha ha ha!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_C105 end

    def Function_33_C179(): pass

    label("Function_33_C179")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "This crowd is something else...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_C179 end

    def Function_34_C1A5(): pass

    label("Function_34_C1A5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It's a lot hotter today than\x01",
            "it's been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ice cold refreshment time!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_C1A5 end

    def Function_35_C1FB(): pass

    label("Function_35_C1FB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "HEY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No cutting in line!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_C1FB end

    def Function_36_C225(): pass

    label("Function_36_C225")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This line sure is taking its\x01",
            "sweet time...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_C225 end

    def Function_37_C25C(): pass

    label("Function_37_C25C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "You hear about that coup d'etat? Was\x01",
            "pretty serious, but the Royal Guard\x01",
            "and the bracers put a stop to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't help wondering about the\x01",
            "Royal Army, though...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_C25C end

    def Function_38_C30D(): pass

    label("Function_38_C30D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "So this is the famous Museum\x01",
            "of History, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Birthday Celebration first.\x01",
            "THEN it's museum time!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_C30D end

    def Function_39_C381(): pass

    label("Function_39_C381")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Never too old to learn more\x01",
            "about the world around you,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_C381 end

    def Function_40_C3CF(): pass

    label("Function_40_C3CF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oogh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got a blister on my feet from\x01",
            "all this walking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It really, really hurts, too!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_C3CF end

    def Function_41_C43D(): pass

    label("Function_41_C43D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's what you get for not\x01",
            "breaking in those shoes,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_C43D end

    def Function_42_C489(): pass

    label("Function_42_C489")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Daad, that is sooooo laaaame!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_C489 end

    def Function_43_C4B3(): pass

    label("Function_43_C4B3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I'm getting chills from the\x01",
            "sheer lameness of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the coup d'etat had \x01",
            "succeeded, would Duke Dunan \x01",
            "have taken over the throne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'd be goners if that happened!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_C4B3 end

    def Function_44_C56D(): pass

    label("Function_44_C56D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I heard the Intelligence\x01",
            "Division was behind the\x01",
            "so-called 'terrorists.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad it didn't turn out\x01",
            "to be the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_C56D end

    def Function_45_C5FA(): pass

    label("Function_45_C5FA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Apparently, the department store's\x01",
            "holding a big sale for the queen's\x01",
            "Birthday Celebration!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the latest brands and\x01",
            "fashions are on sale-- but\x01",
            "only for a limited time!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_C5FA end

    def Function_46_C6B5(): pass

    label("Function_46_C6B5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Are you SERIOUS?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We gotta get over there!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_C6B5 end

    def Function_47_C6F1(): pass

    label("Function_47_C6F1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It sure is calm, considering\x01",
            "there was a coup d'etat not\x01",
            "long ago...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_C6F1 end

    def Function_48_C742(): pass

    label("Function_48_C742")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "So, this is Calvard's embassy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd love to see the inside of it.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_48_C742 end

    def Function_49_C796(): pass

    label("Function_49_C796")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is my first time\x01",
            "visiting the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The roads are so wide!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_C796 end

    def Function_50_C7EA(): pass

    label("Function_50_C7EA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hey! Don't wander off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'm worried my daughter will\x01",
            "get lost in all this craziness.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_C7EA end

    def Function_51_C852(): pass

    label("Function_51_C852")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This year the airships were\x01",
            "a mess, so we missed the\x01",
            "competition altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard it was because of\x01",
            "Colonel Richard's coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I liked that guy, too! Sucks\x01",
            "when someone turns out to be\x01",
            "a backstabber.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_51_C852 end

    def Function_52_C930(): pass

    label("Function_52_C930")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'm gonna get a toy airship!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_52_C930 end

    def Function_53_C959(): pass

    label("Function_53_C959")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My grandson begged me to take\x01",
            "him to the department store.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_53_C959 end

    def Function_54_C9A0(): pass

    label("Function_54_C9A0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now that the coup's been\x01",
            "thwarted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...it's finally sunk in that the\x01",
            "ones who thwarted it were the\x01",
            "tournament champions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Crazy times call for crazy riots!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_54_C9A0 end

    def Function_55_CA52(): pass

    label("Function_55_CA52")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It makes me kind of nervous,\x01",
            "dancing around like this in\x01",
            "front of the Erebonian embassy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's an intimidating place!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_55_CA52 end

    def Function_56_CAD8(): pass

    label("Function_56_CAD8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think you're big enough to\x01",
            "walk by yourself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But whatever!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_56_CAD8 end

    def Function_57_CB28(): pass

    label("Function_57_CB28")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Sis! Give me a piggy-back!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_57_CB28 end

    def Function_58_CB4F(): pass

    label("Function_58_CB4F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The reception is over, so I'm\x01",
            "gonna go look around the city.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_58_CB4F end

    SaveToFile()

Try(main)
