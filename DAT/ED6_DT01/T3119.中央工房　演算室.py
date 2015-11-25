from ED6ScenarioHelper import *

def main():
    # 中央工房　演算室

    CreateScenaFile(
        FileName            = 'T3119   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3119   ._SN',
            'ED6_DT01/T3119_1 ._SN',
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
        'Supervisor Travis',                    # 9
        'Black-Clad Man',                       # 10
        'Black-Clad Man',                       # 11
        'Black-Clad Man',                       # 12
        'Tita',                                 # 13
        'Wilmont',                              # 14
        'Professor Russell',                    # 15
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
        'ED6_DT07/CH01190 ._CH',             # 00
        'ED6_DT07/CH01330 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00101 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00111 ._CH',             # 05
        'ED6_DT07/CH00150 ._CH',             # 06
        'ED6_DT07/CH00151 ._CH',             # 07
        'ED6_DT07/CH00060 ._CH',             # 08
        'ED6_DT07/CH01450 ._CH',             # 09
        'ED6_DT06/CH20104 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01190P._CP',             # 00
        'ED6_DT07/CH01330P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00101P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00111P._CP',             # 05
        'ED6_DT07/CH00150P._CP',             # 06
        'ED6_DT07/CH00151P._CP',             # 07
        'ED6_DT07/CH00060P._CP',             # 08
        'ED6_DT07/CH01450P._CP',             # 09
        'ED6_DT06/CH20104P._CP',             # 0A
    )

    DeclNpc(
        X                   = 600,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 111,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 336,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -118000,
        Y                   = -1000,
        Z                   = 23400,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = -550,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 0,
        TriggerY            = 6300,
        TriggerRange        = 800,
        ActorX              = -540,
        ActorZ              = 900,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -117890,
        TriggerZ            = 0,
        TriggerY            = 24080,
        TriggerRange        = 800,
        ActorX              = -117890,
        ActorZ              = 1000,
        ActorY              = 24080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_489",          # 01, 1
        "Function_2_5A2",          # 02, 2
        "Function_3_5B8",          # 03, 3
        "Function_4_D4D",          # 04, 4
        "Function_5_1982",         # 05, 5
        "Function_6_1A3B",         # 06, 6
        "Function_7_1A51",         # 07, 7
        "Function_8_2510",         # 08, 8
        "Function_9_4490",         # 09, 9
        "Function_10_4D55",        # 0A, 10
        "Function_11_4DDD",        # 0B, 11
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_27E"),
        (104, "loc_291"),
        (100, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2AC"),
    )


    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    Event(0, 7)

    label("loc_28E")

    Jump("loc_2AC")

    label("loc_291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A1")
    Event(0, 9)

    label("loc_2A1")

    Jump("loc_2AC")

    label("loc_2A4")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_2AC")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2CC")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2E7")
    SetChrPos(0x8, -670, 0, 5580, 351)
    Jump("loc_488")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_318")
    SetChrPos(0x8, -670, 0, 5580, 351)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 6900, 268)
    Jump("loc_488")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_349")
    SetChrPos(0x8, -670, 0, 5580, 351)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 6900, 268)
    Jump("loc_488")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_37A")
    SetChrPos(0x8, -670, 0, 5580, 351)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 6900, 268)
    Jump("loc_488")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_389")
    SetChrFlags(0x8, 0x80)
    Jump("loc_488")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_393")
    Jump("loc_488")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_3E4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    SetChrPos(0x8, 470, 0, 6630, 225)
    Jump("loc_488")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_404")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_444")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)
    Jump("loc_488")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_488")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 700, 0, 9380, 353)
    SetChrFlags(0xC, 0x10)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4680, 1000, 10760, 79)

    label("loc_488")

    Return()

    # Function_0_26A end

    def Function_1_489(): pass

    label("Function_1_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CE")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CE")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4EE")
    OP_71(0x4, 0x4)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_50D")
    OP_72(0x7, 0x10)
    OP_6F(0x7, 30)

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_577")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_577")

    OP_72(0x8, 0x10)
    Jump("loc_583")

    label("loc_57F")

    OP_64(0x1, 0x1)

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_595")
    OP_10(0x7, 0x1)
    OP_10(0x1, 0x0)

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1")
    OP_64(0x0, 0x1)

    label("loc_5A1")

    Return()

    # Function_1_489 end

    def Function_2_5A2(): pass

    label("Function_2_5A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A2")

    label("loc_5B7")

    Return()

    # Function_2_5A2 end

    def Function_3_5B8(): pass

    label("Function_3_5B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_67E")

    ChrTalk(
        0xFE,
        (
            "After what you two did, we really\x01",
            "ought to celebrate the professor's\x01",
            "liberation from captivity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I'm sure the army's watching\x01",
            "our every move. No time to goof\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9")

    label("loc_67E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "Well, if it isn't our illustrious heroes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't see much from inside\x01",
            "the factory ship, but from the\x01",
            "little I did see...that was intense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was all over when\x01",
            "those soldiers surrounded the\x01",
            "container.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rehmann was standing next to\x01",
            "me, and I hugged him real tight,\x01",
            "without even thinking about it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C9")

    Jump("loc_D49")

    label("loc_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_91B")

    ChrTalk(
        0xFE,
        (
            "We've decided to adopt that new maintenance\x01",
            "technique I thought of after the orbal\x01",
            "shutdown. We're calling it, 'rebooting.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Of course, we need to get the\x01",
            "Capel back before we can really\x01",
            "ascertain its effectiveness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Bracer Guild is doing their\x01",
            "part, too... Things might be\x01",
            "looking up, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_A10")

    ChrTalk(
        0xFE,
        (
            "Even without the orbal calculator,\x01",
            "I've got work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now's probably my best chance\x01",
            "to get down to the storage room\x01",
            "and do some reorganizing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope once we get the Capel\x01",
            "back everything'll run a little\x01",
            "more smoothly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_AD8")

    ChrTalk(
        0xFE,
        (
            "I didn't think they'd actually get\x01",
            "away with the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But what are they going to\x01",
            "do with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even here in the Central Factory,\x01",
            "only Professor Russell really\x01",
            "understands it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_B53")

    ChrTalk(
        0xFE,
        (
            "Hey...how's the orbal calculator\x01",
            "holding up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My meters are saying that everything\x01",
            "is running smoothly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C0E")

    ChrTalk(
        0xFE,
        (
            "Since this morning, the readings\x01",
            "on the orbal calculator have\x01",
            "been rock-solid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why is that? Do you think it\x01",
            "might have something to do\x01",
            "with the orbal shutdown?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE")

    label("loc_C0E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "Since this morning, the readings\x01",
            "on the orbal calculator have\x01",
            "been rock-solid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I spent all that time tinkering\x01",
            "with it before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why is it working now?\x02",
    )

    CloseMessageWindow()

    label("loc_CBE")

    Jump("loc_D49")

    label("loc_CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(
        0xFE,
        "It just...really bugs me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I fix one thing and another thing\x01",
            "pops up because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm never going to finish!\x02",
    )

    CloseMessageWindow()

    label("loc_D49")

    TalkEnd(0xFE)
    Return()

    # Function_3_5B8 end

    def Function_4_D4D(): pass

    label("Function_4_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_ECC")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCA")

    ChrTalk(
        0xFE,
        (
            "Murdock has ordered the\x01",
            "Capel hidden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know when the army\x01",
            "will show up looking for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC9")

    label("loc_DCA")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "Hey there, all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You did a marvelous job\x01",
            "reacquiring the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And with the professor safe as\x01",
            "well, I can finally relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But still, Murdock has ordered the\x01",
            "Capel hidden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know when the army\x01",
            "will show up looking for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC9")

    Jump("loc_197E")

    label("loc_ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FD0")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Greetings, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard from Murdock. Well,\x01",
            "I haven't heard everything, but\x01",
            "it's time for the rescue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be waiting for the safe return of\x01",
            "both the professor and the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do your best. May Aidios watch\x01",
            "over you all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1012")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I sure hope the professor's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1110")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the time being, we should\x01",
            "get back to work on anything\x01",
            "we can do without the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It won't do for a full-grown man\x01",
            "like me to mope around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Bracer Guild is doing their\x01",
            "best. The only thing we can do\x01",
            "is wait and pray.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1192")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I can hardly believe it...the Capel\x01",
            "was stolen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if I can face\x01",
            "Professor Russell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_12A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1260")
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",                          # 0
            "Ask about the cigarettes\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    Call(1, 2)
    Return()

    label("loc_1217")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you find what you were\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A6")

    label("loc_1260")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you find what you were\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A6")

    Jump("loc_197E")

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_142A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1314")

    ChrTalk(
        0xFE,
        "Go ahead. Touch the panel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should figure out what to\x01",
            "do quickly enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1427")

    label("loc_1314")


    ChrTalk(
        0xFE,
        (
            "The maintenance chief is also in\x01",
            "charge of the airfield, so you'll\x01",
            "find him there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The gasoline is located in\x01",
            "the underground orbment\x01",
            "production facility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just ask the people there and\x01",
            "they'll bring it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come back if there's anything\x01",
            "else you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1427")

    Jump("loc_197E")

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1660")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_152F")

    ChrTalk(
        0xFE,
        (
            "Since I came in this morning\x01",
            "the orbal calculator seems to\x01",
            "be working more smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If things continue at this pace,\x01",
            "we can look forward to work\x01",
            "as usual in a few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't exactly know why, \x01",
            "but I'm feeling much better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165D")

    label("loc_152F")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "Good morning, all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was quite surprised today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I came in this morning\x01",
            "the orbal calculator seems to\x01",
            "be working more smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If things continue at this pace,\x01",
            "we can look forward to work\x01",
            "as usual in a few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't exactly know why, \x01",
            "but I'm feeling much better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165D")

    Jump("loc_197E")

    label("loc_1660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18AD")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16CF")

    ChrTalk(
        0xFE,
        (
            "I may as well check out the\x01",
            "storage area just one more\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* How tedious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18AA")

    label("loc_16CF")

    OP_A2(0x0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(
        0xFE,
        "Hello, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry to have called you in so\x01",
            "suddenly like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560FNo worries at all, sir.\x02\x03",
            "So...any progress?\x01",
            "How's the orbal calculator?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It'll take a little longer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not that I was expecting it to\x01",
            "be repaired overnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064FYes, sir. \x02\x03",
            "#561FI wish I could be more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine. Don't worry, I didn't have\x01",
            "any plans to use it yet anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll call you if I need you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060FYes, sir. Goodbye.\x02",
    )

    CloseMessageWindow()

    label("loc_18AA")

    Jump("loc_197E")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_197E")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Currently the orbal calculator\x01",
            "is in poor condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't seem to repair it\x01",
            "no matter what we try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to act up when we switch\x01",
            "modes. Do you have any ideas to\x01",
            "share with us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197E")

    TalkEnd(0xFE)
    Return()

    # Function_4_D4D end

    def Function_5_1982(): pass

    label("Function_5_1982")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A37")

    ChrTalk(
        0xFE,
        (
            "#560FHmm...let's see.\x02\x03",
            "A problem with mode changeover\x01",
            "means that something is probably\x01",
            "wrong with the memory.\x02\x03",
            "Have you run a full diagnostic\x01",
            "on the memory core yet?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A37")

    TalkEnd(0xFE)
    Return()

    # Function_5_1982 end

    def Function_6_1A3B(): pass

    label("Function_6_1A3B")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A2(0x545)
    OP_A3(0x546)
    Return()

    # Function_6_1A3B end

    def Function_7_1A51(): pass

    label("Function_7_1A51")

    EventBegin(0x0)
    OP_6D(1330, 0, 10350, 0)
    SetChrPos(0x101, -480, 0, 1250, 0)
    SetChrPos(0x102, -1790, 0, 1330, 0)
    FadeToBright(1000, 0)
    OP_6D(150, 0, 4860, 3000)

    ChrTalk(
        0x101,
        (
            "#509FWow...\x01",
            "Check out this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThis has to be the Operations room.\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#3PHey! You two.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3B6, 0x0, 0x1AFE, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFFCEA, 0x0, 0xFC8, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#5PI haven't seen you before, so\x01",
            "you mind telling me what\x01",
            "business you have in here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMy name's Travis, senior\x01",
            "engineer and supervisor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FNice to meet you. We're\x01",
            "with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FWe're here at the request of\x01",
            "Professor Russell, so if--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        "#5PProfessor Russell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PH-He's not in trouble again,\x01",
            "is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F'Again'...? You really don't\x01",
            "have much faith in him,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, I mean... I realize\x01",
            "that he's a genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe was the one who developed\x01",
            "the Capel unit, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut even being acquainted\x01",
            "with him results in no end\x01",
            "of trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTita, on the other hand, is an\x01",
            "incredibly sweet girl. Just an\x01",
            "all-around good kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FHa ha...\x01",
            "Yeah, I get what you mean.\x02\x03",
            "#006FBut I don't think we have\x01",
            "time to stand around talking,\x01",
            "in this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe need to find where the Central\x01",
            "Factory stores its equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, is that what this\x01",
            "is all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIn that case, go right ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI'll show you how it works.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)

    def lambda_1F9B():
        OP_6D(340, 0, 6200, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F9B)

    def lambda_1FB3():
        OP_8E(0xFE, 0x1D6, 0x0, 0x19E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FB3)
    Sleep(500)

    def lambda_1FD3():
        OP_8E(0xFE, 0xFFFFFFCE, 0x0, 0x137E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FD3)
    Sleep(200)

    def lambda_1FF3():
        OP_8E(0xFE, 0xFFFFFB00, 0x0, 0x1342, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FF3)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 45, 400)

    ChrTalk(
        0x8,
        (
            "This cylindrical device is\x01",
            "a type of computer. It's\x01",
            "called the Capel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These days, they mostly get\x01",
            "used to assist in airship\x01",
            "navigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...but this one is equipped for\x01",
            "the fastest general-purpose\x01",
            "data processing in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It can be used for anything, from\x01",
            "calculating material density to\x01",
            "information retrieval.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Now, for information retrieval...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 200)

    ChrTalk(
        0x8,
        (
            "You have to use this front\x01",
            "panel to select that mode.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That will send the signal through\x01",
            "the wiring and allow you to\x01",
            "access the memory orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a quartz inside that\x01",
            "trains a rapid light pulse on\x01",
            "it, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, it simply extracts\x01",
            "the data you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, I trust you know how\x01",
            "it works now?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[No sweat!]\x01",      # 0
            "[No clue.]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_234A"),
        (1, "loc_2427"),
        (SWITCH_DEFAULT, "loc_248C"),
    )


    label("loc_234A")


    ChrTalk(
        0x101,
        "#502FYep! No sweat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FI'm impressed, Estelle.\x02\x03",
            "You're way better with modern\x01",
            "technology than I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007FOkay, so I lied.\x02\x03",
            "#509FAll that stuff went completely\x01",
            "over my head.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_248C")

    label("loc_2427")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#509FWell, actually...\x02\x03",
            "I didn't really get a\x01",
            "single word of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_248C")

    label("loc_248C")


    ChrTalk(
        0x8,
        "Well, here's the setup.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You change the mode with\x01",
            "this panel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure you'll figure\x01",
            "it out in no time.\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x0, 0x1)
    OP_A2(0x514)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_7_1A51 end

    def Function_8_2510(): pass

    label("Function_8_2510")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-200, 0, 7100, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_26BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2677")
    OP_A2(0x533)
    OP_28(0x41, 0x1, 0x8)

    ChrTalk(
        0x107,
        "#065FWha...?! The Capel unit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057FWhat's a 'Capel'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt's the name of a type of operations\x01",
            "orbment developed by the professor.\x01",
            "An orbal calculator, if you will.\x02\x03",
            "It looks like the core's\x01",
            "been removed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FYou think our 'friends' stole it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015FIt's the most likely scenario.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26B9")

    label("loc_2677")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The core of the Capel has been removed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_26B9")

    EventEnd(0x1)
    Return()

    label("loc_26BC")

    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 34, 9)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C) Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W丂#20W\x01",
            "MEMORY_CHECK#100W........#20WOK!\x01",
            "#200W丂#20W\x01",
            "#1SDatabase accessed.\x01",
            "Please input search term.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F99")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        20,
        20,
        1,
        "[Central Factory]\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2804"),
        (SWITCH_DEFAULT, "loc_3F89"),
    )


    label("loc_2804")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        20,
        103,
        1,
        (
            "[Establishment]\x01",       # 0
            "[Universal Tech]\x01",      # 1
            "[Related Topics]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_286E"),
        (1, "loc_3144"),
        (2, "loc_3B55"),
        (SWITCH_DEFAULT, "loc_3F69"),
    )


    label("loc_286E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1154] (S: Septian Calendar) - Death of Prof.\x01",
            "C. Epstein in the sovereign state of Leman.\x01",
            "[S1155] Professor A. Russell returns to the Liberl\x01",
            "Kingdom. He proposes the spread of orbment\x01",
            "technology, to a chilly reception.\x01",
            "[S1157] Prof. Russell forms a partnership with\x01",
            "the Zeiss Clockmaker's Union. Together, they\x01",
            "establish the Zeiss Engineering Factory (later\x01",
            "renamed the Central Factory).\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1160] Edgar III, after an inspection of the\x01",
            "factory, donates a large amount of money to\x01",
            "further its research. Prof. Russell becomes the\x01",
            "first Factory Chief.\x01",
            "[S1162] Edgar III dies, and Alicia II assumes the\x01",
            "throne.\x01",
            "[S1164] Construction is completed on the\x01",
            "Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1168] The first orbal-powered airship, the\x01",
            "Calatrava, is completed. (39 failed test flights\x01",
            "before success was achieved.)\x01",
            "[S1173] Development of the Republic's Verne Corp.\x01",
            "and Empire's Reinford Company begin, and the site\x01",
            "is renamed to the 'Zeiss Central Factory.'\x01",
            "[S1175] The Liberl Orbalship Corporation is\x01",
            "established, and the transit commuter airship,\x01",
            "the Linde, is commissioned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1177] Transit commuter airship, the Cecilia,\x01",
            "is commissioned.\x01",
            "[S1178] Factory airship, the Leibnitz, is\x01",
            "completed.\x01",
            "[S1180] The Zeiss Central Factory is dismantled\x01",
            "and reconstructed at its current site. The\x01",
            "partially-underground factory in the Kaldia\x01",
            "Hills is completed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1182] Professor Russell resigns from his\x01",
            "position as Factory Chief and is succeeded by\x01",
            "Murdock.\x01",
            "[S1185] Natural Science and Medical Research\x01",
            "divisions are founded.\x01",
            "[S1187] The passenger ship, Eterna, sinks in\x01",
            "Calvard waters. Crown prince Judis dies.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1190] The Orbal Network, a joint venture with\x01",
            "the Epstein Foundation, is publicly announced.\x01",
            "[S1192] Outbreak of the Hundred Days War. The\x01",
            "Central Factory is taken by the Erebonian Army.\x01",
            "Prof. Russell develops the Air Defense Ship,\x01",
            "which is used to mount a highly-effective\x01",
            "counteroffensive, and soon becomes central to\x01",
            "the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1S[S1193] Liberl and Erebonia sign a peace accord.\x01",
            "Orbment exports to the Erebonian Empire resume.\x01",
            "[S1197] Version 1.0 of the Capel orbal computer\x01",
            "is completed.\x01",
            "[S1199] Development commences on the high-speed\x01",
            "cruiser, the Arseille.\x01",
            "[S1202] The Arseille is completed and flight\x01",
            "tests commence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F76")

    label("loc_3144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        20,
        219,
        1,
        (
            "[Orbments]\x01",               # 0
            "[Crystal Circuits]\x01",       # 1
            "[Septium]\x01",                # 2
            "[Airships]\x01",               # 3
            "[Orbal Weaponry]\x01",         # 4
            "[Tactical Orbments]\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31E0"),
        (1, "loc_3384"),
        (2, "loc_34A2"),
        (3, "loc_35F1"),
        (4, "loc_3788"),
        (5, "loc_3934"),
        (SWITCH_DEFAULT, "loc_3B35"),
    )


    label("loc_31E0")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Orbment\x01",
            "General term for a device that draws orbal energy\x01",
            "from septium. Invented 50 years ago by Prof. C.\x01",
            "Epstein. The clockwork mechanism inside causes a\x01",
            "reaction between septium and quartz, which in turn\x01",
            "releases energy for virtually any use. This energy\x01",
            "is gradually restored over time, and is cleaner\x01",
            "than energy produced by combustion engines, making\x01",
            "it extremely efficient for business purposes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3384")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Crystal Circuit (Quartz)\x01",
            "An electrical circuit, made from the purified,\x01",
            "processed crystalline structure of a septium\x01",
            "fragment (sepith). When used as an energy\x01",
            "source, this device causes varied phenomena,\x01",
            "but these are never seen unless it is placed\x01",
            "inside an orbment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_34A2")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Septium\x01",
            "A grouping of seven gemstones, found throughout\x01",
            "the continent. Prized as jewels for eons, it was\x01",
            "also regarded as a symbol of mystery. In modern\x01",
            "times, pieces (sepith) that are too small for\x01",
            "jewelry are refined and purified. Its value\x01",
            "increased dramatically upon the discovery of its\x01",
            "use as an energy source.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_35F1")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Orbal Airships\x01",
            "Commonly regarded as the crowning achievement \x01",
            "of orbment technology. Enables the power of\x01",
            "flight by combining a flying machine to provide\x01",
            "lift and an orbal engine for thrust. Because of\x01",
            "the need for high-efficiency orbal energy\x01",
            "transfer, modern airships are equipped with many\x01",
            "high-powered orbal computers. Airships less than\x01",
            "20 arge in length are known as 'flying boats.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3788")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Orbal Weaponry\x01",
            "Any firearm or cannon powered with orbment tech-\x01",
            "nology. Currently the most common form of military\x01",
            "weaponry among many nations. With orbal firearms,\x01",
            "energy is focused in a helical path along the\x01",
            "barrel, down to a tiny point, which then forces a\x01",
            "large metal projectile outward at high velocity.\x01",
            "These guns can fire more rounds than traditional\x01",
            "gunpowder arms, and at adjustable levels of force.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3934")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Tactical Orbments\x01",
            "Orbments used to manipulate orbal magics.\x01",
            "Usually no larger than a pocket watch, so its\x01",
            "internal workings are extremely minute and\x01",
            "elegantly constructed. When quartz designed\x01",
            "for Tactical Orbment use is installed, it\x01",
            "improves the abilities of its bearer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SWhen this quartz synchronizes with the bearer\x01",
            "(a.k.a. the 'Resonance Phenomenon'), the\x01",
            "internal mechanisms are used as part of a\x01",
            "complex process, which give him/her the ability\x01",
            "to perform what are known as 'Arts.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B42")

    label("loc_3B35")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B42")

    label("loc_3B42")

    Jump("loc_3144")

    label("loc_3B45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_3F76")

    label("loc_3B55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        20,
        249,
        1,
        (
            "[Combustion Engine]\x01",      # 0
            "[Gasoline]\x01",               # 1
            "[Haulage Vehicle]\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BBE"),
        (1, "loc_3CD4"),
        (2, "loc_3E20"),
        (SWITCH_DEFAULT, "loc_3F49"),
    )


    label("loc_3BBE")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Combustion Engine\x01",
            "A machine which generates usable energy by\x01",
            "burning fuel within. Less efficient than its\x01",
            "orbal counterpart, due to issues with gaseous\x01",
            "exhaust and noise pollution.\x01\x01",
            "[Combustion Engine] \x01",
            "Number Owned: 1\x01",
            "Owner: Maintenance Chief Gustav\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x200)
    OP_A2(0x1)
    Jump("loc_3F56")

    label("loc_3CD4")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Gasoline\x01",
            "A liquid derived from the purification of the\x01",
            "naturally-occurring hydrocarbon compound known as\x01",
            "petroleum. Used primarily as fuel for combustion\x01",
            "engines and as an industrial solvent.\x01\x01",
            "[Republic-Manufactured Gasoline]\x01",
            "Emergency Stores: 20 mid-sized tanks\x01",
            "Repository: Orbment Manufacturing Factory\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x400)
    OP_A2(0x2)
    Jump("loc_3F56")

    label("loc_3E20")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#1SEntry: Orbal Haulage Vehicle\x01",
            "Any wheeled vehicle powered by orbal energy.\x01",
            "Widely considered uncomfortable to ride and\x01",
            "very limited in speed. Primarily used for\x01",
            "transporting cargo.\x01\x01",
            "[Orbment-Powered Vehicle]\x01",
            "Owner: No Data\x01",
            "Repository: Underground Factory Entrance\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3F46")
    OP_28(0x29, 0x1, 0x8)

    label("loc_3F46")

    Jump("loc_3F56")

    label("loc_3F49")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F56")

    label("loc_3F56")

    Jump("loc_3B55")

    label("loc_3F59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_3F76")

    label("loc_3F69")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F76")

    label("loc_3F76")

    Jump("loc_2804")

    label("loc_3F79")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_3F96")

    label("loc_3F89")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F96")

    label("loc_3F96")

    Jump("loc_27B9")

    label("loc_3F99")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448D")
    OP_A2(0x516)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "#6PLooks like you've found what\x01",
            "you were looking for.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#004FWow... It's like a magic\x01",
            "box or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FOrbal computers are really something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PAs I understand it, Professor Russell's\x01",
            "teacher, Professor Epstein, was responsible\x01",
            "for the original concept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PBut it was Professor Russell's talent\x01",
            "that made an idea into reality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P*sigh* If only his presence\x01",
            "of mind were on par with\x01",
            "his intelligence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha... Well, Aidios isn't\x01",
            "one to bestow two blessings\x01",
            "on one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501FBy the way, where can we find\x01",
            "the guy who has one of those\x01",
            "combustion engine-thingies?\x02\x03",
            "The maintenance chief, right?\x01",
            "Where is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PHe's currently overseeing the\x01",
            "airfield, so you'd have to go\x01",
            "there to speak to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PAlso, the gasoline is likely\x01",
            "in orbment manufacturing, in\x01",
            "the basement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PTalk to the staff there. I'm\x01",
            "sure they'll be happy to get\x01",
            "it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FMaintenance Chief Gustav is down\x01",
            "at the airfield, working on a \x01",
            "combustion engine...\x02\x03",
            "And the gasoline is in\x01",
            "the basement orbment \x01",
            "manufacturing facility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FThanks!\x01",
            "You've been a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PThink nothing of it.\x01",
            "Let me know if you\x01",
            "need anything else.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 0)
    OP_4B(0x8, 255)

    label("loc_448D")

    EventEnd(0x1)
    Return()

    # Function_8_2510 end

    def Function_9_4490(): pass

    label("Function_9_4490")

    EventBegin(0x0)
    OP_6D(-101380, 0, -1870, 0)
    SetChrPos(0x101, -101860, 0, -2090, 270)
    SetChrPos(0x102, -101400, 0, -890, 270)
    SetChrPos(0x106, -101230, 0, -3040, 270)
    SetChrPos(0x107, -100640, 0, -1840, 270)
    SetChrPos(0x9, -117950, 0, -1340, 280)
    SetChrPos(0xA, -116160, 0, 710, 41)
    SetChrPos(0xB, -116560, 0, -600, 204)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0xE, -117490, 0, 22060, 328)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6D(-103580, 0, -540, 1000)

    ChrTalk(
        0x101,
        (
            "#004FHey, what's that door\x01",
            "doing open...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Man's Voice",
        (
            "#2P...Sorry about the wait. I've\x01",
            "secured the last objective.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Man's Voice",
        (
            "#2PAll right.\x01",
            "Let's get out of here, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Man's Voice",
        "#2PAre you all set?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x9, -118930, 0, 21810, 0)
    SetChrPos(0xA, -117340, 0, 21040, 328)
    SetChrPos(0xB, -117550, 0, 22790, 0)

    ChrTalk(
        0x102,
        "#016FThat voice...!\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x52)

    ChrTalk(
        0x106,
        (
            "#054FCome on!\x01",
            "It came from the elevator!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 6)
    OP_72(0x8, 0x10)
    OP_6F(0x8, 30)

    def lambda_4753():
        OP_6D(-117150, 0, -90, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4753)

    def lambda_476B():
        OP_8E(0xFE, 0xFFFE3EB4, 0x0, 0xFFFFFB50, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_476B)
    Sleep(400)

    def lambda_478B():
        OP_8E(0xFE, 0xFFFE3270, 0x0, 0xFFFFFBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_478B)
    Sleep(200)

    def lambda_47AB():
        OP_8E(0xFE, 0xFFFE38A6, 0x0, 0xFFFFFCCC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47AB)
    Sleep(100)

    def lambda_47CB():
        OP_8E(0xFE, 0xFFFE366C, 0x0, 0xFFFFF90C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_47CB)
    Sleep(800)

    def lambda_47EB():
        OP_6D(-117430, 0, 16500, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_47EB)

    def lambda_4803():
        OP_67(0, 3630, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4803)

    def lambda_481B():
        OP_6B(3490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_481B)

    def lambda_482B():
        OP_6C(21000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_482B)
    WaitChrThread(0x106, 0x1)

    def lambda_4840():
        OP_8E(0xFE, 0xFFFE35B8, 0x0, 0x35C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4840)
    WaitChrThread(0x106, 0x1)

    def lambda_4860():
        OP_8E(0xFE, 0xFFFE328E, 0x0, 0x24B8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4860)
    WaitChrThread(0x101, 0x1)

    def lambda_4880():
        OP_8E(0xFE, 0xFFFE2D52, 0x0, 0x22C4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4880)
    WaitChrThread(0x102, 0x1)

    def lambda_48A0():
        OP_8E(0xFE, 0xFFFE35B8, 0x0, 0x21CA, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48A0)
    WaitChrThread(0x107, 0x1)

    def lambda_48C0():
        OP_8E(0xFE, 0xFFFE3180, 0x0, 0x1EF0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_48C0)
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x101,
        "#005FAh-HA!\x02",
    )

    CloseMessageWindow()

    def lambda_48F1():
        OP_8C(0xFE, 303, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_48F1)

    def lambda_48FF():
        TurnDirection(0x9, 0x106, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_48FF)

    def lambda_490D():
        TurnDirection(0xA, 0x106, 800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_490D)
    TurnDirection(0xB, 0x106, 800)
    WaitChrThread(0x106, 0x1)

    ChrTalk(
        0x106,
        "#052FIt's THEM...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x107,
        "#065FGr-Grandpa?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wha...\x01",
            "A-Agate Crosner?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh crap...\x01",
            "Go go go!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)

    def lambda_49B1():
        OP_8E(0xFE, 0xFFFE3284, 0x0, 0x645A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_49B1)
    Sleep(500)

    def lambda_49D1():
        OP_8E(0xFE, 0xFFFE3450, 0x0, 0x6284, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_49D1)

    def lambda_49EC():
        OP_8F(0xFE, 0xFFFE32FC, 0x0, 0x576C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_49EC)
    Sleep(50)

    def lambda_4A0C():
        OP_8E(0xFE, 0xFFFE3450, 0x0, 0x666C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4A0C)

    def lambda_4A27():

        label("loc_4A27")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4A27")

    QueueWorkItem2(0xA, 1, lambda_4A27)

    def lambda_4A38():

        label("loc_4A38")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4A38")

    QueueWorkItem2(0xB, 1, lambda_4A38)

    def lambda_4A49():

        label("loc_4A49")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4A49")

    QueueWorkItem2(0x9, 1, lambda_4A49)

    ChrTalk(
        0x101,
        "#005FH-Hold it right there!\x02",
    )

    CloseMessageWindow()

    def lambda_4A7B():
        OP_8F(0xFE, 0xFFFE3220, 0x0, 0x6220, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4A7B)

    def lambda_4A96():
        OP_6D(-118050, 0, 23420, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A96)

    def lambda_4AAE():
        OP_8E(0xFE, 0xFFFE3284, 0x0, 0x5A1E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4AAE)

    ChrTalk(
        0x106,
        "#10A #054FGet back here!\x05\x02",
    )

    Sleep(200)

    def lambda_4AEC():
        OP_8E(0xFE, 0xFFFE3040, 0x0, 0x55AA, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AEC)
    Sleep(200)

    def lambda_4B0C():
        OP_8E(0xFE, 0xFFFE3450, 0x0, 0x546A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4B0C)
    Sleep(500)

    def lambda_4B2C():
        OP_8E(0xFE, 0xFFFE3270, 0x0, 0x4F10, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4B2C)
    Sleep(100)
    OP_70(0x8, 0x0)
    WaitChrThread(0x106, 0x1)
    Fade(500)
    SetChrChipByIndex(0x106, 6)
    OP_6D(-118180, 0, 22740, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#550FShit!\x01",
            "So close...!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#003FWe almost had them...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x107,
        (
            "#065FN-No...\x02\x03",
            "Why'd they take Grandpa...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FLet's take the emergency\x01",
            "stairs down.\x02\x03",
            "It looks like they're trying\x01",
            "to get out of the factory.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 65535)
    TurnDirection(0x106, 0x107, 800)

    ChrTalk(
        0x106,
        (
            "#057FYeah, if they get away, there's no\x01",
            "way to know if they'll take the tunnel\x01",
            "or just try to lose us in town.\x02\x03",
            "#054FMove your asses, kids!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005FYou don't have to tell\x01",
            "me twice!\x02",
        )
    )

    CloseMessageWindow()
    Fade(2000)
    OP_82(0x1, 0x2)
    OP_A2(0x532)
    OP_28(0x41, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_9_4490 end

    def Function_10_4D55(): pass

    label("Function_10_4D55")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pressing the button does nothing. The elevator cannot be used at the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_4D55 end

    def Function_11_4DDD(): pass

    label("Function_11_4DDD")

    SetPlaceName(0x9A) # 中央工房　演算室
    Return()

    # Function_11_4DDD end

    SaveToFile()

Try(main)
