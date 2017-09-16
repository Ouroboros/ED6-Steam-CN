from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4133   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4133.x',
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
        '士兵',                                 # 9
        '士兵',                                 # 10
        '福立兹',                               # 11
        '乔儿',                                 # 12
        '汉斯',                                 # 13
        '科洛丝',                               # 14
        '科林兹校长',                           # 15
        '克鲁茨',                               # 16
        '卡拉',                                 # 17
        '卢希娅',                               # 18
        '米亚尔',                               # 19
        '帕菲',                                 # 20
        '娜娜',                                 # 21
        '阿鲁姆',                               # 22
        '艾娅莉',                               # 23
        '索菲娜',                               # 24
        '亚妮拉丝',                             # 25
        '信',                                   # 26
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH00100 ._CH',             # 02
        'ED6_DT07/CH00110 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH02390 ._CH',             # 05
        'ED6_DT07/CH02550 ._CH',             # 06
        'ED6_DT07/CH00040 ._CH',             # 07
        'ED6_DT07/CH01040 ._CH',             # 08
        'ED6_DT07/CH02600 ._CH',             # 09
        'ED6_DT07/CH01620 ._CH',             # 0A
        'ED6_DT06/CH20021 ._CH',             # 0B
        'ED6_DT07/CH00015 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01070 ._CH',             # 0E
        'ED6_DT07/CH01043 ._CH',             # 0F
        'ED6_DT07/CH02480 ._CH',             # 10
        'ED6_DT07/CH02490 ._CH',             # 11
        'ED6_DT07/CH01140 ._CH',             # 12
        'ED6_DT07/CH01150 ._CH',             # 13
        'ED6_DT07/CH01690 ._CH',             # 14
        'ED6_DT07/CH01630 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH00100P._CP',             # 02
        'ED6_DT07/CH00110P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH02390P._CP',             # 05
        'ED6_DT07/CH02550P._CP',             # 06
        'ED6_DT07/CH00040P._CP',             # 07
        'ED6_DT07/CH01040P._CP',             # 08
        'ED6_DT07/CH02600P._CP',             # 09
        'ED6_DT07/CH01620P._CP',             # 0A
        'ED6_DT06/CH20021P._CP',             # 0B
        'ED6_DT07/CH00015P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01070P._CP',             # 0E
        'ED6_DT07/CH01043P._CP',             # 0F
        'ED6_DT07/CH02480P._CP',             # 10
        'ED6_DT07/CH02490P._CP',             # 11
        'ED6_DT07/CH01140P._CP',             # 12
        'ED6_DT07/CH01150P._CP',             # 13
        'ED6_DT07/CH01690P._CP',             # 14
        'ED6_DT07/CH01630P._CP',             # 15
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 7410,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3020,
        Z                   = 0,
        Y                   = 1290,
        Direction           = 119,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 3390,
        Z                   = 0,
        Y                   = -390,
        Direction           = 36,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4740,
        Z                   = 0,
        Y                   = 960,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4970,
        Z                   = 0,
        Y                   = -600,
        Direction           = 309,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 36400,
        Z                   = 0,
        Y                   = 111030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 100960,
        Z                   = 0,
        Y                   = 113420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 97040,
        Z                   = 0,
        Y                   = 114630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 157590,
        Z                   = 250,
        Y                   = 55130,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -26610,
        Z                   = 0,
        Y                   = 55500,
        Direction           = 290,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -27940,
        Z                   = 0,
        Y                   = 55480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 155000,
        Z                   = 0,
        Y                   = 114600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 158680,
        Z                   = 0,
        Y                   = 110910,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 35100,
        Z                   = 0,
        Y                   = 53750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 93210,
        Z                   = 0,
        Y                   = 53470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -24660,
        Z                   = -200,
        Y                   = 175270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1114123,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 57010,
        TriggerZ            = 0,
        TriggerY            = 3770,
        TriggerRange        = 800,
        ActorX              = 57010,
        ActorZ              = 1000,
        ActorY              = 3770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7200,
        TriggerZ            = 0,
        TriggerY            = 1690,
        TriggerRange        = 800,
        ActorX              = 7410,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_406",          # 00, 0
        "Function_1_5A8",          # 01, 1
        "Function_2_5EB",          # 02, 2
        "Function_3_601",          # 03, 3
        "Function_4_625",          # 04, 4
        "Function_5_678",          # 05, 5
        "Function_6_99A",          # 06, 6
        "Function_7_C97",          # 07, 7
        "Function_8_DE8",          # 08, 8
        "Function_9_DED",          # 09, 9
        "Function_10_1979",        # 0A, 10
        "Function_11_1E85",        # 0B, 11
        "Function_12_1EC0",        # 0C, 12
        "Function_13_1EEE",        # 0D, 13
        "Function_14_2027",        # 0E, 14
        "Function_15_20DA",        # 0F, 15
        "Function_16_2197",        # 10, 16
        "Function_17_2287",        # 11, 17
        "Function_18_2368",        # 12, 18
        "Function_19_24B2",        # 13, 19
        "Function_20_2534",        # 14, 20
        "Function_21_293F",        # 15, 21
        "Function_22_2FCD",        # 16, 22
        "Function_23_3D43",        # 17, 23
        "Function_24_4954",        # 18, 24
        "Function_25_55AC",        # 19, 25
        "Function_26_58C4",        # 1A, 26
    )


    def Function_0_406(): pass

    label("Function_0_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_414")
    OP_A3(0x3FA)
    Event(0, 20)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_427")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 21)

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_43A")
    SetMapFlags(0x10000000)
    OP_A3(0x3FC)
    Event(0, 24)

    label("loc_43A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (122, "loc_446"),
        (SWITCH_DEFAULT, "loc_459"),
    )


    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_456")
    Event(0, 23)

    label("loc_456")

    Jump("loc_459")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_477")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_5A7")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_486")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5A7")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_490")
    Jump("loc_5A7")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_49A")
    Jump("loc_5A7")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_5A7")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_502")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 34910, 0, 113190, 0)
    OP_43(0xF, 0x0, 0x0, 0x2)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_5A7")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 154870, 0, 51420, 339)
    OP_43(0xF, 0x0, 0x0, 0x3)
    Jump("loc_5A7")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_533")
    Jump("loc_5A7")

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_55A")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 154870, 0, 51420, 339)
    OP_43(0xF, 0x0, 0x0, 0x3)
    Jump("loc_5A7")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_58C")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5A7")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_596")
    Jump("loc_5A7")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5A0")
    Jump("loc_5A7")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5A7")

    label("loc_5A7")

    Return()

    # Function_0_406 end

    def Function_1_5A8(): pass

    label("Function_1_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BC")
    OP_1B(0x0, 0x0, 0x19)
    Jump("loc_5CD")

    label("loc_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CD")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E6")
    OP_72(0x12, 0x10)
    Jump("loc_5EA")

    label("loc_5E6")

    OP_64(0x0, 0x1)

    label("loc_5EA")

    Return()

    # Function_1_5A8 end

    def Function_2_5EB(): pass

    label("Function_2_5EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_600")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5EB")

    label("loc_600")

    Return()

    # Function_2_5EB end

    def Function_3_601(): pass

    label("Function_3_601")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_624")
    OP_8D(0xFE, 153520, 48510, 156020, 53700, 3000)
    Jump("Function_3_601")

    label("loc_624")

    Return()

    # Function_3_601 end

    def Function_4_625(): pass

    label("Function_4_625")

    TalkBegin(0xFE)

    ChrTalk(
        0xE,
        (
            "#780F我和学院的学生代表乔儿还有汉斯一起\x01",
            "来参加诞辰庆典了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_625 end

    def Function_5_678(): pass

    label("Function_5_678")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6BF")

    ChrTalk(
        0x105,
        (
            "#040F艾丝蒂尔、约修亚。\x02\x03",
            "能够遇到你们两个，\x01",
            "我真是太幸福了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_996")

    label("loc_6BF")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "#040F艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F科洛丝，原来你在这里啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040F啊，\x01",
            "我听说校长、乔儿和汉斯他们都来这里了……\x01",
            "　\x02\x03",
            "所以就从王城里面偷偷跑了出来。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈，真看不出来，\x01",
            "科洛丝你也会做出这么大胆的行动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#040F呵呵，这次真是多谢你们了。\x01",
            "　\x02\x03",
            "我从头到尾一直都承蒙你们两位的关照。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～\x01",
            "我觉得倒是科洛丝你教会了我许多东西。\x02\x03",
            "待人温柔，意志坚强……\x01",
            "　\x02\x03",
            "对不起，我不太会说话，\x01",
            "所以说不出什么好的……\x02\x03",
            "总之，我们以后继续像现在这样\x01",
            "互相帮助、一起努力就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#040F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_996")

    TalkEnd(0xFE)
    Return()

    # Function_5_678 end

    def Function_6_99A(): pass

    label("Function_6_99A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A4C")

    ChrTalk(
        0xFE,
        (
            "#730F虽然发生了许多的事情，\x01",
            "不过看到你这么有精神，我就放心了。\x02\x03",
            "如果再到卢安来的话，\x01",
            "记得到学院来玩玩哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_A4C")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "#730F哟，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这不是汉斯吗。\x01",
            "你在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#730F在这里做什么……\x01",
            "这么久没见面了，\x01",
            "你却说出这样绝情的话来。\x02\x03",
            "自从学园祭之后，\x01",
            "又回到独自过夜的生活真是寂寞啊……\x02\x03",
            "因为对你难以忘怀，\x01",
            "所以千里迢迢追到王都来了哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哈哈，你还是老样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#730F嗯，虽然发生了许多的事情，\x01",
            "不过看到你这么有精神，我就放心了。\x02\x03",
            "如果再到卢安来的话，\x01",
            "记得到学院来玩玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    TalkEnd(0xFE)
    Return()

    # Function_6_99A end

    def Function_7_C97(): pass

    label("Function_7_C97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D19")

    ChrTalk(
        0xFE,
        (
            "#640F我从科洛丝那里听说了，\x01",
            "你们这次真是大显神威啊。\x02\x03",
            "不愧是红骑士尤利乌斯哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE4")

    label("loc_D19")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "#640F艾丝蒂尔、约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，乔儿！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#640F好久不见了啦～\x02\x03",
            "我从科洛丝那里听说了，\x01",
            "你们这次真是大显神威啊。\x02\x03",
            "不愧是红骑士尤利乌斯哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_DE4")

    TalkEnd(0xFE)
    Return()

    # Function_7_C97 end

    def Function_8_DE8(): pass

    label("Function_8_DE8")

    Call(0, 9)
    Return()

    # Function_8_DE8 end

    def Function_9_DED(): pass

    label("Function_9_DED")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_ECD")

    ChrTalk(
        0xA,
        (
            "不愧是诞辰庆典啊，\x01",
            "比武术大会还要热闹许多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "从外国来的客人\x01",
            "也比历年的要多很多，\x01",
            "真是快忙不过来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(
        0xA,
        (
            "真是奇怪，\x01",
            "这个时间王城的城门却紧闭着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_101C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FA1")

    ChrTalk(
        0xA,
        (
            "刚才游击士\x01",
            "克鲁茨先生回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但他的脸色\x01",
            "似乎不是很好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1019")

    label("loc_FA1")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "刚才游击士\x01",
            "克鲁茨先生回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但他的脸色\x01",
            "似乎不是很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "应该没事吧……\x02",
    )

    CloseMessageWindow()

    label("loc_1019")

    Jump("loc_1975")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10AB")

    ChrTalk(
        0xA,
        (
            "恭喜你们二人取得\x01",
            "这次武术大会的优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们就不用在意\x01",
            "这边的安排了。\x01",
            "请好好享受王城的晚宴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1244")

    label("loc_10AB")

    OP_A2(0x2)

    ChrTalk(
        0x101,
        "#000F啊，福立兹先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦，艾丝蒂尔小姐，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F今天晚上我们准备住在别的地方了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯，\x01",
            "之前艾南先生已经告知我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "恭喜你们取得\x01",
            "武术大会的优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不用在意这边的安排，\x01",
            "请好好享受王城的晚宴吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不愧是艾南先生啊，\x01",
            "动作这么快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1244")

    Jump("loc_1975")

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1311")

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔小姐，约修亚先生，\x01",
            "今天是武术大会的决赛吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请两位比赛\x01",
            "一定要加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我会在这里默默支持你们的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(
        0xA,
        (
            "外面有很多的士兵\x01",
            "在到处巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "刚才外出的客人\x01",
            "都被他们以禁止夜间外出的理由\x01",
            "强行送了回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_153B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1463")

    ChrTalk(
        0xA,
        (
            "听说从今天起\x01",
            "士兵就要严加巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然给你们带来种种不便，\x01",
            "但是请不要在外面待得太晚，\x01",
            "一定要早点回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_1463")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "刚才收到了\x01",
            "王国军发来的联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "听说从今天起\x01",
            "他们就要严加巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然给你们带来种种不便，\x01",
            "但是请不要在外面待得太晚，\x01",
            "一定要早点回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1538")

    Jump("loc_1975")

    label("loc_153B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_157F")

    ChrTalk(
        0xA,
        "出去的时候请务必小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1603")

    ChrTalk(
        0xA,
        (
            "对了，\x01",
            "还有另外两位游击士\x01",
            "现在也住在酒店里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们见到他们了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_16AD")

    label("loc_1603")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔小姐，约修亚先生，\x01",
            "欢迎你们回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对了，\x01",
            "还有另外两位游击士\x01",
            "现在也住在酒店里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们见到他们了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_16AD")

    Jump("loc_1975")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_16DB")

    ChrTalk(
        0xA,
        (
            "两位打算外出吗？\x01",
            "出去的时候请务必小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1975")

    label("loc_16DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_18CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1770")

    ChrTalk(
        0xA,
        (
            "两位的房间\x01",
            "在楼上走廊尽头的\x01",
            "２０２号室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果有什么需要的话，\x01",
            "请来前台告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C8")

    label("loc_1770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17E4")

    ChrTalk(
        0xA,
        (
            "尊敬的客人，非常抱歉。\x01",
            "现在还不能为你们安排房间，\x01",
            "因为房间还没有清扫完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想要在这里登记住宿的话，\x01",
            "请三点以后再来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C8")

    label("loc_17E4")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "尊敬的客人，非常抱歉。\x01",
            "现在还不能为你们安排房间，\x01",
            "因为房间还没有清扫完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想要在这里登记住宿的话，\x01",
            "请三点以后再来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F待会儿来登记吧，\x01",
            "还是先去找到金先生再说。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FＯＫ。\x02",
    )

    CloseMessageWindow()

    label("loc_18C8")

    Jump("loc_1975")

    label("loc_18CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1975")

    ChrTalk(
        0xA,
        (
            "有许多客人\x01",
            "都是从很远的地方\x01",
            "赶来参加武术大会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我们也非常欢迎\x01",
            "参加大会的选手\x01",
            "前来光顾我们的酒店呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1975")

    TalkEnd(0xA)
    Return()

    # Function_9_DED end

    def Function_10_1979(): pass

    label("Function_10_1979")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1986")
    Jump("loc_1E81")

    label("loc_1986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1990")
    Jump("loc_1E81")

    label("loc_1990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_199A")
    Jump("loc_1E81")

    label("loc_199A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19A4")
    Jump("loc_1E81")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_19AE")
    Jump("loc_1E81")

    label("loc_19AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_END)), "loc_1A0E")

    ChrTalk(
        0xFE,
        (
            "#842F是错觉吗……？\x02\x03",
            "刚才好像感觉到窗户外面\x01",
            "有什么东西横着飞过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E81")

    label("loc_1A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_1AA8")

    ChrTalk(
        0xFE,
        (
            "#840F为明天的比赛做好准备，\x01",
            "你们今天就早点休息吧。\x02\x03",
            "『有备而无患』，\x01",
            "将身体状态调整好，\x01",
            "这对于游击士来说很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E81")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B40")

    ChrTalk(
        0xFE,
        (
            "『不动金』自不用说，\x01",
            "你们的战斗也十分出色。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C36")

    label("loc_1B40")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『不动金』自不用说，\x01",
            "你们的战斗也十分出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每个人的技术都不错，\x01",
            "配合也相当熟练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们的将来无可限量呀。\x02",
    )

    CloseMessageWindow()

    label("loc_1C36")

    Jump("loc_1E81")

    label("loc_1C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C43")
    Jump("loc_1E81")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D2D")

    ChrTalk(
        0xFE,
        (
            "今天我们都能顺利晋级，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样我们的下一个对手\x01",
            "说不定就是你们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E63")

    label("loc_1D2D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哟，这不是艾丝蒂尔和约修亚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天我们都能顺利晋级，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然之前也听卡露娜说过，\x01",
            "不过这次是亲眼见到你们的实力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样我们的下一个对手\x01",
            "说不定就是你们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E63")

    Jump("loc_1E81")

    label("loc_1E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1E70")
    Jump("loc_1E81")

    label("loc_1E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1E7A")
    Jump("loc_1E81")

    label("loc_1E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1E81")

    label("loc_1E81")

    TalkEnd(0xFE)
    Return()

    # Function_10_1979 end

    def Function_11_1E85(): pass

    label("Function_11_1E85")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "这家宾馆真是华丽。\x01",
            "如果把丈夫也一道带来就好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1E85 end

    def Function_12_1EC0(): pass

    label("Function_12_1EC0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哇～沙发好软呀～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1EC0 end

    def Function_13_1EEE(): pass

    label("Function_13_1EEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_1F8E")

    ChrTalk(
        0xFE,
        (
            "为了明天有充足的精力看比赛，\x01",
            "今天就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要好好泡个热水澡\x01",
            "让疲劳一扫而光。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2023")

    label("loc_1F8E")


    ChrTalk(
        0xFE,
        (
            "哎呀～虽然明天才开始正式比赛，\x01",
            "不过今天的比赛就很精彩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "光是喊加油就已经精疲力尽了。\x02",
    )

    CloseMessageWindow()

    label("loc_2023")

    TalkEnd(0xFE)
    Return()

    # Function_13_1EEE end

    def Function_14_2027(): pass

    label("Function_14_2027")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2089")

    ChrTalk(
        0xFE,
        "和同住一条街上的人交往～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要是分手了，以后见面难道不尴尬吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D6")

    label("loc_2089")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我说老姐啊～\x01",
            "你是不是跟男友分手了啊～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D6")

    TalkEnd(0xFE)
    Return()

    # Function_14_2027 end

    def Function_15_20DA(): pass

    label("Function_15_20DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2127")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "啊～那当然尴尬死了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定不想碰面的～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2193")

    label("loc_2127")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "真的～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这样不是正好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他也只不过是个\x01",
            "没什么钱的男人啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2193")

    TalkEnd(0xFE)
    Return()

    # Function_15_20DA end

    def Function_16_2197(): pass

    label("Function_16_2197")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(
        0xFE,
        (
            "本打算和她共赏\x01",
            "王都美丽的夜景呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但从今天起夜间禁止外出。\x01",
            "啊啊，好想去啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2283")

    label("loc_2238")


    ChrTalk(
        0xFE,
        "一会儿我们打算出去看夜景。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "夜幕就要降临了。\x02",
    )

    CloseMessageWindow()

    label("loc_2283")

    TalkEnd(0xFE)
    Return()

    # Function_16_2197 end

    def Function_17_2287(): pass

    label("Function_17_2287")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0xFE,
        (
            "偶尔像这样\x01",
            "放松一下也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只要和他在一起，我就感到非常幸福了㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_2303")


    ChrTalk(
        0xFE,
        (
            "呵呵，能和他一起游览夜色中的王都，\x01",
            "我的心都激动得扑嗵扑嗵在跳了㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    TalkEnd(0xFE)
    Return()

    # Function_17_2287 end

    def Function_18_2368(): pass

    label("Function_18_2368")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_END)), "loc_23F5")

    ChrTalk(
        0xFE,
        "今天街上感觉好安静啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天就是决赛了，\x01",
            "本以为会热闹一点的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24AE")

    label("loc_23F5")


    ChrTalk(
        0xFE,
        (
            "虽然第一次在这里过夜，\x01",
            "但是房间真的很豪华啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我的哥哥\x01",
            "并不太喜欢这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "反而觉得豪华的地方不安稳。\x02",
    )

    CloseMessageWindow()

    label("loc_24AE")

    TalkEnd(0xFE)
    Return()

    # Function_18_2368 end

    def Function_19_24B2(): pass

    label("Function_19_24B2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#811F呀～两位游击士新人。\x02\x03",
            "嘻嘻，\x01",
            "我现在想去冲个澡呢。\x02\x03",
            "#851F今天也是出了一身汗，\x01",
            "好想痛快地洗个澡哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_24B2 end

    def Function_20_2534(): pass

    label("Function_20_2534")

    EventBegin(0x0)
    OP_6D(7350, 0, -5650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6930, 0, 1460, 0)
    SetChrPos(0x102, 7840, 0, 1460, 0)
    OP_4A(0xA, 255)
    FadeToBright(1500, 0)
    OP_6D(7010, 0, 2460, 4000)

    ChrTalk(
        0xA,
        (
            "晚上好。\x01",
            "欢迎光临罗恩鲍姆酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请问二位客人，\x01",
            "你们是要住店的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F是的，我们是游击士协会的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F听说我们两个的房间已经订好了，\x01",
            "请问能不能确认一下呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦哦……\x01",
            "原来是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "没错，确实有这回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F呼～太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F多亏了艾南先生呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "是艾丝蒂尔小姐和约修亚先生吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然很失礼，\x01",
            "不过请让我看一下游击士手册好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，请等一下……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把游击士手册展示给前台接待看。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        "……好，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么，\x01",
            "请拿好这个。\x02",
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
            "得到了\x07\x02",
            "２０２号室的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x375, 1)

    ChrTalk(
        0xA,
        (
            "上楼梯到二楼，\x01",
            "左边最里面的房间就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果有什么事情，\x01",
            "随时到前台这里来找我即可。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x616)
    OP_A2(0x617)
    OP_1B(0x0, 0x0, 0x19)
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_20_2534 end

    def Function_21_293F(): pass

    label("Function_21_293F")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(6980, 0, -3210, 0)
    OP_67(0, 8310, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(337000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6760, 0, -3090, 180)
    SetChrPos(0x102, 7760, 0, -3080, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 6510, -250, -4770, 0)
    SetChrPos(0x9, 7820, -250, -4970, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#008F那个……\x01",
            "真是太感谢你们特地送我们回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F谢谢你们的照顾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没什么，\x01",
            "我们也是你们的支持者啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然同样身为王国军的成员，\x01",
            "但有些事情实在不吐不快……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为我实在不喜欢\x01",
            "特务部队的那些家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊是啊，\x01",
            "也不知道他们天天在想些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦哦……\x01",
            "这样说对理查德上校有点失礼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那就这样吧，\x01",
            "期待着你们的精彩表演。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "明天的比赛，要加油哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊哈哈……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会全力以赴的。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x8, 180, 400)

    def lambda_2C5C():
        OP_8E(0xFE, 0x196E, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C5C)
    OP_8C(0x9, 180, 400)

    def lambda_2C7E():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C7E)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_2CA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2CA3)

    def lambda_2CB5():
        OP_8E(0xFE, 0x196E, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2CB5)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x4)

    def lambda_2CDA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2CDA)

    def lambda_2CEC():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2CEC)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼……真是复杂啊。\x02\x03",
            "看来，那些士兵好像\x01",
            "完全不知道理查德上校的阴谋呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F那也是啊……\x01",
            "他们只不过是普通的士兵而已。\x02\x03",
            "从上级传来的情报和命令，\x01",
            "他们能做到的也只有相信和服从。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x02\x03",
            "他们还支持我们呢，\x01",
            "真是不想和他们敌对啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不管怎么说，\x01",
            "不要让一般士兵卷进事件来就好了。\x02\x03",
            "今天晚上就别再出去了，\x01",
            "在房间里好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，ＯＫ。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 7090, 0, -2590, 0)
    SetChrPos(0x102, 7090, 0, -2590, 0)
    OP_6D(7090, 0, -2590, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_A2(0x629)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_1B(0x0, 0x0, 0x19)
    EventEnd(0x0)
    Return()

    # Function_21_293F end

    def Function_22_2FCD(): pass

    label("Function_22_2FCD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7D")
    OP_A2(0x618)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3015")

    ChrTalk(
        0x101,
        (
            "#006F２０２号室……\x01",
            "这就是我们的房间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3043")

    label("loc_3015")


    ChrTalk(
        0x102,
        (
            "#010F２０２号室……\x01",
            "嗯，就是这里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3043")

    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 34420, 0, 108910, 0)
    SetChrPos(0x102, 35770, 0, 108690, 0)
    OP_6D(34410, 0, 115500, 0)
    OP_67(0, 5930, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(315000, 0)
    OP_6E(437, 0)
    OP_22(0x6, 0x0, 0x64)
    OP_6D(35020, 0, 111190, 2000)

    ChrTalk(
        0x101,
        (
            "#004F哇……\x01",
            "这间屋子气氛很不错啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30E5():
        OP_6D(31860, 0, 115500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30E5)

    def lambda_30FD():
        OP_8E(0xFE, 0x8674, 0x0, 0x1B972, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30FD)
    Sleep(600)

    def lambda_311D():
        OP_8E(0xFE, 0x8BBA, 0x0, 0x1B9C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_311D)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3154():
        OP_8E(0xFE, 0x7B8E, 0x0, 0x1C32C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3154)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#001F快看快看，\x01",
            "从这边可以看到竞技场的夜景呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31BE():
        OP_6D(31160, 0, 115440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31BE)

    def lambda_31D6():
        OP_6B(1700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31D6)

    def lambda_31E6():
        OP_6C(306000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31E6)

    def lambda_31F6():

        label("loc_31F6")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_31F6")

    QueueWorkItem2(0x101, 1, lambda_31F6)
    OP_8E(0x102, 0x7EF4, 0x0, 0x1C32C, 0xFA0, 0x0)
    OP_8C(0x102, 0, 400)

    def lambda_3222():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3222)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        (
            "#014F哎……真的啊。\x02\x03",
            "#019F在这里只是过夜的话，\x01",
            "感觉还真是有点浪费了呢。\x02\x03",
            "就把这里作为我们\x01",
            "在武术大会结束之前的根据地吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#1P（……要在这里\x01",
            "　和约修亚一起度过一段时间啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#504F#3S#1P（哎呀，我在想什么呀～！？）\x01",
            "　\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x102,
        "#013F我说，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(200)
    TurnDirection(0x101, 0x102, 800)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0xFA0, 0x0)

    ChrTalk(
        0x101,
        "#008F#1P#3S呀！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F突然说这样的话可能你会觉得奇怪……\x01",
            "　\x02\x03",
            "#010F嗯，我们是亲人……对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P……哎………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F虽然我可能不像父亲那样值得信赖……\x01",
            "　\x02\x03",
            "也可能不像雪拉姐姐那样\x01",
            "耐心地听别人说话……\x02\x03",
            "#010F不过我觉得作为家人，\x01",
            "我一定要成为能够支持你的人。\x02\x03",
            "所以，你有什么烦恼的话，\x01",
            "随时可以和我说说哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P………啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F因为最近，\x01",
            "你的样子好像有点奇怪……\x02\x03",
            "#013F嗯，如果我弄错了的话，抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#1P哈啊……\x01",
            "真不愧是约修亚啊。\x02\x03",
            "还是那样的敏锐，\x01",
            "不过却搞错重点啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哎……？\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F#1P谢谢，约修亚。\x01",
            "不过你不用那样担心。\x02\x03",
            "#007F确实……\x01",
            "我最近可能有点怪怪的……\x02\x03",
            "劳累、痛苦什么的，\x01",
            "也不是什么大事啦……\x02\x03",
            "只是自己的心情有些整理不清而已……\x01",
            "　\x02\x03",
            "#006F所以……没关系的。\x02\x03",
            "你只要在一旁看着我，就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F是吗……\x02\x03",
            "#010F嗯，那么我也不做多余的担心了。\x01",
            "　\x02\x03",
            "不过，如果解决了烦恼就来告诉我，\x01",
            "我一样会替你感到高兴的。\x02\x03",
            "#014F啊，不是强迫你说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#1P哎，嗯……\x02\x03",
            "嗯……如果整理好心情的话，\x01",
            "说不定会更加说不出口呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#1P没、没什么啦！\x02\x03",
            "#006F虽然还有点早……\x01",
            "不过现在就休息吧？\x02\x03",
            "今天发生了很多事，有点累了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，明天还有比赛……\x01",
            "　\x02\x03",
            "整理完行李就休息吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_3A7D")

    OP_20(0x5DC)
    Fade(1000)
    SetChrPos(0x102, 56580, 0, 2320, 0)
    SetChrPos(0x101, 57920, 0, 2070, 0)
    OP_6D(56650, 0, 3000, 0)
    OP_0D()
    OP_22(0x82, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x32)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F哎……\x02\x03",
            "刚才是不是有什么声音？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_1D(0x51)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#015F（进入房间的同时保持临战状态，\x01",
            "　然后确认里面的状况。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（哎……！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（大概是入侵者。）\x02\x03",
            "（有可能设置了爆炸陷阱，\x01",
            "　所以一定要万分小心。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#580F（等、等一下……不是开玩笑的吧？）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F（拜托了，照我说的去做……）\x02\x03",
            "（如果有什么问题的话，\x01",
            "　你在这里等着也可以。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F（开、开玩笑！）\x02\x03",
            "（我已经做好准备了，\x01",
            "　总之赶快进去看看吧！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F（……好吧。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x62A)
    OP_64(0x0, 0x1)
    OP_71(0x12, 0x10)
    OP_1C(0x12, 0x0, 0xFFFF)
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 23)
    Return()

    # Function_22_2FCD end

    def Function_23_3D43(): pass

    label("Function_23_3D43")

    EventBegin(0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -24300, -200, 175600, 0)
    OP_6D(-25590, 0, 170160, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(325000, 0)
    OP_6E(478, 0)
    SetChrPos(0x101, -23950, 0, 168970, 0)
    SetChrPos(0x102, -25320, 0, 168830, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    FadeToDark(0, 0, -1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_6D(-25590, 0, 172760, 1000)

    ChrTalk(
        0x101,
        "#004F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#5P好像逃跑了。\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#013F#5P不过，奇怪了……\x01",
            "感觉好像没有人来过啊……\x02\x03",
            "陷阱什么的……\x01",
            "好像也没有设置过的迹象。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#5P连、连这些你也能看出来吗？\x02",
    )

    CloseMessageWindow()

    def lambda_3F1B():

        label("loc_3F1B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_3F1B")

    QueueWorkItem2(0x101, 2, lambda_3F1B)

    def lambda_3F2C():
        OP_6D(-24940, 0, 175710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F2C)

    def lambda_3F44():
        OP_8E(0xFE, 0xFFFFA088, 0x0, 0x2AB66, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F44)
    Sleep(800)

    def lambda_3F64():
        OP_8E(0xFE, 0xFFFF9FA2, 0x0, 0x2A634, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F64)
    WaitChrThread(0x102, 0x2)

    def lambda_3F84():

        label("loc_3F84")

        OP_8C(0xFE, 0, 0)
        OP_48()
        Jump("loc_3F84")

    QueueWorkItem2(0x102, 1, lambda_3F84)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    Fade(500)
    SetChrChipByIndex(0x102, 12)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#015F#5P……看起来，\x01",
            "好像只是给我们送来了礼物呢。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#505F那个是……信？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    Fade(500)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚打开信封。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F#5P『——今天晚上１０点，\x01",
            "　请到大圣堂来。』\x02\x03",
            "『另外请不要告诉别人。』\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F#6P……只有这些？\x02\x03",
            "#505F大圣堂……\x01",
            "指的是西街区那个大教会吧？\x02\x03",
            "今天晚上１０点，\x01",
            "马上就要到了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P嗯，虽然可疑的地方太多了，\x01",
            "不过人不是常说『不入虎穴焉得虎子』……\x02\x03",
            "#006F喂，约修亚。\x01",
            "我们真的要应邀过去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F#3S#5P……不行！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F#6P怎、怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#2P不好意思，突然这么大声……\x02\x03",
            "#010F对了，刚才那些士兵不是说过\x01",
            "他们要强化夜间的巡逻吗？\x01",
            "　\x02\x03",
            "这里离西街区很远，\x01",
            "被发现和盘问的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6P啊，忘记了。\x02\x03",
            "#007F嗯～不过如果就这样放着不管，\x01",
            "又会让人觉得十分在意呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2P所以，我一个人去就行了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P这种情况下，\x01",
            "一个人行动要比起两个人保险很多。\x02\x03",
            "这样就能绕过士兵安全到达大圣堂了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P只是去确认一下情况而已，\x01",
            "所以我一个人去就够了。\x02\x03",
            "所以你在这里等着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#3S#6P我说……\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#6P我可是游击士哦。\x02\x03",
            "能自己够照顾自己，\x01",
            "而且我也有自信不会拖你的后腿。\x02\x03",
            "你就算再怎么花言巧语，\x01",
            "也糊弄不过我的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P艾丝蒂尔，我不是打算这样……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#500F#6P我知道，你不是不相信我。\x01",
            "　\x02\x03",
            "说是担心……\x01",
            "大概，也不只是因为这个吧……\x02\x03",
            "#006F你是不是已经知道了什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P………………………………\x02\x03",
            "我的话语已经没什么破绽了，\x01",
            "为什么你连这个也能觉察到？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6P这个……\x01",
            "因为我是观察约修亚的第一人嘛。\x02\x03",
            "不管怎么说，我都会知道啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P………………………………\x02\x03",
            "#015F（……到此为止…吗…………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P知道了，我不会阻止你了。\x02\x03",
            "已经到指定的时间了，\x01",
            "我们赶快去大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#6P啊……嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P不过……\x01",
            "我要你事先做好约定。\x02\x03",
            "如果发生什么事情，\x01",
            "一定要照我的指示去做。\x02\x03",
            "一瞬间的判断失误，\x01",
            "说不定就会丧命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6P嗯……我知道了。\x02\x03",
            "#006F那么我们赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    Fade(1500)
    SetChrPos(0x101, -24630, 0, 173630, 180)
    SetChrPos(0x102, -24630, 0, 173630, 180)
    OP_6D(-24630, 0, 173630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_28(0x48, 0x1, 0x100)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_A2(0x62B)
    Sleep(500)
    EventEnd(0x0)
    OP_1D(0x54)
    Return()

    # Function_23_3D43 end

    def Function_24_4954(): pass

    label("Function_24_4954")

    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F14")
    EventBegin(0x0)
    OP_6D(6980, 0, -3210, 0)
    OP_67(0, 8310, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(337000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6760, 0, -3090, 180)
    SetChrPos(0x102, 7760, 0, -3080, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 6510, -250, -4770, 0)
    SetChrPos(0x9, 7820, -250, -4970, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0D")
    OP_28(0x48, 0x1, 0x800)
    Jump("loc_4A5E")

    label("loc_4A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A22")
    OP_28(0x48, 0x1, 0x1000)
    Jump("loc_4A5E")

    label("loc_4A22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A37")
    OP_28(0x48, 0x1, 0x2000)
    Jump("loc_4A5E")

    label("loc_4A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4C")
    OP_28(0x48, 0x1, 0x4000)
    Jump("loc_4A5E")

    label("loc_4A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5E")
    OP_28(0x48, 0x1, 0x8000)

    label("loc_4A5E")


    ChrTalk(
        0x8,
        "真是会给人添麻烦啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "为了防范恐怖分子，\x01",
            "任何市民一律禁止夜间外出。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x8, 180, 400)

    def lambda_4AF2():
        OP_8E(0xFE, 0x196E, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AF2)
    OP_8C(0x9, 180, 400)

    def lambda_4B14():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFE0C, 0xFFFFE2D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B14)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_4B39():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4B39)

    def lambda_4B4B():
        OP_8E(0xFE, 0x196E, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4B4B)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x4)

    def lambda_4B70():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4B70)

    def lambda_4B82():
        OP_8E(0xFE, 0x1E8C, 0xFFFFFF06, 0xFFFFDCD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4B82)
    Sleep(2000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F哎呀……\x01",
            "被送回来了呢。\x02\x03",
            "只好再试一次了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F刚才我就注意到了……\x02\x03",
            "那些监视着某个固定地方的士兵，\x01",
            "我们最好不要靠近他们。\x02\x03",
            "为了保证不让他们发现，\x01",
            "我们只好绕个远路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F原来如此……\x01",
            "直接往大圣堂所在的\x01",
            "西街区走确实比较困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还有，那些巡逻的士兵……\x02\x03",
            "因为晚上视野不好，\x01",
            "只要不太靠近或是站在他们前面，\x01",
            "也应该不会被发现。\x02\x03",
            "另外，他们各自的巡逻路线\x01",
            "好像是事先安排好的，\x01",
            "稍微注意一下就可以看出规律来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F明白了……\x01",
            "那么我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x101, 7090, 0, -2590, 0)
    SetChrPos(0x102, 7090, 0, -2590, 0)
    OP_6D(7090, 0, -2590, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_A2(0x62D)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EventEnd(0x0)
    Jump("loc_55AB")

    label("loc_4F14")

    EventBegin(0x0)
    OP_6D(7010, 0, -2900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6760, 0, -3090, 180)
    SetChrPos(0x102, 7760, 0, -3080, 180)
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0x102, 0x101, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517F")
    OP_28(0x48, 0x1, 0x800)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5095")

    ChrTalk(
        0x102,
        (
            "#012F那些监视着某个固定地方的士兵，\x01",
            "我们最好不要靠近他们。\x02\x03",
            "为了保证不让他们发现，\x01",
            "我们只好绕个远路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_517C")

    label("loc_5095")


    ChrTalk(
        0x102,
        (
            "#012F因为晚上视野不好，\x01",
            "只要不太靠近或是站在他们前面，\x01",
            "也应该不会被发现。\x02\x03",
            "另外，他们各自的巡逻路线\x01",
            "好像是事先安排好的，\x01",
            "稍微注意一下就可以看出规律来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517C")

    Jump("loc_55A9")

    label("loc_517F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5371")
    OP_28(0x48, 0x1, 0x1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5287")

    ChrTalk(
        0x102,
        (
            "#012F那些监视着某个固定地方的士兵，\x01",
            "我们最好不要靠近他们。\x02\x03",
            "为了保证不让他们发现，\x01",
            "我们只好绕个远路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536E")

    label("loc_5287")


    ChrTalk(
        0x102,
        (
            "#012F因为晚上视野不好，\x01",
            "只要不太靠近或是站在他们前面，\x01",
            "也应该不会被发现。\x02\x03",
            "另外，他们各自的巡逻路线\x01",
            "好像是事先安排好的，\x01",
            "稍微注意一下就可以看出规律来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536E")

    Jump("loc_55A9")

    label("loc_5371")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E8")
    OP_28(0x48, 0x1, 0x2000)

    ChrTalk(
        0x102,
        (
            "#015F士兵好像减少了一些，\x01",
            "别放松警惕，走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_53E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5480")
    OP_28(0x48, 0x1, 0x4000)

    ChrTalk(
        0x102,
        (
            "#010F大部分士兵好像都回去了呢。\x02\x03",
            "大概是夜间的巡逻快要结束了吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_5480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F8")
    OP_28(0x48, 0x1, 0x8000)

    ChrTalk(
        0x102,
        (
            "#010F酒店前面的士兵也走掉了，\x01",
            "很容易就能到南街区了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A9")

    label("loc_54F8")


    ChrTalk(
        0x102,
        (
            "#010F士兵基本上都撤走了。\x02\x03",
            "沿着大道到南街区，\x01",
            "然后就直接到西街区的大圣堂去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A9")

    EventEnd(0x0)

    label("loc_55AB")

    Return()

    # Function_24_4954 end

    def Function_25_55AC(): pass

    label("Function_25_55AC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 0)), scpexpr(EXPR_END)), "loc_574A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569C")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F今晚就回房间休息吧。\x02\x03",
            "再随便外出的话\x01",
            "被士兵碰上就不好办了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，说的也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5747")

    label("loc_569C")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F今晚就回房间休息吧。\x02\x03",
            "再随便外出的话\x01",
            "被士兵碰上就不好办了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5747")

    Jump("loc_58A8")

    label("loc_574A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5817")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "还是不要到外面去了。\x02\x03",
            "明天还有比赛呢。\x01",
            "最好充分地休息一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，说的也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_58A8")

    label("loc_5817")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "还是不要到外面去了。\x02\x03",
            "而且明天还有比赛呢。\x01",
            "最好充分地休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_55AC end

    def Function_26_58C4(): pass

    label("Function_26_58C4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　　事务室　　　　　　　\x01",
            "※工作人员以外禁止进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_58C4 end

    SaveToFile()

Try(main)
