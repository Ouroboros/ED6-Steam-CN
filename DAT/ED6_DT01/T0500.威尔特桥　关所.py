from ED6ScenarioHelper import *

def main():
    # 威尔特桥　关所

    CreateScenaFile(
        FileName            = 'T0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0500.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0500   ._SN',
            'ED6_DT01/T0500_1 ._SN',
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
        'Private Scott',                        # 9
        'Private Harold',                       # 10
        'CWO Ashton',                           # 11
        'Private Antose',                       # 12
        'Private Lacos',                        # 13
        'Sting',                                # 14
        'Anelace',                              # 15
        'Private Scott',                        # 16
        'Private Harold',                       # 17
        'Estelle',                              # 18
        'Joshua',                               # 19
        'Private Scott',                        # 20
        'Private Harold',                       # 21
        'Estelle',                              # 22
        'Milch Main Road',                      # 23
        'East Bose Highway',                    # 24
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 90,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 135,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 90,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH00320 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00324 ._CH',             # 05
        'ED6_DT07/CH00104 ._CH',             # 06
        'ED6_DT07/CH01620 ._CH',             # 07
        'ED6_DT07/CH01630 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH00320P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00324P._CP',             # 05
        'ED6_DT07/CH00104P._CP',             # 06
        'ED6_DT07/CH01620P._CP',             # 07
        'ED6_DT07/CH01630P._CP',             # 08
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = -19010,
        Direction           = 180,
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
        X                   = 16920,
        Z                   = 120,
        Y                   = -7750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3300,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 12900,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 5400,
        Z                   = 0,
        Y                   = 26700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1980,
        Z                   = -410,
        Y                   = -40440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 440,
        Z                   = -510,
        Y                   = 41850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 5680,
        TriggerZ            = -260,
        TriggerY            = -27360,
        TriggerRange        = 1500,
        ActorX              = 5680,
        ActorZ              = 1700,
        ActorY              = -27360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9630,
        TriggerZ            = -150,
        TriggerY            = 27430,
        TriggerRange        = 1500,
        ActorX              = -9630,
        ActorZ              = 1700,
        ActorY              = 27430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37E",          # 00, 0
        "Function_1_3C1",          # 01, 1
        "Function_2_400",          # 02, 2
        "Function_3_416",          # 03, 3
        "Function_4_43A",          # 04, 4
        "Function_5_594",          # 05, 5
        "Function_6_5FB",          # 06, 6
        "Function_7_662",          # 07, 7
        "Function_8_1972",         # 08, 8
        "Function_9_2281",         # 09, 9
        "Function_10_2A17",        # 0A, 10
        "Function_11_30D5",        # 0B, 11
        "Function_12_34BE",        # 0C, 12
        "Function_13_38F1",        # 0D, 13
    )


    def Function_0_37E(): pass

    label("Function_0_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_388")
    Jump("loc_3AD")

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_397")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_3AD")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3A1")
    Jump("loc_3AD")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3AD")
    ClearChrFlags(0xE, 0x80)

    label("loc_3AD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3B9"),
        (SWITCH_DEFAULT, "loc_3C0"),
    )


    label("loc_3B9")

    Event(1, 0)
    Jump("loc_3C0")

    label("loc_3C0")

    Return()

    # Function_0_37E end

    def Function_1_3C1(): pass

    label("Function_1_3C1")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFE0FE8, 0x30005)
    OP_72(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7")
    OP_6F(0x2, 420)

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FF")
    OP_6F(0x1, 420)
    OP_72(0x1, 0x10)

    label("loc_3FF")

    Return()

    # Function_1_3C1 end

    def Function_2_400(): pass

    label("Function_2_400")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_415")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_400")

    label("loc_415")

    Return()

    # Function_2_400 end

    def Function_3_416(): pass

    label("Function_3_416")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439")
    OP_8D(0xFE, 2000, 24900, 7200, 30100, 2000)
    Jump("Function_3_416")

    label("loc_439")

    Return()

    # Function_3_416 end

    def Function_4_43A(): pass

    label("Function_4_43A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_593")
    Sleep(3000)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x438A, 0xFFFFFFC4, 0xFFFF9E94, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFABBE, 0xFFFFFF88, 0xFFFF9C14, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFAB46, 0xFFFFFEFC, 0xFFFF8DC8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFA, 0xFFFFFEF2, 0xFFFF9034, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x1054, 0xFFFFFF10, 0xFFFF89B8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C10, 0xFFFFFE2A, 0xFFFF8A08, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C1A, 0x50, 0xFFFFD79C, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4236, 0xA, 0xFFFFD6E8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4218, 0x78, 0xFFFFE1BA, 0x9C4, 0x0)
    Jump("Function_4_43A")

    label("loc_593")

    Return()

    # Function_4_43A end

    def Function_5_594(): pass

    label("Function_5_594")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East: Rolent - 172 selge\x01",
            "West: Bose City - 420 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_594 end

    def Function_6_5FB(): pass

    label("Function_6_5FB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West: Bose City - 420 selge\x01",
            "East: Rolent - 172 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_5FB end

    def Function_7_662(): pass

    label("Function_7_662")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_11C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_END)), "loc_DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D63")
    EventBegin(0x0)
    OP_4A(0x8, 0)
    Fade(1000)
    SetChrPos(0x101, 2370, 0, -20490, 0)
    SetChrPos(0x102, 3130, 0, -21420, 0)
    SetChrPos(0x103, 1570, 0, -21630, 0)
    TurnDirection(0xFE, 0x101, 0)
    OP_6C(45000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(
        0xFE,
        (
            "Hello there. Are you headed\x01",
            "for Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWe are. But how did you know\x01",
            "we weren't just visiting again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, a number of people like\x01",
            "yourselves have been passing\x01",
            "through lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Exponentially more than usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIs that because flights have been\x01",
            "suspended in the airspace over\x01",
            "Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly what's happened.\x01",
            "You wouldn't believe how busy\x01",
            "this place is because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027FWell, the Royal Army is responsible\x01",
            "for all the restricted flights.\x02\x03",
            "So you're really not in a position\x01",
            "to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, I guess you're right about\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, and another thing: traffic\x01",
            "through this checkpoint is\x01",
            "also being regulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to go through here,\x01",
            "you'll have to get a pass from\x01",
            "the chief warrant officer next door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOh, well, we've already got one.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x32F, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "Gate Pass\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        "Well, aren't you guys prepared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B09")

    label("loc_A7A")


    ChrTalk(
        0x101,
        "#000FAll right, we got one.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x32F, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "Gate Pass\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        "Well, that was quick.\x02",
    )

    CloseMessageWindow()

    label("loc_B09")


    ChrTalk(
        0xFE,
        (
            "Okay then, how about I open the\x01",
            "gate for you?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The soldier opened the gate by remote control.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)
    OP_8C(0x101, 315, 400)
    OP_8C(0x102, 315, 400)
    OP_8C(0x103, 315, 400)
    Sleep(1000)

    def lambda_BB6():
        OP_6D(-900, 0, -9960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BB6)

    def lambda_BCE():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BCE)

    def lambda_BDE():
        OP_67(0, 4000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BDE)

    def lambda_BF6():
        OP_6B(5500, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BF6)
    Sleep(4000)
    OP_22(0xD0, 0x0, 0x64)
    OP_72(0x1, 0x800)
    OP_70(0x1, 0x1A4)
    OP_73(0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(2200, 0, -20370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    TurnDirection(0xFE, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "All right, you're clear to go\x01",
            "on through.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    OP_8C(0x103, 0, 400)

    ChrTalk(
        0xFE,
        (
            "Once you cross over, you won't\x01",
            "be able to come back unless you\x01",
            "get a pass from the other side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be aware of that before\x01",
            "you cross.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGot it.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 0)
    EventEnd(0x0)
    OP_28(0x52, 0x1, 0x2)
    OP_A2(0x304)
    Jump("loc_DF6")

    label("loc_D63")


    ChrTalk(
        0xFE,
        (
            "Once you cross over, you won't\x01",
            "be able to come back unless you\x01",
            "get a pass from the other side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be aware of that before\x01",
            "you cross.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF6")

    Jump("loc_11C4")

    label("loc_DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111D")
    EventBegin(0x0)

    ChrTalk(
        0xFE,
        (
            "Hello there. Are you headed\x01",
            "for Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWe are. But how did you know\x01",
            "we weren't just visiting again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, a number of people like\x01",
            "yourselves have been passing\x01",
            "through lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Exponentially more than usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIs that because flights have been\x01",
            "suspended in the airspace over\x01",
            "Bose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly what's happened.\x01",
            "You wouldn't believe how busy\x01",
            "this place is because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027FWell, the Royal Army is responsible\x01",
            "for all the restricted flights.\x02\x03",
            "So you're really not in a position\x01",
            "to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, I guess you're right about\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, and another thing: traffic\x01",
            "through this checkpoint is\x01",
            "also being regulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to go through here,\x01",
            "you'll have to get a pass from\x01",
            "the chief warrant officer next door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x302)
    EventEnd(0x1)
    Jump("loc_11C4")

    label("loc_111D")


    ChrTalk(
        0xFE,
        (
            "Passage through this checkpoint\x01",
            "is also being regulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to go through here,\x01",
            "you'll have to get a pass from\x01",
            "the chief warrant officer next door.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    Jump("loc_196E")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1350")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(
        0xFE,
        (
            "Recently in the Bose region next door,\x01",
            "there have been a number of burglaries\x01",
            "occurring one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to be the work of\x01",
            "the Sky Bandits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134D")

    label("loc_127D")


    ChrTalk(
        0xFE,
        (
            "Recently in the Bose region next door,\x01",
            "there have been a number of burglaries\x01",
            "occurring one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to be the work of\x01",
            "the Sky Bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'm glad I did that\x01",
            "training now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134D")

    Jump("loc_196E")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1619")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144E")

    ChrTalk(
        0xFE,
        (
            "This is just between you and\x01",
            "me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The chief used to be part of the Royal City's\x01",
            "main forces. They even say he showed some\x01",
            "incredible promise as a leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what could have caused\x01",
            "him to be stationed here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1597")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "The chief used to be part of the Royal City's\x01",
            "main forces. They even say he showed some\x01",
            "incredible promise as a leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what could have caused\x01",
            "him to be stationed here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, hitting us with sudden\x01",
            "training like that was really awful\x01",
            "of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm still hurting from the\x01",
            "exercise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_1597")


    ChrTalk(
        0xFE,
        (
            "At any rate, hitting us with sudden\x01",
            "training like that was really awful\x01",
            "of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm still hurting from the\x01",
            "exercise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1616")

    Jump("loc_196E")

    label("loc_1619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_17E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1775")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FA")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "I'm stuck standing here today, but\x01",
            "travelers are incredibly sparse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, I'm so bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all this free time, I've\x01",
            "started trying to find shapes\x01",
            "in the clouds as they pass by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1772")

    label("loc_16FA")


    ChrTalk(
        0xFE,
        "Man, I'm so bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all this free time, I've\x01",
            "started trying to find shapes\x01",
            "in the clouds as they pass by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1772")

    Jump("loc_17E5")

    label("loc_1775")


    ChrTalk(
        0xFE,
        (
            "I hate being bored like this\x01",
            "but training is even worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My body seriously aches\x01",
            "all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ow...\x02",
    )

    CloseMessageWindow()

    label("loc_17E5")

    Jump("loc_196E")

    label("loc_17E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_196E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C6")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "Ever since airliner flights began,\x01",
            "there haven't been very many\x01",
            "travelers on the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is why guarding the checkpoint\x01",
            "is so boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only one excited about the\x01",
            "job is the chief.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196E")

    label("loc_18C6")


    ChrTalk(
        0xFE,
        (
            "With the number of travelers passing\x01",
            "through here on the decline, the\x01",
            "checkpoint has become a bore to guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only one excited about the\x01",
            "job is the chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196E")

    TalkEnd(0x8)
    Return()

    # Function_7_662 end

    def Function_8_1972(): pass

    label("Function_8_1972")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE8")
    OP_A2(0x29C)

    ChrTalk(
        0xFE,
        (
            "Since joining the army, this is\x01",
            "the first time I've ever been so\x01",
            "busy in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess this is no time to be\x01",
            "fishing or reading books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just bought this book, but\x01",
            "I guess I'll give it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The chief would be livid if\x01",
            "he caught me with this.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x213, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Carnelia - Chapter 2\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_1BEF")

    label("loc_1AE8")


    ChrTalk(
        0xFE,
        (
            "Since joining the army, this is\x01",
            "the first time I've ever been so\x01",
            "busy in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Probably because I've been stuck\x01",
            "guarding a checkpoint that, until\x01",
            "recently, nobody's been using!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the first time I've really\x01",
            "felt like I'm in the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEF")

    Jump("loc_227D")

    label("loc_1BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1D50")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA8")

    ChrTalk(
        0xFE,
        (
            "We're presently on heightened alert.\x01",
            "It's been said there are a bunch of\x01",
            "bandits in the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's just hope they don't\x01",
            "decide to come here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4D")

    label("loc_1CA8")


    ChrTalk(
        0xFE,
        (
            "We're presently on heightened alert.\x01",
            "It's been said there are a bunch of\x01",
            "bandits in the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's just hope we only have\x01",
            "to deal with training...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4D")

    Jump("loc_227D")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1F71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E33")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "The chief almost blew his top\x01",
            "when he caught me fishing in the\x01",
            "river over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, it's such a waste when there\x01",
            "are so many good fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The water is so cool and\x01",
            "refreshing, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1E33")


    ChrTalk(
        0xFE,
        (
            "The chief almost blew his top\x01",
            "when he caught me fishing in the\x01",
            "river over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, it's such a waste when there\x01",
            "are so many good fish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC7")

    Jump("loc_1F6E")

    label("loc_1ECA")


    ChrTalk(
        0xFE,
        (
            "Earlier today, the chief almost\x01",
            "blew his top when he caught me\x01",
            "fishing in the river over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I wonder if that's why he\x01",
            "hit us with that training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6E")

    Jump("loc_227D")

    label("loc_1F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_21FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206D")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "The checkpoint here almost gets\x01",
            "no travelers, and it's quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I can hear is the babbling\x01",
            "of the river and the chirping\x01",
            "song of the birds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is way more relaxing than\x01",
            "the farm where I worked before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_206D")


    ChrTalk(
        0xFE,
        (
            "All I can hear is the babbling\x01",
            "of the river and the chirping\x01",
            "song of the birds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is way more relaxing than\x01",
            "the farm where I worked before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2106")

    Jump("loc_21FC")

    label("loc_2109")


    ChrTalk(
        0xFE,
        (
            "The checkpoint here almost gets\x01",
            "no travelers, and it's quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I can hear is the babbling\x01",
            "of the river and the chirping\x01",
            "song of the birds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew, if not for that training,\x01",
            "this place would have been\x01",
            "more placid than the farm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FC")

    Jump("loc_227D")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_227D")

    ChrTalk(
        0xFE,
        "I was just stationed here recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had been working on a farm,\x01",
            "but I decided to enlist in the\x01",
            "Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227D")

    TalkEnd(0x9)
    Return()

    # Function_8_1972 end

    def Function_9_2281(): pass

    label("Function_9_2281")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_231E")

    ChrTalk(
        0xFE,
        (
            "The burglaries in Bose were the\x01",
            "work of the Sky Bandits...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now let's just hope that this region\x01",
            "returns to its calm, peaceful state.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A13")

    label("loc_231E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_24E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2428")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "Did you say Bose was hit with\x01",
            "a bunch of burglaries?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's this world coming to?\x01",
            "It makes me want to rush there\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, after seeing the border garrison's\x01",
            "airships, I imagine they're already\x01",
            "investigating the matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E1")

    label("loc_2428")


    ChrTalk(
        0xFE,
        (
            "Sky bandits and now burglaries.\x01",
            "It sounds like someone is doing\x01",
            "whatever they please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to work in the garrison\x01",
            "at a checkpoint, I want to work on\x01",
            "the front lines!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E1")

    Jump("loc_2A13")

    label("loc_24E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25B9")

    ChrTalk(
        0xFE,
        (
            "The border garrison seems to have\x01",
            "arrested a number of suspicious\x01",
            "individuals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a maniacal group of women\x01",
            "and children and even an odd con artist,\x01",
            "but none of them were the criminals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A13")

    label("loc_25B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2687")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "Even now, not much information is\x01",
            "being passed on to the checkpoints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't really know how the\x01",
            "Royal Army is moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting impatient...\x01",
            "I want to mobilize too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2713")

    label("loc_2687")


    ChrTalk(
        0xFE,
        (
            "Even now, not much accurate information\x01",
            "is being passed on to the checkpoints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't really know how the\x01",
            "Royal Army is moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2713")

    Jump("loc_2A13")

    label("loc_2716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(
        0xFE,
        (
            "If we compare the east checkpoint\x01",
            "with the west one, the west has\x01",
            "more veteran soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Warrant Officer Dyne, despite his appearance,\x01",
            "does his job to the letter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A13")

    label("loc_27CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C8")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "At any rate,  our CWO does\x01",
            "an admirable job over here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He positioned all of the new recruits\x01",
            "on his side to whip them into shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's respectable and serious,\x01",
            "but he must live with twice the\x01",
            "stress of others.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295D")

    label("loc_28C8")


    ChrTalk(
        0xFE,
        (
            "At any rate, our CWO does\x01",
            "an admirable job over here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's respectable and serious,\x01",
            "but he must live with twice the\x01",
            "stress of others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295D")

    Jump("loc_2A13")

    label("loc_2960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2A13")

    ChrTalk(
        0xFE,
        "Hi. Are you headed to Bose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are currently in a state\x01",
            "of emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are looking for any suspicious\x01",
            "individuals among those heading\x01",
            "from Bose to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A13")

    TalkEnd(0xB)
    Return()

    # Function_9_2281 end

    def Function_10_2A17(): pass

    label("Function_10_2A17")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2A91")

    ChrTalk(
        0xFE,
        (
            "It looks like all airliner flights\x01",
            "have resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really glad that the criminals\x01",
            "were arrested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2B27")

    ChrTalk(
        0xFE,
        (
            "Although the flights have resumed, the\x01",
            "security checks at the checkpoints will\x01",
            "continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope things get back to\x01",
            "normal soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2C")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "It seems that the westward circling\x01",
            "airliner, Cecilia, has resumed\x01",
            "flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, the number of travelers\x01",
            "passing through here has decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder when the eastward circling\x01",
            "airline, Linde, will resume flights.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCE")

    label("loc_2C2C")


    ChrTalk(
        0xFE,
        (
            "It seems that the westward circling\x01",
            "airliner, Cecilia, has resumed\x01",
            "flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, the number of travelers\x01",
            "passing through here has decreased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCE")

    Jump("loc_30D1")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DFE")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "Both of the higher ups here\x01",
            "have been soldiers since the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two of them have very different\x01",
            "personalities but both are extremely\x01",
            "calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially the Warrant Officer, who does\x01",
            "everything at his own pace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He seems as if he enjoys anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EA2")

    label("loc_2DFE")


    ChrTalk(
        0xFE,
        (
            "Both of the higher ups here\x01",
            "have been soldiers since the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two of them have very different\x01",
            "personalities but both are extremely\x01",
            "calm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA2")

    Jump("loc_30D1")

    label("loc_2EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2F4A")

    ChrTalk(
        0xFE,
        (
            "If the missing airliner turns out to\x01",
            "be the work of the Empire, I wonder\x01",
            "if we're looking at another war...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The very thought makes me shudder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2FFE")

    ChrTalk(
        0xFE,
        (
            "People are saying that this is the\x01",
            "first time we've been put on high\x01",
            "alert since the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When somebody tells me that,\x01",
            "it makes me really nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_30D1")

    ChrTalk(
        0xFE,
        (
            "The Eisen Road, which runs north off\x01",
            "the East Bose Highway, is blockaded\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For those heading to the north border,\x01",
            "they'll have to go to Bose first and\x01",
            "then wait until the road reopens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D1")

    TalkEnd(0xC)
    Return()

    # Function_10_2A17 end

    def Function_11_30D5(): pass

    label("Function_11_30D5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33CC")
    OP_A2(0x35F)
    OP_A2(0x4)

    ChrTalk(
        0x101,
        "#000F(Joshua, is this person...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(Yeah, he's a bracer just like us.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FUm, excuse me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FHello?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYo, Sting.\x01",
            "Sociable as ever, I see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "And you are...the bracer-in-\x01",
            "training from some time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FThat's right.\x02\x03",
            "Except now I have the title of\x01",
            "senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm...it appears I mistook you for\x01",
            "someone else. Are you working at\x01",
            "the Bose branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FYes. For now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all the recent incidents\x01",
            "going on, all the bracers in\x01",
            "Bose are out and about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm counting on you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 0)

    ChrTalk(
        0x101,
        (
            "#000F(So that was one of Schera's\x01",
            "acquaintances... He was a bit\x01",
            "scary if you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(But with the way he carries\x01",
            "himself ...he must be fairly\x01",
            "skilled.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BA")

    label("loc_33CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346A")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the 4th monster I've\x01",
            "dealt with today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure things will settle down\x01",
            "when Grant returns from the\x01",
            "Royal City...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BA")

    label("loc_346A")


    ChrTalk(
        0xFE,
        (
            "I'm sure things will settle down\x01",
            "when Grant returns from the\x01",
            "Royal City...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BA")

    TalkEnd(0xD)
    Return()

    # Function_11_30D5 end

    def Function_12_34BE(): pass

    label("Function_12_34BE")

    TalkBegin(0xE)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378F")
    OP_A2(0x360)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#814FIs that you, Scherazard...?\x02\x03",
            "#850FIt's been a long time, hasn't it?\x01",
            "Since we last trained, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FSpeak of the devil, Anelace.\x01",
            "What brings you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FWell, there was a request for a\x01",
            "monster extermination here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FIs that so... Well, we appreciate\x01",
            "you taking the time to come here.\x02\x03",
            "So were you able to master the\x01",
            "use of a sword?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#819FUh...let's avoid that subject right\x01",
            "now. I'm still working on it.\x02\x03",
            "#810FBy the way, Scherazard, are you\x01",
            "on a job for the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FSomething like that, although it's\x01",
            "a bit different than what you're on\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FReally...?\x02\x03",
            "This region has become extremely\x01",
            "dangerous lately.\x02\x03",
            "You be careful, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38ED")

    label("loc_378F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3870")
    OP_A2(0x5)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        "#850FAh, Scherazard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FDid you come here on a job, Anelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FYeah, there's been a boom of various\x01",
            "small-scale incidents going on.\x02\x03",
            "#856FThere are so many, I can't even\x01",
            "take a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38ED")

    label("loc_3870")


    ChrTalk(
        0xFE,
        (
            "#810FThere's been a boom of various\x01",
            "small-scale incidents going on.\x02\x03",
            "#856FThere are so many, I can't even\x01",
            "take a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38ED")

    TalkEnd(0xE)
    Return()

    # Function_12_34BE end

    def Function_13_38F1(): pass

    label("Function_13_38F1")

    EventBegin(0x0)
    Return()

    # Function_13_38F1 end

    SaveToFile()

Try(main)
