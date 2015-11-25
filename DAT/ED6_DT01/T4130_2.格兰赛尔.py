from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
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
        "Function_3_303",          # 03, 3
        "Function_4_578",          # 04, 4
        "Function_5_757",          # 05, 5
        "Function_6_829",          # 06, 6
        "Function_7_9A0",          # 07, 7
        "Function_8_9A5",          # 08, 8
        "Function_9_1324",         # 09, 9
        "Function_10_1F1A",        # 0A, 10
        "Function_11_29EF",        # 0B, 11
        "Function_12_2E97",        # 0C, 12
        "Function_13_30CA",        # 0D, 13
        "Function_14_56F2",        # 0E, 14
        "Function_15_5F21",        # 0F, 15
        "Function_16_5F26",        # 10, 16
        "Function_17_74BC",        # 11, 17
        "Function_18_7660",        # 12, 18
        "Function_19_77C4",        # 13, 19
        "Function_20_7899",        # 14, 20
        "Function_21_7A57",        # 15, 21
        "Function_22_7F62",        # 16, 22
        "Function_23_8620",        # 17, 23
        "Function_24_92B3",        # 18, 24
        "Function_25_92B8",        # 19, 25
        "Function_26_9DE3",        # 1A, 26
        "Function_27_A03F",        # 1B, 27
        "Function_28_AA38",        # 1C, 28
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
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_BE")

    label("loc_8D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A3")
    SetChrSubChip(0xFE, 1)
    Jump("loc_BE")

    label("loc_A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B9")
    SetChrSubChip(0xFE, 0)
    Jump("loc_BE")

    label("loc_B9")

    SetChrSubChip(0xFE, 2)

    label("loc_BE")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_14A")

    ChrTalk(
        0x1F,
        (
            "#100FAgate's a mere chick compared\x01",
            "to the phoenix that is Cassius.\x02\x03",
            "Nonetheless, I am extremely\x01",
            "grateful to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FA")

    label("loc_14A")

    OP_A2(0x6F0)
    OP_A2(0x17)

    ChrTalk(
        0x1F,
        (
            "#104FAhh, dear me... I'm much too\x01",
            "old to be living on the lam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWere you OK, being left\x01",
            "on your own with Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#100FAbsolutely fine!\x02\x03",
            "He was very courteous, and\x01",
            "mindful of my needs.\x02\x03",
            "#100FHe even made sure to plan our\x01",
            "daily routes so as not to wear\x01",
            "me down too much!\x02\x03",
            "#104FI haven't any complaints\x01",
            "about Agate at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FO-Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#101FHe's no Cassius, of course, but\x01",
            "I am still grateful to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_2_68 end

    def Function_3_303(): pass

    label("Function_3_303")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_328")
    SetChrSubChip(0xFE, 1)
    Jump("loc_359")

    label("loc_328")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33E")
    SetChrSubChip(0xFE, 0)
    Jump("loc_359")

    label("loc_33E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_354")
    SetChrSubChip(0xFE, 2)
    Jump("loc_359")

    label("loc_354")

    SetChrSubChip(0xFE, 1)

    label("loc_359")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_3E7")

    ChrTalk(
        0x1E,
        (
            "#560FGrandpa promised he'd have\x01",
            "ice cream with me.\x02\x03",
            "#562FI asked Agate to come too, but\x01",
            "he said he didn't want to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56F")

    label("loc_3E7")

    OP_A2(0x16)
    OP_A2(0x6F1)

    ChrTalk(
        0x1E,
        "#560FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FWow, Tita, you look happy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#061F*giggle* Grandpa promised me\x01",
            "we could have ice cream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FOoh, ice cream! Ice cream is\x01",
            "goooood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#061FYou bet it is!\x02\x03",
            "#064FI asked Agate to come too, but\x01",
            "he said he didn't want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509FAgate eating ice cream... I'd\x01",
            "pay good money to see that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#562FI bet he'd like it if he tried\x01",
            "it, though!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_303 end

    def Function_4_578(): pass

    label("Function_4_578")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_5E0")

    ChrTalk(
        0x1D,
        (
            "#053FThe Martial Arts Tournament...\x02\x03",
            "Could be a good opportunity to\x01",
            "hone my skills...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_753")

    label("loc_5E0")

    OP_A2(0x15)
    OP_A2(0x6EE)

    ChrTalk(
        0x1D,
        (
            "#053FThe Martial Arts Tournament...\x02\x03",
            "Could be a good opportunity to\x01",
            "hone my skills...\x02\x03",
            "#050FAnd if 'Zane the Immovable' made\x01",
            "an appearance there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWhy don't you try to get in\x01",
            "next year, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#053FMaybe. It might be nice, but it's\x01",
            "become such a circus...and I don't\x01",
            "like doing tricks for a crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F...Well, whatever floats your\x01",
            "boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_753")

    TalkEnd(0xFE)
    Return()

    # Function_4_578 end

    def Function_5_757(): pass

    label("Function_5_757")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Special Ops are supposedly keeping\x01",
            "watch over the capital, so the Royal\x01",
            "Garrison have been told to pull back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't agree with the order,\x01",
            "though. Honestly, I'm not even\x01",
            "sure who gave it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_757 end

    def Function_6_829(): pass

    label("Function_6_829")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_8BE")

    ChrTalk(
        0xFE,
        (
            "We have absolutely NO idea\x01",
            "what's going on around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are almost no regular\x01",
            "military troops in the capital\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C")

    label("loc_8BE")

    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "We have absolutely NO idea\x01",
            "what's going on around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are almost no regular\x01",
            "military troops in the capital\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no idea whatsoever as to\x01",
            "the proper course of action from\x01",
            "here on out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C")

    TalkEnd(0xFE)
    Return()

    # Function_6_829 end

    def Function_7_9A0(): pass

    label("Function_7_9A0")

    Call(2, 8)
    Return()

    # Function_7_9A0 end

    def Function_8_9A5(): pass

    label("Function_8_9A5")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A86")

    ChrTalk(
        0x1A,
        (
            "I was shocked when I heard \x01",
            "Colonel Richard had tried\x01",
            "to stage a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I'm just glad it was stopped\x01",
            "before it actually got started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "And that's all thanks to the\x01",
            "Royal Guard and the bracers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_AF7")

    ChrTalk(
        0x1A,
        "What in the world is going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "All of the soldiers are being\x01",
            "called to pull out of the city!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_C08")

    ChrTalk(
        0x1A,
        (
            "Everyone is all caught up in the\x01",
            "Queen's Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But with all this hubbub, is it\x01",
            "even going to happen this year?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Popular rumor is that it's going to be\x01",
            "canceled, and the queen hasn't made any\x01",
            "official announcements to debunk that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_CA3")

    ChrTalk(
        0x1A,
        (
            "Dorothy seems to know the\x01",
            "team that won the Martial\x01",
            "Arts Competition this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "She was practically dancing on\x01",
            "air when she came home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_DF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_D29")

    ChrTalk(
        0x1A,
        (
            "Dorothy's already gone; she\x01",
            "snatched up her camera and\x01",
            "ran off to the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "She seemed unusually focused!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF4")

    label("loc_D29")

    OP_A2(0x12)

    ChrTalk(
        0x1A,
        (
            "Good morning! So, today's\x01",
            "the big day, no? The day of\x01",
            "the championship match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Dorothy's already gone; she\x01",
            "snatched up her camera and\x01",
            "ran off to the arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "She seemed unusually focused!\x02",
    )

    CloseMessageWindow()

    label("loc_DF4")

    Jump("loc_1320")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_E82")

    ChrTalk(
        0x1A,
        (
            "It seems like the Royal Army\x01",
            "has been around constantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "My company's not to blame for\x01",
            "their heightened alert, I hope!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_ED9")

    ChrTalk(
        0x1A,
        "I love Colonel Richard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I'd love to do an exclusive\x01",
            "on him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8D")

    label("loc_ED9")

    OP_A2(0x12)

    ChrTalk(
        0x1A,
        "I love Colonel Richard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "He's smart, he's macho, he's\x01",
            "fit...he's HOT...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I'd love to do an exclusive\x01",
            "on him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Maybe I'll ask Nial what he\x01",
            "thinks of the idea...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8D")

    Jump("loc_1320")

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_103B")

    ChrTalk(
        0x1A,
        (
            "Nial's finally back from\x01",
            "his recent assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "He's known to just disappear for days\x01",
            "at a time, so every return of his is\x01",
            "kind of a special occasion!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1104")

    ChrTalk(
        0x1A,
        (
            "A lot of reporters are gone\x01",
            "during the day; they're off\x01",
            "doing their legwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Nial's hardly ever in the office.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It can be a real pain trying\x01",
            "to get in touch with him\x01",
            "sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_117E")

    ChrTalk(
        0x1A,
        (
            "After work I was going to go\x01",
            "hang out with Dorothy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But she seems to have her hands\x01",
            "full right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_117E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(
        0x1A,
        (
            "There's almost nobody in the newsroom\x01",
            "these days, so I've kinda been put in\x01",
            "charge of it by default.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_11F9")

    OP_A2(0x12)

    ChrTalk(
        0x1A,
        (
            "Welcome to the Liberl News!\x01",
            "Despite our name, we're totally\x01",
            "nonpartisan, I SWEAR! *wink*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "First floor is information,\x01",
            "second floor is the newsroom,\x01",
            "and third floor is printing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "There's almost nobody in the newsroom\x01",
            "these days, so I've kinda been put in\x01",
            "charge of it by default.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1320")

    TalkEnd(0x1A)
    Return()

    # Function_8_9A5 end

    def Function_9_1324(): pass

    label("Function_9_1324")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_13CC")

    ChrTalk(
        0xFE,
        (
            "I'm off to cover this ice\x01",
            "cream shop that people've\x01",
            "been lining up to eat at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in the East Block. I bet\x01",
            "its business is booming again\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F16")

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_14CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1439")

    ChrTalk(
        0xFE,
        "Nial got arrested by the army?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man... Glad I got assigned\x01",
            "to the culture section!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CB")

    label("loc_1439")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        "Nial got arrested by the army?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it was bound to happen\x01",
            "sooner or later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man... Glad I got assigned\x01",
            "to the culture section!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CB")

    Jump("loc_1F16")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_161E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(
        0xFE,
        (
            "I was all ready to go cover\x01",
            "the Anterose in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have to come up with\x01",
            "something else to write about.\x01",
            "Le sigh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161B")

    label("loc_1560")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        "Aww, the airships are stopped!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was all ready to go cover\x01",
            "the Anterose in Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have to think of something\x01",
            "else to write! Cruel fate, why\x01",
            "must you mock me so?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161B")

    Jump("loc_1F16")

    label("loc_161E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_180E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(
        0xFE,
        (
            "Only the culture reporter gets\x01",
            "to go to different restaurants\x01",
            "and comment on the cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait to see the look\x01",
            "on Nial's face when I tell him\x01",
            "what I'm getting paid to do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180B")

    label("loc_16EC")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Heh, my newest article is a \x01",
            "showcase piece for all of the\x01",
            "most popular restaurants here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only the culture reporter gets\x01",
            "to go to different restaurants\x01",
            "and comment on the cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait to see the look\x01",
            "on Nial's face when I tell him\x01",
            "what I'm getting paid to do!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180B")

    Jump("loc_1F16")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1908")

    ChrTalk(
        0xFE,
        (
            "Dorothy only just started, but let me tell\x01",
            "you, she's got a TON of initiative...but not\x01",
            "enough Faults, if you get my drift! Eh? Eh?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the real hero here, though,\x01",
            "is the editor brave enough to hire\x01",
            "a girl like her...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A43")

    label("loc_1908")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Dorothy only just started, but let me tell\x01",
            "you, she's got a TON of initiative...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a real shutterbug, snapping photos of\x01",
            "everything from the tournament to restaurant\x01",
            "cuisine-- and all of 'em look great!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the real hero here, though,\x01",
            "is the editor brave enough to hire\x01",
            "a girl like her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    Jump("loc_1F16")

    label("loc_1A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1ADC")

    ChrTalk(
        0xFE,
        (
            "Lots of my editors and writers\x01",
            "always get sick as the deadline\x01",
            "approaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And let me tell you, that's no\x01",
            "good for anyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC9")

    label("loc_1ADC")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "Lots of my editors and writers\x01",
            "always get sick near deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's an unfortunate cocktail of\x01",
            "stress, insomnia and poor diet,\x01",
            "if you ask me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or they're just playing\x01",
            "hooky. The results are still\x01",
            "the same, either way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC9")

    Jump("loc_1F16")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1C62")

    ChrTalk(
        0xFE,
        (
            "I grabbed an airship to go pick\x01",
            "up a much-needed manuscript the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But wouldn't you know it, it\x01",
            "wasn't done yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D44")

    label("loc_1C62")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "I grabbed an airship to go pick\x01",
            "up a much-needed manuscript the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But wouldn't you know it, it\x01",
            "wasn't done yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If more people used orbal\x01",
            "communications, it'd be so much\x01",
            "easier to stay in touch...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D44")

    Jump("loc_1F16")

    label("loc_1D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D51")
    Jump("loc_1F16")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1DF6")

    ChrTalk(
        0xFE,
        (
            "Today I'm taking an airship\x01",
            "to go get a manuscript.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't finish getting ready\x01",
            "soon, though, I'll miss my flight!\x01",
            "So if you'll excuse me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F16")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(
        0xFE,
        (
            "I'm in charge of the Liberl\x01",
            "News' culture section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's mostly book reviews, or\x01",
            "articles on popular local inns,\x01",
            "restaurants and so forth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F16")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1F16")

    ChrTalk(
        0xFE,
        (
            "If I don't get that manuscript\x01",
            "soon, my editor'll kill me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nial and Noticia are SO much\x01",
            "stricter than the chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F16")

    TalkEnd(0xFE)
    Return()

    # Function_9_1324 end

    def Function_10_1F1A(): pass

    label("Function_10_1F1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1FAE")

    ChrTalk(
        0xFE,
        (
            "Heh... Nial really let me have\x01",
            "it this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to have him teach me\x01",
            "how he always manages to get\x01",
            "such a great scoop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1FEE")

    ChrTalk(
        0xFE,
        (
            "Something seems...off...about\x01",
            "the town lately...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_208E")

    ChrTalk(
        0xFE,
        (
            "Nial was so reckless when he\x01",
            "first started this job. Really,\x01",
            "he still is pretty reckless!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that's probably why he\x01",
            "always gets the goods!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_208E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2128")

    ChrTalk(
        0xFE,
        (
            "That squinty witch captain \x01",
            "just pisses me right off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She can never go two seconds\x01",
            "without making some sort of\x01",
            "snarky comment!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2223")

    label("loc_2128")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "I admire Colonel Richard, but I still\x01",
            "don't approve of his Intelligence \x01",
            "Division or those Special Ops. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially that witch captain\x01",
            "with the squinty eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She can never go two seconds\x01",
            "without making some sort of\x01",
            "snarky comment!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2223")

    Jump("loc_29EB")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_22D6")

    ChrTalk(
        0xFE,
        (
            "The Intelligence Division is always\x01",
            "breathing down our necks. Doesn't\x01",
            "help us one bit, let me tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're almost like the MP\x01",
            "of the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_22D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_23AD")

    ChrTalk(
        0xFE,
        (
            "Both Nial and I get into it sometimes\x01",
            "with our editor over matters of...\x01",
            "journalistic integrity, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's really hard to stay\x01",
            "mad when he's always got that\x01",
            "huge grin on his face!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2493")

    label("loc_23AD")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "Our editor...is a real oddball!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Nial and I get into it sometimes\x01",
            "with him over matters of...journalistic\x01",
            "integrity, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's really hard to stay\x01",
            "mad when he's always got that\x01",
            "huge grin on his face!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2493")

    Jump("loc_29EB")

    label("loc_2496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_25A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2506")

    ChrTalk(
        0xFE,
        (
            "Nial's been up all night doing\x01",
            "some kind of research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I bet he's found a hot lead!\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A6")

    label("loc_2506")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "Nial's been up all night doing\x01",
            "some kind of research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I bet he's found a hot lead!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'm not going to let him\x01",
            "hog all the glory, nosiree!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A6")

    Jump("loc_29EB")

    label("loc_25A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2642")

    ChrTalk(
        0xFE,
        (
            "This year was all group \x01",
            "fighting, so getting good\x01",
            "pictures wasn't easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...My kingdom for a cameraman\x01",
            "with some real shutter skill!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_2642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_27E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_26FD")

    ChrTalk(
        0xFE,
        (
            "The Liberl News is putting \x01",
            "together a special issue for\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got some real legwork to\x01",
            "do if I want to leave my mark\x01",
            "on this one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E5")

    label("loc_26FD")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "The main event starts today.\x01",
            "I'm super-duper excited!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Liberl News is putting \x01",
            "together a special issue for\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got some real legwork to\x01",
            "do if I want to leave my mark\x01",
            "on this one!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E5")

    Jump("loc_29EB")

    label("loc_27E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_287F")

    ChrTalk(
        0xFE,
        "That Nial is a shark!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think he's at rest after a hard\x01",
            "day's work...but no! He's already\x01",
            "out sniffing up his next scoop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_287F")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "That Nial is a shark!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think he's at rest after a hard\x01",
            "day's work...but no! He's already\x01",
            "out sniffing up his next scoop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't let that pale complexion\x01",
            "and the endless cigarettes \x01",
            "fool you. He's a wily one!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2963")

    Jump("loc_29EB")

    label("loc_2966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_29EB")

    ChrTalk(
        0xFE,
        (
            "Aaah! The prelims are gonna\x01",
            "start here soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Camera? Check. Press pass?\x01",
            "Check, and double check.\x01",
            "Checkbook? ...Yes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EB")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F1A end

    def Function_11_29EF(): pass

    label("Function_11_29EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2A82")

    ChrTalk(
        0xA,
        (
            "#151FYou know, Nial was telling me\x01",
            "something interesting...\x02\x03",
            "...He said this story's going\x01",
            "to win us the Fuelitzer Prize!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C95")

    label("loc_2A82")

    OP_A2(0xF)
    OP_A2(0x6F3)

    ChrTalk(
        0xA,
        (
            "#151FYay, it's Estelle and Joshua!\x02\x03",
            "#150FYou know, Nial was telling me\x01",
            "something interesting...\x02\x03",
            "...He said this story's going\x01",
            "to win us the Fuelitzer Prize!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FThe what, now? Don't you mean\x01",
            "the Pu--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FShhh! You want to get sued? The Fuelitzer is\x01",
            "an annual award presented to the very best\x01",
            "examples of journalism, literature and music.\x02\x03",
            "There's no higher honor for\x01",
            "any reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FAh. Well...good for you, then,\x01",
            "I guess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#151FEheh! It's actually all thanks to\x01",
            "YOU two! You're my whole story!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C95")

    Jump("loc_2E93")

    label("loc_2C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2CE8")

    ChrTalk(
        0xA,
        (
            "#151FOh, thank the Goddess Nial is\x01",
            "still alive! *weep* *sniffle*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2D2B")

    ChrTalk(
        0xA,
        (
            "#152FPlease, Estelle! I beg you!\x02\x03",
            "Please save Nial!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E93")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2DC2")

    ChrTalk(
        0xA,
        (
            "#154FThe editor told me to go look\x01",
            "for Nial...\x02\x03",
            "But I have no idea where he\x01",
            "could possibly be! I don't\x01",
            "even know where to begin!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E4D")

    label("loc_2DC2")

    OP_A2(0xF)

    ChrTalk(
        0xA,
        (
            "#151FEstelle and company!\x02\x03",
            "Congratulations! That was\x01",
            "a simply AMAZING match!\x02\x03",
            "I got so many great shots!\x01",
            "I can't wait to show you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4D")

    Jump("loc_2E93")

    label("loc_2E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2E5A")
    Jump("loc_2E93")

    label("loc_2E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2E64")
    Jump("loc_2E93")

    label("loc_2E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2E6E")
    Jump("loc_2E93")

    label("loc_2E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2E78")
    Jump("loc_2E93")

    label("loc_2E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2E82")
    Jump("loc_2E93")

    label("loc_2E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2E8C")
    Jump("loc_2E93")

    label("loc_2E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2E93")

    label("loc_2E93")

    TalkEnd(0xFE)
    Return()

    # Function_11_29EF end

    def Function_12_2E97(): pass

    label("Function_12_2E97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3065")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2F29")

    ChrTalk(
        0xFE,
        (
            "#141FThere is a TON of buzz right\x01",
            "now about your little stunt.\x02\x03",
            "Biggest scoop of my career, you guys!\x01",
            "You did real good!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3062")

    label("loc_2F29")

    OP_A2(0xE)
    OP_A2(0x6F4)

    ChrTalk(
        0xFE,
        (
            "#141FJoshua! Estelle! Great job!\x02\x03",
            "Our special coup edition has\x01",
            "been flying off the stands.\x02\x03",
            "There is a TON of buzz right\x01",
            "now about your little stunt.\x02\x03",
            "Sorry I couldn't get you guys\x01",
            "some fame from it; the guild\x01",
            "made me withhold your names.\x02\x03",
            "#147FBiggest scoop of my career, you guys!\x01",
            "You did real good!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3062")

    Jump("loc_30C6")

    label("loc_3065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_306F")
    Jump("loc_30C6")

    label("loc_306F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3079")
    Jump("loc_30C6")

    label("loc_3079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3083")
    Jump("loc_30C6")

    label("loc_3083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_308D")
    Jump("loc_30C6")

    label("loc_308D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3097")
    Jump("loc_30C6")

    label("loc_3097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_30A1")
    Jump("loc_30C6")

    label("loc_30A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_30AB")
    Jump("loc_30C6")

    label("loc_30AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_30B5")
    Jump("loc_30C6")

    label("loc_30B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_30BF")
    Jump("loc_30C6")

    label("loc_30BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_30C6")

    label("loc_30C6")

    TalkEnd(0xFE)
    Return()

    # Function_12_2E97 end

    def Function_13_30CA(): pass

    label("Function_13_30CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_32D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_31A1")

    ChrTalk(
        0xFE,
        (
            "Our special edition covering Colonel\x01",
            "Richard's coup d'etat has generated\x01",
            "a whole lot of buzz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's already outsold our Mayor\x01",
            "Dalmore AND Colonel Richard\x01",
            "editions combined-- twice over!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D6")

    label("loc_31A1")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "Our special edition covering Colonel\x01",
            "Richard's coup d'etat has generated\x01",
            "a whole lot of buzz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's already outsold our Mayor\x01",
            "Dalmore AND Colonel Richard\x01",
            "editions combined-- twice over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was such a huge incident, everyone\x01",
            "felt they had to write in about it.\x01",
            "We're totally swimming in mail!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D6")

    Jump("loc_56EE")

    label("loc_32D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_33E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3350")

    ChrTalk(
        0xFE,
        (
            "So Nial's been found at the\x01",
            "Erbe Royal Villa, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can finally breathe a sigh\x01",
            "of relief...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E6")

    label("loc_3350")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "So Nial's been found at the\x01",
            "Erbe Royal Villa, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just now heard from the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can finally breathe a sigh\x01",
            "of relief...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E6")

    Jump("loc_56EE")

    label("loc_33E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3420")

    ChrTalk(
        0xFE,
        (
            "I'm leaving Nial in your\x01",
            "capable hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56EE")

    label("loc_3420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_38DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_34D8")

    ChrTalk(
        0xFE,
        (
            "Hmm... I had a question for Nial,\x01",
            "but I can't seem to find him.\x01",
            "Any idea where he might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it...\x01",
            "I haven't seen him in several\x01",
            "days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DB")

    label("loc_34D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3587")

    ChrTalk(
        0xFE,
        (
            "I've been looking for Nial for the\x01",
            "past several days now, but I've seen\x01",
            "hide nor hair of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Not too uncommon in this line\x01",
            "of work, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DB")

    label("loc_3587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_367D")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "Hmm... I had a question for Nial,\x01",
            "but I can't seem to find him.\x01",
            "Any idea where he might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it...\x01",
            "I haven't seen him in several\x01",
            "days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Not too uncommon in this line\x01",
            "of work, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DB")

    label("loc_367D")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you want to see Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm actually looking for him\x01",
            "myself, but I've seen neither\x01",
            "nide nor hair of him for days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Not too uncommon in this line\x01",
            "of work, though, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DB")

    Jump("loc_56EE")

    label("loc_38DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_397C")

    ChrTalk(
        0xFE,
        (
            "Dorothy should be at the arena\x01",
            "getting photos, however, if she\x01",
            "might be of some help to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you see her, be sure to say\x01",
            "hello!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C28")

    label("loc_397C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_39F7")

    ChrTalk(
        0xFE,
        (
            "So, final match today, eh?\x01",
            "Good luck out there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dorothy should already be at\x01",
            "the arena getting photos.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C28")

    label("loc_39F7")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all made it into the\x01",
            "finals, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sadly, I'm a bit too busy to\x01",
            "go the arena, but I'll be\x01",
            "cheering you on from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FThanks!\x02",
    )

    CloseMessageWindow()

    label("loc_3C28")

    Jump("loc_56EE")

    label("loc_3C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_41F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3C90")

    ChrTalk(
        0xFE,
        (
            "My reporters have been out\x01",
            "collecting stories for our\x01",
            "special edition all day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F6")

    label("loc_3C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3CFF")

    ChrTalk(
        0xFE,
        (
            "I thought it was odd for him to\x01",
            "be in the office, but it turns\x01",
            "out he was just waiting for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F6")

    label("loc_3CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_3DFC")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "I've got quite a RAGtag bunch\x01",
            "of RAG-writers here... Heh, I\x01",
            "kill me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're all pretty hard-headed.\x01",
            "I swear, you could sell seats\x01",
            "to our staff meetings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But passion sells, you know?\x01",
            "It's why our paper always does\x01",
            "so well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F6")

    label("loc_3DFC")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you want to see Nial?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_END)), "loc_413B")

    ChrTalk(
        0x101,
        "#000FYep. We have an appointment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was odd for him to\x01",
            "be in the office, but it turns\x01",
            "out he was just waiting for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's usually off...who-knows-where. I never\x01",
            "see him in the office outside of staff\x01",
            "meetings. And even then, it's spotty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that's because he's out\x01",
            "hunting for stories, like a\x01",
            "good little reporter-man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F6")

    label("loc_413B")


    ChrTalk(
        0x101,
        (
            "#000FWell, good thing he's here now,\x01",
            "then, or I'd be a mad missy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed. I think he's still\x01",
            "waiting in the newsroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Second floor of the news building.\x01",
            "You can't miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F6")

    Jump("loc_56EE")

    label("loc_41F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_467D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_42B6")

    ChrTalk(
        0xFE,
        (
            "Lately, the military's Intelligence\x01",
            "Division has been threatening to\x01",
            "censor us. No good such-and-suches!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm fairly certain they don't\x01",
            "have the right to do that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_467A")

    label("loc_42B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4313")

    ChrTalk(
        0xFE,
        (
            "Nial is out right now, working\x01",
            "on a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_467A")

    label("loc_4313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_4442")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "Ever since the queen fell ill,\x01",
            "the Intelligence Division has\x01",
            "gotten excessively pushy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've been calling for\x01",
            "us to censor ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since citizens of Liberl have the right to free\x01",
            "speech, though, I'm fairly certain they have no\x01",
            "authority to enforce anything of the sort!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_467A")

    label("loc_4442")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you want to see Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUh...not especially?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good, because he's not here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()

    label("loc_467A")

    Jump("loc_56EE")

    label("loc_467D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_474F")

    ChrTalk(
        0xFE,
        (
            "Word on the street is, you two\x01",
            "managed to worm your way into\x01",
            "the Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Nial heard, he said he was\x01",
            "going to get an interview with\x01",
            "you, and took off running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C19")

    label("loc_474F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_482A")

    ChrTalk(
        0xFE,
        (
            "So...am I just parroting rumors here,\x01",
            "or did you two really manage to get\x01",
            "into the Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Nial heard, he said he was\x01",
            "going to get an interview with\x01",
            "you, and took off running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C19")

    label("loc_482A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_4954")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        "Oh, hey, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Word on the street is, you two\x01",
            "managed to worm your way into\x01",
            "the Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Nial heard, he said he was\x01",
            "going to get an interview with\x01",
            "you, and took off running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did he catch you, or did you\x01",
            "manage to give him the slip?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C19")

    label("loc_4954")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So...am I just parroting rumors here,\x01",
            "or did you two really manage to get\x01",
            "into the Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Nial heard, he said he was\x01",
            "going to get an interview with\x01",
            "you, and took off running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did he catch you, or did you\x01",
            "manage to give him the slip?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C19")

    Jump("loc_56EE")

    label("loc_4C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_508B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4CAE")

    ChrTalk(
        0xFE,
        (
            "So, the tournament kicks off\x01",
            "today, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My reporters have been out\x01",
            "collecting stories for our\x01",
            "special edition all day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5088")

    label("loc_4CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4D44")

    ChrTalk(
        0xFE,
        (
            "Nial is out right now, getting\x01",
            "us some juicy nuggets of reportable\x01",
            "goodness. The scoop. The skinny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5088")

    label("loc_4D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_4E50")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "So, the tournament kicks off\x01",
            "today, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know how the rest of the Birthday\x01",
            "Celebration will go, but this part has\x01",
            "always been popular, every single year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My reporters have been out\x01",
            "collecting stories for our\x01",
            "special edition all day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5088")

    label("loc_4E50")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you want to see Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUh...not especially?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good, because he's not here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()

    label("loc_5088")

    Jump("loc_56EE")

    label("loc_508B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5128")

    ChrTalk(
        0xFE,
        (
            "Nial is out right now, getting\x01",
            "us some juicy nuggets of reportable\x01",
            "goodness. The scoop. The skinny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5416")

    label("loc_5128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_51DE")

    ChrTalk(
        0xFE,
        (
            "Even though we ran the story on our\x01",
            "society page, we honestly have no real\x01",
            "proof that the queen's fallen ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We couldn't get our hands\x01",
            "on anything...conclusive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5416")

    label("loc_51DE")

    OP_A2(0x67F)
    OP_A2(0xD)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you want to see Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUh...not especially?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good, because he's not here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()

    label("loc_5416")

    Jump("loc_56EE")

    label("loc_5419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_56EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_54B6")

    ChrTalk(
        0xFE,
        (
            "Nial is out right now, getting\x01",
            "us some juicy nuggets of reportable\x01",
            "goodness. The scoop. The skinny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56EE")

    label("loc_54B6")

    OP_A2(0xD)
    OP_A2(0x67F)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        "I know that crest...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Middle-Aged Man",
        (
            "Would you two happen to be the\x01",
            "junior bracers, Estelle and\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI don't know... Who's asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the editor-in-chief of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard about you two from\x01",
            "both Nial and Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, okay. That's us, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt's a pleasure to meet you.\x02\x03",
            "We're avid readers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ha, ha, ha. Glad to hear it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did you want to see Nial?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FUh...not especially?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good, because he's not here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He won't be back for a while.\x02",
    )

    CloseMessageWindow()

    label("loc_56EE")

    TalkEnd(0xFE)
    Return()

    # Function_13_30CA end

    def Function_14_56F2(): pass

    label("Function_14_56F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_58A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_57B3")

    ChrTalk(
        0xFE,
        (
            "The bracers and the Royal Guard,\x01",
            "storming Grancel Castle...it's\x01",
            "sure great for tourism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no wonder the Birthday Celebration\x01",
            "is more packed than ever before...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A2")

    label("loc_57B3")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "It's been a long time since we've\x01",
            "had a story this juicy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bracers and the Royal Guard,\x01",
            "storming Grancel Castle...it's\x01",
            "sure great for tourism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no wonder the Birthday Celebration\x01",
            "is more packed than ever before...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A2")

    Jump("loc_5F1D")

    label("loc_58A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_596F")

    ChrTalk(
        0xFE,
        (
            "Spending your day poring over\x01",
            "books and news articles teaches\x01",
            "you to...notice things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like, that there's something going\x01",
            "on behind our backs that we're not\x01",
            "supposed to know about...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_596F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5A15")

    ChrTalk(
        0xFE,
        (
            "The Royal Guard may seem a bit\x01",
            "antiquated by modern standards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to see them sticking to their\x01",
            "rules of discipline was...simply\x01",
            "breathtaking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5AC3")

    ChrTalk(
        0xFE,
        (
            "There haven't been any details\x01",
            "yet about the queen's illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And she hasn't said anything\x01",
            "herself...so maybe this is all\x01",
            "just an out-of-control rumor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5B0A")

    ChrTalk(
        0xFE,
        (
            "Aaah. A cafe ole does wonders\x01",
            "for morning drowsiness...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5B51")

    ChrTalk(
        0xFE,
        (
            "Oy vey... When did 'soldier'\x01",
            "become a four-letter word?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5BA2")

    ChrTalk(
        0xFE,
        "Reading is food for the soul.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And right now I'm very hungry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5C50")

    ChrTalk(
        0xFE,
        (
            "I'm pretty sure the owner \x01",
            "here used to work over in\x01",
            "diplomatic affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That'd explain why he's been\x01",
            "to the Empire and the Republic\x01",
            "so often, I suppose!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5D0A")

    ChrTalk(
        0xFE,
        (
            "I'm the kind of guy who only\x01",
            "needs to know the results of\x01",
            "the tournament matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd rather be here, quietly \x01",
            "reading than braving those \x01",
            "crowds at the Grand Arena.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5DC8")

    ChrTalk(
        0xFE,
        (
            "The articles in the Liberl \x01",
            "News have been pretty...\x01",
            "tame?...as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been no shock; no sensationalism.\x01",
            "Goes against everything I love about\x01",
            "Liberlism!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EAC")

    label("loc_5DC8")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "The articles in the Liberl \x01",
            "News have been pretty...\x01",
            "tame?...as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's almost all just a parade\x01",
            "of fluff pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been no shock; no sensationalism.\x01",
            "Goes against everything I love about\x01",
            "Liberlism!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EAC")

    Jump("loc_5F1D")

    label("loc_5EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5F1D")

    ChrTalk(
        0xFE,
        "This is a really relaxing place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kill many an hour here, just\x01",
            "sipping a cuppa and reading.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F1D")

    TalkEnd(0xFE)
    Return()

    # Function_14_56F2 end

    def Function_15_5F21(): pass

    label("Function_15_5F21")

    Call(2, 16)
    Return()

    # Function_15_5F21 end

    def Function_16_5F26(): pass

    label("Function_16_5F26")

    TalkBegin(0x16)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                            # 0
            "Shop\x01",                            # 1
            "[Chef's Curry] - 1000 mira\x01",      # 2
            "Leave\x01",                           # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FA1")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x62)
    OP_56(0x0)
    TalkEnd(0x16)
    Return()

    label("loc_5FA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6113")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_60D9")
    SubMira(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "You ate the \x07\x02",
            "Chef's Curry\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x3E8)
    OP_31(0x1, 0xFD, 0x3E8)
    OP_31(0x2, 0xFD, 0x3E8)
    OP_31(0x3, 0xFD, 0x3E8)
    OP_31(0x4, 0xFD, 0x3E8)
    OP_31(0x5, 0xFD, 0x3E8)
    OP_31(0x6, 0xFD, 0x3E8)
    OP_31(0x7, 0xFD, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_603B")
    Jump("loc_60CB")

    label("loc_603B")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Amazingly, through some sort of 'flavor osmosis,'\x01",
            "you've managed to piece out the recipe for \x07\x02",
            "Chef's\x01",
            "Curry\x07\x00",
            ", simply by tasting it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60CB")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_6101")

    label("loc_60D9")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_6101")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x16)
    Return()

    label("loc_6113")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_612D")
    FadeToBright(300, 0)
    TalkEnd(0x16)
    Return()

    label("loc_612D")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6853")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x212)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x213)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x214)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x215)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x216)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x217)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x218)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x219)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x21A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x21B)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x21C)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6853")

    ChrTalk(
        0x16,
        "Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...You guys wouldn't happen to\x01",
            "have the complete collection of\x01",
            "the 'Carnelia,' would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Wow, you do?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I'd always meant to buy every\x01",
            "new volume when it came out,\x01",
            "but never got around to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I was like, I can always read\x01",
            "the whole series when it's\x01",
            "finished, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "And now? It's pretty much\x01",
            "impossible to find the whole\x01",
            "set for sale in one place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "So I beg you, please... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Would you be willing to part\x01",
            "with yon collection of tomes?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_63AF"),
        (1, "loc_640A"),
        (SWITCH_DEFAULT, "loc_6475"),
    )


    label("loc_63AF")

    OP_A2(0x6F7)

    ChrTalk(
        0x16,
        (
            "You will? Really?! Ohmygod\x01",
            "ohmygodohmygodohmygodohmygod,\x01",
            "thank you sooooo much!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6475")

    label("loc_640A")


    ChrTalk(
        0x16,
        (
            "...Fine, then. I see how it is. I\x01",
            "won't forget this, I promise you!\x01",
            "SEARED INTO MY MEMORY, it is!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    label("loc_6475")


    ChrTalk(
        0x16,
        (
            "I work in diplomatic relations, and just \x01",
            "got back from assignment in the far east.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I've built up a pretty impressive\x01",
            "little collection of eastern goods,\x01",
            "too, if I do say so myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I'll let you have one of my\x01",
            "rarer items in exchange for\x01",
            "what I seek...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You're bracers, no? Hmm...\x01",
            "Let's see what I've got that\x01",
            "might catch your eye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...It's between these two. Which\x01",
            "one intrigues you more?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "[Mystic Stave]\x01",      # 0
            "[Twin Plovers]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6677"),
        (1, "loc_66F2"),
        (SWITCH_DEFAULT, "loc_6772"),
    )


    label("loc_6677")


    ChrTalk(
        0x101,
        "#001FOoh, this one is nice!\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received the \x07\x02",
            "Mystic Stave\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_6772")

    label("loc_66F2")


    ChrTalk(
        0x102,
        "#010FThank you. We'll take this.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x30, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received the \x07\x02",
            "Twin Plovers\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_6772")

    label("loc_6772")


    ChrTalk(
        0x16,
        (
            "Oh, very nice; very nice indeed.\x01",
            "It suits you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I've gotten a notification to\x01",
            "close shop early today, so \x01",
            "I have lots of time to read!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Thank you again.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x212, 1)
    OP_3F(0x213, 1)
    OP_3F(0x214, 1)
    OP_3F(0x215, 1)
    OP_3F(0x216, 1)
    OP_3F(0x217, 1)
    OP_3F(0x218, 1)
    OP_3F(0x219, 1)
    OP_3F(0x21A, 1)
    OP_3F(0x21B, 1)
    OP_3F(0x21C, 1)
    TalkEnd(0x16)
    Return()

    label("loc_6853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6907")

    ChrTalk(
        0x16,
        (
            "I didn't think that the Martial\x01",
            "Arts Competition would be used\x01",
            "as a cover for a coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "But Colonel Richard didn't\x01",
            "seem very content with his\x01",
            "position as it was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B8")

    label("loc_6907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6999")

    ChrTalk(
        0x16,
        (
            "The army seems to have really\x01",
            "tightened its hold on the\x01",
            "city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...but us? We have absolutely\x01",
            "no idea what's going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AA0")

    label("loc_6999")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "The Royal Army has pulled back,\x01",
            "and those soldiers in black\x01",
            "have taken over guard duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "And the citizens are none the\x01",
            "wiser as to what's happening\x01",
            "behind the scenes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "People get nervous when they\x01",
            "can tell something fishy is\x01",
            "starting to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AA0")

    Jump("loc_74B8")

    label("loc_6AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6B86")

    ChrTalk(
        0x16,
        (
            "Those Special Ops guys were\x01",
            "grumbling about some search\x01",
            "mission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I caught bits and pieces of it: 'Royal Guard,'\x01",
            "'citizen,' 'uncooperative'...and, er, some...\x01",
            "shall we say...more colorful metaphors?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C9D")

    label("loc_6B86")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "Those Special Ops guys were\x01",
            "grumbling about some search\x01",
            "mission...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I caught bits and pieces of it: 'Royal Guard,'\x01",
            "'citizen,' 'uncooperative'...and, er, some...\x01",
            "shall we say...more colorful metaphors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "What do they expect? The Royal\x01",
            "Guard is very well-respected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C9D")

    Jump("loc_74B8")

    label("loc_6CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6D09")

    ChrTalk(
        0x16,
        "So, the competition's done, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "A victory banquet in the castle...\x01",
            "lucky winners!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B8")

    label("loc_6D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6D53")

    ChrTalk(
        0x16,
        (
            "Would you like to try a cup\x01",
            "of our famous espresso?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC4")

    label("loc_6D53")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Would you like to try a cup\x01",
            "of our famous espresso?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "It'll wake you right up!\x02",
    )

    CloseMessageWindow()

    label("loc_6DC4")

    Jump("loc_74B8")

    label("loc_6DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6E8C")

    ChrTalk(
        0x16,
        (
            "Seems there's a curfew now.\x01",
            "Everyone off the streets by\x01",
            "nine o'clock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Not great for business, but it'll be\x01",
            "nice to close up early, put on some\x01",
            "music and do some reading.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F7D")

    label("loc_6E8C")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "Some Royal Army soldiers came\x01",
            "in here a while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Seems there's a curfew now.\x01",
            "Everyone off the streets by\x01",
            "nine o'clock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Not great for business, but it'll be\x01",
            "nice to close up early, put on some\x01",
            "music and do some reading.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F7D")

    Jump("loc_74B8")

    label("loc_6F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7096")

    ChrTalk(
        0x16,
        (
            "The West Block of Grancel\x01",
            "is overall one of the quieter\x01",
            "parts of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I put a lot of time into finding\x01",
            "the best location for this shop,\x01",
            "and this seemed the ideal choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Maybe it was my long tenure\x01",
            "in the castle, but I really\x01",
            "like peace and quiet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B8")

    label("loc_7096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_714D")

    ChrTalk(
        0x16,
        (
            "I had to travel all over the\x01",
            "world for my old job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Tried a whole lot of different\x01",
            "foods, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The culture of cuisine is some\x01",
            "really fascinating stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_714D")

    OP_A2(0xA)

    ChrTalk(
        0x16,
        (
            "I had to travel all over the\x01",
            "world for my old job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Tried a whole lot of different\x01",
            "foods, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "One of the curries I serve here\x01",
            "comes from a recipe I discovered\x01",
            "along the way, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The culture of cuisine is some\x01",
            "really fascinating stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7254")

    Jump("loc_74B8")

    label("loc_7257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7361")

    ChrTalk(
        0x16,
        (
            "Welcome, welcome! Please, make\x01",
            "yourselves at home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Home is what I was going for here.\x01",
            "I wanted to make this establishment\x01",
            "feel just like a person's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "So kick back and take a load\x01",
            "off. Bathe in the creature\x01",
            "comforts of this fine locale!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B8")

    label("loc_7361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7417")

    ChrTalk(
        0x16,
        (
            "The building next door is the\x01",
            "headquarters and main office\x01",
            "for the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Their reporters and editors\x01",
            "and such all come in here to\x01",
            "eat, or to take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B8")

    label("loc_7417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_74B8")

    ChrTalk(
        0x16,
        (
            "Hello, and welcome to the\x01",
            "Baral Coffee House.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We have almost any kind of\x01",
            "coffee you can imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Go right ahead and make\x01",
            "yourself at home!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74B8")

    TalkEnd(0x16)
    Return()

    # Function_16_5F26 end

    def Function_17_74BC(): pass

    label("Function_17_74BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_74C9")
    Jump("loc_765C")

    label("loc_74C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7527")

    ChrTalk(
        0xFE,
        (
            "Oooh, do you wanna go get\x01",
            "some ice cream sometime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I know the BEST place.\x02",
    )

    CloseMessageWindow()
    Jump("loc_765C")

    label("loc_7527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_756D")

    ChrTalk(
        0xFE,
        (
            "I have nothing to do until\x01",
            "the Birthday Celebration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_765C")

    label("loc_756D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7619")

    ChrTalk(
        0xFE,
        (
            "They so need to go back to one-\x01",
            "on-one fights for next year's\x01",
            "Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That way there can be an actual\x01",
            "Team Joshua for us to cheer on!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_765C")

    label("loc_7619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7623")
    Jump("loc_765C")

    label("loc_7623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_762D")
    Jump("loc_765C")

    label("loc_762D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7637")
    Jump("loc_765C")

    label("loc_7637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7641")
    Jump("loc_765C")

    label("loc_7641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_764B")
    Jump("loc_765C")

    label("loc_764B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7655")
    Jump("loc_765C")

    label("loc_7655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_765C")

    label("loc_765C")

    TalkEnd(0xFE)
    Return()

    # Function_17_74BC end

    def Function_18_7660(): pass

    label("Function_18_7660")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_766D")
    Jump("loc_77C0")

    label("loc_766D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_76A8")

    ChrTalk(
        0xFE,
        "I'm so bored...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anything you wanna do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_77C0")

    label("loc_76A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7741")

    ChrTalk(
        0xFE,
        (
            "Are they even HAVING the Birthday\x01",
            "Celebration this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the queen's gotten sick,\x01",
            "so maybe the party's gonna get\x01",
            "canceled...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C0")

    label("loc_7741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_777D")

    ChrTalk(
        0xFE,
        (
            "I can't believe Lorence lost!\x01",
            "Soooo laaaame!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77C0")

    label("loc_777D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7787")
    Jump("loc_77C0")

    label("loc_7787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7791")
    Jump("loc_77C0")

    label("loc_7791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_779B")
    Jump("loc_77C0")

    label("loc_779B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_77A5")
    Jump("loc_77C0")

    label("loc_77A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_77AF")
    Jump("loc_77C0")

    label("loc_77AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_77B9")
    Jump("loc_77C0")

    label("loc_77B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_77C0")

    label("loc_77C0")

    TalkEnd(0xFE)
    Return()

    # Function_18_7660 end

    def Function_19_77C4(): pass

    label("Function_19_77C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_77D1")
    Jump("loc_7895")

    label("loc_77D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_77DB")
    Jump("loc_7895")

    label("loc_77DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_77E5")
    Jump("loc_7895")

    label("loc_77E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7852")

    ChrTalk(
        0xFE,
        "Congratulations, Zane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew you were a shoe-in from\x01",
            "the very beginning. You rule,\x01",
            "man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7895")

    label("loc_7852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_785C")
    Jump("loc_7895")

    label("loc_785C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7866")
    Jump("loc_7895")

    label("loc_7866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7870")
    Jump("loc_7895")

    label("loc_7870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_787A")
    Jump("loc_7895")

    label("loc_787A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7884")
    Jump("loc_7895")

    label("loc_7884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_788E")
    Jump("loc_7895")

    label("loc_788E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7895")

    label("loc_7895")

    TalkEnd(0xFE)
    Return()

    # Function_19_77C4 end

    def Function_20_7899(): pass

    label("Function_20_7899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_78A6")
    Jump("loc_7A53")

    label("loc_78A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_78B0")
    Jump("loc_7A53")

    label("loc_78B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_78BA")
    Jump("loc_7A53")

    label("loc_78BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_794D")

    ChrTalk(
        0xFE,
        (
            "I met him when we were both\x01",
            "cheering for the same team\x01",
            "at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the match, we went\x01",
            "out for some drinks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A0D")

    label("loc_794D")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "I met him when we were both\x01",
            "cheering for the same team\x01",
            "at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the match, we went\x01",
            "out for some drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're going for an all-nighter\x01",
            "tonight! Whoo hoo hoo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A0D")

    Jump("loc_7A53")

    label("loc_7A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7A1A")
    Jump("loc_7A53")

    label("loc_7A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7A24")
    Jump("loc_7A53")

    label("loc_7A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7A2E")
    Jump("loc_7A53")

    label("loc_7A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7A38")
    Jump("loc_7A53")

    label("loc_7A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7A42")
    Jump("loc_7A53")

    label("loc_7A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7A4C")
    Jump("loc_7A53")

    label("loc_7A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7A53")

    label("loc_7A53")

    TalkEnd(0xFE)
    Return()

    # Function_20_7899 end

    def Function_21_7A57(): pass

    label("Function_21_7A57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7A64")
    Jump("loc_7F5E")

    label("loc_7A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7A6E")
    Jump("loc_7F5E")

    label("loc_7A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7A78")
    Jump("loc_7F5E")

    label("loc_7A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_7A82")
    Jump("loc_7F5E")

    label("loc_7A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7A8C")
    Jump("loc_7F5E")

    label("loc_7A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7CB7")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7AB5")
    SetChrSubChip(0xFE, 0)
    Jump("loc_7AE6")

    label("loc_7AB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7ACB")
    SetChrSubChip(0xFE, 2)
    Jump("loc_7AE6")

    label("loc_7ACB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7AE1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_7AE6")

    label("loc_7AE1")

    SetChrSubChip(0xFE, 0)

    label("loc_7AE6")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7BBD")

    ChrTalk(
        0xFE,
        (
            "#037FHeaven's tears! I couldn't \x01",
            "possibly drink with Schera any\x01",
            "harder or faster than I do.\x02\x03",
            "An evening of drinks with her is\x01",
            "a bacchanal beginning in Elysium\x01",
            "and ending in...well, vomit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CAF")

    label("loc_7BBD")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#037FHa, ha, ha, ha, ha!\x01",
            "...\x01",
            "...Are you for true?\x02\x03",
            "Heaven's tears! I couldn't \x01",
            "possibly drink with Schera any\x01",
            "harder or faster than I do.\x02\x03",
            "An evening of drinks with her is\x01",
            "a bacchanal beginning in Elysium\x01",
            "and ending in...well, vomit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CAF")

    SetChrSubChip(0xFE, 0)
    Jump("loc_7F5E")

    label("loc_7CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7CC1")
    Jump("loc_7F5E")

    label("loc_7CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7E80")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CEA")
    SetChrSubChip(0xFE, 0)
    Jump("loc_7D1B")

    label("loc_7CEA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D00")
    SetChrSubChip(0xFE, 2)
    Jump("loc_7D1B")

    label("loc_7D00")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D16")
    SetChrSubChip(0xFE, 1)
    Jump("loc_7D1B")

    label("loc_7D16")

    SetChrSubChip(0xFE, 0)

    label("loc_7D1B")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7DA8")

    ChrTalk(
        0xFE,
        (
            "#037FAaah, repast. Comfort for the\x01",
            "soul and fuel for the flesh.\x02\x03",
            "A profession worthy of song is\x01",
            "that of the chef!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E78")

    label("loc_7DA8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "#037FHa, ha, ha! Why, the night's\x01",
            "festivities have only just\x01",
            "begun!\x02\x03",
            "There are selge to go before\x01",
            "we sleep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509FWhere is he PUTTING all of\x01",
            "that food? Does he have, like,\x01",
            "a vortex in his belly?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E78")

    SetChrSubChip(0xFE, 0)
    Jump("loc_7F5E")

    label("loc_7E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7E8A")
    Jump("loc_7F5E")

    label("loc_7E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_7F54")

    ChrTalk(
        0xFE,
        (
            "#038FRed...orange...yellow...g-gold...\x01",
            "peri...p-periwinkle... Lookit all\x01",
            "the colors! Such bea-uty!\x02\x03",
            "I will be...with...you...\x01",
            "aaaaalways... I will...be...\x01",
            "true to you...aaaaalways...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F54")

    Jump("loc_7F5E")

    label("loc_7F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7F5E")

    label("loc_7F5E")

    TalkEnd(0xFE)
    Return()

    # Function_21_7A57 end

    def Function_22_7F62(): pass

    label("Function_22_7F62")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7F87")
    SetChrSubChip(0xFE, 1)
    Jump("loc_7FA2")

    label("loc_7F87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7F9D")
    SetChrSubChip(0xFE, 0)
    Jump("loc_7FA2")

    label("loc_7F9D")

    SetChrSubChip(0xFE, 2)

    label("loc_7FA2")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8053")

    ChrTalk(
        0x10,
        (
            "#070FI think I'll stick around a\x01",
            "little while longer.\x02\x03",
            "As long as I'm here, It would be\x01",
            "a waste to leave without testing\x01",
            "my mettle a bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8415")

    label("loc_8053")

    OP_A2(0x4)
    OP_A2(0x6EF)

    ChrTalk(
        0x10,
        "#073FHey, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FZane!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FSo, what's your next move?\x02\x03",
            "Back to the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070FI'm in no rush. There doesn't seem to be\x01",
            "any crisis in the Republic so bad that I\x01",
            "absolutely have to be there for it.\x02\x03",
            "Besides, this country is full\x01",
            "of fine opponents from your\x01",
            "Bracer Guild!\x02\x03",
            "#071FAs long as I'm here, it would be\x01",
            "a waste to leave without testing\x01",
            "my mettle a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F'Fine opponents?' Who'd you\x01",
            "have in mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#074FFor starters, you've got Agate...the\x01",
            "so-called 'Heavy Blade.' Not to mention \x01",
            "your 'Silver Streak,' Scherazard.\x02\x03",
            "And who could forget...\x02\x03",
            "#070F...the champions of this year's\x01",
            "Martial Arts Competition? Perhaps\x01",
            "the strongest of them all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FAww, Zane, that's so sweet!\x02\x03",
            "#006F...But don't think it means I'll\x01",
            "go any easier on you. And don't\x01",
            "you hold back on us! It's ON, man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F...She doesn't speak for both of us.\x01",
            "Feel free to hold back, if you'd like.\x01",
            "In fact, I might even prefer it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8415")

    Jump("loc_8617")

    label("loc_8418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8422")
    Jump("loc_8617")

    label("loc_8422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_842C")
    Jump("loc_8617")

    label("loc_842C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8436")
    Jump("loc_8617")

    label("loc_8436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8440")
    Jump("loc_8617")

    label("loc_8440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_84C0")

    ChrTalk(
        0x10,
        (
            "#078FThe final fight is tomorrow.\x02\x03",
            "Tonight, you need to go home,\x01",
            "eat a good meal, get plenty of\x01",
            "rest...and pray.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8617")

    label("loc_84C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_84CA")
    Jump("loc_8617")

    label("loc_84CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_85FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_850B")

    ChrTalk(
        0x10,
        (
            "#079F*hic* Woo you guysh like a\x01",
            "grink too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85F9")

    label("loc_850B")

    OP_A2(0x4)

    ChrTalk(
        0x10,
        (
            "#079FESHTELL! JOSHUWA!\x02\x03",
            "*hic* Woo you guysh like a\x01",
            "grink too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509FUh, we're underage, you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#076FWazzat? You guysh don wanna\x01",
            "grink...? Grink...heh. I said\x01",
            "grink instead of dring!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019FWell, this is just prime.\x02",
    )

    CloseMessageWindow()

    label("loc_85F9")

    Jump("loc_8617")

    label("loc_85FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8606")
    Jump("loc_8617")

    label("loc_8606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8610")
    Jump("loc_8617")

    label("loc_8610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8617")

    label("loc_8617")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_22_7F62 end

    def Function_23_8620(): pass

    label("Function_23_8620")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_87AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_86DF")

    ChrTalk(
        0xFE,
        (
            "I would never have guessed\x01",
            "Colonel Richard would plan\x01",
            "a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything he said in that magazine\x01",
            "interview... It was all just propaganda.\x01",
            "All just lies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87A9")

    label("loc_86DF")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "I would never have guessed\x01",
            "Colonel Richard would plan\x01",
            "a coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything he said in that magazine\x01",
            "interview... It was all just propaganda.\x01",
            "All just lies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm...utterly shocked.\x02",
    )

    CloseMessageWindow()

    label("loc_87A9")

    Jump("loc_92AF")

    label("loc_87AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8833")

    ChrTalk(
        0xFE,
        (
            "Randomly, the town is full of\x01",
            "soldiers in black now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What happened to the regular\x01",
            "troops? Why were they replaced?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_8833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_88DC")

    ChrTalk(
        0xFE,
        (
            "With the Birthday Celebration\x01",
            "so close, I hope there'll be\x01",
            "some news from the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I pray it's not that the\x01",
            "festivities have been canceled...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_88DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_89A2")

    ChrTalk(
        0xFE,
        (
            "The tournament may be over and done\x01",
            "with, but there are still just as many\x01",
            "soldiers on patrol...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They make me nervous, what \x01",
            "with all these rumors about\x01",
            "Her Highness being sick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_89A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8A32")

    ChrTalk(
        0xFE,
        (
            "There were so many soldiers in\x01",
            "the streets last night, I got\x01",
            "stopped at least four times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do I look THAT suspicious?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE2")

    label("loc_8A32")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "There were so many soldiers in\x01",
            "the streets last night, I got\x01",
            "stopped at least four times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do I look THAT suspicious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It makes me feel a bit self-conscious...\x02",
    )

    CloseMessageWindow()

    label("loc_8AE2")

    Jump("loc_92AF")

    label("loc_8AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8B82")

    ChrTalk(
        0xFE,
        (
            "Ever since that exclusive in \x01",
            "the Liberl News, Colonel \x01",
            "Richard's been quite popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's won over a lot of people,\x01",
            "both young and old.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_8B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8C0D")

    ChrTalk(
        0xFE,
        (
            "The Imperial breakfast at\x01",
            "Baral Coffee House is quite\x01",
            "delicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but I actually prefer the\x01",
            "Liberl breakfast here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_8C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8CD3")

    ChrTalk(
        0xFE,
        (
            "So man, was I ever taken aback\x01",
            "when those Sky Bandits from Bose\x01",
            "showed up in the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it really okay to have\x01",
            "convicted criminals serving\x01",
            "in a sporting event...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DDC")

    label("loc_8CD3")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "So man, was I ever taken aback\x01",
            "when those Sky Bandits from Bose\x01",
            "showed up in the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were more skilled than I\x01",
            "would've expected, though, I\x01",
            "have to admit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it really okay to have\x01",
            "convicted criminals serving\x01",
            "in a sporting event...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DDC")

    Jump("loc_92AF")

    label("loc_8DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8EA6")

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "was originally held to show\x01",
            "off new military techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Queen Alicia took the \x01",
            "throne, she opened it to the\x01",
            "public as a spectator event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA8")

    label("loc_8EA6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "The Martial Arts Competition\x01",
            "was originally held to show\x01",
            "off new military techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Queen Alicia took the \x01",
            "throne, she opened it to the\x01",
            "public as a spectator event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And shortly thereafter, the\x01",
            "public was also invited to\x01",
            "participate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FA8")

    Jump("loc_92AF")

    label("loc_8FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_900A")

    ChrTalk(
        0xFE,
        (
            "*GULP* Don't surprise me like\x01",
            "that! I almost choked on my\x01",
            "forkful of spaghetti!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_900A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_90AF")

    ChrTalk(
        0xFE,
        (
            "This is the first year the\x01",
            "tournament's been fought with\x01",
            "teams, rather than one-on-one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly the duke's idea...\x01",
            "and not a bad one, really!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_90AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_92AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9177")

    ChrTalk(
        0xFE,
        (
            "The Royal Guard is under the magnifying\x01",
            "glass right now, what with all those\x01",
            "allegations of terrorist involvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure seems like a lot's been\x01",
            "going down, these days...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92AF")

    label("loc_9177")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "The Royal Guard is under the magnifying\x01",
            "glass right now, what with all those\x01",
            "allegations of terrorist involvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First the Sky Bandits in Bose, then the\x01",
            "corrupt mayor of Ruan, and now that business\x01",
            "with the orbal blackout in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure seems like a lot's been\x01",
            "going down, these days...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92AF")

    TalkEnd(0xFE)
    Return()

    # Function_23_8620 end

    def Function_24_92B3(): pass

    label("Function_24_92B3")

    Call(2, 25)
    Return()

    # Function_24_92B3 end

    def Function_25_92B8(): pass

    label("Function_25_92B8")

    TalkBegin(0xE)
    OP_A2(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_92C8")
    Jump("loc_92D2")

    label("loc_92C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_92D2")
    OP_A3(0x19)

    label("loc_92D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_94D6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                             # 0
            "Shop\x01",                             # 1
            "[Bouillabaisse] - 1000 mira\x01",      # 2
            "Leave\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9352")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x61)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_9352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94BC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9482")
    SubMira(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Partook of the \x07\x02",
            "Bouillabaisse\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x3E8)
    OP_31(0x1, 0xFD, 0x3E8)
    OP_31(0x2, 0xFD, 0x3E8)
    OP_31(0x3, 0xFD, 0x3E8)
    OP_31(0x4, 0xFD, 0x3E8)
    OP_31(0x5, 0xFD, 0x3E8)
    OP_31(0x6, 0xFD, 0x3E8)
    OP_31(0x7, 0xFD, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9474")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_93F0")
    Jump("loc_9474")

    label("loc_93F0")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Somehow, the act of eating it fired off\x01",
            "long-hidden neurons in the brain, teaching\x01",
            "you the recipe for \x07\x02",
            "Bouillabaisse\x07\x00",
            "!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9474")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_94AA")

    label("loc_9482")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_94AA")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_94BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94D6")
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    label("loc_94D6")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9553")

    ChrTalk(
        0xE,
        (
            "A lot's been happening lately,\x01",
            "but I think things are finally\x01",
            "starting to get back to normal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_962D")

    label("loc_9553")

    OP_A2(0x2)

    ChrTalk(
        0xE,
        (
            "Seeing the queen healthy \x01",
            "was a real comfort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "All that suspicion from the \x01",
            "Royal Guardsmen was unfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A lot's been happening lately,\x01",
            "but I think things are finally\x01",
            "starting to get back to normal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_962D")

    Jump("loc_9DDF")

    label("loc_9630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_96AB")

    ChrTalk(
        0xE,
        (
            "These soldiers don't seem to\x01",
            "understand what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "And we certainly don't know\x01",
            "what's happening!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_96AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_974B")

    ChrTalk(
        0xE,
        (
            "The tournament's over, but the\x01",
            "city's still crawling with\x01",
            "soldiers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Were the Royal Guardsmen really\x01",
            "the ones responsible for the\x01",
            "attack?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_974B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_97CE")

    ChrTalk(
        0xE,
        (
            "Seems like Olivier's not coming\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wanted to congratulate him\x01",
            "on winning the Martial Arts\x01",
            "Competition...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_97CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_98A1")

    ChrTalk(
        0xE,
        (
            "Maaan, I wish I could go to the\x01",
            "arena and watch the matches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But in this line of work, I'm at my busiest\x01",
            "when other people are out and about, having\x01",
            "the time of their lives! It's not fair!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_98A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_996B")

    ChrTalk(
        0xE,
        (
            "Some soldiers came by earlier,\x01",
            "and told me I had to close my\x01",
            "store at nine o'clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Apparently, there's a curfew now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What bar ever made any money\x01",
            "closing their doors at nine?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_996B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9A09")

    ChrTalk(
        0xE,
        "Aren't you in today's matches?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Since the Royal Guardsmen aren't in\x01",
            "the tournament, I might as well cheer\x01",
            "for you guys. Rah, rah, go team!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_9A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9A5D")

    ChrTalk(
        0xE,
        (
            "So, there we have it. Day one,\x01",
            "at an end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I wonder how it went?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_9A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9AB9")

    ChrTalk(
        0xE,
        "Are you all Olivier's friends?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hope the match goes well for you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BEA")

    label("loc_9AB9")

    OP_A2(0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x104, 0)

    ChrTalk(
        0xE,
        (
            "Ah, Olivier! Is your head\x01",
            "feeling any better today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa ha ha! But of course!\x02\x03",
            "#030FTrivialities such as head wounds mean nothing\x01",
            "to me, as long as there exists a spark of love\x01",
            "to fuel the towering inferno of my heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...So, that's a yes, then.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 180, 400)

    label("loc_9BEA")

    Jump("loc_9DDF")

    label("loc_9BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_9CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_9C6C")

    ChrTalk(
        0xE,
        (
            "Well, if it isn't our prodigal\x01",
            "musician, Olivier!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Been striking out with the women\x01",
            "again, I assume?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CBC")

    label("loc_9C6C")


    ChrTalk(
        0xE,
        (
            "Well, I guess the prelims are\x01",
            "over, given the swarm of people\x01",
            "coming in...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CBC")

    Jump("loc_9DDF")

    label("loc_9CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9D33")

    ChrTalk(
        0xE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen are terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's got to be some kind of\x01",
            "mistake!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DDF")

    label("loc_9D33")

    OP_A2(0x2)

    ChrTalk(
        0xE,
        (
            "I can't believe the Royal\x01",
            "Guardsmen are terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Every one of them that comes in\x01",
            "here is an upstanding young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's got to be some kind of\x01",
            "mistake!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DDF")

    TalkEnd(0xE)
    Return()

    # Function_25_92B8 end

    def Function_26_9DE3(): pass

    label("Function_26_9DE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A03B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9E95")

    ChrTalk(
        0xFE,
        (
            "#840FBased on your performance\x01",
            "I'd say you two are already\x01",
            "fine, full-fledged bracers.\x02\x03",
            "But never forget, these are only\x01",
            "the first steps in your career!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A03B")

    label("loc_9E95")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#840FYou did a remarkable job.\x02\x03",
            "Based on your performance\x01",
            "I'd say you two are already\x01",
            "fine, full-fledged bracers.\x02\x03",
            "But never forget, these are only\x01",
            "the first steps in your career!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FThank you, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FSo Kurt, are you feeling any better?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#841FI'm fine. Just fine!\x02\x03",
            "#845FI remember just about everything, EXCEPT\x01",
            "the identity of the bastard who erased my\x01",
            "memories. That's the only missing piece!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A03B")

    TalkEnd(0xFE)
    Return()

    # Function_26_9DE3 end

    def Function_27_A03F(): pass

    label("Function_27_A03F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A51A")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 4660, 0, 540, 90)
    SetChrPos(0x102, 4870, 0, -630, 45)
    SetChrPos(0x108, 3570, 0, 140, 90)
    SetChrSubChip(0xC, 0)
    TurnDirection(0xC, 0x108, 0)
    OP_A2(0x64A)
    OP_28(0x4B, 0x1, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0C6")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_A0C6")

    OP_6D(5350, 0, 360, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#006FHey, it's Grant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#820FWell, well. If it isn't the\x01",
            "big, bad champions!\x02\x03",
            "I hear you guys spent the night at\x01",
            "the castle. Frankly, I'm surprised\x01",
            "to see you back so early!\x02\x03",
            "Did you eat anything good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FYeah, we did...but that's not\x01",
            "what we're here to talk about!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#820FOh? Something on your mind?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained the situation and the queen's request to Grant.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xC,
        (
            "#822F...Holy crap! You're not pulling\x01",
            "my leg, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072FWe are not. Every word is true.\x02\x03",
            "I'd stake my reputation on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#824FIf Zane the Immovable is moved\x01",
            "by this, that's all the proof\x01",
            "I need.\x02\x03",
            "#823FI'll do whatever I can to help.\x02\x03",
            "#822FYou can count on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FThanks, Grant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe'll all be meeting at the guildhouse\x01",
            "to plan our strategy, as soon as\x01",
            "possible.\x02\x03",
            "So if you'd please, head over\x01",
            "there when you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#822FUnderstood. Go well, friends.\x01",
            "I'll catch up with you there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A475():

        label("loc_A475")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A475")

    QueueWorkItem2(0x101, 1, lambda_A475)

    def lambda_A486():

        label("loc_A486")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A486")

    QueueWorkItem2(0x102, 1, lambda_A486)

    def lambda_A497():

        label("loc_A497")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A497")

    QueueWorkItem2(0x108, 1, lambda_A497)
    OP_8E(0xC, 0x15FE, 0x0, 0xFFFFFA42, 0xFA0, 0x0)
    OP_8E(0xC, 0x758, 0x0, 0xFFFFFA38, 0xFA0, 0x0)
    OP_8E(0xC, 0x2C6, 0x0, 0xFFFFEA8E, 0xFA0, 0x0)

    def lambda_A4E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A4E4)
    OP_8E(0xC, 0x2C6, 0xFFFFFF06, 0xFFFFE2D2, 0xFA0, 0x0)
    SetChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)
    Jump("loc_AA34")

    label("loc_A51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A562")

    ChrTalk(
        0xFE,
        (
            "#820FGuess this makes us partners.\x02\x03",
            "Here's to us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A70D")

    label("loc_A562")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "#821FWelcome back, brave heroes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGrant...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#821FYou guys were amazing.\x02\x03",
            "Better than any other junior\x01",
            "bracers I've met, that's for\x01",
            "damn sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FYay us!\x02\x03",
            "#000FWe couldn't have done it without\x01",
            "everyone's help, though.\x02\x03",
            "#505FI mean, my dad ended up saving\x01",
            "my butt in there, so I'm not\x01",
            "exactly solo heroine material!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#820FYou guys are something else.\x02\x03",
            "Guess this makes us partners.\x02\x03",
            "Here's to us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A70D")

    Jump("loc_AA34")

    label("loc_A710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A71A")
    Jump("loc_AA34")

    label("loc_A71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A724")
    Jump("loc_AA34")

    label("loc_A724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A84D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A77C")

    ChrTalk(
        0xFE,
        (
            "#821FHey, where'd the blondie go?\x02\x03",
            "He was quite the sharpshooter!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84A")

    label("loc_A77C")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#821FLooks like the band's back\x01",
            "together again.\x02\x03",
            "Let's see that dance that\x01",
            "won you the tournament!\x02\x03",
            "Of course, I'd've preferred to win\x01",
            "it myself...but I'm not bitter!\x01",
            "I was beaten, fair and square!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A84A")

    Jump("loc_AA34")

    label("loc_A84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A857")
    Jump("loc_AA34")

    label("loc_A857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A861")
    Jump("loc_AA34")

    label("loc_A861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A86B")
    Jump("loc_AA34")

    label("loc_A86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A875")
    Jump("loc_AA34")

    label("loc_A875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_AA23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A8C0")

    ChrTalk(
        0xFE,
        (
            "Bracers gotta eat and bracers\x01",
            "gotta sleep, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA20")

    label("loc_A8C0")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "Hey! Had breakfast yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHey there, Grant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bracers gotta eat and bracers\x01",
            "gotta sleep, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hope that was drilled into your\x01",
            "head at the guild-- a lack of\x01",
            "sleep impairs one's judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIronically enough, that was\x01",
            "the one lesson Estelle DIDN'T\x01",
            "sleep through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FThat's not true! I was\x01",
            "awake for plen--HEY!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA20")

    Jump("loc_AA34")

    label("loc_AA23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_AA2D")
    Jump("loc_AA34")

    label("loc_AA2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_AA34")

    label("loc_AA34")

    TalkEnd(0xC)
    Return()

    # Function_27_A03F end

    def Function_28_AA38(): pass

    label("Function_28_AA38")

    TalkBegin(0x20)

    ChrTalk(
        0xFE,
        "What the heck happened to him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He get kicked by a Gourd Boar\x01",
            "or something?!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x20)
    Return()

    # Function_28_AA38 end

    SaveToFile()

Try(main)
