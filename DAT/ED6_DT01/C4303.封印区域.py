﻿from ED6ScenarioHelper import *

def main():
    CreateScenaFile(
        FileName            = 'C4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4303.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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
        '雪拉',                                 # 9
        '奥利维尔',                             # 10
        '科洛丝',                               # 11
        '阿加特',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '拉赛尔博士',                           # 15
        '基库',                                 # 16
        '理查德上校',                           # 17
        '卡西乌斯',                             # 18
        '机器',                                 # 19
        '机器',                                 # 20
        '机器',                                 # 21
        '机器',                                 # 22
        '\u3000',                               # 23
        '\u3000',                               # 24
        '\u3000',                               # 25
        '\u3000',                               # 26
        '\u3000',                               # 27
        '\u3000',                               # 28
        '\u3000',                               # 29
        '\u3000',                               # 30
        '\u3000',                               # 31
        '\u3000',                               # 32
        '\u3000',                               # 33
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT06/CH20053 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT07/CH02020 ._CH',             # 06
        'ED6_DT07/CH00273 ._CH',             # 07
        'ED6_DT07/CH00271 ._CH',             # 08
        'ED6_DT07/CH02000 ._CH',             # 09
        'ED6_DT07/CH00100 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00110 ._CH',             # 0C
        'ED6_DT07/CH00111 ._CH',             # 0D
        'ED6_DT07/CH00120 ._CH',             # 0E
        'ED6_DT07/CH00121 ._CH',             # 0F
        'ED6_DT07/CH00130 ._CH',             # 10
        'ED6_DT07/CH00131 ._CH',             # 11
        'ED6_DT07/CH00140 ._CH',             # 12
        'ED6_DT07/CH00141 ._CH',             # 13
        'ED6_DT07/CH00150 ._CH',             # 14
        'ED6_DT07/CH00151 ._CH',             # 15
        'ED6_DT07/CH00160 ._CH',             # 16
        'ED6_DT07/CH00161 ._CH',             # 17
        'ED6_DT07/CH00170 ._CH',             # 18
        'ED6_DT07/CH00171 ._CH',             # 19
        'ED6_DT09/CH11002 ._CH',             # 1A
        'ED6_DT09/CH11000 ._CH',             # 1B
        'ED6_DT07/CH00272 ._CH',             # 1C
        'ED6_DT07/CH00274 ._CH',             # 1D
        'ED6_DT06/CH20021 ._CH',             # 1E
        'ED6_DT06/CH20027 ._CH',             # 1F
        'ED6_DT06/CH20028 ._CH',             # 20
        'ED6_DT06/CH20029 ._CH',             # 21
        'ED6_DT06/CH20084 ._CH',             # 22
        'ED6_DT06/CH20077 ._CH',             # 23
        'ED6_DT07/CH02030 ._CH',             # 24
        'ED6_DT07/CH00104 ._CH',             # 25
        'ED6_DT07/CH00114 ._CH',             # 26
        'ED6_DT07/CH00124 ._CH',             # 27
        'ED6_DT07/CH00134 ._CH',             # 28
        'ED6_DT07/CH00144 ._CH',             # 29
        'ED6_DT07/CH00154 ._CH',             # 2A
        'ED6_DT07/CH00164 ._CH',             # 2B
        'ED6_DT07/CH00174 ._CH',             # 2C
        'ED6_DT06/CH20046 ._CH',             # 2D
        'ED6_DT07/CH00270 ._CH',             # 2E
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT06/CH20053P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT07/CH02020P._CP',             # 06
        'ED6_DT07/CH00273P._CP',             # 07
        'ED6_DT07/CH00271P._CP',             # 08
        'ED6_DT07/CH02000P._CP',             # 09
        'ED6_DT07/CH00100P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00110P._CP',             # 0C
        'ED6_DT07/CH00111P._CP',             # 0D
        'ED6_DT07/CH00120P._CP',             # 0E
        'ED6_DT07/CH00121P._CP',             # 0F
        'ED6_DT07/CH00130P._CP',             # 10
        'ED6_DT07/CH00131P._CP',             # 11
        'ED6_DT07/CH00140P._CP',             # 12
        'ED6_DT07/CH00141P._CP',             # 13
        'ED6_DT07/CH00150P._CP',             # 14
        'ED6_DT07/CH00151P._CP',             # 15
        'ED6_DT07/CH00160P._CP',             # 16
        'ED6_DT07/CH00161P._CP',             # 17
        'ED6_DT07/CH00170P._CP',             # 18
        'ED6_DT07/CH00171P._CP',             # 19
        'ED6_DT09/CH11002P._CP',             # 1A
        'ED6_DT09/CH11000P._CP',             # 1B
        'ED6_DT07/CH00272P._CP',             # 1C
        'ED6_DT07/CH00274P._CP',             # 1D
        'ED6_DT06/CH20021P._CP',             # 1E
        'ED6_DT06/CH20027P._CP',             # 1F
        'ED6_DT06/CH20028P._CP',             # 20
        'ED6_DT06/CH20029P._CP',             # 21
        'ED6_DT06/CH20084P._CP',             # 22
        'ED6_DT06/CH20077P._CP',             # 23
        'ED6_DT07/CH02030P._CP',             # 24
        'ED6_DT07/CH00104P._CP',             # 25
        'ED6_DT07/CH00114P._CP',             # 26
        'ED6_DT07/CH00124P._CP',             # 27
        'ED6_DT07/CH00134P._CP',             # 28
        'ED6_DT07/CH00144P._CP',             # 29
        'ED6_DT07/CH00154P._CP',             # 2A
        'ED6_DT07/CH00164P._CP',             # 2B
        'ED6_DT07/CH00174P._CP',             # 2C
        'ED6_DT06/CH20046P._CP',             # 2D
        'ED6_DT07/CH00270P._CP',             # 2E
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 46,
        ChipIndex           = 0x2E,
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
        Unknown3            = 34,
        ChipIndex           = 0x22,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 1250,
        Y                   = 19300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917534,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_586",          # 00, 0
        "Function_1_5C0",          # 01, 1
        "Function_2_622",          # 02, 2
        "Function_3_708",          # 03, 3
        "Function_4_2574",         # 04, 4
        "Function_5_2C66",         # 05, 5
        "Function_6_2C9D",         # 06, 6
        "Function_7_3E44",         # 07, 7
        "Function_8_3FA8",         # 08, 8
        "Function_9_460C",         # 09, 9
        "Function_10_8D84",        # 0A, 10
        "Function_11_8E94",        # 0B, 11
        "Function_12_8EE1",        # 0C, 12
        "Function_13_8F2D",        # 0D, 13
        "Function_14_8F55",        # 0E, 14
        "Function_15_8FBF",        # 0F, 15
        "Function_16_8FF1",        # 10, 16
        "Function_17_9019",        # 11, 17
        "Function_18_90F6",        # 12, 18
        "Function_19_91B7",        # 13, 19
        "Function_20_921A",        # 14, 20
        "Function_21_9285",        # 15, 21
        "Function_22_9336",        # 16, 22
        "Function_23_93AA",        # 17, 23
        "Function_24_942C",        # 18, 24
        "Function_25_945E",        # 19, 25
    )


    def Function_0_586(): pass

    label("Function_0_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_59D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_59D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A9"),
        (SWITCH_DEFAULT, "loc_5BF"),
    )


    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BC")
    OP_A2(0x66A)
    Event(0, 3)

    label("loc_5BC")

    Jump("loc_5BF")

    label("loc_5BF")

    Return()

    # Function_0_586 end

    def Function_1_5C0(): pass

    label("Function_1_5C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x39C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3A1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    OP_4F(0x29, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_5F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3A2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3B3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_621")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_621")

    Return()

    # Function_1_5C0 end

    def Function_2_622(): pass

    label("Function_2_622")

    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(5000)
    LoadEffect(0x1, "map\\\\mp007_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(5000)
    LoadEffect(0x2, "map\\\\mp015_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_2_622 end

    def Function_3_708(): pass

    label("Function_3_708")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_71(0x6, 0x4)
    OP_6F(0x6, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3E8)
    OP_71(0x0, 0x20)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_70(0x0, 0x3E8)
    OP_70(0x1, 0x3E8)
    OP_70(0x2, 0x3E8)
    OP_70(0x3, 0x3E8)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_792")
    SetChrChipByIndex(0x103, 14)

    label("loc_792")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A8")
    SetChrChipByIndex(0x104, 16)
    OP_A2(0x6F5)

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")
    SetChrChipByIndex(0x106, 20)

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CE")
    SetChrChipByIndex(0x105, 18)

    label("loc_7CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E1")
    SetChrChipByIndex(0x107, 22)

    label("loc_7E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F4")
    SetChrChipByIndex(0x108, 24)

    label("loc_7F4")

    SetChrPos(0x101, -1440, 0, -47330, 0)
    SetChrPos(0x102, 720, 0, -47210, 0)

    def lambda_81C():

        label("loc_81C")

        OP_8C(0x101, 45, 0)
        OP_48()
        Jump("loc_81C")

    QueueWorkItem2(0x10, 1, lambda_81C)

    def lambda_82D():

        label("loc_82D")

        OP_8C(0x102, 315, 0)
        OP_48()
        Jump("loc_82D")

    QueueWorkItem2(0x10, 2, lambda_82D)

    def lambda_83E():
        OP_8E(0xFE, 0xFFFFF92A, 0x0, 0x2D82, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_83E)

    def lambda_859():
        OP_8E(0xFE, 0x636, 0x0, 0x2D82, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_859)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8BC")
    SetChrPos(0x0, 970, 0, -49020, 0)

    def lambda_8A4():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8A4)
    Jump("loc_8E8")

    label("loc_8BC")

    SetChrPos(0x0, -2029, 0, -48950, 0)

    def lambda_8D3():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8D3)

    label("loc_8E8")

    OP_A2(0xB)

    label("loc_8EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_936")
    SetChrPos(0x1, 970, 0, -49020, 0)

    def lambda_91E():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_91E)
    Jump("loc_962")

    label("loc_936")

    SetChrPos(0x1, -2029, 0, -48950, 0)

    def lambda_94D():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_94D)

    label("loc_962")

    OP_A2(0xB)

    label("loc_965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9B0")
    SetChrPos(0x2, 970, 0, -49020, 0)

    def lambda_998():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_998)
    Jump("loc_9DC")

    label("loc_9B0")

    SetChrPos(0x2, -2029, 0, -48950, 0)

    def lambda_9C7():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_9C7)

    label("loc_9DC")

    OP_A2(0xB)

    label("loc_9DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A2A")
    SetChrPos(0x3, 970, 0, -49020, 0)

    def lambda_A12():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_A12)
    Jump("loc_A56")

    label("loc_A2A")

    SetChrPos(0x3, -2029, 0, -48950, 0)

    def lambda_A41():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_A41)

    label("loc_A56")

    OP_A2(0xB)

    label("loc_A59")

    FadeToBright(2000, 0)
    OP_6E(350, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 600, 18060, 0)

    def lambda_A87():
        OP_6D(-610, 0, -1460, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A87)
    Sleep(1000)

    def lambda_AA4():
        OP_67(0, 3010, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA4)

    def lambda_ABC():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABC)
    Sleep(1000)

    def lambda_AD1():
        OP_6E(757, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD1)
    Sleep(2000)

    def lambda_AE6():
        OP_6D(130, 1600, 15530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AE6)

    def lambda_AFE():
        OP_6B(1490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFE)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)

    def lambda_B18():
        OP_6D(0, 270, 15110, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_B18)

    def lambda_B30():
        OP_67(0, 4960, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B30)
    Sleep(1000)
    SetChrFlags(0x10, 0x20)
    OP_8C(0x10, 180, 400)
    OP_44(0x10, 0xFF)
    WaitChrThread(0x102, 0x3)

    ChrTalk(
        0x10,
        (
            "#5P#110F……最后还是来了啊。\x02\x03",
            "#110F我还一直以为你们不会来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F理查德上校……\x02\x03",
            "受艾莉茜雅女王陛下的委托，\x01",
            "我们前来阻止你的计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F看来『福音』还没有开始启动。\x01",
            "　\x02\x03",
            "现在……还来得及。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#111F呵呵，那可不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你想做什么！？\x02\x03",
            "『辉之环』究竟是什么！？\x02\x03",
            "将那个东西弄到手，\x01",
            "到底是为了什么目的！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(30, 2000, 17430, 0)
    OP_67(0, 2970, -10000, 0)
    OP_6B(980, 0)
    OP_6C(0, 0)
    OP_6E(757, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#5P#111F当然是为了借助\x01",
            "上天赐予古代人的『七至宝』的力量，\x01",
            "去任意支配海洋、大地和天空。\x02\x03",
            "而这『辉之环』就是『七至宝』之一。\x02\x03",
            "假如这东西真的埋藏在这里的话……\x01",
            "　\x02\x03",
            "对于国家来说意味着什么，\x01",
            "我想你们应该不会不明白吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#1P对、对于国家……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E62")

    NpcTalk(
        0x102,
        "奥利维尔",
        (
            "#035F#2P能得到破坏力不亚于周边国家的\x01",
            "强有力的武器……\x02\x03",
            "#032F你是这样想的，没错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_F26")

    label("loc_E62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC6")

    NpcTalk(
        0x102,
        "科洛丝",
        (
            "#043F#2P可以得到能与周边国家抗衡的\x01",
            "强有力的武器……\x02\x03",
            "是这样，对吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_F26")

    label("loc_EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F26")

    NpcTalk(
        0x102,
        "金",
        (
            "#074F#2P能得到可以对抗周边国家的\x01",
            "强有力的武器……\x02\x03",
            "#072F是这样没错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F86")

    ChrTalk(
        0x102,
        (
            "#015F#2P可以得到能与周边诸国抗衡的\x01",
            "具有惊人杀伤力的武器……\x02\x03",
            "#012F你是这个意思吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F86")


    ChrTalk(
        0x10,
        (
            "#5P#111F没错……\x02\x03",
            "#115F你们稍微想想就会明白——\x01",
            "与周边国家相比，利贝尔的国力处于劣势。\x02\x03",
            "人口是卡尔瓦德的五分之一左右。\x02\x03",
            "至于兵力，\x01",
            "还不到埃雷波尼亚的八分之一。\x02\x03",
            "唯一占据优势的就只有导力技术，\x01",
            "可谁敢保证我们能一直保持领先。\x02\x03",
            "#112F为了不受到第二次的侵略，\x01",
            "我们一定要拥有决定性的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#5P就、就因为这样，\x01",
            "所以才非要取得这个古代物品不可吗！？\x01",
            "　\x02\x03",
            "那么十年前战争，\x01",
            "我们能够取得胜利靠的又是什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#116F之所以能够击退帝国军的侵略，\x01",
            "是因为有卡西乌斯·布莱特的存在。\x02\x03",
            "#115F可是，他已经从军队里退役了。\x02\x03",
            "守护国家的英雄离开了。\x02\x03",
            "#112F或许，也只有奇迹和空之女神\x01",
            "才能将那个深爱着自己爱人的英雄\x01",
            "再次召唤回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#110F因此，我就建立了情报部。\x02\x03",
            "至少，让王国在情报战方面\x01",
            "可以领先于其他国家一步……\x02\x03",
            "利用一切可能的情报网去探寻\x01",
            "能够给予利贝尔决定性力量的物品。\x01",
            "　\x02\x03",
            "当利贝尔陷入苦境的时候，\x01",
            "至少可以用它为国家再次带来奇迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#1P那个……不也是奇迹吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#113F什么……？\x02",
    )

    CloseMessageWindow()
    OP_6D(30, 2000, 13080, 1000)

    ChrTalk(
        0x101,
        (
            "#506F#3P嗯，就拿我们这些游击士来说吧，\x01",
            "守护大家所珍惜的东西是我们的工作……\x01",
            "　\x02\x03",
            "#501F可是，守护只是一个人的事情吗？\x01",
            "难道被守护的一方就不能守护别人吗？\x02\x03",
            "在守护对方的同时，\x01",
            "将『互相守护』这种信念传达出来，\x01",
            "这样，我觉得才是真正的守护。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#112F那……那又怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#3P十年前的战争，我老爸他，\x01",
            "并不是独自一人和帝国军战斗的。\x02\x03",
            "他是在许许多多人的帮助之下，\x01",
            "集合大家的力量一起守护这片国土。\x02\x03",
            "正因为大家相互扶持、相互信任，\x01",
            "所以，我们才取得了最终的胜利。\x02\x03",
            "上校你不也是其中的一个吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#112F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#3P对于今天发生在我们身上的这些事情，\x01",
            "我觉得也是同样的道理。\x02\x03",
            "当得知上校你的计划的时候，\x01",
            "我们根本不知道该怎么办才好……\x02\x03",
            "#006F可是，在许多朋友的帮助之下，\x01",
            "我们最终还是通过努力来到了这里啊。\x02\x03",
            "难道你不觉得这是一种奇迹吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#115F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#3P不过……\x01",
            "其实这并不是什么奇迹……\x02\x03",
            "我觉得，我们只是通过自身的努力拼搏，\x01",
            "让可能实现的事情真正地实现出来。\x02\x03",
            "#500F假如真的有一天，战争不幸爆发了……\x01",
            "　\x02\x03",
            "只要我们大家能够齐心协力，\x01",
            "我想，一定一定可以排除万难的。\x02\x03",
            "#508F与那来历不明的古代力量相比，\x01",
            "我们的信念、我们的努力才更加可靠啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CA")

    ChrTalk(
        0x106,
        "#051F呵呵，真是肺腑之言啊。\x02",
    )

    CloseMessageWindow()

    label("loc_17CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_181C")

    ChrTalk(
        0x104,
        (
            "#031F呵呵，不愧是艾丝蒂尔君。\x01",
            "这种乐观向上的精神的确值得嘉许。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185E")

    ChrTalk(
        0x105,
        (
            "#048F艾丝蒂尔……\x01",
            "说得很好，我也觉得是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1897")

    ChrTalk(
        0x108,
        "#071F哈哈，不愧是卡西乌斯大人的女儿。\x02",
    )

    CloseMessageWindow()

    label("loc_1897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18DB")

    ChrTalk(
        0x103,
        (
            "#021F真是的……\x01",
            "你这孩子什么时候变得如此成熟啦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1925")

    ChrTalk(
        0x107,
        (
            "#560F姐姐，你好棒啊……\x02\x03",
            "我也觉得那样才是对的呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1925")


    ChrTalk(
        0x10,
        (
            "#5P#118F呵呵……你还挺会说的嘛。\x02\x03",
            "的确，也许大家都会有这种信念，\x01",
            "但并非所有人都能像你那样坚强。\x02\x03",
            "当强大的力量就在你的面前时……\x01",
            "要想抵挡这种诱惑谈何容易。\x02\x03",
            "更何况，我为了这一刻的到来，\x01",
            "不知付出了多少的准备和心血。\x02\x03",
            "事到如今，难道要我就此罢手吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4P…………………………\x02\x03",
            "#012F……有一个问题，希望上校能解释一下。\x02\x03",
            "为什么上校你……\x01",
            "会知道这个地方的存在？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#113F什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P你竟然能找到这个连陛下也不知道其存在、\x01",
            "沉睡着禁断之力的古代遗迹……\x02\x03",
            "即使在宝物库建造了通向地下的导力梯，\x01",
            "也只能勉强到达这个遗迹的最上层而已……\x01",
            "　\x02\x03",
            "#012F难以想象单凭情报网的本事\x01",
            "竟然可以查到这个地方的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#112F那是因为……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P还有，那个『福音』……\x02\x03",
            "是使用凌驾于蔡斯中央工房之上的技术\x01",
            "所制造出来的谜之导力器……\x02\x03",
            "你究竟是从哪里得到那东西的？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#115F……我没有义务回答你这些问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F#4P不对……！\x02\x03",
            "对于我的种种疑问，\x01",
            "你根本就回答不出来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#117F#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#3P怎、怎么回事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F#4P虽然如此，你却对这里沉睡着『辉之环』\x01",
            "这样强大的古代遗物之事是如此地确信。\x01",
            "　\x02\x03",
            "而且，你也完全明白只有\x01",
            "得到黑色导力器才能将其唤醒。\x02\x03",
            "因此，这种种迹象都表明，\x01",
            "这一切的开端绝对不是你所想出来的。\x02\x03",
            "我说得对吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#117F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A3(0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(
        0x101,
        "#580F#3P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F和卢安的戴尔蒙市长类似，\x01",
            "他的记忆也很可能被人改动过了吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1F6F")

    label("loc_1E45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB6")

    ChrTalk(
        0x101,
        "#580F#3P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F和空贼团的首领一样，\x01",
            "他的记忆很可能也被人操纵着吗……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1F6F")

    label("loc_1EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F25")

    ChrTalk(
        0x101,
        "#580F#3P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F和那个克鲁茨一样，\x01",
            "他的记忆也很可能被人消除掉了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1F6F")

    label("loc_1F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6F")

    ChrTalk(
        0x101,
        (
            "#580F#3P这、这是……\x02\x03",
            "和那些失去记忆的人情况是一样的吗！？\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6F")


    ChrTalk(
        0x10,
        (
            "#5P#117F胡说八道！\x02\x03",
            "……强大力量的存在\x01",
            "就是这个地下遗迹的最有力证明！\x02\x03",
            "以我们现在的导力技术，\x01",
            "是绝不可能制造出那些人形兵器来的！\x02\x03",
            "所以我……\x01",
            "我会在我选择的道路上继续走下去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2028():
        OP_6B(1290, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2028)

    def lambda_2038():
        OP_6D(-100, 300, 15360, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2038)

    def lambda_2050():
        OP_67(0, 7570, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2050)

    def lambda_2068():
        OP_6C(35000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2068)
    OP_9F(0x12, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x12, -2000, 7300, 15360, 180)
    SetChrPos(0x13, 2000, 7300, 15360, 225)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x12, 27)
    SetChrChipByIndex(0x13, 27)

    def lambda_20CE():
        OP_96(0xFE, 0xFFFFF060, 0x0, 0x3C00, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20CE)
    OP_9F(0x12, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0x12, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0x12, 26)
    OP_99(0x12, 0x0, 0x3, 0x7D0)

    def lambda_2134():

        label("loc_2134")

        OP_99(0xFE, 0x3, 0x7, 0x514)
        OP_48()
        Jump("loc_2134")

    QueueWorkItem2(0x12, 1, lambda_2134)

    def lambda_2147():
        OP_96(0xFE, 0xFA0, 0x0, 0x3C00, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2147)
    OP_9F(0x13, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x13, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0x13, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0x13, 26)
    OP_99(0x13, 0x0, 0x3, 0x7D0)

    def lambda_21AD():

        label("loc_21AD")

        OP_99(0xFE, 0x3, 0x7, 0x514)
        OP_48()
        Jump("loc_21AD")

    QueueWorkItem2(0x13, 1, lambda_21AD)
    Sleep(1000)
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x1, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#118F如果你们所说的那些是真的，\x01",
            "就打败我，然后证明给我看吧……\x02\x03",
            "如果做不到这一点，\x01",
            "你们所说的也只不过是些幼稚的理想罢了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22AD():
        OP_6B(1000, 1000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_22AD)

    def lambda_22BD():
        OP_94(0x0, 0xFE, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_22BD)
    Sleep(100)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 28)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x10, 0x2)
    Sleep(400)

    ChrTalk(
        0x10,
        (
            "#5P#114F好好看看吧！\x01",
            "继承自『剑圣』的剑技！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#5P信口开河！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F#2P那么我们也不用客气，\x01",
            "让他知道我们也并非等闲之辈！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)

    def lambda_2383():
        OP_6D(-100, 300, 17360, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2383)

    def lambda_239B():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_239B)
    Sleep(20)

    def lambda_23B5():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23B5)
    Sleep(20)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_241D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2405")
    Sleep(20)

    def lambda_23F3():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_23F3)
    Jump("loc_241A")

    label("loc_2405")


    def lambda_240B():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_240B)

    label("loc_241A")

    OP_A2(0xB)

    label("loc_241D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_246E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2456")
    Sleep(20)

    def lambda_2444():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_2444)
    Jump("loc_246B")

    label("loc_2456")


    def lambda_245C():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_245C)

    label("loc_246B")

    OP_A2(0xB)

    label("loc_246E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_24A7")
    Sleep(20)

    def lambda_2495():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_2495)
    Jump("loc_24BC")

    label("loc_24A7")


    def lambda_24AD():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_24AD)

    label("loc_24BC")

    OP_A2(0xB)

    label("loc_24BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2510")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_24F8")
    Sleep(20)

    def lambda_24E6():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_24E6)
    Jump("loc_250D")

    label("loc_24F8")


    def lambda_24FE():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_24FE)

    label("loc_250D")

    OP_A2(0xB)

    label("loc_2510")

    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    OP_23(0x90)
    OP_83(0x19, 0x0)
    Battle(0x39C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2544"),
        (SWITCH_DEFAULT, "loc_2547"),
    )


    label("loc_2544")

    OP_B4(0x0)
    Return()

    label("loc_2547")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Call(0, 4)
    Return()

    # Function_3_708 end

    def Function_4_2574(): pass

    label("Function_4_2574")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_71(0x6, 0x4)
    OP_6F(0x6, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3E8)
    OP_71(0x0, 0x20)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_70(0x0, 0x3E8)
    OP_70(0x1, 0x3E8)
    OP_70(0x2, 0x3E8)
    OP_70(0x3, 0x3E8)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 29)
    SetChrPos(0x10, -710, 300, 15890, 180)
    SetChrPos(0x101, -760, 0, 12210, 7)
    SetChrPos(0x102, 530, 0, 12680, 344)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_267F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_266B")
    SetChrPos(0x0, -2370, 0, 13570, 34)
    Jump("loc_267C")

    label("loc_266B")

    SetChrPos(0x0, 1960, 0, 13940, 319)

    label("loc_267C")

    OP_A2(0xB)

    label("loc_267F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_26AF")
    SetChrPos(0x1, -2370, 0, 13570, 34)
    Jump("loc_26C0")

    label("loc_26AF")

    SetChrPos(0x1, 1960, 0, 13940, 319)

    label("loc_26C0")

    OP_A2(0xB)

    label("loc_26C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_26F3")
    SetChrPos(0x2, -2370, 0, 13570, 34)
    Jump("loc_2704")

    label("loc_26F3")

    SetChrPos(0x2, 1960, 0, 13940, 319)

    label("loc_2704")

    OP_A2(0xB)

    label("loc_2707")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_274B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2737")
    SetChrPos(0x3, -2370, 0, 13570, 34)
    Jump("loc_2748")

    label("loc_2737")

    SetChrPos(0x3, 1960, 0, 13940, 319)

    label("loc_2748")

    OP_A2(0xB)

    label("loc_274B")

    OP_6D(-940, 40, 14760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(326000, 0)
    OP_6E(262, 0)
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x1, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#5P#118F真不愧是……\x01",
            "卡西乌斯上校的孩子啊……\x02\x03",
            "不过……你们还是迟了一步。\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x5C)

    def lambda_2837():
        OP_6D(200, 2560, 18960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2837)

    def lambda_284F():
        OP_67(0, 5560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_284F)

    def lambda_2867():
        OP_6C(338000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2867)

    def lambda_2877():
        OP_6E(455, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2877)
    Sleep(1000)
    OP_22(0xB8, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp007_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F糟糕……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#513F#5P呜……！\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 1100)
    OP_70(0x5, 0x5DC)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x2, 1850)
    OP_6F(0x3, 1880)
    OP_6F(0x1, 1910)
    OP_6F(0x0, 1940)
    OP_70(0x0, 0x94C)
    OP_70(0x1, 0x94C)
    OP_70(0x2, 0x94C)
    OP_70(0x3, 0x94C)
    Sleep(4000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x64)

    def lambda_2981():

        label("loc_2981")

        OP_7C(0x0, 0x12C, 0xBB8, 0xBB8)
        OP_48()
        Jump("loc_2981")

    QueueWorkItem2(0x10, 1, lambda_2981)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C5")

    ChrTalk(
        0x107,
        "#068F#5P呀啊啊啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_29C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F1")

    ChrTalk(
        0x106,
        "#550F#5P可恶，这是……！\x02",
    )

    CloseMessageWindow()

    label("loc_29F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A21")

    ChrTalk(
        0x104,
        "#039F#5P这就是传说中的……！\x02",
    )

    CloseMessageWindow()

    label("loc_2A21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A68")

    ChrTalk(
        0x105,
        (
            "#046F#5P是让戴尔蒙市长的古代遗物\x01",
            "停止运作的光……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A9C")

    ChrTalk(
        0x108,
        "#077F#5P这是……『阴』的气息吗！\x02",
    )

    CloseMessageWindow()

    label("loc_2A9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AD7")

    ChrTalk(
        0x103,
        (
            "#523F#5P这是……\x01",
            "『导力停止现象』……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD7")


    def lambda_2ADD():
        OP_6D(-5080, 5590, -6070, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2ADD)

    def lambda_2AF5():
        OP_67(0, 4890, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AF5)

    def lambda_2B0D():
        OP_6B(4730, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B0D)

    def lambda_2B1D():
        OP_6C(44000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B1D)

    def lambda_2B2D():
        OP_6E(478, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2B2D)
    Sleep(1500)
    OP_44(0x10, 0x1)
    OP_22(0x91, 0x0, 0x64)
    LoadEffect(0x2, "map\\\\mp015_00.eff")
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x6, 0x4)
    OP_6F(0x6, 0)
    OP_70(0x6, 0xF0)
    Sleep(250)
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2574 end

    def Function_5_2C66(): pass

    label("Function_5_2C66")

    OP_9F(0xFE, 0x64, 0x64, 0xFF, 0xFF, 0x3E8)

    def lambda_2C77():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_2C77)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 27)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Return()

    # Function_5_2C66 end

    def Function_6_2C9D(): pass

    label("Function_6_2C9D")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 2380)
    OP_6F(0x1, 2380)
    OP_6F(0x2, 2380)
    OP_6F(0x3, 2380)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 29)
    SetChrPos(0x10, -710, 300, 15890, 180)
    SetChrPos(0x101, -760, 0, 12210, 7)
    SetChrPos(0x102, 530, 0, 12680, 344)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2D60")
    SetChrPos(0x0, -2370, 0, 13570, 34)
    Jump("loc_2D71")

    label("loc_2D60")

    SetChrPos(0x0, 1960, 0, 13940, 319)

    label("loc_2D71")

    OP_A2(0xB)

    label("loc_2D74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2DA4")
    SetChrPos(0x1, -2370, 0, 13570, 34)
    Jump("loc_2DB5")

    label("loc_2DA4")

    SetChrPos(0x1, 1960, 0, 13940, 319)

    label("loc_2DB5")

    OP_A2(0xB)

    label("loc_2DB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2DE8")
    SetChrPos(0x2, -2370, 0, 13570, 34)
    Jump("loc_2DF9")

    label("loc_2DE8")

    SetChrPos(0x2, 1960, 0, 13940, 319)

    label("loc_2DF9")

    OP_A2(0xB)

    label("loc_2DFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2E2C")
    SetChrPos(0x3, -2370, 0, 13570, 34)
    Jump("loc_2E3D")

    label("loc_2E2C")

    SetChrPos(0x3, 1960, 0, 13940, 319)

    label("loc_2E3D")

    OP_A2(0xB)

    label("loc_2E40")

    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E5D")
    SetChrChipByIndex(0x103, 14)

    label("loc_2E5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E70")
    SetChrChipByIndex(0x104, 16)

    label("loc_2E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E83")
    SetChrChipByIndex(0x106, 20)

    label("loc_2E83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E96")
    SetChrChipByIndex(0x105, 18)

    label("loc_2E96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EA9")
    SetChrChipByIndex(0x107, 22)

    label("loc_2EA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBC")
    SetChrChipByIndex(0x108, 24)

    label("loc_2EBC")

    OP_6D(-710, 5300, 15670, 0)
    OP_67(0, 10500, -25720, 0)
    OP_6B(640, 0)
    OP_6C(13000, 0)
    OP_6E(697, 0)
    FadeToBright(2000, 0)
    OP_6D(-710, 300, 15670, 3000)
    OP_0D()

    ChrTalk(
        0x101,
        "#580F怎、怎么了，刚才那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F虽然表现为导力停止现象，\x01",
            "但和以前的应该不一样……\x02\x03",
            "难道说，有什么东西被解封了……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)
    OP_22(0xB9, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)

    def lambda_2FB9():
        OP_6D(-560, 1650, 16460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FB9)
    OP_72(0x5, 0x4)
    OP_6F(0x5, 1300)
    OP_70(0x5, 0x3E8)
    Sleep(2000)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(1000)
    Fade(1000)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 1000)
    OP_70(0x5, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……警告……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警告全体人员……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#580F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P这个装置在说话……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『辉之环』封印结构的\x01",
            "第一结界已确认失效。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "推测为在封印区域的最深处\x01",
            "使用了『福音』……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『电子驱动塔』启动确认……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)
    OP_1D(0x23)
    Sleep(500)

    def lambda_319D():
        OP_6D(2820, 0, 40, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_319D)

    def lambda_31B5():
        OP_67(0, 19430, -25720, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31B5)

    def lambda_31CD():
        OP_6B(1410, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_31CD)

    def lambda_31DD():
        OP_6C(90000, 11000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_31DD)

    def lambda_31ED():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_31ED)

    def lambda_31FB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_31FB)

    def lambda_3209():
        OP_8C(0xFE, 132, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_3209)

    def lambda_3217():
        OP_8C(0xFE, 222, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_3217)
    Sleep(3000)
    OP_6F(0x0, 2380)
    OP_70(0x0, 0xB22)
    OP_6F(0x1, 2380)
    OP_70(0x1, 0xB22)
    OP_6F(0x2, 2380)
    OP_70(0x2, 0xB22)
    OP_6F(0x3, 2380)
    OP_70(0x3, 0xB22)
    OP_73(0x3)
    OP_22(0xBA, 0x0, 0x64)
    OP_6F(0x0, 2851)
    OP_70(0x0, 0xCA8)
    OP_6F(0x1, 2851)
    OP_70(0x1, 0xCA8)
    OP_6F(0x2, 2851)
    OP_70(0x2, 0xCA8)
    OP_6F(0x3, 2851)
    OP_70(0x3, 0xCA8)

    def lambda_32A2():
        OP_67(0, 13510, -25720, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_32A2)
    OP_73(0x3)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    Sleep(500)
    Fade(1000)
    OP_6F(0x6, 240)
    OP_0D()
    Fade(1000)
    OP_44(0x0, 0xFF)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 1100)
    OP_70(0x5, 0x578)
    OP_6D(-510, 300, 15530, 0)
    OP_67(0, 7800, -15530, 0)
    OP_6B(1000, 0)
    OP_6C(357000, 0)
    OP_6E(697, 0)
    OP_66(0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#005F这、这是什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F第一结界……\x01",
            "『辉之环』封印结构……\x02\x03",
            "上校，这到底是……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#117F不……不知道……\x02\x03",
            "……我根本没有想到\x01",
            "会演变成这种出乎意料的事态……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第一结界失效的同时，\x01",
            "从『环』内释放出微量干扰波……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『环之守护者』的封印解除确认……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全体相关人员，\x01",
            "请以最快的速度撤离封印区域……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_34AF():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_34AF)

    def lambda_34BD():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_34BD)

    def lambda_34CB():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_34CB)

    def lambda_34D9():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_34D9)

    def lambda_34E7():
        OP_6D(21480, 4400, 50, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34E7)

    def lambda_34FF():
        OP_6E(1000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34FF)

    def lambda_350F():
        OP_67(300, 4890, 20, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_350F)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x64, 0x3E418, 0x0)
    Sleep(100)
    StopSound(0x3A98, 0x9C40, 0x1770)
    Sleep(1900)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    OP_A1(0x17, 0x7)
    OP_A1(0x18, 0xA)
    OP_A1(0x19, 0xB)
    OP_72(0x7, 0x4)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 40)
    OP_70(0x7, 0x3B)
    SetChrPos(0x17, 49760, 0, 0, 90)
    SetChrPos(0x18, 36600, 3000, 4140, 90)
    SetChrPos(0x19, 36600, 3000, -4140, 90)
    OP_22(0xBB, 0x0, 0x64)
    OP_B0(0x4, 0x50)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3E8)

    def lambda_35FE():
        OP_6B(210, 14000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_35FE)

    def lambda_360E():
        OP_6E(180, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_360E)
    Sleep(7000)
    OP_20(0xBB8)

    def lambda_3628():
        OP_8F(0xFE, 0x2C88, 0xFA0, 0xCE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3628)

    def lambda_3643():
        OP_8F(0xFE, 0x2C88, 0xFA0, 0xFFFFF31C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3643)
    Sleep(3000)
    OP_72(0x7, 0x20)
    OP_73(0x7)
    OP_1D(0x2D)
    LoadEffect(0x5, "map\\\\mp030_0.eff")
    Play3DEffect(0x5, 0x0, 0x7, "Frame8_Bone__7_", 0x3B6, 0x258, 0x1F4, 0x0, 0x0, 0x0, 0x2BC, 0x2BC, 0x2BC, 0x0)
    Sleep(400)
    Play3DEffect(0x5, 0x1, 0x7, "Frame8_Bone__7_", 0x41A, 0xFFFFFF9C, 0x2BC, 0x0, 0x0, 0x0, 0x258, 0x258, 0x258, 0x0)
    Sleep(100)
    Play3DEffect(0x5, 0x2, 0x7, "Frame8_Bone__7_", 0x3B6, 0x12C, 0x384, 0x0, 0x0, 0x0, 0x2BC, 0x2BC, 0x2BC, 0x0)
    Sleep(100)
    Play3DEffect(0x5, 0x3, 0x7, "Frame8_Bone__7_", 0x47E, 0xC8, 0xFA, 0x0, 0x0, 0x0, 0x384, 0x384, 0x384, 0x0)

    def lambda_3767():
        OP_67(300, -500, 20, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3767)

    def lambda_377F():
        OP_6D(16980, 3210, 0, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_377F)

    def lambda_3797():
        OP_6B(700, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3797)

    def lambda_37A7():
        OP_6E(730, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37A7)
    Sleep(1000)
    OP_43(0x17, 0x3, 0x0, 0x7)
    WaitChrThread(0x18, 0x0)

    def lambda_37C8():
        OP_8C(0xFE, 45, 80)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_37C8)

    def lambda_37D6():
        OP_8F(0xFE, 0x2710, 0xBB8, 0x1A90, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_37D6)
    WaitChrThread(0x19, 0x0)

    def lambda_37F6():
        OP_8C(0xFE, 135, 80)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_37F6)

    def lambda_3804():
        OP_8F(0xFE, 0x2710, 0xBB8, 0xFFFFE570, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3804)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    WaitChrThread(0x17, 0x3)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0xFF)
    Fade(1500)
    OP_66(0x1)
    SetChrPos(0x0, 3380, 0, 950, 90)
    SetChrPos(0x1, 3480, 0, -870, 90)
    SetChrPos(0x3, 1900, 0, 2270, 90)
    SetChrPos(0x2, 2520, 0, -2190, 90)
    ClearMapFlags(0x10)
    OP_6D(9220, 1300, 140, 0)
    OP_67(0, 7430, -15660, 0)
    OP_6B(1680, 0)
    OP_6C(90000, 0)
    OP_6E(433, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#509F什、什么呀，这个难看的家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#016F各位，请不要放松警惕……\x01",
            "这家伙可是『环之守护者』！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_395C")

    ChrTalk(
        0x103,
        (
            "#023F哈哈……\x01",
            "这不是在做梦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_395C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3999")

    ChrTalk(
        0x104,
        (
            "#032F这个也是古代文明的遗物吗……！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3999")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39D6")

    ChrTalk(
        0x105,
        (
            "#042F竟然有这样的东西被封在里面……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_39D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A19")

    ChrTalk(
        0x107,
        (
            "#065F难以置信……\x01",
            "竟然有这么大的人形兵器……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3A19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A50")

    ChrTalk(
        0x106,
        (
            "#055F喂喂……要和它战斗吗！？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3A50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A93")

    ChrTalk(
        0x108,
        (
            "#077F不要被迷惑了！\x01",
            "这家伙……必定非同寻常！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3A93")

    WaitChrThread(0x0, 0x0)
    OP_72(0x7, 0x20)
    OP_73(0x7)

    def lambda_3AA6():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AA6)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#15A门电路固定……\x05\x02",
        )
    )

    Sleep(500)
    OP_B0(0x7, 0x8)
    OP_6F(0x7, 230)
    OP_70(0x7, 0xEC)
    OP_73(0x7)
    OP_22(0xED, 0x0, 0x64)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 237)
    OP_70(0x7, 0xF3)
    OP_73(0x7)
    OP_22(0xEE, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#15A导力供给恢复……\x05\x02",
        )
    )

    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B0(0x7, 0x7)
    OP_6F(0x7, 244)
    OP_70(0x7, 0xF9)
    OP_73(0x7)
    OP_22(0xED, 0x0, 0x64)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 250)
    OP_70(0x7, 0xFE)
    OP_73(0x7)
    OP_22(0xEE, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#15A再启动完成……\x05\x02",
        )
    )

    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 254)
    OP_70(0x7, 0x116)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#15AMODE：搜索入侵敌人……\x05\x02",
        )
    )

    OP_B0(0x7, 0x14)
    OP_6F(0x7, 279)
    OP_70(0x7, 0x120)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#10A坐标确认……\x05\x02",
        )
    )

    OP_B0(0x7, 0xA)
    OP_6F(0x7, 293)
    OP_70(0x7, 0x133)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#10A封印结构设施·最深处……\x05\x02",
        )
    )

    OP_B0(0x7, 0xF)
    OP_6F(0x7, 308)
    OP_70(0x7, 0x13B)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#10A『环之守护者』幻想乐曲…\x05\x02",
        )
    )

    OP_B0(0x7, 0xF)
    OP_6F(0x7, 289)
    OP_70(0x7, 0x124)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)
    OP_B0(0x7, 0xC)
    OP_6F(0x7, 316)
    OP_70(0x7, 0x144)
    OP_73(0x7)
    OP_B0(0x7, 0x9)
    OP_6F(0x7, 325)
    OP_70(0x7, 0x149)
    OP_73(0x7)
    OP_B0(0x7, 0x7)
    OP_6F(0x7, 330)
    OP_70(0x7, 0x14C)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#20A搜索入侵敌人、行动再次开始……\x05\x02",
        )
    )

    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0xBB8)
    Sleep(2000)
    OP_56(0x0)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x5A)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 333)
    OP_70(0x7, 0x17E)
    SetChrFlags(0x17, 0x4)

    def lambda_3DC1():
        OP_91(0x17, 0xFFFFD120, 0xFFFFE890, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3DC1)

    def lambda_3DDC():
        OP_6D(8900, 5600, 110, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3DDC)

    def lambda_3DF4():
        OP_6B(1380, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3DF4)

    def lambda_3E04():
        OP_67(0, -130, -18290, 500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3E04)
    Sleep(500)
    OP_44(0x17, 0xFF)
    OP_72(0x7, 0x8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    Battle(0x3A1, 0x100009, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_2C9D end

    def Function_7_3E44(): pass

    label("Function_7_3E44")

    OP_B0(0x7, 0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F72")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    def lambda_3E6F():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3E6F)
    OP_B0(0x7, 0xA)
    OP_6F(0x7, 141)
    OP_70(0x7, 0x92)
    OP_73(0x7)

    def lambda_3E9F():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3E9F)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 147)
    OP_70(0x7, 0x96)
    OP_73(0x7)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_4A(0x17, 0)
    Sleep(100)
    OP_4B(0x17, 0)

    def lambda_3EF2():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3EF2)
    OP_B0(0x7, 0xA)
    OP_6F(0x7, 151)
    OP_70(0x7, 0x9C)
    OP_73(0x7)

    def lambda_3F22():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3F22)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 157)
    OP_70(0x7, 0x9F)
    OP_73(0x7)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_4A(0x17, 0)
    Sleep(100)
    OP_4B(0x17, 0)
    Jump("loc_3E52")

    label("loc_3F72")

    OP_73(0x7)
    OP_6F(0x7, 180)
    OP_70(0x7, 0xD1)
    Sleep(1000)
    OP_22(0xEC, 0x0, 0x64)
    OP_73(0x7)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 40)
    OP_70(0x7, 0x3B)
    OP_B0(0x7, 0xF)
    Return()

    # Function_7_3E44 end

    def Function_8_3FA8(): pass

    label("Function_8_3FA8")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x17, 0x8)
    OP_72(0x8, 0x4)
    OP_6F(0x8, 20)
    OP_6D(-200, 7250, -130, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(134000, 0)
    OP_6E(434, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4077")
    SetChrChipByIndex(0x103, 14)

    label("loc_4077")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_408A")
    SetChrChipByIndex(0x104, 16)

    label("loc_408A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_409D")
    SetChrChipByIndex(0x106, 20)

    label("loc_409D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B0")
    SetChrChipByIndex(0x105, 18)

    label("loc_40B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40C3")
    SetChrChipByIndex(0x107, 22)

    label("loc_40C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D6")
    SetChrChipByIndex(0x108, 24)

    label("loc_40D6")

    SetChrPos(0x17, 5900, 0, -30, 90)
    SetChrPos(0x0, -6050, 0, -660, 90)
    SetChrPos(0x1, -6050, 0, 660, 90)
    SetChrPos(0x2, -4270, 0, -2020, 90)
    SetChrPos(0x3, -4270, 0, 2020, 90)
    OP_6F(0x8, 22)
    OP_70(0x8, 0x29)
    OP_71(0x8, 0x20)
    FadeToBright(1000, 0)
    OP_6D(-200, 2250, -130, 3000)

    ChrTalk(
        0x101,
        "#580F为、为什么打不倒它！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#016F它还打算继续吗！\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(200)
    Fade(1000)

    def lambda_41C5():
        OP_6C(90000, 11000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_41C5)
    OP_6D(5470, 1000, -180, 0)
    OP_67(0, 8560, -10000, 0)
    OP_6B(1940, 0)
    OP_6C(134000, 0)
    OP_6E(434, 0)
    OP_72(0x8, 0x20)
    OP_6F(0x8, 42)
    OP_70(0x8, 0x40)
    OP_21()
    OP_1D(0x2E)
    OP_73(0x8)
    OP_22(0xEF, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_6F(0x8, 65)
    OP_70(0x8, 0x50)
    Sleep(500)

    def lambda_4254():
        OP_6D(5470, 3000, -180, 5500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4254)

    def lambda_426C():
        OP_6B(3390, 600)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_426C)
    OP_73(0x8)
    OP_6F(0x8, 81)
    OP_70(0x8, 0x6B)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_73(0x8)
    OP_22(0xF0, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_6F(0x8, 108)
    OP_70(0x8, 0x6E)
    OP_73(0x8)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)

    def lambda_42D9():
        OP_6B(1870, 3500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_42D9)
    OP_6F(0x8, 112)
    OP_70(0x8, 0x97)
    OP_73(0x8)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    OP_44(0x0, 0x3)

    def lambda_430F():
        OP_67(0, 160, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_430F)
    OP_22(0xF1, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x8, 152)
    OP_70(0x8, 0xAE)
    OP_73(0x8)
    OP_22(0xF1, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    def lambda_435C():
        OP_6B(1870, 2600)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_435C)
    OP_6F(0x8, 175)
    OP_70(0x8, 0xCE)
    OP_73(0x8)
    OP_22(0xF2, 0x0, 0x64)

    def lambda_4382():
        OP_6E(651, 300)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4382)

    def lambda_4392():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4392)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_6F(0x8, 207)
    OP_70(0x8, 0xFA)
    Sleep(300)

    def lambda_43C6():
        OP_6E(409, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_43C6)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 251)
    OP_70(0x8, 0x10E)
    WaitChrThread(0x0, 0x3)
    WaitChrThread(0x0, 0x2)
    OP_44(0x0, 0xFF)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#15AMODE：彻底歼灭……\x05\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    Sleep(2000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#10A『环之守护者』幻想乐曲…\x05\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    Sleep(1500)
    OP_B0(0x7, 0xC)
    OP_6F(0x7, 316)
    OP_70(0x7, 0x144)
    OP_73(0x7)
    OP_B0(0x7, 0x9)
    OP_6F(0x7, 325)
    OP_70(0x7, 0x149)
    OP_73(0x7)
    OP_B0(0x7, 0x7)
    OP_6F(0x7, 330)
    OP_70(0x7, 0x14C)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#20A现在再次展开歼灭行动……\x05\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xBB8)
    Sleep(2000)
    OP_56(0x0)
    OP_72(0x8, 0x20)
    OP_73(0x8)

    def lambda_4515():
        OP_67(0, 4190, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4515)

    def lambda_452D():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_452D)
    OP_6F(0x8, 320)
    OP_70(0x8, 0x14E)
    OP_73(0x8)
    LoadEffect(0x4, "map\\\\mp021_04.eff")
    PlayEffect(0x4, 0xFF, 0xFF, 5470, 3000, -180, 0, 90, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_22(0xF3, 0x0, 0x64)

    def lambda_459C():
        OP_6B(6000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_459C)
    OP_7C(0x0, 0x1F4, 0xBB8, 0xBB8)
    OP_6F(0x8, 336)
    OP_70(0x8, 0x159)
    Sleep(1000)
    OP_44(0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3A2, 0x100008, 0x0, 0x80, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_45F0"),
        (SWITCH_DEFAULT, "loc_45F3"),
    )


    label("loc_45F0")

    OP_B4(0x0)
    Return()

    label("loc_45F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4602")
    OP_83(0x19, 0x1)

    label("loc_4602")

    OP_71(0x8, 0x4)
    Call(0, 9)
    Return()

    # Function_8_3FA8 end

    def Function_9_460C(): pass

    label("Function_9_460C")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)
    OP_3F(0x357, 1)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x17, 0x9)
    OP_72(0x9, 0x4)
    OP_6F(0x9, 275)
    OP_6D(1640, 0, -1300, 0)
    OP_67(0, 6640, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(111000, 0)
    OP_6E(418, 0)
    SetChrPos(0x17, 5900, 0, -30, 75)
    SetChrPos(0x10, -4780, 0, 6090, 137)
    SetChrFlags(0x10, 0x80)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 29)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    SetChrPos(0x101, -2910, 0, -3850, 47)
    SetChrPos(0x102, -1740, 0, -6390, 6)
    SetChrPos(0x0, -4710, 0, 610, 127)
    SetChrPos(0x1, -5270, 0, -1970, 111)
    SetChrChipByIndex(0x101, 37)
    SetChrChipByIndex(0x102, 38)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4770")
    SetChrChipByIndex(0x103, 39)

    label("loc_4770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4783")
    SetChrChipByIndex(0x104, 40)

    label("loc_4783")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4796")
    SetChrChipByIndex(0x106, 42)

    label("loc_4796")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A9")
    SetChrChipByIndex(0x105, 41)

    label("loc_47A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47BC")
    SetChrChipByIndex(0x107, 43)

    label("loc_47BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47CF")
    SetChrChipByIndex(0x108, 44)

    label("loc_47CF")

    SetChrSubChip(0x0, 3)
    SetChrSubChip(0x1, 3)
    SetChrSubChip(0x2, 3)
    SetChrSubChip(0x3, 3)
    LoadEffect(0x0, "monster\\\\ms10000.eff")
    LoadEffect(0x1, "monster\\\\ms10001.eff")
    LoadEffect(0x2, "monster\\\\ms10002.eff")
    LoadEffect(0x3, "monster\\msc0270b.eff")

    def lambda_4845():
        OP_6B(2530, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4845)

    def lambda_4855():
        OP_6C(69000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4855)
    Sleep(4000)

    ChrTalk(
        0x101,
        (
            "#581F呼呼……\x02\x03",
            "总算、总算打倒了……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F嗯……\x01",
            "好像已经不能动了……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 36)
    SetChrSubChip(0x10, 0)
    OP_66(0x0)
    OP_6D(-880, 0, 620, 2000)

    ChrTalk(
        0x10,
        (
            "#5P#112F『环之守护者』……\x02\x03",
            "这家伙本来的使命应该是为了\x01",
            "将意图封印『辉之环』的设施破坏掉……\x01",
            "　\x02\x03",
            "然而在『辉之环』成功被封印的同时，\x01",
            "它也在刚才的门里停止了机能……\x02\x03",
            "#115F难道说……围绕着这个『辉之环』，\x01",
            "古代人曾有那么一段互相对立的历史？\x01",
            "还是另有……\x02\x03",
            "#116F可是……\x01",
            "关键的『辉之环』在哪里……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_B0(0x9, 0x3)
    OP_6F(0x9, 275)
    OP_70(0x9, 0x118)
    Sleep(1000)
    OP_62(0x0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_21()
    OP_73(0x9)
    OP_B0(0x9, 0xC)
    OP_6F(0x9, 281)
    OP_70(0x9, 0x11D)
    OP_73(0x9)
    OP_1D(0x2D)
    OP_B0(0x9, 0x14)
    OP_6F(0x9, 286)
    OP_70(0x9, 0x127)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEC, 0x0, 0x64)

    ChrTalk(
        0x10,
        (
            "#113F#5P#10A怎么……\x01",
            "它还能动吗！？\x05\x02",
        )
    )

    OP_72(0x9, 0x20)
    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x1770)
    Sleep(900)

    def lambda_4B32():
        OP_6D(1630, 550, -840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B32)
    OP_43(0x17, 0x1, 0x0, 0xA)
    Sleep(500)
    WaitChrThread(0x17, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B90")

    ChrTalk(
        0x103,
        (
            "#522F#5P呜……\x01",
            "身体动弹不了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4B90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BD5")

    ChrTalk(
        0x104,
        (
            "#034F#5P竟、竟然让本人完全不能动弹……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4BD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C14")

    ChrTalk(
        0x106,
        (
            "#550F#5P可恶……\x01",
            "身体完全不听使唤！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4C14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C50")

    ChrTalk(
        0x107,
        "#069F#5P啊，我已经站不起来了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C88")

    ChrTalk(
        0x108,
        "#077F#5P呜……还是不行吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4C88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CC0")

    ChrTalk(
        0x105,
        (
            "#541F#5P已经……动不了了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CC0")


    ChrTalk(
        0x101,
        "#581F#5P约、约修亚……！\x02",
    )

    CloseMessageWindow()
    OP_66(0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#016F#2P艾丝蒂尔……！\x02",
    )

    CloseMessageWindow()

    def lambda_4D08():

        label("loc_4D08")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4D08")

    QueueWorkItem2(0x102, 2, lambda_4D08)
    SetChrChipByIndex(0x102, 12)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0x102, 0xFFFFFA1A, 0x0, 0xFFFFF358, 0x1F4, 0xFA0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x9, 0x20)
    OP_73(0x9)
    OP_B0(0x9, 0x6)
    OP_6F(0x9, 210)
    OP_70(0x9, 0xD5)

    def lambda_4D5D():
        OP_6C(70000, 1700)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D5D)

    def lambda_4D6D():
        OP_67(0, -1770, -30160, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4D6D)

    def lambda_4D85():
        OP_6D(2730, 3000, -2190, 1700)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4D85)

    def lambda_4D9D():
        OP_6B(770, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4D9D)
    OP_73(0x9)
    OP_B0(0x9, 0x6)
    OP_6F(0x9, 214)
    OP_70(0x9, 0xDD)
    OP_73(0x9)
    WaitChrThread(0x0, 0x1)
    SetChrPos(0x1A, 1980, 5000, 1220, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0x3E8)
    OP_B0(0x9, 0xD)
    OP_73(0x9)
    OP_6F(0x9, 222)
    OP_70(0x9, 0xE2)
    OP_73(0x9)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 28)
    SetChrPos(0x10, -440, 0, 4310, 119)
    SetChrPos(0x1B, -440, 0, 4310, 119)
    SetChrPos(0x1C, -440, 0, 4310, 119)
    SetChrPos(0x1D, -440, 0, 4310, 119)
    SetChrPos(0x1E, -440, 0, 4310, 119)

    def lambda_4EA3():
        OP_6D(1680, 1900, 600, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4EA3)

    def lambda_4EBB():
        OP_67(0, 12070, -30160, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4EBB)

    def lambda_4ED3():
        OP_6B(740, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4ED3)

    def lambda_4EE3():
        OP_6C(18000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4EE3)

    def lambda_4EF3():
        OP_6E(512, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4EF3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0x258, 0xBB8, 0x64)

    def lambda_4F1D():
        OP_8C(0xFE, 120, 50)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4F1D)
    OP_8C(0x17, 110, 0)
    OP_B0(0x9, 0xD)
    OP_6F(0x9, 227)
    OP_70(0x9, 0x103)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 50)
    OP_70(0x9, 0x45)
    WaitChrThread(0x0, 0x3)

    ChrTalk(
        0x101,
        "#5P#004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#114F……休想得逞！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#5P上、上校……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#112F这家伙由我来对付！\x02\x03",
            "你们赶快离开这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#5P可、可是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#114F你们刚才已经和这家伙拼死战斗过了！\x01",
            "　\x02\x03",
            "所以，我也应该做些什么了！\x02\x03",
            "或多或少可以拖延一些时间！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x10, 0x4)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x1B, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)

    def lambda_50F7():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_50F7)
    Sleep(50)

    def lambda_5117():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_5117)
    Sleep(50)

    def lambda_5137():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_5137)
    Sleep(50)

    def lambda_5157():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_5157)
    Sleep(50)

    def lambda_5177():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5177)
    WaitChrThread(0x10, 0x0)
    Fade(1000)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(6200, 3370, 160, 0)
    OP_67(0, 12070, -30160, 0)
    OP_6B(850, 0)
    OP_6C(152000, 0)
    OP_6E(512, 0)

    def lambda_5213():
        OP_6D(5750, 2370, -170, 15000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5213)

    def lambda_522B():
        OP_67(0, 4050, -30160, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_522B)

    def lambda_5243():
        OP_6B(970, 15000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5243)

    def lambda_5253():
        OP_6C(97000, 15000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5253)

    def lambda_5263():
        OP_6E(561, 15000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_5263)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrChipByIndex(0x1B, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)
    SetChrChipByIndex(0x10, 8)
    SetChrPos(0x1B, 5370, 0, 710, 139)
    SetChrPos(0x1C, 5370, 0, 710, 139)
    SetChrPos(0x1D, 5370, 0, 710, 139)
    SetChrPos(0x1E, 5370, 0, 710, 139)
    SetChrPos(0x10, 5370, 0, 710, 139)
    OP_72(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_43(0x10, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xD)
    WaitChrThread(0x10, 0x0)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_73(0x9)
    OP_6F(0x9, 510)
    OP_70(0x9, 0x212)
    OP_43(0x10, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xE)
    Sleep(600)
    OP_22(0xED, 0x0, 0x64)
    OP_73(0x9)
    OP_22(0x55, 0x0, 0x64)
    OP_7C(0x0, 0x3E8, 0xBB8, 0x64)
    OP_43(0x10, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_7C(0x0, 0xC8, 0xBB8, 0xBB8)
    OP_43(0x1C, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xF)
    WaitChrThread(0x10, 0x0)
    OP_7C(0x0, 0x1, 0xBB8, 0xA)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 3900, 3300, 1120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x9, 227)
    OP_70(0x9, 0xFE)
    OP_43(0x10, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x10)
    WaitChrThread(0x10, 0x0)
    OP_73(0x9)
    OP_43(0x10, 0x0, 0x0, 0x11)
    Sleep(430)
    OP_B0(0x9, 0x32)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x73)
    Sleep(200)
    OP_B0(0x9, 0x32)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x73)
    Sleep(200)
    OP_B0(0x9, 0x50)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_73(0x9)
    OP_6F(0x9, 510)
    OP_70(0x9, 0x213)
    Sleep(200)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    def lambda_562C():
        OP_8C(0xFE, 46, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_562C)
    Sleep(650)
    OP_22(0xED, 0x0, 0x64)
    OP_73(0x9)
    OP_6F(0x9, 227)
    OP_70(0x9, 0xFE)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_565A():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_565A)
    SetChrSubChip(0x10, 7)
    Sleep(200)

    def lambda_567F():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_567F)
    Sleep(200)

    def lambda_569F():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_569F)
    Sleep(200)

    def lambda_56BF():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56BF)

    def lambda_56DA():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_56DA)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1B, 0x80)
    OP_43(0x1B, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1C, 0x80)
    OP_43(0x1C, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1D, 0x80)
    OP_43(0x1D, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1E, 0x80)
    OP_43(0x1E, 0x0, 0x0, 0x12)
    Sleep(350)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x70)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 1500, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2500, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_73(0x9)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x70)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2800, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 3300, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2800, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2500, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 50)
    OP_70(0x9, 0x45)

    ChrTalk(
        0x101,
        "#004F#2P好、好厉害……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#2P不愧是继承了父亲的剑术……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    TurnDirection(0x10, 0x101, 800)

    ChrTalk(
        0x10,
        (
            "#5P#114F还在那做什么！\x01",
            "快走！！\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x9, 0x20)

    def lambda_598E():
        OP_6B(640, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_598E)

    def lambda_599E():
        OP_6C(139000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_599E)

    def lambda_59AE():
        OP_6D(390, 0, 1360, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_59AE)

    def lambda_59C6():
        OP_6E(561, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_59C6)

    def lambda_59D6():
        OP_67(0, 16200, -30160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_59D6)

    def lambda_59EE():
        OP_8C(0xFE, 90, 100)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_59EE)
    OP_B0(0x9, 0x32)
    OP_6F(0x9, 489)
    OP_70(0x9, 0x1BC)
    OP_73(0x9)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 443)
    OP_70(0x9, 0x1A5)
    Sleep(60)
    OP_96(0x10, 0xFFFFFFB0, 0x0, 0x942, 0x1F4, 0x1770)
    OP_8C(0x10, 14, 800)
    OP_73(0x9)
    OP_22(0x55, 0x0, 0x50)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    WaitChrThread(0x10, 0x1)
    Sleep(100)
    SetChrChipByIndex(0x10, 33)
    OP_22(0x1F8, 0x0, 0x64)
    OP_99(0x10, 0x0, 0x1, 0x7D0)

    def lambda_5A7C():
        OP_6D(0, 2800, -50, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5A7C)

    def lambda_5A94():
        OP_67(0, 15760, -30160, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5A94)

    def lambda_5AAC():
        OP_6C(130000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5AAC)
    OP_9E(0x10, 0x50, 0x0, 0xFA, 0x7530)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 100, 1000, 3150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_5B1D():
        OP_99(0xFE, 0x2, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5B1D)
    OP_B0(0x9, 0x96)
    OP_6F(0x9, 421)
    OP_70(0x9, 0x1BB)
    OP_43(0x20, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_43(0x1B, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_7C(0x0, 0x64, 0xBB8, 0x1388)
    OP_43(0x1C, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_43(0x1D, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_43(0x1E, 0x0, 0x0, 0x13)
    OP_73(0x9)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 444)
    OP_70(0x9, 0x1E9)
    Sleep(400)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_5BB8():
        OP_8F(0xFE, 0x33E, 0x0, 0x50A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_5BB8)

    def lambda_5BD3():
        OP_99(0xFE, 0x6, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5BD3)

    def lambda_5BE3():

        label("loc_5BE3")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_5BE3")

    QueueWorkItem2(0x10, 2, lambda_5BE3)
    Sleep(1300)
    Sleep(100)

    def lambda_5BFE():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5BFE)
    OP_73(0x9)

    def lambda_5C0F():
        OP_6B(680, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5C0F)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 515)
    OP_70(0x9, 0x20E)
    OP_73(0x9)
    OP_22(0xED, 0x0, 0x64)
    OP_6F(0x9, 527)
    OP_70(0x9, 0x212)
    OP_73(0x9)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3160, 1480, 1320, 0)

    ChrTalk(
        0x10,
        "#10A#117F呜、呜哦哦哦哦！？\x05\x02",
    )

    OP_B0(0x9, 0xF)
    OP_6F(0x9, 531)
    OP_70(0x9, 0x24B)
    WaitChrThread(0x0, 0x3)

    def lambda_5CA1():
        OP_67(0, 6790, -30160, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5CA1)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_6F(0x9, 588)
    OP_70(0x9, 0x25F)

    ChrTalk(
        0x101,
        "#580F#2P上、上校！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F#2P可恶……怎么办！？\x02",
    )

    CloseMessageWindow()

    def lambda_5D09():
        OP_6D(5700, 2800, 380, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5D09)

    ChrTalk(
        0x10,
        (
            "#5P#117F快、快点离开这里！\x02\x03",
            "在和你们的决斗失败之时……\x01",
            "我的命运……就已经到尽头了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#1P怎、怎么会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#118F因此……\x01",
            "你们不用在意……\x02\x03",
            "我的计划还是以失败告终了……\x02\x03",
            "在最后的时刻可以帮助你们，\x01",
            "算是表达……我的歉意吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, 260, 0, -8970, 154)

    NpcTalk(
        0x11,
        "男性的声音",
        "#1P哎呀呀……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "男性的声音",
        (
            "#1P只要坚持自己的信念，\x01",
            "就一定会找到取胜的机会。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "男性的声音",
        "#1P我教给你的这些，难道都忘记了吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x15E, 2400, 0x2, 0x7, 0x50, 0x1)
    WaitChrThread(0x0, 0x0)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "craft\\\\cr201_01.eff")
    LoadEffect(0x2, "monster\\\\ms10002.eff")
    LoadEffect(0x3, "monster\\\\ms10001.eff")
    LoadEffect(0x4, "map\\\\mp021_04.eff")
    SoundLoad(132)
    SoundLoad(521)
    SoundLoad(136)
    SetChrFlags(0x20, 0x80)
    OP_72(0x9, 0x20)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0x8)
    OP_6F(0x9, 588)
    OP_70(0x9, 0x25F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_6947")
    OP_A3(0x7)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5FBD():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5FBD)

    def lambda_5FCF():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xC8, 0x2BC)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_5FCF)

    def lambda_5FE1():
        OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0xA0, 0x384)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_5FE1)

    def lambda_5FF3():
        OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x78, 0x44C)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_5FF3)

    def lambda_6005():
        OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x50, 0x514)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_6005)

    def lambda_6017():
        OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x28, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_6017)
    OP_43(0x11, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1F, 0x0, 0x0, 0x15)

    def lambda_606C():
        OP_6D(5630, 2800, -60, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_606C)

    def lambda_6084():
        OP_67(0, 16840, -30160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6084)

    def lambda_609C():
        OP_6B(510, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_609C)

    def lambda_60AC():
        OP_6C(73000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_60AC)

    def lambda_60BC():
        OP_6E(926, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_60BC)
    OP_A6(0x7)
    OP_A3(0x7)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 4650, 2500, 3240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x11,
        "#10A嘿呀！\x05\x02",
    )

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x9, 0x20)
    OP_B0(0x9, 0xD)
    OP_6F(0x9, 646)
    OP_70(0x9, 0x2AC)
    OP_43(0x10, 0x0, 0x0, 0x14)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 685)
    OP_70(0x9, 0x2BF)
    WaitChrThread(0x0, 0x0)

    ChrTalk(
        0x101,
        "#004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P难道是……！\x02",
    )

    CloseMessageWindow()
    OP_72(0x9, 0x20)

    def lambda_61A1():
        OP_6D(5610, 1150, -1750, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_61A1)

    def lambda_61B9():
        OP_67(0, 26710, -30160, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_61B9)

    def lambda_61D1():
        OP_6B(460, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_61D1)

    def lambda_61E1():
        OP_6C(18000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_61E1)

    def lambda_61F1():
        OP_6E(698, 5000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_61F1)
    OP_43(0x11, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1B, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1C, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1D, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1E, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1F, 0x0, 0x0, 0x16)
    OP_A3(0x7)
    OP_A6(0x7)
    OP_A3(0x7)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 5190, 0, -3170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x11,
        "#10A嘿呀！\x05\x02",
    )

    OP_6F(0x9, 746)
    OP_70(0x9, 0x305)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    WaitChrThread(0x11, 0x0)
    Sleep(900)
    OP_43(0x11, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1B, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1C, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1D, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1E, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1F, 0x0, 0x0, 0x17)
    OP_A3(0x7)
    OP_73(0x9)
    OP_A2(0x7)
    Sleep(350)
    PlayEffect(0x3, 0xFF, 0xFF, 5690, 4400, -2090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_22(0x88, 0x0, 0x64)

    ChrTalk(
        0x11,
        "#10A喝————！\x05\x02",
    )

    Sleep(100)
    OP_6F(0x9, 774)
    OP_70(0x9, 0x31B)
    Sleep(215)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0xFF, 0xFF, 6210, 400, -720, 0, 90, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x7D0, 0x64)
    OP_73(0x9)
    Sleep(1000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Fade(1500)
    OP_6D(6150, 200, -1670, 0)
    OP_67(0, 19180, -30160, 0)
    OP_6B(500, 0)
    OP_6C(66000, 0)
    OP_6E(702, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_643C():
        OP_6D(6150, 850, -1670, 4500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_643C)

    def lambda_6454():
        OP_6C(135000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6454)

    def lambda_6464():
        OP_67(0, 11370, -30160, 4500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6464)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x11, 0, 0, 0, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    Sleep(1250)
    OP_B0(0x9, 0x8)
    OP_6F(0x9, 796)
    OP_70(0x9, 0x32F)
    OP_73(0x9)
    WaitChrThread(0x0, 0x2)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)

    def lambda_64DD():
        OP_6B(590, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_64DD)

    def lambda_64ED():
        OP_6D(7980, 1430, -610, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_64ED)
    OP_22(0x84, 0x0, 0x64)
    OP_43(0x11, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1B, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1C, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1D, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1E, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1F, 0x0, 0x0, 0x18)
    OP_22(0x209, 0x0, 0x64)
    OP_4A(0x0, 255)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x11, 0)
    SetChrSubChip(0x1B, 7)
    SetChrSubChip(0x1C, 7)
    SetChrSubChip(0x1D, 7)
    SetChrSubChip(0x1E, 7)
    SetChrSubChip(0x11, 7)
    OP_6F(0x9, 816)
    OP_82(0x1, 0x0)
    OP_20(0xBB8)
    PlayEffect(0x2, 0xFF, 0xFF, 5800, 2800, -720, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6B(480, 500)
    OP_4B(0x0, 255)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x11, 0)
    OP_22(0xF6, 0x0, 0x64)

    ChrTalk(
        0x11,
        "#10A哼！\x05\x02",
    )

    LoadEffect(0x4, "map\\\\mp031_0.eff")
    PlayEffect(0x4, 0xFF, 0xFF, 7600, 1730, -590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0xBB8)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 816)
    OP_70(0x9, 0x34B)
    OP_73(0x9)
    Fade(1000)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_44(0x11, 0xFF)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x11, 13)
    OP_21()

    ChrTalk(
        0x11,
        "呼……这种东西。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#080F我回来了。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "真是好久没见了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(3230, 700, -1570, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3510, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1170, 0, 380, 0)
    SetChrPos(0x102, -1160, 0, -890, 0)
    SetChrPos(0x0, -400, 0, -2790, 0)
    SetChrPos(0x1, 2090, 0, -3410, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_67AE():

        label("loc_67AE")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_67AE")

    QueueWorkItem2(0x0, 3, lambda_67AE)

    def lambda_67BF():

        label("loc_67BF")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_67BF")

    QueueWorkItem2(0x1, 3, lambda_67BF)

    def lambda_67D0():

        label("loc_67D0")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_67D0")

    QueueWorkItem2(0x2, 3, lambda_67D0)

    def lambda_67E1():

        label("loc_67E1")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_67E1")

    QueueWorkItem2(0x3, 3, lambda_67E1)
    OP_0D()

    ChrTalk(
        0x101,
        "#580F老、老、老……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#5S老爸！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_6838():
        OP_6D(190, 0, -590, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6838)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0x924, 0x0, 0xFFFFFD76, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x11, 10)
    Sleep(200)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0x294, 0x0, 0xFFFFFD44, 0x1F4, 0x7D0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(
        0x11,
        (
            "#085F虽然经历了不少修行，\x01",
            "可是还差得很远呢。\x02\x03",
            "#080F不过，这次就算你们合格吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F什、什么合格不合格啊！\x02\x03",
            "怎么回事啊，老爸！\x01",
            "你怎么会跑这里来了！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_733E")

    label("loc_6947")

    OP_A3(0x7)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_6992():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_6992)

    def lambda_69A4():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xC8, 0x2BC)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_69A4)

    def lambda_69B6():
        OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0xA0, 0x384)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_69B6)

    def lambda_69C8():
        OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x78, 0x44C)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_69C8)

    def lambda_69DA():
        OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x50, 0x514)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_69DA)

    def lambda_69EC():
        OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x28, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_69EC)
    OP_43(0x11, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1F, 0x0, 0x0, 0x19)

    def lambda_6A41():
        OP_6D(2340, 1150, 10, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6A41)

    def lambda_6A59():
        OP_67(0, 8830, -30160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6A59)

    def lambda_6A71():
        OP_6B(640, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6A71)

    def lambda_6A81():
        OP_6C(82000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6A81)

    def lambda_6A91():
        OP_6E(602, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_6A91)
    OP_A6(0x7)
    OP_A3(0x7)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 4650, 2500, 3240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x11,
        "#10A嘿呀！\x05\x02",
    )

    OP_20(0x5DC)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x102, 0x17, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B2C")
    SetChrChipByIndex(0x103, 14)
    TurnDirection(0x103, 0x17, 0)

    label("loc_6B2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B46")
    SetChrChipByIndex(0x104, 16)
    TurnDirection(0x104, 0x17, 0)

    label("loc_6B46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B60")
    SetChrChipByIndex(0x106, 20)
    TurnDirection(0x106, 0x17, 0)

    label("loc_6B60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B7A")
    SetChrChipByIndex(0x105, 18)
    TurnDirection(0x105, 0x17, 0)

    label("loc_6B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B94")
    SetChrChipByIndex(0x107, 22)
    TurnDirection(0x107, 0x17, 0)

    label("loc_6B94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BAE")
    SetChrChipByIndex(0x108, 24)
    TurnDirection(0x108, 0x17, 0)

    label("loc_6BAE")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x9, 0x20)
    OP_B0(0x9, 0xD)
    OP_6F(0x9, 646)
    OP_70(0x9, 0x2AC)
    OP_43(0x10, 0x0, 0x0, 0x14)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 685)
    OP_70(0x9, 0x2BF)
    WaitChrThread(0x0, 0x0)

    ChrTalk(
        0x101,
        "#004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P难道是……！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x11, 13)
    TurnDirection(0x11, 0x101, 800)
    OP_21()
    OP_1D(0x2B)
    Sleep(500)

    ChrTalk(
        0x11,
        "#5P#087F就是现在！把它彻底击溃！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_31(0x0, 0xFA, 0x1)
    OP_31(0x1, 0xFA, 0x1)
    OP_31(0x2, 0xFA, 0x1)
    OP_31(0x3, 0xFA, 0x1)
    OP_31(0x4, 0xFA, 0x1)
    OP_31(0x5, 0xFA, 0x1)
    OP_31(0x6, 0xFA, 0x1)
    OP_31(0x7, 0xFA, 0x1)
    OP_31(0x0, 0x5, 0xC8)
    OP_31(0x1, 0x5, 0xC8)
    OP_31(0x2, 0x5, 0xC8)
    OP_31(0x3, 0x5, 0xC8)
    OP_31(0x4, 0x5, 0xC8)
    OP_31(0x5, 0x5, 0xC8)
    OP_31(0x6, 0x5, 0xC8)
    OP_31(0x7, 0x5, 0xC8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CF4")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xFF)

    label("loc_6CF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D08")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xFF)

    label("loc_6D08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D1C")
    RemoveParty(0x5, 0xFF)
    AddParty(0x5, 0xFF)

    label("loc_6D1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D30")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xFF)

    label("loc_6D30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D44")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF)

    label("loc_6D44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D58")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xFF)

    label("loc_6D58")

    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D75")
    SetChrChipByIndex(0x103, 14)

    label("loc_6D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D8B")
    SetChrChipByIndex(0x104, 16)
    OP_A2(0x6F5)

    label("loc_6D8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D9E")
    SetChrChipByIndex(0x106, 20)

    label("loc_6D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DB1")
    SetChrChipByIndex(0x105, 18)

    label("loc_6DB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DC4")
    SetChrChipByIndex(0x107, 22)

    label("loc_6DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DD7")
    SetChrChipByIndex(0x108, 24)

    label("loc_6DD7")

    SetChrPos(0x101, -2910, 0, -3850, 47)
    SetChrPos(0x102, -1510, 0, -3240, 47)
    SetChrPos(0x2, -4710, 0, 610, 127)
    SetChrPos(0x3, -5270, 0, -1970, 111)
    TurnDirection(0x0, 0x17, 0)
    TurnDirection(0x1, 0x17, 0)
    TurnDirection(0x2, 0x17, 0)
    TurnDirection(0x3, 0x17, 0)
    OP_83(0x19, 0x0)
    Battle(0x3B3, 0x10000A, 0x0, 0x0, 0xFF)
    OP_83(0x19, 0x1)
    EventBegin(0x0)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x17, 0x9)
    OP_72(0x9, 0x20)
    OP_72(0x9, 0x4)
    OP_6F(0x9, 843)
    OP_70(0x9, 0x34B)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 3450, 0, 6350, 209)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3590, 1600, 5110, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 32)
    SetChrPos(0x10, 4790, 0, 6510, 0)
    OP_6D(21280, 0, -530, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1170, 0, 380, 0)
    SetChrPos(0x102, -1160, 0, -890, 0)
    SetChrPos(0x0, -400, 0, -2790, 0)
    SetChrPos(0x1, 2090, 0, -3410, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FF3")
    SetChrChipByIndex(0x103, 14)

    label("loc_6FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7009")
    SetChrChipByIndex(0x104, 16)
    OP_A2(0x6F5)

    label("loc_7009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_701C")
    SetChrChipByIndex(0x106, 20)

    label("loc_701C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_702F")
    SetChrChipByIndex(0x105, 18)

    label("loc_702F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7042")
    SetChrChipByIndex(0x107, 22)

    label("loc_7042")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7055")
    SetChrChipByIndex(0x108, 24)

    label("loc_7055")

    TurnDirection(0x0, 0x17, 0)
    TurnDirection(0x1, 0x17, 0)
    TurnDirection(0x2, 0x17, 0)
    TurnDirection(0x3, 0x17, 0)
    FadeToBright(2000, 0)
    OP_6D(11670, 0, 850, 4000)
    Fade(1000)
    OP_6D(3700, 0, -1810, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_83(0x19, 0x1)

    ChrTalk(
        0x101,
        "#007F终于、终于胜利啦～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2P……辛苦你们了。\x02",
    )

    CloseMessageWindow()
    OP_1D(0x1)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_713D():
        OP_6D(190, 0, -590, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_713D)

    def lambda_7155():
        OP_6B(3300, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7155)

    def lambda_7165():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_7165)

    def lambda_7173():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_7173)

    def lambda_7181():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_7181)

    def lambda_718F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_718F)
    Sleep(1500)

    def lambda_71A2():

        label("loc_71A2")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_71A2")

    QueueWorkItem2(0x0, 3, lambda_71A2)

    def lambda_71B3():

        label("loc_71B3")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_71B3")

    QueueWorkItem2(0x1, 3, lambda_71B3)

    def lambda_71C4():

        label("loc_71C4")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_71C4")

    QueueWorkItem2(0x2, 3, lambda_71C4)

    def lambda_71D5():

        label("loc_71D5")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_71D5")

    QueueWorkItem2(0x3, 3, lambda_71D5)

    def lambda_71E6():
        OP_8E(0x11, 0x2BC, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_71E6)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 270, 400)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#080F我回来了。\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "真是好久没有见到你们了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F老、老、老……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#5S老爸！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#085F虽然到最后还是有点疏忽大意，\x01",
            "不过，修行的成果总算体现出来了。\x02\x03",
            "#080F你们合格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F什、什么合格不合格啊！\x02\x03",
            "怎么回事啊，老爸！\x01",
            "你怎么会跑到这里来了！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_733E")


    ChrTalk(
        0x11,
        (
            "#084F你问我怎么会到这里来……\x02\x03",
            "#081F随便过来看看不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F什、什么叫做随便过来看看啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈……太好了。\x01",
            "爸爸您依然还是那么的精力充沛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F哦哦……\x01",
            "你看起来好像长高了一些嘛。\x02\x03",
            "怎么样，为了保护我这宝贝女儿，\x01",
            "这段时间你吃了不少苦头吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F这、这是什么意思！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F呵呵，没有那回事啦。\x02\x03",
            "#010F而且我和艾丝蒂尔一直是互相扶持的。\x01",
            "　\x02\x03",
            "所以我们才能走到今天这一步啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F这样啊……\x01",
            "看来是一次很不错的旅行呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7506():
        OP_6D(720, 0, -2650, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7506)
    WaitChrThread(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76B4")

    ChrTalk(
        0x103,
        "#021F老师……您回来了！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(
        0x11,
        (
            "#080F我回来了，雪拉扎德。\x02\x03",
            "我不在的这段时间，\x01",
            "协会的工作肯定让你忙不过来吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F是啊，很辛苦。\x02\x03",
            "不过也是很好的修行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#081F不愧是我最优秀的徒弟。\x02\x03",
            "#080F艾丝蒂尔和约修亚在协会\x01",
            "工作得怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这个嘛……\x01",
            "已经不能再算是见习的了。\x02\x03",
            "#021F不过，他们有没有意识到\x01",
            "自己已经达到了一个更高的程度，\x01",
            "这点我就不太清楚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7882")

    ChrTalk(
        0x104,
        (
            "#030F呵呵，初次见面。\x01",
            "卡西乌斯·布莱特大人。\x02\x03",
            "本人名为奥利维尔·朗海姆，\x01",
            "是来自帝国的演奏家。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x104, 400)

    ChrTalk(
        0x11,
        (
            "#084F哦，是这样啊……\x02\x03",
            "#080F事情告一段落之后，\x01",
            "就和我说说整个事情的经过吧。\x02\x03",
            "还有，非常感谢你能在这次事件里\x01",
            "全力协助我那两个孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F没什么，大人您太客气了。\x01",
            "这也是一次很有意义的体验嘛。\x02\x03",
            "#030F而且，您的功夫真是了得。\x02\x03",
            "能亲眼看到传说中的大人的英姿，\x01",
            "真是让人大饱眼福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F呵呵……\x01",
            "我也还在修行中呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A16")

    ChrTalk(
        0x106,
        (
            "#054F喂，大叔！\x02\x03",
            "神秘失踪了那么多天，\x01",
            "究竟跑到哪游山玩水去了！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(
        0x11,
        (
            "#084F哦，不良青年。\x01",
            "我从博士那里听说了你的事。\x02\x03",
            "#081F看来你也相当地努力嘛。\x01",
            "　\x02\x03",
            "了不起，了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F不、不要把我当成小鬼！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F开个玩笑。\x02\x03",
            "调查特务兵那件差事，\x01",
            "我知道你做得十分尽职尽责。\x02\x03",
            "而且还给我那两个孩子不少的帮助，\x01",
            "不管怎么说，还真是要感谢你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F这、这……\x02",
    )

    CloseMessageWindow()

    label("loc_7A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B60")

    ChrTalk(
        0x107,
        (
            "#560F卡西乌斯叔叔……\x01",
            "好久没有见到你了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x107, 400)

    ChrTalk(
        0x11,
        (
            "#080F哎哟，是提妲啊。\x02\x03",
            "一年多没见了，\x01",
            "你长高了不少啊。\x02\x03",
            "听说你和艾丝蒂尔还有约修亚\x01",
            "成了好朋友对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F嗯，是啊。\x02\x03",
            "姐姐他们把我当做妹妹一样爱护呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#081F哈哈，那就太好了。\x02\x03",
            "不过他们俩还不是很可靠，\x01",
            "还请你多多指点他们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CF7")

    ChrTalk(
        0x105,
        (
            "#048F卡西乌斯先生。\x01",
            "您好，好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x105, 400)

    ChrTalk(
        0x11,
        (
            "#080F公主殿下。\x01",
            "我们差不多有半年没见了吧。\x02\x03",
            "我听说你之前被囚禁起来了，\x01",
            "现在能平安无事也总算是让我放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F呵呵，谢谢卡西乌斯先生关心。\x01",
            "这也多亏了艾丝蒂尔他们的帮助啊。\x02\x03",
            "#040F对了，今年的王立学院学园祭，\x01",
            "艾丝蒂尔他们一起参加了舞台剧呢。\x02\x03",
            "卡西乌斯先生如果也能看到就好了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#084F哦……\x01",
            "那还真是可惜啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EA3")

    ChrTalk(
        0x108,
        (
            "#070F哟，大人。\x01",
            "您回来得还真晚啊。\x02\x03",
            "我已经等了您好久了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x108, 400)

    ChrTalk(
        0x11,
        (
            "#082F抱歉啊，金。\x02\x03",
            "特地把你从共和国叫过来，\x01",
            "真是麻烦你了……\x02\x03",
            "因为我实在放不下心，\x01",
            "所以才让你过来帮帮这些年轻人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F没什么，请别放在心上。\x02\x03",
            "就算您不叫我来，\x01",
            "我自己也会来王国走走啊。\x02\x03",
            "#070F而且还能见识到大人引以为豪的\x01",
            "两个孩子的精彩表现……\x02\x03",
            "这段时间真的过得很愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#080F是吗……\x01",
            "你能这么说我也很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EA3")


    ChrTalk(
        0x101,
        (
            "#005F这、这里可不是聊天叙旧的地方吧！\x01",
            "　\x02\x03",
            "#007F真是的～才刚回来，\x01",
            "又把我们的风头给抢走了……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0xFF)
    SetChrChipByIndex(0x10, 31)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 2670, 0, 6490, 180)
    SetChrPos(0xE, -1860, 0, -15040, 0)

    ChrTalk(
        0xE,
        (
            "#3P哎呀呀……\x01",
            "看来总算是把危机解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F69():
        OP_6D(1200, 0, -3730, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7F69)
    ClearChrFlags(0xE, 0x80)

    def lambda_7F86():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFED36, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7F86)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FBC")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 5)
    Jump("loc_7FF2")

    label("loc_7FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FCF")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 5)
    Jump("loc_7FF2")

    label("loc_7FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FE2")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 5)
    Jump("loc_7FF2")

    label("loc_7FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF2")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 5)

    label("loc_7FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8013")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 1)
    Jump("loc_8049")

    label("loc_8013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8026")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 1)
    Jump("loc_8049")

    label("loc_8026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8039")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 1)
    Jump("loc_8049")

    label("loc_8039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8049")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 1)

    label("loc_8049")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_806A")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 0)
    Jump("loc_80A0")

    label("loc_806A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_807D")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 0)
    Jump("loc_80A0")

    label("loc_807D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8090")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 0)
    Jump("loc_80A0")

    label("loc_8090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80A0")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 0)

    label("loc_80A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80C1")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 2)
    Jump("loc_80F7")

    label("loc_80C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80D4")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 2)
    Jump("loc_80F7")

    label("loc_80D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80E7")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 2)
    Jump("loc_80F7")

    label("loc_80E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80F7")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 2)

    label("loc_80F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8118")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 3)
    Jump("loc_814E")

    label("loc_8118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812B")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 3)
    Jump("loc_814E")

    label("loc_812B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_813E")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 3)
    Jump("loc_814E")

    label("loc_813E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_814E")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 3)

    label("loc_814E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_816F")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 4)
    Jump("loc_81A5")

    label("loc_816F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8182")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 4)
    Jump("loc_81A5")

    label("loc_8182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8195")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 4)
    Jump("loc_81A5")

    label("loc_8195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81A5")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 4)

    label("loc_81A5")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 110, 0, -17400, 0)

    def lambda_81C1():
        OP_8E(0xFE, 0xA8C, 0x0, 0xFFFFE2A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_81C1)
    Sleep(200)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2180, 0, -17210, 0)

    def lambda_81F7():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0xFFFFE23C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_81F7)
    Sleep(200)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1530, 0, -17240, 0)

    def lambda_822D():
        OP_8E(0xFE, 0xF0, 0x0, 0xFFFFDD46, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_822D)
    Sleep(200)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -720, 0, -17320, 0)

    def lambda_8263():
        OP_8E(0xFE, 0x55A, 0x0, 0xFFFFDE0E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8263)
    Sleep(1000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_8293():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_8293)

    def lambda_82A1():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_82A1)

    def lambda_82AF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_82AF)

    def lambda_82BD():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_82BD)

    def lambda_82CB():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_82CB)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x0, 0x0)

    ChrTalk(
        0x11,
        (
            "#080F哦，博士。\x01",
            "你们来得还真是慢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#102F#2P你先行一步之后，\x01",
            "就有大批人形兵器涌了过来。\x02\x03",
            "我们也是好不容易将它们击退的，\x01",
            "然后才赶到这里来啊……\x02\x03",
            "#101F终于……\x01",
            "一切都处理妥当了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#085F嗯……\x02\x03",
            "#080F虽然还残留有很多的事情，\x01",
            "不过总算是了结一件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F可、可是……\x02\x03",
            "那些被情报部操控的正规军\x01",
            "不是已经迫近王城了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#6P的确……\x01",
            "而且警备飞艇也来了。\x02\x03",
            "#012F爸爸您来的时候，\x01",
            "王都地上的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 315, 400)

    def lambda_8492():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8492)

    def lambda_84A0():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_84A0)

    ChrTalk(
        0x11,
        (
            "#080F#5P啊啊。\x01",
            "这点你们不用担心。\x02\x03",
            "我刚回到利贝尔的时候，\x01",
            "就已经拜托摩尔根将军处理这件事了。\x02\x03",
            "而且希德少校也采取了行动，\x01",
            "相信这场动乱很快就可以平息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F这、这样就～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#2P呵呵……原来如此啊……\x02\x03",
            "在来这里之前，\x01",
            "原来就已经处理好了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_85BE():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_85BE)

    def lambda_85CC():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_85CC)

    def lambda_85DA():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_85DA)

    def lambda_85E8():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_85E8)

    def lambda_85F6():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_85F6)
    OP_20(0x5DC)

    def lambda_8609():
        OP_6D(2300, 0, 2700, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8609)
    OP_6C(44000, 4000)
    OP_21()
    OP_1D(0x53)
    Sleep(400)

    ChrTalk(
        0x11,
        "#082F#4P……你醒过来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#118F摩尔根将军被我们严密监视着……\x01",
            "　\x02\x03",
            "希德的亲属也被列为了人质，\x01",
            "谅他也不敢背叛我……\x02\x03",
            "不过……到了最后，\x01",
            "他们还是都被你救出来了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#085F#4P啊，就算是这样吧。\x02\x03",
            "#080F可是理查德，\x01",
            "我也只不过是稍微帮了点忙而已。\x02\x03",
            "即使我没有回到王国，\x01",
            "他们自己也会想办法度过这个难关的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#115F不……终归还是实力的问题。\x01",
            "由始至终，你都是一位英雄……\x02\x03",
            "#116F自从你离开了军队之后，\x01",
            "我感到很不安……可又无计可施……\x02\x03",
            "如果国家再次受到侵略的话，\x01",
            "我想，难以像上次那样再有奇迹发生……\x02\x03",
            "因此……我就把希望寄托到了别的地方。\x02\x03",
            "#118F假如你还是继续留在军中的话，\x01",
            "今天的事情，我敢保证不会发生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#082F#4P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_88BC():
        OP_6D(3460, 0, 7840, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_88BC)

    def lambda_88D4():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_88D4)
    OP_8E(0x11, 0x898, 0x0, 0xF14, 0x7D0, 0x0)
    Sleep(500)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 35)
    SetChrSubChip(0x11, 0)
    OP_8E(0x11, 0x988, 0x0, 0x1568, 0x2710, 0x0)
    SetChrSubChip(0x11, 1)

    def lambda_8925():
        OP_8E(0x11, 0xA28, 0x0, 0x1928, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8925)
    OP_22(0x1FB, 0x0, 0x64)
    Sleep(50)

    def lambda_894A():
        OP_8E(0x11, 0xA28, 0x0, 0x1928, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_894A)
    OP_22(0x229, 0x0, 0x64)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    OP_96(0x10, 0xADC, 0x0, 0x2486, 0x258, 0xBB8)
    OP_22(0x22A, 0x0, 0x64)
    SetChrChipByIndex(0x10, 32)
    OP_96(0x10, 0xADC, 0x0, 0x285A, 0x12C, 0x3E8)
    Sleep(1000)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_89C0():
        OP_99(0x10, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_89C0)
    OP_9E(0x10, 0x14, 0x0, 0x190, 0x1770)

    ChrTalk(
        0x10,
        "#5P#117F呜……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#087F#4P理查德，你这个懦夫！\x02\x03",
            "你若总是希望我再次出现来帮你，\x01",
            "那就是你天大的错误了！\x01",
            "　\x02\x03",
            "你拥有那样优秀的能力，\x01",
            "为何就不能靠自己去闯出一片天地呢！？\x02\x03",
            "我不也是因为你坐镇军中，\x01",
            "所以才安心地辞去了军务吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#113F上、上校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#086F#4P我……并不是你想象的那样无所不能。\x02\x03",
            "十年前，我也是因为有将军和你的帮助，\x01",
            "所以才能和大家一起，取得最后的胜利。\x02\x03",
            "其实，我只是一个不能保护自己最重要的人、\x01",
            "最终选择了逃避现实的男人而已！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#113F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F……老爸……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#085F#4P不过……\x01",
            "我已经不打算再逃避了。\x02\x03",
            "#082F因此，理查德，\x01",
            "你也不要像我那样继续逃避了。\x02\x03",
            "在偿还自己犯下的罪孽的同时，\x01",
            "好好反思一下自己还有哪些不足吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，在众人的努力阻止之下，\x01",
            "情报部发动的政变计划最后以失败告终。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摩尔根将军和希德少校\x01",
            "也成功收拾了王国军部队内部的混乱……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "参与发动这次政变的\x01",
            "情报部相关人员也在王国各地相继被捕。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一周之后——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x2000000)
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_460C end

    def Function_10_8D84(): pass

    label("Function_10_8D84")

    OP_66(0x1)

    def lambda_8D8D():
        OP_6D(4690, 2000, -1350, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D8D)

    def lambda_8DA5():
        OP_67(0, 2630, -27100, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8DA5)

    def lambda_8DBD():
        OP_6C(85000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DBD)
    OP_7C(0x0, 0x33, 0xBB8, 0x1388)
    OP_B0(0x9, 0x14)
    OP_6F(0x9, 296)
    OP_70(0x9, 0x150)
    OP_73(0x9)
    OP_22(0xF4, 0x0, 0x64)
    OP_B0(0x9, 0x19)
    OP_6F(0x9, 337)
    OP_70(0x9, 0x197)
    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x1770)

    def lambda_8E20():
        OP_6B(1110, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8E20)
    OP_73(0x9)
    OP_B0(0x9, 0x16)
    OP_6F(0x9, 408)
    OP_70(0x9, 0x1BD)
    OP_73(0x9)
    OP_B0(0x9, 0x13)
    OP_6F(0x9, 446)
    OP_70(0x9, 0x1E0)
    OP_73(0x9)
    OP_B0(0x9, 0x10)
    OP_6F(0x9, 481)
    OP_70(0x9, 0x1EE)
    OP_73(0x9)

    def lambda_8E72():
        OP_6B(1300, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8E72)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 50)
    OP_70(0x9, 0x45)
    Return()

    # Function_10_8D84 end

    def Function_11_8E94(): pass

    label("Function_11_8E94")

    OP_8F(0xFE, 0xAA0, 0x0, 0x83E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 28)
    Sleep(100)

    def lambda_8EC2():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8EC2)
    OP_8F(0xFE, 0x12D4, 0x7D0, 0x316, 0x2710, 0x0)
    Return()

    # Function_11_8E94 end

    def Function_12_8EE1(): pass

    label("Function_12_8EE1")


    def lambda_8EE7():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8EE7)
    OP_96(0xFE, 0x10A4, 0x0, 0xB72, 0x12C, 0x2710)

    def lambda_8F0E():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F0E)
    OP_8F(0xFE, 0x12D4, 0x7D0, 0x316, 0x2710, 0x0)
    Return()

    # Function_12_8EE1 end

    def Function_13_8F2D(): pass

    label("Function_13_8F2D")


    def lambda_8F33():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F33)
    OP_96(0xFE, 0xCEE, 0x0, 0x6CC, 0x12C, 0x1F40)
    Return()

    # Function_13_8F2D end

    def Function_14_8F55(): pass

    label("Function_14_8F55")

    Sleep(250)

    def lambda_8F60():
        OP_96(0xFE, 0x582, 0x0, 0xE88, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F60)
    Sleep(600)

    def lambda_8F83():
        OP_96(0xFE, 0xA0A, 0x0, 0x1112, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F83)
    Sleep(300)

    def lambda_8FA6():
        OP_96(0xFE, 0xD02, 0xB4A, 0xF78, 0xFA0, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FA6)
    Return()

    # Function_14_8F55 end

    def Function_15_8FBF(): pass

    label("Function_15_8FBF")

    SetChrFlags(0xFE, 0x4)
    WaitChrThread(0xFE, 0x1)

    def lambda_8FCF():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FCF)
    OP_96(0xFE, 0xD16, 0x992, 0x550, 0x3E8, 0x1770)
    Return()

    # Function_15_8FBF end

    def Function_16_8FF1(): pass

    label("Function_16_8FF1")


    def lambda_8FF7():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FF7)
    OP_96(0xFE, 0x8FC, 0x0, 0xD66, 0x12C, 0x1770)
    Return()

    # Function_16_8FF1 end

    def Function_17_9019(): pass

    label("Function_17_9019")

    SetChrPos(0x1A, 5140, 2450, 340, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(200)
    SetChrPos(0x1A, 5140, 2450, 340, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(200)
    SetChrPos(0x1A, 5140, 2450, 340, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Return()

    # Function_17_9019 end

    def Function_18_90F6(): pass

    label("Function_18_90F6")

    SetChrSubChip(0xFE, 11)
    SetChrPos(0xFE, 740, 0, 1920, 46)
    TurnDirection(0xFE, 0x17, 400)
    OP_96(0xFE, 0x1180, 0x0, 0x2DA, 0x1F4, 0xFA0)
    Sleep(50)

    def lambda_9135():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9135)
    OP_99(0xFE, 0x0, 0x2, 0x7D0)
    SetChrFlags(0xFE, 0x2)

    def lambda_9161():

        label("loc_9161")

        OP_99(0xFE, 0x20, 0x31, 0xDAC)
        OP_48()
        Jump("loc_9161")

    QueueWorkItem2(0xFE, 2, lambda_9161)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    TurnDirection(0xFE, 0x17, 0)

    def lambda_9189():
        OP_99(0xFE, 0x5, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9189)
    Sleep(1000)
    OP_96(0xFE, 0x30C, 0x0, 0x11F8, 0x1F4, 0x1770)
    TurnDirection(0xFE, 0x17, 0)
    Return()

    # Function_18_90F6 end

    def Function_19_91B7(): pass

    label("Function_19_91B7")

    SetChrChipByIndex(0xFE, 45)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 100, -600, 3150, 0)

    def lambda_91EC():

        label("loc_91EC")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_91EC")

    QueueWorkItem2(0xFE, 1, lambda_91EC)
    OP_96(0xFE, 0xFFFFF01A, 0xFFFFFDA8, 0xFDB, 0xFA0, 0xFA0)
    OP_44(0xFE, 0x1)
    SetChrSubChip(0xFE, 8)
    Return()

    # Function_19_91B7 end

    def Function_20_921A(): pass

    label("Function_20_921A")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3590, 1600, 5110, 0)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    OP_96(0x10, 0x11A8, 0x0, 0x17CA, 0x7D0, 0xFA0)
    SetChrChipByIndex(0x10, 32)
    OP_96(0x10, 0x12B6, 0x0, 0x196E, 0x190, 0xFA0)
    OP_95(0x10, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
    Return()

    # Function_20_921A end

    def Function_21_9285(): pass

    label("Function_21_9285")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 1)
    SetChrPos(0xFE, 260, 0, -8970, 154)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrSubChip(0xFE, 1)
    OP_8E(0xFE, 0x910, 0x0, 0xFFFFF916, 0x2710, 0x0)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92E7")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x10)

    label("loc_92E7")

    OP_96(0xFE, 0x1180, 0x71C, 0xD0C, 0x76C, 0x3E8)
    OP_A2(0x7)
    SetChrSubChip(0xFE, 1)

    def lambda_930C():
        OP_8C(0xFE, 77, 400)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_930C)
    OP_96(0xFE, 0x6E0, 0x0, 0xFFFFFC2C, 0xC8, 0xBB8)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 10)
    Return()

    # Function_21_9285 end

    def Function_22_9336(): pass

    label("Function_22_9336")

    SetChrSubChip(0xFE, 4)

    def lambda_9341():
        OP_8C(0xFE, 170, 1200)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9341)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9359")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x12)

    label("loc_9359")

    OP_96(0xFE, 0xE7E, 0x0, 0xFFFFF574, 0x1F4, 0x1B58)
    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 90, 1200)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 5)
    OP_8C(0xFE, 135, 1200)
    Sleep(100)
    OP_A2(0x7)
    OP_8C(0xFE, 0, 1200)
    OP_8C(0xFE, 90, 400)
    SetChrSubChip(0xFE, 6)
    Return()

    # Function_22_9336 end

    def Function_23_93AA(): pass

    label("Function_23_93AA")

    SetChrSubChip(0xFE, 11)

    def lambda_93B5():
        OP_8C(0xFE, 90, 800)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_93B5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93CD")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x13)

    label("loc_93CD")

    OP_96(0xFE, 0x163A, 0x11F8, 0xFFFFF7D6, 0x1770, 0x1B58)
    SetChrSubChip(0xFE, 12)
    OP_A6(0x7)
    Sleep(250)
    OP_8F(0xFE, 0x152C, 0x8B6, 0xFFFFF61E, 0x3A98, 0x0)
    Sleep(500)
    SetChrSubChip(0xFE, 11)
    OP_96(0xFE, 0x564, 0x0, 0xFFFFFC22, 0x1F4, 0xFA0)
    SetChrSubChip(0xFE, 6)
    Return()

    # Function_23_93AA end

    def Function_24_942C(): pass

    label("Function_24_942C")

    SetChrSubChip(0xFE, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9441")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x14)

    label("loc_9441")

    OP_96(0xFE, 0x1DB0, 0x6C2, 0xFFFFFDB2, 0xBB8, 0x2EE0)
    SetChrSubChip(0xFE, 6)
    Return()

    # Function_24_942C end

    def Function_25_945E(): pass

    label("Function_25_945E")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 1)
    SetChrPos(0xFE, 260, 0, -8970, 154)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrSubChip(0xFE, 1)
    OP_8E(0xFE, 0x910, 0x0, 0xFFFFF916, 0x2710, 0x0)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94C0")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x10)

    label("loc_94C0")

    OP_96(0xFE, 0x1180, 0x71C, 0xD0C, 0x76C, 0x3E8)
    OP_A2(0x7)
    SetChrSubChip(0xFE, 1)

    def lambda_94E5():
        OP_8C(0xFE, 77, 400)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_94E5)
    OP_96(0xFE, 0xB54, 0x0, 0x161C, 0xC8, 0xBB8)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 10)
    Return()

    # Function_25_945E end

    SaveToFile()

Try(main)
