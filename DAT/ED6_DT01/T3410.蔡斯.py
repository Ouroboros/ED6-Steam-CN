from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3410   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3410.x',
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
        '迪鲁队长',                             # 9
        '士兵维恩',                             # 10
        '多杰',                                 # 11
        '拉德米拉',                             # 12
        '卡雷尔',                               # 13
        '士兵儒勒',                             # 14
        '士兵埃克托尔',                         # 15
        '士兵切斯利',                           # 16
        '阿鲁姆',                               # 17
        '艾娅莉',                               # 18
        '塔尔瓦托副长',                         # 19
        '桑吉特',                               # 20
        '黛米',                                 # 21
        '玛丽安',                               # 22
        '诺琪',                                 # 23
        '塔丽娅',                               # 24
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01140 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH02640 ._CH',             # 04
        'ED6_DT07/CH01300 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH01300 ._CH',             # 0A
        'ED6_DT07/CH01520 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
        'ED6_DT07/CH01213 ._CH',             # 0D
        'ED6_DT07/CH01233 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT07/CH00003 ._CH',             # 10
        'ED6_DT07/CH00013 ._CH',             # 11
        'ED6_DT07/CH02053 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01140P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH02640P._CP',             # 04
        'ED6_DT07/CH01300P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH01300P._CP',             # 0A
        'ED6_DT07/CH01520P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
        'ED6_DT07/CH01213P._CP',             # 0D
        'ED6_DT07/CH01233P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT07/CH00003P._CP',             # 10
        'ED6_DT07/CH00013P._CP',             # 11
        'ED6_DT07/CH02053P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 6790,
        Z                   = 0,
        Y                   = 2810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        TalkScenaIndex      = 21,
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
        TalkScenaIndex      = 20,
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
        TalkScenaIndex      = 19,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )


    DeclActor(
        TriggerX            = 58180,
        TriggerZ            = 5000,
        TriggerY            = 51630,
        TriggerRange        = 1000,
        ActorX              = 58180,
        ActorZ              = 6500,
        ActorY              = 51630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6760,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = 6790,
        ActorZ              = 1500,
        ActorY              = 2810,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 109850,
        TriggerZ            = 0,
        TriggerY            = 21800,
        TriggerRange        = 1000,
        ActorX              = 111940,
        ActorZ              = 1500,
        ActorY              = 22150,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 91680,
        TriggerZ            = 0,
        TriggerY            = -22240,
        TriggerRange        = 1000,
        ActorX              = 89560,
        ActorZ              = 1500,
        ActorY              = -22370,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3D2",          # 00, 0
        "Function_1_BD6",          # 01, 1
        "Function_2_C91",          # 02, 2
        "Function_3_CA7",          # 03, 3
        "Function_4_CCB",          # 04, 4
        "Function_5_CEF",          # 05, 5
        "Function_6_CF4",          # 06, 6
        "Function_7_1A1C",         # 07, 7
        "Function_8_1A1D",         # 08, 8
        "Function_9_1A1E",         # 09, 9
        "Function_10_1A1F",        # 0A, 10
        "Function_11_1C5E",        # 0B, 11
        "Function_12_1E5F",        # 0C, 12
        "Function_13_2AB3",        # 0D, 13
        "Function_14_38BF",        # 0E, 14
        "Function_15_4605",        # 0F, 15
        "Function_16_4B00",        # 10, 16
        "Function_17_4EF3",        # 11, 17
        "Function_18_4EF8",        # 12, 18
        "Function_19_5A6C",        # 13, 19
        "Function_20_5E01",        # 14, 20
        "Function_21_6034",        # 15, 21
        "Function_22_616A",        # 16, 22
        "Function_23_616F",        # 17, 23
        "Function_24_8FE7",        # 18, 24
        "Function_25_9131",        # 19, 25
        "Function_26_935E",        # 1A, 26
        "Function_27_9B1F",        # 1B, 27
    )


    def Function_0_3D2(): pass

    label("Function_0_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3DC")
    Jump("loc_475")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3FC")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2760, 0, 2290, 87)
    Jump("loc_475")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_406")
    Jump("loc_475")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_410")
    Jump("loc_475")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_41A")
    Jump("loc_475")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_424")
    Jump("loc_475")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_42E")
    Jump("loc_475")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_438")
    Jump("loc_475")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_442")
    Jump("loc_475")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_475")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18880, 0, 2680, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 17270, 0, 2680, 90)

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4FB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_586")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 89690, 0, -24010, 0)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_611")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 89690, 0, -24010, 0)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_697")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_71D")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_7A3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_82C")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 80890, 0, 23550, 110)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 82450, 0, 23660, 271)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8B5")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 80890, 0, 23550, 110)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 82450, 0, 23660, 271)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    Jump("loc_BD5")

    label("loc_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_993")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 17220, 0, 2570, 103)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 18530, 0, 2570, 249)
    Jump("loc_BD5")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A71")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 22840, 0, -3730, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 21050, 0, -3760, 90)
    Jump("loc_BD5")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_B26")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 89540, 0, -24220, 0)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 180)
    SetChrFlags(0x17, 0x10)
    Jump("loc_BD5")

    label("loc_B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BD5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 111940, 0, 22150, 283)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11620, 0, -1350, 259)
    OP_43(0x12, 0x0, 0x0, 0x3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54970, 0, -21440, 4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 61040, 0, -24890, 265)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 58600, 150, -27620, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 60840, 150, -27720, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 89560, 0, -22370, 98)

    label("loc_BD5")

    Return()

    # Function_0_3D2 end

    def Function_1_BD6(): pass

    label("Function_1_BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_BE5")
    OP_1B(0x0, 0x0, 0x19)
    Jump("loc_BEA")

    label("loc_BE5")

    OP_1B(0x1, 0x0, 0x18)

    label("loc_BEA")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0A")
    OP_65(0x0, 0x1)

    label("loc_C0A")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_C18")
    Jump("loc_C8B")

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_C22")
    Jump("loc_C8B")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C2C")
    Jump("loc_C8B")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_C36")
    Jump("loc_C8B")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_C40")
    Jump("loc_C8B")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_C4A")
    Jump("loc_C8B")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_C58")
    OP_64(0x2, 0x1)
    Jump("loc_C8B")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_C66")
    OP_64(0x2, 0x1)
    Jump("loc_C8B")

    label("loc_C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_C70")
    Jump("loc_C8B")

    label("loc_C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_C7A")
    Jump("loc_C8B")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C84")
    Jump("loc_C8B")

    label("loc_C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C8B")

    label("loc_C8B")

    OP_1C(0x5, 0x0, 0x1B)
    Return()

    # Function_1_BD6 end

    def Function_2_C91(): pass

    label("Function_2_C91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_C91")

    label("loc_CA6")

    Return()

    # Function_2_C91 end

    def Function_3_CA7(): pass

    label("Function_3_CA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CCA")
    OP_8D(0xFE, 5070, 820, 17900, -3880, 2000)
    Jump("Function_3_CA7")

    label("loc_CCA")

    Return()

    # Function_3_CA7 end

    def Function_4_CCB(): pass

    label("Function_4_CCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEE")
    OP_8D(0xFE, 56600, -23980, 64040, -26210, 2000)
    Jump("Function_4_CCB")

    label("loc_CEE")

    Return()

    # Function_4_CCB end

    def Function_5_CEF(): pass

    label("Function_5_CEF")

    Call(0, 6)
    Return()

    # Function_5_CEF end

    def Function_6_CF4(): pass

    label("Function_6_CF4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D76")

    ChrTalk(
        0x8,
        (
            "武术大会平安无事地结束了，\x01",
            "但是恐怖分子会在诞辰庆典时\x01",
            "发动袭击也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不要松懈，\x01",
            "继续保持高度警戒吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_E25")

    ChrTalk(
        0x8,
        (
            "我听说情报部的特务部队\x01",
            "似乎聚集了一批\x01",
            "能力相当强的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "仔细想想的话，\x01",
            "有调集那么多精英部队\x01",
            "到情报部去的必要吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_E25")

    OP_A2(0xF)

    ChrTalk(
        0x8,
        (
            "我听说情报部的特务部队\x01",
            "似乎聚集了一批\x01",
            "能力相当强的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "仔细想想的话，\x01",
            "有调集那么多精英部队\x01",
            "到情报部去的必要吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然不是我应该深究的事，\x01",
            "不过最近有很多现象让我在意……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F19")

    Jump("loc_1A18")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_FD0")

    ChrTalk(
        0x8,
        (
            "上面下达了\x01",
            "再次强化警备体制的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "情报部好像还没有\x01",
            "确定恐怖分子的行踪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1077")

    ChrTalk(
        0x8,
        (
            "我们圣海姆的守备队\x01",
            "也接到了不准接近\x01",
            "艾尔贝离宫的命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我觉得其实也不用特意强调嘛。\x01",
            "那是我们管辖区之外的地方，\x01",
            "根本就没想要去靠近那里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_1077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1114")

    ChrTalk(
        0x8,
        (
            "关于蔡斯事件的调查，\x01",
            "好像由情报部出马了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "交给理查德上校的话，\x01",
            "肯定能像柏斯的空贼那样，\x01",
            "把恐怖分子一网打尽吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_1114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_11BE")

    ChrTalk(
        0x8,
        (
            "刚才误会你们了，\x01",
            "实在是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，快到诞辰庆典了，\x01",
            "盘查行动是\x01",
            "绝对不能放松的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_1334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1246")

    ChrTalk(
        0x8,
        (
            "绝对不能让\x01",
            "犯人们入侵王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "紧张的日子还会再持续下去，\x01",
            "请你们再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1331")

    label("loc_1246")

    OP_A2(0xF)
    OP_4A(0x12, 255)

    ChrTalk(
        0x12,
        (
            "队长，\x01",
            "先前的命令已经向士兵们传达了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我向他们发出了\x01",
            "在避免不必要的纠纷的同时\x01",
            "严格盘查来往人员的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很好，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "紧张的日子还会再持续下去，\x01",
            "现在是不能松懈的时期。\x01",
            "请你们再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)

    label("loc_1331")

    Jump("loc_1A18")

    label("loc_1334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_14AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(
        0x8,
        (
            "绝对不能让\x01",
            "罪犯们入侵王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "紧张的日子还会再持续下去，\x01",
            "请你们再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A7")

    label("loc_13BC")

    OP_A2(0xF)
    OP_4A(0x12, 255)

    ChrTalk(
        0x12,
        (
            "队长，\x01",
            "先前的命令已经向士兵们传达了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我向他们发出了\x01",
            "在避免不必要的纠纷的同时\x01",
            "严格盘查来往人员的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很好，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "紧张的日子还会再持续下去，\x01",
            "现在是不能松懈的时期。\x01",
            "请你们再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)

    label("loc_14A7")

    Jump("loc_1A18")

    label("loc_14AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_156E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1517")

    ChrTalk(
        0x8,
        (
            "……对我来说，\x01",
            "盘查解除的命令完全不能理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是命令就是命令。\x01",
            "就是这么一回事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156B")

    label("loc_1517")

    OP_A2(0xF)

    ChrTalk(
        0x8,
        "……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我现在很忙。\x01",
            "有问题的话去找其他士兵吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_156B")

    Jump("loc_1A18")

    label("loc_156E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1625")

    ChrTalk(
        0x8,
        (
            "只有这个是最重要的事。\x01",
            "王国军正规的搜查\x01",
            "不久就要开始了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "到那个时候\x01",
            "犯人就会变成瓮中之鳖了。\x01",
            "所以在这之前还是先忍耐吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1710")

    label("loc_1625")

    OP_A2(0xF)

    ChrTalk(
        0x8,
        (
            "现在，来往的旅行者\x01",
            "在确认身份之前是不能通过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "理由不用说你们也明白吧。\x01",
            "就是因为蔡斯发生了恐怖事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为了不让犯人从蔡斯逃跑，\x01",
            "王国军也是尽了全力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1710")

    Jump("loc_1A18")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "是这样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如何建立当情况紧急时\x01",
            "能快速和王都取得联络的体制\x01",
            "是关键所在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1834")

    label("loc_1795")

    OP_A2(0xF)

    ChrTalk(
        0x8,
        (
            "哦？你们有什么事？\x01",
            "对不起，我现在正忙于公务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "除非有急事，\x01",
            "否则还是去问别的士兵吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1834")

    Jump("loc_1A18")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_18F9")

    ChrTalk(
        0x8,
        (
            "现在随时都可能\x01",
            "会向游击士协会请求帮助……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可是那边的人手也是有限的。\x01",
            "不能抱太大希望。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_18F9")

    OP_A2(0xF)

    ChrTalk(
        0x8,
        (
            "圣海姆门守备队的使命，\x01",
            "首先就是城门的警备工作，\x01",
            "但同时也必须确保街道的安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "马上就到女王的诞辰庆典了。\x01",
            "那时候旅行者的人数也会激増吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个时候如果出现了凶暴的魔兽，\x01",
            "该怎么对付才好呢……\x01",
            "现在必须要好好想想了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A18")

    TalkEnd(0x8)
    Return()

    # Function_6_CF4 end

    def Function_7_1A1C(): pass

    label("Function_7_1A1C")

    Return()

    # Function_7_1A1C end

    def Function_8_1A1D(): pass

    label("Function_8_1A1D")

    Return()

    # Function_8_1A1D end

    def Function_9_1A1E(): pass

    label("Function_9_1A1E")

    Return()

    # Function_9_1A1E end

    def Function_10_1A1F(): pass

    label("Function_10_1A1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A2C")
    Jump("loc_1C5A")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1AB6")

    ChrTalk(
        0xFE,
        (
            "太好了，\x01",
            "终于可以按照预定计划返回王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为啊，\x01",
            "想和她一起逛的地方还有很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B30")

    label("loc_1AB6")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "呼，太好了。\x01",
            "结束盘查的时间比我想象得还要早。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "现在已经没有危险了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样就可以\x01",
            "按照预定计划返回王都了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B30")

    Jump("loc_1C5A")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(
        0xFE,
        (
            "冷……冷静点！\x01",
            "无论发生什么事也要临危不惧啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C46")

    label("loc_1B76")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "听说蔡斯那边\x01",
            "发生了什么大事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为盘查，\x01",
            "现在都不能回王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但、但是，\x01",
            "在这种时候我更要保持冷静。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 270, 400)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "亲爱的……\x01",
            "我、我一定会保护你的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C46")

    Jump("loc_1C5A")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1C53")
    Jump("loc_1C5A")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C5A")

    label("loc_1C5A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A1F end

    def Function_11_1C5E(): pass

    label("Function_11_1C5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1C6B")
    Jump("loc_1E5B")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1D57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(
        0xFE,
        (
            "返回王都以后，\x01",
            "就该到女王的诞辰庆典了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，真是期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D54")

    label("loc_1CCD")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "啊，太好了。\x01",
            "好像又恢复正常了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "盘查的时候，\x01",
            "士兵们给人的感觉好可怕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这时我会比平时\x01",
            "更加娇气地依靠着他哦㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D54")

    Jump("loc_1E5B")

    label("loc_1D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1DF2")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "阿鲁姆有些过于激动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，稍微有点不可靠\x01",
            "也是他的魅力所在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E47")

    label("loc_1DF2")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "唉，又出事了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然都不是大事，\x01",
            "可最近全都是这样的消息啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E47")

    Jump("loc_1E5B")

    label("loc_1E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1E54")
    Jump("loc_1E5B")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E5B")

    label("loc_1E5B")

    TalkEnd(0xFE)
    Return()

    # Function_11_1C5E end

    def Function_12_1E5F(): pass

    label("Function_12_1E5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F10")

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "关所接到的命令\x01",
            "基本上都是由情报部发出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是因为理查德上校成为了\x01",
            "公爵的辅佐的缘故吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_1F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1FB3")

    ChrTalk(
        0xFE,
        (
            "有关女王陛下的病情，\x01",
            "陛下自己没有发表任何声明，\x01",
            "这一点让人在意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典\x01",
            "到底会怎么样呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_1FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2037")

    ChrTalk(
        0xFE,
        (
            "正在举行的武术大会\x01",
            "好像还平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能像这样\x01",
            "一切顺利结束就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_20B7")

    ChrTalk(
        0xFE,
        (
            "如果和游击士协会合作的话，\x01",
            "追查恐怖分子的行动\x01",
            "应该会更加有把握吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但实现起来还是很困难啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2161")

    ChrTalk(
        0xFE,
        (
            "刚才从格兰赛尔那边\x01",
            "来了个身材非常高大的\x01",
            "共和国人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说是要参加武术大会，\x01",
            "来这里是为了\x01",
            "做一下热身运动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_21C8")

    ChrTalk(
        0xFE,
        (
            "刚才真是\x01",
            "对不住各位了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但这也是我的工作。\x01",
            "希望你们能理解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_21C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_2325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(
        0xFE,
        (
            "逃亡中的犯人\x01",
            "现在处境应该也很艰难吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在不能松懈这一点上，\x01",
            "他们倒是和我们一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2322")

    label("loc_2238")

    OP_A2(0xF)
    OP_4A(0x8, 255)

    ChrTalk(
        0xFE,
        (
            "队长，\x01",
            "先前的命令已经向士兵们传达了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我向他们发出了\x01",
            "在避免不必要的纠纷的同时\x01",
            "严格盘查来往人员的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很好，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "紧张的日子还会再持续下去，\x01",
            "现在是不能松懈的时期。\x01",
            "请你们再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)

    label("loc_2322")

    Jump("loc_2AAF")

    label("loc_2325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2395")

    ChrTalk(
        0xFE,
        (
            "逃亡中的犯人\x01",
            "现在处境应该也很艰难吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在不能松懈这一点上，\x01",
            "他们倒是和我们一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_2395")

    OP_A2(0xF)
    OP_4A(0x8, 255)

    ChrTalk(
        0xFE,
        (
            "队长，\x01",
            "先前的命令已经向士兵们传达了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我向他们发出了\x01",
            "在避免不必要的纠纷的同时\x01",
            "严格盘查来往人员的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "很好，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "紧张的日子还会再持续下去，\x01",
            "现在是不能松懈的时期。\x01",
            "请你们再加把劲。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)

    label("loc_247F")

    Jump("loc_2AAF")

    label("loc_2482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2615")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2549")

    ChrTalk(
        0xFE,
        (
            "一定是军队的上层\x01",
            "得到了什么決定性的重要情报，\x01",
            "所以才会认为盘查也没有用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么想的话，就能说明一切了。\x01",
            "不管能不能理解……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2612")

    label("loc_2549")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "……解除盘查\x01",
            "是军队总部的正式命令。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的责任就是服从命令，\x01",
            "而不是去判断那个命令是否正确。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，今后仍然还是要\x01",
            "继续保持警戒的方针。\x01",
            "为了预防万一嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2612")

    Jump("loc_2AAF")

    label("loc_2615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_26F9")

    ChrTalk(
        0xFE,
        (
            "游击士协会也有所行动，\x01",
            "可还是没能抓住犯人的踪迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对手可是光天化日就敢\x01",
            "明目张胆袭击中央工房的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果不早一点抓到的话……\x02",
    )

    CloseMessageWindow()
    Jump("loc_276D")

    label("loc_26F9")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "实在对不起，\x01",
            "现在要对通行者进行盘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是为了阻止\x01",
            "恐怖分子逃亡而采取的措施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "无论如何请大家理解。\x02",
    )

    CloseMessageWindow()

    label("loc_276D")

    Jump("loc_2AAF")

    label("loc_2770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_287C")

    ChrTalk(
        0xFE,
        (
            "『亚宁堡』长城\x01",
            "一共设置了两个关所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个圣海姆门和\x01",
            "洛连特那边的格鲁纳门\x01",
            "都是保护王都的绝对防线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对我们守备队来说，\x01",
            "无论是多么平静的一天，\x01",
            "也不应该有懈怠的时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295F")

    label("loc_287C")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "唔，女王的诞辰庆典马上就到了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有必要提前训练一下\x01",
            "有大量旅客时的警备体制呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赶快向迪鲁队长\x01",
            "请示一下训练的实施计划吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295F")

    Jump("loc_2AAF")

    label("loc_2962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2A30")

    ChrTalk(
        0xFE,
        (
            "从里面的楼梯上去，\x01",
            "就可以到『亚宁堡』的\x01",
            "城墙上面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为是利用了原来的遗迹建成的，\x01",
            "所以里面的走廊稍微有些复杂。\x01",
            "这也是没办法的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2A30")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "啊，你们是来参观的吗？\x01",
            "有问题的话请尽管提出来，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要在我的解答范围之内\x01",
            "我都会尽力回答的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAF")

    TalkEnd(0xFE)
    Return()

    # Function_12_1E5F end

    def Function_13_2AB3(): pass

    label("Function_13_2AB3")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                               # 0
            "买东西\x01",                             # 1
            "欢迎品尝「终极肉火锅」700米拉\x01",      # 2
            "离开\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2C")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x4A)
    OP_56(0x0)
    TalkEnd(0x13)
    Return()

    label("loc_2B2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C32")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BF8")
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
            "终极肉火锅\x07\x00",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_2BBD")
    Jump("loc_2BEA")

    label("loc_2BBD")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "终极肉火锅\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEA")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_2C20")

    label("loc_2BF8")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_2C20")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x13)
    Return()

    label("loc_2C32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4C")
    FadeToBright(300, 0)
    TalkEnd(0x13)
    Return()

    label("loc_2C4C")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2CDD")

    ChrTalk(
        0xFE,
        (
            "无论再忙，\x01",
            "饭也是必须要好好吃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好～为了士兵们，\x01",
            "我要仔细制订\x01",
            "确保营养的特别菜单！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2D62")

    ChrTalk(
        0xFE,
        (
            "黛米那家伙\x01",
            "不知还在哪里偷懒呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，算了。\x01",
            "现在客人也不多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_2D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2DFF")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "这个时间还是休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又进了不少材料，\x01",
            "考虑一下新的菜式吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_2DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2EB1")

    ChrTalk(
        0xFE,
        (
            "武术大会开始以后，\x01",
            "基本上没有通行的旅客了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为有士兵在，\x01",
            "倒不是完全没有客人来，\x01",
            "不过还是有些寂寞啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_2EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_308B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2F6F")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚才来用餐的那个巨汉\x01",
            "也吃得好香呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看他吃的样子，都把我感动了。\x01",
            "不由自主地就给他的餐费打了折。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3088")

    label("loc_2F6F")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "如果客人觉得美味，\x01",
            "我会很高兴哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也一直在\x01",
            "钻研烹饪技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才来用餐的那个巨汉\x01",
            "也吃得好香呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看他吃的样子，都把我感动了。\x01",
            "不由自主地就给他的餐费打了折。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3088")

    Jump("loc_38BB")

    label("loc_308B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_31AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_30C6")
    TurnDirection(0x13, 0x10E, 400)

    ChrTalk(
        0xFE,
        (
            "学者先生，\x01",
            "您的研究也要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AA")

    label("loc_30C6")

    OP_A2(0xA)
    TurnDirection(0x13, 0x10E, 400)

    ChrTalk(
        0xFE,
        (
            "咦，\x01",
            "你不就是刚才的那个客人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F哦，\x01",
            "刚才真的是承蒙关照了，\x01",
            "非常感谢您啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没什么没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的手艺不怎么样，\x01",
            "你也能吃得那么香。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还要感谢你呢。\x01",
            "您的研究也要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AA")

    Jump("loc_38BB")

    label("loc_31AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_3276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3220")

    ChrTalk(
        0xFE,
        (
            "请问客人们\x01",
            "是要去格兰赛尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真好啊，\x01",
            "我也想去诞辰庆典玩呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3273")

    label("loc_3220")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也可以当作休息室，\x01",
            "请随便坐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3273")

    Jump("loc_38BB")

    label("loc_3276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_32D0")

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也可以当作休息室，\x01",
            "请随便坐吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_32D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_340B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_335F")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "说起来还没听说\x01",
            "已经抓到犯人了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "盘查就这样解除了，\x01",
            "这么做好吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3408")

    label("loc_335F")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "啊～欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "盘查解除得比预想还要早……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，我是无所谓。\x01",
            "但是捜査那边没问题吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3408")

    Jump("loc_38BB")

    label("loc_340B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3476")

    ChrTalk(
        0xFE,
        "但是，竟然敢袭击中央工房。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那些人也真是胆大包天。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3584")

    label("loc_3476")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "事情好像变得很严重了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在能做的事就是\x01",
            "给不能外出的人们\x01",
            "做出美味的食物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果就那么饿着肚子的话，\x01",
            "人就会越发脆弱了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "填饱肚子的话，\x01",
            "心情也会愉快的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3584")

    Jump("loc_38BB")

    label("loc_3587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_37B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3662")

    ChrTalk(
        0xFE,
        (
            "这里需要直接面对客人。\x01",
            "所以任何时候都要全力以赴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～说起来，\x01",
            "黛米那家伙到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "稍微偷懒一下倒没关系，\x01",
            "但是也要看时候吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AE")

    label("loc_3662")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "我年轻的时候，目标是经营一流的餐厅。\x01",
            "但是随着实际工作的展开，\x01",
            "想法也开始改变了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就这样一直\x01",
            "在这个食堂工作也很好啊。\x01",
            "我现在就是这么想的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里能直接面对客人不是吗？\x01",
            "从客人的反应马上就会知道\x01",
            "饭菜是好吃还是难吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以任何时候都要全力以赴。\x01",
            "想要提高烹饪水平的话，\x01",
            "这里确实是最佳地点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AE")

    Jump("loc_38BB")

    label("loc_37B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3878")

    ChrTalk(
        0xFE,
        (
            "这里现有的材料也就这么多了，\x01",
            "没办法作出丰富的菜式来……\x01",
            "只好用烹饪技术来弥补这一不足了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有机会的话你们也来尝尝看吧。\x01",
            "料理的好坏不是用价格衡量的。\x01",
            "希望你们也能明白这一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_3878")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请随便坐吧。\x02",
    )

    CloseMessageWindow()

    label("loc_38BB")

    TalkEnd(0xFE)
    Return()

    # Function_13_2AB3 end

    def Function_14_38BF(): pass

    label("Function_14_38BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_392C")

    ChrTalk(
        0xFE,
        (
            "最近士兵们\x01",
            "好像都很忙哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，看不到我中意的人，\x01",
            "真是好无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4601")

    label("loc_392C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_39D4")

    ChrTalk(
        0xFE,
        (
            "有时我觉得\x01",
            "严厉的人也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有真的关心对方\x01",
            "才会如此严格要求，\x01",
            "不是吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AA6")

    label("loc_39D4")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "这么考虑的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有温柔\x01",
            "果然还是不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时我觉得\x01",
            "严厉的人也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有真的关心对方\x01",
            "才会如此严格要求，\x01",
            "不是吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA6")

    Jump("loc_4601")

    label("loc_3AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3B63")

    ChrTalk(
        0xFE,
        "是吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "桑吉特先生\x01",
            "又随便给人打折了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他人确实挺不错的，\x01",
            "不过没办法成为有钱人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4601")

    label("loc_3B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3BEE")

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "这个时间比较无聊，\x01",
            "要不要去找妈妈玩呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "在旅馆帮忙也很无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C83")

    label("loc_3BEE")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "现在这个时间， \x01",
            "士兵们都在工作，无聊死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "要不要去找妈妈玩呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "在旅馆帮忙也很无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C83")

    Jump("loc_4601")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3D3E")

    ChrTalk(
        0xFE,
        (
            "刚才有一个\x01",
            "像熊一样的大哥哥来了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他的食量好惊人，\x01",
            "看得我真是佩服啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "桑吉特先生\x01",
            "又给他打了折，\x01",
            "这样下去会亏本的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4601")

    label("loc_3D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_3DC6")

    ChrTalk(
        0xFE,
        (
            "桑吉特先生\x01",
            "一看到客人吃得开心，\x01",
            "马上就会给客人打折。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这家店，\x01",
            "真的能赚钱吗……\x01",
            "我真是担心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4601")

    label("loc_3DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_3EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3E43")

    ChrTalk(
        0xFE,
        (
            "刚才来的那个客人\x01",
            "光点便宜的菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此，\x01",
            "桑吉特先生也给他打折了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC6")

    label("loc_3E43")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "刚才来的那个客人\x01",
            "光点便宜的菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此，\x01",
            "桑吉特先生也给他打折了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他的心肠也太好了……\x02",
    )

    CloseMessageWindow()

    label("loc_3EC6")

    Jump("loc_4601")

    label("loc_3EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_404B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3F9B")

    ChrTalk(
        0xFE,
        (
            "以前觉得\x01",
            "欧鲁尼斯先生挺普通的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过不知道为什么，\x01",
            "最近觉得他变帅了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道……\x01",
            "是交了女朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，如果是那样的话，\x01",
            "真是可惜啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4048")

    label("loc_3F9B")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "马上就到士兵们来吃饭的时间了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "守卫王都那一侧的欧鲁尼斯先生\x01",
            "最近也很帅哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……\x01",
            "他们赶快来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4048")

    Jump("loc_4601")

    label("loc_404B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_41E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_414B")

    ChrTalk(
        0xFE,
        (
            "进行盘查时的士兵们\x01",
            "比平时要帅多了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "儒勒先生和埃克托尔先生\x01",
            "就算是被调到亲卫队\x01",
            "我也不会觉得奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "穿上亲卫队制服的儒勒先生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "光是想象我都要燃烧了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E2")

    label("loc_414B")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "太好了，\x01",
            "又恢复平时的体制了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "儒勒先生他们在盘查时\x01",
            "认真的样子也很帅哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "这就是男人的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E2")

    Jump("loc_4601")

    label("loc_41E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4317")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4277")

    ChrTalk(
        0xFE,
        (
            "果然恋人就是要\x01",
            "在任何时候都可以依靠的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么考虑的话，\x01",
            "士兵就是我理想的恋人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4314")

    label("loc_4277")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "蔡斯发生的事件真是太可怕了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，这种非常时刻\x01",
            "有强者在旁边的话就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……\x01",
            "士兵们果然很了不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4314")

    Jump("loc_4601")

    label("loc_4317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_43EC")

    ChrTalk(
        0xFE,
        (
            "桑吉特先生是个好人，\x01",
            "就是性格有点怪，不能当我恋爱对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不深入交往是不可能了解\x01",
            "一个人原本的性格的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "一开始只能凭外表来选择了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_446E")

    label("loc_43EC")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "我说，\x01",
            "妈妈觉得儒勒先生\x01",
            "和埃克托尔先生哪个比较好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "儒勒先生\x01",
            "虽然人长得帅，\x01",
            "但是有些过于严厉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446E")

    Jump("loc_4601")

    label("loc_4471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4565")

    ChrTalk(
        0xFE,
        (
            "男人就是要看外表呢。\x01",
            "在所有士兵中，儒勒先生是最帅的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后就是埃克托尔先生……\x01",
            "副长先生也还不错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "剩下的就不在我考虑范围内了。  \x02",
    )

    CloseMessageWindow()
    Jump("loc_4601")

    label("loc_4565")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "马上就到士兵们来吃饭的时间了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……\x01",
            "儒勒先生，快点来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4601")

    TalkEnd(0xFE)
    Return()

    # Function_14_38BF end

    def Function_15_4605(): pass

    label("Function_15_4605")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4612")
    Jump("loc_4AFC")

    label("loc_4612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_46BA")

    ChrTalk(
        0xFE,
        "盘查好像解除了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是\x01",
            "已经抓到犯人了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是如果是这样，\x01",
            "《利贝尔通讯》又没有报道……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AFC")

    label("loc_46BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4891")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_476F")

    ChrTalk(
        0xFE,
        (
            "在柏斯旅行的时候\x01",
            "遇到了空贼团的事件，\x01",
            "不能乘坐定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "女神爱德丝心情不太好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488E")

    label("loc_476F")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "刚才军队的人\x01",
            "说明了盘查的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们两个本来就是格兰赛尔的市民，\x01",
            "所以还好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是很多旅行者\x01",
            "在确认身份之前都不能离开呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说到底就是因为\x01",
            "发生了恐怖袭击事件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_488E")

    Jump("loc_4AFC")

    label("loc_4891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4940")

    ChrTalk(
        0xFE,
        (
            "在像安特洛丝餐厅\x01",
            "那样的一流饭店用餐，\x01",
            "享受高级服务虽然很棒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过偶尔来这种有个性的地方\x01",
            "体会一下新鲜感也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A37")

    label("loc_4940")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "其实这个食堂\x01",
            "也有着很好的风评呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里有其他地方\x01",
            "品尝不到的特殊风味的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在像安特洛丝餐厅那样的一流饭店\x01",
            "享受高级服务虽然很棒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过偶尔来这种有个性的地方\x01",
            "体会一下新鲜感也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A37")

    Jump("loc_4AFC")

    label("loc_4A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4AFC")

    ChrTalk(
        0xFE,
        (
            "我们是从王都那边\x01",
            "来艾尔贝周游道散步的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾尔贝周游道\x01",
            "气氛相当优雅恬静，\x01",
            "简直像花园中的庭院小路呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "建议你们去王都的时候\x01",
            "也到那里散散步。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFC")

    TalkEnd(0xFE)
    Return()

    # Function_15_4605 end

    def Function_16_4B00(): pass

    label("Function_16_4B00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4B0D")
    Jump("loc_4EEF")

    label("loc_4B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4C01")

    ChrTalk(
        0xFE,
        (
            "太好了。\x01",
            "看起来好像恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是这么早\x01",
            "就停止了盘查，\x01",
            "不会影响搜查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我是外行，\x01",
            "不过还是有点担心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EEF")

    label("loc_4C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4C8B")

    ChrTalk(
        0xFE,
        (
            "最近一段时间\x01",
            "连续发生了很多大事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "暂时还是不要到处旅行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D10")

    label("loc_4C8B")

    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "真是很可怕啊。\x01",
            "这次又是在蔡斯发生了恐怖活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近一段时间，\x01",
            "连续发生了很多大事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "希望只是不幸的偶然……\x02",
    )

    CloseMessageWindow()

    label("loc_4D10")

    Jump("loc_4EEF")

    label("loc_4D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4DD2")

    ChrTalk(
        0xFE,
        (
            "听说这是食堂独创的菜式，\x01",
            "我本来没有报什么期待的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过吃过之后觉得还挺不错。\x01",
            "想尝尝其他的菜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E83")

    label("loc_4DD2")

    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "这里的饭菜还真是好吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以利贝尔料理为基础，\x01",
            "其中隐藏着的东方香料\x01",
            "将味道提升至极致……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然是食堂独创的菜式，\x01",
            "但真的是美味的料理啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E83")

    Jump("loc_4EEF")

    label("loc_4E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4EEF")

    ChrTalk(
        0xFE,
        (
            "我家先生啊，\x01",
            "从来都不回家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在王都呆着除了无聊的事，\x01",
            "也没有其他事可干了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EEF")

    TalkEnd(0xFE)
    Return()

    # Function_16_4B00 end

    def Function_17_4EF3(): pass

    label("Function_17_4EF3")

    Call(0, 18)
    Return()

    # Function_17_4EF3 end

    def Function_18_4EF8(): pass

    label("Function_18_4EF8")

    TalkBegin(0x17)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F58")
    OP_0D()
    OP_A9(0x49)
    OP_56(0x0)
    TalkEnd(0x17)
    Return()

    label("loc_4F58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F69")
    TalkEnd(0x17)
    Return()

    label("loc_4F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_500B")

    ChrTalk(
        0x17,
        (
            "士兵们也一直都保持着紧张状态，\x01",
            "难道他们不累吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "不过，那是他们的工作。\x01",
            "累也没办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_500B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5098")

    ChrTalk(
        0x17,
        (
            "这孩子也别絮絮叨叨了，\x01",
            "早点交个男朋友，\x01",
            "给我带来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "她年纪也不小了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_5098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5119")

    ChrTalk(
        0x17,
        (
            "这个孩子每天\x01",
            "都要来说这些话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "这么明目张胆地偷懒\x01",
            "很容易被开除的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_5119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_51A5")

    ChrTalk(
        0x17,
        (
            "用餐时间结束了，\x01",
            "食堂那边\x01",
            "也该闲下来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "我预感到那孩子该来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_51A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_523F")

    ChrTalk(
        0x17,
        (
            "今天天气不错。\x01",
            "晒床单的话应该很快就能干吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "如果在『亚宁堡』上晒衣服\x01",
            "会干得很快吧……\x01",
            "但是队长肯定会生气的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_523F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_52F3")

    ChrTalk(
        0x17,
        (
            "在这里工作，\x01",
            "就算自己不愿意，\x01",
            "也不得不听士兵们谈话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "像什么恐怖分子啦，袭击什么的，\x01",
            "那些讨厌的事情都会听到，\x01",
            "弄得心情都很不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_52F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_5433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5366")

    ChrTalk(
        0x17,
        (
            "之前一段时间\x01",
            "来这里的人很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "不过现在大家\x01",
            "都已经出发去王都了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5430")

    label("loc_5366")

    OP_A2(0xE)

    ChrTalk(
        0x17,
        "啊～欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "之前一段时间\x01",
            "来这里的人很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "不过现在大家\x01",
            "都已经出发去王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "因为武术大会就要开始了嘛。\x01",
            "他们急切的心情我很理解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5430")

    Jump("loc_5A68")

    label("loc_5433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_5529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_54D4")

    ChrTalk(
        0x17,
        (
            "其他的客人\x01",
            "都已经去王都了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "因为武术大会就要开始了嘛。\x01",
            "他们急切的心情我很理解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5526")

    label("loc_54D4")

    OP_A2(0xE)

    ChrTalk(
        0x17,
        "啊～欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "其他的客人\x01",
            "都已经去王都了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5526")

    Jump("loc_5A68")

    label("loc_5529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_563B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_558E")

    ChrTalk(
        0x17,
        (
            "虽然有些不能理解， \x01",
            "不过一定是军队里发生了什么吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5638")

    label("loc_558E")

    OP_A2(0xE)

    ChrTalk(
        0x17,
        (
            "虽然不太明白，\x01",
            "但是盘查已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "队长先生好像\x01",
            "也不能理解这件事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "他也不知道理由吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5638")

    Jump("loc_5A68")

    label("loc_563B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_57C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_56E1")

    ChrTalk(
        0x17,
        (
            "中央工房被袭击了，\x01",
            "确实是不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "盘查也好怎么也好，\x01",
            "赶快把犯人抓住吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57C4")

    label("loc_56E1")

    OP_A2(0xE)

    ChrTalk(
        0x17,
        (
            "不管怎么说，\x01",
            "这可是非同一般的案件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "早点抓住犯人结束盘查虽然很好，\x01",
            "但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "本来被禁止外出的客人\x01",
            "已经做好住宿的准备了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57C4")

    Jump("loc_5A68")

    label("loc_57C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_593E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_581F")

    ChrTalk(
        0x17,
        "……话说回来，黛米。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "你在这种地方\x01",
            "偷懒没关系吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_593B")

    label("loc_581F")

    OP_A2(0xE)

    ChrTalk(
        0x17,
        (
            "如果是我的话，\x01",
            "就会盯住厨师桑吉特呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "他只会认真工作，\x01",
            "对女人没兴趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "虽然他缺乏情趣，\x01",
            "不过讲信用才是结婚的第一前提呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "抛开这个不说，\x01",
            "他也是个很会听别人说话的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_593B")

    Jump("loc_5A68")

    label("loc_593E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_598E")

    ChrTalk(
        0x17,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "怎么？想休息吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_598E")

    OP_A2(0xE)

    ChrTalk(
        0x17,
        (
            "啊，\x01",
            "欢迎来到圣海姆门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "这里是旅行者专用的住宿设施。\x01",
            "任何人都可以放心使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "旁边有个食堂，\x01",
            "我的女儿就在那里工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "如果方便的话，也到那边光顾一下吧。\x01",
            "那里的饭菜有着不错的评价呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A68")

    TalkEnd(0x17)
    Return()

    # Function_18_4EF8 end

    def Function_19_5A6C(): pass

    label("Function_19_5A6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D65")
    OP_A2(0x583)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找结晶回路碎片的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "接下来要去格兰赛尔了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "不，去蔡斯。\x01",
            "因为在格兰赛尔卖了些东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈说要用那些米拉\x01",
            "买些导力器回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿，老妈也开始知道\x01",
            "什么东西才是有价值的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F怎么样都好啦。\x01",
            "你还是老样子，那么自大傲慢呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是吗？我觉得自己 \x01",
            "只不过是说了理所当然的话而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那再见吧。\x01",
            "老这么乱逛的话，\x01",
            "老妈又要唠叨了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFD")

    label("loc_5D65")


    ChrTalk(
        0xFE,
        (
            "格兰赛尔这城市\x01",
            "果然很厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家看起来都很有钱，\x01",
            "我们带来的商品都很顺利地卖出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来要去蔡斯\x01",
            "购入一些导力器制品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFD")

    TalkEnd(0xFE)
    Return()

    # Function_19_5A6C end

    def Function_20_5E01(): pass

    label("Function_20_5E01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 2)), scpexpr(EXPR_END)), "loc_5EC5")

    ChrTalk(
        0xFE,
        (
            "格兰赛尔的确是个好地方。\x01",
            "我们的民间手工艺品也很畅销哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赚够了本钱，\x01",
            "就可以去进一些\x01",
            "导力器制品了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6030")

    label("loc_5EC5")

    OP_A2(0x582)

    ChrTalk(
        0xFE,
        (
            "格兰赛尔的确是个好地方。\x01",
            "不愧是被称为王都的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家的钱包都是鼓鼓的，\x01",
            "我们的民间手工艺品也很畅销哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既然已经赚够了本钱，\x01",
            "就可以去进一些\x01",
            "导力器制品了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果把导力器拿回共和国去卖，\x01",
            "会赚一大笔钱的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6030")

    TalkEnd(0xFE)
    Return()

    # Function_20_5E01 end

    def Function_21_6034(): pass

    label("Function_21_6034")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_6166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_607B")

    ChrTalk(
        0xFE,
        (
            "哎呀～去王都的飞艇坪\x01",
            "就是接下来的期待所在了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6166")

    label("loc_607B")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "想到难得有这样的机会，\x01",
            "回共和国的时候\x01",
            "还是乘坐定期船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正准备去\x01",
            "格兰赛尔的国际空港。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，旅费有限，\x01",
            "到王都这段路还是走着去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6166")

    TalkEnd(0xFE)
    Return()

    # Function_21_6034 end

    def Function_22_616A(): pass

    label("Function_22_616A")

    Call(0, 23)
    Return()

    # Function_22_616A end

    def Function_23_616F(): pass

    label("Function_23_616F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8564")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 7450, 0, 880, 0)
    SetChrPos(0x102, 6480, 0, 880, 0)
    OP_6D(7630, 200, 2180, 0)
    OP_8C(0x9, 180, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5P你们好。\x01",
            "欢迎来到圣海姆门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P是来办理\x01",
            "去王都的通行手续的吗？\x02",
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
            "【办理通行手续】\x01",      # 0
            "【还是算了】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_62B4"),
        (1, "loc_6340"),
        (SWITCH_DEFAULT, "loc_6375"),
    )


    label("loc_62B4")

    OP_B7(0xD, 0x1)
    AddParty(0xD, 0xFF)
    SetChrFlags(0x10E, 0x80)
    TurnDirection(0x9, 0x102, 0)
    SetChrPos(0x101, 7450, 0, 880, 0)
    SetChrPos(0x102, 6480, 0, 880, 0)

    ChrTalk(
        0x101,
        (
            "#006F嗯，是的。\x01",
            "请问现在可以办理吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P可以，请过来吧。\x01",
            "在这张单子上签个名就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6375")

    label("loc_6340")


    ChrTalk(
        0x9,
        (
            "#5P我知道了。\x01",
            "准备好的话请告诉我一声。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    label("loc_6375")

    OP_A2(0x606)
    OP_28(0x54, 0x1, 0x20)
    OP_28(0x2A, 0x4, 0x40)
    OP_28(0x2D, 0x4, 0x40)
    OP_28(0x2E, 0x4, 0x40)
    OP_28(0x2F, 0x4, 0x40)
    OP_28(0x30, 0x4, 0x40)
    OP_28(0x31, 0x4, 0x40)
    OP_28(0x34, 0x4, 0x40)
    OP_1B(0x0, 0x0, 0x19)
    OP_1B(0x1, 0x0, 0xFFFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "在手续单据上填写了必要的事项。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "#5P不过话说回来，\x01",
            "最近的孩子也真是的……\x01",
            "该说你们前卫呢还是胆大什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P特地沿着街道远足过来，\x01",
            "你们两个是在约会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎！？\x02\x03",
            "#503F约、约会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，不是这样的。\x02\x03",
            "别看我们这样，其实我们是兄妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P哎～一点也不像，\x01",
            "不过姓氏确实一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P好了，这样通行手续就办完了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#582F………呜………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔……？\x02\x03",
            "从刚才开始你的样子就不对劲，\x01",
            "是不是哪里不舒服了？\x02\x03",
            "还是休息一下比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F啊～～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#007F没事没事，\x01",
            "我真的没关系啦。\x02\x03",
            "加快脚步去王都吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那样的话就好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P不过，如果不是约会的话，\x01",
            "是不是去参观武术大会呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_670D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_670D)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#004F哎，武术大会……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P什么嘛，又没猜中吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P武术大会就是\x01",
            "在王都的『王立竞技场』举行的、\x01",
            "每年一次的比武格斗盛会啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P以王国军队的精锐为首，\x01",
            "各地的武术强人齐聚一堂，\x01",
            "在大会上以武术一较高下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P今天下午\x01",
            "就开始举行预选赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎～真是有意思啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，\x01",
            "是艾丝蒂尔你喜欢的事情嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P按照女王陛下的意愿，\x01",
            "今年的门票也打折了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P啊啊，要不是为了值勤，\x01",
            "我也想跑过去看看啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊哈哈，真是不巧啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F不过，我们与其光去参观，\x01",
            "倒不如直接参加还好呢。\x02\x03",
            "还可以检验一下自己的修行成果。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F确实……\x02\x03",
            "不过今天已经开始进行预选了，\x01",
            "应该不能再参加了吧。\x02\x03",
            "而且还要完成委托，\x01",
            "有余闲的话去看看就算了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F嘁，真可惜啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_6AF5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AF5)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#501F嗯？士兵先生？\x02\x03",
            "你怎么了？\x01",
            "这样盯着我们看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P你胸前那个徽章……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P因为你们太年轻了，所以才没注意到。\x01",
            "……你们难道是游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯，是又怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P不，那个……\x01",
            "该说是问题呢还是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P算了……\x01",
            "怎么想都不可能……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13070, 0, 4800, 0)
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_6C3B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C3B)

    def lambda_6C49():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C49)

    def lambda_6C57():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C57)

    def lambda_6C65():
        OP_6D(8280, 0, 2380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C65)
    OP_4A(0x8, 255)
    OP_8E(0x8, 0x30AC, 0x0, 0xB5E, 0x7D0, 0x0)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "……喂。\x01",
            "值勤的时候不要自言自语的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x2670, 0x0, 0x852, 0x7D0, 0x0)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x9,
        "#1P啊，队长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "怎么，有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P这两个人好像是……\x01",
            "……游击士……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F？？？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 400)

    ChrTalk(
        0x8,
        "啊，我说你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "能不能稍微耽误你们一点时间？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎～？\x01",
            "可是我们现在要赶去王都啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦……是去王都啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "作为参考，\x01",
            "我能问问你们去那里做什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F哎、哎？\x01",
            "那个是……被委托的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "工作的内容呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，博士的……\x02\x03",
            "#003F……不对！\x01",
            "唔，该怎么说呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F这位队长，非常抱歉。\x01",
            "游击士协会有明文规定。\x02\x03",
            "委托人的隐私是不能随便透露出去的。\x01",
            "希望您能够体谅我们工作的难处。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯……这可真是可疑啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "看起来，\x01",
            "有必要问你们一些事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F到底是怎么回事，\x01",
            "我完全不明白……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "#1P那个，实际上……\x01",
            "军队本部传达下来了命令。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_705B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_705B)

    def lambda_7069():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7069)

    ChrTalk(
        0x9,
        (
            "#1P说王室亲卫队背叛了女王陛下，\x01",
            "还在各地掀起恐怖事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P而且，好像其中还有\x01",
            "伪装成游击士进行活动的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P正因如此，\x01",
            "需要对自称游击士的人进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#3S你，你说什么！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "喂，不要说多余的话。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "虽然很对不起，\x01",
            "但这是军队上面的命令。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7219():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7219)

    def lambda_7227():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7227)

    ChrTalk(
        0x8,
        (
            "在证实身份之前，\x01",
            "请你们暂时留在这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F别、别开玩笑了。\x01",
            "为什么我们非要听你们……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10E, 0x80)
    SetChrPos(0x10E, 21410, 0, -620, 0)

    NpcTalk(
        0x10E,
        "男性的声音",
        (
            "#3P啊啊！\x01",
            "你们终于来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7325():

        label("loc_7325")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_7325")

    QueueWorkItem2(0x101, 1, lambda_7325)

    def lambda_7336():

        label("loc_7336")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_7336")

    QueueWorkItem2(0x8, 1, lambda_7336)

    def lambda_7347():

        label("loc_7347")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_7347")

    QueueWorkItem2(0x9, 1, lambda_7347)

    def lambda_7358():
        OP_8E(0xFE, 0x242C, 0x0, 0x118, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_7358)
    OP_6D(8990, 0, 2340, 2000)

    ChrTalk(
        0x101,
        "#004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F你是……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x1)

    ChrTalk(
        0x10E,
        (
            "#130F#2P哎呀～真是让我等了很久啊。\x01",
            "　\x02\x03",
            "如果办完了通行手续，\x01",
            "那就马上继续前往王都吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎、哎、哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_7427():
        OP_8E(0xFE, 0x1EB4, 0x0, 0xFFFFFE84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7427)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x10E, 400)

    ChrTalk(
        0x102,
        (
            "#010F真是抱歉，教授。\x02\x03",
            "签证的时候遇到点麻烦，\x01",
            "所以可能要等一阵子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "等、等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……那个，您是哪位……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x8, 400)

    ChrTalk(
        0x10E,
        (
            "#130F啊，抱歉，我忘了说。\x01",
            "我是考古学家亚鲁瓦。\x02\x03",
            "诺桑普里亚自治州出身，\x01",
            "是来利贝尔王国进行研究调查的。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x8, 0x9, 400)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "对了……\x01",
            "这个人办完通行手续了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P啊，是的，就在刚才……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P护照是真的，\x01",
            "而且王都的历史资料馆\x01",
            "可以为这位先生做身份保证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是吗……\x01",
            "这样就没有问题了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x10E, 400)

    ChrTalk(
        0x8,
        "失敬了，亚鲁瓦先生。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x8, 400)

    ChrTalk(
        0x8,
        (
            "请问一下，\x01",
            "你是怎么认识这两位的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F啊，他们是游击士嘛。\x02\x03",
            "之前好几次从危险的地方把我救出来，\x01",
            "是我的救命恩人呢。\x02\x03",
            "正因为如此，\x01",
            "这次就请了他们护送我去王都。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(
        0x10E,
        (
            "#130F#2P对吧？\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77EA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77EA)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#004F哎……啊，没错！\x02\x03",
            "#506F实、实际上就是这样～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "算了……\x01",
            "这样的话就有身份保证了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "真是抱歉，\x01",
            "刚才误会你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嗯、嗯，明白了就好～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你们也是因职务所在才这样做，\x01",
            "请不要放在心上。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(59550, 200, -27280, 0)
    OP_6B(2800, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x10E, 0x4)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 17)
    SetChrChipByIndex(0x10E, 18)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 1)
    SetChrPos(0x10E, 59680, 200, -26270, 180)
    SetChrPos(0x101, 58630, 200, -27770, 90)
    SetChrPos(0x102, 59690, 200, -28910, 0)
    SetChrFlags(0x14, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#009F真是的～\x01",
            "不要吓我好不好。\x02\x03",
            "教授就不说了，\x01",
            "连约修亚也立刻就接上话了。\x02\x03",
            "在那一刻我还以为自己\x01",
            "真的是忘记了约定好的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F哈哈，才不是这样……\x02\x03",
            "#010F逢场作戏这种事情，\x01",
            "应该立刻就要想到才行嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哼。\x01",
            "理解力不好真是抱歉啊。\x02\x03",
            "#003F自己都没察觉到一件很重要的事情，\x01",
            "还说人家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哎……你刚才说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F什么都没说～啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F#5P哈哈，真是不好意思。\x01",
            "刚才好像让你吃惊了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    Sleep(50)
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x10E,
        (
            "#130F#5P看见你们好像遇到了点麻烦，\x01",
            "就过去帮帮忙……\x02\x03",
            "是不是让你感到为难了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊，没关系。\x01",
            "#006F确实遇到了点麻烦。\x02\x03",
            "谢谢，亚鲁瓦教授。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F刚才真是多亏您出手相救。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F#5P没什么没什么。\x01",
            "就当作是以前帮助我的还礼吧。\x02\x03",
            "#131F不过……\x01",
            "怎么又和军队的人争执起来了？\x02\x03",
            "我刚才听见什么恐怖活动之类的话。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F最近，好像有一伙犯罪分子\x01",
            "伪装成他人发动骚乱和袭击。\x02\x03",
            "看起来……\x01",
            "我们大概是被误认为是那伙人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F对对，肯定是这样。\x01",
            "真是让人火冒三丈啊。\x02\x03",
            "果然军队里还是蛮横的人多啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#131F#5P啊，还真是不走运呢。\x02\x03",
            "在『红莲之塔』发生的那件事是绑架事件，\x01",
            "这我也听说了……\x02\x03",
            "对了，那件事情已经解决了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯、嗯……\x02\x03",
            "虽然从根本上来说还留下不少问题，\x01",
            "不过也可以说已经解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F#5P啊，真是后生可畏啊。\x02\x03",
            "第一次见面的时候，\x01",
            "我就觉得你们两个肯定能成为\x01",
            "会闯出一番事业的游击士呢。\x02\x03",
            "嗯嗯……\x01",
            "看来我没有看走眼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F讨、讨厌啦～\x01",
            "就算这么夸奖我们，也没有奖励给你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F哈哈，我们还在修行中呢。\x02\x03",
            "#010F话说回来……\x01",
            "教授为什么会来这种地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F#5P当然是在去王都的途中了。\x01",
            "　\x02\x03",
            "本来想乘坐定期船的，\x01",
            "可是又心疼花这点无谓的钱……\x02\x03",
            "反正，考古学家的体力就是生命，\x01",
            "就当成是锻炼脚力吧……\x02\x03",
            "#131F……哈哈哈……呼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F没、没有必要\x01",
            "把自己逼到这种地步吧……\x02\x03",
            "不过，你看起来还是老样子，\x01",
            "依旧过着清贫的生活呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F#5P文科系学者的钱包都是一样的呢。\x01",
            "　\x02\x03",
            "特别是考古学，\x01",
            "一得到钱立刻就花在发掘上面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真是没办法。\x02\x03",
            "#006F不过，先不说这个了……\x01",
            "能在这里见面还真是有缘啊。\x02\x03",
            "难得再次相见，\x01",
            "教授就和我们一起去王都吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F等、等一下，艾丝蒂尔。\x02\x03",
            "还不知道亚鲁瓦教授的安排呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F#5P我很赞成哦。\x02\x03",
            "街道上可能会有魔兽，\x01",
            "和你们两个在一起能壮胆呢。\x02\x03",
            "而且从这里到王都距离也不是很远了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样的话……\x01",
            "就请您多多指教了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F那么就决定了。\x02\x03",
            "目标王都，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x10E, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10E, 65535)
    SetChrPos(0x101, 61550, 0, -21950, 0)
    SetChrPos(0x102, 61550, 0, -21950, 0)
    SetChrPos(0x10E, 61550, 0, -21950, 0)
    ClearChrFlags(0x14, 0x80)
    OP_6D(61550, 0, -21950, 0)
    OP_6B(2600, 0)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_8FE3")

    label("loc_8564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_86DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_85F5")

    ChrTalk(
        0x9,
        (
            "虽然通过这里的人数减少了，\x01",
            "不过还有恐怖分子的隐患。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "还是老样子，\x01",
            "非常警戒体制还要持续下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86DB")

    label("loc_85F5")

    OP_A2(0x8)

    ChrTalk(
        0x9,
        (
            "观看完武术大会，\x01",
            "然后在诞辰庆典之前\x01",
            "一直留在王都里的人会有很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然通过这里的人数减少了，\x01",
            "不过还有恐怖分子的隐患。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "还是老样子，\x01",
            "非常警戒体制还要持续下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86DB")

    Jump("loc_8FE3")

    label("loc_86DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8799")

    ChrTalk(
        0x9,
        (
            "大会的决赛好像是\x01",
            "特务部队和游击士的对阵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "特务部队有那么多强人，\x01",
            "应该会获得优胜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FE3")

    label("loc_8799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_880F")

    ChrTalk(
        0x9,
        (
            "从今天开始， \x01",
            "原定的训练全部停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "与此同时关所\x01",
            "处在紧张警戒之中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FE3")

    label("loc_880F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_888F")

    ChrTalk(
        0x9,
        (
            "从今天开始终于到了\x01",
            "武术大会的正式赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "王国军的选手们\x01",
            "也要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FE3")

    label("loc_888F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_89F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_892B")

    ChrTalk(
        0x9,
        (
            "虽然没有亲眼\x01",
            "见到过理查德上校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过看过利贝尔通讯的\x01",
            "采访报道之后，\x01",
            "我就完全成为他的支持者了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89F6")

    label("loc_892B")

    OP_A2(0x8)

    ChrTalk(
        0x9,
        (
            "虽然没有亲眼\x01",
            "见到过理查德上校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过看过利贝尔通讯的\x01",
            "采访报道之后，\x01",
            "我就完全成为他的支持者了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他的见解犀利，\x01",
            "头脑又好，真是好帅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89F6")

    Jump("loc_8FE3")

    label("loc_89F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_8B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8AB3")

    ChrTalk(
        0x9,
        (
            "最近在艾尔贝周游道\x01",
            "好像也有士兵在巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果诞辰庆典上发生恐怖活动，\x01",
            "受害会相当大的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B4E")

    label("loc_8AB3")

    OP_A2(0x8)

    ChrTalk(
        0x9,
        (
            "啊，是你们。\x01",
            "刚才很抱歉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "通行手续已经办好了，\x01",
            "你们可以去王都了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那么，祝旅行愉快。\x02",
    )

    CloseMessageWindow()

    label("loc_8B4E")

    Jump("loc_8FE3")

    label("loc_8B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_8B5B")
    Jump("loc_8FE3")

    label("loc_8B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8B65")
    Jump("loc_8FE3")

    label("loc_8B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_8C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8BAE")

    ChrTalk(
        0x9,
        (
            "直到最后我们也不知道，\x01",
            "到底是为了什么而盘查的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C0D")

    label("loc_8BAE")

    OP_A2(0x8)

    ChrTalk(
        0x9,
        (
            "突然，\x01",
            "盘查就下令被解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "犯人明明还没有抓到啊。\x01",
            "这到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C0D")

    Jump("loc_8FE3")

    label("loc_8C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_8D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8C98")

    ChrTalk(
        0x9,
        (
            "为了抓住恐怖事件的犯人\x01",
            "才开始实行盘查的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对不起，\x01",
            "现在不能这么轻易地就发行通行许可证。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D51")

    label("loc_8C98")

    OP_A2(0x8)

    ChrTalk(
        0x9,
        (
            "呼，\x01",
            "本来今天预定有训练的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过因为发生了恐怖事件，\x01",
            "所以进入了紧急状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对不起，\x01",
            "现在不能这么轻易地就发行通行许可证。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D51")

    Jump("loc_8FE3")

    label("loc_8D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_8DD4")

    ChrTalk(
        0x9,
        (
            "哟，\x01",
            "欢迎你们来到圣海姆门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "请各位好好体会一下\x01",
            "『亚宁堡』的威严哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FE3")

    label("loc_8DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8F00")

    ChrTalk(
        0x9,
        (
            "这里虽然是负责办理通往王都手续的关所，\x01",
            "但同时也是一座历史遗迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就算在定期船开始运营之后，\x01",
            "来参观的人也有很多哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为马上就是女王的诞辰庆典了，\x01",
            "我想通过这里的人也会变得更多吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FE3")

    label("loc_8F00")

    OP_A2(0x8)

    ChrTalk(
        0x9,
        "欢迎来到圣海姆门。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里虽然是负责办理通往王都手续的关所，\x01",
            "但同时也是一座历史遗迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就算在定期船开始运营之后，\x01",
            "来参观的人也有很多哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FE3")

    TalkEnd(0x9)
    Return()

    # Function_23_616F end

    def Function_24_8FE7(): pass

    label("Function_24_8FE7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_903E")

    ChrTalk(
        0x106,
        (
            "#050F这边是格兰赛尔吗……\x02\x03",
            "……现在没有去王都的必要呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9115")

    label("loc_903E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90B1")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#010F前面就是格兰赛尔地区了。\x02\x03",
            "没有通行许可证的话，\x01",
            "是不能从这边出去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9115")

    label("loc_90B1")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F前面就是格兰赛尔地区了。\x02\x03",
            "没有通行许可证的话，\x01",
            "是不能从这边出去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9115")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_24_8FE7 end

    def Function_25_9131(): pass

    label("Function_25_9131")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91BE")

    ChrTalk(
        0x104,
        (
            "#030F唔，\x01",
            "这边是往蔡斯的出口吗……\x02\x03",
            "可能什么时候会到那里探访，\x01",
            "但现在还不是时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9342")

    label("loc_91BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_924E")

    ChrTalk(
        0x108,
        (
            "#073F哦，\x01",
            "这边是通往其他地区的出口。\x02\x03",
            "被士兵缠上就麻烦了。\x01",
            "还是乖乖地回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9342")

    label("loc_924E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9264")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_926B")

    label("loc_9264")

    TurnDirection(0x102, 0x0, 400)

    label("loc_926B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_92EA")

    ChrTalk(
        0x102,
        (
            "#012F现在关所被封锁了。\x02\x03",
            "士兵们也在巡逻，\x01",
            "我们还是早点回去比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9342")

    label("loc_92EA")


    ChrTalk(
        0x102,
        (
            "#010F这边是蔡斯地区。\x02\x03",
            "我们还没取得许可证，\x01",
            "是不能从这边出去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9342")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_25_9131 end

    def Function_26_935E(): pass

    label("Function_26_935E")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(57670, 5000, 52610, 0)
    SetChrPos(0x101, 57160, 5000, 52610, 133)
    SetChrPos(0x102, 58440, 5000, 53220, 189)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93B7")
    SetChrPos(0x107, 57140, 5000, 51520, 103)

    label("loc_93B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93D6")
    SetChrPos(0x106, 57290, 5000, 53600, 134)

    label("loc_93D6")

    OP_0D()
    OP_64(0x0, 0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "发现了一个油纸包。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "里面放着\x07\x02",
            "３１棵丝柏树\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x345, 1)
    OP_28(0x30, 0x1, 0x4)

    ChrTalk(
        0x101,
        (
            "#508F好啊！\x01",
            "找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这是最后一本了……\x02\x03",
            "图书管理员的任务总算是完成了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是啊，好长的任务啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F……………………咦？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_954A")

    def lambda_9542():
        TurnDirection(0x107, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9542)

    label("loc_954A")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F唔，\x01",
            "书里面夹着一张卡片。\x02\x03",
            "……啊，上面写了些什么东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "　辛苦你了。\x01",
            "　虽然不知道你是谁，\x01",
            "　但总算是摸索到这里了。\x01",
            "　\x01",
            "　简单做一下自我介绍。\x01",
            "　我是结晶回路的研究员，\x01",
            "　也就是隐藏三本书的犯人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "　我希望把自己的作品\x01",
            "　托付给那些聪明的人们，\x01",
            "　这就是为何会出现谜语的原因……\x01",
            "　对于你出色的表现，我会给予奖励。\x01",
            "　\x01",
            "　奖品结晶回路和这封信附在一起。\x01",
            "　请注意查收包裹内部。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "　那么，就多谢你们的配合了。\x01",
            "　我制作的这个结晶回路\x01",
            "　一定会对你很有用的。\x01",
            "　\x01",
            "　另：找到这本书的朋友，\x01",
            "　　　还请把它归还到\x01",
            "　　　中央工房二楼的资料室。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#007F………………读完了。\x02\x03",
            "#505F呼～\x01",
            "这好像不是单纯的恶作剧呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_997E")
    TurnDirection(0x107, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9939")

    ChrTalk(
        0x107,
        "#060F嗯，好像是～呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F要调查一下这个包裹吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_997B")

    label("loc_9939")


    ChrTalk(
        0x107,
        "#060F好像是～呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F要调查一下这个包裹吗？\x02",
    )

    CloseMessageWindow()

    label("loc_997B")

    Jump("loc_99BB")

    label("loc_997E")


    ChrTalk(
        0x102,
        (
            "#010F是啊。\x02\x03",
            "……要调查一下这个包裹吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99BB")


    ChrTalk(
        0x101,
        (
            "#004F哦，对了，\x01",
            "这里面会是……嗯。\x02",
        )
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
            "得到了\x07\x02",
            "妨害３\x07\x00",
            "的结晶回路。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        "#001F呵呵呵，真的有呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还是拿给委托人确认一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好的。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x2C3, 1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AEB")

    def lambda_9ADC():
        OP_92(0x107, 0x101, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9ADC)

    label("loc_9AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B0E")

    def lambda_9AFF():
        OP_92(0x106, 0x101, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_9AFF)

    label("loc_9B0E")

    OP_92(0x102, 0x101, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    Return()

    # Function_26_935E end

    def Function_27_9B1F(): pass

    label("Function_27_9B1F")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_27_9B1F end

    SaveToFile()

Try(main)
