from ED6ScenarioHelper import *

def main():
    # 空贼要塞

    CreateScenaFile(
        FileName            = 'C1304   ._SN',
        MapName             = 'Bose',
        Location            = 'C1304.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        '古兰托机长',                           # 9
        '特里诺',                               # 10
        '乘务员卡拉莉丝',                       # 11
        '波嘉',                                 # 12
        '卡尔托斯',                             # 13
        '迪蒙',                                 # 14
        '登克',                                 # 15
        '芬尼尔',                               # 16
        '布拉奥',                               # 17
        '普罗梅笛',                             # 18
        '莉诺',                                 # 19
        '雷加洛',                               # 20
        '希尔碧',                               # 21
        '巴雷尔',                               # 22
        '鲁蓓',                                 # 23
        '阿杰',                                 # 24
        '空贼阿伦',                             # 25
        '空贼洛西',                             # 26
        '空贼雷古',                             # 27
        '空贼蒂诺',                             # 28
        '空贼',                                 # 29
        '空贼',                                 # 30
        '空贼',                                 # 31
        '空贼',                                 # 32
        '空贼',                                 # 33
        '空贼',                                 # 34
        '空贼',                                 # 35
        '空贼',                                 # 36
        '目标用摄像机',                         # 37
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01440 ._CH',             # 00
        'ED6_DT07/CH01200 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01290 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT07/CH01100 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT07/CH01220 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01030 ._CH',             # 0C
        'ED6_DT07/CH01070 ._CH',             # 0D
        'ED6_DT07/CH01380 ._CH',             # 0E
        'ED6_DT07/CH00360 ._CH',             # 0F
        'ED6_DT07/CH00364 ._CH',             # 10
        'ED6_DT07/CH00361 ._CH',             # 11
        'ED6_DT07/CH00363 ._CH',             # 12
        'ED6_DT07/CH00122 ._CH',             # 13
        'ED6_DT07/CH00100 ._CH',             # 14
        'ED6_DT07/CH00101 ._CH',             # 15
        'ED6_DT07/CH00110 ._CH',             # 16
        'ED6_DT07/CH00111 ._CH',             # 17
        'ED6_DT07/CH00120 ._CH',             # 18
        'ED6_DT07/CH00121 ._CH',             # 19
        'ED6_DT07/CH00130 ._CH',             # 1A
        'ED6_DT07/CH00131 ._CH',             # 1B
        'ED6_DT06/CH20074 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH01440P._CP',             # 00
        'ED6_DT07/CH01200P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01290P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT07/CH01100P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT07/CH01220P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01030P._CP',             # 0C
        'ED6_DT07/CH01070P._CP',             # 0D
        'ED6_DT07/CH01380P._CP',             # 0E
        'ED6_DT07/CH00360P._CP',             # 0F
        'ED6_DT07/CH00364P._CP',             # 10
        'ED6_DT07/CH00361P._CP',             # 11
        'ED6_DT07/CH00363P._CP',             # 12
        'ED6_DT07/CH00122P._CP',             # 13
        'ED6_DT07/CH00100P._CP',             # 14
        'ED6_DT07/CH00101P._CP',             # 15
        'ED6_DT07/CH00110P._CP',             # 16
        'ED6_DT07/CH00111P._CP',             # 17
        'ED6_DT07/CH00120P._CP',             # 18
        'ED6_DT07/CH00121P._CP',             # 19
        'ED6_DT07/CH00130P._CP',             # 1A
        'ED6_DT07/CH00131P._CP',             # 1B
        'ED6_DT06/CH20074P._CP',             # 1C
    )

    DeclNpc(
        X                   = -51200,
        Z                   = 0,
        Y                   = -44970,
        Direction           = 180,
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
        X                   = -44800,
        Z                   = 0,
        Y                   = -44500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -49400,
        Z                   = 0,
        Y                   = -44100,
        Direction           = 180,
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
        X                   = -52870,
        Z                   = 0,
        Y                   = -45150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -48530,
        Z                   = 0,
        Y                   = -45460,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -53480,
        Z                   = 0,
        Y                   = -43740,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -51250,
        Z                   = 0,
        Y                   = -43660,
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
        X                   = -49800,
        Z                   = 0,
        Y                   = -41400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -54600,
        Z                   = 0,
        Y                   = -40800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -56400,
        Z                   = 0,
        Y                   = -43000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -47800,
        Z                   = 0,
        Y                   = -42400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -45700,
        Z                   = 0,
        Y                   = -42960,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -45400,
        Z                   = 0,
        Y                   = -41900,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -57380,
        Z                   = 0,
        Y                   = -45290,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -51600,
        Z                   = 0,
        Y                   = -40500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -52100,
        Z                   = 0,
        Y                   = -40700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_532",          # 00, 0
        "Function_1_779",          # 01, 1
        "Function_2_77A",          # 02, 2
        "Function_3_902",          # 03, 3
        "Function_4_BDC",          # 04, 4
        "Function_5_D4B",          # 05, 5
        "Function_6_E48",          # 06, 6
        "Function_7_F2E",          # 07, 7
        "Function_8_1138",         # 08, 8
        "Function_9_1238",         # 09, 9
        "Function_10_1373",        # 0A, 10
        "Function_11_13FD",        # 0B, 11
        "Function_12_14C1",        # 0C, 12
        "Function_13_158F",        # 0D, 13
        "Function_14_1636",        # 0E, 14
        "Function_15_16E2",        # 0F, 15
        "Function_16_17ED",        # 10, 16
        "Function_17_18E8",        # 11, 17
        "Function_18_19CD",        # 12, 18
        "Function_19_1A6E",        # 13, 19
        "Function_20_2A3D",        # 14, 20
    )


    def Function_0_532(): pass

    label("Function_0_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_540")
    OP_A3(0x3FA)
    Event(0, 19)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_54E")
    OP_A3(0x3FB)
    Event(0, 20)

    label("loc_54E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_562"),
        (102, "loc_66D"),
        (101, "loc_66D"),
        (SWITCH_DEFAULT, "loc_778"),
    )


    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x18, 10200, 0, -92518, 225)
    SetChrPos(0x19, 3520, 0, -93920, 35)
    SetChrPos(0x1C, 2640, 0, -91700, 4)
    SetChrPos(0x1D, 9860, 0, -97730, 260)
    SetChrPos(0x1E, 1950, 0, -97080, 217)
    SetChrPos(0x1F, 2350, 0, -98760, 140)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x18, 28)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66A")

    Jump("loc_778")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x18, -54970, 0, -93490, 315)
    SetChrPos(0x19, -48920, 0, -91340, 53)
    SetChrPos(0x1C, -45150, 0, -93440, 163)
    SetChrPos(0x1D, -48280, 0, -97510, 119)
    SetChrPos(0x1E, -54960, 0, -97820, 86)
    SetChrPos(0x1F, -53760, 0, -91280, 172)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x18, 28)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_775")

    Jump("loc_778")

    label("loc_778")

    Return()

    # Function_0_532 end

    def Function_1_779(): pass

    label("Function_1_779")

    Return()

    # Function_1_779 end

    def Function_2_77A(): pass

    label("Function_2_77A")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_8EC")

    label("loc_7AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_8EC")

    label("loc_7C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_8EC")

    label("loc_7DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F5")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_8EC")

    label("loc_7F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80E")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_8EC")

    label("loc_80E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_827")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_8EC")

    label("loc_827")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_8EC")

    label("loc_840")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_8EC")

    label("loc_859")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_872")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_8EC")

    label("loc_872")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_8EC")

    label("loc_88B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A4")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_8EC")

    label("loc_8A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_8EC")

    label("loc_8BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_8EC")

    label("loc_8D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_901")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_8EC")

    label("loc_901")

    Return()

    # Function_2_77A end

    def Function_3_902(): pass

    label("Function_3_902")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")
    OP_A2(0x0)

    ChrTalk(
        0x101,
        (
            "#006F机长，\x01",
            "那些空贼没有逃到这里来吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有，不过我听到外面\x01",
            "好像有吵闹声和脚步声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是有人\x01",
            "跑到上面去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F艾丝蒂尔，他们果然要坐飞艇逃跑。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，追上去！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F抱歉了，机长。\x01",
            "就请你们再稍等片刻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好，你们也要小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_B08")


    ChrTalk(
        0xFE,
        (
            "那些家伙\x01",
            "应该是跑到上面去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "小心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_B54")

    Jump("loc_BD8")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(
        0xFE,
        (
            "空贼的头目很可能\x01",
            "就在这儿的最底层。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们要小心哦。\x02",
    )

    CloseMessageWindow()

    label("loc_BD8")

    TalkEnd(0x8)
    Return()

    # Function_3_902 end

    def Function_4_BDC(): pass

    label("Function_4_BDC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(
        0xFE,
        (
            "我还有不少生意\x01",
            "要准备去洽谈呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "各～位，无论如何也要坚持下去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能回到柏斯，\x01",
            "第一件要做的事就是向大家赔礼道歉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D47")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_D47")

    ChrTalk(
        0xFE,
        (
            "没想到你们竟然能\x01",
            "潜入到这种地方来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士也是\x01",
            "一个很辛苦的职业啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D47")

    TalkEnd(0x9)
    Return()

    # Function_4_BDC end

    def Function_5_D4B(): pass

    label("Function_5_D4B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_DCE")

    ChrTalk(
        0xFE,
        (
            "外面好像\x01",
            "还有不少的空贼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们没有尽到\x01",
            "保护旅客的职责……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E44")

    label("loc_DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_E44")

    ChrTalk(
        0xFE,
        (
            "能够得到你们的帮助，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有人受伤或者生病，\x01",
            "乘务员和乘客都平安无事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E44")

    TalkEnd(0xA)
    Return()

    # Function_5_D4B end

    def Function_6_E48(): pass

    label("Function_6_E48")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "游击士还真了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "区区几个人\x01",
            "就冲入了空贼团的基地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2A")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(
        0xFE,
        "我坚信我们能够获救。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "姐姐，谢谢你们了！\x02",
    )

    CloseMessageWindow()

    label("loc_F2A")

    TalkEnd(0xB)
    Return()

    # Function_6_E48 end

    def Function_7_F2E(): pass

    label("Function_7_F2E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1014")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "空贼团的老大\x01",
            "实在是太可怕了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过空贼团的成员\x01",
            "也不是全部都很可恶啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其中也有很亲切的人，\x01",
            "无论在哪里都还是有好人的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109F")

    label("loc_1014")


    ChrTalk(
        0xFE,
        (
            "空贼团的成员\x01",
            "也不是全部都很可恶啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其中也有很亲切的人，\x01",
            "无论在哪里都还是有好人的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109F")

    Jump("loc_1134")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1134")

    ChrTalk(
        0xFE,
        "呀啊，快要受不了了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个空贼团的老大\x01",
            "怎么看都觉得有些不正常。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1134")

    TalkEnd(0xC)
    Return()

    # Function_7_F2E end

    def Function_8_1138(): pass

    label("Function_8_1138")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(
        0xFE,
        (
            "我要尽快把获救的事\x01",
            "向飞艇公社报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1234")

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(
        0xFE,
        "虽然得救了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我们的『林德号』\x01",
            "被弄到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为我们被蒙上了眼睛，\x01",
            "所以不太清楚当时的状况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1234")

    TalkEnd(0xD)
    Return()

    # Function_8_1138 end

    def Function_9_1238(): pass

    label("Function_9_1238")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_12D6")

    ChrTalk(
        0xFE,
        (
            "要是那些家伙现在进来，\x01",
            "我一定会狠狠给他们一拳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们是『林德号』的仇敌。\x01",
            "不可饶恕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136F")

    label("loc_12D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_136F")

    ChrTalk(
        0xFE,
        (
            "那群败类，\x01",
            "竟然把我精心维护过的\x01",
            "『林德号』的引擎给拆下来带走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "绝对不可饶恕。\x02",
    )

    CloseMessageWindow()

    label("loc_136F")

    TalkEnd(0xE)
    Return()

    # Function_9_1238 end

    def Function_10_1373(): pass

    label("Function_10_1373")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(
        0xFE,
        "她怎么样了呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡特丽亚现在\x01",
            "肯定正在担心我吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F9")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_13F9")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "我的店铺现在怎么样了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F9")

    TalkEnd(0xF)
    Return()

    # Function_10_1373 end

    def Function_11_13FD(): pass

    label("Function_11_13FD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1470")

    ChrTalk(
        0xFE,
        (
            "本来打算去拜访在洛连特的旧友，\x01",
            "可没想到会发生这种事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_1470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_14BD")

    ChrTalk(
        0xFE,
        "哦哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我做梦都在想着\x01",
            "能够被救出去啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BD")

    TalkEnd(0x10)
    Return()

    # Function_11_13FD end

    def Function_12_14C1(): pass

    label("Function_12_14C1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1550")

    ChrTalk(
        0xFE,
        (
            "我去了王立学院授课，\x01",
            "回来的时候乘了定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "竟然遇到这种事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158B")

    label("loc_1550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "这下终于可以回蔡斯去了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158B")

    TalkEnd(0x11)
    Return()

    # Function_12_14C1 end

    def Function_13_158F(): pass

    label("Function_13_158F")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_15CE")

    ChrTalk(
        0xFE,
        "家人肯定很担心我呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1632")

    ChrTalk(
        0xFE,
        "谢谢你们，游击士！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这下终于可以回家去了。\x02",
    )

    CloseMessageWindow()

    label("loc_1632")

    TalkEnd(0x12)
    Return()

    # Function_13_158F end

    def Function_14_1636(): pass

    label("Function_14_1636")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1667")

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "大家能够平安无事真是万幸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DE")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_16DE")

    ChrTalk(
        0xFE,
        (
            "太好了～\x01",
            "这下又可以继续旅行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "这回真是被关了好久啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    TalkEnd(0x13)
    Return()

    # Function_14_1636 end

    def Function_15_16E2(): pass

    label("Function_15_16E2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(
        0xFE,
        (
            "要去追击那些空贼吧。\x01",
            "虽然帮不上忙，但我会为你们加油的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "加油吧～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_17E9")

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_17E9")

    ChrTalk(
        0xFE,
        (
            "难得我专程赶到柏斯超市去，\x01",
            "但是买的东西竟然\x01",
            "全部被那些空贼抢走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "游击士啊，帮我夺回来吧！\x02",
    )

    CloseMessageWindow()

    label("loc_17E9")

    TalkEnd(0x14)
    Return()

    # Function_15_16E2 end

    def Function_16_17ED(): pass

    label("Function_16_17ED")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1862")

    ChrTalk(
        0xFE,
        (
            "现、现在\x01",
            "外面还有空贼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "快、快点\x01",
            "把他们解决了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_1862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_18E4")

    ChrTalk(
        0xFE,
        (
            "我、我是\x01",
            "头一回乘坐定期船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没想到会遇到这样的事情……\x02",
    )

    CloseMessageWindow()

    label("loc_18E4")

    TalkEnd(0x15)
    Return()

    # Function_16_17ED end

    def Function_17_18E8(): pass

    label("Function_17_18E8")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1974")

    ChrTalk(
        0xFE,
        (
            "那些空贼\x01",
            "还给了小孩子面包吃哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来他们也并非\x01",
            "全部都是坏人嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C9")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_19C9")

    ChrTalk(
        0xFE,
        "太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "与我自己获救相比，\x01",
            "孩子能够得救更让我欣慰。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C9")

    TalkEnd(0x16)
    Return()

    # Function_17_18E8 end

    def Function_18_19CD(): pass

    label("Function_18_19CD")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1A18")

    ChrTalk(
        0xFE,
        "那个那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请不要太为难\x01",
            "那些叔叔们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_1A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1A6A")

    ChrTalk(
        0xFE,
        (
            "姐姐你们\x01",
            "是游击士～吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些叔叔们\x01",
            "被你们抓住了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    TalkEnd(0x17)
    Return()

    # Function_18_19CD end

    def Function_19_1A6E(): pass

    label("Function_19_1A6E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetMapFlags(0x400000)
    SetChrPos(0x101, 4948, 0, -101090, 0)
    SetChrPos(0x102, 4948, 0, -101090, 0)
    SetChrPos(0x103, 4948, 0, -101090, 0)
    SetChrPos(0x104, 4948, 0, -101090, 0)
    SetChrPos(0x18, 6280, 0, -94290, 270)
    SetChrPos(0x19, 4610, 0, -94970, 0)
    SetChrPos(0x1C, 9423, 0, -92822, 0)
    SetChrPos(0x1D, 9856, 0, -97201, 90)
    SetChrPos(0x1E, 3340, 0, -93640, 90)
    SetChrPos(0x1F, 88, 0, -97865, 270)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 22)
    SetChrChipByIndex(0x103, 24)
    SetChrChipByIndex(0x104, 26)
    OP_6D(5230, 0, -96500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_62(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1C54():
        OP_6D(5440, 0, -94380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C54)
    ClearChrFlags(0x101, 0x80)

    def lambda_1C71():
        OP_8E(0xFE, 0x1308, 0x0, 0xFFFE8271, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C71)
    Sleep(200)
    ClearChrFlags(0x102, 0x80)

    def lambda_1C96():
        OP_8E(0xFE, 0x1631, 0x0, 0xFFFE81AD, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C96)
    Sleep(200)
    ClearChrFlags(0x104, 0x80)

    def lambda_1CBB():
        OP_8E(0xFE, 0x18A9, 0x0, 0xFFFE7EDF, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CBB)
    Sleep(200)
    ClearChrFlags(0x103, 0x80)

    def lambda_1CE0():
        OP_8E(0xFE, 0xF99, 0x0, 0xFFFE7E42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CE0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x103, 0x1)

    def lambda_1D0F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1D0F)

    def lambda_1D1D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1D1D)

    def lambda_1D2B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1D2B)

    def lambda_1D39():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1D39)

    def lambda_1D47():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1D47)

    def lambda_1D55():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1D55)
    WaitChrThread(0x18, 0x1)

    ChrTalk(
        0x18,
        "啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "你们几个，是新来的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F你说呢……\x01",
            "怎么想也不可能吧！\x02\x03",
            "真是没有紧张感的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#1P哎，可是……\x01",
            "除了新来的还能是什么人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "……难、难道是入侵者？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0xA6, 0x0, 0x64)

    ChrTalk(
        0x104,
        "#031FＢｉｎｇｏ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们是游击士协会的。\x01",
            "请你们马上放下武器投降吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x18, 15)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 15)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 15)
    Sleep(100)
    SetChrChipByIndex(0x1D, 15)
    Sleep(75)
    SetChrChipByIndex(0x1E, 15)
    Sleep(50)
    SetChrChipByIndex(0x1F, 15)

    ChrTalk(
        0x19,
        "#1P开、开什么玩笑！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "干掉他们！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)

    def lambda_1FC4():
        OP_6D(5230, 0, -96500, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FC4)
    SetChrChipByIndex(0x19, 17)

    def lambda_1FE1():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1FE1)
    SetChrChipByIndex(0x1C, 17)

    def lambda_1FFB():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1FFB)
    SetChrChipByIndex(0x1D, 17)

    def lambda_2015():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2015)
    SetChrChipByIndex(0x1E, 17)

    def lambda_202F():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_202F)
    SetChrChipByIndex(0x1F, 17)

    def lambda_2049():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2049)
    Sleep(250)
    SetChrChipByIndex(0x18, 17)

    def lambda_2068():
        OP_96(0x18, 0x16D8, 0x0, 0xFFFE84CF, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2068)
    Sleep(400)
    Battle(0x38A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_209E"),
        (SWITCH_DEFAULT, "loc_20A1"),
    )


    label("loc_209E")

    OP_B4(0x0)
    Return()

    label("loc_20A1")

    EventBegin(0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrPos(0x101, 5750, 0, -97780, 39)
    SetChrPos(0x102, 6780, 0, -98300, 4)
    SetChrPos(0x103, 4320, 0, -97780, 72)
    SetChrPos(0x104, 4700, 0, -96480, 85)
    SetChrPos(0x19, 3520, 0, -93920, 35)
    SetChrPos(0x1C, 2640, 0, -91700, 4)
    SetChrPos(0x1D, 9860, 0, -97730, 260)
    SetChrPos(0x1E, 1950, 0, -97080, 217)
    SetChrPos(0x1F, 2350, 0, -98760, 140)
    SetChrPos(0x18, 6511, 0, -96547, 0)
    TurnDirection(0x19, 0x101, 0)
    TurnDirection(0x18, 0x101, 0)
    TurnDirection(0x1C, 0x101, 0)
    TurnDirection(0x1D, 0x101, 0)
    SetChrChipByIndex(0x18, 16)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x18, 0)
    TurnDirection(0x102, 0x18, 0)
    TurnDirection(0x104, 0x18, 0)
    TurnDirection(0x103, 0x18, 0)
    OP_6D(6280, 0, -96740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "呜呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F说！\x01",
            "人质在哪里？\x02\x03",
            "不老实交代的话，\x01",
            "有你好受的哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "要、要杀要剐随你的便。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "白痴才会告诉你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F啊，是吗。\x02\x03",
            "艾丝蒂尔，你先退下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#004F啊，嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_23C6():
        OP_8E(0xFE, 0x1536, 0x0, 0xFFFE7ECE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23C6)
    WaitChrThread(0x101, 0x1)

    def lambda_23E6():
        OP_6D(6700, 0, -96370, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23E6)

    def lambda_23FE():
        OP_92(0x103, 0x18, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23FE)
    OP_8C(0x101, 22, 400)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 24)
    Sleep(1000)
    OP_44(0x103, 0xFF)
    SetChrChipByIndex(0x103, 19)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_2437():
        OP_99(0x103, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2437)
    Sleep(200)
    SetChrFlags(0x18, 0x20)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x12, 0x0, 0x18, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x18, 0x20)
    TurnDirection(0x18, 0x103, 0)
    OP_8F(0x18, 0x204F, 0x0, 0xFFFE8E09, 0x1F40, 0x0)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2)

    ChrTalk(
        0x18,
        "哎呀……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F#3P呵呵，我可是手下留情了哦，\x01",
            "不会那么简单就让你晕过去的。\x02\x03",
            "老实交代的话，\x01",
            "倒是可以让你好好睡上一觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "呀呀呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "就在下面的楼层！\x01",
            "有我们的兄弟在把守着！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#3P真是乖孩子。\x02\x03",
            "那么你们的首领\x01",
            "吉尔和乔丝特又在哪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "别、别太过分了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "大白痴才会告诉你这个！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#3P呼，先不说人质，\x01",
            "不出卖首领这一点的确算是有骨气。\x02\x03",
            "#021F没办法，那就先说声抱歉啦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x103, 0x20)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2727():
        OP_6D(8010, 0, -95060, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2727)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2744():
        OP_96(0x103, 0x1DE0, 0x0, 0xFFFE8B9B, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2744)
    Sleep(500)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_276C():
        OP_99(0x103, 0x1, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_276C)
    Sleep(200)
    SetChrFlags(0x18, 0x20)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x18, 18)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x20)
    TurnDirection(0x18, 0x103, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_8F(0x18, 0x27D8, 0x3E8, 0xFFFE969A, 0x3A98, 0x0)
    PlayEffect(0x12, 0xFF, 0x18, 0, 0, -500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x8E, 0x0, 0x64)
    OP_6B(3070, 0)
    OP_6B(3000, 80)
    Sleep(500)
    OP_8F(0x18, 0x27D8, 0x0, 0xFFFE969A, 0x3E8, 0x0)
    OP_22(0x25, 0x0, 0x64)
    SetChrChipByIndex(0x18, 16)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x18, 0x2, 0x3, 0x3E8)

    ChrTalk(
        0x18,
        "呜～……\x02",
    )

    CloseMessageWindow()

    def lambda_284D():
        OP_6D(6700, 0, -96370, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_284D)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F呜哇～……\x01",
            "下手还是那么狠啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x103, 24)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F#1P真过分，\x01",
            "我已经手下留情了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F的确是留了情，\x01",
            "看他的样子不是挺舒服的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F#1P哎呀，你也想试试吗？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x104, 0xFF)
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(
        0x104,
        "#035F不了，下次有机会再说吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        (
            "#012F人质应该是\x01",
            "被囚禁在下面的楼层。\x02\x03",
            "我们赶快过去吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1E, 0x4)
    OP_44(0x103, 0xFF)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    EventEnd(0x0)
    OP_A2(0x355)
    OP_28(0x39, 0x1, 0x4)
    ClearMapFlags(0x400000)
    Return()

    # Function_19_1A6E end

    def Function_20_2A3D(): pass

    label("Function_20_2A3D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetMapFlags(0x400000)
    SetChrPos(0x101, -51020, 0, -100510, 0)
    SetChrPos(0x102, -51020, 0, -100510, 0)
    SetChrPos(0x103, -51020, 0, -100510, 0)
    SetChrPos(0x104, -51020, 0, -100510, 0)
    SetChrPos(0x1A, -49700, 0, -95128, 270)
    SetChrPos(0x1B, -51210, 0, -95060, 90)
    SetChrPos(0x20, -46020, 0, -97600, 90)
    SetChrPos(0x21, -50250, 0, -91580, 270)
    SetChrPos(0x22, -52750, 0, -91250, 90)
    SetChrPos(0x23, -56510, 0, -97430, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 22)
    SetChrChipByIndex(0x103, 24)
    SetChrChipByIndex(0x104, 26)
    OP_6D(-50990, 0, -98940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2C32():
        OP_6D(-51370, 0, -96390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C32)
    ClearChrFlags(0x101, 0x80)

    def lambda_2C4F():
        OP_8E(0xFE, 0xFFFF363E, 0x0, 0xFFFE816C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C4F)
    Sleep(200)
    ClearChrFlags(0x103, 0x80)

    def lambda_2C74():
        OP_8E(0xFE, 0xFFFF3A9E, 0x0, 0xFFFE7FD2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C74)
    Sleep(200)
    ClearChrFlags(0x102, 0x80)

    def lambda_2C99():
        OP_8E(0xFE, 0xFFFF31CA, 0x0, 0xFFFE7E74, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C99)
    Sleep(200)
    ClearChrFlags(0x104, 0x80)

    def lambda_2CBE():
        OP_8E(0xFE, 0xFFFF3CD8, 0x0, 0xFFFE7C4E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CBE)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 0)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 45, 0)

    def lambda_2CFB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2CFB)

    def lambda_2D09():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2D09)

    def lambda_2D17():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2D17)

    def lambda_2D25():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2D25)

    def lambda_2D33():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2D33)

    def lambda_2D41():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2D41)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(
        0x1A,
        "你、你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "游击士！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "从、从哪里进来的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F看起来，\x01",
            "里面的房间就是囚禁人质的地方了。\x02\x03",
            "你们还是乖乖地投降吧。\x01",
            "不然的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x22, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x1A, 15)
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1B, 15)
    OP_51(0x1B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x20, 15)
    Sleep(100)
    SetChrChipByIndex(0x21, 15)
    Sleep(75)
    SetChrChipByIndex(0x22, 15)
    Sleep(50)
    SetChrChipByIndex(0x23, 15)

    ChrTalk(
        0x1A,
        "开、开玩笑！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "干掉他们！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x20, 17)

    def lambda_2F14():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2F14)
    SetChrChipByIndex(0x21, 17)

    def lambda_2F2E():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2F2E)
    SetChrChipByIndex(0x22, 17)

    def lambda_2F48():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2F48)
    SetChrChipByIndex(0x23, 17)

    def lambda_2F62():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2F62)
    Sleep(250)
    SetChrChipByIndex(0x1A, 17)

    def lambda_2F81():
        OP_96(0xFE, 0xFFFF3954, 0x0, 0xFFFE84E1, 0x76C, 0x1388)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F81)
    SetChrChipByIndex(0x1B, 17)

    def lambda_2FA4():
        OP_96(0xFE, 0xFFFF3792, 0x0, 0xFFFE865F, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2FA4)
    Sleep(400)
    Battle(0x38B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2FDA"),
        (SWITCH_DEFAULT, "loc_2FDD"),
    )


    label("loc_2FDA")

    OP_B4(0x0)
    Return()

    label("loc_2FDD")

    EventBegin(0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrChipByIndex(0x1A, 16)
    SetChrChipByIndex(0x1B, 16)
    SetChrChipByIndex(0x20, 16)
    SetChrChipByIndex(0x21, 16)
    SetChrChipByIndex(0x22, 16)
    SetChrChipByIndex(0x23, 16)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x20, 0xFF)
    OP_44(0x21, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-50610, 0, -43450, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "怎、怎么了……\x01",
            "外面发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唔……就算是吵架，\x01",
            "也未免也太吵了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x101, -51210, 0, -51500, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#005F#1P大家没事吧？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3336():
        OP_6D(-50590, 0, -45100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3336)
    ClearChrFlags(0x101, 0x80)

    def lambda_3353():
        OP_8E(0xFE, 0xFFFF3562, 0x0, 0xFFFF4782, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3353)
    Sleep(200)
    SetChrPos(0x103, -51210, 0, -51500, 0)

    def lambda_3384():
        OP_8E(0xFE, 0xFFFF3A44, 0x0, 0xFFFF4638, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3384)
    Sleep(200)
    SetChrPos(0x102, -51210, 0, -51500, 0)
    SetChrFlags(0x102, 0x4)

    def lambda_33BA():
        OP_8E(0xFE, 0xFFFF3184, 0x0, 0xFFFF43AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33BA)
    Sleep(200)
    SetChrPos(0x104, -51210, 0, -51500, 0)

    def lambda_33EB():
        OP_8E(0xFE, 0xFFFF3CBA, 0x0, 0xFFFF419C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33EB)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 0)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 0, 0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x103,
        (
            "#020F我们是游击士协会的人。\x01",
            "前来营救大家。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF4A20, 0x0, 0xFFFF4C64, 0xFA0, 0x0)

    ChrTalk(
        0x9,
        (
            "真、真的吗……\x01",
            "是来救我们的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看守的空贼已经被制伏了，\x01",
            "总之请大家放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1P真、真的……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1P得、得救啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P我是定期船『林德号』的\x01",
            "机长古兰托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P真是太感谢你们了……\x01",
            "都不知该说些什么才好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F感谢的话等离开后再说吧。\x02\x03",
            "对了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 45, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F……咦？咦咦咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好像不在这里面啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F请、请问一下……\x02\x03",
            "所有的人质都在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P啊啊，说得没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P乘坐『林德号』的\x01",
            "乘客和乘务员全部都在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F请问乘客当中有没有\x01",
            "有一个叫做卡西乌斯·布莱特的人？\x02\x03",
            "他是游击士协会的成员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P卡西乌斯·布莱特……？\x01",
            "这名字我好像在哪听到过。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "啊，机长……\x01",
            "就是那位客人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0xA,
        "起航之前下机的那位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P啊啊！\x01",
            "是有这么一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F怎、怎么回事？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#1P啊，在起航之前，\x01",
            "有一位客人临时下机了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P他是在王都登机的男乘客，\x01",
            "的确，我记得就是叫这个名字。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F怎么会这样……！\x02\x03",
            "但、但是乘客名单上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P因为是起航前才下机的，\x01",
            "所以没来得及办理文件手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P本应在到达洛连特之后补办手续的，\x01",
            "但我们途中遭劫机，之后被关在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F……………………（松了口气）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F原来如此，发生了这样的事啊。\x02\x03",
            "父亲被空贼抓住，\x01",
            "这一点本来就觉得很奇怪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F呼……\x01",
            "疑惑也终于解开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#031F哈·哈·哈，可真是奇妙的巧合啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#009F慢、慢着。\x02\x03",
            "这、这么说来……\x01",
            "老爸现在到底在做什么呢？\x02\x03",
            "发生了这么大的骚动，\x01",
            "怎么也不联络我们一下！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F冷静点，艾丝蒂尔。\x02\x03",
            "这件事的确很奇怪，\x01",
            "不过现在想这问题也无济于事。\x02\x03",
            "我们必须优先\x01",
            "确保这里人质的安全。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F#2P啊……嗯。\x02\x03",
            "明白了，先不想这个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F各位，\x01",
            "我们现在要去逮捕空贼的首领。\x02\x03",
            "所以很抱歉，\x01",
            "请大家再稍稍忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P啊，好的……\x01",
            "那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "这样的话，我们就忍耐一下吧。\x01",
            "现在我们的命都交托在你们手上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "请你们无论如何也要加油！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-51030, 0, -47780, 0)
    OP_6B(2600, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    SetChrPos(0x0, -51030, 0, -47780, 0)
    SetChrPos(0x1, -51030, 0, -47780, 0)
    SetChrPos(0x2, -51030, 0, -47780, 0)
    SetChrPos(0x3, -51030, 0, -47780, 0)
    OP_0D()
    ClearMapFlags(0x400000)
    OP_A2(0x356)
    OP_28(0x39, 0x1, 0x8)
    OP_28(0x39, 0x1, 0x10)
    OP_28(0x39, 0x1, 0x20)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x18, -54970, 0, -93490, 315)
    SetChrPos(0x19, -48920, 0, -91340, 53)
    SetChrPos(0x1C, -45150, 0, -93440, 163)
    SetChrPos(0x1D, -48280, 0, -97510, 119)
    SetChrPos(0x1E, -54960, 0, -97820, 86)
    SetChrPos(0x1F, -53760, 0, -91280, 172)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x18, 28)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    Return()

    # Function_20_2A3D end

    SaveToFile()

Try(main)
