from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3221   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '麻绪婆婆',                             # 9
        '艾德',                                 # 10
        '拜舍尔',                               # 11
        '林',                                   # 12
        '莉西亚',                               # 13
        '希利尔',                               # 14
        '艾缇',                                 # 15
        '拉克',                                 # 16
        '希玛',                                 # 17
        '库安',                                 # 18
        '西加罗',                               # 19
        '艾德尔',                               # 20
        '东方打扮的男人',                       # 21
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01160 ._CH',             # 07
        'ED6_DT07/CH01020 ._CH',             # 08
        'ED6_DT07/CH01060 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01043 ._CH',             # 0C
        'ED6_DT07/CH01213 ._CH',             # 0D
        'ED6_DT07/CH00073 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01160P._CP',             # 07
        'ED6_DT07/CH01020P._CP',             # 08
        'ED6_DT07/CH01060P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01043P._CP',             # 0C
        'ED6_DT07/CH01213P._CP',             # 0D
        'ED6_DT07/CH00073P._CP',             # 0E
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 14070,
        Z                   = 0,
        Y                   = 2040,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 8960,
        TriggerZ            = 250,
        TriggerY            = 13840,
        TriggerRange        = 1000,
        ActorX              = 9100,
        ActorZ              = 1750,
        ActorY              = 13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5290,
        TriggerZ            = 0,
        TriggerY            = 71030,
        TriggerRange        = 800,
        ActorX              = 5290,
        ActorZ              = 1000,
        ActorY              = 71030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2670,
        TriggerZ            = 250,
        TriggerY            = 3820,
        TriggerRange        = 400,
        ActorX              = 2590,
        ActorZ              = 1750,
        ActorY              = 5360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9940,
        TriggerZ            = 0,
        TriggerY            = 90,
        TriggerRange        = 400,
        ActorX              = 8490,
        ActorZ              = 1500,
        ActorY              = 340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_352",          # 00, 0
        "Function_1_6E3",          # 01, 1
        "Function_2_71D",          # 02, 2
        "Function_3_733",          # 03, 3
        "Function_4_757",          # 04, 4
        "Function_5_9D2",          # 05, 5
        "Function_6_CC5",          # 06, 6
        "Function_7_13F1",         # 07, 7
        "Function_8_175A",         # 08, 8
        "Function_9_1761",         # 09, 9
        "Function_10_1768",        # 0A, 10
        "Function_11_1B9F",        # 0B, 11
        "Function_12_1BA4",        # 0C, 12
        "Function_13_2157",        # 0D, 13
        "Function_14_21D4",        # 0E, 14
        "Function_15_21DB",        # 0F, 15
        "Function_16_21E2",        # 10, 16
        "Function_17_21E9",        # 11, 17
        "Function_18_21EE",        # 12, 18
        "Function_19_3402",        # 13, 19
        "Function_20_3B85",        # 14, 20
        "Function_21_46E8",        # 15, 21
        "Function_22_4A31",        # 16, 22
        "Function_23_4A74",        # 17, 23
    )


    def Function_0_352(): pass

    label("Function_0_352")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_362"),
        (109, "loc_390"),
        (SWITCH_DEFAULT, "loc_3A6"),
    )


    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375")
    OP_A2(0x51D)
    Event(0, 19)

    label("loc_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38D")
    SetMapFlags(0x10000000)
    OP_A2(0x520)
    Event(0, 20)

    label("loc_38D")

    Jump("loc_3A6")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A3")
    OP_A2(0x526)
    Event(0, 21)

    label("loc_3A3")

    Jump("loc_3A6")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3DC")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    Jump("loc_6E2")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_45B")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1040, 0, 40770, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -28880, 0, 43500, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28740, 0, 38750, 93)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_6E2")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4D1")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28740, 0, 38750, 93)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE")
    ClearChrFlags(0x14, 0x80)

    label("loc_4CE")

    Jump("loc_6E2")

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_559")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 12)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 11260, 150, 10650, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 13)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 11070, 150, 8460, 358)
    Jump("loc_6E2")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5A5")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    Jump("loc_6E2")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_643")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1040, 0, 40770, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 12)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 11260, 150, 10650, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 13)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 11070, 150, 8460, 358)
    Jump("loc_6E2")

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_679")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10430, 0, 1740, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2230, 250, 3550, 0)
    Jump("loc_6E2")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_699")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 11910, 0, 67870, 180)
    Jump("loc_6E2")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8490, 0, 340, 102)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2080, 250, 6150, 195)

    label("loc_6E2")

    Return()

    # Function_0_352 end

    def Function_1_6E3(): pass

    label("Function_1_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FB")
    OP_B1("t3221_y")
    Jump("loc_704")

    label("loc_6FB")

    OP_B1("t3221_n")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    OP_72(0x2, 0x10)
    Jump("loc_71C")

    label("loc_718")

    OP_64(0x1, 0x1)

    label("loc_71C")

    Return()

    # Function_1_6E3 end

    def Function_2_71D(): pass

    label("Function_2_71D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_732")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_71D")

    label("loc_732")

    Return()

    # Function_2_71D end

    def Function_3_733(): pass

    label("Function_3_733")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_756")
    OP_8D(0xFE, -30720, 37410, -25780, 40750, 1500)
    Jump("Function_3_733")

    label("loc_756")

    Return()

    # Function_3_733 end

    def Function_4_757(): pass

    label("Function_4_757")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_764")
    Jump("loc_9CE")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7F5")

    ChrTalk(
        0xFE,
        (
            "回到王都以后\x01",
            "又要开始忙碌的日子了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前泡泡温泉，\x01",
            "积蓄一些精力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_8A4")

    ChrTalk(
        0xFE,
        (
            "听客房的服务生说，\x01",
            "蔡斯好像出事了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连这种偏僻地方\x01",
            "都已经听到了传闻，\x01",
            "那边肯定是发生大乱子了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_90E")

    ChrTalk(
        0xFE,
        (
            "好好泡一下温泉，\x01",
            "缓解旅途的劳累……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了接下来的采购\x01",
            "养足精神吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_918")
    Jump("loc_9CE")

    label("loc_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_9B3")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "看到那些可爱的餐具，\x01",
            "想也没想就买下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家特产店里\x01",
            "好像还可以淘到很多宝贝呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_9BD")
    Jump("loc_9CE")

    label("loc_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_9C7")
    Jump("loc_9CE")

    label("loc_9C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9CE")

    label("loc_9CE")

    TalkEnd(0xFE)
    Return()

    # Function_4_757 end

    def Function_5_9D2(): pass

    label("Function_5_9D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_9DF")
    Jump("loc_CC1")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_A85")

    ChrTalk(
        0xFE,
        (
            "和妻子商量过了，\x01",
            "最近就在这里\x01",
            "好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在女王的诞辰庆典开始之前\x01",
            "回王都就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC1")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A8F")
    Jump("loc_CC1")

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(
        0xFE,
        (
            "那么～\x01",
            "这就去泡个晨澡吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E")

    label("loc_ACC")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "你们要离开这里了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们暂时还会\x01",
            "在这里休息一阵子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0E")

    Jump("loc_CC1")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B1B")
    Jump("loc_CC1")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(
        0xFE,
        (
            "就在我没注意的一瞬间，\x01",
            "妻子已经去特产店买了好多东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然买东西没什么不好，\x01",
            "不过还是希望她想好了之后再去买。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA3")

    label("loc_BD8")

    OP_A2(0xA)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "就在我没注意的一瞬间，\x01",
            "妻子已经去特产店买了好多东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然买东西没什么不好，\x01",
            "不过还是希望她想好了之后再去买。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA3")

    Jump("loc_CC1")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_CB0")
    Jump("loc_CC1")

    label("loc_CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_CBA")
    Jump("loc_CC1")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CC1")

    label("loc_CC1")

    TalkEnd(0xFE)
    Return()

    # Function_5_9D2 end

    def Function_6_CC5(): pass

    label("Function_6_CC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D9B")

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "好不容易闲下来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "就趁现在赶快准备一下\x01",
            "待会儿的饭菜吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天突然\x01",
            "一下子来了很多客人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E73")

    label("loc_D9B")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "好不容易闲下来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "为什么客人们\x01",
            "都在同一天来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果每个人能把\x01",
            "来的时间错开的话，\x01",
            "就能更舒服地享受温泉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E73")

    Jump("loc_13ED")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EF3")

    ChrTalk(
        0xFE,
        "怎么样，调查进展如何了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里和平常一样还是很忙啊。\x01",
            "因为老是只有我一个人干活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "难道你们今天是来调查案件的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里也已经传来消息了。\x01",
            "中央工房的东西被盗走了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当游击士\x01",
            "实在是很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1013")

    ChrTalk(
        0xFE,
        "啊，要走了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后有空的话\x01",
            "要再来玩啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_112E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(
        0xFE,
        (
            "东方的料理\x01",
            "不仅味道可口，\x01",
            "而且对健康很有好处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然做起来\x01",
            "要花不少时间和精力，\x01",
            "不过却相当值得。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112B")

    label("loc_10B4")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "啊，要去泡澡了吗？\x01",
            "慢慢享受吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我就趁这段时间给你们\x01",
            "做好吃的东方料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112B")

    Jump("loc_13ED")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_123E")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "刚才麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听到客人平安无事，\x01",
            "我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这下可以开始安心地准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为来了不少新客人，\x01",
            "我这边也变得更忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_123E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_12D0")

    ChrTalk(
        0xFE,
        (
            "没想到竟然\x01",
            "会有游击士在这里。\x01",
            "这下就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这件事就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_12DA")
    Jump("loc_13ED")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_135D")

    ChrTalk(
        0xFE,
        (
            "偶尔放松一下，\x01",
            "给自己放个假虽然很好……\x01",
            "但是时间久了就会消磨干劲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "人啊，\x01",
            "真是容易懒散下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13ED")

    label("loc_135D")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "啊～今天很闲啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "偶尔放松一下，\x01",
            "给自己放个假虽然很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是时间久了\x01",
            "就会消磨干劲了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13ED")

    TalkEnd(0xFE)
    Return()

    # Function_6_CC5 end

    def Function_7_13F1(): pass

    label("Function_7_13F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13FE")
    Jump("loc_1756")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_14CC")

    ChrTalk(
        0xFE,
        (
            "我觉得只有充分休息\x01",
            "才能让身心都恢复活力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "总觉得有一种\x01",
            "会钓到大型猎物的预感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好，最好抓紧时间。\x01",
            "趁这种感觉还没消失，\x01",
            "快赶到下一个钓场！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1548")

    ChrTalk(
        0xFE,
        (
            "刚才听到了小道消息，\x01",
            "说是蔡斯出事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "最近的骚动真让人不安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_1548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1552")
    Jump("loc_1756")

    label("loc_1552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15E6")

    ChrTalk(
        0xFE,
        (
            "嘿，\x01",
            "你们也要在这里住宿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "一定要泡露天温泉哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要体验过一次，\x01",
            "你们就会迷上这个温泉的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1756")

    label("loc_15E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_15F0")
    Jump("loc_1756")

    label("loc_15F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_174F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16CE")

    ChrTalk(
        0xFE,
        (
            "就算不泡澡，\x01",
            "也还有很多乐趣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个『红叶亭』的\x01",
            "正宗东方料理味道相当不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，这里确实是个天堂。\x01",
            "我现在就开始期待晚餐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174C")

    label("loc_16CE")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "抽取温泉水的水泵\x01",
            "好像有一点故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算啦，\x01",
            "这个温泉胜地已经有年头了。\x01",
            "发生这种事情也没什么好奇怪的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174C")

    Jump("loc_1756")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1756")

    label("loc_1756")

    TalkEnd(0xFE)
    Return()

    # Function_7_13F1 end

    def Function_8_175A(): pass

    label("Function_8_175A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_175A end

    def Function_9_1761(): pass

    label("Function_9_1761")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_1761 end

    def Function_10_1768(): pass

    label("Function_10_1768")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1775")
    Jump("loc_1B9B")

    label("loc_1775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_189E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1810")

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "快点抓住那些\x01",
            "袭击中央工房的犯人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "绝对不能让那种\x01",
            "无法无天的家伙逍遥法外。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_1810")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "啊，是你们。\x01",
            "还是这么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从艾德那里听说了，\x01",
            "你们是游击士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请加油。\x01",
            "我支持你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189B")

    Jump("loc_1B9B")

    label("loc_189E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_18A8")
    Jump("loc_1B9B")

    label("loc_18A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_18B2")
    Jump("loc_1B9B")

    label("loc_18B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_18BC")
    Jump("loc_1B9B")

    label("loc_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_19E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_18FD")

    ChrTalk(
        0xFE,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『柚子之间』\x01",
            "是这里隔壁的房间哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E2")

    label("loc_18FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_196D")

    ChrTalk(
        0xFE,
        (
            "那么，趁现在还早，\x01",
            "赶快收拾一下床铺吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "马上就是晚饭时间了，\x01",
            "客人们都该回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E2")

    label("loc_196D")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "哎呀，太好了。\x01",
            "有人来修理水泵了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们总是受到\x01",
            "中央工房的照顾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E2")

    Jump("loc_1B9B")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "今天真难办啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为，\x01",
            "温泉的水泵出了点故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不早点修理好的话\x01",
            "会让客人们失望的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "客人们都是为了温泉\x01",
            "才来这里的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B91")

    label("loc_1AE8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "欢迎。\x01",
            "这里是温泉旅馆『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个旅馆的客房\x01",
            "都有各自的名字哦。\x01",
            "这里叫做『柚子之间』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起『２０１室』这类的名字\x01",
            "更加有情调吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B91")

    Jump("loc_1B9B")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B9B")

    label("loc_1B9B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1768 end

    def Function_11_1B9F(): pass

    label("Function_11_1B9F")

    Call(0, 12)
    Return()

    # Function_11_1B9F end

    def Function_12_1BA4(): pass

    label("Function_12_1BA4")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                 # 0
            "买东西\x01",                               # 1
            "欢迎品尝「诱惑山菜火锅」700米拉\x01",      # 2
            "离开\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C21")
    OP_0D()
    OP_A9(0x46)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_1C21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CF5")
    SubMira(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "诱惑山菜火锅\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4)"), scpexpr(EXPR_END)), "loc_1CB6")
    Jump("loc_1CE7")

    label("loc_1CB6")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "诱惑山菜火锅\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE7")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1D1D")

    label("loc_1CF5")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1D1D")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_1D2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D40")
    TalkEnd(0xE)
    Return()

    label("loc_1D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DBD")

    ChrTalk(
        0xE,
        (
            "只有这种时候\x01",
            "才适合做扫除啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "一会儿旅馆又会挤满\x01",
            "来这里泡温泉的客人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E42")

    label("loc_1DBD")

    OP_A2(0x6)

    ChrTalk(
        0xE,
        (
            "啊，欢迎光临。\x01",
            "这里是『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "因为大家都去王都参加诞辰庆典了，\x01",
            "所以能有客人来我们非常欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E42")

    Jump("loc_2153")

    label("loc_1E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1E4F")
    Jump("loc_2153")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1F02")

    ChrTalk(
        0xE,
        (
            "今天不管和谁说话，\x01",
            "都是在谈论蔡斯的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "难得来到这个温泉胜地，\x01",
            "却只顾着谈论这么阴暗的话题……\x01",
            "真是感到有些失落啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_1F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(
        0xE,
        "啊，已经要回去了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "下次来的时候，\x01",
            "要慢慢好好享受哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1FCC")

    ChrTalk(
        0xE,
        (
            "泡完澡出来享用东方料理，\x01",
            "会更有一番风味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "痛痛快快地出汗吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_1FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_END)), "loc_202E")

    ChrTalk(
        0xE,
        (
            "差不多该去\x01",
            "帮忙准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "我们这里的东方料理是正宗的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_20B9")

    ChrTalk(
        0xE,
        (
            "这次来修理水泵的\x01",
            "好像是提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "明明年纪还很小，\x01",
            "却这么了不起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "再看我自己，\x01",
            "连换个灯泡都不会呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_20C3")
    Jump("loc_2153")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_20CD")
    Jump("loc_2153")

    label("loc_20CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2153")

    ChrTalk(
        0xE,
        (
            "啊，欢迎光临。\x01",
            "这里是『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "请好好享受\x01",
            "我们的东方料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2153")

    TalkEnd(0xE)
    Return()

    # Function_12_1BA4 end

    def Function_13_2157(): pass

    label("Function_13_2157")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#073F这里的东方料理挺正宗的。\x01",
            "　\x02\x03",
            "#070F不过难得有机会来这里，\x01",
            "还是想尝尝真正的利贝尔料理啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2157 end

    def Function_14_21D4(): pass

    label("Function_14_21D4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_21D4 end

    def Function_15_21DB(): pass

    label("Function_15_21DB")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_15_21DB end

    def Function_16_21E2(): pass

    label("Function_16_21E2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_16_21E2 end

    def Function_17_21E9(): pass

    label("Function_17_21E9")

    Call(0, 18)
    Return()

    # Function_17_21E9 end

    def Function_18_21EE(): pass

    label("Function_18_21EE")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224E")
    OP_0D()
    OP_A9(0x45)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_224E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225F")
    TalkEnd(0x8)
    Return()

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2928")
    EventBegin(0x0)
    OP_A2(0x525)
    OP_28(0x40, 0x1, 0x800)
    OP_28(0x40, 0x4, 0x10)
    Fade(1000)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, 1810, 250, 3490, 45)
    SetChrPos(0x102, 2500, 250, 2380, 0)
    SetChrPos(0x107, 3160, 250, 3550, 0)
    OP_6D(2080, 250, 5120, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#680F提妲，谢谢你啦。\x02\x03",
            "多亏你的帮忙，\x01",
            "水泵已经修好了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F嘿嘿……\x02\x03",
            "经常受到婆婆您的照顾，\x01",
            "这点小事也是我应该做的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F呵呵，这孩子不仅能干，\x01",
            "而且小嘴还是那么的甜。\x02\x03",
            "#680F对了，还有这边两位。\x01",
            "刚才也真是辛苦你们了。\x02\x03",
            "那客人应该是你们的熟人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F#1P啊哈哈，算是吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 270, 400)

    ChrTalk(
        0x107,
        "#064F发生了什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也没什么。\x01",
            "算是做了点游击士的份内工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F总之，\x01",
            "你们真是帮了大忙啦。\x02\x03",
            "为了聊表我的谢意，\x01",
            "今天就在这里休息一晚吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P哎，可以吗！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(
        0x107,
        (
            "#065F那、那个，婆婆。\x02\x03",
            "我们没和爷爷说\x01",
            "今天要住在这里的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F啊，不用担心了。\x01",
            "刚才拉赛尔已经和我联络过了。\x02\x03",
            "他说『这里的工作明天才能完成，\x01",
            "让他们今天就住在你那里吧』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F爷爷这样说吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P嘿嘿～\x01",
            "博士还真机灵嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F既然如此，\x01",
            "那就恭敬不如从命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F嗯，不要客气啦。\x02\x03",
            "二楼的『柚子之间』是给你们准备的，\x01",
            "去把行李放下吧。\x02\x03",
            "离晚饭还有段时间，\x01",
            "你们先去泡泡温泉好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#1P饭前洗澡？\x02\x03",
            "唔……\x01",
            "一般不都是睡觉前才洗的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F哎呀～你在说啥呀。\x01",
            "难得来这一趟，当然要泡温泉才行啦。\x02\x03",
            "从早到晚，\x01",
            "啥时候泡都是正常的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(
        0x107,
        (
            "#061F呵呵～～\x01",
            "就算一天泡三次也是常有的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#1P是、是这样啊……\x02\x03",
            "嗯～虽然我很喜欢洗澡，\x01",
            "但一天泡那么多次一定会晕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，泡温泉之前，\x01",
            "我们先把行李放到房间里吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_33FE")

    label("loc_2928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2993")

    ChrTalk(
        0x8,
        (
            "#680F有空的话\x01",
            "你们可以随时来这里住。\x02\x03",
            "那么，\x01",
            "去王都的路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDB")

    label("loc_2993")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#683F啊，是你们……\x01",
            "犯人的调查已经告一段落了吗？\x02\x03",
            "#680F工作完成之后，\x01",
            "就来好好歇歇吧。\x02\x03",
            "上次多亏你们，客人们也十分满意。\x01",
            "我可以把整个露天温泉包给你们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～\x01",
            "我们也想这样……\x02\x03",
            "不过，\x01",
            "现在必须得去王都一趟呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "之前真是承蒙照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F哪里，别这么客气嘛。\x01",
            "就算是修理水泵的谢礼吧。\x02\x03",
            "#680F提妲还是老样子，\x01",
            "又在帮拉赛尔干活吗？\x02\x03",
            "这样太勉强那个孩子了，\x01",
            "你们俩要帮我\x01",
            "和拉赛尔说说才行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F啊…………\x02\x03",
            "#501F……嗯！\x01",
            "我知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会转达的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F那么，\x01",
            "去王都的路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDB")

    Jump("loc_33FE")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2C93")

    ChrTalk(
        0x8,
        (
            "#680F啊，是你们。\x02\x03",
            "总是为了追捕犯人\x01",
            "而东奔西走忙个不停啊。\x02\x03",
            "虽然很遗憾……\x01",
            "不过在这一带\x01",
            "没有听说什么线索。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D37")

    ChrTalk(
        0x8,
        (
            "#680F听说中央工房发生了强盗事件，\x01",
            "真是有点担心啊。\x01",
            "　\x02\x03",
            "不过看你们的样子好像没什么问题。\x01",
            "呼，终于放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE8")

    label("loc_2D37")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#682F啊啊，是你们。\x01",
            "不过应该没事吧？\x02\x03",
            "听说中央工房发生了强盗事件，\x01",
            "真是有点担心啊。\x01",
            "　\x02\x03",
            "不过看你们的样子好像没什么问题。\x01",
            "呼，终于放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE8")

    Jump("loc_33FE")

    label("loc_2DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E48")

    ChrTalk(
        0x8,
        (
            "#680F啊，怎么了呢。\x02\x03",
            "是不是又想去\x01",
            "露天温泉泡澡呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_2E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_2EDE")

    ChrTalk(
        0x8,
        (
            "#680F温泉和这里是分开的，\x01",
            "从食堂里面的通道过去吧。\x02\x03",
            "请在我们引以为豪的露天温泉里\x01",
            "慢慢享受一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_2EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_327D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_END)), "loc_2F64")

    ChrTalk(
        0x8,
        (
            "#680F你们的房间 \x01",
            "是二楼的『柚子之间』哦。\x02\x03",
            "先把行李放好，\x01",
            "然后可以一直在温泉里泡到吃晚饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_2F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_301D")

    ChrTalk(
        0x8,
        (
            "#680F那孩子和拉赛尔一样，\x01",
            "一摸到机械就停不下手。\x02\x03",
            "麻烦你们去水泵小屋看看情况吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_301D")

    OP_A2(0x58D)

    ChrTalk(
        0x8,
        (
            "#680F哎呀，\x01",
            "真是辛苦你们了呢。\x02\x03",
            "那个客人是你们的熟人吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊哈哈，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来水泵的修理也顺利地完成了呢。\x01",
            "　\x02\x03",
            "外面的水井也开始有热水涌出来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F啊，是吗？\x02\x03",
            "但是提妲还在小屋那里没回来呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "刚才应该先去小屋看看情况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊，我们现在去看看吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F那就拜托你们了。\x02\x03",
            "那孩子和拉赛尔一样，\x01",
            "一摸到机械就停不下手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F哈哈，没错呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F麻烦你们了，\x01",
            "又让你们跑一趟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327A")

    Jump("loc_33FE")

    label("loc_327D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_32E6")

    ChrTalk(
        0x8,
        (
            "#680F不好意思，\x01",
            "又给你们添麻烦了。\x02\x03",
            "无论如何请帮忙\x01",
            "到平原道找到那个客人，\x01",
            "并把她平安地带回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_32E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3366")

    ChrTalk(
        0x8,
        (
            "#680F怎么，\x01",
            "忘了水泵小屋在哪里了吗？\x02\x03",
            "走到村子的广场那里，\x01",
            "从北面的斜坡上去就到了。\x02\x03",
            "那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_3366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33FE")

    ChrTalk(
        0x8,
        (
            "#680F嘿～欢迎。\x01",
            "本旅馆有我们引以为豪的天然温泉。\x02\x03",
            "其中东方风格的露天澡堂\x01",
            "特别受客人们欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FE")

    TalkEnd(0x8)
    Return()

    # Function_18_21EE end

    def Function_19_3402(): pass

    label("Function_19_3402")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(560, 250, 2580, 0)
    SetChrPos(0x101, 490, 0, -1490, 0)
    SetChrPos(0x102, 2040, 0, -1370, 0)
    SetChrPos(0x107, 1200, 0, -430, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        "#061F您好，麻绪婆婆。\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#681F哎呀，提妲，\x01",
            "你总算来了呀。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34C6():
        OP_6D(2050, 250, 4540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34C6)

    def lambda_34DE():
        OP_8E(0xFE, 0xA78, 0xFA, 0xDCA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_34DE)
    Sleep(500)

    def lambda_34FE():
        OP_8E(0xFE, 0xDF2, 0xFA, 0xA5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34FE)
    Sleep(300)

    def lambda_351E():
        OP_8E(0xFE, 0x8CA, 0xFA, 0x9D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_351E)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(
        0x8,
        (
            "#680F就在刚刚，\x01",
            "工房长和我联络过了。\x02\x03",
            "说拉赛尔那家伙\x01",
            "让你一个人来帮忙修理，\x01",
            "自己却在搞啥乱七八糟的研究是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F不、不是那样呢～\x02\x03",
            "其实其实，\x01",
            "爷爷他本来是打算亲自来的。\x01",
            "是我硬求他让我来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F哎呀～提妲可真是个\x01",
            "又温柔又体贴的好孩子呢。\x02\x03",
            "不过嘛，\x01",
            "太娇纵那老头子可不行哦。\x02\x03",
            "从以前开始就只知道研究啊研究，\x01",
            "就这样放任不管的话，\x01",
            "真不知会沉沦到啥地步呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F（好健朗的婆婆啊。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（好像和博士很熟呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#683F啊，你们两位是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，婆婆，\x01",
            "我来介绍一下。\x02\x03",
            "这两位是艾丝蒂尔姐姐和约修亚哥哥。\x02\x03",
            "他们是游击士协会的游击士，\x01",
            "这次是特地护送我来这里的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F婆婆，您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F哦，是这样啊。\x01",
            "真是麻烦你们两位了。\x02\x03",
            "#680F我是这个『红叶亭』的老板娘，\x01",
            "你们叫我麻绪婆婆就行了。\x02\x03",
            "拉赛尔和我是儿时玩伴，\x01",
            "所以这孩子呀，就像我的亲孙女一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎～是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F嘿嘿……\x02\x03",
            "#064F对了，婆婆。\x02\x03",
            "那个导力泵\x01",
            "真的是坏了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#682F啊啊，是啊。\x02\x03",
            "已经是４０年前的机械了，\x01",
            "差不多快寿终正寝了吧……\x02\x03",
            "唉，虽说迟早要换新泵，\x01",
            "眼下还是应急修理一下吧。\x02\x03",
            "提妲，没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F嗯，交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#680F好，那就把这个拿去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "借来了\x07\x02",
            "水泵小屋的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x369, 1)

    ChrTalk(
        0x8,
        (
            "#680F水泵小屋就在村里的广场北边，\x01",
            "向北登上高台就是了。\x02\x03",
            "那么就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x4)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_19_3402 end

    def Function_20_3B85(): pass

    label("Function_20_3B85")

    EventBegin(0x0)
    OP_6D(560, 250, 2580, 0)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x101, 490, 0, -1490, 0)
    SetChrPos(0x102, 2040, 0, -1370, 0)
    FadeToBright(1000, 0)

    def lambda_3BCE():
        OP_6D(1770, 250, 5380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BCE)

    def lambda_3BE6():
        OP_8E(0xFE, 0x92E, 0xFA, 0xDA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BE6)

    def lambda_3C01():
        OP_8E(0xFE, 0xE38, 0xFA, 0xD84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C01)
    OP_0D()
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#683F#2P哎呀，是你们啊。\x01",
            "提妲她搞得怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，已经开始修理了。\x02\x03",
            "既然我们帮不上什么忙，\x01",
            "站在她旁边又反而会妨碍她工作，\x01",
            "所以还是先在这里等等她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#681F#2P啊哈哈，\x01",
            "真是明智的选择。\x02\x03",
            "那孩子在某些方面，\x01",
            "可是比拉赛尔更有天分呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F天分……\x01",
            "这么说来也的确是啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F年纪那么小\x01",
            "就能在中央工房帮忙工作，\x01",
            "在普通人看来已经是很不简单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F#2P而且人又细心、又坚强，\x01",
            "无论什么时候都面带开朗的笑容。\x02\x03",
            "虽说一开始摆弄机器\x01",
            "就会马上迷了进去……\x02\x03",
            "总之，就是个非常好的孩子啦。\x02\x03",
            "#682F……不过……\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F怎么啦，婆婆？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#680F#2P不……没啥。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 970, 0, -2050, 0)
    OP_4A(0x9, 255)

    ChrTalk(
        0x9,
        "#2P喂～麻绪婆婆！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3F3D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F3D)

    def lambda_3F4B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F4B)

    def lambda_3F59():
        OP_6D(1070, 250, 4930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F59)

    def lambda_3F71():

        label("loc_3F71")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3F71")

    QueueWorkItem2(0x101, 1, lambda_3F71)

    def lambda_3F82():

        label("loc_3F82")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3F82")

    QueueWorkItem2(0x102, 1, lambda_3F82)

    def lambda_3F93():
        OP_8E(0xFE, 0xD02, 0xFA, 0xA1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F93)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3FBE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3FBE)
    OP_8E(0x9, 0x7C6, 0xFA, 0xDC0, 0xBB8, 0x0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "#683F#2P艾德，你回来了啊。\x02\x03",
            "那么着急的样子，\x01",
            "发生啥事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P哎呀，那个……\x01",
            "有件事我想打听一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P那个从王都来的小姐\x01",
            "回来了没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#680F#2P从王都来的……\x01",
            "啊啊，你是说昨天来的那个客人吗。\x02\x03",
            "她说要去散步，\x01",
            "到现在还没有回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P果然是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P嗯……这下糟了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#683F#2P怎么了？\x01",
            "她不在村子里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P不，那个……其实啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P刚才我在村子的门口\x01",
            "看到那个小姐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P她好像说为了找景色漂亮的地方，\x01",
            "要到平原那里去散步……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#682F#2P去平原散步？\x01",
            "那里有很多魔兽啊，怎么这么乱来……\x02\x03",
            "#684F你这个大笨蛋！\x01",
            "当时怎么不阻止她呀！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x9,
        "#1P可、可是，我阻止过了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P该怎么说呢，\x01",
            "她是那种我行我素的类型啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P刚才一点儿也不\x01",
            "把我的劝阻当成一回事。\x01",
            "所以我才担心，过来问你嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(
        0x101,
        "#002F那个，打扰一下可以吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 400)
    OP_8C(0x8, 135, 400)

    ChrTalk(
        0x9,
        "#1P嗯？什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P咦，来了新客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#6P我想请问一下……\x01",
            "您是在什么时候见到那位客人的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P什么时候……\x01",
            "我想大概是中午吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P我正好吃完午饭回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F中午……\x01",
            "嗯，看来应该能赶得上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#6P我们马上去追吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P我说……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F别看我们这样年轻，\x01",
            "其实我们两个都是协会的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P我们这就出发，\x01",
            "去护送那位去平原的客人回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P协会……你们是游击士！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P这下可放心了。\x01",
            "那我可就全拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        (
            "#684F#2P拜托这句话，你还好意思说吗？\x02\x03",
            "#682F#2P算了……\x01",
            "客人的安全才是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)

    ChrTalk(
        0x8,
        (
            "#682F#2P虽然很不好意思，\x01",
            "不过这次就麻烦你们两位了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#006F嗯，包在我们身上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#6P那我们出发了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x20)
    OP_28(0x40, 0x1, 0x40)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    Return()

    # Function_20_3B85 end

    def Function_21_46E8(): pass

    label("Function_21_46E8")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(28000, 0, 40030, 0)
    SetChrPos(0x101, 33900, 0, 44790, 180)
    SetChrPos(0x102, 34550, 0, 44500, 180)
    SetChrPos(0x107, 33460, 0, 45000, 180)
    FadeToBright(1000, 0)

    def lambda_4742():
        OP_6D(32210, 0, 43130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4742)
    OP_8E(0x101, 0x8476, 0x0, 0xA53C, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#501F哎～这房间真不错啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊，感觉的确很好。\x01",
            "东方风格的装饰果然别具一格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F因为麻绪婆婆\x01",
            "是东方出身的嘛。\x02\x03",
            "婆婆还小的时候，\x01",
            "就和家人一起搬来了利贝尔。\x02\x03",
            "这个村子里还有不少\x01",
            "和婆婆一样东方出身的人呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊，\x01",
            "怪不得感觉这里的氛围有点特别。\x02\x03",
            "已经开始期待这里的晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊。\x02\x03",
            "不过，难得老板娘推荐，\x01",
            "吃饭前还是先去泡泡温泉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，对啊！\x02\x03",
            "#001F提妲，\x01",
            "和我一起去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F嗯，好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P放好行李之后，\x01",
            "我们就马上去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49BF():
        OP_8E(0xFE, 0x7C6A, 0x0, 0x9C0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49BF)
    Sleep(100)

    def lambda_49DF():
        OP_8E(0xFE, 0x8070, 0x0, 0x9EAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49DF)
    Sleep(300)

    def lambda_49FF():
        OP_8E(0xFE, 0x8070, 0x0, 0x9EAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_49FF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_46E8 end

    def Function_22_4A31(): pass

    label("Function_22_4A31")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "露天澡堂在这边  ≡\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_4A31 end

    def Function_23_4A74(): pass

    label("Function_23_4A74")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上贴着一张纸条。\x01",
            "『熟睡中，请勿打扰。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_4A74 end

    SaveToFile()

Try(main)
