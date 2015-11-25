from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Louise',                               # 9
        'Yuriel',                               # 10
        'Rutherford',                           # 11
        'Sotiria',                              # 12
        'Muriel',                               # 13
        'Randall',                              # 14
        'Stain',                                # 15
        'Elise',                                # 16
        'Vince',                                # 17
        'Ursus',                                # 18
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01200 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01270 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01200P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01270P._CP',             # 09
    )

    DeclNpc(
        X                   = -1900,
        Z                   = 4000,
        Y                   = 23230,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 25860,
        Direction           = 263,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -3290,
        Z                   = 0,
        Y                   = 2790,
        Direction           = 224,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 23740,
        Z                   = 0,
        Y                   = 1040,
        Direction           = 142,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 23410,
        Z                   = 150,
        Y                   = 740,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 27780,
        Z                   = 0,
        Y                   = 25700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    ScpFunction(
        "Function_0_23A",          # 00, 0
        "Function_1_446",          # 01, 1
        "Function_2_468",          # 02, 2
        "Function_3_47E",          # 03, 3
        "Function_4_4A2",          # 04, 4
        "Function_5_4C6",          # 05, 5
        "Function_6_4EA",          # 06, 6
        "Function_7_50E",          # 07, 7
        "Function_8_532",          # 08, 8
        "Function_9_136A",         # 09, 9
        "Function_10_1F77",        # 0A, 10
        "Function_11_2B4F",        # 0B, 11
        "Function_12_3342",        # 0C, 12
        "Function_13_3B84",        # 0D, 13
        "Function_14_3D04",        # 0E, 14
        "Function_15_4A0B",        # 0F, 15
        "Function_16_4BDB",        # 10, 16
        "Function_17_4E3B",        # 11, 17
    )


    def Function_0_23A(): pass

    label("Function_0_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_270")
    SetChrFlags(0xA, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xC, 21930, 0, 2180, 138)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_445")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A6")
    SetChrFlags(0xA, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xC, 21930, 0, 2180, 138)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_445")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2BF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_445")

    label("loc_2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28100, 0, 22440, 0)
    Jump("loc_445")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_38A")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1800, 0, 21070, 263)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrPos(0x8, -1720, 0, 24500, 275)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4050, 0, -3180, 348)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 26330, 4000, 25200, 76)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 27970, 4000, 25230, 275)
    SetChrPos(0xA, 21330, 0, 3950, 352)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Jump("loc_445")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    SetChrPos(0xB, -4740, 0, 2840, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -3450, 0, 2830, 270)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jump("loc_445")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_445")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_420")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -1800, 0, 21070, 263)
    Jump("loc_445")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_434")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_445")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_445")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_445")

    Return()

    # Function_0_23A end

    def Function_1_446(): pass

    label("Function_1_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E")
    OP_B1("t3110_y")
    Jump("loc_467")

    label("loc_45E")

    OP_B1("t3110_n")

    label("loc_467")

    Return()

    # Function_1_446 end

    def Function_2_468(): pass

    label("Function_2_468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_468")

    label("loc_47D")

    Return()

    # Function_2_468 end

    def Function_3_47E(): pass

    label("Function_3_47E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A1")
    OP_8D(0xFE, 290, 22470, 1800, 25300, 2000)
    Jump("Function_3_47E")

    label("loc_4A1")

    Return()

    # Function_3_47E end

    def Function_4_4A2(): pass

    label("Function_4_4A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C5")
    OP_8D(0xFE, -1920, 1860, 2170, -2770, 2000)
    Jump("Function_4_4A2")

    label("loc_4C5")

    Return()

    # Function_4_4A2 end

    def Function_5_4C6(): pass

    label("Function_5_4C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E9")
    OP_8D(0xFE, -4730, 3760, -1290, 1770, 2000)
    Jump("Function_5_4C6")

    label("loc_4E9")

    Return()

    # Function_5_4C6 end

    def Function_6_4EA(): pass

    label("Function_6_4EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50D")
    OP_8D(0xFE, 20960, 3050, 25510, -530, 2000)
    Jump("Function_6_4EA")

    label("loc_50D")

    Return()

    # Function_6_4EA end

    def Function_7_50E(): pass

    label("Function_7_50E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531")
    OP_8D(0xFE, -5320, 520, -1440, 630, 2000)
    Jump("Function_7_50E")

    label("loc_531")

    Return()

    # Function_7_50E end

    def Function_8_532(): pass

    label("Function_8_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_59C")
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        "Ah, what a wonderful morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing like a hard day's work\x01",
            "to help you sleep!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_73B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_66F")

    ChrTalk(
        0xFE,
        (
            "I can't BELIEVE I'm really taking\x01",
            "part in the construction of an\x01",
            "actual orbal engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gonna have to come up with\x01",
            "good input and leave my mark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nope. No time for soup now!\x02",
    )

    CloseMessageWindow()
    Jump("loc_735")

    label("loc_66F")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "*sigh* I can't believe I was\x01",
            "selected to be part of the\x01",
            "Orbal Engine Project...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and I can't come up with\x01",
            "any ideas to contribute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No use moaning about it. \x01",
            "Time to get working.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735")

    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7C3")
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        "Sure seems...busy...out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...What am I doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is no time to rubberneck!\x01",
            "Gotta get to work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87E")

    label("loc_7C3")

    OP_A2(0x2)
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        "Gotta readjust the barrel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know how much more\x01",
            "of this I can take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, Lady Aidios. PLEASE \x01",
            "answer my prayer and send\x01",
            "me some airship-related work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87E")

    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_93A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "Okay...the paperwork's in order,\x01",
            "and my sister's with Ursus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Guess it's time to go to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yep. Not feeling the old\x01",
            "motivation today. At all.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_93A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_BB5")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9E3")

    ChrTalk(
        0xFE,
        (
            "I've never even HEARD of an\x01",
            "orbment stopping, let alone\x01",
            "seen one actually stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll bet the Central Factory's a\x01",
            "madhouse right about now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAF")

    label("loc_9E3")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "Oh! Good morning, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last night was some crazy\x01",
            "stuff, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#562FUuuugggh...\x02\x03",
            "Go easy on me today, okay?\x02\x03",
            "I ended up spending all night\x01",
            "working with Chief Murdock\x01",
            "after everything calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still though...that's the first\x01",
            "time I've ever heard of an \x01",
            "orbment shutting down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet Wilmont in Operations is\x01",
            "completely losing his mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The orbal calculator had to\x01",
            "have just been blown out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAF")

    TalkEnd(0x8)
    Jump("loc_1369")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CB3")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "Let's see here...\x01",
            "'Septium Optic Annals'...\x01",
            "'Septium Optic Annals'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Where did I put that book?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't take employment at the Central\x01",
            "Factory to make orbal guns. *grumble*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Part of working for the man...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_117D")

    label("loc_CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CE")
    OP_A2(0x573)
    OP_A2(0x2)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF4")

    ChrTalk(
        0xFE,
        (
            "Hmm? Tita?\x01",
            "Something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2F")

    label("loc_CF4")


    ChrTalk(
        0xFE,
        "Hold on...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "Tita, what are you doing here?\x02",
    )

    CloseMessageWindow()

    label("loc_D2F")


    ChrTalk(
        0x107,
        (
            "#064FLouise! Aren't you supposed\x01",
            "to be working in the Design\x01",
            "Room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, but first they wanted me to\x01",
            "finish calibrating the orbal guns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you showing these two bracers\x01",
            "the ropes or something, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061FYes, I am. We're on our way\x01",
            "back to my house now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Speaking of your house, Tita,\x01",
            "it sure has been quiet around\x01",
            "there as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No gas leaks or explosions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F(...Ex-explosions?!)\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#560FI wouldn't go so far as to say\x01",
            "'explosions,' Louise.\x02\x03",
            "Just a little flying glass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F'Just a little FLYING GLASS?!'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019FHow...exciting?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0xFE,
        (
            "Whatever. I want to see the\x01",
            "professor's newest inventions\x01",
            "as much as anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't stop your tests due to worries\x01",
            "about collateral damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560FUh, okay. Thank you...?\x02\x03",
            "#061FGood luck on the production of\x01",
            "the new orbal guns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many thanks. Nose to the ol'\x01",
            "grindstone and all that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_117D")

    label("loc_10CE")

    TalkBegin(0x8)
    OP_A2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(
        0xFE,
        (
            "Hmm? Tita? Still not finished\x01",
            "showing those guests around?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117A")

    label("loc_1123")


    ChrTalk(
        0xFE,
        "Hold on...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "Hmm? Tita? Still not finished\x01",
            "showing those guests around?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117A")

    TalkEnd(0x8)

    label("loc_117D")

    Jump("loc_1369")

    label("loc_1180")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1237")
    OP_A2(0x0)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0xFE, 400)

    ChrTalk(
        0x9,
        "Hurry up and make the bed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You're holding up my nap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, okay. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm a little busy right now.\x01",
            "I'll talk to you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    Jump("loc_135F")

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D6")
    OP_A2(0x1)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0xFE, 400)

    ChrTalk(
        0x9,
        "Louise! Are you LISTENING?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "MAKE! THE! BED!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(
        0xFE,
        "Will you shut up a second?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm looking for a book!\x02",
    )

    OP_8C(0xFE, 254, 400)
    CloseMessageWindow()
    OP_4B(0x9, 255)
    Jump("loc_135F")

    label("loc_12D6")


    ChrTalk(
        0xFE,
        (
            "Why did I get stuck with such\x01",
            "a mouthy brat of a sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd trade her for Professor Russell's\x01",
            "granddaughter Tita in a second.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135F")

    OP_8C(0x9, 263, 0)
    TalkEnd(0x8)

    label("loc_1369")

    Return()

    # Function_8_532 end

    def Function_9_136A(): pass

    label("Function_9_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_144E")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DD")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "There was this huge book on\x01",
            "the bed when I woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It made it so hard to sleep.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1448")

    label("loc_13DD")


    ChrTalk(
        0xFE,
        (
            "Why can't my sister clean up\x01",
            "her stuff properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a bookcase right there\x01",
            "next to the bed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1448")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_151C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AD")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "I swear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess she just doesn't want\x01",
            "to keep things clean.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1516")

    label("loc_14AD")


    ChrTalk(
        0xFE,
        (
            "Oh well. I'll just get Ursus to\x01",
            "do it for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's his job right? \x01",
            "As my sister's boyfriend?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1516")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_166B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F2")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "My sister was worrying about\x01",
            "her job last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But she seemed to figure something\x01",
            "out when she was drinking the soup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe there's something in it\x01",
            "that jogs your brain...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1665")

    label("loc_15F2")


    ChrTalk(
        0xFE,
        (
            "I wonder if there's something\x01",
            "in the soup that helps your\x01",
            "brain work better...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll ask Sister Kiera...\x02",
    )

    CloseMessageWindow()

    label("loc_1665")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1789")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1717")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "My sister seems really motivated\x01",
            "about work lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, her boyfriend comes over,\x01",
            "and still it's all work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Kinda creepy, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1783")

    label("loc_1717")


    ChrTalk(
        0xFE,
        (
            "Instead of moaning all the time,\x01",
            "she should rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She should at least have some\x01",
            "of Ursus' soup...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1783")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_19B8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191D")
    OP_A2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1845")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "I heard there was an accident\x01",
            "at the factory or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063FAh...\x02\x03",
            "Y-Yes. I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's good to hear.\x02",
    )

    CloseMessageWindow()
    Jump("loc_191A")

    label("loc_1845")


    ChrTalk(
        0xFE,
        (
            "I heard there was an accident\x01",
            "at the factory or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My sister hasn't been going to\x01",
            "the factory for a while, so she\x01",
            "didn't get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad she was safe, but it's\x01",
            "kind of embarrassing, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191A")

    Jump("loc_19B2")

    label("loc_191D")


    ChrTalk(
        0xFE,
        (
            "My sister hasn't been going\x01",
            "to the factory for a while, so\x01",
            "she didn't get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad she was safe, but it's\x01",
            "kind of embarrassing, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B2")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CC")
    SetChrFlags(0xFE, 0x10)

    label("loc_19CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A72")
    OP_A2(0x3)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x11, 400)

    ChrTalk(
        0xFE,
        "Hey, Ursus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you finish making lunch,\x01",
            "can you make the bed for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Louise didn't do it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 400)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_1AD7")

    label("loc_1A72")


    ChrTalk(
        0xFE,
        "Ursus is my sister's boyfriend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's dating HER, of all people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel sorry for him.\x02",
    )

    CloseMessageWindow()

    label("loc_1AD7")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1B61")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Louise, shouldn't you be leaving\x01",
            "for work now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can still make it before\x01",
            "everybody breaks for lunch...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1CC0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C76")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "*yawn* Good morning.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "Oh, hi, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061FHi, Yuriel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you have work today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060FI sure do.\x02\x03",
            "I'm helping my granddad today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You seem really busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good for you though. You're the\x01",
            "definition of the tireless mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBA")

    label("loc_1C76")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "You seem so busy, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Not like my sister at all.\x02",
    )

    CloseMessageWindow()

    label("loc_1CBA")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1EAF")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 4)), scpexpr(EXPR_END)), "loc_1D3A")

    ChrTalk(
        0xFE,
        (
            "I mean, look at this place!\x01",
            "It's like she doesn't even\x01",
            "know how to clean up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's so lazy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EA9")

    label("loc_1D3A")

    OP_A2(0x574)

    ChrTalk(
        0xFE,
        "Hi, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FYuriel! Finished with school?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't be silly, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sunday school isn't today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065FOh...\x02\x03",
            "It wasn't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tita, dear, you need to rest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And come to school sometime, too.\x01",
            "Everybody wants to see you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067FOkay.\x01",
            "I've just been real busy lately.\x02\x03",
            "I'll come back as soon as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's a promise, right? \x02",
    )

    CloseMessageWindow()

    label("loc_1EA9")

    TalkEnd(0xFE)
    Jump("loc_1F76")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBC")
    SetChrFlags(0xFE, 0x10)

    label("loc_1EBC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F37")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x8, 400)

    ChrTalk(
        0xFE,
        "Louise, why are you so lazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurry up and make the bed!\x01",
            "I can't take my nap!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 400)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_1F73")

    label("loc_1F37")


    ChrTalk(
        0xFE,
        "My sister is so LAZY.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I mean, look at this place.\x02",
    )

    CloseMessageWindow()

    label("loc_1F73")

    TalkEnd(0x9)

    label("loc_1F76")

    Return()

    # Function_9_136A end

    def Function_10_1F77(): pass

    label("Function_10_1F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2014")

    ChrTalk(
        0xFE,
        (
            "You know, I haven't seen Professor\x01",
            "Russell lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's probably locked himself\x01",
            "in his lab to finish some new\x01",
            "invention again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2190")

    label("loc_2014")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "I received notice from Hugo that they've\x01",
            "decided to add a new member to the orbal\x01",
            "engine research team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently it's a young woman, but it's\x01",
            "not like age and gender actually matter\x01",
            "so long as you've got the skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, just look at Professor\x01",
            "Russell. Textbook case of 'no\x01",
            "age discrimination' there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, I haven't seen\x01",
            "Professor Russell lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2190")

    Jump("loc_2B4B")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_22B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2237")

    ChrTalk(
        0xFE,
        (
            "Times like this remind me of\x01",
            "that seaside vacation I took.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I wouldn't give to be in\x01",
            "that little casino bar, feet up\x01",
            "and relaxing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22AE")

    label("loc_2237")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Okay, these contracts all seem\x01",
            "to be in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It always seems that all the work\x01",
            "comes in when I'm alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22AE")

    Jump("loc_2B4B")

    label("loc_22B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2368")

    ChrTalk(
        0xFE,
        "Items stolen...one orbal calculator.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Lot of good stealing THAT is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Professor Russell's the only\x01",
            "person around who'd have \x01",
            "any idea how to even use it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246E")

    label("loc_2368")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "I heard about the incident at\x01",
            "the Central Factory. What a\x01",
            "surprise that was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No injuries, thank goodness,\x01",
            "but they did manage to make\x01",
            "off with an orbal calculator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't tell you what the\x01",
            "perpetrator's motivation\x01",
            "could've been, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246E")

    Jump("loc_2B4B")

    label("loc_2471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_260D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2500")

    ChrTalk(
        0xFE,
        (
            "I tell you what, though, the whole\x01",
            "town sure is up in arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of mess did the\x01",
            "professor get into this time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260A")

    label("loc_2500")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Yesterday I met a young merchant from\x01",
            "the Calvard Republic in the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he was an orbment merchant.\x01",
            "I'd like to talk to him again sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our country will no doubt expand \x01",
            "trade with the Republic. It'd be\x01",
            "good to get in early on it.  \x02",
        )
    )

    CloseMessageWindow()

    label("loc_260A")

    Jump("loc_2B4B")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_27BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(
        0xFE,
        (
            "My wife Sotiria hates the\x01",
            "big airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After what she saw last night\x01",
            "she's probably scarred forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a total mess it's turned\x01",
            "out to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BA")

    label("loc_26BC")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "What would happen to an airship\x01",
            "if its orbments gave out like they\x01",
            "did last night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, I hope my wife doesn't\x01",
            "hear me talking like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She hates airships enough\x01",
            "as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She'll probably never set foot\x01",
            "on one after last night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27BA")

    Jump("loc_2B4B")

    label("loc_27BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_294D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2846")

    ChrTalk(
        0xFE,
        "It was pretty scary yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope anybody looking to buy\x01",
            "an airship doesn't get a bad\x01",
            "impression from it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294A")

    label("loc_2846")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "My job is selling airships, \x01",
            "but I have to admit yesterday\x01",
            "was a pretty scary scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something like that were to\x01",
            "happen on an airship that was\x01",
            "in mid-flight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope anybody looking to buy\x01",
            "an airship doesn't get a bad\x01",
            "impression from it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294A")

    Jump("loc_2B4B")

    label("loc_294D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_298C")

    ChrTalk(
        0xFE,
        (
            "Okay, break time's finished.\x01",
            "Back to work I go!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4B")

    label("loc_298C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A98")

    ChrTalk(
        0xFE,
        "My job is selling airships.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the Arseille was being built,\x01",
            "both the factory and the Royal\x01",
            "Guard came to me for advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the test flight they stopped\x01",
            "contact with me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it seems like everything\x01",
            "turned out all right. I'm glad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4B")

    label("loc_2A98")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "I just got back from Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that the Arseille was\x01",
            "seen flying around Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a shame, if I had stayed a\x01",
            "little longer I bet I could've seen\x01",
            "it myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F77 end

    def Function_11_2B4F(): pass

    label("Function_11_2B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2C51")

    ChrTalk(
        0xFE,
        (
            "My little Muriel talks about\x01",
            "working at the Central Factory\x01",
            "when she grows up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But she says she wants to be\x01",
            "one of the receptionists there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was a little relieved, to tell the\x01",
            "truth. I'm afraid she isn't...cut\x01",
            "out for science.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2D61")

    ChrTalk(
        0xFE,
        (
            "After the incident, my little Muriel\x01",
            "suddenly decided she'd like to work\x01",
            "at the factory. Can you believe it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, if she really wants to\x01",
            "work there I'll speak with her\x01",
            "grandfather about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but I don't really think it'd\x01",
            "do very much good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_2D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2DCE")

    ChrTalk(
        0xFE,
        (
            "Since my grandfather was at the\x01",
            "bar, he says he didn't hear about\x01",
            "the incident at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E5E")

    label("loc_2DCE")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "My grandfather's at home now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the bar all day and back\x01",
            "home by dark...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Usually it's 'bar all night and\x01",
            "home by morning'...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5E")

    Jump("loc_333E")

    label("loc_2E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2EB1")

    ChrTalk(
        0xFE,
        "Attacking the Central Factory...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Who would do such a thing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_2EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F02")

    ChrTalk(
        0xFE,
        "Now that I think about it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Where IS my grandfather?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FC1")

    label("loc_2F02")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "Hello, Tita. Heading out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FYes, ma'am. I'm off to Elmo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I see. Busy as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should stop by the hot\x01",
            "springs while you're there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My grandfather loves them.\x02",
    )

    CloseMessageWindow()

    label("loc_2FC1")

    Jump("loc_333E")

    label("loc_2FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_307E")

    ChrTalk(
        0xFE,
        (
            "I asked my husband what would\x01",
            "happen to an airship if its orbments\x01",
            "stopped working mid-flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He didn't answer me.\x01",
            "As usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's why I don't trust airships.\x02",
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_307E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30E8")

    ChrTalk(
        0xFE,
        (
            "I was making dinner when the\x01",
            "orbal stove stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Orbments are iffy like that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3183")

    label("loc_30E8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "I was cooking dinner and suddenly\x01",
            "the orbment stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luckily it only meant that the\x01",
            "stew my daughter forgot on\x01",
            "the stove didn't get burned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3183")

    Jump("loc_333E")

    label("loc_3186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3217")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "When you get back to school, \x01",
            "I wonder if you could help \x01",
            "Muriel with her studies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you in advance, Tita!\x02",
    )

    CloseMessageWindow()
    Jump("loc_328D")

    label("loc_3217")

    OP_A2(0x5)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "Tita! Come on in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone just got back from a\x01",
            "little family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Muriel wore herself out.\x02",
    )

    CloseMessageWindow()

    label("loc_328D")

    Jump("loc_333E")

    label("loc_3290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_32E9")

    ChrTalk(
        0xFE,
        (
            "Guess things are back to normal\x01",
            "now that the family's all together\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_32E9")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "My family just returned from\x01",
            "a trip to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They had a wonderful time!\x02",
    )

    CloseMessageWindow()

    label("loc_333E")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B4F end

    def Function_12_3342(): pass

    label("Function_12_3342")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_33E7")

    ChrTalk(
        0xFE,
        (
            "Grandpa, I want to be a receptionist\x01",
            "at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know lots of important people\x01",
            "at the factory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Put in a good word for me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B80")

    label("loc_33E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3470")

    ChrTalk(
        0xFE,
        (
            "I really think the best thing for\x01",
            "my future is to get a job at the\x01",
            "Central Factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's the hottest place in Zeiss!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B80")

    label("loc_3470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_34D3")

    ChrTalk(
        0xFE,
        (
            "What? I'm not happy about the\x01",
            "incident at the factory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's just...wow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3541")

    label("loc_34D3")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "Did you hear about the incident\x01",
            "at the factory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure does seem to be the\x01",
            "center of attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3541")

    Jump("loc_3B80")

    label("loc_3544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_35CB")

    ChrTalk(
        0xFE,
        (
            "I'd so love to work at the \x01",
            "Central Factory one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Professor Russell's there,\x01",
            "so I bet it's never boring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3644")

    label("loc_35CB")

    OP_A2(0x6)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        "You're so lucky, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064FWhat? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You've got purpose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm SO bored now.\x02",
    )

    CloseMessageWindow()

    label("loc_3644")

    Jump("loc_3B80")

    label("loc_3647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_37C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_36B3")

    ChrTalk(
        0xFE,
        (
            "You know, life is full of stuff to\x01",
            "look at, but nothing to SEE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Or something.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37C6")

    label("loc_36B3")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "I've been sick of everything since\x01",
            "coming back from my trip, but\x01",
            "yesterday was...wow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When all the orbments stopped\x01",
            "and the town went dark...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I looked up and the stars were\x01",
            "so beautiful in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, I'm always looking up\x01",
            "at the sky. It's weird.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C6")

    Jump("loc_3B80")

    label("loc_37C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3940")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_385A")

    ChrTalk(
        0xFE,
        (
            "I was making dinner with my\x01",
            "mom when the lights went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I went outside and everywhere\x01",
            "was black. I kind of lost it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393D")

    label("loc_385A")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "I was making dinner with my\x01",
            "mom when the lights went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ran outside and everywhere\x01",
            "was black. I kind of lost it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#561FOh...I'm sorry, Muriel.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "Hmm? How come?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why are you apologizing, Tita?\x02",
    )

    CloseMessageWindow()

    label("loc_393D")

    Jump("loc_3B80")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_39C5")

    ChrTalk(
        0xFE,
        (
            "And now everything goes back\x01",
            "to being dull again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should ask my grandpa to take\x01",
            "me on a trip someplace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B08")

    label("loc_39C5")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "Goddess, I HATE this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060FHi, Muriel!\x01",
            "How was your trip?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, it was the best! I had\x01",
            "such a great time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...But then I came back HERE.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And life went directly down\x01",
            "the toilet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What was waiting for me?\x01",
            "Boring days and mountains \x01",
            "of Sunday school homework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067FSorry to hear that.\x02",
    )

    CloseMessageWindow()

    label("loc_3B08")

    Jump("loc_3B80")

    label("loc_3B0B")


    ChrTalk(
        0xFE,
        (
            "I wish Mom had come with us \x01",
            "on our trip to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it was no use. She's got\x01",
            "this phobia about airships.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B80")

    TalkEnd(0xFE)
    Return()

    # Function_12_3342 end

    def Function_13_3B84(): pass

    label("Function_13_3B84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3BF9")

    ChrTalk(
        0xFE,
        "My granddaughter asked me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "..she asked me t' find her a \x01",
            "job a' the Central Factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C99")

    label("loc_3BF9")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "I know people there...but \x01",
            "they're all workin' in Engineerin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ain't no use askin' 'em about\x01",
            "a job 's a receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Losin' my touch.\x02",
    )

    CloseMessageWindow()

    label("loc_3C99")

    Jump("loc_3D00")

    label("loc_3C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3D00")

    ChrTalk(
        0xFE,
        (
            "Wonder if Sotiria's got dinner\x01",
            "ready yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Been talking all day long.\x01",
            "I'm starvin'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D00")

    TalkEnd(0xFE)
    Return()

    # Function_13_3B84 end

    def Function_14_3D04(): pass

    label("Function_14_3D04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3F11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3DF4")

    ChrTalk(
        0xFE,
        (
            "Elkan's finally started seeing\x01",
            "things my way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's got the hands for fine\x01",
            "tuning and the eye to judge\x01",
            "when and how to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he can get over some small\x01",
            "hang-ups, I'm sure he'll be a\x01",
            "fantastic merchant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F0E")

    label("loc_3DF4")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "Last night I was discussing shop\x01",
            "stock policy with Elkan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he's finally started seeing\x01",
            "things my way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We weapons merchants sell products\x01",
            "people literally stake their lives on.\x01",
            "Dedication is a must.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really have to make sure he\x01",
            "understands that point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0E")

    Jump("loc_4A07")

    label("loc_3F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_407B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3FA5")

    ChrTalk(
        0xFE,
        (
            "I think my son, Vince, really respects\x01",
            "scientists, deep down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that's what he ends up as\x01",
            "though, I hope he has vision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4078")

    label("loc_3FA5")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "The world grows by building out,\x01",
            "not just building up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You need to invent a thing that\x01",
            "everyone has a use for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like how they did in the Orbal\x01",
            "Revolution, using the septium\x01",
            "to invent orbments. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_4078")

    Jump("loc_4A07")

    label("loc_407B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4156")

    ChrTalk(
        0xFE,
        (
            "I think Karl's finally starting\x01",
            "to understand the power of\x01",
            "dependability in a weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Probably had to take the\x01",
            "point-of-view of the user \x01",
            "during his research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hope Elkan notices it, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4264")

    label("loc_4156")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "I don't know why, but Karl\x01",
            "came to see me this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Said he came to tell me he\x01",
            "finally understood my policy\x01",
            "about weapon dependability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He probably had to take the\x01",
            "point-of-view of the user\x01",
            "during some research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Changed his OWN point-of-view.\x02",
    )

    CloseMessageWindow()

    label("loc_4264")

    Jump("loc_4A07")

    label("loc_4267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4534")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_43DC")

    ChrTalk(
        0xFE,
        (
            "Weapons need two things:\x01",
            "dependability and usability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have to be something anyone\x01",
            "can use when the time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the most important thing\x01",
            "for our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And in spite of that, here they\x01",
            "come trying to sell these\x01",
            "experimental orbal guns...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At least once, Karl needs to\x01",
            "think about things from the\x01",
            "position of the user.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4531")

    label("loc_43DC")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "I went to visit Karl in the\x01",
            "Central Factory today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He talked Elkan into selling\x01",
            "test weapons at my store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to tell him my store\x01",
            "only carries goods that users\x01",
            "can depend on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But there was that incident,\x01",
            "so unfortunately I didn't get\x01",
            "a chance to see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to make time for that\x01",
            "talk sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4531")

    Jump("loc_4A07")

    label("loc_4534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_45C3")

    ChrTalk(
        0xFE,
        (
            "Glad all that hubbub around the\x01",
            "factory has begun to dissipate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "School should be finished.\x01",
            "Vince will be here soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_468E")

    label("loc_45C3")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "Glad all that hubbub around the\x01",
            "factory has begun to dissipate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness everything\x01",
            "calmed down before Sunday\x01",
            "school finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't want the children to\x01",
            "see all that chaos.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468E")

    Jump("loc_4A07")

    label("loc_4691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_47FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4718")

    ChrTalk(
        0xFE,
        "Of course I don't blame Elkan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I blame all these scientists\x01",
            "who are rushing in where \x01",
            "angels fear to tread.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F9")

    label("loc_4718")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "Elkan's dedicated to the job,\x01",
            "and he's good with machinery,\x01",
            "but he's hung up on efficiency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An efficient yet undependable\x01",
            "weapon is a useless weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I keep telling him that, but it\x01",
            "doesn't seem to sink in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F9")

    Jump("loc_4A07")

    label("loc_47FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_488A")

    ChrTalk(
        0xFE,
        (
            "I've got an old technician's pride\x01",
            "mixed with a careful eye for stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I carry the best, so come visit\x01",
            "my store sometime!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A07")

    label("loc_488A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4956")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "My family used to make watches.\x01",
            "I was a technician at the Central\x01",
            "Factory myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I loved interacting with\x01",
            "my customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before I knew it, I was running\x01",
            "a store of my own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A07")

    label("loc_4956")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "Oh, are you all bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stain Arms & Guards has the\x01",
            "means to fill your needs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My shop is just across the \x01",
            "street from the Bracer Guild,\x01",
            "so drop by any time! \x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A07")

    TalkEnd(0xFE)
    Return()

    # Function_14_3D04 end

    def Function_15_4A0B(): pass

    label("Function_15_4A0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4A80")

    ChrTalk(
        0xFE,
        (
            "Vince! You cut class again,\x01",
            "didn't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why do you keep doing this?\x01",
            "You're such a smart boy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD7")

    label("loc_4A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4AFE")

    ChrTalk(
        0xFE,
        (
            "Sunday school should be just\x01",
            "about finished by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope Vince did some real\x01",
            "studying this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD7")

    label("loc_4AFE")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "I'm glad there were no fires\x01",
            "or injuries...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I still can't believe something\x01",
            "like this happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh my, it's almost time for\x01",
            "Sunday school to finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I should go pick\x01",
            "up Vince...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD7")

    TalkEnd(0xFE)
    Return()

    # Function_15_4A0B end

    def Function_16_4BDB(): pass

    label("Function_16_4BDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4C9B")

    ChrTalk(
        0xFE,
        (
            "I want to be a scientist\x01",
            "when I get older.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, I probably won't be\x01",
            "able to focus on just one\x01",
            "research project at a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But that can be a plus, too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D4E")

    label("loc_4C9B")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "Karl came by early this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Karl's eyes were all bloodshot.\x01",
            "I wonder if he got any sleep\x01",
            "last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing how focused he is on\x01",
            "his job is so inspiring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D4E")

    Jump("loc_4E37")

    label("loc_4D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4DD6")

    ChrTalk(
        0xFE,
        "Mother, don't be like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just don't have it in me to\x01",
            "stay focused on just one\x01",
            "thing for a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E37")

    label("loc_4DD6")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "I wasn't 'cutting class.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was 'exploring interests apart\x01",
            "from the rest of class.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E37")

    TalkEnd(0xFE)
    Return()

    # Function_16_4BDB end

    def Function_17_4E3B(): pass

    label("Function_17_4E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4E73")

    ChrTalk(
        0xFE,
        "Well, let's warm up this soup.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ED5")

    label("loc_4E73")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "*sigh* Louise let it all boil down\x01",
            "again, didn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If only she'd eat something...\x02",
    )

    CloseMessageWindow()

    label("loc_4ED5")

    Jump("loc_4FCC")

    label("loc_4ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4F63")

    ChrTalk(
        0xFE,
        (
            "After I finish cooking, I need to\x01",
            "get back to the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ben can't handle the place on\x01",
            "his own, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FCC")

    label("loc_4F63")

    OP_A2(0xC)
    TurnDirection(0x11, 0x9, 400)

    ChrTalk(
        0xFE,
        (
            "I don't mind doing the cooking,\x01",
            "but...Yuriel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why do I have to make your bed?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 0)

    label("loc_4FCC")

    TalkEnd(0xFE)
    Return()

    # Function_17_4E3B end

    SaveToFile()

Try(main)
