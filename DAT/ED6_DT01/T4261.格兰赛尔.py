from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4261   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4261.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '玛多克工房长',                         # 9
        '理查德上校',                           # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '雪拉扎德',                             # 13
        '雷沃尔',                               # 14
        '妮舒',                                 # 15
        '提妲',                                 # 16
        '拉赛尔',                               # 17
        '塔罗牌',                               # 18
        '塔罗牌',                               # 19
        '塔罗牌',                               # 20
        '塔罗牌',                               # 21
        '塔罗牌',                               # 22
        '塔罗牌',                               # 23
        '塔罗牌',                               # 24
        '阿加特',                               # 25
        '金',                                   # 26
        '奥利维尔',                             # 27
        '玻璃杯',                               # 28
        '瓶子',                                 # 29
        '瓶子',                                 # 30
        '瓶子',                                 # 31
        '瓶子',                                 # 32
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
        'ED6_DT07/CH02623 ._CH',             # 00
        'ED6_DT07/CH02030 ._CH',             # 01
        'ED6_DT07/CH02460 ._CH',             # 02
        'ED6_DT07/CH02230 ._CH',             # 03
        'ED6_DT07/CH02240 ._CH',             # 04
        'ED6_DT07/CH02140 ._CH',             # 05
        'ED6_DT07/CH02470 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
        'ED6_DT07/CH01570 ._CH',             # 08
        'ED6_DT07/CH01350 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH00060 ._CH',             # 0B
        'ED6_DT07/CH02020 ._CH',             # 0C
        'ED6_DT07/CH02033 ._CH',             # 0D
        'ED6_DT07/CH00003 ._CH',             # 0E
        'ED6_DT07/CH00013 ._CH',             # 0F
        'ED6_DT07/CH02620 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT07/CH00023 ._CH',             # 12
        'ED6_DT06/CH20021 ._CH',             # 13
        'ED6_DT06/CH20133 ._CH',             # 14
        'ED6_DT07/CH00053 ._CH',             # 15
        'ED6_DT07/CH00073 ._CH',             # 16
        'ED6_DT07/CH00030 ._CH',             # 17
        'ED6_DT06/CH20020 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH02623P._CP',             # 00
        'ED6_DT07/CH02030P._CP',             # 01
        'ED6_DT07/CH02460P._CP',             # 02
        'ED6_DT07/CH02230P._CP',             # 03
        'ED6_DT07/CH02240P._CP',             # 04
        'ED6_DT07/CH02140P._CP',             # 05
        'ED6_DT07/CH02470P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
        'ED6_DT07/CH01570P._CP',             # 08
        'ED6_DT07/CH01350P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH00060P._CP',             # 0B
        'ED6_DT07/CH02020P._CP',             # 0C
        'ED6_DT07/CH02033P._CP',             # 0D
        'ED6_DT07/CH00003P._CP',             # 0E
        'ED6_DT07/CH00013P._CP',             # 0F
        'ED6_DT07/CH02620P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT07/CH00023P._CP',             # 12
        'ED6_DT06/CH20021P._CP',             # 13
        'ED6_DT06/CH20133P._CP',             # 14
        'ED6_DT07/CH00053P._CP',             # 15
        'ED6_DT07/CH00073P._CP',             # 16
        'ED6_DT07/CH00030P._CP',             # 17
        'ED6_DT06/CH20020P._CP',             # 18
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
        TalkScenaIndex      = 12,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 141250,
        Z                   = 0,
        Y                   = 7610,
        Direction           = 278,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 78740,
        Z                   = 0,
        Y                   = -1880,
        Direction           = 194,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 83700,
        Z                   = 300,
        Y                   = -52940,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 90160,
        Z                   = 0,
        Y                   = -56780,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458771,
        ChipIndex           = 0x13,
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
        Unknown3            = 524307,
        ChipIndex           = 0x13,
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
        Unknown3            = 589843,
        ChipIndex           = 0x13,
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
        Unknown3            = 655379,
        ChipIndex           = 0x13,
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
        Unknown3            = 720915,
        ChipIndex           = 0x13,
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
        Unknown3            = 786451,
        ChipIndex           = 0x13,
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
        Unknown3            = 262163,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 86360,
        Z                   = 200,
        Y                   = -52990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 30310,
        Z                   = 200,
        Y                   = -53530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 135100,
        Z                   = 0,
        Y                   = 9440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 134700,
        Z                   = 700,
        Y                   = 10040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327699,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 135400,
        Z                   = 700,
        Y                   = 10100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835032,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29400,
        Z                   = 500,
        Y                   = -53300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900568,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29400,
        Z                   = 500,
        Y                   = -53900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900568,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29000,
        Z                   = 500,
        Y                   = -53600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900568,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 139320,
        TriggerZ            = 0,
        TriggerY            = 7540,
        TriggerRange        = 400,
        ActorX              = 141250,
        ActorZ              = 1500,
        ActorY              = 7610,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_496",          # 00, 0
        "Function_1_6F5",          # 01, 1
        "Function_2_790",          # 02, 2
        "Function_3_90D",          # 03, 3
        "Function_4_D3E",          # 04, 4
        "Function_5_FA5",          # 05, 5
        "Function_6_12AA",         # 06, 6
        "Function_7_17A4",         # 07, 7
        "Function_8_1B3F",         # 08, 8
        "Function_9_1D93",         # 09, 9
        "Function_10_1DCF",        # 0A, 10
        "Function_11_1DD4",        # 0B, 11
        "Function_12_2025",        # 0C, 12
        "Function_13_2A4C",        # 0D, 13
        "Function_14_3FFB",        # 0E, 14
        "Function_15_4056",        # 0F, 15
        "Function_16_5B1B",        # 10, 16
        "Function_17_6919",        # 11, 17
        "Function_18_6ABB",        # 12, 18
        "Function_19_6AC2",        # 13, 19
        "Function_20_6B7C",        # 14, 20
    )


    def Function_0_496(): pass

    label("Function_0_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_4A1")
    Event(0, 18)

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4B8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_4CF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_4CF")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_4DF"),
        (108, "loc_4F5"),
        (SWITCH_DEFAULT, "loc_508"),
    )


    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F2")
    OP_A2(0x646)
    Event(0, 15)

    label("loc_4F2")

    Jump("loc_508")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    Event(0, 17)

    label("loc_505")

    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 38190, 200, -58050, 90)

    label("loc_52A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_554")
    SetChrChipByIndex(0x0, 2)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_638")
    ClearChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    SetChrPos(0xC, 30760, 200, 53020, 270)
    SetChrPos(0x17, 29800, 500, 53440, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, 29750, 500, 53150, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, 29750, 500, 52650, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, 29300, 500, 53440, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 29300, 500, 52920, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 29300, 500, 52420, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_6F4")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_65D")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_6F4")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrFlags(0xD, 0x80)
    Jump("loc_6F4")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_69D")
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x8, 16)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 37860, 0, -59000, 90)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_6F4")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_6C9")
    SetChrChipByIndex(0x8, 16)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 37860, 0, -59000, 90)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_6F4")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_6F4")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 30330, 250, -53540, 270)

    label("loc_6F4")

    Return()

    # Function_0_496 end

    def Function_1_6F5(): pass

    label("Function_1_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_711")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_739")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_729")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_739")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_739")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_745")
    OP_1B(0x0, 0x0, 0x13)

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_74F")
    Jump("loc_786")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_759")
    Jump("loc_786")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_767")
    OP_64(0x0, 0x1)
    Jump("loc_786")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_775")
    OP_64(0x0, 0x1)
    Jump("loc_786")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_77F")
    Jump("loc_786")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_786")

    label("loc_786")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_6F5 end

    def Function_2_790(): pass

    label("Function_2_790")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8F7")

    label("loc_7B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8F7")

    label("loc_7CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8F7")

    label("loc_7E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_800")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8F7")

    label("loc_800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_819")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8F7")

    label("loc_819")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_832")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8F7")

    label("loc_832")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8F7")

    label("loc_84B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_864")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8F7")

    label("loc_864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8F7")

    label("loc_87D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_896")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8F7")

    label("loc_896")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8F7")

    label("loc_8AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8F7")

    label("loc_8C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8F7")

    label("loc_8E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8F7")

    label("loc_90C")

    Return()

    # Function_2_790 end

    def Function_3_90D(): pass

    label("Function_3_90D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB6")
    OP_A2(0x5)

    ChrTalk(
        0x10,
        (
            "#102F理查德上校使用的『福音』\x01",
            "已经顺利回收了……\x02\x03",
            "等封印区域的调查结束了，\x01",
            "回到蔡斯之后还得进行更彻底的相关调查。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……确实让人很在意啊。\x02\x03",
            "#505F到最后还是没有弄清楚\x01",
            "是谁制造了这个东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#102F嗯。\x02\x03",
            "只要能判定『福音』的真面目，\x01",
            "那么在封印区域发生的事情\x01",
            "所隐含的真正意义不也就清楚了吗。\x02\x03",
            "#101F嗯，充满干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F充满干劲固然很好……\x02\x03",
            "不过还是要注意\x01",
            "别在研究时被人绑架了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#104F我知道了，\x01",
            "以后我会小心的。\x02\x03",
            "#100F顺便说一下，\x01",
            "现在『福音』是由卡西乌斯那家伙保管的。\x02\x03",
            "没有比这更好的保管场所了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F的确……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_CB6")


    ChrTalk(
        0x10,
        (
            "#103F不过说起来，\x01",
            "这个口琴的音色十分不错啊。\x02\x03",
            "#101F呵呵，\x01",
            "看来用导力器是无论如何也模仿不了的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    TalkEnd(0xFE)
    Return()

    # Function_3_90D end

    def Function_4_D3E(): pass

    label("Function_4_D3E")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D63")
    SetChrSubChip(0xFE, 1)
    Jump("loc_D94")

    label("loc_D63")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D79")
    SetChrSubChip(0xFE, 2)
    Jump("loc_D94")

    label("loc_D79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8F")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D94")

    label("loc_D8F")

    SetChrSubChip(0xFE, 1)

    label("loc_D94")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F59")
    OP_A2(0x4)

    ChrTalk(
        0xF,
        (
            "#560F好美的音色……\x01",
            "是谁在吹呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，\x01",
            "和提妲在一起的时候他没有吹过呢。\x02\x03",
            "这是约修亚吹的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#064F约修亚哥哥！？\x02\x03",
            "#061F哇，\x01",
            "原来哥哥他会吹口琴啊。\x02\x03",
            "吹得真好呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，还可以吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#067F我很笨，\x01",
            "所以什么乐器都不会。\x02\x03",
            "我好羡慕他啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F（唔～如果说提妲都很笨，\x01",
            "　那么我算是什么呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9C")

    label("loc_F59")


    ChrTalk(
        0xF,
        (
            "#061F原来约修亚哥哥会吹口琴啊。\x01",
            "　\x02\x03",
            "吹得真好呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9C")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_D3E end

    def Function_5_FA5(): pass

    label("Function_5_FA5")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FCA")
    SetChrSubChip(0xFE, 2)
    Jump("loc_FFB")

    label("loc_FCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FE0")
    SetChrSubChip(0xFE, 1)
    Jump("loc_FFB")

    label("loc_FE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FF6")
    SetChrSubChip(0xFE, 0)
    Jump("loc_FFB")

    label("loc_FF6")

    SetChrSubChip(0xFE, 2)

    label("loc_FFB")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1235")
    OP_A2(0x8)

    ChrTalk(
        0x18,
        (
            "#053F这音色……\x01",
            "怎么让人感觉如此怀念。\x02\x03",
            "小的时候在村里好像听到过……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "阿加特是在拉文努村出生的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#552F……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#061F嘿嘿，\x01",
            "阿加特大哥哥在故乡有个妹妹呢。\x02\x03",
            "是叫做米夏吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#055F喂、喂……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F不会吧？\x01",
            "你竟然还有妹妹！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#551F你这是什么意思。\x02\x03",
            "#552F的确，我很少回去看看，\x01",
            "不是一个好哥哥……\x02\x03",
            "#051F这次的事件总算解决了，\x01",
            "隔了这么久，我也该回村里去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A1")

    label("loc_1235")


    ChrTalk(
        0x18,
        (
            "#051F这次的事件总算解决了，\x01",
            "隔了这么久，我也该回村里去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_5_FA5 end

    def Function_6_12AA(): pass

    label("Function_6_12AA")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12CF")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1300")

    label("loc_12CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12E5")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1300")

    label("loc_12E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12FB")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1300")

    label("loc_12FB")

    SetChrSubChip(0xFE, 2)

    label("loc_1300")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1747")
    OP_A2(0x7)

    ChrTalk(
        0x19,
        (
            "#070F哟，艾丝蒂尔。\x02\x03",
            "卡西乌斯大人现在还在开会吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，好像是。\x02\x03",
            "凯诺娜上尉和洛伦斯少尉至今还没有抓到。\x01",
            "　\x02\x03",
            "军队指挥系统要重新改制，\x01",
            "还有许许多多其他的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#073F哦，我还说要请他喝酒，\x01",
            "看来是不行了。\x02\x03",
            "#075F不过，那个女的姑且不论，\x01",
            "要想抓捕洛伦斯少尉，\x01",
            "大人恐怕得费一番力气了。\x02\x03",
            "我总觉得在武术大会上\x01",
            "他根本没有用尽全力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F的确，第二次对决时，\x01",
            "他的强大和之前简直就是天壤之别……\x02\x03",
            "#002F听说他原来是个猎兵，\x01",
            "猎兵真的那么强吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#072F是啊，\x01",
            "身经百战的佣兵当然是很强的了……\x02\x03",
            "而且那种强大远远不是\x01",
            "这么简单就可以说清楚的。\x02\x03",
            "#074F修罗——\x01",
            "这个词用在他身上是最合适的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_179B")

    label("loc_1747")


    ChrTalk(
        0x19,
        (
            "#070F话说回来，这首曲子很不错。\x02\x03",
            "正好作为我晚上小酌的下酒菜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_6_12AA end

    def Function_7_17A4(): pass

    label("Function_7_17A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB1")
    OP_A2(0x6)

    ChrTalk(
        0x1A,
        (
            "#033F哦……\x01",
            "这是约修亚君在演奏啊。\x02\x03",
            "#031F我当时在湖畔就听到过，\x01",
            "的确不是一般的水准。\x02\x03",
            "应该经过了很久的练习吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F的确，\x01",
            "从很早以前他就一直在吹这首曲子。\x02\x03",
            "虽然有时候也会吹其他的曲子，\x01",
            "不过还是这首吹得最有感情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#030F唔……\x02\x03",
            "不过，据我对这首曲子的了解，\x01",
            "约修亚君也确实是很厉害。\x02\x03",
            "帝国的人姑且不论，就王国的人而言，\x01",
            "知道这首曲子的人可谓寥寥无几。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "这是埃雷波尼亚的曲子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#033F『星之所在』对吧？\x02\x03",
            "#035F一首在帝国传唱了很久的曲子。\x01",
            "　\x02\x03",
            "帝都暂且不说，对于乡村的人们来说，\x01",
            "至今都还非常的熟悉，一直都在流传着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F哦～是这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B3B")

    label("loc_1AB1")


    ChrTalk(
        0x1A,
        (
            "#037F呵……\x01",
            "不愧是约修亚君啊。\x02\x03",
            "婀娜多姿的旋律\x01",
            "让我的心都在扑通扑通地跳动哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3B")

    TalkEnd(0xFE)
    Return()

    # Function_7_17A4 end

    def Function_8_1B3F(): pass

    label("Function_8_1B3F")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B64")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1B95")

    label("loc_1B64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B7A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1B95")

    label("loc_1B7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B90")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1B95")

    label("loc_1B90")

    SetChrSubChip(0xFE, 2)

    label("loc_1B95")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0F")
    OP_A2(0x3)

    ChrTalk(
        0xC,
        (
            "#021F哎呀，\x01",
            "这不是约修亚的口琴声吗。\x02\x03",
            "从外面传来的声音来看，\x01",
            "那孩子应该在空中庭园呢。\x02\x03",
            "#027F难得气氛这么好，\x01",
            "现在就下定决心吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F也、也许是吧……\x02\x03",
            "#509F……不行！\x01",
            "这次还没那个打算！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#025F唉～遗憾啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D8A")

    label("loc_1D0F")


    ChrTalk(
        0xC,
        (
            "#020F快呀快呀，去呀，\x01",
            "快去空中庭园呀。\x02\x03",
            "这回只有你们两个，好好谈谈吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_8_1B3F end

    def Function_9_1D93(): pass

    label("Function_9_1D93")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "这边是拉赛尔博士和\x01",
            "提妲小姐的房间。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1D93 end

    def Function_10_1DCF(): pass

    label("Function_10_1DCF")

    Call(0, 11)
    Return()

    # Function_10_1DCF end

    def Function_11_1DD4(): pass

    label("Function_11_1DD4")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1DF9")

    ChrTalk(
        0xD,
        "哟，今天怎么只有你一个人呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2021")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E5D")

    ChrTalk(
        0xD,
        "那位理查德上校竟然是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我至今还认为\x01",
            "他不应该是那种\x01",
            "会反叛女王陛下的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_1E5D")

    OP_A2(0x0)

    ChrTalk(
        0xD,
        (
            "理查德上校\x01",
            "每晚都会到这里来\x01",
            "向我打听一些事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "至今我还是觉得他不应该是\x01",
            "会反叛女王陛下的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F08")

    Jump("loc_2021")

    label("loc_1F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1F15")
    Jump("loc_2021")

    label("loc_1F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1F1F")
    Jump("loc_2021")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1F8F")

    ChrTalk(
        0xD,
        (
            "作为饭后的消遣，\x01",
            "来一杯饮料如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "就算菜单上没有的种类\x01",
            "也可以立刻调配出来的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2021")

    label("loc_1F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(
        0xD,
        (
            "这里是谈话室。\x01",
            "请在这里放松一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "如果客人\x01",
            "需要酒水的话，\x01",
            "请尽管吩咐我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2021")

    TalkEnd(0xD)
    Return()

    # Function_11_1DD4 end

    def Function_12_2025(): pass

    label("Function_12_2025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2597")
    OP_A2(0x63C)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 29590, 0, -55060, 0)
    SetChrPos(0x102, 28580, 0, -55120, 45)
    OP_6D(29870, 0, -54070, 0)
    SetChrSubChip(0xFE, 1)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#802F哦哦……\x01",
            "艾丝蒂尔、约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F工房长先生！\x01",
            "您果然也被邀请了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为邀请的都是市长级别的人物，\x01",
            "所以觉得工房长肯定也会来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#801F你们才是，\x01",
            "真没想到能得到武术大会冠军，\x01",
            "还被邀请来格兰赛尔城呢。\x02\x03",
            "哎呀～\x01",
            "不愧是卡西乌斯先生的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "因为得到了很多人的帮助嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F对了，最近这些天有什么动静吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F嗯……\x01",
            "你们刚出发去王都，\x01",
            "情报部的凯诺娜上尉就来了。\x02\x03",
            "虽然没办法拒绝出席晚宴，\x01",
            "不过关于你们潜入要塞的事，\x01",
            "不管怎么说还是瞒过去了。\x02\x03",
            "逃走的拉赛尔博士他们，\x01",
            "好像也没有被军队发现。\x02\x03",
            "#803F不过，这种情况再持续下去，\x01",
            "被抓住也只是时间上的问题了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F刚才，我向凯诺娜上尉\x01",
            "提出要探望女王陛下的要求，\x01",
            "但话音刚落就被她一口拒绝了……\x02\x03",
            "果然还是很难直接见面吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F好像是呢……\x01",
            "#006F不过别担心，已经有办法了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不管怎么说，\x01",
            "一定要把博士的传话带给女王陛下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    EventEnd(0x0)
    Jump("loc_2A4B")

    label("loc_2597")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_26B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_2615")

    ChrTalk(
        0x8,
        (
            "#800F街上还是那么热闹啊。\x01",
            "　\x02\x03",
            "难得来一趟王都。\x01",
            "回去之前就去酒馆里放松一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B5")

    label("loc_2615")


    ChrTalk(
        0x8,
        (
            "#800F我和拉赛尔博士\x01",
            "这么长时间不在中央工房，\x01",
            "真是担心那边的情况啊。\x02\x03",
            "我打算明天就乘『林德号』返回蔡斯。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B5")

    Jump("loc_2A48")

    label("loc_26B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_26C2")
    Jump("loc_2A48")

    label("loc_26C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_26CC")
    Jump("loc_2A48")

    label("loc_26CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_292B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 1)), scpexpr(EXPR_END)), "loc_2741")

    ChrTalk(
        0x8,
        (
            "#800F听说陛下的病情有了好转，\x01",
            "让人松了一口气啊。\x02\x03",
            "只要知道这件事，\x01",
            "来王都这一趟就值得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2928")

    label("loc_2741")

    OP_A2(0x6F9)

    ChrTalk(
        0x8,
        (
            "#800F希尔丹夫人，好久不见了。\x01",
            "看到您这么有精神，真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#711F玛多克工房长也没变呢。\x02\x03",
            "还是老样子，\x01",
            "总是闲不下来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#801F哈～哈，话说回来，\x01",
            "中央工房优秀的新人辈出，\x01",
            "让人甚感欣慰啊。\x02\x03",
            "#800F而且听说陛下的病情有了好转，\x01",
            "让人松了一口气啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x0,
        "希尔丹夫人",
        (
            "#710F……嗯，我想再过不久\x01",
            "就可以和陛下见面了吧。\x02\x03",
            "玛多克工房长，\x01",
            "如果您有什么需要的话，\x01",
            "请别客气，尽量提出来。\x02\x03",
            "我们会马上为您准备好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#800F……哦，让您费心了。\x02",
    )

    CloseMessageWindow()

    label("loc_2928")

    Jump("loc_2A48")

    label("loc_292B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2974")

    ChrTalk(
        0x8,
        (
            "#800F哦，艾丝蒂尔和约修亚。\x02\x03",
            "怎么样，\x01",
            "和女王陛下见到面了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A48")

    label("loc_2974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2A48")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_299D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_29CE")

    label("loc_299D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29B3")
    SetChrSubChip(0xFE, 1)
    Jump("loc_29CE")

    label("loc_29B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29C9")
    SetChrSubChip(0xFE, 0)
    Jump("loc_29CE")

    label("loc_29C9")

    SetChrSubChip(0xFE, 2)

    label("loc_29CE")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x8,
        (
            "#800F情报部的那些人非常地狡猾。\x01",
            "　\x02\x03",
            "你们两个务必要\x01",
            "谨慎小心地行动哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_2A48")

    TalkEnd(0xFE)

    label("loc_2A4B")

    Return()

    # Function_12_2025 end

    def Function_13_2A4C(): pass

    label("Function_13_2A4C")

    EventBegin(0x0)
    OP_6D(132620, 4000, -1250, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x9, 13)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x102, 15)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 149100, 4200, 7600, 270)
    SetChrPos(0x102, 146580, 4200, 8100, 90)
    SetChrPos(0x101, 146580, 4200, 7130, 90)
    FadeToBright(1500, 0)
    OP_6D(147760, 4000, 7560, 5000)
    Fade(1000)
    OP_6D(148910, 4000, 7610, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(1090, 0)
    OP_6C(88000, 0)
    OP_6E(699, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#110F……第一次见到卡西乌斯上校时\x01",
            "我只是个刚从士官学校毕业的学生。\x02\x03",
            "加入王国军之后，我就被分配到\x01",
            "他所率领的独立机动部队去了……\x02\x03",
            "从那以后，直到他引退的那段日子，\x01",
            "我都在工作和生活各方面都受到他的照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F呵、呵～呵……\x01",
            "是这样的啊……\x02\x03",
            "#501F嗯，当时我的老爸\x01",
            "给上校您留下什么样的印象呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#115F用一个词形容，就是『英雄』。\x02\x03",
            "称为『剑圣』也毫不为过的精湛技艺。\x02\x03",
            "面对任何战况都可以灵活应对，\x01",
            "拥有立体的全方位指挥能力……\x02\x03",
            "而且不仅仅是拥有各种战术，\x01",
            "还拥有指挥部队的高超战略能力……\x02\x03",
            "#110F不管哪一项都无人能及。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F听、听起来总觉得\x01",
            "这么厉害的人不像是老爸呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F父亲退役和那个『百日战役』\x01",
            "是在同一时期吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#116F嗯……\x01",
            "我当时在卡西乌斯上校的麾下。\x02\x03",
            "到现在我都还记得很清楚，\x01",
            "他所部署的奇迹般的作战给我们\x01",
            "军中将士所带来的热情与兴奋……\x02\x03",
            "#115F一说起那个时候的事情，\x01",
            "再有多少时间都不够用，\x01",
            "以后有机会我会和你们慢慢道来的……\x02\x03",
            "但仅凭这些就可以断定一点。\x02\x03",
            "#112F那就是——如果那时没有一位\x01",
            "叫做卡西乌斯·布莱特的男人，\x01",
            "利贝尔就已经被埃雷波尼亚所吞并了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F不、不会吧！？\x02\x03",
            "的确有些难以置信……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F呵呵，能将难以置信之事\x01",
            "化为可能的就是『英雄』。\x02\x03",
            "而且他在战争之后很快就退役了，\x01",
            "更加拒绝了女王陛下授予的勋章，\x01",
            "不让世人知道其威名……\x02\x03",
            "至今为止，在一部分军人之中还把\x01",
            "卡西乌斯上校的名字作为英雄的代名词。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F唔～……\x02\x03",
            "#582F那个小气的老爸，\x01",
            "这些事情竟然一个字也没跟我提起过！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)

    ChrTalk(
        0x102,
        (
            "#010F如果特地和女儿说这番话，\x01",
            "也不见得她能听得进去啊。\x02\x03",
            "若是责备父亲的话，他也太可怜了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#005F可、可怜的是我们啊！\x02\x03",
            "#509F……说起来，\x01",
            "约修亚你似乎不是很吃惊啊。\x02\x03",
            "难道说……\x01",
            "刚才那些事情你是都知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F理查德上校是父亲的部下这一点\x01",
            "的确不知道……\x01",
            "　\x02\x03",
            "#015F不过……其他的我是知道的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F什、什么～！？\x02\x03",
            "这么说约修亚就是共犯了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F太、太夸张了，艾丝蒂尔。\x02\x03",
            "我是从别的地方得知的，\x01",
            "父亲并没有亲口告诉过我。\x02\x03",
            "而且父亲也没必要\x01",
            "特地告诉我们这些事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F唔～不太令人信服哦～……\x02\x03",
            "#582F真是的……\x01",
            "回去之后一定要好好教训他一顿！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#110F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#503F啊，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F非、非常抱歉。\x01",
            "中途打断了您说话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#115F哪里……\x01",
            "看见你们这样我也稍感安心了。\x02\x03",
            "卡西乌斯上校要退役的时候，\x01",
            "我曾经打算用尽方法来挽留住他……\x02\x03",
            "不过那样的选择，\x01",
            "对他来说也许是最合适的。\x02\x03",
            "#110F有你们陪伴在他身旁，\x01",
            "失去夫人的悲痛一定会逐渐消去的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F理查德上校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(147760, 4000, 7560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, 148530, 4000, 6210, 270)
    ClearChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x102, 2)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#111F#2P那么……\x01",
            "多谢你们能陪我聊一下天。\x02\x03",
            "因为公爵大人还在等着我过去，\x01",
            "所以我就先告辞了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F抱歉，那个……\x01",
            "我们完全是在听您的讲话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F#2P不，没那回事。\x01",
            "你们让我得知了我最想知道的。\x02\x03",
            "#115F……这样一来我就没有什么可以遗憾的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F这究竟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#111F#2P哈哈，最近一段时间\x01",
            "我们还会有机会见面的。\x02\x03",
            "那时就可以和卡西乌斯上校\x01",
            "还有你们一起好好聊聊了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_62(0x101, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_3944():
        OP_6D(146770, 2000, -760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3944)
    OP_43(0x9, 0x1, 0x0, 0xE)
    SetChrSubChip(0x101, 2)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_63(0x101)
    OP_63(0x102)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x102, 146580, 4000, 8100, 90)
    SetChrPos(0x101, 146580, 4000, 7130, 90)

    def lambda_39B1():
        OP_8E(0xFE, 0x24068, 0xFA0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39B1)
    Sleep(300)

    def lambda_39D1():
        OP_8E(0xFE, 0x24414, 0xFA0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39D1)
    WaitChrThread(0x101, 0x1)

    def lambda_39F1():
        OP_6D(148490, 4000, 5300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39F1)
    OP_8C(0x101, 225, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#505F#6P嗯……\x02\x03",
            "刚才那个人真的是理查德上校吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F#2P我说……你睡迷糊了啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#003F#6P可、可是他那样钦佩地\x01",
            "说着老爸过去的事情……\x02\x03",
            "怎么说好呢……\x01",
            "和以往留下的印象不同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P……的确。\x01",
            "他并不是一个单纯的坏人。\x02\x03",
            "#012F可是，抛开这个不提，\x01",
            "他肯定是有什么企图的。\x02\x03",
            "否则怎么会对父亲的事情\x01",
            "了解得那么清楚明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P嗯……\x01",
            "话是这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P丑话先说在前面……\x02\x03",
            "把我们这么亲切地找来，\x01",
            "也许是处于什么目的……\x02\x03",
            "#012F像他那样的情报专家，\x01",
            "要想欺骗我们这样的小孩，\x01",
            "简直就是易如反掌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#6P你、你敢肯定刚才你说的那些话\x01",
            "没有言过其实吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P嗯……肯定。\x02\x03",
            "防人之心不可无。\x02\x03",
            "你只要相信你自己的直觉就可以了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P要做好各种准备，\x01",
            "对任何人都不可掉以轻心。\x02\x03",
            "这一点也是游击士所要做到的……\x01",
            "我认为就是这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#500F#6P…………………………\x02\x03",
            "#006F嗯，我明白了。\x02\x03",
            "我会牢记在心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2P……谢谢你，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#6P什么～呀。\x01",
            "约修亚你怎么和我讲起礼来了。\x02\x03",
            "#006F接下来我们要立刻\x01",
            "赶到希尔丹夫人那里去。\x02\x03",
            "她大概已经等得不耐烦了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P是啊……\x01",
            "这就前去女佣的休息室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_A2(0x641)
    EventEnd(0x0)
    OP_1D(0x11)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_2A4C end

    def Function_14_3FFB(): pass

    label("Function_14_3FFB")

    OP_8E(0xFE, 0x241E4, 0xFA0, 0xED8, 0xBB8, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_8E(0xFE, 0x241D0, 0x7D0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x22632, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20666, 0x0, 0x320, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_3FFB end

    def Function_15_4056(): pass

    label("Function_15_4056")

    EventBegin(0x0)
    OP_6D(88650, 0, 6240, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(1940, 0)
    OP_6C(46000, 0)
    OP_6E(474, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x138, 2)
    SetChrPos(0x138, 87950, 0, 4590, 0)
    SetChrPos(0x101, 87640, 0, 6230, 90)
    SetChrPos(0x102, 89210, 0, 6370, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#327F呼……\x01",
            "约修亚你可真受欢迎啊。\x02\x03",
            "那个家伙一听到约修亚的名字，\x01",
            "顿时就两眼放光呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#337F#2P哪、哪有那样的事。\x02\x03",
            "倒是你啊，装得还真像回事。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#473F我那个时候对着那个家伙，\x01",
            "可是一点紧张感都没有呢。\x02\x03",
            "#327F呼～不管怎么说～\x01",
            "还是觉得有些不够自信啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#332F#2P嗯……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 93780, 0, 850, 90)
    SetChrPos(0xB, 93780, 0, 850, 90)
    OP_72(0x24, 0x10)
    OP_6F(0x24, 0)
    OP_70(0x24, 0x3C)
    OP_73(0x24)

    NpcTalk(
        0xA,
        "男人的声音",
        (
            "嗝……\x01",
            "什么人在吵吵嚷嚷的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x138, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_42FB():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42FB)

    def lambda_4309():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4309)

    def lambda_4317():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_4317)
    OP_6D(90380, 0, 5100, 1000)

    def lambda_4336():

        label("loc_4336")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4336")

    QueueWorkItem2(0x101, 1, lambda_4336)

    def lambda_4347():

        label("loc_4347")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4347")

    QueueWorkItem2(0x102, 1, lambda_4347)

    def lambda_4358():

        label("loc_4358")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4358")

    QueueWorkItem2(0x138, 1, lambda_4358)

    def lambda_4369():
        OP_6D(89070, 0, 5570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4369)

    def lambda_4381():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4381)
    WaitChrThread(0xA, 0x1)
    ClearChrFlags(0xB, 0x80)

    def lambda_43A6():
        OP_8E(0xFE, 0x15D06, 0x0, 0x1158, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_43A6)
    OP_8E(0xB, 0x1658A, 0x0, 0x4BA, 0x7D0, 0x0)
    OP_72(0x24, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    def lambda_43ED():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_43ED)
    WaitChrThread(0xB, 0x1)

    def lambda_440D():
        OP_8E(0xFE, 0x15EA0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_440D)
    WaitChrThread(0xA, 0x1)

    def lambda_442D():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_442D)

    ChrTalk(
        0x138,
        "#712F公爵大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#227F我还以为是谁呢，这不是女管家吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#481F哦……\x01",
            "怎么，那两个侍女是……\x02\x03",
            "嗝……\x01",
            "以前没见过的小姑娘哦……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_4590")

    ChrTalk(
        0x138,
        (
            "#713F新来的实习侍女，\x01",
            "莱娜和卡玲。\x02\x03",
            "因为她们对城里还不熟悉，\x01",
            "所以我刚才带她们到处走走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4706")

    label("loc_4590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_464C")

    ChrTalk(
        0x138,
        (
            "#713F新来的实习侍女，\x01",
            "雪拉和卡玲。\x02\x03",
            "因为她们对城里还不熟悉，\x01",
            "所以我刚才带她们到处走走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4706")

    label("loc_464C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_4706")

    ChrTalk(
        0x138,
        (
            "#713F新来的实习侍女，\x01",
            "朵洛希和卡玲。\x02\x03",
            "因为她们对城里还不熟悉，\x01",
            "所以我刚才带她们到处走走。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4706")

    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#722F哦……？\x02",
    )

    CloseMessageWindow()
    OP_8E(0xB, 0x16044, 0x0, 0x10AE, 0x7D0, 0x0)
    OP_8E(0xB, 0x15F40, 0x0, 0x14BE, 0x7D0, 0x0)
    TurnDirection(0xB, 0x102, 400)
    Sleep(500)
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(
        0xB,
        "#721F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#323F#1P（啊……注意到了？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#335F（……糟糕了。）\x02\x03",
            "（毕竟和这个管家见过几次面，\x01",
            "　所以被注意到也不奇怪……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#481F怎么了，菲利普。\x01",
            "目不转睛的盯着看……\x02\x03",
            "#229F哇哈哈，你这个正经古板的家伙，\x01",
            "很少见你有这么出格的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#720F失礼了……\x02\x03",
            "因为这位小姐和我的侄女很相似，\x01",
            "所以不禁一下子就呆住了。\x02\x03",
            "两位小姐，刚才真是非常的抱歉。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#474F#1P啊，没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#331F请不要介意……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#227F嘿嘿，仔细地再瞧一下，\x01",
            "不管哪个都是精选的上等货色啊……\x02\x03",
            "尤其是棕色头发的那位，\x01",
            "真是极具阳光女孩的气息啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#476F#1P……（鄙视）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#227F至于黑色头发的那位嘛……\x01",
            "要是再稍微把腰挺直点就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#338F……惶、惶恐之至。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#483F呼，那么……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_4B58")

    ChrTalk(
        0xA,
        (
            "#482F#3S莱娜！\x01",
            "我命令你今晚来伺候我！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4C18")

    label("loc_4B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_4BB9")

    ChrTalk(
        0xA,
        (
            "#482F#3S雪拉！\x01",
            "我命令你今晚来伺候我！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4C18")

    label("loc_4BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_4C18")

    ChrTalk(
        0xA,
        (
            "#482F#3S朵洛希！\x01",
            "我命令你今晚来伺候我！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    label("loc_4C18")


    ChrTalk(
        0x102,
        "#332F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#324F#1P哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        "#721F公、公爵大人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#473F#1P（咦，什么叫伺候呢？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#334F（唔，该怎么说好呢……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#714F公爵大人，再怎么说，\x01",
            "玩笑也开得有些过分了吧……\x02\x03",
            "在这个格兰赛尔城工作的侍女\x01",
            "全都是诚心服侍女王陛下的。\x02\x03",
            "您难道忘记了这一点吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x138, 400)

    ChrTalk(
        0xA,
        (
            "#480F我知道、我知道……\x01",
            "真是个连玩笑都受不起的大婶。\x02\x03",
            "#483F嗝……\x01",
            "反正一周之后这个王城就是我的了。\x02\x03",
            "嘿嘿嘿……\x01",
            "到那时我再来好好享受这番乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#714F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#723F公、公爵大人！\x01",
            "请您说话适可而止！\x02\x03",
            "暴饮暴食姑且不论，\x01",
            "沉溺女色简直就是岂有此理！\x02\x03",
            "我菲利普就算拼了老命，\x01",
            "也会阻止大人您做出如此……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(
        0xA,
        (
            "#482F刚才不是说了只是在开玩笑嘛！\x01",
            "　\x02\x03",
            "够了！\x01",
            "今晚赶快回去休息吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#722F公、公爵大人所言极是。\x01",
            "　\x02\x03",
            "#720F大人您的房间就在前面，\x01",
            "请您小心脚下慢慢走。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FE7():
        OP_6D(87270, 0, 5910, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4FE7)

    def lambda_4FFF():
        OP_8E(0xFE, 0x15996, 0x0, 0x1482, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4FFF)
    Sleep(600)

    def lambda_501F():
        OP_8E(0xFE, 0x151EE, 0x0, 0x15C2, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_501F)
    WaitChrThread(0xA, 0x1)

    def lambda_503F():
        OP_8E(0xFE, 0x14E38, 0x0, 0x15B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_503F)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)

    def lambda_5064():

        label("loc_5064")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5064")

    QueueWorkItem2(0xB, 2, lambda_5064)

    def lambda_5075():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5075)
    OP_8F(0xA, 0x14E92, 0x0, 0x18EC, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_5149")

    ChrTalk(
        0xA,
        (
            "#227F嗯～……\x01",
            "对了，莱娜。\x02\x03",
            "#483F如果有什么感情上的问题的话，\x01",
            "请不用客气，随时来找我商量哦。\x02\x03",
            "嘿嘿……身为下任国王的我\x01",
            "一定会亲自帮你好好解决的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52BB")

    label("loc_5149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_5203")

    ChrTalk(
        0xA,
        (
            "#227F嗯～……\x01",
            "对了，雪拉。\x02\x03",
            "#483F如果有什么感情上的问题的话，\x01",
            "请不用客气，随时来找我商量哦。\x02\x03",
            "嘿嘿……身为下任国王的我\x01",
            "一定会亲自帮你好好解决的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52BB")

    label("loc_5203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_52BB")

    ChrTalk(
        0xA,
        (
            "#227F嗯～……\x01",
            "对了，朵洛希。\x02\x03",
            "#483F如果有什么感情上的问题的话，\x01",
            "请不用客气，随时来找我商量哦。\x02\x03",
            "嘿嘿……身为下任国王的我\x01",
            "一定会亲自帮你好好解决的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52BB")


    ChrTalk(
        0x101,
        (
            "#476F啊哈……哈哈……\x01",
            "在此先向您谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#229F哇哈哈，可爱的宝贝儿。\x02\x03",
            "#227F嗯……不错不错！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    def lambda_533E():
        OP_6D(83810, 0, 6600, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_533E)
    OP_8E(0xA, 0x13416, 0x0, 0x1B4E, 0x5DC, 0x0)
    OP_8E(0xA, 0x13448, 0x0, 0x1CE8, 0x5DC, 0x0)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x3C)
    OP_73(0x21)
    OP_8E(0xA, 0x13416, 0x0, 0x2576, 0x5DC, 0x0)
    OP_72(0x21, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    def lambda_53D4():

        label("loc_53D4")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_53D4")

    QueueWorkItem2(0x101, 1, lambda_53D4)

    def lambda_53E5():

        label("loc_53E5")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_53E5")

    QueueWorkItem2(0x102, 1, lambda_53E5)

    def lambda_53F6():

        label("loc_53F6")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_53F6")

    QueueWorkItem2(0x138, 1, lambda_53F6)

    def lambda_5407():
        OP_6D(88010, 0, 6080, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5407)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        (
            "#722F让你们受惊了。\x02\x03",
            "大人明天一早起来的时候，\x01",
            "就会什么也记不起来的了。\x02\x03",
            "请两位小姐放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#714F……希望会是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#720F真是非常的抱歉。\x02\x03",
            "夫人、两位姑娘，\x01",
            "那我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    OP_8E(0xB, 0x13466, 0x0, 0x1694, 0xBB8, 0x0)
    OP_8E(0xB, 0x134B6, 0x0, 0x268E, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x138,
        (
            "#716F唉，那个当管家的也够辛苦的……\x02\x03",
            "几十年来都是那么辛苦地背负着\x01",
            "杜南公爵那个累人的负担……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        (
            "#324F咦……\x01",
            "希尔丹夫人和菲利普先生认识吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x138, 0x101, 400)

    ChrTalk(
        0x138,
        (
            "#715F在年幼的时候就认识了。\x02\x03",
            "可是到了今天，不管在工作方面\x01",
            "还是在立场方面都有了距离……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x138, 400)

    ChrTalk(
        0x102,
        "#330F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#327F的确，菲利普先生看起来\x01",
            "就是一副饱经沧桑的样子啊。\x02\x03",
            "#473F他对公爵被上校唆使这件事\x01",
            "好像非常担心的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#330F很有可能……\x02\x03",
            "#338F对了，艾丝蒂尔，\x01",
            "看来你也很受男性欢迎嘛。\x02\x03",
            "公爵看来很喜欢你呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#476F哼……\x01",
            "你好像是在幸灾乐祸啊……\x02\x03",
            "#471F啊，对了对了……\x01",
            "到底那个『伺候』是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#337F那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#713F艾丝蒂尔。\x02\x03",
            "如果你想知道其中的含义，\x01",
            "也并不是件十分困难的事情。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_598E():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_598E)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        "#324F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F……把耳朵凑过来。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    OP_8E(0x138, 0x15626, 0x0, 0x1644, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "希尔丹夫人对艾丝蒂尔说了悄悄话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8F(0x138, 0x1578E, 0x0, 0x11EE, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#472F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#711F……明白了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        (
            "#472F啊、唔……\x02\x03",
            "#327F…………知道了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#333F（果真是毫无防备啊……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4254   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_4056 end

    def Function_16_5B1B(): pass

    label("Function_16_5B1B")

    EventBegin(0x0)
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    SetChrPos(0xC, 30760, 200, 53020, 270)
    SetChrPos(0x17, 29800, 500, 53440, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, 29750, 500, 53150, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, 29750, 500, 52650, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, 29300, 500, 53440, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 29300, 500, 52920, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 29300, 500, 52420, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x101, 31390, 0, 55480, 270)
    OP_6D(29710, 0, 54720, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(45000, 0)
    OP_6E(401, 0)
    FadeToBright(2000, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x101, 0x7170, 0x0, 0xD6D8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8E(0x101, 0x7A9E, 0x0, 0xD6D8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    OP_8E(0x101, 0x7170, 0x0, 0xD6D8, 0x7D0, 0x0)
    Sleep(500)
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#505F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F怎么了，艾丝蒂尔。\x01",
            "从刚才开始就静不下来。\x02\x03",
            "是不是有什么心事呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        "#007F#5P嗯，是啊……\x02",
    )

    CloseMessageWindow()

    def lambda_5D30():
        OP_6D(30840, 0, 54690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D30)
    OP_8E(0x101, 0x74D6, 0x0, 0xD430, 0x3E8, 0x0)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#002F#6P我说，雪拉姐……\x02\x03",
            "刚才一起吃饭的时候，\x01",
            "觉不觉得约修亚的样子很奇怪啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#023F#2P？？？\x02\x03",
            "奇怪的是你啊。\x02\x03",
            "那孩子不是和平时一样沉着冷静吗。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#6P话是这样说没错……\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#027F#2P哈哈。\x02\x03",
            "是吗，原来是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P怎、怎么了，突然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#021F#2P你瞒不住我的～⊙\x02\x03",
            "虽然看你平时总是呆呆的……\x01",
            "不过到最后还是察觉出了自己的心意吧。\x02\x03",
            "#027F你啊……\x01",
            "是不是喜欢上约修亚了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#6P………唔…………\x02\x03",
            "#503F看、看得出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#027F#2P不好意思哦～被我发现了。\x02\x03",
            "不过你这个样子，\x01",
            "可没办法向约修亚表达真正的心意哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#6P嗯……我也这样觉得……\x02\x03",
            "那个约修亚从以前开始，\x01",
            "就对这方面的事情很迟钝……\x02\x03",
            "#506F哎，我也没有资格说别人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#520F#2P哎呀，真是单纯的想法啊。\x02\x03",
            "那个不谙世事的艾丝蒂尔，\x01",
            "也终于走到这一步了呢……\x02\x03",
            "姐姐我真是感动啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#6P……真是的～再这样的话，\x01",
            "我就不和雪拉姐说了哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F#2P抱歉抱歉，我不开玩笑了。\x01",
            "　\x02\x03",
            "#026F不过，也的确是……\x02\x03",
            "仔细想想的话，\x01",
            "你们在很小的时候就已经认识了。\x02\x03",
            "所以没有注意到对方心意的变化\x01",
            "也是没办法的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#6P是、是这样吗……\x02\x03",
            "#503F我也是在旅行的途中，\x01",
            "才开始慢慢意识到这种感觉的……\x02\x03",
            "当、当我有一次非常在意他的时候，\x01",
            "我就一下子意识到这种感觉……\x02\x03",
            "#504F啊啊，真是的。\x01",
            "这样根本不像我的性格啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#027F#2P呵呵……\x01",
            "世上没有不会绽放的花蕾。\x02\x03",
            "女孩子都是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F#2P虽然表达心意不能太过轻率……\x01",
            "　\x02\x03",
            "不过，既然你已经下定决心的话，\x01",
            "坦白地说出来不是更好吗？\x02\x03",
            "如果觉得难以决定的话，\x01",
            "不如姐姐我来为你占卜一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#6P不用了……\x01",
            "其实，我已经下定决心了。\x02\x03",
            "而且也和他约好要听他说自己以前的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F#2P是吗……\x02\x03",
            "#520F好，这样才是我的妹妹嘛！\x02\x03",
            "哎呀，真是的。\x01",
            "姐姐我都要感动得想哭了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#6P就不能说多点建设性的话吗……\x02\x03",
            "#501F不过，谢谢你，雪拉姐。\x01",
            "我觉得现在已经有点勇气了。\x02\x03",
            "我这就去约修亚那里看看。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xC,
        (
            "#023F#2P哎……！\x02\x03",
            "不、不会现在就要去告白吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6P不是啦，是其他的事情。\x02\x03",
            "不知道是不是心理作用，\x01",
            "总觉得刚才约修亚的样子有点奇怪呢。\x02\x03",
            "我先问问他是怎么回事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#025F#2P是、是吗……\x02\x03",
            "#020F不管怎样，\x01",
            "你对他的事情还真是很了解啊。\x02\x03",
            "#021F你和约修亚一定会发展得很顺利的。\x01",
            "　\x02\x03",
            "如果聊天的时候气氛不错，\x01",
            "干脆就趁势向他告白吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P唔……尽量吧……\x02\x03",
            "#006F那么，我走了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    def lambda_6804():
        OP_6D(31870, 0, 54140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6804)
    OP_8E(0x101, 0x816A, 0x0, 0xD430, 0x1388, 0x0)
    SetChrSubChip(0xC, 1)
    OP_8E(0x101, 0x88B8, 0x0, 0xC490, 0x1388, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_684E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_684E)
    OP_8E(0x101, 0x88B8, 0x0, 0xBF54, 0x1388, 0x0)
    Sleep(1500)

    def lambda_6879():
        OP_6D(30840, 0, 54690, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6879)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrChipByIndex(0xC, 20)
    SetChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0)
    OP_0D()
    Sleep(400)
    SetChrSubChip(0xC, 1)
    Sleep(400)
    OP_99(0xC, 0x1, 0x3, 0x320)
    Sleep(400)

    ChrTalk(
        0xC,
        (
            "#026F#5P……初恋吗……\x02\x03",
            "#027F如果能顺利就好了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 17)
    Return()

    # Function_16_5B1B end

    def Function_17_6919(): pass

    label("Function_17_6919")

    EventBegin(0x0)
    OP_6D(89230, 0, 60740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 79820, 0, 50600, 0)

    def lambda_696F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_696F)
    FadeToBright(1000, 0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_698F():
        OP_8E(0xFE, 0x13754, 0x0, 0xD7B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_698F)
    OP_6D(81310, 0, 56390, 4000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#004F#6P咦……两个人都不在啊。\x01",
            "　\x02\x03",
            "#505F对了，老爸说过还要开会……\x01",
            "　\x02\x03",
            "可是，约修亚呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x4A)
    OP_1F(0x50, 0xC8)
    Sleep(2000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#501F#6P约修亚……\x02\x03",
            "他在哪里吹口琴呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_1B(0x6, 0x0, 0xFFFF)
    OP_A2(0x670)
    EventEnd(0x0)
    Return()

    # Function_17_6919 end

    def Function_18_6ABB(): pass

    label("Function_18_6ABB")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_18_6ABB end

    def Function_19_6AC2(): pass

    label("Function_19_6AC2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B37")
    OP_A2(0x9)

    ChrTalk(
        0x101,
        (
            "#505F口琴声……\x01",
            "好像是从外面传来的。\x02\x03",
            "也就是说，\x01",
            "约修亚在空中庭园了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B65")

    label("loc_6B37")


    ChrTalk(
        0x101,
        (
            "#006F总之到屋顶的空中庭园去看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B65")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x1)
    Return()

    # Function_19_6AC2 end

    def Function_20_6B7C(): pass

    label("Function_20_6B7C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#007F哎呀，我真是的。\x01",
            "这是往哪里走啊。\x02\x03",
            "#000F……不赶快去约修亚的房间的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_20_6B7C end

    SaveToFile()

Try(main)
