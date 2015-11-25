from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1410   ._SN',
        MapName             = 'Bose',
        Location            = 'T1410.x',
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
        '诺朗',                                 # 9
        '艾蕾米亚',                             # 10
        '马尔科',                               # 11
        '金发青年',                             # 12
        '卫兵',                                 # 13
        '王国军士兵',                           # 14
        '王国军士兵',                           # 15
        '摩尔根将军',                           # 16
        '梅贝尔市长',                           # 17
        '斯丁克',                               # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '王国军军官',                           # 21
        '尼冈德',                               # 22
        '塔罗牌',                               # 23
        '塔罗牌',                               # 24
        '咖啡',                                 # 25
        '咖啡',                                 # 26
        '咖啡',                                 # 27
        '塔罗牌',                               # 28
        '王国军士兵',                           # 29
        '王国军宪兵',                           # 30
        '王国军宪兵',                           # 31
        '目标用摄像机',                         # 32
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01100 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH02080 ._CH',             # 05
        'ED6_DT07/CH02360 ._CH',             # 06
        'ED6_DT07/CH01620 ._CH',             # 07
        'ED6_DT07/CH01310 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH00033 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT06/CH20021 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT07/CH01650 ._CH',             # 0E
        'ED6_DT07/CH00003 ._CH',             # 0F
        'ED6_DT07/CH00013 ._CH',             # 10
        'ED6_DT07/CH00023 ._CH',             # 11
        'ED6_DT06/CH20045 ._CH',             # 12
        'ED6_DT07/CH02083 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01100P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH02080P._CP',             # 05
        'ED6_DT07/CH02360P._CP',             # 06
        'ED6_DT07/CH01620P._CP',             # 07
        'ED6_DT07/CH01310P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH00033P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT06/CH20021P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT07/CH01650P._CP',             # 0E
        'ED6_DT07/CH00003P._CP',             # 0F
        'ED6_DT07/CH00013P._CP',             # 10
        'ED6_DT07/CH00023P._CP',             # 11
        'ED6_DT06/CH20045P._CP',             # 12
        'ED6_DT07/CH02083P._CP',             # 13
    )

    DeclNpc(
        X                   = 18100,
        Z                   = 0,
        Y                   = 16400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 15350,
        Z                   = 0,
        Y                   = 15480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 13100,
        Z                   = -100,
        Y                   = 17110,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 18850,
        Z                   = 200,
        Y                   = 14150,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 131075,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 19944,
        Z                   = 0,
        Y                   = 8440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 203044,
        Z                   = 0,
        Y                   = 9046,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 203044,
        Z                   = 0,
        Y                   = 9046,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 209550,
        Z                   = 200,
        Y                   = 11820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -60835,
        Z                   = 0,
        Y                   = 38681,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18300,
        Z                   = 0,
        Y                   = 14300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 201700,
        Z                   = 0,
        Y                   = 109600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 104300,
        Z                   = 0,
        Y                   = 107600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 204600,
        Z                   = 0,
        Y                   = 15300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 110330,
        Z                   = 0,
        Y                   = -74950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 18500,
        Z                   = 750,
        Y                   = 15400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 524299,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 19100,
        Z                   = 700,
        Y                   = 15300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327692,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14950,
        Z                   = 700,
        Y                   = 12390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15000,
        Z                   = 700,
        Y                   = 11770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13190,
        Z                   = 700,
        Y                   = 12340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13240,
        Z                   = 700,
        Y                   = 11670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 103480,
        Z                   = 0,
        Y                   = -74820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 110330,
        Z                   = 0,
        Y                   = -77770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 106850,
        Z                   = 0,
        Y                   = -77680,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 118930,
        TriggerZ            = 0,
        TriggerY            = 14070,
        TriggerRange        = 800,
        ActorX              = 118930,
        ActorZ              = 800,
        ActorY              = 14070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 123890,
        TriggerZ            = 0,
        TriggerY            = 11990,
        TriggerRange        = 800,
        ActorX              = 123890,
        ActorZ              = 800,
        ActorY              = 11990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17690,
        TriggerZ            = 0,
        TriggerY            = 14350,
        TriggerRange        = 800,
        ActorX              = 18100,
        ActorZ              = 1500,
        ActorY              = 16400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4B6",          # 00, 0
        "Function_1_603",          # 01, 1
        "Function_2_62F",          # 02, 2
        "Function_3_645",          # 03, 3
        "Function_4_662",          # 04, 4
        "Function_5_6D7",          # 05, 5
        "Function_6_6DC",          # 06, 6
        "Function_7_10DA",         # 07, 7
        "Function_8_18D2",         # 08, 8
        "Function_9_1C0C",         # 09, 9
        "Function_10_2EE1",        # 0A, 10
        "Function_11_3535",        # 0B, 11
        "Function_12_3824",        # 0C, 12
        "Function_13_3AA6",        # 0D, 13
        "Function_14_4174",        # 0E, 14
        "Function_15_421A",        # 0F, 15
        "Function_16_44EF",        # 10, 16
        "Function_17_4923",        # 11, 17
        "Function_18_4CE6",        # 12, 18
        "Function_19_4FBE",        # 13, 19
        "Function_20_5AD1",        # 14, 20
        "Function_21_724D",        # 15, 21
        "Function_22_72AB",        # 16, 22
        "Function_23_730E",        # 17, 23
        "Function_24_7371",        # 18, 24
        "Function_25_73C1",        # 19, 25
        "Function_26_7402",        # 1A, 26
        "Function_27_83AA",        # 1B, 27
        "Function_28_B840",        # 1C, 28
        "Function_29_B889",        # 1D, 29
        "Function_30_B8CD",        # 1E, 30
        "Function_31_B902",        # 1F, 31
        "Function_32_B94B",        # 20, 32
    )


    def Function_0_4B6(): pass

    label("Function_0_4B6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_4C2"),
        (SWITCH_DEFAULT, "loc_4CF"),
    )


    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_END)), "loc_4CC")
    OP_A2(0x9)

    label("loc_4CC")

    Jump("loc_4CF")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_503")
    SetChrPos(0x9, 16900, 0, 14300, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_59C")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_51E")
    SetChrPos(0x9, 16900, 0, 14300, 0)
    Jump("loc_59C")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_539")
    SetChrPos(0x9, 16900, 0, 14300, 0)
    Jump("loc_59C")

    label("loc_539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_559")
    SetChrPos(0x9, 21600, 0, 11200, 180)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_59C")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_563")
    Jump("loc_59C")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_END)), "loc_572")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_59C")

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_581")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_59C")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_590")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_59C")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_59C")
    ClearChrFlags(0xA, 0x80)

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5D8")
    SetChrChipByIndex(0xB, 10)
    SetChrPos(0xB, 18850, 200, 14150, 225)
    SetChrSubChip(0xB, 2)
    Jump("loc_5DD")

    label("loc_5D8")

    SetChrChipByIndex(0xB, 10)

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_5EB")
    OP_A3(0x3FA)
    Event(0, 26)

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_602")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 27)

    label("loc_602")

    Return()

    # Function_0_4B6 end

    def Function_1_603(): pass

    label("Function_1_603")

    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_END)), "loc_617")
    Jump("loc_623")

    label("loc_617")

    OP_6F(0x2, 0)
    OP_72(0x2, 0x10)

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_62E")
    OP_64(0x0, 0x1)

    label("loc_62E")

    Return()

    # Function_1_603 end

    def Function_2_62F(): pass

    label("Function_2_62F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_644")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_62F")

    label("loc_644")

    Return()

    # Function_2_62F end

    def Function_3_645(): pass

    label("Function_3_645")

    OP_A3(0xA)

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_661")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_648")

    label("loc_661")

    Return()

    # Function_3_645 end

    def Function_4_662(): pass

    label("Function_4_662")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D6")
    OP_8E(0xFE, 0x4AE2, 0x0, 0x326E, 0x5DC, 0x0)
    OP_8E(0xFE, 0x57D0, 0x0, 0x2C88, 0x5DC, 0x0)
    OP_8C(0xFE, 180, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x57D0, 0x0, 0x2C88, 0x5DC, 0x0)
    OP_8E(0xFE, 0x425E, 0x0, 0x3804, 0x5DC, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    Jump("Function_4_662")

    label("loc_6D6")

    Return()

    # Function_4_662 end

    def Function_5_6D7(): pass

    label("Function_5_6D7")

    Call(0, 6)
    Return()

    # Function_5_6D7 end

    def Function_6_6DC(): pass

    label("Function_6_6DC")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "休息\x01",        # 2
            "离开\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x18)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_74A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763")
    OP_0D()
    OP_A9(0x17)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77D")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_821")

    ChrTalk(
        0x8,
        (
            "那些空贼\x01",
            "一个不留地都被抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "国境守备队的士兵们\x01",
            "终于可以好好休息一阵子了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_9AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_924")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "军人同志们都累得不行了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然找到了失踪的飞艇，\x01",
            "不过他们好像还没有抓到\x01",
            "那些作案的犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "摩尔根将军彻夜不眠地\x01",
            "指挥手下执行搜索任务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A9")

    label("loc_924")


    ChrTalk(
        0x8,
        "军人同志们都累得不行了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "摩尔根将军彻夜不眠地\x01",
            "指挥手下执行搜索任务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A9")

    Jump("loc_10D6")

    label("loc_9AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "刚把吃霸王餐的犯人\x01",
            "关进监牢里面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这次是不是又抓到了\x01",
            "袭击定期船的家伙们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，搞错了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B15")

    label("loc_A82")


    ChrTalk(
        0x8,
        (
            "空贼团那些家伙\x01",
            "很难被抓获啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他们是可以在天空飞翔的家伙。\x01",
            "要抓到他们也不是件容易事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B15")

    Jump("loc_10D6")

    label("loc_B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_CC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "国境守备队好像十分忙碌。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然出动了很多士兵来搜索，\x01",
            "可还是没发现定期船的踪影。\x01",
            "我看他们以后怎么摆架子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过话说回来，\x01",
            "士兵们也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBD")

    label("loc_C1C")


    ChrTalk(
        0x8,
        "国境守备队好像十分忙碌。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然出动了很多士兵来搜索，\x01",
            "不过还是没发现定期船的踪影。\x01",
            "我看他们以后怎么摆架子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBD")

    Jump("loc_10D6")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7B")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "哈～哈～哈～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈肯大门的名产，\x01",
            "就是将军阁下的雷声降下呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "士兵们也是人，\x01",
            "犯错是难免的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E12")

    label("loc_D7B")


    ChrTalk(
        0x8,
        (
            "哈肯大门的名产，\x01",
            "就是将军阁下的雷声降下呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "士兵们也是人，\x01",
            "犯错是难免的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E12")

    Jump("loc_10D6")

    label("loc_E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "王国军封锁了\x01",
            "通往这里的钢壁之路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从帝国过来的人\x01",
            "以及打算出国的人\x01",
            "都只能滞留在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那边的金发小兄弟\x01",
            "也是同样的情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8A")

    label("loc_F02")


    ChrTalk(
        0x8,
        (
            "王国军封锁了\x01",
            "通往这里的钢壁之路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从帝国过来的人\x01",
            "以及打算出国的人\x01",
            "都只能滞留在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8A")

    Jump("loc_10D6")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_10D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1064")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "你好，欢迎来到关所酒场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这里好歹也是个酒场，\x01",
            "食物和饮料应有尽有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "虽然都是些粗茶淡饭。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_1064")


    ChrTalk(
        0x8,
        (
            "这里好歹也是个酒场，\x01",
            "食物和饮料应有尽有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "虽然都是些粗茶淡饭。\x02",
    )

    CloseMessageWindow()

    label("loc_10D6")

    TalkEnd(0x8)
    Return()

    # Function_6_6DC end

    def Function_7_10DA(): pass

    label("Function_7_10DA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1196")

    ChrTalk(
        0xFE,
        (
            "前几天，\x01",
            "军队的士兵抓到了一个古怪的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "听说那个男人做了什么欺诈的事情。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A9")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "最近，即使一到睡觉的时间，\x01",
            "军队的士兵还一直在进进出出的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "吵得我们也睡得不舒服……呼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下次那些士兵来喝酒的话，\x01",
            "要向他们发发牢骚才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_12A9")


    ChrTalk(
        0xFE,
        (
            "最近，即使一到睡觉的时间，\x01",
            "军队的士兵还一直在进进出出的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "吵得我们也睡得不舒服……呼。\x02",
    )

    CloseMessageWindow()

    label("loc_132E")

    Jump("loc_18CE")

    label("loc_1331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1429")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "传言中的精英上校\x01",
            "来我们店里吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他真是风度翩翩的绅士，\x01",
            "和这里粗鲁的军人\x01",
            "简直是天壤之别的对比啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不经意，我都迷上他了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_1429")


    ChrTalk(
        0xFE,
        (
            "这世上，\x01",
            "还会有如此动人的男人在啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1480")

    Jump("loc_18CE")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1596")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "在此之前，我曾经\x01",
            "从那些士兵听过上校的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到那个超帅的精英上校\x01",
            "会来关所这里视察。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呀，要是他向我打招呼的话，\x01",
            "人家怎么应他才好呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要穿一件漂亮的衣服\x01",
            "来迎接上校的到来才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161D")

    label("loc_1596")


    ChrTalk(
        0xFE,
        (
            "没想到那个超帅的精英上校\x01",
            "会来关所这里视察。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呀，要是他向我打招呼的话，\x01",
            "人家怎么应他才好呢㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161D")

    Jump("loc_18CE")

    label("loc_1620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_177E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F8")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "将军的怒吼声\x01",
            "还是和以前一样震耳欲聋啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种小店\x01",
            "也能听得这么清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一听到那个声音，\x01",
            "新兵们一个一个都\x01",
            "哭着跑到这里来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177B")

    label("loc_16F8")


    ChrTalk(
        0xFE,
        (
            "将军的怒吼声\x01",
            "还是和以前一样震耳欲聋啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一听到那个声音，\x01",
            "新兵们一个一个都\x01",
            "哭着跑到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177B")

    Jump("loc_18CE")

    label("loc_177E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1839")

    ChrTalk(
        0xFE,
        (
            "说起这里的客人，\x01",
            "都是一些歇班的士兵\x01",
            "和等待入境办理手续的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以说，\x01",
            "大部分的客人都已经很脸熟啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_1839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_18CE")

    ChrTalk(
        0xFE,
        (
            "那位金发的小兄弟，\x01",
            "看上去样子还不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过和他谈了两句之后，\x01",
            "发现他真是个奇怪的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")

    TalkEnd(0x9)
    Return()

    # Function_7_10DA end

    def Function_8_18D2(): pass

    label("Function_8_18D2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_194E")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "街道的封锁总算解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "入境许可证也办理好了，\x01",
            "我终于可以到柏斯去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C08")

    label("loc_194E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B03")
    OP_A2(0x393)

    ChrTalk(
        0xFE,
        (
            "由于定期船一直停航，\x01",
            "我只能靠走路来到这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底要让身为帝都商人的我\x01",
            "等到什么时候才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呆在这里太清闲了，\x01",
            "所以把带在身上的书给看完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "带在身上觉得有点麻烦，\x01",
            "不如把这本书送给你们算了。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x214, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第３卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_1BAF")

    label("loc_1B03")


    ChrTalk(
        0xFE,
        (
            "到底要让身为帝都商人的我\x01",
            "等到什么时候才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小国所做的事情\x01",
            "就是欠缺优雅的气派……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAF")

    Jump("loc_1C08")

    label("loc_1BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(
        0xFE,
        "我是埃雷波尼亚帝国的商人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在我正在去柏斯的途中。\x02",
    )

    CloseMessageWindow()

    label("loc_1C08")

    TalkEnd(0xA)
    Return()

    # Function_8_18D2 end

    def Function_9_1C0C(): pass

    label("Function_9_1C0C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1D04")
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C38")
    SetChrSubChip(0xB, 1)
    Jump("loc_1C53")

    label("loc_1C38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4E")
    SetChrSubChip(0xB, 2)
    Jump("loc_1C53")

    label("loc_1C4E")

    SetChrSubChip(0xB, 0)

    label("loc_1C53")

    OP_8C(0xB, 225, 0)
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#030F哎哟，\x01",
            "难道说你们改变主意打算带我去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F怎么可能～你做梦吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#034F小气。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 2)
    Jump("loc_2EDD")

    label("loc_1D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC5")
    EventBegin(0x0)
    OP_A2(0x310)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 17370, 0, 13720, 90)
    SetChrPos(0x102, 17820, 0, 12390, 45)
    SetChrPos(0x103, 19280, 0, 12690, 0)
    SetChrPos(0xB, 18850, 200, 14150, 225)
    SetChrSubChip(0xB, 0)
    OP_69(0xB, 0x0)
    OP_67(0, 6740, -10000, 0)
    OP_6B(1210, 0)
    OP_6C(45000, 0)
    OP_6E(660, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#030F呀，你们好啊。\x02\x03",
            "你们看起来好像是利贝尔人，\x01",
            "要到帝国旅行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不呢，\x01",
            "我们是因为有事要办才到这里来的。\x02\x03",
            "没打算去帝国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你看起来\x01",
            "好像是埃雷波尼亚人。\x02\x03",
            "是来利贝尔王国旅游的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#035F呵呵，一半工作，一半游玩啦。\x02\x03",
            "#035F你们是来办事的吗……\x01",
            "那么本人可看出你们的真面目了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F哎，真面目？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#030F你们其实是游击士吧？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F为、为什么……\x01",
            "明明游击士徽章都摘下来了！\x02\x03",
            "难道说，你是同行？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#035F确实帝国也有游击士协会，\x01",
            "可惜，本人并不是游击士。\x02\x03",
            "#030F只是在游击士协会有熟人而已。\x02\x03",
            "你们给我的感觉和他们很像，\x01",
            "所以我就稍微猜测了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F真是敏锐的观察力呀……\x01",
            "我想你不会是个普通人吧。\x02\x03",
            "#012F真的只是来旅行的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#035F呵呵，\x01",
            "先不要用这幅表情瞪着我嘛。\x02\x03",
            "冰冷地闪烁着琥珀色光辉的眼眸……\x01",
            "宛如极品白兰地的色泽。\x02\x03",
            "#037F让人不禁想要\x01",
            "紧紧拥抱一亲芳泽啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x102, 0xB4, 0x258, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        "#018F什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F真……敢说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F慢、慢着！\x01",
            "难道你是有那种嗜好的人！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#031F嘻……\x01",
            "本人只是迷恋美丽的东西罢了。\x02\x03",
            "玲珑有致的美女。\x01",
            "沉静惊艳的少年。\x02\x03",
            "天籁之音，洗涤心灵的风景。\x01",
            "名匠之作，震撼魂魄的故事。\x02\x03",
            "再加之极品美酒与上等料理……\x02\x03",
            "以上所说，\x01",
            "皆是本人所好之物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F只是单纯的没有节操罢了吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F不可救药的享乐主义者呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#034F哈～不管是哪个时代，\x01",
            "天才果然都是孤独的啊。\x02\x03",
            "本人像玻璃一样，\x01",
            "脆弱易碎的纯洁心灵已经受到了伤害呢。\x02\x03",
            "#030F黑发的少年……\x01",
            "来抚慰一下我受伤的心灵好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F不好意思，我拒绝。\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(
        0x8,
        "（尽说些奇怪的话……）\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xC, 20020, 0, 8730, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#1P喂～你们几个。\x02",
    )

    CloseMessageWindow()
    OP_4A(0xC, 255)
    ClearChrFlags(0xC, 0x80)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_27D0)
    OP_8E(0xC, 0x4DD0, 0x0, 0x2562, 0x7D0, 0x0)
    OP_4B(0x8, 255)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    def lambda_2835():
        OP_6D(20620, 0, 12620, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2835)

    def lambda_284D():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_284D)

    def lambda_285B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_285B)

    def lambda_2869():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2869)
    SetChrSubChip(0xB, 1)
    OP_8E(0xC, 0x5014, 0x0, 0x2B5C, 0xBB8, 0x0)
    OP_8C(0xC, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(
        0x103,
        "#020F#5P啊，是刚才的那个士兵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P就在刚才，\x01",
            "将军已经回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2P我已经向将军禀报了你们的事，\x01",
            "他可以马上接见你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#5P哎，是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2P请赶快到营房来。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    OP_8E(0xC, 0x4E2A, 0x0, 0x2832, 0xBB8, 0x0)

    def lambda_29AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_29AD)
    OP_8E(0xC, 0x4E2A, 0x0, 0x21F2, 0x7D0, 0x0)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    OP_6D(18830, 0, 13990, 1200)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#010F比预想中回来得要早啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#020F#2P是啊。\x01",
            "终于要得到情报了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#035F呵呵……\x01",
            "那我们马上去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2EDD")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E19")
    EventBegin(0x0)
    OP_A2(0x30F)

    ChrTalk(
        0xB,
        (
            "#035F呵呵，真令人惊讶……\x02\x03",
            "#035F初次品尝正宗的利贝尔料理，\x01",
            "想不到味道还真不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈，\x01",
            "能听到你这么说我也很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果到了城市那边，\x01",
            "你会找到更多富有利贝尔特色的饭店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这也是旅行中的乐趣所在啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#030F当然，本人就是如此打算的。\x02\x03",
            "#030F偏远地区的酒馆也能做出如此美味的料理，\x01",
            "看来今后真是令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嘿嘿，这里的确偏远，真过意不去啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "再喝点酒怎么样？\x01",
            "虽然是便宜货，但是口感相当好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#035F呼，让我考虑一下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（这个人，难道是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（看上去好像是从帝国来的旅行者。）\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_2EDD")

    label("loc_2E19")


    ChrTalk(
        0xB,
        (
            "#030F嗯，这酒的确不错……\x02\x03",
            "#030F没想到利贝尔的东西\x01",
            "是如此的价廉物美。\x02\x03",
            "#030F这也许是女王\x01",
            "赐予民众的恩惠之一吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDD")

    TalkEnd(0xB)
    Return()

    # Function_9_1C0C end

    def Function_10_2EE1(): pass

    label("Function_10_2EE1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3258")
    OP_A2(0x35F)
    OP_A2(0x3)

    ChrTalk(
        0x101,
        "#006F（啊，这个人……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，\x01",
            "　好像和我们一样都是游击士呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F喂，打扰一下？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F你还是那样讨人厌呢，\x01",
            "斯丁克。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "你是……\x01",
            "以前的那个见习游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F没错呢。\x02\x03",
            "托你的福，\x01",
            "现在我已经是正游击士啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……看起来的确成熟了不少。\x01",
            "在柏斯支部有工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，现在就正在工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近发生了很多事情，\x01",
            "游击士的人手远远不够呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……那就靠你们了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    ChrTalk(
        0x101,
        (
            "#002F（是雪拉姐的熟人吧。\x01",
            "　感觉有点恐怖的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（但是那走路的动作……\x01",
            "　看起来应该很厉害吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3531")

    label("loc_3258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3480")
    OP_A2(0x3)

    ChrTalk(
        0x103,
        "#020F这不是斯丁克吗。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是雪拉扎德啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F柏斯支部的同行也都很忙吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚把一位\x01",
            "帝国的旅行者送走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后打算不回支部\x01",
            "直接去办下一件事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F真的是很忙呢。\x02\x03",
            "怎么样，等我们都忙完了，\x01",
            "一起去喝一杯吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "算了，我不会喝酒。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F啊，是吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    Jump("loc_3531")

    label("loc_3480")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "我刚把一位\x01",
            "帝国的旅行者送走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后打算不回支部\x01",
            "直接去办下一件事情……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    label("loc_3531")

    TalkEnd(0x11)
    Return()

    # Function_10_2EE1 end

    def Function_11_3535(): pass

    label("Function_11_3535")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_36B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3633")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "空贼被抓获了，\x01",
            "终于可以恢复正常的工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，这里毕竟是\x01",
            "和埃雷波尼亚接壤的国境啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们可不能\x01",
            "掉以轻心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B4")

    label("loc_3633")


    ChrTalk(
        0xFE,
        (
            "虽然恢复正常工作了，\x01",
            "这里就是和埃雷波尼亚接壤的国境，\x01",
            "我们可不能掉以轻心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B4")

    Jump("loc_3820")

    label("loc_36B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3742")

    ChrTalk(
        0xFE,
        (
            "明早要乘坐警备飞艇\x01",
            "在山里面进行搜索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天得早点睡才行啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3820")

    label("loc_3742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_379F")

    ChrTalk(
        0xFE,
        "啊啊，今天很累啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起吃饭和洗澡，\x01",
            "现在最想做的还是好好睡一觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3820")

    label("loc_379F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3820")

    ChrTalk(
        0xFE,
        (
            "其实今天\x01",
            "本来不是我当班的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为上面下达了\x01",
            "让我们在要塞内待命的命令。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3820")

    TalkEnd(0x13)
    Return()

    # Function_11_3535 end

    def Function_12_3824(): pass

    label("Function_12_3824")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_390D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F2")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "即使那些空贼被抓住了，\x01",
            "也并不代表我能得到休假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在处于\x01",
            "睡眠不足的状态啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔……想睡觉……\x02",
    )

    CloseMessageWindow()
    Jump("loc_390A")

    label("loc_38F2")


    ChrTalk(
        0xFE,
        "唔……想睡觉……\x02",
    )

    CloseMessageWindow()

    label("loc_390A")

    Jump("loc_3AA2")

    label("loc_390D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_39A2")

    ChrTalk(
        0xFE,
        (
            "明天歇班的士兵\x01",
            "也会被召集起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可能会进行一场\x01",
            "大规模的搜索行动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA2")

    label("loc_39A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3A24")

    ChrTalk(
        0xFE,
        "嗯……睡觉是最舒服的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁现在去食堂\x01",
            "弄点饭吃吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA2")

    label("loc_3A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3AA2")

    ChrTalk(
        0xFE,
        "呼啊啊～～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天参加飞艇的搜查，\x01",
            "很晚才回来，现在好困。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA2")

    TalkEnd(0x12)
    Return()

    # Function_12_3824 end

    def Function_13_3AA6(): pass

    label("Function_13_3AA6")

    TalkBegin(0xF)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3ACB")
    SetChrSubChip(0xFE, 2)
    Jump("loc_3AFC")

    label("loc_3ACB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AE1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3AFC")

    label("loc_3AE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AF7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3AFC")

    label("loc_3AF7")

    SetChrSubChip(0xFE, 2)

    label("loc_3AFC")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC8")
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#160F唔，你们两个是卡西乌斯的……\x02\x03",
            "来干什么啊？\x01",
            "这里已经没你们的事了。\x02\x03",
            "我现在有很多工作要处理，\x01",
            "没空和你们瞎闹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0B")

    label("loc_3BC8")


    ChrTalk(
        0xF,
        (
            "#160F来干什么啊？\x01",
            "这里已经没你们的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0B")

    Jump("loc_416B")

    label("loc_3C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3C90")

    ChrTalk(
        0xF,
        (
            "#163F这次连情报部的家伙也来了，\x01",
            "我们非得要靠他们协助才行吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F42")

    label("loc_3C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 1)), scpexpr(EXPR_END)), "loc_3DCD")
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#163F唔～\x01",
            "如果继续动员守备队的士兵的话，\x01",
            "那岂不忽视了对帝国方面的监视。\x02\x03",
            "明知我们的工作已经够忙的了，\x01",
            "还要叫这些家伙过来耍派头，\x01",
            "这叫什么上策啊……\x02\x03",
            "这次连情报部的家伙也来了，\x01",
            "我们非得要靠他们协助才行吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F42")

    label("loc_3DCD")

    OP_A2(0x361)

    ChrTalk(
        0xF,
        (
            "#160F怎么，是卡西乌斯的孩子吗……\x02\x03",
            "别老在我面前走来走去的行不行……\x01",
            "　\x02\x03",
            "我事先给你们一个忠告，\x01",
            "这次的事件属于军队的管辖范围。\x02\x03",
            "要是你们以后再有出格的行为，\x01",
            "就别怪我不客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F（将军的脸色好像不太好呢。\x01",
            "　看来工作累坏了吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（嗯，因为军队也在拼命地\x01",
            "　到处搜索那些空贼的行踪。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F42")

    Jump("loc_416B")

    label("loc_3F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_416B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CF")
    OP_A2(0x361)
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#160F怎么，是卡西乌斯的孩子吗……\x02\x03",
            "别老在我面前走来走去的行不行……\x01",
            "　\x02\x03",
            "我事先给你们一个忠告，\x01",
            "这次的事件属于军队的管辖范围。\x02\x03",
            "要是你们以后再有出格的行为，\x01",
            "就别怪我不客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F（将军的脸色好像不太好呢。\x01",
            "　看来工作累坏了吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（嗯，因为军队也在拼命地\x01",
            "　到处搜索那些空贼的行踪。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_416B")

    label("loc_40CF")


    ChrTalk(
        0xF,
        (
            "#160F我事先给你们一个忠告，\x01",
            "这次的事件属于军队的管辖范围。\x02\x03",
            "要是你们以后再有出格的行为，\x01",
            "就别怪我不客气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_416B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xF)
    Return()

    # Function_13_3AA6 end

    def Function_14_4174(): pass

    label("Function_14_4174")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4216")

    ChrTalk(
        0xFE,
        (
            "那些空贼已经被押送到\x01",
            "蔡斯的雷斯顿要塞那里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不久之后，\x01",
            "他们会受到军队的严厉审讯的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4216")

    TalkEnd(0x14)
    Return()

    # Function_14_4174 end

    def Function_15_421A(): pass

    label("Function_15_421A")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_43D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4357")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "为、为什么我会\x01",
            "鬼迷心窍做出这种事……\x01",
            "只、只是一时的糊涂而已啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我以后再也不做坏事了。\x01",
            "请原谅我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我很胆小的，\x01",
            "而且身体很虚弱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果一直被关在监狱里，\x01",
            "一定会生病的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D3")

    label("loc_4357")


    ChrTalk(
        0xFE,
        (
            "我、我很胆小的，\x01",
            "而且身体很虚弱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我以后再也不做坏事了。\x01",
            "请原谅我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D3")

    Jump("loc_44EB")

    label("loc_43D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448C")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "所以啊，我说了好几遍啦，\x01",
            "请拿出证据来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果还是怀疑我的话，\x01",
            "就把证据拿出来再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵哈哈哈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44EB")

    label("loc_448C")


    ChrTalk(
        0xFE,
        (
            "如果还是怀疑我的话，\x01",
            "就把证据拿出来再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵哈哈哈。\x02",
    )

    CloseMessageWindow()

    label("loc_44EB")

    TalkEnd(0x15)
    Return()

    # Function_15_421A end

    def Function_16_44EF(): pass

    label("Function_16_44EF")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BF")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "被关在监牢里的这个大叔\x01",
            "看起来是个坏人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然以貌取人\x01",
            "是不太礼貌的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过像这样\x01",
            "一目了然的情况也很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4631")

    label("loc_45BF")


    ChrTalk(
        0xFE,
        (
            "虽然以貌取人\x01",
            "是不太礼貌的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过像这样\x01",
            "一目了然的情况也很多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4631")

    Jump("loc_491F")

    label("loc_4634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_476B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F6")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "被关在监牢里的这个大叔\x01",
            "看起来是个很坏的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然以貌取人\x01",
            "是不太礼貌的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过像这样\x01",
            "一目了然的情况也很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4768")

    label("loc_46F6")


    ChrTalk(
        0xFE,
        (
            "虽然以貌取人\x01",
            "是不太礼貌的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过像这样\x01",
            "一目了然的情况也很多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4768")

    Jump("loc_491F")

    label("loc_476B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485D")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "被关在监牢里的这个大叔\x01",
            "不管怎么看都是个坏蛋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是只要没有找到证据，\x01",
            "就不得不释放他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人无法接受呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_491F")

    label("loc_485D")


    ChrTalk(
        0xFE,
        (
            "只要没有找到被关在监牢里的\x01",
            "这个大叔的犯罪证据，\x01",
            "就不得不释放他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把这样的坏人释放出去，\x01",
            "真是让人无法接受呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491F")

    TalkEnd(0x1C)
    Return()

    # Function_16_44EF end

    def Function_17_4923(): pass

    label("Function_17_4923")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A49")

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "你怎么解释这本黑账簿？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "别着急，\x01",
            "你可以想好了再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "反正时间还非常充裕。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CE2")

    label("loc_4A49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4B6A")

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "你怎么解释这本黑账簿？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "别着急，\x01",
            "你可以想好了再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "反正时间还非常充裕。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CE2")

    label("loc_4B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C54")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "喂，你到底把那本帐簿上\x01",
            "记载的钱弄到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "早点交待清楚，对你是有好处的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正我们迟早\x01",
            "也会找到证据的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE2")

    label("loc_4C54")


    ChrTalk(
        0xFE,
        "早点交待清楚，对你是有好处的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正我们迟早\x01",
            "也会找到证据的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE2")

    TalkEnd(0x1D)
    Return()

    # Function_17_4923 end

    def Function_18_4CE6(): pass

    label("Function_18_4CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x1, 0x8000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x338)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D05")
    Call(0, 19)
    Jump("loc_4FBD")

    label("loc_4D05")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DBC")

    ChrTalk(
        0xFE,
        "终于解决掉尼冈德这家伙的事情了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很快就可以把他关押起来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FBA")

    label("loc_4DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4E93")

    ChrTalk(
        0xFE,
        (
            "在空贼团的据点里\x01",
            "找到了尼冈德这家伙的黑账本。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肯定是强盗来的时候\x01",
            "把它一起抢走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "坏蛋帮了坏蛋的忙，\x01",
            "还真是奇妙的偶然啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FBA")

    label("loc_4E93")


    ChrTalk(
        0xFE,
        (
            "我们怀疑这个男人\x01",
            "侵占了工房的财产……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是在那家伙的店铺里面调查后，\x01",
            "又没有发现任何有力的证据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拘留是有期限的，\x01",
            "很快就要到释放他的时候了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBA")

    TalkEnd(0x1E)

    label("loc_4FBD")

    Return()

    # Function_18_4CE6 end

    def Function_19_4FBE(): pass

    label("Function_19_4FBE")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 106320, 0, -76490, 180)
    SetChrPos(0x102, 105450, 0, -77130, 135)
    TurnDirection(0x101, 0x1D, 0)
    TurnDirection(0x102, 0x1D, 0)
    OP_6D(109770, 0, -76050, 2000)
    OP_0D()
    OP_4A(0x15, 0)
    OP_4A(0x1D, 0)

    ChrTalk(
        0x1D,
        (
            "喂，你到底把那本帐簿上\x01",
            "记载的钱弄到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "早点交待清楚，对你是有好处的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "反正我们迟早\x01",
            "也会找到证据的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "所以啊，我说了好几遍啦，\x01",
            "请拿出证据来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "如果还是怀疑我的话，\x01",
            "就把证据拿出来再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "呵呵哈哈哈。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    OP_4B(0x15, 0)
    OP_4B(0x1D, 0)
    OP_6D(106250, 0, -77490, 1500)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x101, 180, 400)
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x101,
        "#000F请问，这里怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 400)
    OP_4A(0x1E, 0)

    ChrTalk(
        0x1E,
        "嗯？是这样的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "我们怀疑这个男人\x01",
            "侵占了工房的财产……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "但是在那家伙的店铺里面调查后，\x01",
            "又没有发现任何有力的证据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "拘留是有期限的，\x01",
            "很快就要到释放他的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F咦～要证据啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F…………\x02\x03",
            "……对了，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F说起来，我们不是在空贼的基地里\x01",
            "发现了一个奇怪的东西吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F奇怪的东西？\x02\x03",
            "#001F……啊，是那个。\x02\x03",
            "是说在吸尘器里面藏着的笔记本吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x1E,
        "吸尘器里面的……笔记本？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "不好意思，\x01",
            "你们说的东西，能让我看看吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_551B():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_551B)
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x101,
        "#002F好的，说不定对你们有用。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "黑色笔记本\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8C(0x1E, 45, 400)
    OP_62(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x1E,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E)
    Sleep(800)
    OP_62(0x1E, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x1E,
        "…………就是它。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 400)

    ChrTalk(
        0x1E,
        "就是它，没错了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "这就是那个家伙经营的工房的黑账簿。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x15, 400)

    ChrTalk(
        0x1E,
        "喂，尼冈德！\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5709():
        OP_69(0x1F, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5709)

    def lambda_5717():
        TurnDirection(0x1D, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5717)

    def lambda_5725():
        TurnDirection(0x1C, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5725)

    def lambda_5733():
        TurnDirection(0x101, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5733)

    def lambda_5741():
        TurnDirection(0x102, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5741)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x15, 0x1E, 400)
    OP_4A(0x15, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1C, 0)
    WaitChrThread(0x1F, 0x1)

    ChrTalk(
        0x1E,
        (
            "看清楚了。\x01",
            "这个就是你犯罪的证据！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x15, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    Sleep(400)

    ChrTalk(
        0x15,
        "这、这不可能！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "它应该和吸尘器一起\x01",
            "被强盗给抢走了的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5835():

        label("loc_5835")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_5835")

    QueueWorkItem2(0x0, 1, lambda_5835)

    def lambda_5846():

        label("loc_5846")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_5846")

    QueueWorkItem2(0x1, 1, lambda_5846)

    def lambda_5857():

        label("loc_5857")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_5857")

    QueueWorkItem2(0x15, 1, lambda_5857)
    OP_92(0x1E, 0x1D, 0x3E8, 0x7D0, 0x0)
    Sleep(2000)
    OP_44(0x15, 0x1)
    OP_8C(0x1D, 0, 400)
    OP_8C(0x15, 180, 400)

    def lambda_588D():
        OP_6D(106250, 0, -77490, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_588D)
    OP_8E(0x1E, 0x1A162, 0x0, 0xFFFED090, 0x7D0, 0x0)
    TurnDirection(0x1E, 0x101, 400)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)

    def lambda_58C8():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_58C8)
    OP_8C(0x102, 135, 400)
    WaitChrThread(0x1F, 0x1)

    ChrTalk(
        0x1E,
        "谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "这种麻烦的事情，\x01",
            "果然就要靠游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "有了那个记事本，\x01",
            "就肯定可以定那家伙的罪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "我一定会通过游击士协会，\x01",
            "正式支付你们酬劳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "再次感谢你们的协助。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【黑色笔记本】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x338, 1)
    OP_28(0x14, 0x4, 0x2)
    OP_28(0x14, 0x4, 0x4)
    OP_28(0x14, 0x4, 0x10)
    OP_28(0x14, 0x1, 0x1)
    OP_28(0x14, 0x1, 0x2)
    OP_28(0x14, 0x1, 0x4)
    OP_A3(0xF)
    OP_A3(0x8)
    OP_8C(0x1E, 45, 0)
    OP_8C(0x1C, 270, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x15, 0)
    EventEnd(0x0)
    Return()

    # Function_19_4FBE end

    def Function_20_5AD1(): pass

    label("Function_20_5AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_724C")
    EventBegin(0x0)

    ChrTalk(
        0x102,
        (
            "#010F走廊尽头的左边……\x01",
            "这一间就是将军的房间吧。\x02",
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
            "【敲门试试】\x01",      # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5B93"),
        (0, "loc_5B98"),
        (SWITCH_DEFAULT, "loc_724C"),
    )


    label("loc_5B93")

    EventEnd(0x1)
    Jump("loc_724C")

    label("loc_5B98")

    Fade(1000)
    OP_6D(118940, 0, 12530, 0)
    SetChrPos(0xF, 119060, 0, 14740, 0)
    SetChrPos(0x101, 118650, 0, 13360, 0)
    SetChrPos(0x102, 119650, 0, 12540, 315)
    SetChrPos(0x103, 117980, 0, 11970, 0)
    OP_0D()
    OP_A2(0x312)

    ChrTalk(
        0x101,
        "#002F先敲一下……\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(
        0xF,
        "男性的声音",
        "……是梅贝尔小姐的使者吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#4P啊，正是。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "男性的声音",
        "嗯，进来吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F那么，打扰了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(206210, 0, 13220, 0)
    OP_4A(0xF, 255)
    SetChrPos(0xF, 209550, 200, 11820, 270)
    SetChrFlags(0xF, 0x4)
    OP_0D()
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)

    def lambda_5D1B():
        OP_6D(209700, 0, 13260, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D1B)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    OP_43(0x101, 0x0, 0x0, 0x15)
    OP_43(0x103, 0x0, 0x0, 0x17)
    OP_43(0x102, 0x0, 0x0, 0x16)
    WaitChrThread(0x102, 0x0)

    ChrTalk(
        0xF,
        (
            "#160F#2P终于来了啊。\x01",
            "我就是摩尔根。\x02\x03",
            "艾莉茜雅女王任命的\x01",
            "看守哈肯大门的负责人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#5P初次见面。\x01",
            "我们是梅贝尔市长的使者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F在您百忙之中前来打扰，非常抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F#2P哪里，梅贝尔小姐尚年幼的时候\x01",
            "我就认识她了。\x02\x03",
            "何况是以市长立场而传达的话，\x01",
            "我就更是不能不听了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#6P嗯，那么，\x01",
            "还是请您先读读这封信吧。\x02",
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
            "交出了\x07\x02",
            "梅贝尔市长的信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x32D, 1)

    ChrTalk(
        0xF,
        (
            "#161F#2P………………………\x02\x03",
            "#163F唔……\x01",
            "果然是和那个事件有关。\x02\x03",
            "这些事情本来不能向外人透漏的。\x01",
            "但既然是那孩子的委托，就顺应她意思吧。\x02\x03",
            "#160F我就把所掌握的情报告诉你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#6P太好了，真走运☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#161F#2P……？\x02\x03",
            "你为什么要这么兴奋？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#003F#6P（不妙……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F梅贝尔市长她\x01",
            "对这次的事件非常地担心。\x02\x03",
            "所以，我们也很希望能\x01",
            "尽自己的全力来帮助市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F#2P原来如此，梅贝尔小姐\x01",
            "有这么出色的协助者真是太好了。\x02\x03",
            "我马上向你们说明搜索情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#022F#5P洗耳恭听。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F#2P……定期船『林德号』\x01",
            "是在柏斯国际空港起飞后，\x01",
            "飞往洛连特方向的途中失踪的。\x02\x03",
            "现在，各方面的部队还在搜索中，\x01",
            "但到目前为止还没有发现目标。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这么说来，被魔兽攻击或是发生事故的\x01",
            "可能性就大大降低了。\x02\x03",
            "那么庞大的飞船，\x01",
            "如果真的是坠机的话， \x01",
            "在最初进行搜索时就一定能发现了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F#2P正是如此。\x02\x03",
            "实际上，柏斯和洛连特之间的航线\x01",
            "是在视野比较开阔的平原上空。\x02\x03",
            "坠落入瓦雷利亚湖，\x01",
            "甚至海里的可能性应该也很小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P啊～太好了。\x01",
            "没有发生最糟糕的事情……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#022F#5P那样的话，由人为原因而导致\x01",
            "定期船被劫持的可能性就很高了啊。\x02\x03",
            "可以想到的原因，也只有抢夺货物，\x01",
            "甚至是挟持人质来要求赎金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F也就是所谓的劫机事件吧。\x02\x03",
            "#013F还有，从地理情况上考虑的话，\x01",
            "是帝国军队所做的地下活动……\x01",
            "这样的可能性也不能排除。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#505F#6P这、这么说的话，事情可就严重了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#161F#2P…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x103, 0xF, 400)

    ChrTalk(
        0x101,
        "#004F#6P怎么了，将军？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F#2P没什么，只是觉得以寻常百姓而言，\x01",
            "你们的观点相当有见地。\x02\x03",
            "我们军方也为了查明帝国军队\x01",
            "是否有参与此事件的可能性，\x01",
            "正在进行彻底的情报管制。\x02\x03",
            "在国际问题上轻举妄动的话，\x01",
            "很有可能会发展成大规模的战争。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#6P战争……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F#2P但是，不幸中的万幸，\x01",
            "今天早上这种可能性被排除了。\x02\x03",
            "某个组织已经\x01",
            "向王家飞艇公社发表了犯罪声明，\x01",
            "并且要求赎回乘客的赎金。\x02\x03",
            "那个组织的名字叫『卡普亚一家』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#580F#6P『卡普亚一家』？\x02\x03",
            "那、那么，难道说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F……看来这是毫无疑问的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F#2P他们是一伙以兄妹三人为首的的空贼团，\x01",
            "经常在柏斯地区流窜作案。\x02\x03",
            "难道说，\x01",
            "你们也听说过他们的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#6P何止听说过，\x01",
            "之前在洛连特还和他们交过手呢。\x02\x03",
            "那帮家伙，难道就是\x01",
            "到目前为止这个大事件的始作俑者……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6D10():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6D10)

    ChrTalk(
        0x102,
        "#012F艾丝蒂尔……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008F#6P啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#161F#2P在洛连特交过手？\x02\x03",
            "那些家伙在洛连特地区\x01",
            "出没的事情我倒是听说过……\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#6P啊，完了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#025F#5P哈啊～大笨蛋……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xF, 400)
    Sleep(500)

    ChrTalk(
        0xF,
        (
            "#163F#2P……原来如此啊。\x02\x03",
            "作为普通市民能如此思维敏捷而且能说会道，\x01",
            "我正觉得奇怪……\x02\x03",
            "#160F不过还真是没想到，\x01",
            "这样的小女孩儿竟也会是游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#6P什、什么呀，什么小女孩儿！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F但是，我们受到梅贝尔市长委托\x01",
            "这件事的确是事实……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_6B(3070, 0)
    OP_6B(3000, 80)

    def lambda_6FF2():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FF2)

    def lambda_7010():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7010)

    def lambda_702E():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_702E)

    ChrTalk(
        0xF,
        "#162F#3S#2P住口，难道要我姑息你们吗！？#2S\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 5)
    SetChrPos(0xF, 209430, 0, 11990, 270)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0xF,
        "#162F#3S#2P给我来人！！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P好，好大的嗓门……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F#5P简直像狮吼一样……\x02",
    )

    CloseMessageWindow()

    def lambda_711B():
        OP_6D(206340, 0, 12850, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_711B)
    OP_43(0xD, 0x0, 0x0, 0x18)
    OP_43(0xE, 0x0, 0x0, 0x19)
    Sleep(500)

    def lambda_7146():

        label("loc_7146")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_7146")

    QueueWorkItem2(0x101, 2, lambda_7146)

    def lambda_7157():

        label("loc_7157")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_7157")

    QueueWorkItem2(0x103, 2, lambda_7157)

    def lambda_7168():

        label("loc_7168")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_7168")

    QueueWorkItem2(0x102, 2, lambda_7168)
    Sleep(1000)

    ChrTalk(
        0xD,
        "将军，有什么吩咐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "这些人怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F#3P各位游击士要回去了！#2P\x02\x03",
            "#3P立刻，请他们出去！！#2P\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x200)
    OP_28(0x35, 0x1, 0x400)
    SetMapFlags(0x400000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_724C")

    label("loc_724C")

    Return()

    # Function_20_5AD1 end

    def Function_21_724D(): pass

    label("Function_21_724D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_725E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_725E)
    SetChrPos(0xFE, 202980, 0, 8390, 0)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xBB8, 0x0)
    OP_8E(0xFE, 0x328DE, 0x0, 0x2AF8, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_724D end

    def Function_22_72AB(): pass

    label("Function_22_72AB")

    Sleep(1600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_72C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_72C1)
    SetChrPos(0xFE, 202980, 0, 8390, 0)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xBB8, 0x0)
    OP_8E(0xFE, 0x322F8, 0x0, 0x2D1E, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_22_72AB end

    def Function_23_730E(): pass

    label("Function_23_730E")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7324():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7324)
    SetChrPos(0xFE, 202980, 0, 8390, 0)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xBB8, 0x0)
    OP_8E(0xFE, 0x32906, 0x0, 0x3228, 0xBB8, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_23_730E end

    def Function_24_7371(): pass

    label("Function_24_7371")

    SetChrChipByIndex(0xFE, 14)
    SetChrPos(0xFE, 202630, 0, 7280, 0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xFA0, 0x0)
    OP_8E(0xFE, 0x31B28, 0x0, 0x30F2, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_24_7371 end

    def Function_25_73C1(): pass

    label("Function_25_73C1")

    Sleep(500)
    SetChrChipByIndex(0xFE, 14)
    SetChrPos(0xFE, 202630, 0, 7280, 0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x318A8, 0x0, 0x2B02, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_25_73C1 end

    def Function_26_7402(): pass

    label("Function_26_7402")

    OP_31(0x3, 0x0, 0xD)
    OP_B5(0x3, 0x0)
    OP_B5(0x3, 0x1)
    OP_B5(0x3, 0x2)
    OP_B5(0x3, 0x3)
    OP_B5(0x3, 0x4)
    OP_41(0x3, 0x5C)
    OP_41(0x3, 0xF3)
    OP_41(0x3, 0x111)
    OP_41(0x3, 0x25B, 0x0)
    OP_41(0x3, 0x26A, 0x1)
    OP_41(0x3, 0x25E, 0x2)
    OP_35(0x3, 0xB4)
    OP_36(0x3, 0xF5)
    AddParty(0x3, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(14980, 200, 13030, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(45000, 0)
    OP_6E(484, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x101, 15)
    SetChrChipByIndex(0x102, 16)
    SetChrChipByIndex(0x103, 17)
    SetChrChipByIndex(0x104, 10)
    SetChrPos(0x101, 13130, 200, 10750, 0)
    SetChrPos(0x102, 14990, 200, 10750, 0)
    SetChrPos(0x103, 13190, 200, 13350, 180)
    SetChrPos(0x104, 14980, 200, 13350, 225)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 1)
    SetChrSubChip(0x104, 0)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(
        0x104,
        "金发青年",
        (
            "#030F#5P——重新做一下自我介绍。\x02\x03",
            "本人名为奥利维尔·朗海姆。\x01",
            "漂泊的诗人兼演奏家。\x02\x03",
            "正如你们所知，从埃雷波尼亚来，\x01",
            "到利贝尔王国进行巡回演出的旅行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#6P我叫艾丝蒂尔…… \x02\x03",
            "#005F喂、喂喂……\x01",
            "凭什么一定要自我介绍啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，方法姑且不论，\x01",
            "毕竟把那种场面和平解决了。\x02\x03",
            "啊，我的名字叫约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#3P我是雪拉扎德。\x02\x03",
            "刚才，我也是一时太冲动了，\x01",
            "多亏你出手收拾局面。\x02\x03",
            "不管怎样，在这里向你道谢了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#035F#5P呵呵，不必道谢哦。\x02\x03",
            "本人是爱与和平的热爱者，\x01",
            "那样做是理所当然的……\x02\x03",
            "但是，如果你一定要感谢的话，\x01",
            "那就请和本人约会一天吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F#3P我拒绝。\x01",
            "首先，没那个闲工夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#034F#5P真是太遗憾了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0)
    Sleep(100)
    SetChrSubChip(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#030F#5P那么作为补偿，\x01",
            "约修亚君你来怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F怎么会到我头上呢……\x02\x03",
            "请别开这种恶劣的玩笑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F#5P真意外呢。\x01",
            "我可不是在开玩笑哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F感觉更差了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#009F#6P你给我等一下。\x01",
            "为什么就不邀请我呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#033F#5P你？\x02\x03",
            "嗯～问题是你不仅长得有些抱歉，\x01",
            "而且也缺少女性魅力。\x02\x03",
            "#035F最好还是稍稍向这两位学习一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#005F#6P哼～～～！\x01",
            "没有女性魅力可真是对不起呀！\x02\x03",
            "再说，约修亚是个男孩子，\x01",
            "为什么要向他学习呢！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#014F冷、冷静点。\x01",
            "我一直都觉得艾丝蒂尔非常可爱。\x02\x03",
            "#017F不过，确实是……\x01",
            "缺少了点女性魅力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F#3P哎呀哎呀……\x02\x03",
            "#020F好了，正如刚才所说，\x01",
            "我们现在有很多事情要办。\x02\x03",
            "虽然很抱歉无法向你表达更多的谢意，\x01",
            "但是我们差不多该告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#5P嗯～那样的话……\x02\x03",
            "让本人也和你们一起去\x01",
            "那个叫柏斯的城市吧？\x02\x03",
            "不管怎么说，我也是初次来到王国。\x01",
            "就拜托你们做向导了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#3P好吧，只是这种小事的话，\x01",
            "我倒是没什么意见……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#009F#6P等等，雪拉姐！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#020F#1P只是做向导的话还好啦。\x01",
            "反正大家的目的地都一样嘛。\x02\x03",
            "而且做向导也是\x01",
            "游击士工作的一种哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P唉，没办法了。\x02\x03",
            "#003F可是可是，\x01",
            "万一那家伙向约修亚下毒手的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x102,
        "#014F喂喂，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#002F#6P约修亚，你别担心！\x02\x03",
            "就算发生了什么万一，\x01",
            "我也一定会保护你的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F我要担心什么呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F#5P真是的，把人家说得像禽兽似的。\x01",
            "下次再这样说人家可不依哦。\x02\x03",
            "#035F换个好听点的，\x01",
            "就叫我『爱情猎人』吧。\x02\x03",
            "『恋爱盗贼』也不错呢，嘻嘻……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 1)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#509F#6P你的脑子是不是进水了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#5P那么，\x01",
            "我们还是赶快向柏斯出发吧。\x02\x03",
            "就拜托你们几位带路了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P又在旁若无人地自说自唱……\x02\x03",
            "#005F喂，说你呢！\x01",
            "多少也要听听别人说的话呀！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18700, 0, 12270, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 18700, 0, 12267, 180)
    SetChrPos(0x102, 18700, 0, 12267, 180)
    SetChrPos(0x103, 18700, 0, 12267, 180)
    SetChrPos(0x104, 18700, 0, 12267, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x104, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    OP_0D()
    Return()

    # Function_26_7402 end

    def Function_27_83AA(): pass

    label("Function_27_83AA")

    OP_78(0x64, 0x78, 0x82)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_3F(0x32E, 1)
    OP_A2(0x32A)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_31(0x3, 0x0, 0xF)
    AddParty(0x3, 0xFF)
    OP_41(0x3, 0x5C)
    OP_41(0x3, 0xF3)
    OP_41(0x3, 0x111)
    OP_41(0x3, 0x25B, 0x0)
    OP_41(0x3, 0x26A, 0x1)
    OP_41(0x3, 0x25E, 0x2)
    SetChrPos(0x101, 109190, 0, -72940, 180)
    SetChrPos(0x102, 110080, 0, -71930, 180)
    SetChrPos(0x103, 108560, 0, -71890, 180)
    SetChrPos(0x104, 113220, 0, -74620, 225)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    SetChrPos(0xD, 108515, 0, -76468, 0)
    SetChrPos(0xE, 109535, 0, -76968, 0)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    OP_6D(102920, 0, -73120, 0)
    OP_67(0, 10460, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_6D(109920, 0, -73120, 3000)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#5P明天早上，\x01",
            "将军会亲自审问你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P如果你们确实无罪的话，\x01",
            "那么两三天之内就会被释放。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2P今晚就先呆在这儿，\x01",
            "让头脑稍微冷静一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    Sleep(1000)

    def lambda_85D2():
        OP_69(0x102, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_85D2)
    Sleep(500)
    OP_8C(0x102, 225, 400)
    OP_8C(0x103, 135, 400)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x0, 0x3)

    ChrTalk(
        0x101,
        (
            "#007F#4P唉……这真是天大的笑话。\x02\x03",
            "竟然连一句解释也不听\x01",
            "就把我们关在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P如果王国军能早日抓到空贼团，\x01",
            "我们的嫌疑就可以洗脱了吧。\x02\x03",
            "不过，要抓住他们也很难啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊，为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P还记得在废坑一战里\x01",
            "那个空贼头目说的话吗？\x02\x03",
            "就是『消息有误』，\x01",
            "还有『来得太早了吧』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#4P说起来，\x01",
            "他们的确说过这些话。\x02\x03",
            "#580F难、难道他们……\x01",
            "早就知道军队的行动！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P嗯，我想十有八九是这样。\x02\x03",
            "况且这还意味着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F#1P王国军内部有间谍。\x02\x03",
            "或者有人专门向\x01",
            "空贼提供军队的情报。\x02\x03",
            "#022F你想说的就是这个吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#2P是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#4P如、如果那是真的，\x01",
            "怪不得很难抓到他们啦！\x02\x03",
            "真是的，\x01",
            "我们还费那么大的力气去追捕他们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#522F#1P真是四处碰壁啊。\x02\x03",
            "这种时候，如果老师在的话，\x01",
            "会怎么应付这样的局面呢……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "青年的声音",
        (
            "呵呵呵……\x02\x03",
            "遇到什么麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#505F#4P咦……\x01",
            "约修亚，你在说话吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P不，我什么也没……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F#1P隔壁好像有人在说话。\x02\x03",
            "而且那声音，\x01",
            "听起来有点耳熟……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "青年的声音",
        (
            "讨厌啦，干嘛跟人家这么见外。\x01",
            "下次再这样说人家可不依哦。\x02\x03",
            "不过，一听到如此成熟艳丽的声音，\x01",
            "我就心领神会，知道是谁来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#509F#4P这、这么没根据的自信……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(
        0x102,
        "#017F#2P还有这种自我陶醉的口吻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F#1P难道隔壁那个人是……奥利维尔？\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)

    NpcTalk(
        0x104,
        "青年的声音",
        "Ｂｉｎｇｏ㈱\x02",
    )

    CloseMessageWindow()

    def lambda_8D96():
        OP_6D(111710, 0, -72760, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8D96)

    def lambda_8DAE():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8DAE)

    def lambda_8DBE():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_8DBE)

    def lambda_8DD6():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_8DD6)
    Sleep(1000)

    def lambda_8DEB():
        OP_8E(0xFE, 0x1ACFC, 0x0, 0xFFFEDC8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DEB)
    Sleep(500)

    def lambda_8E0B():
        OP_8E(0xFE, 0x1A9E6, 0x0, 0xFFFEDE3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E0B)
    Sleep(500)

    def lambda_8E2B():
        OP_8E(0xFE, 0x1AE46, 0x0, 0xFFFEE058, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E2B)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 135, 0)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 135, 0)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 135, 0)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x104,
        (
            "#031F#2P啊啊，\x01",
            "没想到我们会在这种地方邂逅……\x02\x03",
            "这就是空之女神的引导啊。\x01",
            "我们的命运果然是紧紧相连的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你、你……\x01",
            "你怎么会在这里？\x02\x03",
            "你明明应该在柏斯的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F而且还被别人\x01",
            "关在这个牢房里面……\x02\x03",
            "究竟发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2P呵～呵～\x01",
            "你们别像审犯那样问人家嘛。\x02\x03",
            "说起来，这可是一个\x01",
            "比山还高、比海还深的故事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F这样啊，那我们就不问了。\x02\x03",
            "直觉告诉我，\x01",
            "听你那所谓的故事肯定挺累人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F真巧啊，艾丝蒂尔。\x01",
            "我也恰好有同样的预感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F所以说\x01",
            "你最好还是不要告诉我们。\x02\x03",
            "也是为了我们的健康和美容着想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#2P哈·哈·哈。\x01",
            "你们就别这么见外嘛。\x02\x03",
            "#030F我这就向你们讲述……\x01",
            "这件发生在我身上的悲剧事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（真的不想听啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2P和你们分手之后……\x02\x03",
            "我先到超市转了一圈，\x01",
            "之后就进了『安特洛丝餐厅』。\x02\x03",
            "在品尝了各种美食之后，\x01",
            "我即兴弹起了钢琴。\x02\x03",
            "而餐厅负责人被我的表演所震撼，\x01",
            "感动得赞不绝口。\x02\x03",
            "之后，他还打算聘请我\x01",
            "做餐厅专门的钢琴演奏家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F真的会聘请你吗……\x01",
            "我记得，你好像是弹鲁特琴的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2P呵呵，真正的天才，\x01",
            "是会将所有乐器视为自己的朋友。\x02\x03",
            "#030F先不谈这个……\x01",
            "我可是提出了一个条件，\x01",
            "才会接受他们的聘请要求的。\x02\x03",
            "钱，我可以一分都不要，\x01",
            "不过，料理和葡萄酒都可以任我享用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说这种话……\x01",
            "还真是很像奥利维尔的风格。\x02\x03",
            "可是，为什么\x01",
            "你又会无缘无故地被关在这里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#2P啊啊，回想起来，\x01",
            "这还真是个听者泣、闻者泪的故事呢。\x02\x03",
            "那天夜晚……\x01",
            "主厨特意为我准备了奶油炒鸭肉，\x01",
            "味道嘛，还算过得去。\x02\x03",
            "还有特制的鸭血汤，\x01",
            "汤味比较浓，不过也还算差强人意。\x02\x03",
            "虽说有葡萄酒相伴，\x01",
            "不过说到底毕竟只是普通级数的货色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F我越来越想痛揍\x01",
            "这个不知足的家伙了……\x02\x03",
            "然后呢，你又吃了些什么好东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#2P然后我就打开了餐厅里的冰箱，\x01",
            "拿了一瓶貌似极品的葡萄酒。\x02\x03",
            "『格兰·夏利拿』１１８３年的经典杰作。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#024F『格兰·夏利拿』……\x01",
            "而且还是１１８３年的！？\x02\x03",
            "那不是王都的拍卖品吗？\x01",
            "被称为『幻之经典』的古典葡萄酒！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F#2P啊，看来雪拉小姐\x01",
            "对葡萄酒也蛮了解的嘛。\x02\x03",
            "#033F以前也只是听闻这酒非同一般而已，\x01",
            "没想到竟有机会能品尝到这酒中极品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F拍、拍卖品……\x01",
            "这东西可以值多少钱啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F据我所知……\x01",
            "至少需要５０万米拉才能买下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#005F５、５０万米拉～！？\x02\x03",
            "只是一瓶葡萄酒而已啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F物以稀为贵的世界啊……\x02\x03",
            "#018F奥利维尔，\x01",
            "难道你把那瓶葡萄酒给……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#2P呵呵，那还用说。\x01",
            "实在是美妙得令人难以忘怀。\x02\x03",
            "酒香入鼻、馥郁纯正。\x02\x03",
            "丝滑润喉、滋味芳醇。\x02\x03",
            "你们能理解吗？\x02\x03",
            "闪耀着动人蔷薇之色的时空中，\x01",
            "的确是存在这样的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F……不想听了………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F……果然听得很累………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#025F……已经震惊得无语了………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2P话说回来，美味倒是美味，\x01",
            "不过料理的分量始终还是太少了嘛。\x02\x03",
            "当我正打算叫主厨\x01",
            "再做点其他美味佳肴的时候，\x01",
            "餐厅的负责人刚好回来了。\x02\x03",
            "你也知道我为人相当豪爽。\x01",
            "本来打算叫他一起来品尝美酒佳肴，\x01",
            "没想到我向他劝酒的时候……\x02\x03",
            "负责人竟然暴跳如雷。\x02\x03",
            "还在我不知所措的瞬间，\x01",
            "叫了一大群士兵进来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, 100)

    ChrTalk(
        0x104,
        "#035F#2P……之后就……怎么说好呢………\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -56)

    ChrTalk(
        0x104,
        "#035F#2P……就是这样了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x104,
        (
            "#030F#2P以上，就是我会来到这里的原因。\x01",
            "一件充满血与泪的悲剧事件。\x02\x03",
            "#031F来吧！\x01",
            "对我的不幸遭遇表示一下同情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#500F……呼…呼………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F……嘶…嘶………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#025F……呼唔…傻瓜……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F#2P……………哎哟？\x02\x03",
            "#033F#2P等一下嘛你们……\x02\x03",
            "那个『呼』、『嘶』，\x01",
            "还有『呼唔，傻瓜』是什么意思嘛？\x02\x03",
            "#035F很好听吧？\x01",
            "故事的高潮才刚刚开始呢。\x02\x03",
            "我被带到这里之后，\x01",
            "等待我的是一场更加严酷的试炼……\x02\x03",
            "#036F喂喂——？\x01",
            "你们有没有听我说话？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(2000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    SetChrPos(0x101, 109190, 0, -72940, 180)
    SetChrPos(0x102, 110080, 0, -71930, 180)
    SetChrPos(0x103, 108560, 0, -71890, 180)
    SetChrPos(0x104, 113180, 0, -74620, 225)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 109535, 0, -76170, 0)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    OP_6D(109920, 0, -73120, 0)
    OP_67(0, 10460, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    ChrTalk(
        0xE,
        (
            "#4P喂！\x01",
            "你们几个，快起来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#1P唔……呼哇哇……\x02\x03",
            "嗯……我还要睡～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#1P怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F#1P哎呀……\x01",
            "一大早就来审问我们了？\x02\x03",
            "能不能让我们再睡会儿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4P不，正好相反。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4P你们被释放了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P啊……！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x10)
    FadeToBright(2000, 0)
    OP_0D()
    OP_8E(0xE, 0x1A0D8, 0x0, 0xFFFED694, 0x7D0, 0x0)
    OP_8C(0xE, 0, 400)
    Sleep(500)
    OP_22(0x6E, 0x0, 0x64)
    OP_72(0x3, 0x800)
    OP_70(0x3, 0x50)
    OP_73(0x3)
    OP_8E(0xE, 0x1A70C, 0x0, 0xFFFED676, 0x7D0, 0x0)
    OP_8C(0xE, 271, 400)

    ChrTalk(
        0x101,
        "#004F为、为什么这么快就……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F应该有什么理由吧……\x02",
    )

    CloseMessageWindow()
    OP_4A(0x10, 255)
    OP_4A(0xF, 255)
    SetChrChipByIndex(0xF, 5)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 102150, 0, -78020, 0)
    SetChrPos(0xF, 102150, 0, -76690, 0)
    SetChrFlags(0xF, 0x1)

    NpcTalk(
        0x10,
        "女性的声音",
        "#2P……就是因为有理由。\x02",
    )

    CloseMessageWindow()

    def lambda_A45C():
        OP_6D(108420, 0, -75290, 1500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A45C)
    OP_8C(0x101, 225, 400)
    OP_8C(0x102, 225, 400)
    OP_8C(0x103, 225, 400)

    def lambda_A489():
        OP_8E(0xFE, 0x19A8C, 0x0, 0xFFFECF3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A489)
    Sleep(600)

    def lambda_A4A9():
        OP_8E(0xFE, 0x1980C, 0x0, 0xFFFED46E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_A4A9)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 45, 400)
    WaitChrThread(0xF, 0x0)
    OP_8C(0xF, 90, 400)
    WaitChrThread(0x104, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#004F市、市长姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F哎呀呀。\x01",
            "没想到在这种地方再见面。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A581():
        OP_6D(106510, 0, -76720, 1500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A581)
    OP_43(0x101, 0x1, 0x0, 0x1D)
    OP_43(0x102, 0x1, 0x0, 0x1E)
    OP_43(0x103, 0x1, 0x0, 0x1F)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x10,
        (
            "#611F#4P给大家添麻烦了。\x02\x03",
            "不过请各位安心。\x01",
            "将军已经知道你们是清白的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F唔，不过这并不代表\x01",
            "我认同你们的所作所为……\x02\x03",
            "算了，既然是梅贝尔小姐亲自出面。\x01",
            "你们要谢就谢她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#5P嘿嘿，那样啊……\x02\x03",
            "原来是市长姐姐\x01",
            "救我们脱离了苦海。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F#4P也没那么夸张。\x02\x03",
            "我不过是将大家的实际情况\x01",
            "向摩尔根将军解释清楚而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P我们的实际情况……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F……你们两个。\x01",
            "我有句话要问你们。\x02\x03",
            "你们真的是\x01",
            "卡西乌斯·布莱特的孩子吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xF, 400)
    TurnDirection(0x102, 0xF, 400)
    TurnDirection(0x103, 0xF, 400)

    ChrTalk(
        0x101,
        "#004F#5P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F是的，正如将军所言。\x02\x03",
            "#010F她是艾丝蒂尔·布莱特……\x02\x03",
            "而我是养子约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F是啊……\x02\x03",
            "的确，小姑娘的样貌\x01",
            "颇有几分莱娜小姐的影子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F#5P！！！\x02\x03",
            "您认识我的妈妈！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F以前到你们家造访的时候，\x01",
            "我可是吃过好几顿你母亲煮的菜哦。\x02\x03",
            "#163F现在想想，\x01",
            "那还是你刚出生时的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#5P等、等一下……\x02\x03",
            "摩尔根将军\x01",
            "也认识我的老爸吗？\x02\x03",
            "虽然我知道\x01",
            "老爸以前是一名军人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F哼……自从那家伙做起游击士，\x01",
            "我就把他当作陌生人了。\x02\x03",
            "我认识的只有\x01",
            "身为军人的卡西乌斯。\x02\x03",
            "被称为『稀世的战略家』的卡西乌斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P战略家？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F真是的，不知道那家伙脑子想什么，\x01",
            "加入什么游击士协会……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0xF,
        (
            "#162F……啊啊！\x01",
            "一想起这件事就满肚子火！\x02\x03",
            "我先失陪了！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xF, 0xFF)

    def lambda_ABC1():

        label("loc_ABC1")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABC1")

    QueueWorkItem2(0x10, 1, lambda_ABC1)

    def lambda_ABD2():

        label("loc_ABD2")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABD2")

    QueueWorkItem2(0x101, 1, lambda_ABD2)

    def lambda_ABE3():

        label("loc_ABE3")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABE3")

    QueueWorkItem2(0x102, 1, lambda_ABE3)

    def lambda_ABF4():

        label("loc_ABF4")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_ABF4")

    QueueWorkItem2(0x103, 1, lambda_ABF4)
    OP_43(0xF, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_8E(0xE, 0x1A61C, 0x0, 0xFFFECFAA, 0xBB8, 0x0)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    Sleep(2000)
    OP_44(0x10, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)

    ChrTalk(
        0x101,
        "#007F#5P又、又怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 45, 400)

    ChrTalk(
        0x10,
        (
            "#611F呵呵……\x02\x03",
            "因为艾丝蒂尔的父亲\x01",
            "是一位非常优秀的军人。\x02\x03",
            "我听说在他退伍的时候，\x01",
            "摩尔根将军曾多次出面挽留他。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)
    TurnDirection(0x103, 0x10, 0)
    TurnDirection(0x102, 0x10, 0)

    ChrTalk(
        0x101,
        (
            "#008F#5P有、有这么一回事啊……\x02\x03",
            "听起来还真有点不可思议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F不过，这可是事实啊……\x02\x03",
            "将军这么不喜欢游击士，\x01",
            "也许就是因为这个原因吧。\x02\x03",
            "看着自己亲手栽培的部下退伍，\x01",
            "对将军来说的确很不是滋味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F说的也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#5P这么说，就是因为老爸得罪了别人，\x01",
            "才害我们白吃了这么多苦。\x02\x03",
            "#582F那、那个乱来的老爸～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F呵呵……\x02\x03",
            "#610F好了，事情总算解决了。\x01",
            "我们马上回柏斯好吗？\x02\x03",
            "既然定期船找到了，\x01",
            "那么事态肯定会迎来新的局面。\x02\x03",
            "我还有很多事情想和你们商量一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#5P啊，嗯……\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#613F哎呀，怎么了艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#505F#5P我非常赞成现在回去，\x01",
            "可是我们好像忘了些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F究竟是什么呢……？\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(400)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(3000)
    OP_1D(0x49)

    NpcTalk(
        0x104,
        "青年的声音",
        (
            "#3P啊啊……\x01",
            "人类果然是无情的生物。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_1F(0x64, 0x190)
    SetChrChipByIndex(0x104, 18)
    SetChrPos(0x104, 113250, 0, -74620, 180)

    def lambda_B172():
        OP_6D(109470, 0, -72760, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B172)

    def lambda_B18A():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_B18A)

    def lambda_B19A():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_B19A)

    def lambda_B1B2():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_B1B2)

    def lambda_B1C2():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B1C2)

    def lambda_B1D0():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1D0)

    def lambda_B1DE():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1DE)

    def lambda_B1EC():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B1EC)
    Sleep(3000)

    ChrTalk(
        0x104,
        (
            "#034F#5P如此轻易就将\x01",
            "与自己共度一夜的伙伴忘记……\x02\x03",
            "无言的悲剧……\x01",
            "悲哀的无奈啊……\x02\x03",
            "这样也好，就让我在这黑暗的炼狱里，\x01",
            "独身一人走向腐朽的彼方吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x104, 0x0, 0x0, 0x3)
    Sleep(2000)

    ChrTalk(
        0x101,
        "#509F#2P你想去就去吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#2P嗯……\x01",
            "完全忘了有这么一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P虽说很同情他，\x01",
            "不过怎么才能帮他呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#612F#2P那位先生……\x01",
            "难道就是传闻中的演奏家吗？\x02\x03",
            "毫不客气地品尝了\x01",
            "『格兰·夏利拿』的特别客人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x10)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x104, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x104, 225, 400)

    ChrTalk(
        0x104,
        (
            "#031F#5P呵呵，不敢当……\x02\x03",
            "话说回来，\x01",
            "小姐可能有些误会了。\x02\x03",
            "因为我已经预付了费用，\x01",
            "华丽的钢琴演奏可不是随便就能欣赏到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F#2P呵呵，听起来挺有趣的。\x02\x03",
            "算了，反正也是顺便的事情。\x01",
            "我刚才已经和将军打了招呼，\x01",
            "你也可以和他们一起离开这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#033F#5P哦……？\x02",
    )

    CloseMessageWindow()

    def lambda_B610():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B610)
    Sleep(100)

    def lambda_B623():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B623)
    Sleep(100)

    def lambda_B636():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B636)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#506F#2P连、连他也可以释放吗？\x01",
            "这样会不会有点勉强……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F#2P餐厅方面不用理会吗？\x01",
            "如果餐厅对他进行起诉怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F#2P呵呵……\x01",
            "餐厅方面你们不用担心。\x02\x03",
            "因为餐厅的拥有者\x01",
            "就是我梅贝尔本人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#611F#2P那瓶『格兰·夏利拿』\x01",
            "也是我之前竞投买下的东西。\x02\x03",
            "这样的话你们可以放心了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(1500, 0)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_83AA end

    def Function_28_B840(): pass

    label("Function_28_B840")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x192A3, 0x0, 0xFFFED3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x191CF, 0x0, 0xFFFEEEAB, 0xBB8, 0x0)
    OP_8E(0xFE, 0x18300, 0x7D0, 0xFFFEEDE9, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_B840 end

    def Function_29_B889(): pass

    label("Function_29_B889")

    OP_8E(0xFE, 0x1A216, 0x0, 0xFFFEE06C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A1B2, 0x0, 0xFFFED68A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x19DB6, 0x0, 0xFFFED432, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_29_B889 end

    def Function_30_B8CD(): pass

    label("Function_30_B8CD")

    Sleep(1000)
    OP_8E(0xFE, 0x1A216, 0x0, 0xFFFEE06C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A1B2, 0x0, 0xFFFED68A, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_30_B8CD end

    def Function_31_B902(): pass

    label("Function_31_B902")

    Sleep(500)
    OP_8E(0xFE, 0x1A216, 0x0, 0xFFFEE06C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A1B2, 0x0, 0xFFFED68A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1A20C, 0x0, 0xFFFED306, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_31_B902 end

    def Function_32_B94B(): pass

    label("Function_32_B94B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_32_B94B end

    SaveToFile()

Try(main)
