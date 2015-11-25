from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1310   ._SN',
        MapName             = 'Bose',
        Location            = 'T1310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Warrant Officer Serose',               # 9
        'Private Usher',                        # 10
        'CWO Zelste',                           # 11
        'Anelace',                              # 12
        'Private Egel',                         # 13
        'Private Mikey',                        # 14
        'Private Cutinger',                     # 15
        'Dish',                                 # 16
        'Dish',                                 # 17
        'Coffee',                               # 18
        'Coffee',                               # 19
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01630 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT06/CH20008 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01630P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT06/CH20008P._CP',             # 07
    )

    DeclNpc(
        X                   = 19990,
        Z                   = 0,
        Y                   = 22490,
        Direction           = 90,
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
        X                   = 22000,
        Z                   = 0,
        Y                   = 9500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 79860,
        Z                   = 0,
        Y                   = 13400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 22100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 19990,
        Z                   = 0,
        Y                   = 7950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 76700,
        Z                   = 0,
        Y                   = 7590,
        Direction           = 270,
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
        X                   = 25000,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65541,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65541,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572869,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572869,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 21950,
        TriggerZ            = 0,
        TriggerY            = 22540,
        TriggerRange        = 400,
        ActorX              = 19990,
        ActorZ              = 1500,
        ActorY              = 22490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22050,
        TriggerZ            = 0,
        TriggerY            = 7990,
        TriggerRange        = 400,
        ActorX              = 19990,
        ActorZ              = 1500,
        ActorY              = 7950,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18440,
        TriggerZ            = 0,
        TriggerY            = 12120,
        TriggerRange        = 1000,
        ActorX              = 18440,
        ActorZ              = 1000,
        ActorY              = 12120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_416",          # 01, 1
        "Function_2_4CD",          # 02, 2
        "Function_3_4E3",          # 03, 3
        "Function_4_4E8",          # 04, 4
        "Function_5_185B",         # 05, 5
        "Function_6_2087",         # 06, 6
        "Function_7_2C81",         # 07, 7
        "Function_8_30C3",         # 08, 8
        "Function_9_30C8",         # 09, 9
        "Function_10_31C5",        # 0A, 10
        "Function_11_34A4",        # 0B, 11
        "Function_12_3D55",        # 0C, 12
        "Function_13_5E8E",        # 0D, 13
        "Function_14_6139",        # 0E, 14
        "Function_15_65F4",        # 0F, 15
        "Function_16_66E1",        # 10, 16
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    OP_82(0x80, 0x0)
    OP_A2(0x36B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2F7")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xA, 20390, 0, 10700, 180)
    SetChrPos(0xE, 79990, 0, 13380, 0)
    Jump("loc_3C8")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_321")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xA, 20390, 0, 10700, 180)
    Jump("loc_3C8")

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_34B")
    SetChrPos(0xA, 20390, 0, 10700, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3C8")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_364")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3C8")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_378")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3C8")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3C8")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Jump("loc_3C8")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Jump("loc_3C8")

    label("loc_3BE")

    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3D6")
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3F6")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B1("t1310_n")
    Event(0, 14)

    label("loc_3F6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_402"),
        (SWITCH_DEFAULT, "loc_415"),
    )


    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_412")
    Event(0, 12)

    label("loc_412")

    Jump("loc_415")

    label("loc_415")

    Return()

    # Function_0_2B6 end

    def Function_1_416(): pass

    label("Function_1_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42E")
    OP_B1("t1310_y")
    Jump("loc_437")

    label("loc_42E")

    OP_B1("t1310_n")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_44F")
    OP_1B(0x0, 0x0, 0xF)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 99)

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_45D")
    OP_64(0x1, 0x1)
    Jump("loc_483")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_483")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_475")
    OP_64(0x1, 0x1)
    Jump("loc_483")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_47F")
    Jump("loc_483")

    label("loc_47F")

    OP_64(0x1, 0x1)

    label("loc_483")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_416 end

    def Function_2_4CD(): pass

    label("Function_2_4CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4CD")

    label("loc_4E2")

    Return()

    # Function_2_4CD end

    def Function_3_4E3(): pass

    label("Function_3_4E3")

    Call(0, 4)
    Return()

    # Function_3_4E3 end

    def Function_4_4E8(): pass

    label("Function_4_4E8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53D")

    ChrTalk(
        0x8,
        (
            "Hmm, maybe I should try making a\x01",
            "dish using wild vegetables today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_5E6")

    ChrTalk(
        0x8,
        (
            "It looks like we had some fish\x01",
            "delivered from Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I'll cook something a bit lavish\x01",
            "this evening to help everyone\x01",
            "recharge their batteries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_690")

    ChrTalk(
        0x8,
        (
            "We haven't seen any of those\x01",
            "monsters after they attacked\x01",
            "us the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Any way I look at it, it just seems\x01",
            "like they weren't from around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_71A")

    ChrTalk(
        0x8,
        (
            "Oh, if it isn't the bracers from\x01",
            "the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What can we help you with today?\x01",
            "Do you have some business up here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_12FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B5")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0x8, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 6)), scpexpr(EXPR_END)), "loc_78B")

    ChrTalk(
        0x8,
        (
            "So you want to fill out some paperwork\x01",
            "to head over to Ruan, do you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCD")

    label("loc_78B")


    ChrTalk(
        0x101,
        "#001FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Good morning to yourselves as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks for helping us out the way\x01",
            "you did last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FTee hee. We didn't do much.\x02\x03",
            "How about you guys? Did you\x01",
            "run into any trouble patrolling\x01",
            "the area after that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nope. Everything was fine, like\x01",
            "on any normal night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I tell you what though,\x01",
            "that was rather strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FStrange? What was?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know how the lights along the roads\x01",
            "and at the checkpoints have the ability\x01",
            "to ward off monsters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, even if there were monsters that\x01",
            "approached the checkpoint, they wouldn't\x01",
            "be any more than two or three in number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So yesterday was the first time\x01",
            "I've ever seen them come in a\x01",
            "large pack like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FYeah, that is rather strange, now\x01",
            "that you mention it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then again, these monsters were\x01",
            "small change when compared with\x01",
            "the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We should probably just consider\x01",
            "it good training in protecting our\x01",
            "base of operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FI-Is that really the issue here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For us, that's all we're really\x01",
            "concerned about. Protecting\x01",
            "the checkpoint is paramount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll leave figuring out what the\x01",
            "monsters were thinking up to\x01",
            "you bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, getting back on topic...\x01",
            "You guys are heading over to\x01",
            "Ruan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you ready to fill out the\x01",
            "paperwork for your gate pass?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCD")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Fill out paperwork for gate pass]\x01",      # 0
            "[Not yet]\x01",                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_D4B"),
        (0, "loc_D8A"),
        (SWITCH_DEFAULT, "loc_11B2"),
    )


    label("loc_D4B")


    ChrTalk(
        0x8,
        (
            "Let me know when you're done\x01",
            "making preparations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x446)
    EventEnd(0x1)
    Jump("loc_11B2")

    label("loc_D8A")


    ChrTalk(
        0x102,
        "#010FYes, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua filled out the paperwork to enter the Ruan region.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "Well, that's that. It looks like\x01",
            "you're done here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Enjoy your travels in Ruan.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(300)

    def lambda_E7A():
        OP_6D(23120, 0, 24400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E7A)
    WaitChrThread(0x101, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The warrant officer operated the gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_70(0x2, 0x64)
    OP_8B(0x0, 0x5A50, 0x5F50, 0x190)
    OP_8B(0x1, 0x5A50, 0x5F50, 0x190)
    OP_73(0x2)

    def lambda_F07():
        TurnDirection(0x8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F07)
    OP_69(0x8, 0x5DC)

    ChrTalk(
        0x8,
        (
            "Welcome to the Ruan region!\x01",
            "Blue oceans and white magnolias\x01",
            "await you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That reminds me, you'll be\x01",
            "heading to Ruan City, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA5():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FA5)
    TurnDirection(0x1, 0x8, 400)

    ChrTalk(
        0x101,
        "#000FYep, that was the plan. Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, just make sure to report to\x01",
            "the guild concerning the incident\x01",
            "that happened up here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There will be a payment there\x01",
            "from the army for helping us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, but you're going to have\x01",
            "to divvy your spoils with Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All right, enjoy yourselves and\x01",
            "good luck in your endeavor to\x01",
            "become senior bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe really appreciate everything\x01",
            "you've done for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x407)
    OP_28(0x3A, 0x4, 0x10)
    OP_28(0x3A, 0x1, 0x4)
    OP_28(0x11, 0x4, 0x40)
    OP_28(0x13, 0x4, 0x40)
    OP_1B(0x0, 0x0, 0xF)
    NewScene("ED6_DT01/T1300   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_11B2")

    Jump("loc_12F7")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "Oh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Make sure you report to the guild\x01",
            "concerning the incident that\x01",
            "happened up here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Take care and enjoy your trip\x01",
            "to Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_126A")


    ChrTalk(
        0x8,
        (
            "Make sure you report to the guild\x01",
            "concerning the incident that\x01",
            "happened up here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Take care and enjoy your trip\x01",
            "to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F7")

    Jump("loc_1857")

    label("loc_12FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1368")

    ChrTalk(
        0x8,
        (
            "Huh? What are you kids doing\x01",
            "hiking at a time like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's pretty cold out there, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_1368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_156B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "No matter how experienced of a traveler\x01",
            "you are, you shouldn't be hiking around\x01",
            "in a place like this at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The trail is steep and there are\x01",
            "a lot of monsters out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That reminds me, as strange as it sounds,\x01",
            "we've seen a lot of organized packs of\x01",
            "monsters recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've never seen anything like it\x01",
            "until now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1568")

    label("loc_14CE")


    ChrTalk(
        0x8,
        (
            "That reminds me, as strange as it sounds,\x01",
            "we've seen a lot of organized packs of\x01",
            "monsters recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've never seen anything like it\x01",
            "until now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1568")

    Jump("loc_1857")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_160C")

    ChrTalk(
        0x8,
        (
            "All soldiers are allotted at least\x01",
            "six hours of sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's because they can't fight\x01",
            "to their full ability if they have\x01",
            "insufficient rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_160C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_17C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1724")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "Despite my appearance as a soldier\x01",
            "in the Royal Army, I love to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I often get the chief's permission\x01",
            "so I can cook here at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just so you know, the traveler's\x01",
            "quarters are over there so feel free\x01",
            "to use them whenever you need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BD")

    label("loc_1724")


    ChrTalk(
        0x8,
        (
            "Despite my appearance as a soldier\x01",
            "in the Royal Army, I love to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I often get the chief's permission\x01",
            "so I can cook here at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BD")

    Jump("loc_1857")

    label("loc_17C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1836")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "So are you heading to Ruan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before you do that you're going to\x01",
            "need to get permission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_1836")


    ChrTalk(
        0x8,
        "So are you heading to Ruan?\x02",
    )

    CloseMessageWindow()

    label("loc_1857")

    TalkEnd(0x8)
    Return()

    # Function_4_4E8 end

    def Function_5_185B(): pass

    label("Function_5_185B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(
        0xFE,
        (
            "Everybody up here in the fort is\x01",
            "talking about the mayor being\x01",
            "arrested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_18B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_19F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1970")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "It was my day to cook today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then the warrant officer came and told\x01",
            "me to let him cook in my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy really likes cooking,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F1")

    label("loc_1970")


    ChrTalk(
        0xFE,
        (
            "The warrant officer just came and told\x01",
            "me to let him cook in my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy really likes cooking,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F1")

    Jump("loc_2083")

    label("loc_19F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1AF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9D")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "The Bose region has been rather\x01",
            "quiet since the Sky Bandits were\x01",
            "apprehended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess it's better than\x01",
            "an endless string of events.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF0")

    label("loc_1A9D")


    ChrTalk(
        0xFE,
        (
            "The Bose region has been rather\x01",
            "quiet since the Sky Bandits were\x01",
            "apprehended.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF0")

    Jump("loc_2083")

    label("loc_1AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0xFE,
        (
            "Those monsters the other day were\x01",
            "a lot stronger than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which means I'll have to train a\x01",
            "lot harder than I have been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_1C24")

    ChrTalk(
        0xFE,
        (
            "The attack on the checkpoint\x01",
            "last night was good practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I should be better prepared\x01",
            "for an emergency-- both in body and\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1CBB")

    ChrTalk(
        0xFE,
        (
            "With the border garrison's investigation\x01",
            "carrying on this long, I'm sure they're\x01",
            "tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope they'll find some new leads\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1D8A")

    ChrTalk(
        0xFE,
        (
            "This area is covered with mountains\x01",
            "and filled with monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention there are big,\x01",
            "vicious ones roaming around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Daily training is an essential\x01",
            "part of being a soldier here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E83")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "This is due to the rugged terrain\x01",
            "which covers the Krone Range.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Sky Bandits may just be\x01",
            "hiding around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which is why the border garrison\x01",
            "has already investigated this area\x01",
            "on multiple occasions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F17")

    label("loc_1E83")


    ChrTalk(
        0xFE,
        (
            "On a normal day, we almost get\x01",
            "no travelers coming through the\x01",
            "steep pass here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Sky Bandits may just be\x01",
            "hiding around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_2083")

    label("loc_1F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF7")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "On a normal day, we get almost\x01",
            "no travelers coming through the\x01",
            "steep pass here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But now, with the airliners being stopped,\x01",
            "those in a hurry to get to Ruan or Bose\x01",
            "have been making the trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_1FF7")


    ChrTalk(
        0xFE,
        (
            "That said, I would tell anybody\x01",
            "to avoid trying to come through\x01",
            "this pass at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's way too dangerous for a\x01",
            "normal traveler.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2083")

    TalkEnd(0x9)
    Return()

    # Function_5_185B end

    def Function_6_2087(): pass

    label("Function_6_2087")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2120")

    ChrTalk(
        0xFE,
        (
            "It's really unfortunate to hear about\x01",
            "what the mayor was involved in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Politician or not, those types of\x01",
            "actions are unforgivable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2269")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "These checkpoints around Liberl were useful in\x01",
            "the war 10 years ago to separate the various\x01",
            "troops of the Imperial Army from each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And even today they're still used\x01",
            "as strategic points by the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is why we, as garrisons who\x01",
            "oversee these places, can never\x01",
            "let down our guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2351")

    label("loc_2269")


    ChrTalk(
        0xFE,
        (
            "These checkpoints around Liberl were useful in\x01",
            "the war 10 years ago to separate the various\x01",
            "troops of the Imperial Army from each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is why we, as garrisons who\x01",
            "oversee these places, can never\x01",
            "let down our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2351")

    Jump("loc_2C7D")

    label("loc_2354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245E")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "Soldiers have been stationed at\x01",
            "each checkpoint to protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But occasionally we have to rescue\x01",
            "hikers here in the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's because we have a lot of hikers\x01",
            "who find themselves in trouble here\x01",
            "along the Krone Range.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EC")

    label("loc_245E")


    ChrTalk(
        0xFE,
        (
            "Soldiers have been stationed at\x01",
            "each checkpoint to protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But occasionally we have to rescue\x01",
            "hikers here in the mountains.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EC")

    Jump("loc_2C7D")

    label("loc_24EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2575")

    ChrTalk(
        0xFE,
        (
            "How should we protect against\x01",
            "an enemy if we are attacked on\x01",
            "both sides...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's the topic of today's training.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_25D5")

    ChrTalk(
        0xFE,
        "Oh, so you're leaving, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a wild world out there, so\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_25D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_264A")

    ChrTalk(
        0xFE,
        (
            "Good morning. Were you able\x01",
            "to sleep well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks for lending us a hand\x01",
            "like you did last night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_264A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_28C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2864")
    EventBegin(0x0)
    OP_A2(0x404)
    OP_69(0xFE, 0x3E8)

    ChrTalk(
        0xFE,
        "Huh? And you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe apologize for intruding at\x01",
            "this hour.\x02\x03",
            "But we were actually wondering...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Joshua explained the situation and asked if they could stay the night.\x01",
            "Estelle tried to make her eyes as large and yearning as she could in the\x01",
            "hopes of scoring some free food, as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "I see. Well, that's no problem.\x01",
            "I can see from the emblem\x01",
            "that you're bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to use the room next\x01",
            "to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FWe really appreciate this,\x01",
            "sir.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_28BD")

    label("loc_2864")


    ChrTalk(
        0xFE,
        (
            "Feel free to use the room next\x01",
            "to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about warming yourselves\x01",
            "up first?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28BD")

    Jump("loc_2C7D")

    label("loc_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_297F")

    ChrTalk(
        0xFE,
        (
            "It appears that the border garrison\x01",
            "has requested reinforcements for\x01",
            "the headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the general is planning\x01",
            "to make his move sometime in the\x01",
            "near future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A35")

    ChrTalk(
        0xFE,
        (
            "Hmm, it appears that General Morgan\x01",
            "has narrowed his search area to the\x01",
            "northern mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So the Sky Bandits have been\x01",
            "lurking somewhere along the\x01",
            "border, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7D")

    label("loc_2A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B75")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "General Morgan has issued an\x01",
            "order to bolster security in the\x01",
            "surrounding area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's because we still don't know\x01",
            "where the Sky Bandits are hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mountainous areas are an\x01",
            "especially good place for them\x01",
            "to make a hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to tell my men to get\x01",
            "squared away as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C14")

    label("loc_2B75")


    ChrTalk(
        0xFE,
        (
            "General Morgan has issued an\x01",
            "order to bolster security in the\x01",
            "surrounding area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's because we still don't know\x01",
            "where the Sky Bandits are hiding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C14")

    Jump("loc_2C7D")

    label("loc_2C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2C7D")

    ChrTalk(
        0xFE,
        (
            "If you need a gate pass I can\x01",
            "issue one for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just let me know when you need\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7D")

    TalkEnd(0xA)
    Return()

    # Function_6_2087 end

    def Function_7_2C81(): pass

    label("Function_7_2C81")

    TalkBegin(0xB)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F99")
    OP_A2(0x360)
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#814FIsn't that you, Scherazard?\x02\x03",
            "#850FIt's nice to see you again. I haven't\x01",
            "seen you since the last time you\x01",
            "were here during your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FIf it isn't Anelace. What\x01",
            "are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FWell, we had a request to\x01",
            "exterminate a monster in\x01",
            "this area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FOh really...?\x02\x03",
            "So how has your swordsmanship been\x01",
            "coming along? Have you started\x01",
            "mastering the use of that weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#819FAh ha ha... Uh...let's avoid that subject\x01",
            "right now. I'm still working on it.\x02\x03",
            "#810FBy the way Scherazard, are you\x01",
            "here on a job for the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020FYeah, something like that. Although\x01",
            "the job is a little different from the\x01",
            "one you're handling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810FIs that so...\x02\x03",
            "Well, this region has become\x01",
            "more dangerous recently.\x02\x03",
            "Make sure to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30BF")

    label("loc_2F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_304E")
    OP_A2(0x3)

    ChrTalk(
        0x103,
        "#020FWell, if it isn't Anelace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#850FScherazard!\x02\x03",
            "#810FSo how is your investigation\x01",
            "coming along? Have you\x01",
            "made any progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020FIn a sense, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BF")

    label("loc_304E")


    ChrTalk(
        0xFE,
        (
            "#810FOne more thing, Scherazard.\x01",
            "The region has become really\x01",
            "dangerous recently.\x02\x03",
            "Make sure to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30BF")

    TalkEnd(0xB)
    Return()

    # Function_7_2C81 end

    def Function_8_30C3(): pass

    label("Function_8_30C3")

    Call(0, 9)
    Return()

    # Function_8_30C3 end

    def Function_9_30C8(): pass

    label("Function_9_30C8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3168")

    ChrTalk(
        0xC,
        (
            "Uh, you're heading to Ruan,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This side leads to Bose. If you're\x01",
            "heading to Ruan, then you need\x01",
            "to leave through the opposite door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C1")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_31C1")

    ChrTalk(
        0xC,
        (
            "Since this place is at such a high\x01",
            "altitude, it gets really cold after dark.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C1")

    TalkEnd(0xC)
    Return()

    # Function_9_30C8 end

    def Function_10_31C5(): pass

    label("Function_10_31C5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3241")

    ChrTalk(
        0xFE,
        (
            "Is it true that the mayor of Ruan\x01",
            "was arrested?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who knew that something like\x01",
            "that could ever happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_32DC")

    ChrTalk(
        0xFE,
        (
            "The wound I got from that\x01",
            "monster has finally healed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'm going to need to\x01",
            "train harder to make sure\x01",
            "that never happens again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_32DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_336E")

    ChrTalk(
        0xFE,
        "The warrant officer loves to cook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even when it's not his turn to cook,\x01",
            "there are times he still makes\x01",
            "things in the kitchen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_336E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_340E")

    ChrTalk(
        0xFE,
        "We're almost out of firewood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After I finish my training today and\x01",
            "report back to the chief, I think I'll\x01",
            "go out and gather some more wood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_340E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_3446")

    ChrTalk(
        0xFE,
        "Owowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That monster got me good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_3446")


    ChrTalk(
        0xFE,
        (
            "It's almost time for me to go\x01",
            "on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better hurry up and eat while\x01",
            "I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A0")

    TalkEnd(0xD)
    Return()

    # Function_10_31C5 end

    def Function_11_34A4(): pass

    label("Function_11_34A4")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_350B")

    ChrTalk(
        0xFE,
        (
            "I tell you what, despite the season,\x01",
            "it still gets freezing cold in these\x01",
            "mountains.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_350B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_356B")

    ChrTalk(
        0xFE,
        (
            "I've still got time until I go\x01",
            "on duty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should catch a\x01",
            "few winks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_356B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_36F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3690")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Since this is the middle of the\x01",
            "mountains, it's really inconvenient\x01",
            "to get food brought up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We usually get our stuff delivered\x01",
            "from Bose or Ruan along the trail\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And along with the deliverer's\x01",
            "own escort we have to go and\x01",
            "meet them along the way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3690")


    ChrTalk(
        0xFE,
        (
            "It gets really bad when it's the\x01",
            "middle of the winter and we've\x01",
            "got snow piled up to here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F0")

    Jump("loc_3D51")

    label("loc_36F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3787")

    ChrTalk(
        0xFE,
        "It's almost time for training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In light of the monsters attacking\x01",
            "the checkpoint, I need to get\x01",
            "myself ready for anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_3787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_38DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3855")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "Hi again. Thanks for your help\x01",
            "the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You may be young, but I shouldn't\x01",
            "expect anything less from a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was excellent work you\x01",
            "made of those monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_3855")


    ChrTalk(
        0xFE,
        (
            "You may be young, but I shouldn't\x01",
            "expect anything less from a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was excellent work you\x01",
            "made of those monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D9")

    Jump("loc_3D51")

    label("loc_38DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_39A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_395D")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "What's wrong? You're welcome to\x01",
            "go in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you feel like taking a rest, please\x01",
            "let the chief know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399D")

    label("loc_395D")


    ChrTalk(
        0xFE,
        (
            "If you feel like taking a rest, please\x01",
            "let the chief know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399D")

    Jump("loc_3D51")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC7")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "It seems like nobody's been able\x01",
            "to figure out exactly where the\x01",
            "Sky Bandits really are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The border garrison often comes\x01",
            "here to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's because the Bose region\x01",
            "is covered with mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This area is the perfect place for\x01",
            "criminals to hide.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B41")

    label("loc_3AC7")


    ChrTalk(
        0xFE,
        (
            "That's because the Bose region\x01",
            "is covered with mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This area is the perfect place for\x01",
            "criminals to hide.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B41")

    Jump("loc_3D51")

    label("loc_3B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3BF6")

    ChrTalk(
        0xFE,
        (
            "It seems as though the missing\x01",
            "airliner was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, since the criminals weren't\x01",
            "apprehended, these security checks\x01",
            "are going to continue for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_3BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3CD3")

    ChrTalk(
        0xFE,
        (
            "Sky Bandits, huh? Sounds like a\x01",
            "troublesome group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, this time General Morgan\x01",
            "is spearheading the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only a matter of time until\x01",
            "he's got this bunch locked up\x01",
            "behind bars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D51")

    label("loc_3CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3D51")

    ChrTalk(
        0xFE,
        (
            "We are on high alert at the\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're heading anywhere,\x01",
            "then you'll need to fill out\x01",
            "some paperwork.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D51")

    TalkEnd(0xE)
    Return()

    # Function_11_34A4 end

    def Function_12_3D55(): pass

    label("Function_12_3D55")

    EventBegin(0x0)
    AddParty(0x5, 0xFF)
    EventBegin(0x0)
    OP_6D(80631, 0, 54990, 0)
    SetChrPos(0x101, 75900, 0, 53900, 90)
    SetChrPos(0x102, 74500, 0, 53000, 90)
    SetChrPos(0x106, 73600, 0, 52570, 90)
    SetChrPos(0x8, 73600, 0, 52570, 90)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    FadeToBright(1000, 0)

    def lambda_3DD9():
        OP_8E(0xFE, 0x138E4, 0x0, 0xD28C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD9)

    def lambda_3DF4():
        OP_8E(0xFE, 0x13560, 0x0, 0xCF08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DF4)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000FSo this is the room for travelers,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010FYeah. Let's get that fireplace\x01",
            "on, shall we?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E82():
        OP_6D(82761, 0, 52570, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E82)
    OP_8E(0x102, 0x13BA0, 0x0, 0xCF08, 0x7D0, 0x0)

    def lambda_3EAE():
        OP_8E(0xFE, 0x144BF, 0x0, 0xCA1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EAE)
    Sleep(500)

    def lambda_3ECE():
        OP_8E(0xFE, 0x14344, 0x0, 0xCD5E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ECE)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 90, 400)
    Sleep(1000)
    OP_22(0x86, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8E(0x102, 0x14344, 0x0, 0xC83C, 0x7D0, 0x0)
    OP_8C(0x102, 52, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F#3PAh...\x01",
            "It's so nice and warm...\x02\x03",
            "Mmmm...but y'know, wood stoves\x01",
            "just feel so much more cozy than\x01",
            "these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah, I agree.\x02\x03",
            "Orbment stoves may heat up quickly, and they're\x01",
            "certainly efficient, but they can't compare with\x01",
            "the feel of a real wood-burning stove.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3PTrue, but these ones are much\x01",
            "easier to use.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2PHey, I'm sorry to bother you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_412F():
        OP_6D(81370, 0, 53270, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_412F)

    def lambda_4147():

        label("loc_4147")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4147")

    QueueWorkItem2(0x102, 1, lambda_4147)
    Sleep(100)

    def lambda_415D():

        label("loc_415D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_415D")

    QueueWorkItem2(0x101, 1, lambda_415D)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    OP_8E(0x8, 0x130B0, 0x0, 0xD048, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "I heard from the chief that\x01",
            "you'll be staying the night.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need anything for dinner,\x01",
            "we'll be happy to share what we\x01",
            "have with you, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FThat would be wonderful, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No worries. After the airliners went into\x01",
            "service, the number of travelers coming\x01",
            "through here drastically decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, with all the free time we've\x01",
            "got, we welcome any guests coming\x01",
            "through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#4PTee hee. Well, in that case, we'll\x01",
            "really make sure to eat up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All right then, give us a little time\x01",
            "to get supper in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, uh, full disclosure here: I think\x01",
            "it's Usher's night to cook, so I hope\x01",
            "your stomachs aren't delicate.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_8E(0x8, 0x1234A, 0x0, 0xCEAE, 0xBB8, 0x0)

    def lambda_4467():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4467)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F#4PThere sure was a lot of rivalry going\x01",
            "on over the Sky Bandit incident...\x02\x03",
            "But there are quite a few nice\x01",
            "soldiers once you start to talk\x01",
            "to them on a personal level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FYeah, that's true.\x02\x03",
            "#015FAlthough, I think Liberl is probably\x01",
            "about the only place you're going\x01",
            "to find nice soldiers.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45D3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45D3)

    ChrTalk(
        0x101,
        "#501F#3PHuh? What do you mean by that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FDon't take me too seriously, I was just\x01",
            "thinking out loud... In the meantime,\x01",
            "let's put our bags down somewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_A2(0x3FC)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1311   ._SN", 2, 0, 0)
    IdleLoop()
    OP_6D(80990, 200, 53320, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x101, 81090, 200, 51050, 270)
    SetChrPos(0x102, 78250, 200, 51000, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrPos(0xF, 79980, 750, 50430, 0)
    SetChrPos(0x10, 79200, 750, 51110, 0)
    SetChrPos(0x11, 80060, 700, 51150, 0)
    SetChrPos(0x12, 79240, 700, 50480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Sleep(1000)
    OP_1D(0x54)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F#2POh man, I'm so stuffed.\x02\x03",
            "Although they said not to expect\x01",
            "much, the food was pretty good,\x01",
            "didn't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FY-Yeah. It was, uh, certainly like\x01",
            "nothing I've ever had before.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x10, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 72320, 0, 52990, 90)

    ChrTalk(
        0x8,
        "#2PExcuse me for disturbing you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    SetChrFlags(0x8, 0x4)

    def lambda_48C9():
        OP_6D(79690, 0, 53470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48C9)
    SetChrSubChip(0x102, 1)
    OP_8C(0x8, 90, 0)
    ClearChrFlags(0x8, 0x80)

    def lambda_48F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_48F2)
    OP_8E(0x8, 0x1372C, 0x0, 0xCE86, 0xBB8, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x101,
        (
            "#001F#4POh, sir! The meal was delicious!\x01",
            "Thanks so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4P...Yes, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PR-Really? You must have taste buds\x01",
            "of iron, too...I mean, I'm glad to hear\x01",
            "that you enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAnyway...we've had another guest arrive,\x01",
            "so if it's not too much trouble, could\x01",
            "you two share the same room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#4PAnother guest...in the middle of\x01",
            "the night like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#4PThey must have some serious guts\x01",
            "to be hiking around in the mountains\x01",
            "at this hour.\x02\x03",
            "But no, we don't mind. It's not like\x01",
            "we're paying to stay here either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PI really appreciate that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHe's actually in the same line of\x01",
            "work as the both of you, so I'm sure\x01",
            "you'll get along fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4PThe same line of work?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x106, 72320, 0, 52990, 90)

    NpcTalk(
        0x106,
        "Man's Voice",
        (
            "#2PHmph...I knew I'd seen you two\x01",
            "somewhere before.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x106, 7)
    ClearChrFlags(0x106, 0x80)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4C6F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_4C6F)

    def lambda_4C81():
        OP_8E(0xFE, 0x13330, 0x0, 0xD160, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4C81)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 400)

    ChrTalk(
        0x101,
        "#004F#4PY-You're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4PThe 'Heavy Blade' Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3POh, so you know each other\x01",
            "already, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(
        0x8,
        (
            "#4PBy the way, Agate, what do you\x01",
            "plan to do about dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050FI appreciate the invitation, but\x01",
            "I had something before coming\x01",
            "up here.\x02\x03",
            "All I need is somewhere to crash\x01",
            "for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#3PGo ahead and divide up the beds\x01",
            "amongst yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PAll right, good night.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_44(0x106, 0xFF)
    OP_8E(0x8, 0x13240, 0x0, 0xCC06, 0xBB8, 0x0)

    def lambda_4EB1():

        label("loc_4EB1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4EB1")

    QueueWorkItem2(0x106, 3, lambda_4EB1)
    OP_8E(0x8, 0x1234A, 0x0, 0xCEAE, 0xBB8, 0x0)

    def lambda_4ED6():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4ED6)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_4F0B():
        OP_6D(80990, 200, 53320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F0B)
    OP_44(0x106, 0xFF)
    OP_8C(0x106, 135, 400)
    OP_8E(0x106, 0x1372C, 0x0, 0xCE86, 0x7D0, 0x0)
    OP_8C(0x106, 180, 400)

    ChrTalk(
        0x106,
        (
            "#050F#3PNow if I remember right...weren't\x01",
            "you Cassius' kids?\x02\x03",
            "What are you doing sleeping in\x01",
            "a place like this?\x02\x03",
            "And what happened to Scherazard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2PSchera returned to Rolent.\x02\x03",
            "Now it's just the two of us\x01",
            "traveling together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2PWe're thinking of making our way\x01",
            "around the kingdom in order to\x01",
            "become senior bracers.\x02\x03",
            "We're going to see the places we\x01",
            "want to protect and train so that\x01",
            "we can do just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F#3PSenior bracers? Traveling the entire\x01",
            "kingdom on foot?\x02\x03",
            "You two are really a bunch of\x01",
            "carefree brats, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#2PWhat did you just call us?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#3PThere's no way the two of you are\x01",
            "going to simply become senior\x01",
            "bracers.\x02\x03",
            "Use your brains and think about\x01",
            "it for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2PSay what you want, but we helped\x01",
            "in the arrest of the Sky Bandits!\x02\x03",
            "And we've even got some recommendations,\x01",
            "so quit treating us like we're a bunch\x01",
            "of kids!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F#3POh, that? I heard all about it from\x01",
            "old man Lugran.\x02\x03",
            "#050FLet me ask you this... Suppose you had\x01",
            "been the only ones there. Do you still\x01",
            "think you would have succeeded?\x02\x03",
            "Just you two alone, without\x01",
            "Scherazard's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2PIt would've been a lot tougher,\x01",
            "definitely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#3PI should think so.\x02\x03",
            "You two are newbies. And little\x01",
            "brats, to say the least.\x02\x03",
            "Not to mention, you're lacking in strength\x01",
            "and experience. You don't have the ability\x01",
            "to make quick, sound judgments.\x02\x03",
            "If you get all caught up in yourselves and\x01",
            "forget that, one of these days you're going\x01",
            "to get the rug pulled out from under you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2PWe-we're not all caught up in\x01",
            "ourselves!\x02\x03",
            "How about yourself, Mr. Macho Man? What\x01",
            "were you thinking trying to hike through\x01",
            "the pass at this hour of the night?\x02\x03",
            "You're either plain careless...\x01",
            "or maybe that bandanna's just a\x01",
            "little too tight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#3PWatch your mouth, brat. I'm not like\x01",
            "you amateurs. I'm trying to hone my\x01",
            "skills out here.\x02\x03",
            "And besides, I'm here for work.\x01",
            "Don't try and compare my actions\x01",
            "with your tourist-training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2PWork? You mean a guild job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#3PYeah, that's right. The work your\x01",
            "old man forced on me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2PDad pushed his work onto you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F#3P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 315, 400)

    ChrTalk(
        0x106,
        (
            "#053FForget about it. I've got an early\x01",
            "day ahead of me, so I need to\x01",
            "get some rest.\x02\x03",
            "You two quit talking and get some\x01",
            "sleep, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_586C():
        OP_6D(79640, 0, 54740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_586C)
    OP_8E(0x106, 0x12F52, 0x0, 0xDCA0, 0x9C4, 0x0)
    OP_8C(0x106, 180, 400)
    SetChrFlags(0x106, 0x4)
    OP_96(0x106, 0x1287C, 0x0, 0xDDCC, 0x3E8, 0x1388)

    ChrTalk(
        0x101,
        (
            "#005F#2PAh! He just avoided finishing\x01",
            "the conversation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#2PWell, he did drop a tidbit about Dad.\x01",
            "That's something, at least...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F#3PEnough already, you two! Just shut\x01",
            "the hell up, and let me sleep!\x02\x03",
            "And you better stop poking around\x01",
            "where you shouldn't or you're gonna\x01",
            "get burned.\x02\x03",
            "#053FInstead, why don't you get your\x01",
            "behinds over to Ruan, and do some\x01",
            "jobs off the bulletin board?\x02\x03",
            "That's...*yawn*...far better suited\x01",
            "for the likes of you...\x02\x03",
            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#2PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5PIt looks like he's asleep...and just\x01",
            "as quickly as someone I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2PDon't you even dare suggest that\x01",
            "I'm anything like this jerk!\x02\x03",
            "#007FWhat's his deal anyway?!\x02\x03",
            "It seems to me like all he's trying\x01",
            "to do is pick a fight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5PRelax, Estelle. It's true we're still\x01",
            "just novices at this.\x02\x03",
            "He's probably just worried about\x01",
            "us, and doesn't know how else to\x01",
            "express it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P...\x02\x03",
            "Do you really think so, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#005F#5PI wish I could say for sure,\x01",
            "but I don't know.\x02\x03",
            "#010FHe was right about one thing for\x01",
            "sure, though: we SHOULD turn in\x01",
            "for the night.\x02\x03",
            "We've still got to hike down through\x01",
            "the pass tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2PI'm all riled up now, but I guess\x01",
            "there's nothing to be done about\x01",
            "it...\x02\x03",
            "#006FUnless...we doodle on this jerk's\x01",
            "face and then go to sleep.\x02\x03",
            "I'm pretty sure he wouldn't wake up\x01",
            "with the way he's snoring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#5PDon't even think about it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3D55 end

    def Function_13_5E8E(): pass

    label("Function_13_5E8E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(80978, 0, 152763, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x101, 84150, 0, 151987, 45)
    SetChrPos(0x102, 80770, 0, 151987, 45)
    SetChrPos(0x106, 76070, 0, 151787, 315)
    OP_62(0x101, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    OP_8C(0x101, 225, 400)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 225, 400)
    OP_62(0x102, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    OP_63(0x102)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x106, 135, 400)
    OP_62(0x106, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    OP_63(0x106)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#000FWh-What was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#5PSounds like something's going on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F...\x02\x03",
            "I'm going to go check it out.\x01",
            "You two stay here.\x02",
        )
    )

    CloseMessageWindow()
    OP_96(0x106, 0x1302D, 0x0, 0x25051, 0x3E8, 0x1770)
    OP_8E(0x106, 0x12E29, 0x0, 0x242F5, 0x1388, 0x0)
    OP_8E(0x106, 0x11E79, 0x0, 0x240ED, 0x1388, 0x0)
    SetChrFlags(0x106, 0x80)

    ChrTalk(
        0x101,
        "#000FAh! Now just you wait a min...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#5PI think we'd better go see for\x01",
            "ourselves, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FOf course that's what we\x01",
            "should do!\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 82130, 0, 148000, 270)
    RemoveParty(0x5, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_13_5E8E end

    def Function_14_6139(): pass

    label("Function_14_6139")

    OP_72(0x3, 0x20)
    OP_6F(0x3, 10)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    RemoveParty(0x5, 0xFF)
    EventBegin(0x0)
    OP_6D(84500, 0, 57320, 0)
    SetChrPos(0x102, 82610, 0, 56640, 90)
    SetChrPos(0x101, 84250, 650, 56940, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 7)
    FadeToDark(0, 0, -1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#010FEstelle. Estelle, wake up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#455F#4P*yawn*...Come on, can't a woman\x01",
            "have her beauty sleep...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 16)
    OP_1D(0x10)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#457F#4PHuh? Joshua...?\x02\x03",
            "Is it already time to go to the\x01",
            "guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FWhat are you talking about?\x01",
            "This is the Krone Pass Checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_62F0():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F0)
    Sleep(50)
    OP_6F(0x3, 10)
    OP_70(0x3, 0x14)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#456F#4POh right...we had that monster\x01",
            "scare last night and...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x11, 0x15, 0x5DC)

    ChrTalk(
        0x101,
        "#453F#4PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_6D(82170, 0, 55040, 1500)

    ChrTalk(
        0x101,
        "#451F#4PWhere'd the redheaded jerk go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3PIt looks like he took off early this\x01",
            "morning. Apparently, he had an\x01",
            "urgent job to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#452F#4POh...\x02\x03",
            "#455F#4PAnd after we helped him fend off\x01",
            "those monsters last night, too.\x02\x03",
            "How rude of him not to say\x01",
            "anything before leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3PIt's not that big of a deal,\x01",
            "Estelle.\x02\x03",
            "How about we get ready ourselves?\x01",
            "I'd like to make it through the pass\x01",
            "by noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#454F#4PAll right.\x02\x03",
            "It's off to Ruan we go!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_72(0x3, 0x8)
    OP_72(0x3, 0x20)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    SetChrPos(0x101, 77640, 0, 53190, 270)
    SetChrPos(0x102, 77640, 0, 53190, 270)
    OP_6D(77640, 0, 53190, 0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x406)
    OP_28(0x3A, 0x4, 0x2)
    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x1, 0x1)
    OP_28(0x3A, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_14_6139 end

    def Function_15_65F4(): pass

    label("Function_15_65F4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6665")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#010FThis leads back to the Bose region.\x02\x03",
            "Without a pass, we can't return\x01",
            "that way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C5")

    label("loc_6665")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010FThis leads back to the Bose region.\x02\x03",
            "Without a pass, we can't return\x01",
            "that way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C5")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_15_65F4 end

    def Function_16_66E1(): pass

    label("Function_16_66E1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68FC")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x32)
    OP_73(0x33)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 19740, 0, 13090, 217)
    SetChrPos(0x1, 19740, 0, 13090, 217)
    SetChrPos(0x2, 19740, 0, 13090, 217)
    SetChrPos(0x3, 19740, 0, 13090, 217)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_68FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6916")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_6916")

    Return()

    # Function_16_66E1 end

    SaveToFile()

Try(main)
