from ED6ScenarioHelper import *

def main():
    # 洛连特市长官邸

    CreateScenaFile(
        FileName            = 'T0210   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0210.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60010",
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
        'Mayor Klaus',                          # 9
        'Mylene',                               # 10
        'Lita',                                 # 11
        'Josette',                              # 12
        'Scherazard',                           # 13
        'Target Camera',                        # 14
        'Leaf',                                 # 15
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH01180 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02330 ._CH',             # 03
        'ED6_DT07/CH00020 ._CH',             # 04
        'ED6_DT07/CH02353 ._CH',             # 05
        'ED6_DT06/CH20034 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH01180P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02330P._CP',             # 03
        'ED6_DT07/CH00020P._CP',             # 04
        'ED6_DT07/CH02353P._CP',             # 05
        'ED6_DT06/CH20034P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
    )

    DeclNpc(
        X                   = 82247,
        Z                   = 0,
        Y                   = 2548,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 7138,
        Z                   = 0,
        Y                   = 64539,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 506,
        Z                   = 0,
        Y                   = -1811,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81266,
        Z                   = 0,
        Y                   = 53214,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 138350,
        Z                   = 50,
        Y                   = -52070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 851975,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -6321,
        Y                   = 0,
        Z                   = -3741,
        Range               = -3987,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE60E,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = 75880,
        TriggerZ            = 0,
        TriggerY            = 56920,
        TriggerRange        = 500,
        ActorX              = 75880,
        ActorZ              = 700,
        ActorY              = 56920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 138350,
        TriggerZ            = 0,
        TriggerY            = -52070,
        TriggerRange        = 500,
        ActorX              = 138350,
        ActorZ              = 0,
        ActorY              = -52070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 78710,
        TriggerZ            = 0,
        TriggerY            = 52510,
        TriggerRange        = 1800,
        ActorX              = 78710,
        ActorZ              = 1000,
        ActorY              = 52510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 77520,
        TriggerZ            = 0,
        TriggerY            = 50360,
        TriggerRange        = 500,
        ActorX              = 77520,
        ActorZ              = 900,
        ActorY              = 50360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 82150,
        TriggerZ            = 0,
        TriggerY            = 50830,
        TriggerRange        = 500,
        ActorX              = 82150,
        ActorZ              = 1200,
        ActorY              = 50830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 82490,
        TriggerZ            = 310,
        TriggerY            = 57230,
        TriggerRange        = 500,
        ActorX              = 82490,
        ActorZ              = 1200,
        ActorY              = 57230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 78330,
        TriggerZ            = 0,
        TriggerY            = 57050,
        TriggerRange        = 500,
        ActorX              = 78330,
        ActorZ              = 500,
        ActorY              = 57050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84700,
        TriggerZ            = 0,
        TriggerY            = 55320,
        TriggerRange        = 500,
        ActorX              = 84700,
        ActorZ              = 500,
        ActorY              = 55320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_34E",          # 00, 0
        "Function_1_5DC",          # 01, 1
        "Function_2_64B",          # 02, 2
        "Function_3_661",          # 03, 3
        "Function_4_15CA",         # 04, 4
        "Function_5_21D8",         # 05, 5
        "Function_6_2B19",         # 06, 6
        "Function_7_3D70",         # 07, 7
        "Function_8_4774",         # 08, 8
        "Function_9_49C7",         # 09, 9
        "Function_10_4C15",        # 0A, 10
        "Function_11_4D0B",        # 0B, 11
        "Function_12_4E27",        # 0C, 12
        "Function_13_4F1C",        # 0D, 13
        "Function_14_5012",        # 0E, 14
        "Function_15_50C0",        # 0F, 15
        "Function_16_517B",        # 10, 16
        "Function_17_5919",        # 11, 17
        "Function_18_5962",        # 12, 18
        "Function_19_6F37",        # 13, 19
        "Function_20_6F5A",        # 14, 20
        "Function_21_6F7B",        # 15, 21
        "Function_22_6F9E",        # 16, 22
        "Function_23_7B28",        # 17, 23
        "Function_24_7B44",        # 18, 24
        "Function_25_7B65",        # 19, 25
    )


    def Function_0_34E(): pass

    label("Function_0_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_37F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 200010, 0, 44420, 270)
    SetChrPos(0xA, 201860, 0, 1360, 90)
    Jump("loc_42E")

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3B0")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 200010, 0, 44420, 270)
    SetChrPos(0xA, 201860, 0, 1360, 90)
    Jump("loc_42E")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_3C9")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_42E")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3D8")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_42E")

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_409")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 201700, 0, 43930, 90)
    SetChrPos(0xA, 7130, 0, 64540, 0)
    Jump("loc_42E")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_422")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_42E")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_42E")
    ClearChrFlags(0x9, 0x80)

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_486")
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 7150, 200, -3320, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_486")
    SetChrPos(0xC, 5410, 0, -3320, 90)
    ClearChrFlags(0xC, 0x80)

    label("loc_486")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (112, "loc_49E"),
        (115, "loc_4F0"),
        (100, "loc_517"),
        (1, "loc_55F"),
        (SWITCH_DEFAULT, "loc_5DB"),
    )


    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9")
    OP_A2(0x24F)
    OP_28(0x3, 0x1, 0x200)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x4, 0x4, 0x40)
    OP_28(0x6, 0x4, 0x40)
    Event(0, 18)
    Jump("loc_4ED")

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED")
    SetChrPos(0x0, 84098, 0, 52559, 270)
    OP_69(0x0, 0x0)

    label("loc_4ED")

    Jump("loc_5DB")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514")
    SetChrPos(0x0, 75765, 0, 54963, 90)
    OP_69(0x0, 0x0)

    label("loc_514")

    Jump("loc_5DB")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    EventBegin(0x0)
    SetChrPos(0x101, -5800, 0, -3300, 0)
    SetChrPos(0x102, -4800, 0, -3300, 0)
    SetChrPos(0x8, -1180, 1750, 3000, 0)
    Event(0, 22)

    label("loc_55C")

    Jump("loc_5DB")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D8")
    SetChrPos(0x101, 81771, 0, 55487, 0)
    SetChrPos(0x102, 81444, 0, 54476, 0)
    SetChrPos(0x8, 83000, 0, 53344, 0)
    SetChrPos(0xC, 81266, 0, 53214, 0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x25A)
    OP_28(0x1A, 0x4, 0x4)
    OP_28(0x1A, 0x1, 0x1)
    OP_28(0x1A, 0x1, 0x2)
    ClearChrFlags(0xC, 0x80)
    OP_69(0x101, 0x0)
    Event(0, 16)

    label("loc_5D8")

    Jump("loc_5DB")

    label("loc_5DB")

    Return()

    # Function_0_34E end

    def Function_1_5DC(): pass

    label("Function_1_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4")
    OP_B1("t0210_y")
    Jump("loc_5FD")

    label("loc_5F4")

    OP_B1("t0210_n")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_614")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    Jump("loc_62C")

    label("loc_614")

    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 6)), scpexpr(EXPR_END)), "loc_627")
    OP_64(0x1, 0x1)
    Jump("loc_62C")

    label("loc_627")

    ClearChrFlags(0xE, 0x80)

    label("loc_62C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64A")

    Return()

    # Function_1_5DC end

    def Function_2_64B(): pass

    label("Function_2_64B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_660")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_64B")

    label("loc_660")

    Return()

    # Function_2_64B end

    def Function_3_661(): pass

    label("Function_3_661")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#600FOh, Estelle and Joshua.\x02\x03",
            "#600FYou've really been of great\x01",
            "service this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FI wish we could have done\x01",
            "more...\x02\x03",
            "#015FI'm really sorry that we let the\x01",
            "criminals get away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#601FNever mind that, the fact that you're\x01",
            "all safe and the crystal has been\x01",
            "recovered is good enough.\x02\x03",
            "#600FThe general theory seems to be that the\x01",
            "Sky Bandits who've been terrorizing the\x01",
            "Bose region are the culprits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FYeah, that seems to be what\x01",
            "we've gathered as well.\x02\x03",
            "I'm just so mad they got away\x01",
            "in their airship like that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#601FHa ha, you really can't lay a\x01",
            "hand on them if they're up in\x01",
            "the sky, though!\x02\x03",
            "#602FOn the subject of Bose, however...\x01",
            "I hear tell that an airliner\x01",
            "went missing there recently.\x02\x03",
            "I'm not sure of the exact details,\x01",
            "but I've been looking into it as\x01",
            "best as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#603FI don't think we should let these Sky\x01",
            "Bandits go unchecked, so I think I'll\x01",
            "make a call to the mayor of Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE0")

    label("loc_A32")


    ChrTalk(
        0xFE,
        (
            "#602FI'm concerned about the airliner that's\x01",
            "gone missing, and we shouldn't let\x01",
            "these Sky Bandits go unchecked.\x02\x03",
            "I think I'll make a call to the\x01",
            "mayor of Bose about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE0")

    Jump("loc_15C6")

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEE")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#600FI can't believe something like this\x01",
            "happened while I was away...\x02\x03",
            "I have also personally asked that\x01",
            "the guild conduct the investigation.\x02\x03",
            "I apologize for the short notice,\x01",
            "but your assistance in this matter\x01",
            "would be highly appreciated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_BEE")


    ChrTalk(
        0xFE,
        (
            "#600FI have also personally asked that\x01",
            "the guild conduct the investigation.\x02\x03",
            "I apologize for the short notice,\x01",
            "but your assistance in this matter\x01",
            "would be highly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    Jump("loc_15C6")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(
        0xFE,
        (
            "#600FThis is what things looked\x01",
            "like when I came home...\x02\x03",
            "I didn't get a glimpse of the\x01",
            "criminals either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDF")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#600FYou two did well in bringing back\x01",
            "the crystal safely.\x02\x03",
            "I hear you're really making a name\x01",
            "for yourselves.\x02\x03",
            "I'm looking forward to your future\x01",
            "success as bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_DDF")


    ChrTalk(
        0xFE,
        (
            "#600FI'm looking forward to your future\x01",
            "success as bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_15C6")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA8")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600FThe mine is to the north of Rolent\x01",
            "at the end of the Malga Trail.\x02\x03",
            "It shouldn't be too far\x01",
            "of a walk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0B")

    label("loc_EA8")


    ChrTalk(
        0xFE,
        (
            "#600FIf you show them this referral,\x01",
            "they should let you into the mine.\x02\x03",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0B")

    Jump("loc_15C6")

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_FAF")

    ChrTalk(
        0x8,
        (
            "#600FI hear something wonderful came\x01",
            "out of a new lode at the Malga\x01",
            "Mine.\x02\x03",
            "I've put in a request to the Bracer\x01",
            "Guild to transport it here, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1079")

    ChrTalk(
        0xFE,
        (
            "#600FI heard that a new lode was\x01",
            "discovered at the Malga Mine\x01",
            "to the north of here.\x02\x03",
            "And it seems that it's a pretty promising\x01",
            "deposit as well. This is definitely good\x01",
            "news for the mine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_1079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600FWhen I think about the days after the Hundred\x01",
            "Days War ended, there is something amazing\x01",
            "about the reconstruction of the Liberl Kingdom.\x02\x03",
            "Normalization of diplomatic ties with\x01",
            "the Empire, development of orbal\x01",
            "technology, fostering trade...\x02\x03",
            "Queen Alicia's political finesse is\x01",
            "really something else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120F")

    label("loc_11C4")


    ChrTalk(
        0x8,
        (
            "#600FI tell you...Queen Alicia's political\x01",
            "finesse is something else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120F")

    Jump("loc_15C6")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_139C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1316")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600FCompared to other cities, Rolent\x01",
            "is certainly rural with no distinct\x01",
            "features.\x02\x03",
            "However, I love this city.\x02\x03",
            "There's just something warm\x01",
            "and inviting about Rolent.\x02\x03",
            "I want to build a city that gives\x01",
            "importance to that atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1399")

    label("loc_1316")


    ChrTalk(
        0x8,
        (
            "#600FThere's just something warm\x01",
            "and inviting about Rolent.\x02\x03",
            "I want to build a city that gives\x01",
            "importance to that atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1399")

    Jump("loc_15C6")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1533")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#600FOh, good morning, Estelle and\x01",
            "Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGood morning, Mayor Klaus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FI've been hearing great things about the both\x01",
            "of you.\x02\x03",
            "So you're undergoing bracer training, are you?\x02\x03",
            "#601FHaving such youngsters sign up all\x01",
            "by themselves to become bracers\x01",
            "and protect everyone is inspiring!\x02\x03",
            "I expect great things out of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FWe'll do our best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C6")

    label("loc_1533")


    ChrTalk(
        0x8,
        (
            "#601FHaving such youngsters sign up all\x01",
            "by themselves to become bracers\x01",
            "and protect everyone is inspiring!\x02\x03",
            "I expect great things out of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C6")

    TalkEnd(0x8)
    Return()

    # Function_3_661 end

    def Function_4_15CA(): pass

    label("Function_4_15CA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1679")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "We suffered some damage,\x01",
            "but I'm glad nobody was hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything had happened to my\x01",
            "husband or Lita... It makes me\x01",
            "shudder to think of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_1679")


    ChrTalk(
        0xFE,
        (
            "I really appreciate what\x01",
            "you've done for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AB")

    Jump("loc_21D4")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1725")

    ChrTalk(
        0xFE,
        (
            "It looks like the intruders took off\x01",
            "with a bunch of preserved food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if they were hungry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_END)), "loc_19A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1938")
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)
    OP_A2(0x25C)
    OP_28(0x1A, 0x1, 0x20)

    ChrTalk(
        0x101,
        "#002FAre you all right, ma'am?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, I'm fine. The intruders weren't\x01",
            "violent toward us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIs there anything you noticed in\x01",
            "particular about the intruders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They were wearing masks, so\x01",
            "I wouldn't be able to tell you\x01",
            "about any specific features...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That reminds me. I'm certain\x01",
            "the front door was locked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I locked the door just to be safe since\x01",
            "my husband had gone to the chapel\x01",
            "and there were just the two of us here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder how in the world\x01",
            "they got in...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_19A5")

    label("loc_1938")


    ChrTalk(
        0x9,
        (
            "It looks like the intruders took off\x01",
            "with a bunch of preserved food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I wonder if they were hungry.\x02",
    )

    CloseMessageWindow()

    label("loc_19A5")

    Jump("loc_21D4")

    label("loc_19A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB1")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "It seems you're the ones who took\x01",
            "on my husband's request, are you\x01",
            "not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two of you are doing a\x01",
            "wonderful job for being so\x01",
            "young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if Cassius is away, if we've\x01",
            "got the two of you around, Rolent\x01",
            "has nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B16")

    label("loc_1AB1")


    ChrTalk(
        0xFE,
        (
            "Even if Cassius is away, if we've\x01",
            "got the two of you around, Rolent\x01",
            "has nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B16")

    Jump("loc_21D4")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE4")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "I heard from Lita that the vegetables\x01",
            "from the Perzel Farm haven't arrived...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what's going on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The vegetables from there have\x01",
            "such a delicious, fresh flavor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1BE4")


    ChrTalk(
        0xFE,
        (
            "I heard from Lita that the vegetables\x01",
            "from the Perzel Farm haven't arrived...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what's going on.\x02",
    )

    CloseMessageWindow()

    label("loc_1C56")

    Jump("loc_21D4")

    label("loc_1C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "Our son is working as a teacher\x01",
            "at the Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The house has felt quite spacious\x01",
            "since he left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But it's at times like these\x01",
            "when I feel a little lonely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9B")

    label("loc_1D24")


    ChrTalk(
        0xFE,
        (
            "Our son is working as a teacher\x01",
            "at the Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The house has felt quite spacious\x01",
            "since he left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9B")

    Jump("loc_21D4")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1F07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E83")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "Let's see, maybe I should start\x01",
            "making preparations for dinner\x01",
            "with Lita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today, I'm thinking about making\x01",
            "my husband's favorite corn cream\x01",
            "stew, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe I'd better check with\x01",
            "Lita first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1E83")


    ChrTalk(
        0x9,
        (
            "Today, I'm thinking about making\x01",
            "my husband's favorite corn cream\x01",
            "stew, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe I'd better check with\x01",
            "Lita first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F04")

    Jump("loc_21D4")

    label("loc_1F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_20DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2056")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "Lita takes care of all the\x01",
            "housework, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I feel a little awkward about it\x01",
            "and often end up doing some\x01",
            "of it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure it's because I used to\x01",
            "do it all myself before coming\x01",
            "to live at this house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It appears like I'm taking Lita's\x01",
            "job away, so I wonder if I'm\x01",
            "causing her any trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_2056")


    ChrTalk(
        0x9,
        (
            "Lita takes care of all the\x01",
            "housework, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I feel a little awkward about it\x01",
            "and often end up doing some\x01",
            "of it myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D8")

    Jump("loc_21D4")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2192")
    OP_A2(0x1)

    ChrTalk(
        0x101,
        "#000FGood morning, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, good morning to the two\x01",
            "of you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Why are you out so early in the\x01",
            "morning? That must be tough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_2192")


    ChrTalk(
        0x9,
        (
            "Why are you out so early in the\x01",
            "morning? That must be tough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D4")

    TalkEnd(0x9)
    Return()

    # Function_4_15CA end

    def Function_5_21D8(): pass

    label("Function_5_21D8")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_22F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "I finally got the study all\x01",
            "cleaned up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It makes me so angry...\x01",
            "I spend so much time keeping\x01",
            "this place clean every day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F5")

    label("loc_2273")


    ChrTalk(
        0xFE,
        (
            "If I ever find these criminals, they're going\x01",
            "to get a rag to the face and the business end\x01",
            "of my broom somewhere sensitive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F5")

    Jump("loc_2B15")

    label("loc_22F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_END)), "loc_2553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247F")
    EventBegin(0x0)
    OP_69(0xA, 0x3E8)
    OP_A2(0x25B)
    OP_28(0x1A, 0x1, 0x10)

    ChrTalk(
        0xA,
        "I had such a scare!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I was cleaning up the attic when\x01",
            "suddenly a bunch of masked men\x01",
            "came barging in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FMasked 'men', huh?\x01",
            "That means this wasn't\x01",
            "a one-man job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FHow many people were in\x01",
            "the group?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm...I'd probably guess\x01",
            "about 3 or 4.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, that reminds me.\x01",
            "One of them was short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It might have even been a girl.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_2550")

    label("loc_247F")


    ChrTalk(
        0xA,
        (
            "When I think about the fact that\x01",
            "I'm going to have to clean up that\x01",
            "study, my head starts to spin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When I get my hands on those\x01",
            "criminals, I'm going to give them\x01",
            "a beating like they'll never forget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2550")

    Jump("loc_2B15")

    label("loc_2553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_26DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2648")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "Let's see, I guess I'll get to work\x01",
            "cleaning the attic next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That room's dark and sometimes\x01",
            "has rats. Oooh, they just give me the\x01",
            "shivers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not afraid of ghosts,\x01",
            "but I hate rats with a passion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DA")

    label("loc_2648")


    ChrTalk(
        0xFE,
        (
            "Let's see, I guess I'll get to work\x01",
            "cleaning the attic next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That room's dark and sometimes\x01",
            "it has rats which just give me the\x01",
            "shivers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DA")

    Jump("loc_2B15")

    label("loc_26DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_2771")

    ChrTalk(
        0xFE,
        (
            "Right now, the mayor's in his\x01",
            "study with a visitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you've got business with the\x01",
            "mayor, then please be quiet\x01",
            "when you enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_2771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_283B")

    ChrTalk(
        0xFE,
        (
            "It seems like the Perzel Farm's\x01",
            "vegetables are finally going to\x01",
            "be shipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By any measure, the weather\x01",
            "certainly hasn't been bad this\x01",
            "year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if something happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2845")
    Jump("loc_2B15")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_28C1")

    ChrTalk(
        0xA,
        (
            "Hmm...I wonder what I should\x01",
            "do about the menu this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Maybe I should discuss it with\x01",
            "the missus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_28C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_29FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A6")
    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "The missus sometimes helps me\x01",
            "with my jobs around the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On top of that, she treats me\x01",
            "like I'm a part of the family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She even took me out to eat\x01",
            "the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I couldn't be happier!\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FB")

    label("loc_29A6")


    ChrTalk(
        0xA,
        (
            "The missus treats me like\x01",
            "I'm a part of the family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I couldn't be happier!\x02",
    )

    CloseMessageWindow()

    label("loc_29FB")

    Jump("loc_2B15")

    label("loc_29FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB6")
    OP_A2(0x2)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "I am so busy, busy, busy.\x01",
            "This mansion is quite big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've got the serving, cleaning,\x01",
            "and washing to do. Mornings\x01",
            "are so busy for a maid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B15")

    label("loc_2AB6")


    ChrTalk(
        0xA,
        "Today's objective!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To finish the cleaning before the missus\x01",
            "returns from the chapel!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B15")

    TalkEnd(0xA)
    Return()

    # Function_5_21D8 end

    def Function_6_2B19(): pass

    label("Function_6_2B19")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CBA")
    EventBegin(0x0)

    ChrTalk(
        0xC,
        (
            "#020FI had the mayor run me through\x01",
            "all the details.\x02\x03",
            "#020FHow about you two, did you\x01",
            "find anything?\x02",
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
            "We're going to look around a bit longer.\x01",      # 0
            "Yep, we found lots of new evidence!\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2C46"),
        (0, "loc_3C57"),
        (SWITCH_DEFAULT, "loc_3CB7"),
    )


    label("loc_2C46")

    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, 4720, 0, -2800, 90)
    SetChrPos(0x102, 5720, 0, -3920, 0)
    SetChrPos(0xC, 6370, 0, -2250, 225)
    OP_6D(6020, 0, -2610, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#020FAll right...then let's check the\x01",
            "details one by one and see\x01",
            "what you've come up with.\x02\x03",
            "#020FFirst off, what were the criminals\x01",
            "after?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Something that could be sold for mira.]\x01",      # 0
            "[The septium in the safe.]\x01",                    # 1
            "[The food preserves from the kitchen.]\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DEF"),
        (1, "loc_2E00"),
        (2, "loc_2E11"),
        (SWITCH_DEFAULT, "loc_2E22"),
    )


    label("loc_2DEF")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E22")

    label("loc_2E00")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E22")

    label("loc_2E11")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E22")

    label("loc_2E22")


    ChrTalk(
        0xC,
        "#020FHow many of them were there?\x02",
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
            "[There was a group of 2, a guy and a girl.]\x01",       # 0
            "[There was a group of 3 or 4.]\x01",                    # 1
            "[The crime was carried out by a lone woman.]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F16"),
        (1, "loc_2F27"),
        (2, "loc_2F38"),
        (SWITCH_DEFAULT, "loc_2F49"),
    )


    label("loc_2F16")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F49")

    label("loc_2F27")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F49")

    label("loc_2F38")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F49")

    label("loc_2F49")


    ChrTalk(
        0xC,
        (
            "#020FWhere did they get into the\x01",
            "house from?\x02",
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
            "[From the 1st floor window.]\x01",              # 0
            "[They picked the front door lock.]\x01",        # 1
            "[From the terrace on the 2nd floor.]\x01",      # 2
            "[Through the roof into the attic.]\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_305C"),
        (1, "loc_306D"),
        (2, "loc_3070"),
        (3, "loc_3081"),
        (SWITCH_DEFAULT, "loc_3084"),
    )


    label("loc_305C")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3084")

    label("loc_306D")

    Jump("loc_3084")

    label("loc_3070")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3084")

    label("loc_3081")

    Jump("loc_3084")

    label("loc_3084")


    ChrTalk(
        0xC,
        (
            "#020FPoint-blank, what is the portrait\x01",
            "of those thought to have committed\x01",
            "the crime?\x02",
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
            "[Citizens coming and going during the day.]\x01",      # 0
            "[Relatives of Mayor Klaus.]\x01",                      # 1
            "[Somebody who works at the Malga Mine.]\x01",          # 2
            "[A traveler who visited recently.]\x01",               # 3
            "[None of the above.]\x01",                             # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31E3"),
        (1, "loc_31F4"),
        (2, "loc_3205"),
        (3, "loc_3216"),
        (4, "loc_3227"),
        (SWITCH_DEFAULT, "loc_322A"),
    )


    label("loc_31E3")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_31F4")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_3205")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_3216")

    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322A")

    label("loc_3227")

    Jump("loc_322A")

    label("loc_322A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CA")
    OP_2B(0x1A, 0x4)
    OP_28(0x1A, 0x1, 0x8000)

    ChrTalk(
        0xC,
        (
            "#021FWow, you did a good job investigating.\x01",
            "It looks like we'll be able to specify who\x01",
            "the criminals are with this information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FD")

    label("loc_32CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3378")
    OP_2B(0x1A, 0x2)
    OP_28(0x1A, 0x1, 0x4000)

    ChrTalk(
        0xC,
        (
            "#020FWell, I guess you did a decent enough\x01",
            "job. It looks like we'll be able to specify\x01",
            "who the criminals are with this information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FD")

    label("loc_3378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_33FD")
    OP_28(0x1A, 0x1, 0x2000)

    ChrTalk(
        0xC,
        (
            "#025FA few things don't add up, but we\x01",
            "might be able to specify who the\x01",
            "criminals are with this information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FD")

    TurnDirection(0xC, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0xC,
        (
            "#022FMayor Klaus...\x02\x03",
            "#022FOver the past two or three days,\x01",
            "have you had any new faces in\x01",
            "your study?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#604FWhen you put it that way,\x01",
            "I guess there's been a number\x01",
            "of people...\x02\x03",
            "That reporter from the magazine\x01",
            "company was one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOh, so those two came to visit\x01",
            "you too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FBut at the time of the crime, they\x01",
            "were with us at the Esmelas Tower.\x02\x03",
            "#012FI think we can cross them off\x01",
            "the list of suspects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020FI see...so, Mayor Klaus, were\x01",
            "there any others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FOther than that...there was\x01",
            "only Josette.\x02\x03",
            "#601FHa ha ha, but let's not kid\x01",
            "ourselves here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FHa ha, I think it'd be a bit of a\x01",
            "stretch for her to be our thief.\x02\x03",
            "#001FAfter all, she's a student at the\x01",
            "Royal Academy.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 225, 400)

    ChrTalk(
        0xC,
        (
            "#022FCriminals aren't always dressed\x01",
            "so they can be easily spotted.\x02\x03",
            "#022FAs for a school uniform, if\x01",
            "someone put their mind to it,\x01",
            "they could create a replica.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        (
            "#000FBut I'm telling you, she was a\x01",
            "really nice girl. She was modest\x01",
            "and courteous...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001FRight, Joshua?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015FI'm sorry to say this,\x01",
            "but I completely disagree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FDuring that time-- when the mayor\x01",
            "put the septium into the safe...\x02\x03",
            "#012FThat girl's eyes lit up like a\x01",
            "hunter's, eyeing her prey.\x02\x03",
            "#012FOf course, since I had no conclusive\x01",
            "evidence, I couldn't call her out on\x01",
            "it...\x02\x03",
            "#012FBut at least to me, she didn't\x01",
            "look like any ordinary student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003FY-You must be joking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#602FUnbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#022FAt any rate, it looks like we're\x01",
            "going to have to ask this girl\x01",
            "a few questions.\x02\x03",
            "#022FYou wouldn't happen to know\x01",
            "where she is, would you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 0)
    Sleep(300)
    TurnDirection(0x102, 0xC, 0)

    ChrTalk(
        0x101,
        (
            "#002FIf I remember right, she should\x01",
            "be staying at the hotel...\x02\x03",
            "#002FBut she said something about taking\x01",
            "off from Rolent sometime today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#026FHm, well it looks like we're going\x01",
            "to have to hurry then.\x02\x03",
            "#024FEstelle, Joshua.\x01",
            "Let's try the hotel first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FR-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FUnderstood.\x02",
    )

    CloseMessageWindow()

    def lambda_3BB7():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3BB7)
    SetChrFlags(0xC, 0x40)
    OP_92(0xC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    OP_A2(0x261)
    OP_28(0x1A, 0x1, 0x200)
    OP_28(0x1B, 0x4, 0x4)
    OP_28(0x1B, 0x1, 0x1)
    OP_28(0x1B, 0x1, 0x2)
    OP_20(0x5DC)
    EventEnd(0x0)
    OP_31(0x2, 0x0, 0xC)
    OP_B5(0x2, 0x0)
    OP_B5(0x2, 0x1)
    OP_B5(0x2, 0x5)
    OP_B5(0x2, 0x4)
    OP_41(0x2, 0x3D)
    OP_41(0x2, 0xF2)
    OP_41(0x2, 0x110)
    OP_41(0x2, 0x26D, 0x0)
    OP_41(0x2, 0x26A, 0x1)
    OP_41(0x2, 0x25E, 0x5)
    OP_41(0x2, 0x267, 0x4)
    OP_35(0x2, 0xAA)
    OP_36(0x2, 0xF0)
    AddParty(0x2, 0xFF)
    ClearMapFlags(0x800)
    OP_21()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1E()
    Jump("loc_3CB7")

    label("loc_3C57")


    ChrTalk(
        0xC,
        (
            "#020FThen how about you go and\x01",
            "look again? But remember,\x01",
            "we're running short on time.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_3CB7")

    label("loc_3CB7")

    Jump("loc_3D6C")

    label("loc_3CBA")


    ChrTalk(
        0xC,
        (
            "#020FAre you really done investigating?\x01",
            "It seems a little too quick to me.\x02\x03",
            "#020FHow about looking around a little\x01",
            "more carefully. I'm sure there's\x01",
            "something you've missed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6C")

    TalkEnd(0xC)
    Return()

    # Function_6_2B19 end

    def Function_7_3D70(): pass

    label("Function_7_3D70")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470F")
    Fade(1000)
    SetChrPos(0x101, 75500, 0, 55990, 0)
    SetChrPos(0x102, 76250, 0, 55794, 315)
    OP_6D(76000, 0, 56380, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F#3PThe gift that we delivered to the\x01",
            "mayor for the queen is...\x02\x03",
            "#005FThose crooks are not gonna get\x01",
            "away with this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4PIt doesn't look like they jimmied\x01",
            "the door either.\x02\x03",
            "#012FThey must've decrypted the\x01",
            "combination and opened it or...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F#3PCould they really have cracked\x01",
            "the combination?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4PIt's not impossible, but I imagine\x01",
            "that it'd be difficult for anyone\x01",
            "besides a skilled pro.\x02\x03",
            "#012FMy best guess is that they figured\x01",
            "out the combination using a much\x01",
            "simpler means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#3PWhat do you mean by simpler\x01",
            "means...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4PWell, let's see...\x02\x03",
            "#012FThey could have, for example, dusted\x01",
            "the buttons with a special powder.\x02\x03",
            "#012FA powder like that would have absorptive\x01",
            "properties, and due to its fineness, it\x01",
            "would be invisible to the naked eye.\x02\x03",
            "#012FHowever, if a blue light were placed\x01",
            "over it, it would glow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#3PAll right, and...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PNow let's imagine for a minute that\x01",
            "the mayor entered the combination\x01",
            "with the powder present.\x02\x03",
            "#015FThe powder on the buttons would\x01",
            "stick to his fingers and come off.\x02\x03",
            "#015FThis would be one way to know\x01",
            "which buttons were pressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#3PNow wait a minute. Wouldn't they\x01",
            "still not know the order in which\x01",
            "the buttons were pressed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4PThat's not exactly the case.\x02\x03",
            "#012FAs the powder collected on the\x01",
            "fingers increased, the amount taken\x01",
            "from the buttons would decrease.\x02\x03",
            "#012FIn other words, the crooks could press\x01",
            "the buttons in order starting from\x01",
            "the least luminescent.\x02\x03",
            "#012FIt might be a little more difficult if there were\x01",
            "duplicate numbers, but the crooks should be able\x01",
            "to make a pretty good guess as to what they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3PThat makes sense...\x01",
            "Joshua, are you a genius\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4PThat's just basic knowledge.\x01",
            "Anyway, let's check out the buttons.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44CF():
        OP_6D(77550, 0, 56660, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44CF)
    OP_8E(0x102, 0x12E8A, 0x0, 0xDAE8, 0x7D0, 0x0)
    OP_8E(0x102, 0x12DCC, 0x0, 0xDE8D, 0x7D0, 0x0)
    OP_8C(0x102, 225, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x101, 0x12CE6, 0x0, 0xD9EE, 0x7D0, 0x0)
    OP_8E(0x101, 0x12F98, 0x0, 0xDC5A, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(2000)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#012F#3PJust as I thought. Powder was used.\x02\x03",
            "#012FNow there's no doubt in my mind\x01",
            "that this safe was opened using\x01",
            "the same method I just explained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4POh, right...\x02\x03",
            "#006FNow the big question is: Who dusted\x01",
            "the buttons with that powder?\x02\x03",
            "#006FWe know it would have to at least be\x01",
            "someone who visited the residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#3PRight. Now, figuring out who that IS...\x01",
            "That's going to be the tricky part.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25D)
    OP_28(0x1A, 0x1, 0x4)
    OP_28(0x1A, 0x1, 0x8)
    EventEnd(0x0)
    Jump("loc_4773")

    label("loc_470F")


    ChrTalk(
        0x102,
        (
            "#010FWe've already worked out how the\x01",
            "crooks opened the safe, so let's\x01",
            "check somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)

    label("loc_4773")

    Return()

    # Function_7_3D70 end

    def Function_8_4774(): pass

    label("Function_8_4774")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4788")
    Jump("loc_49C1")

    label("loc_4788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F9")
    EventBegin(0x1)

    ChrTalk(
        0x102,
        (
            "#012FEstelle, let's check around the\x01",
            "inside of the residence first.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_49C1")

    label("loc_47F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4938")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -5150, 0, -3680, 180)
    SetChrPos(0x102, -5810, 0, -2850, 180)
    OP_6D(-5150, 0, -2820, 1000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002FThey said that the door was locked\x01",
            "at the time of the burglary, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#002FIt doesn't look like the lock's been\x01",
            "broken, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWhich means...they got in\x01",
            "another way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25F)
    OP_28(0x1A, 0x1, 0x40)
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_49C1")

    label("loc_4938")

    EventBegin(0x1)

    ChrTalk(
        0x102,
        (
            "#012FIt doesn't look like the crooks came\x01",
            "in through the front door.\x02\x03",
            "#012FLet's check somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_49C1")

    ClearMapFlags(0x80)
    Return()

    # Function_8_4774 end

    def Function_9_49C7(): pass

    label("Function_9_49C7")

    EventBegin(0x0)
    OP_A2(0x25E)
    OP_28(0x1A, 0x1, 0x100)

    ChrTalk(
        0x101,
        "#004FHuh? What's this?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrFlags(0xE, 0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found \x07\x02",
            "Servais Leaf\x07\x00",
            ".  \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32A, 1)
    ClearMapFlags(0x1)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x320)

    ChrTalk(
        0x101,
        (
            "#505FDon't you think it's a bit strange for\x01",
            "a leaf to be in a place like this?\x02\x03",
            "On top of that, it's not a type\x01",
            "that grows around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYou're sharp, Estelle.\x02\x03",
            "#010FThis is the place where the residents\x01",
            "were locked up.\x02\x03",
            "#010FIt was probably dropped by one of\x01",
            "the criminals as they were locking\x01",
            "everybody up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FSo it's a key piece of material\x01",
            "evidence, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1, 0x1)
    EventEnd(0x1)
    Return()

    # Function_9_49C7 end

    def Function_10_4C15(): pass

    label("Function_10_4C15")

    EventBegin(0x0)
    OP_6D(78710, 0, 52510, 1000)

    ChrTalk(
        0x101,
        (
            "#002FThis place is all torn apart.\x02\x03",
            "Lita would probably faint if she\x01",
            "saw this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt looks like all the books on the shelf\x01",
            "have been scattered about the room.\x02\x03",
            "It seems kind of senseless to have\x01",
            "done all this...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_10_4C15 end

    def Function_11_4D0B(): pass

    label("Function_11_4D0B")

    EventBegin(0x0)
    OP_6D(77520, 0, 50360, 1000)

    ChrTalk(
        0x101,
        (
            "#000FThere are several documents\x01",
            "inside the drawer...\x02\x03",
            "They don't appear to have\x01",
            "been disturbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThey seem to be documents regarding\x01",
            "Rolent City's government.\x02\x03",
            "The fact that these are as they are\x01",
            "suggests that there was no political\x01",
            "aim involved.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_11_4D0B end

    def Function_12_4E27(): pass

    label("Function_12_4E27")

    EventBegin(0x0)
    OP_6D(82150, 0, 50830, 1000)

    ChrTalk(
        0x101,
        (
            "#008FIt's just like the mayor to have\x01",
            "a ton of difficult books like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt looks like he's got some valuable\x01",
            "antique books here as well.\x02\x03",
            "The criminals either had no idea\x01",
            "about the value of the books or...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_12_4E27 end

    def Function_13_4F1C(): pass

    label("Function_13_4F1C")

    EventBegin(0x0)
    OP_6D(82490, 310, 57230, 1000)

    ChrTalk(
        0x101,
        (
            "#008FIt's just like the mayor to have\x01",
            "a ton of difficult books like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt looks like he's got some valuable\x01",
            "antique books here as well.\x02\x03",
            "The criminals either had no idea\x01",
            "about the value of the books, or...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_13_4F1C end

    def Function_14_5012(): pass

    label("Function_14_5012")

    EventBegin(0x0)
    OP_6D(78330, 0, 57050, 1000)

    ChrTalk(
        0x101,
        (
            "#000FThis pot's been tipped over,\x01",
            "but there's nothing inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt looks like it only tipped over after\x01",
            "being hit by something with force.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_14_5012 end

    def Function_15_50C0(): pass

    label("Function_15_50C0")

    EventBegin(0x0)
    OP_6D(84700, 0, 55320, 1000)

    ChrTalk(
        0x101,
        (
            "#002FThis is just a clutter box, right?\x01",
            "It's empty as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThe box lock looks like it was\x01",
            "burned off...\x02\x03",
            "The criminals may have used an\x01",
            "orbal gun.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_15_50C0 end

    def Function_16_517B(): pass

    label("Function_16_517B")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_44(0x8, 0xFF)
    OP_44(0xC, 0xFF)
    FadeToBright(2000, 0)
    OP_6B(2600, 0)
    OP_6D(82702, 0, 54610, 0)
    OP_8C(0x101, 315, 0)
    OP_8C(0x102, 270, 0)
    OP_8C(0x8, 270, 0)
    OP_8C(0xC, 225, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        "#004FWow, this place is an absolute mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#023FThe crooks really tore through here...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0xC, 270, 0)
    OP_6D(79224, 0, 54590, 1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x101, 0x13986, 0x0, 0xD8E0, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        "#004FLook at the safe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603FThe septium, which was supposed to\x01",
            "be given to Her Majesty the Queen,\x01",
            "has been stolen.\x02\x03",
            "I'm really sorry, especially after having\x01",
            "you go to all the trouble to bring it here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 0)
    OP_69(0x102, 0x320)

    ChrTalk(
        0x102,
        (
            "#012FIt's not you who should be apologizing.\x01",
            "It's the crooks who are in the wrong.\x02\x03",
            "#012FBy the way...how are the other rooms\x01",
            "in the house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#602FThe other rooms for the most part\x01",
            "appear to have been left untouched.\x02\x03",
            "They're about as messy as the attic\x01",
            "room in which my wife and Lita were\x01",
            "locked up in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#026FHmmm...\x02\x03",
            "#026F...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        (
            "#022FEstelle, Joshua. There's something\x01",
            "I want you to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    TurnDirection(0x102, 0xC, 400)

    ChrTalk(
        0x101,
        "#002FWhich is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#022FI'll speak with the mayor about\x01",
            "the incident.\x02\x03",
            "#022FI want you two to check out the\x01",
            "inside of the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FYou mean like...an on-site investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FAre you sure we're up to the task?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020FSince we're all here, splitting up\x01",
            "WOULD be the best way to cover the\x01",
            "most ground, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FAll right. We'll see what we can do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#020FProceed carefully and deliberately.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 400)

    ChrTalk(
        0xC,
        (
            "#020FAll right, Mayor Klaus.\x01",
            "How about we talk in the parlor?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 400)

    ChrTalk(
        0x8,
        "#602FSure. Now, where to begin...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_43(0x8, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_8E(0xC, 0x14A14, 0x0, 0xCF26, 0x7D0, 0x0)
    SetChrFlags(0xC, 0x4)
    OP_8E(0xC, 0x154BE, 0x0, 0xCF26, 0x7D0, 0x0)
    OP_72(0x3, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x3, 9)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_71(0x3, 0x800)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x8, 4994, 0, -8380, 315)
    SetChrPos(0xC, 3173, 0, -5730, 135)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x320)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006FAn on-site investigation, huh?\x01",
            "I'm starting to get butterflies\x01",
            "in my stomach.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012FHow about we start from\x01",
            "this room?\x02\x03",
            "#012FAnd let's not forget to ask for witness\x01",
            "statements from the other residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FSounds like a plan!\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    EventEnd(0x0)
    OP_21()
    SetMapFlags(0x800)
    OP_1D(0x57)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_517B end

    def Function_17_5919(): pass

    label("Function_17_5919")

    Sleep(100)
    OP_8E(0x8, 0x14A14, 0x0, 0xCF26, 0x7D0, 0x0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x9)
    OP_73(0x3)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x154BE, 0x0, 0xCF26, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_17_5919 end

    def Function_18_5962(): pass

    label("Function_18_5962")

    ClearChrFlags(0xB, 0x80)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetMapFlags(0x400000)
    OP_6D(80120, 0, 270, 0)
    OP_6B(3000, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 78100, 200, -950, 90)
    SetChrPos(0xB, 80250, 0, -950, 270)
    SetChrPos(0x101, 84060, 0, -150, 270)
    SetChrPos(0x102, 84240, 0, -950, 270)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(
        0xB,
        "Girl in Uniform",
        (
            "#217FI see... I would never have imagined that\x01",
            "the clock tower had such an anecdote\x01",
            "to go with it.\x02\x03",
            "I'm totally blown away after hearing that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603FWith war, it's easy to speak of tragedy.\x02\x03",
            "But I think what's important is the\x01",
            "strength to overcome the pain and\x01",
            "establish peace.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#604FWell, who do we have here...?\x02",
    )

    CloseMessageWindow()
    OP_43(0x102, 0x1, 0x0, 0x14)
    OP_8E(0x101, 0x13F9C, 0x0, 0x362, 0xBB8, 0x0)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000F#3PWe've come to deliver the object\x01",
            "you requested.\x02\x03",
            "#000FUm, did we catch you in the\x01",
            "middle of something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601FOh, Estelle and Joshua.\x01",
            "You're no trouble at all.\x02\x03",
            "#601FIn fact, you've come at a good time.\x01",
            "Let me introduce you to my guest.\x02\x03",
            "#601FThis is Josette. She's a student\x01",
            "at the Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#3PThe Jenis Royal Academy...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xB, 400)

    ChrTalk(
        0x102,
        (
            "#010FI've heard of it before.\x02\x03",
            "#010FIt's a boarding school for higher education\x01",
            "in the Ruan region, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#218FYes, that's right.\x02\x03",
            "It's a pleasure to meet you.\x01",
            "My name is Josette Haar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#3PI'm Estelle.\x01",
            "It's nice to meet you, Josette.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYou can call me Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FThe two of them are actually bracers.\x02\x03",
            "I had asked them to do a personal\x01",
            "job for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#217FBracers?!\x02\x03",
            "You mean the proud knights of freedom\x01",
            "who love peace above all else and do\x01",
            "not succumb to any power?!\x02\x03",
            "#218FThis is such an inspiring moment!\x01",
            "I never thought I'd run into any real\x01",
            "bracers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#3PThe inspiring part sounds a little much...\x02\x03",
            "#008FBy the way, is it all right if I just call\x01",
            "you Josette?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#218FYes, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3PSo why did you come to Rolent?\x01",
            "Are you a friend of the mayor's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217FNo, today is actually the first time\x01",
            "we've ever met.\x02\x03",
            "I'm researching the important cultural\x01",
            "assets of each region as a part of my\x01",
            "independent studies.\x02\x03",
            "And although I thought he might be\x01",
            "busy, I've been lucky enough to get\x01",
            "an audience with the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3PYou're really serious about your\x01",
            "studies, aren't you?\x02\x03",
            "#000FMaybe we're intruding a bit, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217FNo, I've already asked the mayor\x01",
            "enough questions.\x02\x03",
            "#217FInstead...maybe it is I who am\x01",
            "in the way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)

    ChrTalk(
        0x8,
        (
            "#600FDon't be silly. It's not like that at all.\x02\x03",
            "#600FEstelle, this is a great opportunity,\x01",
            "so how about showing her what\x01",
            "you've brought with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#3PSure. Hold on a second...\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_8E(0x102, 0x13826, 0x0, 0x17C, 0xBB8, 0x0)
    SetChrSubChip(0x8, 1)
    OP_8C(0x102, 225, 400)
    Sleep(1000)
    OP_22(0x80, 0x0, 0x64)
    SetChrChipByIndex(0x101, 6)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#217FOh, my word...!\x01",
            "That's septium, right?\x02\x03",
            "#217FWhat a wonderful glow it gives off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601FYes, and its size is impressive, too.\x02\x03",
            "This is, indeed, a gift worthy of expressing\x01",
            "the appreciation of all Rolent's citizens.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#3PA gift?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PWorthy of expressing our appreciation...\x02\x03",
            "#019FI see. So this is a gift for\x01",
            "the queen's anniversary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601FYou're sharp, Joshua.\x02\x03",
            "I intend to send an engraved orbment\x01",
            "using this to the queen.\x02\x03",
            "As a token of Rolent's citizens'\x01",
            "appreciation to Her Majesty,\x01",
            "who will be turning 60 years old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3PSo it's a present for the queen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#218FHow delightful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FWe, as citizens of Liberl, owe\x01",
            "Her Majesty a great debt for\x01",
            "all she has done for us.\x02\x03",
            "In fact, the reason why we can use an\x01",
            "airliner with such ease is because of\x01",
            "the support of the Royal Family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PI've even heard that the Bracer Guild\x01",
            "in Liberl has received support from\x01",
            "the Royal Family.\x02\x03",
            "#010FWe do owe her a great debt\x01",
            "of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3PWow! That's pretty amazing!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F#3PAnd can you believe it, Joshua?\x02\x03",
            "#001FWe carried a present for the queen\x01",
            "with these very hands!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#011F#4PAnd what's more, you ran around with\x01",
            "it in those hands like a wild maniac.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008F#3PYou weren't supposed to tell anyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#218FHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601FHa ha ha. I wouldn't have imagined\x01",
            "anything less from you, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F#3PY-You guys...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0xB, 0x8, 400)
    OP_43(0x8, 0x1, 0x0, 0x13)

    ChrTalk(
        0x101,
        (
            "#000F#3PHere you go, Mayor Klaus.\x01",
            "It has been faithfully delivered.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Gave \x07\x02",
            "Septium Crystal\x07\x00",
            " to the mayor.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x323, 1)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x101, 65535)

    ChrTalk(
        0x8,
        (
            "#602FThank you very much.\x02\x03",
            "And as a matter of precaution...\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x8, 77740, 0, -250, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_8E(0x8, 0x12732, 0x0, 0x762, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    OP_44(0x8, 0xFF)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x68)
    OP_73(0x4)
    Sleep(500)
    SetChrFlags(0x8, 0x4)
    OP_8F(0x8, 0x128C2, 0x0, 0x9CE, 0x7D0, 0x0)
    OP_82(0x0, 0x2)
    Sleep(200)
    PlayEffect(0x0, 0x1, 0xFF, 75970, 500, 3330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_8F(0x8, 0x12732, 0x0, 0x762, 0x7D0, 0x0)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0x4, 104)
    OP_70(0x4, 0x0)
    Sleep(500)
    OP_82(0x1, 0x2)
    OP_73(0x4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#603FOkay. It'll be safe in there.\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x13)
    OP_8E(0x8, 0x12FAC, 0x0, 0xFFFFFF06, 0x7D0, 0x0)
    Fade(1000)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 78100, 200, -950, 90)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#601FNow all that's left is to have Melders\x01",
            "Orbal Factory finish up the engraving\x01",
            "on its orbment!\x02\x03",
            "I can't wait to see what it'll look\x01",
            "like when it's done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3PDon't hog it all to yourself when\x01",
            "you do!\x02\x03",
            "#000FLet me see it too when it's\x01",
            "finished, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217FIt's too bad I won't be here to\x01",
            "see it for myself.\x02\x03",
            "#218FBut today I was lucky enough to\x01",
            "speak with the mayor and see\x01",
            "something as beautiful as that.\x02\x03",
            "How shall I ever thank you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FDon't mention it. This is all part\x01",
            "of my job as a mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#217FThank you for everything.\x02\x03",
            "But I think it's time for me to\x01",
            "say goodbye.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#000F#3PI think we should be going ourselves.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(
        0x102,
        (
            "#010F#4PAgreed.\x02\x03",
            "#010FHave a nice day, Mayor Klaus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#601FYourselves as well.\x02",
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0200   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_18_5962 end

    def Function_19_6F37(): pass

    label("Function_19_6F37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F59")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0xB, 0xFE, 0)
    OP_48()
    Jump("Function_19_6F37")

    label("loc_6F59")

    Return()

    # Function_19_6F37 end

    def Function_20_6F5A(): pass

    label("Function_20_6F5A")

    Sleep(500)
    OP_8E(0x102, 0x14190, 0x0, 0xFFFFFFEC, 0xBB8, 0x0)
    TurnDirection(0x102, 0x8, 0)
    Return()

    # Function_20_6F5A end

    def Function_21_6F7B(): pass

    label("Function_21_6F7B")

    OP_8E(0x101, 0x133F8, 0x0, 0x190, 0xBB8, 0x0)
    OP_8C(0x101, 180, 400)
    TurnDirection(0xB, 0x101, 400)
    Return()

    # Function_21_6F7B end

    def Function_22_6F9E(): pass

    label("Function_22_6F9E")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x8, 0xFF)
    ClearMapFlags(0x1)
    OP_6D(-5266, 0, -1110, 0)
    OP_0D()
    OP_A2(0x23B)
    OP_28(0x3, 0x1, 0x2)
    OP_28(0x3, 0x1, 0x4)

    ChrTalk(
        0x101,
        (
            "#006FDo you think the mayor's even\x01",
            "in today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FBeing as busy as he is, I'm sure\x01",
            "there's a pretty good chance that\x01",
            "he's out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWell, bless my soul.\x01",
            "If it isn't Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 0)
    OP_6D(-2250, 1750, 3170, 2000)

    ChrTalk(
        0x101,
        "#001F#5PHi, Mayor Klaus.\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x19)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_6D(-4620, 0, 1950, 1500)
    Sleep(1500)

    ChrTalk(
        0x102,
        (
            "#010FI hope we're not disturbing you, sir,\x01",
            "but we've come on behalf of the Bracer\x01",
            "Guild about a job you requested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FYes, I heard from the guild that\x01",
            "the two of you would be coming.\x02\x03",
            "So, you're taking over your father's\x01",
            "work while he's away, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FWell, we're trying to at least...\x02\x03",
            "#505FI'm very sorry about my dad reneging\x01",
            "on his promise like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603FThere's no need for apologies. Knowing\x01",
            "your father, it's typical for him to be\x01",
            "swamped with work like this.\x02\x03",
            "#600FAnyway, with Lita and my wife out\x01",
            "and about, I'd like to move this\x01",
            "conversation somewhere else.\x02\x03",
            "Why don't we head upstairs to my\x01",
            "study and go over the details?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(2000)
    OP_6D(79750, 0, 190, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 78100, 200, -950, 90)
    SetChrPos(0x101, 80520, 0, -840, 270)
    SetChrPos(0x102, 80370, 0, 180, 225)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#600FIn truth, I don't think you'll find this\x01",
            "request particularly difficult.\x02\x03",
            "And it's for that reason, I think, that\x01",
            "asking the guild to do this job may\x01",
            "have been a bit presumptuous.\x02\x03",
            "Unfortunately, I'm unable to get away\x01",
            "from my work, and I had to break down\x01",
            "and ask the guild for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe were informed that this job involves the\x01",
            "transport of a certain something, but what is it\x01",
            "exactly that you would like us to carry and where?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FI would like you to pick up a Septium\x01",
            "Crystal from the Malga Mine and\x01",
            "deliver it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FWhen you say septium...\x02\x03",
            "Do you mean like, sepith that\x01",
            "we often come across?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAccurately speaking, sepith is fragmented\x01",
            "septium which is too small to be used as\x01",
            "precious stones.\x02\x03",
            "Therefore, this sepith is refined and\x01",
            "processed into quartz which can be\x01",
            "installed into orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FSo that's the difference, huh? I think\x01",
            "I've got a better grasp on things now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#603FWe've actually been able to obtain a certain\x01",
            "kind of septium called 'esmelas' from the\x01",
            "Malga Mine since the olden days.\x02\x03",
            "However, since a large piece of this crystal was\x01",
            "recently discovered, I've asked the mine chief\x01",
            "to hold onto it until someone could pick it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSo, you'd like us to pick up this\x01",
            "crystal from the mine chief and\x01",
            "bring it here, is that correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#600FPrecisely. What do you think?\x01",
            "Is this something you think you\x01",
            "can handle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FThe transport of a precious gem,\x01",
            "huh?\x02\x03",
            "#505FIt'll be a nice change from fighting\x01",
            "monsters. Should keep us on our\x01",
            "toes, too...\x02\x03",
            "#001FAll right, we'll do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#601FI appreciate your willingness to help.\x02\x03",
            "Please take this with you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Mayor's Referral\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x321, 1)

    ChrTalk(
        0x8,
        (
            "#600FIf you show that to one of the workers,\x01",
            "they should let you into the mine.\x02\x03",
            "#600FGood luck.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_22_6F9E end

    def Function_23_7B28(): pass

    label("Function_23_7B28")

    OP_8E(0x101, 0xFFFFE69C, 0x0, 0x4EC, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 0)
    Return()

    # Function_23_7B28 end

    def Function_24_7B44(): pass

    label("Function_24_7B44")

    Sleep(500)
    OP_8E(0x102, 0xFFFFEBF6, 0x0, 0x3E8, 0x7D0, 0x0)
    TurnDirection(0x102, 0x8, 0)
    Return()

    # Function_24_7B44 end

    def Function_25_7B65(): pass

    label("Function_25_7B65")

    OP_8E(0x8, 0xFFFFEDFE, 0x0, 0xB7C, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 0)
    Return()

    # Function_25_7B65 end

    SaveToFile()

Try(main)
