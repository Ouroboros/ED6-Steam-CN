from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1121   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1121   ._SN',
            'ED6_DT01/T1121_1 ._SN',
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
        'Lugran',                               # 9
        'Sting',                                # 10
        'Anelace',                              # 11
        'Maybelle',                             # 12
        'Lila',                                 # 13
        'Receptionist Ted',                     # 14
        'Package',                              # 15
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
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH02360 ._CH',             # 03
        'ED6_DT07/CH02370 ._CH',             # 04
        'ED6_DT07/CH01290 ._CH',             # 05
        'ED6_DT07/CH00003 ._CH',             # 06
        'ED6_DT07/CH00013 ._CH',             # 07
        'ED6_DT07/CH00023 ._CH',             # 08
        'ED6_DT07/CH00033 ._CH',             # 09
        'ED6_DT06/CH20020 ._CH',             # 0A
        'ED6_DT06/CH20021 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH02360P._CP',             # 03
        'ED6_DT07/CH02370P._CP',             # 04
        'ED6_DT07/CH01290P._CP',             # 05
        'ED6_DT07/CH00003P._CP',             # 06
        'ED6_DT07/CH00013P._CP',             # 07
        'ED6_DT07/CH00023P._CP',             # 08
        'ED6_DT07/CH00033P._CP',             # 09
        'ED6_DT06/CH20020P._CP',             # 0A
        'ED6_DT06/CH20021P._CP',             # 0B
    )

    DeclNpc(
        X                   = 186,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x114,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 34900,
        Z                   = 0,
        Y                   = -2300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 25010,
        Z                   = 0,
        Y                   = 630,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -60835,
        Z                   = 0,
        Y                   = 38681,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 0,
        Y                   = -2500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46050,
        Z                   = 0,
        Y                   = 19400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 25390,
        Z                   = 750,
        Y                   = -3760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983051,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E7,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 130,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 600,
        ActorX              = 186,
        ActorZ              = 1500,
        ActorY              = 4400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4470,
        TriggerZ            = 0,
        TriggerY            = -2690,
        TriggerRange        = 1400,
        ActorX              = -4470,
        ActorZ              = 2000,
        ActorY              = -2690,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3520,
        TriggerZ            = 0,
        TriggerY            = -780,
        TriggerRange        = 1400,
        ActorX              = 3520,
        ActorZ              = 2000,
        ActorY              = -780,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_2CB",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_2E2",          # 03, 3
        "Function_4_306",          # 04, 4
        "Function_5_555",          # 05, 5
        "Function_6_1D22",         # 06, 6
        "Function_7_234C",         # 07, 7
        "Function_8_2F90",         # 08, 8
        "Function_9_4452",         # 09, 9
        "Function_10_5E95",        # 0A, 10
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_26F")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_29E")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_279")
    Jump("loc_29E")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_288")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_29E")

    label("loc_288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_292")
    Jump("loc_29E")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_29E")
    ClearChrFlags(0x9, 0x80)

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2AC")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_2AC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B8"),
        (SWITCH_DEFAULT, "loc_2CA"),
    )


    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7")
    OP_A2(0x308)
    Event(0, 8)

    label("loc_2C7")

    Jump("loc_2CA")

    label("loc_2CA")

    Return()

    # Function_0_256 end

    def Function_1_2CB(): pass

    label("Function_1_2CB")

    Return()

    # Function_1_2CB end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CC")

    label("loc_2E1")

    Return()

    # Function_2_2CC end

    def Function_3_2E2(): pass

    label("Function_3_2E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_305")
    OP_8D(0xFE, 24030, 2670, 26360, -1350, 1500)
    Jump("Function_3_2E2")

    label("loc_305")

    Return()

    # Function_3_2E2 end

    def Function_4_306(): pass

    label("Function_4_306")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x35, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_423")

    ChrTalk(
        0x8,
        (
            "#630FWe've received payment from Mayor\x01",
            "Maybelle for your investigative\x01",
            "efforts thus far.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_AF(0x1C, 0x35)
    Sleep(100)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)

    ChrTalk(
        0x8,
        (
            "#630FKeep up the good work, and be\x01",
            "careful out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536")

    label("loc_423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x1C)"), scpexpr(EXPR_END)), "loc_4AD")

    ChrTalk(
        0x8,
        (
            "#630FGood work. It looks like you managed\x01",
            "to achieve your objective.\x02\x03",
            "Come back again if you have\x01",
            "anything else to report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536")

    label("loc_4AD")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#630FHmm, it looks like there's nothing\x01",
            "to report at this point in time.\x02\x03",
            "Come back again if you have\x01",
            "anything else to report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_53F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_550")
    TalkEnd(0x8)
    Return()

    label("loc_550")

    Call(0, 5)
    Return()

    # Function_4_306 end

    def Function_5_555(): pass

    label("Function_5_555")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630FSo you're headed to Ruan,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FYeah, thanks for everything, Lugran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe really appreciate everything\x01",
            "you did for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FDon't mention it.\x02\x03",
            "I'm going to really miss having\x01",
            "you guys around.\x02\x03",
            "If you ever happen to be in Bose\x01",
            "again, don't forget to stop by.\x02\x03",
            "#631FYou're always welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FThanks. Anyway, we'd better get\x01",
            "going now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_6EA")


    ChrTalk(
        0x8,
        (
            "#630FThe pass to get to Ruan is a bit\x01",
            "of a chore.\x02\x03",
            "Make sure you're careful out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_746")

    Jump("loc_1D1E")

    label("loc_749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_864")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630FSo you're headed to the inn\x01",
            "on the lakeshore, are you?\x02\x03",
            "Well, then all you need to do is\x01",
            "follow the New Ansel Path by\x01",
            "heading south from town.\x02\x03",
            "That inn is right there on the\x01",
            "shore of Valleria Lake, so you\x01",
            "can't miss it.\x02\x03",
            "Be careful on your way there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FD")

    label("loc_864")


    ChrTalk(
        0x8,
        (
            "#630FSo you're headed to the inn\x01",
            "on the lakeshore, are you?\x02\x03",
            "Well, then all you need to do is\x01",
            "follow the New Ansel Path by\x01",
            "heading south from town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FD")

    Jump("loc_1D1E")

    label("loc_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B")
    OP_A2(0x36D)

    ChrTalk(
        0x8,
        (
            "#630FOh, are you three back already?\x02\x03",
            "You all gave me quite a surprise.\x02\x03",
            "It was unprecedented to hear that some\x01",
            "of our bracers had been taken into\x01",
            "custody during an investigation.\x02\x03",
            "That General Morgan, I tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022FWe're sorry to make you worry\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FOh, never mind that. I'm just glad\x01",
            "you're all back safe.\x02\x03",
            "I was even considering protesting\x01",
            "in the Royal City through our\x01",
            "main branch.\x02\x03",
            "But Mayor Maybelle managed to\x01",
            "smooth everything out before\x01",
            "that could happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FW-Was it really such a big deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FThink about it, Estelle...\x02\x03",
            "In the Liberl Kingdom the Bracer\x01",
            "Guild's right to investigate crimes\x01",
            "is recognized by law.\x02\x03",
            "Therefore, the general's actions would\x01",
            "be in direct defiance of the system of\x01",
            "rules that governs this kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FHmm, well, at least things have\x01",
            "settled down as a result of this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3D")

    label("loc_C6B")


    ChrTalk(
        0x8,
        (
            "#630FAt any rate, we should probably just\x01",
            "focus on investigating the recent\x01",
            "string of burglaries.\x02\x03",
            "I know you'll probably have to deal with\x01",
            "some soldiers from the army again,\x01",
            "but please act with prudence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3D")

    Jump("loc_1D1E")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_F81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630FSo you're headed to Ravennue Village,\x01",
            "are you?\x02\x03",
            "Then all you need to do is head along the\x01",
            "West Bose Highway and turn off onto the\x01",
            "trail about halfway down the road.\x02\x03",
            "The village can be easily reached by\x01",
            "just following the trail.\x02\x03",
            "#632FRavennue Village, huh... Always makes me think\x01",
            "of...well, another bracer. If he were here,\x01",
            "this would be no problem at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7E")

    label("loc_EC6")


    ChrTalk(
        0x8,
        (
            "#630FIf you're heading to Ravennue Village all\x01",
            "you need to do is get onto the trail along\x01",
            "the West Bose Highway.\x02\x03",
            "As long as you follow the trail you'll\x01",
            "get where you need to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7E")

    Jump("loc_1D1E")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(
        0x8,
        (
            "#630FThe Sky Bandits and the Capua\x01",
            "Family, huh?\x02\x03",
            "Who'd have ever thought they'd be\x01",
            "fearless enough to pull off a crime\x01",
            "like this?\x02\x03",
            "That said, I still wish we had\x01",
            "more clues.\x02\x03",
            "Anyway, why don't we have you\x01",
            "start gathering information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1110")

    label("loc_1085")


    ChrTalk(
        0x8,
        (
            "#630FThe Sky Bandits and the Capua\x01",
            "Family, huh?\x02\x03",
            "Who'd have ever thought they'd be\x01",
            "fearless enough to pull off a crime\x01",
            "like they did?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1110")

    Jump("loc_1D1E")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_END)), "loc_11F2")

    ChrTalk(
        0x8,
        (
            "#630FThe Sky Bandits and the Capua Family, huh?\x02\x03",
            "Who'd have ever thought they'd be\x01",
            "fearless enough to pull off a crime\x01",
            "like this?\x02\x03",
            "I think it would be best if you hurried\x01",
            "and reported this to Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1E")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19D4")
    EventBegin(0x0)
    OP_A2(0x314)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, 940, 0, 2160, 0)
    SetChrPos(0x102, 240, 0, 790, 0)
    SetChrPos(0x103, -540, 0, 1860, 0)
    OP_6D(640, 0, 2790, 1000)

    ChrTalk(
        0x8,
        (
            "#633FOh, it's you kids? So did you find out\x01",
            "anything about the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FTee hee... You bet! Valuable\x01",
            "information, at that!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle relayed the information they had obtained from General Morgan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#631FThe Sky Bandits and the Capua Family...\x01",
            "You're right, that IS valuable information!\x02\x03",
            "It looks like we'll be able to decide\x01",
            "on a policy for the Bracer Guild\x01",
            "related to this.\x02\x03",
            "#632FHowever, I'm surprised to hear that General\x01",
            "Morgan is an even bigger bracer-hater than I\x01",
            "had originally thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FYeah, I was really surprised myself.\x02\x03",
            "In Rolent, the job of a bracer is pretty much\x01",
            "respected by everyone, so to encounter\x01",
            "someone that hates bracers that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FDon't worry about it. General Morgan\x01",
            "is an exception.\x02\x03",
            "Under normal circumstances, the Royal\x01",
            "Army and the guild maintain a pretty good\x01",
            "cooperative relationship.\x02\x03",
            "#634FHowever, it looks like this time you're\x01",
            "going to have to deal with a lot more\x01",
            "than you bargained for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FWell, then I guess we'll have to\x01",
            "try and make steady efforts while\x01",
            "maintaining a low profile.\x02\x03",
            "But it looks like these recent\x01",
            "burglaries are also the work of\x01",
            "the Sky Bandits, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632FYes. Taking into account the incident in\x01",
            "Rolent, it's pretty clear who's behind these.\x02\x03",
            "To call them burglaries is one thing though,\x01",
            "because most of the stuff that's been\x01",
            "stolen hasn't been all that valuable.\x02\x03",
            "I would have never thought they would\x01",
            "go as far as to commit a heinous\x01",
            "crime like hijacking the Linde.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FNow that you mention it, that is\x01",
            "rather odd.\x02\x03",
            "The burglary that happened in Rolent\x01",
            "was also rather mild in comparison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FYeah, and to hijack an airliner and\x01",
            "then to turn around and demand a\x01",
            "ransom from the royal family...\x02\x03",
            "The risks there are greater than\x01",
            "any potential reward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026FHmm, in light of that, we should\x01",
            "probably do a little more on the\x01",
            "investigative side ourselves.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1D1E")

    label("loc_19D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#630FSo you're going to meet General\x01",
            "Morgan at the Haken Gate,\x01",
            "are you?\x02\x03",
            "To be honest, I am glad you are\x01",
            "taking on the mayor's request.\x02\x03",
            "Recently we've been dealing with\x01",
            "a lot of accidents or incidents\x01",
            "involving monsters.\x02\x03",
            "Although none of these incidents have\x01",
            "been very big, all of my bracers here at\x01",
            "the branch have been tied up with them.\x02\x03",
            "And frankly speaking, since I had no free hands\x01",
            "I was thinking about asking for assistance\x01",
            "from one of the other guild branches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C77")

    label("loc_1BC6")


    ChrTalk(
        0x8,
        (
            "#630FSo you're going to meet General\x01",
            "Morgan at the Haken Gate,\x01",
            "are you?\x02\x03",
            "Then you'll need to head on to the\x01",
            "East Bose Highway and then from\x01",
            "there head down the Eisen Road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C77")

    Jump("loc_1D1E")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1D1E")

    ChrTalk(
        0x8,
        (
            "#630FI'll leave the mayor's request up\x01",
            "to you then.\x02\x03",
            "The mayor's residence is near the\x01",
            "West gate of town. If you can't find\x01",
            "it, just try asking around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1E")

    TalkEnd(0x8)
    Return()

    # Function_5_555 end

    def Function_6_1D22(): pass

    label("Function_6_1D22")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_1D9E")

    ChrTalk(
        0xFE,
        "So you're leaving, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm looking forward to seeing you\x01",
            "guys again as future bracers...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF3")

    label("loc_1D9E")


    ChrTalk(
        0xFE,
        "Aren't you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...the junior bracers who were\x01",
            "working with Scherazard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF3")

    Jump("loc_2348")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216A")
    OP_A2(0x35F)
    OP_A2(0x1)

    ChrTalk(
        0x101,
        "#006F(Huh, who's this guy...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(Um, he looks like a bracer if\x01",
            "you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FHello? Is anybody there?\x02",
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
            "#020FAs unfriendly as ever, aren't you,\x01",
            "Sting?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "Weren't you...that bracer in training\x01",
            "from some time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYou got it.\x02\x03",
            "And thanks to you I can call\x01",
            "myself a senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm...I almost didn't recognize you.\x01",
            "Do you have some work here at the\x01",
            "Bose branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FAt the moment, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now we are dealing with a\x01",
            "number of incidents, so we're a\x01",
            "little shorthanded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Any help you could give us would\x01",
            "be useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    ChrTalk(
        0x101,
        (
            "#002F(So he was one of Schera's acquaintances,\x01",
            "huh? He does seem like a bit of a scary\x01",
            "guy if you ask me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F(That may be so, but with the way he\x01",
            "carries himself...he looks pretty\x01",
            "capable as a bracer.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2348")

    label("loc_216A")

    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B5")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, it's you guys, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While I'd love to give you a warm\x01",
            "welcome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both Grant and Anelace appear\x01",
            "to be out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F(Could he actually be a nice guy\x01",
            "after all...?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        (
            "#020F(Ha ha. Don't let appearances fool\x01",
            "you. He's the type to look out for\x01",
            "those around him.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_2348")

    label("loc_22B5")


    ChrTalk(
        0xFE,
        (
            "Right now we are dealing with a\x01",
            "number of incidents, so we're a\x01",
            "little shorthanded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Any help you could give us would\x01",
            "be useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    label("loc_2348")

    TalkEnd(0x9)
    Return()

    # Function_6_1D22 end

    def Function_7_234C(): pass

    label("Function_7_234C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_251B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C6")
    OP_A2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_2418")

    ChrTalk(
        0xFE,
        (
            "#814FAre you leaving so soon?\x02\x03",
            "#818FThat's too bad...I was hoping\x01",
            "we could work together.\x02\x03",
            "#810FWell, good luck with whatever lies\x01",
            "ahead-- and remember, never give up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C3")

    label("loc_2418")


    ChrTalk(
        0xFE,
        (
            "#814FHuh? Were you the ones working\x01",
            "alongside Schera?\x02\x03",
            "#810FWow, you two are really young...\x02\x03",
            "Well, good luck with whatever lies\x01",
            "ahead-- and remember, never give up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C3")

    Jump("loc_2518")

    label("loc_24C6")


    ChrTalk(
        0xFE,
        (
            "#810FWell, good luck with whatever lies\x01",
            "ahead-- and remember, never give up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2518")

    Jump("loc_2F8C")

    label("loc_251B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0A")
    TurnDirection(0xFE, 0x103, 0)
    OP_A2(0x360)
    OP_A2(0x2)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#850FIt's nice to see you, Scherazard. If I \x01",
            "remember right, the last time we saw\x01",
            "each other was during training, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FWell, if it isn't Anelace? It's certainly\x01",
            "been a while, hasn't it?\x02\x03",
            "So how has your swordsmanship been\x01",
            "coming along? Have you started\x01",
            "mastering the use of that weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#819FPlease don't even ask.\x01",
            "I'm still working on that.\x02\x03",
            "#817FI can't believe you guys were tossed\x01",
            "into prison without a shred of\x01",
            "conclusive evidence...\x02\x03",
            "#818FI wonder what that old bearded\x01",
            "general is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FWell, it turned out to be one of those\x01",
            "situations of being in the wrong place\x01",
            "at the wrong time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FHa ha. I'm just glad you're\x01",
            "all right.\x02\x03",
            "Now, this is a little off subject,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#810FI heard that your new recruits were\x01",
            "Cassius Bright's kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYes, that's right.\x01",
            "I'm Estelle Bright.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#010FAnd I'm Joshua. We're actually\x01",
            "not related by blood though.\x01",
            "I'm his adopted son.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#818FI see...so you're Cassius'...\x02\x03",
            "I don't think that you'll be super bracers\x01",
            "like he is just because you're his kids...\x02\x03",
            "#811FBut I'm excited to have the chance\x01",
            "to meet you in person like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F(So I guess she knows dad too,\x01",
            "huh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(Looks that way to me.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDB")
    OP_A2(0x2)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#810FSo, Scherazard, it looks like you ran\x01",
            "into a bit of trouble, huh?\x02\x03",
            "#817FI can't believe you guys were tossed\x01",
            "into prison without a shred of\x01",
            "conclusive evidence...\x02\x03",
            "#818FI wonder what that old bearded\x01",
            "general is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FWell, it turned out to be one of those\x01",
            "situations of being in the wrong place\x01",
            "at the wrong time.\x02\x03",
            "#020FThat aside, was it you who let the\x01",
            "mayor know about our situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FYep, right you are on that one.\x02\x03",
            "I just happened to run across her\x01",
            "while I was on a job at the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021FHa ha. I kind of feel bad for all the\x01",
            "trouble you had to go through for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FHa ha. It was no big deal, really.\x02\x03",
            "Now, this is a little off subject,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#810FI heard that you new recruits were\x01",
            "Cassius Bright's kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYes, that's right.\x01",
            "I'm Estelle Bright.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#010FAnd I'm Joshua. We're actually\x01",
            "not related by blood though.\x01",
            "I'm his adopted son.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#818FI see...so you're Cassius'...\x02\x03",
            "I don't think that you'll be super bracers\x01",
            "like he is just because you're his kids...\x02\x03",
            "#811FBut I'm excited to have the chance\x01",
            "to meet you in person like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F(So I guess she knows Dad too,\x01",
            "huh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F(Looks that way to me.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F8C")

    label("loc_2EDB")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "#810FI don't think that you'll be super bracers\x01",
            "like he is just because you're his kids...\x02\x03",
            "#811FBut I'm excited to have the chance\x01",
            "to meet you in person like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    TalkEnd(0xA)
    Return()

    # Function_7_234C end

    def Function_8_2F90(): pass

    label("Function_8_2F90")

    EventBegin(0x0)
    SetChrPos(0x101, -1120, 0, -4740, 0)
    SetChrPos(0x102, 22, 0, -4880, 0)
    SetChrPos(0x103, -57, 0, -3932, 0)

    def lambda_2FCB():
        OP_6D(0, 0, 2800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FCB)
    Sleep(2000)
    OP_4A(0x8, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#633FOh, Scherazard. You arrived a lot\x01",
            "sooner than I expected.\x02\x03",
            "I appreciate you coming all\x01",
            "the way from Rolent.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3079():
        OP_8E(0x103, 0xFFFFFE2A, 0x0, 0x776, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3079)
    Sleep(500)

    def lambda_3099():
        OP_8E(0x101, 0xFFFFFBA0, 0x0, 0x2C6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3099)
    Sleep(500)

    def lambda_30B9():
        OP_8E(0x102, 0x16, 0x0, 0x2C6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30B9)
    WaitChrThread(0x103, 0x1)

    ChrTalk(
        0x103,
        (
            "#020F#4PIt's been a while, hasn't it,\x01",
            "Lugran?\x02\x03",
            "Did someone tell you that we\x01",
            "were coming ahead of time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FYes, I received a call from Aina\x01",
            "not that long ago.\x02\x03",
            "So that means these two kids with\x01",
            "you are Cassius' children?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F#4PYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2PUm...it's nice to meet you, sir.\x01",
            "I'm Estelle Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAnd I'm Joshua Bright. It's a pleasure\x01",
            "to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631FI'm Lugran, and I oversee the\x01",
            "Bose branch.\x02\x03",
            "Your father and I go way back.\x02\x03",
            "Please just call me Lugran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#2PSure, we'll do that.\x02\x03",
            "#002FThat said...could you give us\x01",
            "a quick update on the missing\x01",
            "airliner incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632FYes, about that...\x02\x03",
            "The Royal Army is still continuing\x01",
            "its search.\x02\x03",
            "#634FHowever, with the army's current restriction\x01",
            "on information, no public updates of the\x01",
            "situation have been made.\x02\x03",
            "And not only has the general public\x01",
            "been kept in the dark, but the guild\x01",
            "hasn't heard a word either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2PReally?!\x02\x03",
            "Why not? Aren't the army and the guild\x01",
            "supposed to be cooperating together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F#4PWell, that's the way it is on the\x01",
            "surface, anyway.\x02\x03",
            "But in actuality, there's a lot of\x01",
            "opposition between both parties\x01",
            "on a number of aspects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FSo, pretty much what you're saying\x01",
            "is that it's a bunch of jurisdictional\x01",
            "disputes, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632FI hate to admit it...but that's\x01",
            "the situation.\x02\x03",
            "In addition, General Morgan has\x01",
            "gotten involved.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#023F#4PDid you just say General Morgan...?\x01",
            "Great. Now it really looks like\x01",
            "things are going to be a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2PGeneral Morgan? Who's that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FHe's famous for repelling the\x01",
            "Imperial Army's invasion 10\x01",
            "years ago.\x02\x03",
            "You should have read about\x01",
            "him in the history books.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F#2PHmm. Amazingly enough, I don't\x01",
            "recall the name.\x02\x03",
            "#002FSo what's the big deal with this\x01",
            "famous guy anyway?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#025F#4PFrom what I've heard, he's not the\x01",
            "biggest fan of the Bracer Guild.\x01",
            "Hates bracers, in fact.\x02\x03",
            "It seems he even makes it a point\x01",
            "to routinely assert that there's\x01",
            "no need for a Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#009F#2PSounds like a real whack-job\x01",
            "to me.\x02\x03",
            "So what you're saying is that we're\x01",
            "not getting any information because\x01",
            "of this general?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#634FThat's not really important at\x01",
            "the moment...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#632FWhat really matters is that bracers\x01",
            "are being prohibited from entering\x01",
            "the regions they are investigating.\x02\x03",
            "And because of that, it's causing\x01",
            "conflicts with our other work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2PB-But...we just came all the way\x01",
            "here from Rolent...\x02\x03",
            "If that's the way it's gonna be, then it's time\x01",
            "to duel it out with this general to decide who\x01",
            "gets to investigate the incident!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FYou're talking like a crazy\x01",
            "person, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FKeep your cool, bracer.\x01",
            "There ARE other ways.\x02\x03",
            "Such as...the request we just received\x01",
            "from the mayor concerning the incident.\x02\x03",
            "She has asked that we conduct an\x01",
            "investigation from the guild side,\x01",
            "separate from the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#4PWell, that's encouraging news.\x02\x03",
            "If it's an official request from the mayor,\x01",
            "it'll be a great pretext for us to conduct\x01",
            "our own investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2PI see. Well, isn't this perfect\x01",
            "timing.\x02\x03",
            "Lugran, we'll accept the mayor's\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#634FThat sounds fine by me.\x02\x03",
            "#630FBut before you go...you two are\x01",
            "junior bracers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#2PYeah, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FJunior bracers, so to speak, are\x01",
            "members-in-training registered\x01",
            "at various branches.\x02\x03",
            "In short, their performance is\x01",
            "monitored by the branch where\x01",
            "they're currently registered.\x02\x03",
            "And right now, for you two,\x01",
            "that would be Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2PSo what you're trying to say is\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe have to change our registration\x01",
            "if we want to accept jobs here,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#630FYou've got it.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x5A9, 0x0, 0x1072, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#630FHere, all you need to do is sign\x01",
            "on these forms to transfer your\x01",
            "registration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#2PUh, sure...\x02",
    )

    CloseMessageWindow()

    def lambda_3FE5():
        OP_8E(0xFE, 0x6AE, 0x0, 0x910, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FE5)
    Sleep(500)

    def lambda_4005():
        OP_6D(2210, 0, 3140, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4005)
    OP_8E(0x101, 0xFFFFFE34, 0x0, 0x37A, 0xBB8, 0x0)
    OP_8E(0x101, 0x366, 0x0, 0x8FC, 0xBB8, 0x0)

    def lambda_4045():
        TurnDirection(0x103, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4045)
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    Sleep(500)

    ChrTalk(
        0x102,
        "#010F#4POur names go here and...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua filled out the registration transfer forms.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#630FAll right, it looks like everything\x01",
            "is in order.\x02\x03",
            "Junior bracers, Estelle and Joshua.\x02\x03",
            "As of this day at 15:20, your\x01",
            "registration at the Bose branch\x01",
            "has been approved.\x02\x03",
            "#631FThis means that you are now\x01",
            "members of the Bose branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021FSo you know, once you become a senior\x01",
            "bracer you can do any job without being\x01",
            "registered to a particular branch.\x02\x03",
            "But on the flip-side, your duties and\x01",
            "responsibilities increase as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#010F#4PUnderstood...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2PSo pretty much we're still\x01",
            "newbies...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4300():
        OP_6D(490, 0, 3220, 1000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4300)
    OP_8E(0x8, 0xBA, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#630FWell, it looks like now I'll be\x01",
            "able to entrust you with the\x01",
            "mayor's request.\x02\x03",
            "The mayor's residence is near\x01",
            "the west gate. You should go\x01",
            "there and talk to her directly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x101,
        "#006FWe'll do that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_28(0x52, 0x3, 0x2)
    OP_28(0x52, 0x3, 0x4)
    OP_28(0x35, 0x4, 0x2)
    OP_28(0x35, 0x4, 0x4)
    OP_28(0x35, 0x1, 0x1)
    OP_28(0x35, 0x1, 0x2)
    OP_28(0x35, 0x1, 0x4)
    OP_4B(0x8, 0)
    EventEnd(0x0)
    Return()

    # Function_8_2F90 end

    def Function_9_4452(): pass

    label("Function_9_4452")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, -710, 0, -80, 45)
    SetChrPos(0xC, -1790, 0, -290, 45)
    SetChrPos(0x101, 500, 0, 2000, 225)
    SetChrPos(0x102, -910, 0, 2000, 180)
    SetChrPos(0x103, 1580, 0, 1390, 225)
    SetChrPos(0x104, 1700, 0, 190, 270)
    OP_6D(830, 0, 5070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_6D(830, 0, 2120, 2000)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#611F#5PI really appreciate all your\x01",
            "hard work.\x02\x03",
            "It appears that my impression\x01",
            "about you was right.\x02\x03",
            "I knew that you would come through\x01",
            "and bring closure to this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6PYeah, but the army took off with\x01",
            "all the glory.\x02\x03",
            "So I don't know if we could exactly\x01",
            "say that we solved the case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#610F#5PNo, that's not true.\x02\x03",
            "If you hadn't been there, I don't\x01",
            "know if the army's raid would\x01",
            "have been so successful.\x02\x03",
            "Backed into a corner as they were,\x01",
            "the Sky Bandits may very well have\x01",
            "harmed the hostages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631FAgreed. Everything worked out because\x01",
            "you infiltrated their hideout and took\x01",
            "them out ahead of time.\x02\x03",
            "You should be proud of what\x01",
            "you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#6PY-You really think so...?\x01",
            "Tee hee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FIt's true that the hostages were freed\x01",
            "and the Sky Bandits arrested...\x02\x03",
            "But it's a bit vexing to know that\x01",
            "there are still some unanswered\x01",
            "questions left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1PThe men who appeared at the Valleria\x01",
            "Lakeshore and the mystifying attitude\x01",
            "of the leader of the Sky Bandits...\x02\x03",
            "I think we should consider that\x01",
            "there's a lot behind this incident\x01",
            "that we don't know about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#632FWell, I guess we'll have to leave\x01",
            "that part up to the Royal Army\x01",
            "to figure out.\x02\x03",
            "With all the culprits being detained\x01",
            "by them, there's really not much\x01",
            "left we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#610F#5PAnyway, we should just be glad that\x01",
            "all the hostages came back safe.\x02\x03",
            "Thanks to the news about the arrest of\x01",
            "the Sky Bandits, things are returning\x01",
            "to normal here in town.\x02\x03",
            "As a token of my thanks, I've added\x01",
            "a bit of a bonus to your reward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#6PReally, are you okay with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#611F#5PHa ha. Of course I am.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0xB, 90, 200)

    ChrTalk(
        0xB,
        "#610F#5PI'd like to thank you too, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#4PHa...I just hope that my work\x01",
            "was worth the price of that\x01",
            "Grand Chardonnay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#611F#5PYes, in fact there was change\x01",
            "to spare.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0xB, 45, 200)

    ChrTalk(
        0xB,
        (
            "#611F#5PI hope you all have a wonderful day.\x01",
            "And if anything else comes up, I'd\x01",
            "greatly appreciate your help again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#621F#5PGood day...\x02",
    )

    CloseMessageWindow()

    def lambda_4CF4():

        label("loc_4CF4")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4CF4")

    QueueWorkItem2(0x101, 1, lambda_4CF4)

    def lambda_4D05():

        label("loc_4D05")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4D05")

    QueueWorkItem2(0x102, 1, lambda_4D05)

    def lambda_4D16():

        label("loc_4D16")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4D16")

    QueueWorkItem2(0x103, 1, lambda_4D16)

    def lambda_4D27():

        label("loc_4D27")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_4D27")

    QueueWorkItem2(0x104, 1, lambda_4D27)
    OP_8C(0xB, 180, 400)

    def lambda_4D3F():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDEE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4D3F)
    Sleep(300)
    OP_8C(0xC, 180, 400)

    def lambda_4D66():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDEE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4D66)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    OP_22(0x6, 0x0, 0x64)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    ChrTalk(
        0x101,
        (
            "#008F#6PWow...nice that someone appreciates\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    ChrTalk(
        0x102,
        (
            "#010F#3PI'm sure that if the incident had gone\x01",
            "on any longer, it would have caused\x01",
            "much more confusion.\x02\x03",
            "It's probably only natural that the\x01",
            "mayor is as happy as she is.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#001F#4PHeh heh... Now I'm starting to feel\x01",
            "all giddy inside.\x02\x03",
            "I don't think a bracer could be any more\x01",
            "happy than knowing her work helped out a\x01",
            "bunch of other people!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F53():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F53)
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#027FHmm-hmm-hmm... If you say so.\x02\x03",
            "But I think it's safe to say that you're\x01",
            "no longer greenhorns.\x02\x03",
            "Honestly, the two of you really\x01",
            "surprised me this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#008F#6PTee hee, you think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#630FAt any rate, please accept your\x01",
            "assessment and pay for clearing\x01",
            "up the incident.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_508F():
        OP_6D(770, 0, 3160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_508F)

    def lambda_50A7():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50A7)

    def lambda_50B5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50B5)

    def lambda_50C3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50C3)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x101, 0x3)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FA")
    OP_AF(0x1C, 0x35)
    Sleep(100)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)

    label("loc_50FA")

    OP_AF(0x1C, 0x37)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x38, 0x4, 0x10)
    OP_28(0x38, 0x4, 0x20)
    OP_28(0x39, 0x4, 0x10)
    OP_28(0x39, 0x4, 0x20)
    OP_28(0x39, 0x1, 0x400)

    ChrTalk(
        0x8,
        (
            "#630FHere's the pay the mayor was\x01",
            "talking about. It's a very,\x01",
            "very nice sum!\x02\x03",
            "#630FAnd this is from me...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "Recommendation\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x333, 1)

    ChrTalk(
        0x101,
        (
            "#004F#4PIsn't this...a recommendation from\x01",
            "the Bose Branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#2PIs it all right to give this to us\x01",
            "so soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631FOf course! It would be downright rude\x01",
            "of me not to recommend you after\x01",
            "resolving such a big incident.\x02\x03",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4PThank you, Lugran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2PWe'll work hard so that we don't\x01",
            "bring any embarrassment on this\x01",
            "recommendation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#021F#4PHa ha. Great work, you two.\x02\x03",
            "I'm sure your father would be\x01",
            "extremely pleased if he heard\x01",
            "the news.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        "#003F#6PSure...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        "#013F#1PYou're probably right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#634FI wonder what on earth Cassius\x01",
            "could be doing right now.\x02\x03",
            "Not contacting the guild is one thing,\x01",
            "but not contacting his family is a\x01",
            "completely different matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#522F#4PYeah...it's definitely not like him.\x02\x03",
            "After he suddenly disembarked from\x01",
            "the airliner in Bose, I wonder where\x01",
            "he could have gone.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xD, -800, 0, -8480, 0)

    NpcTalk(
        0xD,
        "Young Man's Voice",
        "#1PExcuse me, please!\x02",
    )

    CloseMessageWindow()

    def lambda_55A4():
        OP_6D(830, 0, 2120, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_55A4)

    def lambda_55BC():

        label("loc_55BC")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55BC")

    QueueWorkItem2(0x101, 1, lambda_55BC)

    def lambda_55CD():

        label("loc_55CD")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55CD")

    QueueWorkItem2(0x102, 1, lambda_55CD)

    def lambda_55DE():

        label("loc_55DE")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55DE")

    QueueWorkItem2(0x103, 1, lambda_55DE)

    def lambda_55EF():

        label("loc_55EF")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_55EF")

    QueueWorkItem2(0x104, 1, lambda_55EF)
    ClearChrFlags(0xD, 0x80)
    OP_8E(0xD, 0xFFFFFDF8, 0x0, 0xFFFFFBDC, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        (
            "#633FAren't you that receptionist from\x01",
            "the landing port...?\x02\x03",
            "What's the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You see, we recovered some of the\x01",
            "cargo stolen by the Sky Bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And among some of the pieces were\x01",
            "a number of parcels addressed to\x01",
            "the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So I'm here to deliver one of\x01",
            "them today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#631FI appreciate you doing that.\x02\x03",
            "#632FBut wait a minute...\x02\x03",
            "Why is there something addressed\x01",
            "to this branch when the airliner left\x01",
            "Bose to begin with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's actually addressed to the\x01",
            "Rolent branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But aren't Cassius Bright's family\x01",
            "members here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#6PWhat?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0x102,
        "#014FThat's us, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Oh, perfect!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We contacted the Rolent branch and\x01",
            "they said you had come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Here you are. This is the parcel.\x02",
    )

    CloseMessageWindow()
    OP_92(0xD, 0x101, 0x320, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle was given both the letter and parcel.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0xD, 0x50, 0x0, 0x1AE, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#501F#6PThis letter...yep, it's in Dad's\x01",
            "handwriting.\x02\x03",
            "It's addressed to Joshua and\x01",
            "I at the Rolent branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIt seems as if he just scribbled it\x01",
            "out before he got off the airliner.\x02\x03",
            "#019FI guess Dad did intend on getting\x01",
            "in contact with us after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021FWell, that's good to hear.\x02\x03",
            "#020FSo that parcel is from your dad,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#6PNo, this one looks like it was sent\x01",
            "to my dad by someone else.\x02\x03",
            "#004FHuh...? That's odd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FYeah...the sender hasn't written\x01",
            "their name anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Okay. My business here is done,\x01",
            "so I'll be on my way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    def lambda_5C0D():

        label("loc_5C0D")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C0D")

    QueueWorkItem2(0x101, 1, lambda_5C0D)

    def lambda_5C1E():

        label("loc_5C1E")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C1E")

    QueueWorkItem2(0x102, 1, lambda_5C1E)

    def lambda_5C2F():

        label("loc_5C2F")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C2F")

    QueueWorkItem2(0x103, 1, lambda_5C2F)

    def lambda_5C40():

        label("loc_5C40")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5C40")

    QueueWorkItem2(0x104, 1, lambda_5C40)
    OP_8E(0xD, 0xFFFFFE5C, 0x0, 0xFFFFFBDC, 0x7D0, 0x0)
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xD, 0, 400)

    ChrTalk(
        0xD,
        (
            "Oh, and one other thing. Good job in\x01",
            "helping arrest those Sky Bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You bracers sure do excellent work.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)
    OP_8E(0xD, 0xFFFFFCE0, 0x0, 0xFFFFDEE0, 0xBB8, 0x0)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xD, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    def lambda_5D2D():
        OP_6D(770, 0, 3160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D2D)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "#630FAnd to think that a clue about\x01",
            "your father would be mixed in\x01",
            "with the airliner's cargo.\x02\x03",
            "Feel free to use the lounge upstairs\x01",
            "to read his letter, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DF5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DF5)

    def lambda_5E03():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E03)

    def lambda_5E11():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E11)
    TurnDirection(0x101, 0x8, 400)
    Sleep(200)

    ChrTalk(
        0x101,
        "#501FThanks, Lugran!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FHa, well then, let's have a look\x01",
            "at the contents, shall we?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 10)
    Return()

    # Function_9_4452 end

    def Function_10_5E95(): pass

    label("Function_10_5E95")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 26780, 200, -3520, 270)
    SetChrPos(0x102, 26780, 200, -4800, 270)
    SetChrPos(0x103, 24180, 200, -3500, 90)
    SetChrPos(0x104, 24180, 200, -4700, 90)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x102, 7)
    SetChrChipByIndex(0x103, 8)
    SetChrChipByIndex(0x104, 9)
    SetChrSubChip(0x101, 1)
    OP_6D(26360, 200, -3250, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(1730, 0)
    OP_6C(45000, 0)
    OP_6E(459, 0)
    ClearChrFlags(0xE, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F#6PDo you mind telling me what\x01",
            "you're still doing here...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#5PIt's just plain and simple curiosity,\x01",
            "that's all.\x02\x03",
            "Why did your father disembark the airliner\x01",
            "prior to its departure?\x02\x03",
            "Were I forced to wait around for an answer,\x01",
            "the question would stick in my mind so I'd\x01",
            "never be able to sleep at night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#6PA-And you're telling me this\x01",
            "because...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#5POh, how heartless and cruel can you\x01",
            "be to a companion who has traveled\x01",
            "alongside you...?\x02\x03",
            "And just who is it you have to thank\x01",
            "for being able to infiltrate the Sky\x01",
            "Bandits' hideout, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6PAll right already...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027FYou can be a rather obnoxious\x01",
            "fellow, I hope you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI guess we don't have much of a\x01",
            "choice...\x02\x03",
            "#012FHowever, depending on the content,\x01",
            "we may have to ask you to leave,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#031F#5PHa, of course I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6PAll right, let's see what he has\x01",
            "to say...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle started by cutting the letter's seal.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1F(0x50, 0x12C)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Dear Estelle and Joshua,'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'I'm sure you're probably about\x01",
            "finished with the jobs I left for\x01",
            "you, right?'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'I'm also sure there are many things you'll have\x01",
            "trouble with in the beginning, but take each one\x01",
            "step at a time. I know you both can succeed.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Anyway, it turns out that I've had\x01",
            "a little trouble with my own work.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'And unfortunately, it looks like I\x01",
            "won't be able to make it home for\x01",
            "quite some time.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Please don't expect my return\x01",
            "until after the queen's birthday\x01",
            "celebration.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'I'm really sorry that things turned out like\x01",
            "they did, but you should be grown up enough\x01",
            "not to be lonely while I'm away.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'So until I get back, I'll leave it\x01",
            "up to the both of you to decide how\x01",
            "you want to live.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'You're free to continue working\x01",
            "in Rolent...'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'...or you're free to pursue qualifying\x01",
            "as a senior bracer.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Your 16th year is a vintage time in\x01",
            "your life, so make sure not to waste\x01",
            "it.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Please give my regards to\x01",
            "Scherazard and Aina.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'-Cassius Bright'\x07\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_1F(0x64, 0x12C)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#020FThat seems like the type of letter\x01",
            "your father would write.\x02\x03",
            "It touches lightly on things, but\x01",
            "it's full of consideration toward\x01",
            "the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#6PYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FIt looks that way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#5PHmm, the queen's birthday celebration,\x01",
            "is it?\x02\x03",
            "From what I've heard, that's still\x01",
            "a ways off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYep, it's about two or three months\x01",
            "away.\x02\x03",
            "Which means this would be the\x01",
            "perfect time to take a small\x01",
            "trip...\x02\x03",
            "I really wonder where your father\x01",
            "is and what he's up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#5PForget about that and let's focus\x01",
            "on what's in that package.\x02\x03",
            "With an unknown sender there's bound\x01",
            "to be something interesting inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#6PTo be honest, I'm pretty curious\x01",
            "myself...\x02\x03",
            "But we shouldn't be opening things\x01",
            "addressed to my dad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5PWhy don't you think of it this way...\x02\x03",
            "It was a package delivered by\x01",
            "an unknown sender about the\x01",
            "time your father disappeared.\x02\x03",
            "The two might be related, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#6PTh-That's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FOlivier...\x02\x03",
            "Don't coax Estelle into doing\x01",
            "something to satisfy your own\x01",
            "curiosity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FActually though, Olivier does have\x01",
            "a good point.\x02\x03",
            "Instead of leaving it until our\x01",
            "dad comes home...\x02\x03",
            "It might be worth looking into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#6P...\x02\x03",
            "#006FOkay, let's check it out!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle opened the parcel from the unknown sender.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    Fade(1000)
    SetChrPos(0xE, 25190, 750, -3960, 0)
    SetChrSubChip(0xE, 16)
    OP_0D()
    OP_AD(0x4001F, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Inside was a shiny, black hemispherical device.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also enclosed was a single memo with the item.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    OP_1D(0x21)
    Sleep(1000)
    OP_3E(0x35B, 1)

    ChrTalk(
        0x101,
        "#004F#4PWh-What's this supposed to be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIt's an orbment. Although I'm not\x01",
            "sure what it's used for.\x02\x03",
            "Let's see what the memo says...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'I was able to secure the item the\x01",
            "aforesaid group was carrying, so\x01",
            "please take care of it.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "'Please ask Professor R to do an\x01",
            "analysis of it when you find an\x01",
            "opportunity. -K.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#580F#4PTh-That's it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FYep...it looks like the sender\x01",
            "didn't write anything else.\x02\x03",
            "#012FSchera. Do you have any idea who\x01",
            "K or Professor R might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025FUm...I hate to say this, but I don't\x01",
            "have a clue for either.\x02\x03",
            "Your father's pretty well-known, so\x01",
            "there's a possibility these people\x01",
            "could be foreigners too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4PIf this is the only thing we've got\x01",
            "to go on, then honestly I'm about\x01",
            "ready to throw in the towel.\x02\x03",
            "#505FWhat the heck is this black\x01",
            "orbment anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022FFrom the shape alone, it doesn't\x01",
            "look like anything intended for\x01",
            "general use.\x02\x03",
            "Although it feels a little similar\x01",
            "to a battle orbment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#032F#5PEven so, it's still quite different.\x02\x03",
            "A normal battle orbment has slots\x01",
            "in which to install quartz...\x02\x03",
            "But this one has none.\x02\x03",
            "Maybe this one is...an artifact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PAn artifact?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5PPrecisely. An artifact is an orbment created\x01",
            "by an ancient civilization. Artifacts are the\x01",
            "models for all orbments produced today.\x02\x03",
            "They're still occasionally discovered in\x01",
            "ruins...and for the most part, the Septian\x01",
            "Church has custody over them.\x02\x03",
            "They're a type of antique, so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022FBut this one doesn't appear to\x01",
            "be that old.\x02\x03",
            "It looks to me like it was made\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#5PYou're right about that...\x02\x03",
            "However, this one almost seems\x01",
            "like a black-market item.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#582F#4P#3SJeez... Now look at what's happened\x01",
            "because of my good-for-nothing dad!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#582F#4P#3SDoesn't he know that we're all\x01",
            "worried about him?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FE-Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#4PNow he's getting some sketchy\x01",
            "item from an unknown sender...\x02\x03",
            "What in the world has my dad\x01",
            "gotten himself into this time?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#522FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()

    ChrTalk(
        0x102,
        (
            "#010FYou know, Estelle, I've been\x01",
            "thinking...\x02\x03",
            "How about we continue our journey?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        "#004F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023FJoshua?\x02",
    )

    CloseMessageWindow()
    OP_1D(0x58)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#010FThat's what Dad wrote in his\x01",
            "letter, right?\x02\x03",
            "He said, 'or you're free to pursue\x01",
            "qualifying as a senior bracer.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#6PYeah...he did say that, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe've already managed to get\x01",
            "recommendations from Rolent\x01",
            "and Bose, right?\x02\x03",
            "All that's left are Ruan, Zeiss,\x01",
            "and Grancel. Only those three.\x02\x03",
            "If we do jobs as we travel around\x01",
            "to these other regions...\x02\x03",
            "We just might hear something\x01",
            "about where Dad is or what\x01",
            "he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FI think we're just worrying ourselves\x01",
            "for nothing, considering Dad's skills...\x02\x03",
            "And there's also the possibility that\x01",
            "he may have even traveled abroad...\x02\x03",
            "#010FBut I think getting off our own duffs\x01",
            "is a lot better than just sitting around\x01",
            "and waiting.\x02\x03",
            "And we just might be able to find this\x01",
            "'Professor R', too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#6P...\x02\x03",
            "Um...Joshua...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWhat?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 26826, 0, -3385, 180)
    SetChrSubChip(0x101, 0)
    OP_96(0x101, 0x6856, 0x0, 0xFFFFEFCA, 0x2BC, 0xFA0)
    SetChrSubChip(0x101, 2)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#001F#6P#5SYOU'RE A GENIUS!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        (
            "#014FE-Estelle? What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6PThis is like killing two birds with\x01",
            "one stone or maybe even ten!\x02\x03",
            "Sometimes I hate you for being\x01",
            "so smart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FSo...should I consider that a 'yes'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#6POh, is it ever! Yes, yes, triple YES!\x02\x03",
            "#001FTraining to be senior bracers as\x01",
            "we travel around Liberl...\x02\x03",
            "And exposing what that no-good\x01",
            "middle-aged man has been doing\x01",
            "in the process!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018FUm...I think you're somehow\x01",
            "missing the point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021FHa ha ha... It looks like she's\x01",
            "back to her old self.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#031F#5PHa ha. I guess it's settled, then!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_5E95 end

    SaveToFile()

Try(main)
