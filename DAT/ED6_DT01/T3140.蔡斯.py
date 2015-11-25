from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3140   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3140.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'ED6_DT07/CH01433 ._CH',             # 00
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
        'ED6_DT07/CH01433P._CP',             # 00
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
        Z                   = 250,
        Y                   = 23230,
        Direction           = 254,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        Z                   = 0,
        Y                   = 740,
        Direction           = 308,
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
        X                   = 27980,
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
        "Function_1_42E",          # 01, 1
        "Function_2_42F",          # 02, 2
        "Function_3_445",          # 03, 3
        "Function_4_469",          # 04, 4
        "Function_5_48D",          # 05, 5
        "Function_6_4B1",          # 06, 6
        "Function_7_4D5",          # 07, 7
        "Function_8_4F9",          # 08, 8
        "Function_9_12EB",         # 09, 9
        "Function_10_1E2F",        # 0A, 10
        "Function_11_2A0E",        # 0B, 11
        "Function_12_31F3",        # 0C, 12
        "Function_13_39BC",        # 0D, 13
        "Function_14_3B3C",        # 0E, 14
        "Function_15_4843",        # 0F, 15
        "Function_16_4AA4",        # 10, 16
        "Function_17_4D04",        # 11, 17
    )


    def Function_0_23A(): pass

    label("Function_0_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_249")
    SetChrFlags(0xA, 0x80)
    Jump("loc_42D")

    label("loc_249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_286")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xA, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xC, 21930, 0, 2180, 138)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_42D")

    label("loc_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2A6")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_42D")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2DC")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28080, 0, 25700, 170)
    Jump("loc_42D")

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_387")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1800, 0, 21070, 263)
    SetChrPos(0x9, 750, 0, 24620, 270)
    SetChrPos(0x8, -1720, 220, 24700, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -160, 0, -100, 315)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 26330, 4000, 25200, 76)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 27970, 4000, 25230, 275)
    SetChrPos(0xA, 21330, 0, 3950, 352)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Jump("loc_42D")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3BA")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -3830, 0, 330, 269)
    OP_43(0xF, 0x0, 0x0, 0x7)
    Jump("loc_42D")

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_42D")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_404")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1800, 0, 21070, 263)
    Jump("loc_42D")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_41A")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xE, 0x80)
    Jump("loc_42D")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_42D")
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xE, 0x80)

    label("loc_42D")

    Return()

    # Function_0_23A end

    def Function_1_42E(): pass

    label("Function_1_42E")

    Return()

    # Function_1_42E end

    def Function_2_42F(): pass

    label("Function_2_42F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_444")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_42F")

    label("loc_444")

    Return()

    # Function_2_42F end

    def Function_3_445(): pass

    label("Function_3_445")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_468")
    OP_8D(0xFE, 290, 22470, 1800, 25300, 2000)
    Jump("Function_3_445")

    label("loc_468")

    Return()

    # Function_3_445 end

    def Function_4_469(): pass

    label("Function_4_469")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48C")
    OP_8D(0xFE, -1920, 1860, 2170, -2770, 2000)
    Jump("Function_4_469")

    label("loc_48C")

    Return()

    # Function_4_469 end

    def Function_5_48D(): pass

    label("Function_5_48D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B0")
    OP_8D(0xFE, -4730, 3760, -1290, 1770, 2000)
    Jump("Function_5_48D")

    label("loc_4B0")

    Return()

    # Function_5_48D end

    def Function_6_4B1(): pass

    label("Function_6_4B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D4")
    OP_8D(0xFE, 20960, 3050, 25510, -530, 2000)
    Jump("Function_6_4B1")

    label("loc_4D4")

    Return()

    # Function_6_4B1 end

    def Function_7_4D5(): pass

    label("Function_7_4D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F8")
    OP_8D(0xFE, -5320, 520, -1440, 630, 2000)
    Jump("Function_7_4D5")

    label("loc_4F8")

    Return()

    # Function_7_4D5 end

    def Function_8_4F9(): pass

    label("Function_8_4F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_563")
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
    Jump("loc_12EA")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_702")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_636")

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
    Jump("loc_6FC")

    label("loc_636")

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

    label("loc_6FC")

    TalkEnd(0x8)
    Jump("loc_12EA")

    label("loc_702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_84B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_78A")
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
    Jump("loc_845")

    label("loc_78A")

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

    label("loc_845")

    TalkEnd(0x8)
    Jump("loc_12EA")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_901")
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
    Jump("loc_12EA")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_B5E")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9AA")

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
    Jump("loc_B58")

    label("loc_9AA")

    OP_A2(0x2)

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

    ChrTalk(
        0x107,
        (
            "#060FUuuugggh...\x02\x03",
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

    label("loc_B58")

    TalkEnd(0x8)
    Jump("loc_12EA")

    label("loc_B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1105")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C57")
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
        "But that's work, I guess.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1102")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1053")
    OP_A2(0x573)
    OP_A2(0x2)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(
        0xFE,
        (
            "Hmm? Tita?\x01",
            "Something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCD")

    label("loc_C98")


    ChrTalk(
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "Tita, what are you doing here?\x02",
    )

    CloseMessageWindow()

    label("loc_CCD")


    ChrTalk(
        0x107,
        (
            "#060FLouise! Aren't you supposed\x01",
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
            "#060FYes, I am. We're on our way\x01",
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
        "#000FEx-explosions?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#060FI wouldn't go so far as to say\x01",
            "'explosions,' Louise.\x02\x03",
            "Just a little flying glass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FJust a little FLYING GLASS?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FHa ha...wait...seriously?\x02",
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
            "#060FUh, okay. Thank you...?\x02\x03",
            "Good luck on the production of\x01",
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
    Jump("loc_1102")

    label("loc_1053")

    TalkBegin(0x8)
    OP_A2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A8")

    ChrTalk(
        0xFE,
        (
            "Hmm? Tita? Still not finished\x01",
            "showing those guests around?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B8")

    label("loc_10A8")


    ChrTalk(
        0xFE,
        "Hold on...\x02",
    )

    CloseMessageWindow()

    label("loc_10B8")

    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "Hmm? Tita? Still not finished\x01",
            "showing those guests around?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1102")

    Jump("loc_12EA")

    label("loc_1105")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x8)
    OP_44(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BD")
    OP_A2(0x0)
    SetChrFlags(0x9, 0x20)
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
    Jump("loc_12DD")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1254")
    OP_A2(0x1)
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
    Jump("loc_12DD")

    label("loc_1254")


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

    label("loc_12DD")

    OP_8C(0x9, 263, 400)
    OP_85(0x9)
    TalkEnd(0x8)

    label("loc_12EA")

    Return()

    # Function_8_4F9 end

    def Function_9_12EB(): pass

    label("Function_9_12EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13CF")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135E")
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
    Jump("loc_13C9")

    label("loc_135E")


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

    label("loc_13C9")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_13CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_149D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142E")
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
    Jump("loc_1497")

    label("loc_142E")


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

    label("loc_1497")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_149D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_15EC")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1573")
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
    Jump("loc_15E6")

    label("loc_1573")


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

    label("loc_15E6")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_15EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_170A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1698")
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
    Jump("loc_1704")

    label("loc_1698")


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

    label("loc_1704")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_170A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_184C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B1")
    OP_A2(0x3)

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
            "#060FAh...\x02\x03",
            "Y-Yes. I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's good to hear.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1846")

    label("loc_17B1")


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

    label("loc_1846")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_193A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CF")
    OP_A2(0x3)

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
    Jump("loc_1934")

    label("loc_18CF")


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

    label("loc_1934")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_193A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_19BE")
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
    Jump("loc_1E2E")

    label("loc_19BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1B0F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACC")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "*yawn* Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, hi, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FHi, Yuriel.\x02",
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
    Jump("loc_1B09")

    label("loc_1ACC")


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

    label("loc_1B09")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1CFE")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 4)), scpexpr(EXPR_END)), "loc_1B89")

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
    Jump("loc_1CF8")

    label("loc_1B89")

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
            "#060FOh...\x02\x03",
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
            "#060FOkay.\x01",
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

    label("loc_1CF8")

    TalkEnd(0xFE)
    Jump("loc_1E2E")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0B")
    SetChrFlags(0xFE, 0x10)

    label("loc_1D0B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEC")
    OP_44(0x8, 0xFF)
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

    ChrTalk(
        0x8,
        "Yeah, okay. Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm a little busy right now.\x01",
            "I'll talk to you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hurry UP!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 263, 400)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_1E28")

    label("loc_1DEC")


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

    label("loc_1E28")

    OP_85(0x8)
    TalkEnd(0x9)

    label("loc_1E2E")

    Return()

    # Function_9_12EB end

    def Function_10_1E2F(): pass

    label("Function_10_1E2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1ED1")

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
            "engine research team.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204F")

    label("loc_1ED1")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "I received notice from Hugo that they've\x01",
            "decided to add a new member to the orbal\x01",
            "engine had been chosen.\x02",
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

    label("loc_204F")

    Jump("loc_2A0A")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20F6")

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
    Jump("loc_216D")

    label("loc_20F6")

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

    label("loc_216D")

    Jump("loc_2A0A")

    label("loc_2170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2227")

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
    Jump("loc_232D")

    label("loc_2227")

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

    label("loc_232D")

    Jump("loc_2A0A")

    label("loc_2330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_24CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_23BF")

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
    Jump("loc_24C9")

    label("loc_23BF")

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

    label("loc_24C9")

    Jump("loc_2A0A")

    label("loc_24CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_267C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_257B")

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
    Jump("loc_2679")

    label("loc_257B")

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

    label("loc_2679")

    Jump("loc_2A0A")

    label("loc_267C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_280C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2705")

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
    Jump("loc_2809")

    label("loc_2705")

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

    label("loc_2809")

    Jump("loc_2A0A")

    label("loc_280C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_284B")

    ChrTalk(
        0xFE,
        (
            "Okay, break time's finished.\x01",
            "Back to work I go!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A0A")

    label("loc_284B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2957")

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
    Jump("loc_2A0A")

    label("loc_2957")

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

    label("loc_2A0A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1E2F end

    def Function_11_2A0E(): pass

    label("Function_11_2A0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2B10")

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
    Jump("loc_31EF")

    label("loc_2B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2C20")

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
    Jump("loc_31EF")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C8D")

    ChrTalk(
        0xFE,
        (
            "Since my grandfather was at the\x01",
            "bar, he says he didn't hear about\x01",
            "the incident at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1D")

    label("loc_2C8D")

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

    label("loc_2D1D")

    Jump("loc_31EF")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D70")

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
    Jump("loc_31EF")

    label("loc_2D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2DC1")

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
    Jump("loc_2E80")

    label("loc_2DC1")

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

    label("loc_2E80")

    Jump("loc_31EF")

    label("loc_2E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2F3D")

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
    Jump("loc_31EF")

    label("loc_2F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2FA7")

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
    Jump("loc_3042")

    label("loc_2FA7")

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

    label("loc_3042")

    Jump("loc_31EF")

    label("loc_3045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30CF")

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
    Jump("loc_313E")

    label("loc_30CF")

    OP_A2(0x5)

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

    label("loc_313E")

    Jump("loc_31EF")

    label("loc_3141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_319A")

    ChrTalk(
        0xFE,
        (
            "Guess things are back to normal\x01",
            "now that the family's all together\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31EF")

    label("loc_319A")

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

    label("loc_31EF")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A0E end

    def Function_12_31F3(): pass

    label("Function_12_31F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3298")

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
    Jump("loc_39B8")

    label("loc_3298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3321")

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
    Jump("loc_39B8")

    label("loc_3321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_33F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3384")

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
    Jump("loc_33F2")

    label("loc_3384")

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

    label("loc_33F2")

    Jump("loc_39B8")

    label("loc_33F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_34F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_347C")

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
    Jump("loc_34EE")

    label("loc_347C")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "You're so lucky, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FWhat? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You've got purpose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm SO bored now.\x02",
    )

    CloseMessageWindow()

    label("loc_34EE")

    Jump("loc_39B8")

    label("loc_34F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_355D")

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
    Jump("loc_3636")

    label("loc_355D")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "But last night was...wow.\x02",
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
            "The view of the sky from the\x01",
            "veranda took my breath away.\x02",
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

    label("loc_3636")

    Jump("loc_39B8")

    label("loc_3639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_37B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_36CA")

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
    Jump("loc_37AD")

    label("loc_36CA")

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
            "I ran to the veranda and everywhere\x01",
            "was black. I kind of lost it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FOh...I'm sorry, Muriel.\x02",
    )

    CloseMessageWindow()

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

    label("loc_37AD")

    Jump("loc_39B8")

    label("loc_37B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3835")

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
    Jump("loc_3940")

    label("loc_3835")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "*sigh* And now everything goes\x01",
            "back to being dull again.\x02",
        )
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
        0x107,
        "#060FSorry to hear that.\x02",
    )

    CloseMessageWindow()

    label("loc_3940")

    Jump("loc_39B8")

    label("loc_3943")


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

    label("loc_39B8")

    TalkEnd(0xFE)
    Return()

    # Function_12_31F3 end

    def Function_13_39BC(): pass

    label("Function_13_39BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A31")

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
    Jump("loc_3AD1")

    label("loc_3A31")

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

    label("loc_3AD1")

    Jump("loc_3B38")

    label("loc_3AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3B38")

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

    label("loc_3B38")

    TalkEnd(0xFE)
    Return()

    # Function_13_39BC end

    def Function_14_3B3C(): pass

    label("Function_14_3B3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3C2C")

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
    Jump("loc_3D46")

    label("loc_3C2C")

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

    label("loc_3D46")

    Jump("loc_483F")

    label("loc_3D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3EB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3DDD")

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
    Jump("loc_3EB0")

    label("loc_3DDD")

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

    label("loc_3EB0")

    Jump("loc_483F")

    label("loc_3EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_409F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3F8E")

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
    Jump("loc_409C")

    label("loc_3F8E")

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

    label("loc_409C")

    Jump("loc_483F")

    label("loc_409F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_436C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4214")

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
    Jump("loc_4369")

    label("loc_4214")

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

    label("loc_4369")

    Jump("loc_483F")

    label("loc_436C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_44C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_43FB")

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
    Jump("loc_44C6")

    label("loc_43FB")

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

    label("loc_44C6")

    Jump("loc_483F")

    label("loc_44C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4550")

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
    Jump("loc_4631")

    label("loc_4550")

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

    label("loc_4631")

    Jump("loc_483F")

    label("loc_4634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_46C2")

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
    Jump("loc_483F")

    label("loc_46C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_478E")
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
    Jump("loc_483F")

    label("loc_478E")

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

    label("loc_483F")

    TalkEnd(0xFE)
    Return()

    # Function_14_3B3C end

    def Function_15_4843(): pass

    label("Function_15_4843")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_48BF")

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
    Jump("loc_4946")

    label("loc_48BF")

    OP_A2(0xA)
    OP_62(0xF, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(1000)

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

    label("loc_4946")

    Jump("loc_4AA0")

    label("loc_4949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_49C7")

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
    Jump("loc_4AA0")

    label("loc_49C7")

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

    label("loc_4AA0")

    TalkEnd(0xFE)
    Return()

    # Function_15_4843 end

    def Function_16_4AA4(): pass

    label("Function_16_4AA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4B64")

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
    Jump("loc_4C17")

    label("loc_4B64")

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

    label("loc_4C17")

    Jump("loc_4D00")

    label("loc_4C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4C9F")

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
    Jump("loc_4D00")

    label("loc_4C9F")

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

    label("loc_4D00")

    TalkEnd(0xFE)
    Return()

    # Function_16_4AA4 end

    def Function_17_4D04(): pass

    label("Function_17_4D04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4D3C")

    ChrTalk(
        0xFE,
        "Well, let's warm up this soup.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9E")

    label("loc_4D3C")

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

    label("loc_4D9E")

    Jump("loc_4E87")

    label("loc_4DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4E87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4E2C")

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
    Jump("loc_4E87")

    label("loc_4E2C")

    OP_A2(0xC)

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

    label("loc_4E87")

    TalkEnd(0xFE)
    Return()

    # Function_17_4D04 end

    SaveToFile()

Try(main)
