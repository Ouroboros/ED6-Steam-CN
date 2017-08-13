from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131   ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1131   ._SN',
            'ED6_DT01/T1131_1 ._SN',
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
        '梅贝尔',                               # 9
        '维尔纳',                               # 10
        '普拉达',                               # 11
        '科梅尔斯',                             # 12
        '琉肯',                                 # 13
        '西蒙',                                 # 14
        '奈尔',                                 # 15
        '雷克多主管',                           # 16
        '罗宋厨师长',                           # 17
        '格露娜',                               # 18
        '斯托隆',                               # 19
        '莉诺',                                 # 20
        '玛丽安',                               # 21
        '诺琪',                                 # 22
        '赫雷思老人',                           # 23
        '阿尔妲婆婆',                           # 24
        '卡洛塔',                               # 25
        '沙库',                                 # 26
        '雷塔',                                 # 27
        '法娜',                                 # 28
        '甜点',                                 # 29
        '甜点',                                 # 30
        '汤碗',                                 # 31
        '勺子',                                 # 32
        '叉子',                                 # 33
        '叉子',                                 # 34
        '刀子',                                 # 35
        '刀子',                                 # 36
        '料理',                                 # 37
        '酒',                                   # 38
        '茶壶',                                 # 39
        '茶壶',                                 # 40
        '茶壶',                                 # 41
        '瓶子',                                 # 42
        '酒杯',                                 # 43
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
        'ED6_DT07/CH02363 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01660 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
        'ED6_DT06/CH20086 ._CH',             # 06
        'ED6_DT07/CH01560 ._CH',             # 07
        'ED6_DT07/CH01280 ._CH',             # 08
        'ED6_DT07/CH02480 ._CH',             # 09
        'ED6_DT07/CH01570 ._CH',             # 0A
        'ED6_DT07/CH02540 ._CH',             # 0B
        'ED6_DT07/CH01213 ._CH',             # 0C
        'ED6_DT07/CH01233 ._CH',             # 0D
        'ED6_DT07/CH01003 ._CH',             # 0E
        'ED6_DT07/CH01183 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01123 ._CH',             # 11
        'ED6_DT07/CH01043 ._CH',             # 12
        'ED6_DT07/CH01053 ._CH',             # 13
        'ED6_DT07/CH00003 ._CH',             # 14
        'ED6_DT07/CH00013 ._CH',             # 15
        'ED6_DT07/CH00023 ._CH',             # 16
        'ED6_DT07/CH02060 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH02363P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01660P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
        'ED6_DT06/CH20086P._CP',             # 06
        'ED6_DT07/CH01560P._CP',             # 07
        'ED6_DT07/CH01280P._CP',             # 08
        'ED6_DT07/CH02480P._CP',             # 09
        'ED6_DT07/CH01570P._CP',             # 0A
        'ED6_DT07/CH02540P._CP',             # 0B
        'ED6_DT07/CH01213P._CP',             # 0C
        'ED6_DT07/CH01233P._CP',             # 0D
        'ED6_DT07/CH01003P._CP',             # 0E
        'ED6_DT07/CH01183P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01123P._CP',             # 11
        'ED6_DT07/CH01043P._CP',             # 12
        'ED6_DT07/CH01053P._CP',             # 13
        'ED6_DT07/CH00003P._CP',             # 14
        'ED6_DT07/CH00013P._CP',             # 15
        'ED6_DT07/CH00023P._CP',             # 16
        'ED6_DT07/CH02060P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
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
        X                   = 2970,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -6030,
        Z                   = 3350,
        Y                   = 5100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = 0,
        Y                   = 1480,
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
        X                   = -1450,
        Z                   = 3250,
        Y                   = 3420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -7300,
        Z                   = 1400,
        Y                   = -4100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196614,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -42600,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 0,
        Y                   = 46700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -47450,
        Z                   = 0,
        Y                   = 44160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -38500,
        Z                   = 1500,
        Y                   = 14200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -53300,
        Z                   = 1500,
        Y                   = 200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -52950,
        Z                   = 1600,
        Y                   = 11400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -52950,
        Z                   = 1600,
        Y                   = 8600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -45600,
        Z                   = 1600,
        Y                   = 11000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -36400,
        Z                   = 1600,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -39120,
        Z                   = 1600,
        Y                   = 7410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -39130,
        Z                   = 1600,
        Y                   = 4590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -42400,
        Z                   = 1600,
        Y                   = 11000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -39600,
        Z                   = 1600,
        Y                   = 11000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -52960,
        Z                   = 2230,
        Y                   = 9560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52940,
        Z                   = 2230,
        Y                   = 10400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 2150,
        Y                   = -1060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196633,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35750,
        Z                   = 2150,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1350,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -46510,
        Z                   = 2230,
        Y                   = 10750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393241,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -46750,
        Z                   = 2230,
        Y                   = 11300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327704,
        ChipIndex           = 0x18,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39030,
        Z                   = 2200,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703961,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39030,
        Z                   = 2200,
        Y                   = 6500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39030,
        Z                   = 2200,
        Y                   = 5300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6490,
        Z                   = 2100,
        Y                   = -3560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6360,
        Z                   = 2100,
        Y                   = -4420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3050,
        TriggerZ            = 0,
        TriggerY            = 1520,
        TriggerRange        = 400,
        ActorX              = 2970,
        ActorZ              = 1500,
        ActorY              = 3650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5FE",          # 00, 0
        "Function_1_6DB",          # 01, 1
        "Function_2_6DC",          # 02, 2
        "Function_3_6F2",          # 03, 3
        "Function_4_716",          # 04, 4
        "Function_5_C53",          # 05, 5
        "Function_6_C77",          # 06, 6
        "Function_7_EFC",          # 07, 7
        "Function_8_F01",          # 08, 8
        "Function_9_1572",         # 09, 9
        "Function_10_1AB5",        # 0A, 10
        "Function_11_208E",        # 0B, 11
        "Function_12_299A",        # 0C, 12
        "Function_13_2C2C",        # 0D, 13
        "Function_14_4807",        # 0E, 14
        "Function_15_52E2",        # 0F, 15
        "Function_16_575D",        # 10, 16
        "Function_17_5D5D",        # 11, 17
        "Function_18_6276",        # 12, 18
        "Function_19_669E",        # 13, 19
        "Function_20_6C69",        # 14, 20
        "Function_21_7194",        # 15, 21
        "Function_22_780C",        # 16, 22
        "Function_23_7C9A",        # 17, 23
        "Function_24_7EE6",        # 18, 24
        "Function_25_8267",        # 19, 25
        "Function_26_841A",        # 1A, 26
        "Function_27_8606",        # 1B, 27
        "Function_28_915A",        # 1C, 28
    )


    def Function_0_5FE(): pass

    label("Function_0_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_60C")
    OP_A3(0x3FA)
    Event(0, 27)

    label("loc_60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_62F")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0xB, 0x80)
    Jump("loc_6DA")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_64D")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    Jump("loc_6DA")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_66B")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    Jump("loc_6DA")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_675")
    Jump("loc_6DA")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_697")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    Jump("loc_6DA")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_END)), "loc_6AB")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_6DA")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_6BA")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_6DA")

    label("loc_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6C9")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_6DA")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6DA")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)

    label("loc_6DA")

    Return()

    # Function_0_5FE end

    def Function_1_6DB(): pass

    label("Function_1_6DB")

    Return()

    # Function_1_6DB end

    def Function_2_6DC(): pass

    label("Function_2_6DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6DC")

    label("loc_6F1")

    Return()

    # Function_2_6DC end

    def Function_3_6F2(): pass

    label("Function_3_6F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_715")
    OP_8D(0xFE, 1450, 3690, 4800, 3990, 1000)
    Jump("Function_3_6F2")

    label("loc_715")

    Return()

    # Function_3_6F2 end

    def Function_4_716(): pass

    label("Function_4_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_855")

    label("loc_721")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_852")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_721")

    label("loc_852")

    Jump("loc_C52")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_944")

    label("loc_860")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_941")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15E, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0x44C, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_860")

    label("loc_941")

    Jump("loc_C52")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A7F")

    label("loc_94B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_94B")

    label("loc_A7C")

    Jump("loc_C52")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_B6A")

    label("loc_A86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B67")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15E, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0x44C, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_A86")

    label("loc_B67")

    Jump("loc_C52")

    label("loc_B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C52")

    label("loc_B71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C52")
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15E, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0x44C, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFBB4, 0x0, 0x1130, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xDAC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("loc_B71")

    label("loc_C52")

    Return()

    # Function_4_716 end

    def Function_5_C53(): pass

    label("Function_5_C53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C76")
    OP_8D(0xFE, -48200, 42570, -46450, 46500, 1000)
    Jump("Function_5_C53")

    label("loc_C76")

    Return()

    # Function_5_C53 end

    def Function_6_C77(): pass

    label("Function_6_C77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFB")
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xCE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x21FC, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2580, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D18, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF4D7C, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5FD8, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x1F40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6DE8, 0x5DC, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF72FC, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF748C, 0x5DC, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF7428, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7748, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x960, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF3990, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x1CE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x9C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF2FCC, 0x5DC, 0xC8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    Jump("Function_6_C77")

    label("loc_EFB")

    Return()

    # Function_6_C77 end

    def Function_7_EFC(): pass

    label("Function_7_EFC")

    Call(0, 8)
    Return()

    # Function_7_EFC end

    def Function_8_F01(): pass

    label("Function_8_F01")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                     # 0
            "买东西\x01",                                   # 1
            "欢迎品尝「仰天奶酪肉汁烩饭」300米拉\x01",      # 2
            "离开\x01",                                     # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F83")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x1D)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_F83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1080")
    SubMira(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "尝了尝\x07\x02",
            "仰天奶酪肉汁烩饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFC, 0x0)
    OP_31(0x1, 0xFC, 0x0)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x3, 0xFC, 0x0)
    OP_31(0x4, 0xFC, 0x0)
    OP_31(0x5, 0xFC, 0x0)
    OP_31(0x6, 0xFC, 0x0)
    OP_31(0x7, 0xFC, 0x0)
    OP_31(0x0, 0xFD, 0x96)
    OP_31(0x1, 0xFD, 0x96)
    OP_31(0x2, 0xFD, 0x96)
    OP_31(0x3, 0xFD, 0x96)
    OP_31(0x4, 0xFD, 0x96)
    OP_31(0x5, 0xFD, 0x96)
    OP_31(0x6, 0xFD, 0x96)
    OP_31(0x7, 0xFD, 0x96)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1072")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x5)"), scpexpr(EXPR_END)), "loc_1044")
    Jump("loc_1072")

    label("loc_1044")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "仰天奶酪肉汁烩饭\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1072")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_10A6")

    label("loc_1080")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_10A6")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x9)
    Return()

    label("loc_10B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CF")
    FadeToBright(300, 0)
    TalkEnd(0x9)
    Return()

    label("loc_10CF")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1175")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "强盗事件原来是\x01",
            "空贼团所犯下的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过最后，\x01",
            "摩尔根将军率领的王国军队\x01",
            "把他们一网打尽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好久都没有\x01",
            "感到这么轻松愉快了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CD")

    label("loc_1175")


    ChrTalk(
        0x9,
        (
            "摩尔根将军率领的王国军队\x01",
            "把空贼们一网打尽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好久都没有\x01",
            "感到这么轻松愉快了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CD")

    Jump("loc_156E")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1232")

    ChrTalk(
        0x9,
        (
            "最近，\x01",
            "总是发生一些让人不安的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们做百姓的只是希望\x01",
            "能过上些安稳的日子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156E")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_12A8")

    ChrTalk(
        0x9,
        (
            "南街区的商店街\x01",
            "好像都被强盗搞得一团乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "柏斯是一个聚财的地方，\x01",
            "自古以来这样的事件就没有断绝过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156E")

    label("loc_12A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_130B")

    ChrTalk(
        0x9,
        (
            "我开这家店与其说是做生意，\x01",
            "不如说是凭兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "如果能让客人感到更放松一点就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_156E")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_13C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1387")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "安特洛丝餐厅\x01",
            "不是能让人久坐的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "相反我们的店子\x01",
            "可以为各位食客营造\x01",
            "一个放松舒适的环境。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C6")

    label("loc_1387")


    ChrTalk(
        0x9,
        "宾至如归的酒馆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，\x01",
            "就以这个作为关键词来努力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C6")

    Jump("loc_156E")

    label("loc_13C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_152E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C9")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "经常有客人把本店\x01",
            "和安特洛丝餐厅相比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们和他们本来就不是一回事，\x01",
            "没有拿来比的必要吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "便宜又方便地享受快餐\x01",
            "是我们的宗旨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而安特洛丝餐厅则只提供\x01",
            "有格调的高档料理和服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "面向的客户群不同，\x01",
            "也不会互相竞争吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152B")

    label("loc_14C9")


    ChrTalk(
        0x9,
        (
            "经常有客人把本店\x01",
            "和安特洛丝餐厅相比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们和他们本来就不是一回事，\x01",
            "没有拿来比的必要吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152B")

    Jump("loc_156E")

    label("loc_152E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_156E")

    ChrTalk(
        0x9,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "本酒馆的饭菜\x01",
            "又便宜又好吃哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156E")

    TalkEnd(0x9)
    Return()

    # Function_8_F01 end

    def Function_9_1572(): pass

    label("Function_9_1572")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_15B6")

    ChrTalk(
        0xFE,
        "工作工作～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要赶快把麻烦的事情\x01",
            "全部处理掉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB1")

    label("loc_15B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1688")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "城里还是有案件接连发生，\x01",
            "不过我们店里却风平浪静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这大概正如店长所说的，\x01",
            "我们店里的气氛\x01",
            "能让人感到轻松自如吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然觉得有些无聊……\x01",
            "不过没和案件扯上关系，\x01",
            "也算是一件好事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1701")

    label("loc_1688")


    ChrTalk(
        0xFE,
        (
            "城里还是有案件接连发生，\x01",
            "不过我们店里却风平浪静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这大概正如店长所说的，\x01",
            "我们店里的气氛\x01",
            "能让人感到轻松自如吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1701")

    Jump("loc_1AB1")

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_185C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "强盗果然是\x01",
            "懂得选择场所下手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "南街区有许多\x01",
            "大商店和商人住宅，\x01",
            "但是那里晚上却很少有行人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使他们袭击我们这家店，\x01",
            "估计也只能抢走些食材吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "连这个也偷的话那和老鼠有啥区别。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_17D9")


    ChrTalk(
        0xFE,
        (
            "强盗果然是\x01",
            "懂得选择场所下手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使他们袭击我们这家店，\x01",
            "估计也只能抢走些食材吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "连这个也偷的话那和老鼠有啥区别。\x02",
    )

    CloseMessageWindow()

    label("loc_1859")

    Jump("loc_1AB1")

    label("loc_185C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(
        0xFE,
        (
            "店长经常一本正经地说\x01",
            "这家店是按照他的品位开的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，传说那家安特洛丝餐厅\x01",
            "也是老板根据自己的品位而经营的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "品位的等级还真是相差得很远呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AB1")

    label("loc_1902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_19E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199B")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "我们店里的客人\x01",
            "好像大多都喜欢一直坐在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是不是谈生意的人比较多的缘故呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里是个休闲的地方，\x01",
            "能让人们心情舒畅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E5")

    label("loc_199B")


    ChrTalk(
        0xFE,
        (
            "喝醉酒说胡话的客人，\x01",
            "或者其他奇怪的客人有不少，\x01",
            "这也是这里的特征吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E5")

    Jump("loc_1AB1")

    label("loc_19E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1A80")

    ChrTalk(
        0xFE,
        (
            "经常有客人把本店\x01",
            "有些客人总喜欢拿我们和那家作比较。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总是说这些也没什么用吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那边是有钱人去的地方。\x01",
            "而我们这里则面向工薪阶层。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB1")

    label("loc_1A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1AB1")

    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请到空位上入座吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1AB1")

    TalkEnd(0xA)
    Return()

    # Function_9_1572 end

    def Function_10_1AB5(): pass

    label("Function_10_1AB5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3C")
    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "尼冈德那家伙\x01",
            "被带到哈肯门去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那家伙好像\x01",
            "做了相当坏的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如果能找出\x01",
            "他骗人的证据就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B61")

    label("loc_1B3C")


    ChrTalk(
        0xB,
        (
            "尼冈德那家伙\x01",
            "被带到哈肯门去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B61")

    Jump("loc_208A")

    label("loc_1B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1C50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF7")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "刚才有军队上的人\x01",
            "来我这里打听情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们问我工房\x01",
            "最近的经营状况怎么样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在我更奇怪了，到底发生了什么事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C4D")

    label("loc_1BF7")


    ChrTalk(
        0xFE,
        (
            "刚才有军队上的人\x01",
            "来我这里打听情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们问我工房\x01",
            "最近的经营状况怎么样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4D")

    Jump("loc_208A")

    label("loc_1C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD5")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我所经营的工房\x01",
            "也被强盗袭击了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尼冈德那家伙也就算了，\x01",
            "我只担心雇来的工匠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果没事就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D2D")

    label("loc_1CD5")


    ChrTalk(
        0xFE,
        (
            "我所经营的工房\x01",
            "也被强盗袭击了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尼冈德那家伙也就算了，\x01",
            "我只担心雇来的工匠。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2D")

    Jump("loc_208A")

    label("loc_1D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB6")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "……就这样一直哭\x01",
            "也无济于事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工房被抢只能说明\x01",
            "自己太缺乏经验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好，在柏斯超市\x01",
            "重新开始创业吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E02")

    label("loc_1DB6")


    ChrTalk(
        0xFE,
        (
            "工房被抢只能说明\x01",
            "自己太缺乏经验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好，在柏斯超市\x01",
            "重新开始创业吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E02")

    Jump("loc_208A")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE4")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "尼冈德那家伙真该死……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一直以来和我合作得好好的，\x01",
            "竟然突然背叛我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来工房借债就是\x01",
            "他用强硬手段逼我签下的合同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且现在他竟然\x01",
            "成为了工房的店主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底是怎么回事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EFC")

    label("loc_1EE4")


    ChrTalk(
        0xFE,
        "到底是怎么回事……\x02",
    )

    CloseMessageWindow()

    label("loc_1EFC")

    Jump("loc_208A")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD0")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "那间导力器工房\x01",
            "一直以来是我经营的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有一次，\x01",
            "借了他的钱却没办法还清……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他就以这个借口\x01",
            "把我的店抢走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还想着从超市独立出来\x01",
            "经营自己的店的梦想终于实现了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202D")

    label("loc_1FD0")


    ChrTalk(
        0xFE,
        (
            "本来还想着从超市独立出来\x01",
            "经营自己的店的梦想终于实现了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊～未来一片黑暗……\x02",
    )

    CloseMessageWindow()

    label("loc_202D")

    Jump("loc_208A")

    label("loc_2030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_208A")

    ChrTalk(
        0xFE,
        "啊啊……啊呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我倾注了一生的\x01",
            "那间工房……啊呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208A")

    TalkEnd(0xB)
    Return()

    # Function_10_1AB5 end

    def Function_11_208E(): pass

    label("Function_11_208E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_218E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213A")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这个地方果然保存着\x01",
            "关于目击到古代龙的记载。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼呼呼，我的热情燃烧起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它们为什么会突然失踪……\x01",
            "这一谜题的答案说不定很快就能揭晓。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218B")

    label("loc_213A")


    ChrTalk(
        0xFE,
        (
            "这个地方还保存着\x01",
            "关于目击到古代龙的记载。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼呼呼，我的热情燃烧起来了。\x02",
    )

    CloseMessageWindow()

    label("loc_218B")

    Jump("loc_2996")

    label("loc_218E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_226F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221B")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "古代龙最后被目击的地点\x01",
            "就是在这个柏斯地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "我才会到这里来进行调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "首先要仔细收集当地的情报。\x02",
    )

    CloseMessageWindow()
    Jump("loc_226C")

    label("loc_221B")


    ChrTalk(
        0xFE,
        (
            "古代龙最后被目击的地点\x01",
            "就是在这个柏斯地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "首先要仔细收集当地的情报。\x02",
    )

    CloseMessageWindow()

    label("loc_226C")

    Jump("loc_2996")

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_22DF")

    ChrTalk(
        0xFE,
        (
            "在『大崩坏』之前\x01",
            "就已经存在的古代龙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它们好像是按照自己的意志\x01",
            "而选择在这个世界上消失的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_22DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_259E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2542")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我的研究对象是在『大崩坏』以前的\x01",
            "旧世界中生存的生物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "被称为比人类还要聪明，\x01",
            "近似于神的存在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对，就是指古代龙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，在主日学校学到过呢。\x02\x03",
            "但不是说，古代龙直到数十年前\x01",
            "还在利贝尔王国生存的吗？\x02\x03",
            "可是，自从导力器发明出来之后，\x01",
            "它们就消失无踪了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F……………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#501F怎么了，约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没什么，\x01",
            "只是觉得你能记得上课讲的东西，\x01",
            "还真是难得啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F真是没礼貌啊～\x02\x03",
            "#000F因为，\x01",
            "体型那么大头脑又好的生物，\x01",
            "听起来就很想亲眼看看呢。\x02\x03",
            "#001F只是想想就觉得很兴奋。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0xFE,
        (
            "哈哈，我也想亲眼看看呢。\x01",
            "所以才在各地进行调查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_259B")

    label("loc_2542")


    ChrTalk(
        0xFE,
        (
            "我的研究对象是在『大崩坏』以前的\x01",
            "在旧世界生存的智慧生物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对，就是指古代龙。\x02",
    )

    CloseMessageWindow()

    label("loc_259B")

    Jump("loc_2996")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_26C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265A")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "在『大崩坏』之前，\x01",
            "大陆上好像有比现在\x01",
            "更加优秀的导力技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且现在也发现了\x01",
            "在『大崩坏』之前的时代\x01",
            "所使用过的导力装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以『古代遗物』相称\x01",
            "也毫不为过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BD")

    label("loc_265A")


    ChrTalk(
        0xFE,
        (
            "现在也发现了\x01",
            "在『大崩坏』之前的时代\x01",
            "所使用过的导力装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以『古代遗物』相称\x01",
            "也毫不为过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BD")

    Jump("loc_2996")

    label("loc_26C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_27FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2773")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "你知道『大崩坏』吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很久很久以前，在这块大陆上\x01",
            "有高度发达的导力文明存在着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过后来因为一场被称为『大崩坏』的\x01",
            "天地异变的破坏而全部消失掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27F7")

    label("loc_2773")


    ChrTalk(
        0xFE,
        (
            "很久很久以前，在这块大陆上\x01",
            "有高度发达的导力文明存在着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过后来因为一场被称为『大崩坏』的\x01",
            "天地异变的破坏而全部消失掉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F7")

    Jump("loc_2996")

    label("loc_27FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2902")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "我是一个\x01",
            "研究古代生物的学者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "之前去进行地质调查的时候，\x01",
            "无意间发现一只行动非常敏捷的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好像就是在西柏斯街道上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那是种非常珍贵的魔兽，\x01",
            "虽然我想抓住它，\x01",
            "但是凭我的脚力是追不上的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "看来还是要多做点运动啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2902")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "之前去进行地质调查的时候，\x01",
            "无意间发现一只行动非常敏捷的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那是种非常珍贵的魔兽，\x01",
            "虽然我想抓住它，\x01",
            "但是凭我的脚力是追不上的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2996")

    TalkEnd(0xC)
    Return()

    # Function_11_208E end

    def Function_12_299A(): pass

    label("Function_12_299A")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2F")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "特里诺家的米拉诺，\x01",
            "现在可以称得上是\x01",
            "实力仅次于市长的女强人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "博尔德家也非常有实力，\x01",
            "但是如今，形势倾向于米拉诺啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A91")

    label("loc_2A2F")


    ChrTalk(
        0xFE,
        (
            "我自己将来\x01",
            "该怎么生活下去才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "协助米拉诺工作也不错，\x01",
            "但是我还是想做自己喜欢的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A91")

    Jump("loc_2C28")

    label("loc_2A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B61")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "米拉诺突然请了急假，\x01",
            "到底是怎么回事……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "飞艇停止航行\x01",
            "不是无法进行工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她老是说忙的时候\x01",
            "才会想做这样那样的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在休息的时候\x01",
            "反而会觉得什么事情就做不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB7")

    label("loc_2B61")


    ChrTalk(
        0xFE,
        (
            "米拉诺突然请了急假\x01",
            "到底是怎么回事……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "飞艇停止航行\x01",
            "不是无法进行工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB7")

    Jump("loc_2C28")

    label("loc_2BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(
        0xFE,
        (
            "哈啊……\x01",
            "陪着米拉诺还真累啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但正因为有那种干劲，\x01",
            "所以才能称得上实力\x01",
            "仅次于市长的女强人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C28")

    TalkEnd(0xD)
    Return()

    # Function_12_299A end

    def Function_13_2C2C(): pass

    label("Function_13_2C2C")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4616")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -7020, 1500, -2310, 180)
    SetChrPos(0x102, -5070, 1500, -2700, 225)
    SetChrPos(0x103, -6250, 1500, -1960, 180)
    OP_6D(-7050, 1500, -2350, 0)
    OP_0D()
    OP_A2(0x318)
    OP_28(0x36, 0x4, 0x2)
    OP_28(0x36, 0x4, 0x4)
    OP_28(0x36, 0x1, 0x1)
    OP_28(0xE, 0x4, 0x40)
    OP_28(0x15, 0x4, 0x40)

    ChrTalk(
        0xE,
        (
            "#145F呜……可恶……\x02\x03",
            "真是的……别开玩笑了……\x02\x03",
            "……呜……嗝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F人是找到了，\x01",
            "可是喝得烂醉的样子……\x02\x03",
            "只不过是被拒绝采访，\x01",
            "受到的打击有那么大吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F明明是个大男人，还真是没出息啊。\x02\x03",
            "酒是用来喝的，\x01",
            "可不是用来灌的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 0)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#007F一般人当然没法和\x01",
            "无底洞一样的雪拉姐相提并论啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F说得真过分，\x01",
            "无底洞用来形容爱娜还差不多。\x02\x03",
            "那个女人不管喝多少，\x01",
            "都是面不改色、泰然自若呢。\x02\x03",
            "和我这种舒爽自然的醉酒方式\x01",
            "根本不能混为一谈啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F什么舒爽自然的醉酒方式啊。\x02\x03",
            "明明总是喝得酩酊大醉，\x01",
            "只会一个劲儿地连累周围的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F如果说雪拉姐姐是酒桶的话，\x01",
            "那么爱娜姐姐给人的感觉就是酒缸。\x02\x03",
            "两人的酒量都没有界限这一点，\x01",
            "我倒是觉得没有什么不同……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#022F哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#145F……唔…………\x02",
    )

    CloseMessageWindow()

    def lambda_2F7F():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F7F)

    def lambda_2F8D():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F8D)
    OP_6D(-7050, 1500, -2800, 1000)
    OP_62(0xE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(300)
    SetChrSubChip(0xE, 0)
    Sleep(900)

    ChrTalk(
        0xE,
        "#142F呜～这里是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像醒过来了。\x01",
            "酒喝得太多对身体可不好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#145F呜……\x01",
            "脑袋里像在打鼓一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0xE, 1)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#143F……怎么回事？\x01",
            "这不是那两个游击士新人吗。\x02\x03",
            "喂喂，\x01",
            "为什么我还在洛连特啊！？\x02\x03",
            "明明已经来到柏斯了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F你还没睡醒吧。\x01",
            "是我们也到柏斯来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#145F呼……\x01",
            "真是吓了我一跳……\x02\x03",
            "#141F哎哟，这次是和一位\x01",
            "性感的姐姐一起来的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F初次见面，记者先生。\x01",
            "我是雪拉扎德·哈维。\x02\x03",
            "是这两个孩子的前辈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#143F雪拉扎德……\x02\x03",
            "难道说你就是\x01",
            "那个『银闪雪拉扎德』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F哎呀，真荣幸。\x01",
            "竟然知道我的名字呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#141F啊啊，以前听过你的传闻。\x02\x03",
            "『银闪』可是年轻一辈的\x01",
            "游击士中数一数二的人物啊。\x02\x03",
            "也就是说，\x01",
            "你们几个是来调查这次事件的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F啊，算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你收集到什么情报了吗？\x02\x03",
            "刚才在市长家门前看到你了，\x01",
            "好像遇到什么困难的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#145F可恶，被你们看见了啊……\x02\x03",
            "#144F没错，就是这样！\x01",
            "我正为没有材料可写而发愁啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊，果然是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#142F都是因为军队的什么情报管制，\x01",
            "搞得我们连这件事到底是不是事故都不知道。\x02\x03",
            "为了和摩尔根将军会面，\x01",
            "我们去了哈肯大门，\x01",
            "中途在检查站给拦了下来……\x02\x03",
            "我们想，那么至少采访一下\x01",
            "那位传说中的美人市长吧，\x01",
            "又被女佣给挡在门外……\x02\x03",
            "再加上，那个傻丫头\x01",
            "时不时地犯些愚蠢的错误……\x02\x03",
            "#145F唉，女神啊！\x01",
            "告诉我该怎么办呀！ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F好像被逼到绝境了呢～\x02\x03",
            "如果这么想得到情报的话，\x01",
            "告诉你也不是不可以……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#143F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F我们现在正在协助\x01",
            "梅贝尔市长调查这次的事件。\x02\x03",
            "由于市长的介绍，\x01",
            "我们也见到了摩尔根将军。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#143F…………………真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嗯，真的。\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#147F噢噢噢噢噢噢！\x01",
            "这真是女神的相助！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#144F无论如何也拜托了！\x01",
            "把这件事的详情全告诉我吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F告诉你倒是没什么关系……\x02\x03",
            "#010F奈尔先生，\x01",
            "你没有忘记这种情况下的规则吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#143F#1P……哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F呵呵……\x01",
            "也就是说情报不是免费的。\x02\x03",
            "需要付出一定的代价。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0xE,
        (
            "#142F#1P难、难道是要钱？\x02\x03",
            "不是我骗你们，\x01",
            "我这次的取材费差不多快用完了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们又不是情报站，\x01",
            "所以不会要钱的。\x02\x03",
            "奈尔先生，你们是不是\x01",
            "在事件发生之后就立刻来到柏斯了？\x02\x03",
            "之后一定听说了\x01",
            "各种各样有趣的事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#145F#1P嘁，摆出一副大人的样子，\x01",
            "真是个滑头的小鬼……\x02\x03",
            "话说在前面，\x01",
            "我这里的消息可不是什么大情报哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F只要是和事件相关，\x01",
            "无论多么细微的情报都没有关系。\x02\x03",
            "#019F不过……\x01",
            "如果你舍不得说出来，那我们也不勉强你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#144F#1P我知道了，我全说出来总行了吧！\x02\x03",
            "我这里有两条消息。\x01",
            "就用这些和你们交换吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F那就这样定了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        "#006F（约修亚真是能说会道啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F（呵呵，看起来\x01",
            "　讨价还价的本事相当不错嘛。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(3330, 0, -1410, 0)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0x101, 5100, 200, -1040, 270)
    SetChrPos(0x102, 5100, 200, -2450, 270)
    SetChrPos(0x103, 2950, 200, -2590, 90)
    SetChrPos(0xE, 2950, 0, -1070, 90)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 21)
    SetChrChipByIndex(0x103, 22)
    SetChrSubChip(0x102, 2)
    SetChrSubChip(0x103, 1)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#140F#2P第一条消息，\x01",
            "是在西边的拉文努村的目击情报。\x02\x03",
            "是从正好来到柏斯市的\x01",
            "村民那里打听来的。\x02\x03",
            "事件发生的当晚，\x01",
            "有村民目击到夜空中有个巨大的影子飞过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F夜空中有个巨大的影子飞过？\x01",
            "那、那是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#142F#2P嗯，不管谁听到\x01",
            "都会认为是那艘定期船吧？\x02\x03",
            "#145F之后，军方也派了部队去调查，\x01",
            "但结果好像什么也没发现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F什么呀。\x01",
            "害我白期待了半天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F那就是说，只是单纯的看错了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#144F#2P所以我不是说了吗！\x01",
            "不是什么大情报啦！\x02\x03",
            "即使像这种小消息，在情报管制下，\x01",
            "收集起来也是相当辛苦的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P您辛苦了。\x01",
            "那么，另外一条消息是？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 2)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#142F#2P哼……\x02\x03",
            "……另一条是，\x01",
            "军队的情报部好像开始有所行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F情报部？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F我倒是听说过这方面的传闻。\x02\x03",
            "最近，王国军新设立了一个\x01",
            "专门负责情报收集和分析的机构。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#140F#2P对，据说是个\x01",
            "与王室亲卫队并立的精英组织。\x02\x03",
            "担任司令的是一位\x01",
            "叫作理查德上校的人，\x01",
            "据说是相当干练的军人呢。\x02\x03",
            "人们都在议论，如果由他出马的话，\x01",
            "这件事一定会顺利解决的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……\x02\x03",
            "可是，这种消息对我们的调查\x01",
            "好像没什么帮助呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#144F#2P那就抱歉了，没帮上什么忙！\x02\x03",
            "不过，约定就是约定！\x01",
            "你们自己也这么说的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#3P嗯，那个请不用担心。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚把在洛连特发生的事件和\x01",
            "从摩尔根将军处听到的消息\x01",
            "全部告诉了奈尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xE,
        (
            "#143F#2P空贼团『卡普亚一家』……\x01",
            "向王家和飞艇公社提出赎金要求……\x02\x03",
            "#147F就是这个！\x01",
            "这就是我死也要得到的\x01",
            "所谓的决定性情报！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P现在满足了吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 2)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#141F#2P当然啦！\x01",
            "这样就能够写报道了！\x02\x03",
            "不能再耽搁了……\x01",
            "得赶快找到朵洛希那家伙！\x02\x03",
            "#144F就这样，再见啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 0)
    SetChrChipByIndex(0xE, 23)
    OP_96(0xE, 0xBAE, 0x0, 0xFFFFFF88, 0x258, 0x1F40)
    OP_43(0x101, 0x2, 0x0, 0x1C)

    def lambda_4030():
        OP_6D(2130, 0, -2640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4030)
    OP_8E(0xE, 0x5D2, 0x0, 0xFFFFFE8E, 0x1770, 0x1)
    OP_8E(0xE, 0x6E, 0xC8, 0xFFFFE9B2, 0x1770, 0x1)

    def lambda_4070():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4070)
    OP_8E(0xE, 0x32, 0xC8, 0xFFFFE0C0, 0xBB8, 0x0)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0x101, 0x3)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F好，好强的气势……\x02",
    )

    CloseMessageWindow()

    def lambda_40D9():
        OP_6D(3330, 0, -1410, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_40D9)
    Sleep(500)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(100)
    SetChrSubChip(0x103, 0)
    Sleep(300)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x102,
        (
            "#010F#3P最近老是为取材的事烦恼，\x01",
            "快被逼到绝境了吧。\x02\x03",
            "能帮上忙真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P你还敢说呢。\x01",
            "刚才还在一本正经地讨价还价。\x02\x03",
            "你呀，有时候还真是一肚子坏水……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#3P我并没有别的意思。\x02\x03",
            "这只不过是\x01",
            "以互惠互利为前提的商谈而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F呵呵，说得很有道理。\x02\x03",
            "游击士所接触的\x01",
            "可不光是善良的人啊。\x02\x03",
            "如果交涉对象并非通情达理之辈，\x01",
            "强硬一点也是必要的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F#2P唔～对于我来说，\x01",
            "做到这一点可是很难啊……\x02\x03",
            "#006F……啊，不说这个了！\x02\x03",
            "夜空中飞过的黑影……\x01",
            "你们不觉得这说法很让人在意吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#3P是拉文努村的目击情报吗。\x02\x03",
            "既然军队已经调查过，\x01",
            "我认为实际是误报的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P可是可是，\x01",
            "那个调查也许不是很全面啊。\x02\x03",
            "倒也不是针对摩尔根将军，\x01",
            "不过那些军人好像都有点死脑筋，\x01",
            "他们总会看漏了什么地方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#3P确实如此……\x02\x03",
            "#010F即使没用，也应该去调查一下。\x01",
            "说不定会有什么收获呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_END)), "loc_44B8")

    ChrTalk(
        0x103,
        (
            "#021F呵呵，\x01",
            "你们两个都成长了不少啊。\x02\x03",
            "#020F既然这样，\x01",
            "我们就赶快去拉文努村看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4561")

    label("loc_44B8")


    ChrTalk(
        0x103,
        (
            "#021F呵呵，\x01",
            "你们两个都成长了不少啊。\x02\x03",
            "#020F拉文努村，是西边的一个\x01",
            "以果树栽培而闻名的小村落。\x02\x03",
            "在西柏斯街道途中有一条向北的山道，\x01",
            "村子就在那边哦。\x02\x03",
            "我们立刻出发吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4561")


    ChrTalk(
        0x101,
        "#006F#2P好！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0xE, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, 1150, 0, -2300, 180)
    SetChrPos(0x103, 1150, 0, -2300, 180)
    SetChrPos(0x102, 1150, 0, -2300, 180)
    OP_69(0x101, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_4803")

    label("loc_4616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_46FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BC")
    OP_A2(0x6)

    ChrTalk(
        0xE,
        "#146F嗝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F喂，奈尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#146F…………………………\x02\x03",
            "既然这样，\x01",
            "我只好再去追其它的新闻线索了……\x02\x03",
            "嗝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F这样不行啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_46FA")

    label("loc_46BC")


    ChrTalk(
        0xE,
        (
            "#146F嗝……\x02\x03",
            "既然这样，\x01",
            "我只好再去追其它的新闻线索了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46FA")

    Jump("loc_4803")

    label("loc_46FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47BF")
    OP_A2(0x6)

    ChrTalk(
        0x102,
        "#010F啊，奈尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#146F呜～……嗝……\x02\x03",
            "真是的，\x01",
            "好不容易从洛连特走着来到这里……\x02\x03",
            "咕噜咕噜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎呀，喝得烂醉呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F能醉成这个样子，真是差劲呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4803")

    label("loc_47BF")


    ChrTalk(
        0xE,
        (
            "#146F呜～……嗝……\x02\x03",
            "真是的，\x01",
            "好不容易从洛连特走着来到这里……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4803")

    TalkEnd(0xE)
    Return()

    # Function_13_2C2C end

    def Function_14_4807(): pass

    label("Function_14_4807")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4871")

    ChrTalk(
        0xFE,
        (
            "多亏了这一连串事件得到解决，\x01",
            "顾客们的脸色也都喜气洋洋的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "果然和平还是最美好的啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_52DE")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4902")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "最近，好像城里非常多事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店是否也要\x01",
            "配备几名警备比较好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果万一有客人遭遇到什么不幸，\x01",
            "那就糟糕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494D")

    label("loc_4902")


    ChrTalk(
        0xFE,
        "最近，好像城里非常多事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店是否也要\x01",
            "配备几名警备比较好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_494D")

    Jump("loc_52DE")

    label("loc_4950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4C1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC7")
    OP_A2(0x38D)
    TurnDirection(0xFE, 0x104, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)

    ChrTalk(
        0xFE,
        "咦，你、你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不，你是那个时候的……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哟，主管先生。\x01",
            "上次真是多谢您的款待了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊——！\x01",
            "你、你不是已经被交给士兵了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这、这样的话，\x01",
            "我是不是要再通报一次……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵，你就冷静一下嘛。\x02\x03",
            "#030F你们能请我来吃饭已经算十分荣幸的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#035F能够理解我这位极富艺术修养的人才的人，\x01",
            "也唯有你们餐厅的老板了。\x01",
            "　\x02\x03",
            "而且，\x01",
            "她还是一位如此闭月羞花的美丽女性。\x02\x03",
            "#030F这家安特洛丝餐厅的将来，\x01",
            "必定会如同沐浴在春日阳光下一般明艳动人。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F主管先生……\x01",
            "我真的非常同情你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F嗯嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C19")

    label("loc_4BC7")


    ChrTalk(
        0xFE,
        (
            "这次的事情\x01",
            "是作为主管的我失职引起的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～……\x01",
            "我真是对不起老板啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C19")

    Jump("loc_52DE")

    label("loc_4C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB5")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "欢、欢迎光临……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F（怎么了，\x01",
            "　看起来样子相当没精神呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F（嗯，腰也直不起来了。\x01",
            "　难道发生了什么事吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CDC")

    label("loc_4CB5")


    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "这件事该如何向老板交待呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDC")

    Jump("loc_52DE")

    label("loc_4CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_4E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DEF")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "现在，我们正在寻找一位\x01",
            "能为本店弹琴的专属钢琴家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是在国内好像\x01",
            "没有什么非常出色的人才。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我已经跟老板商量过了，\x01",
            "我们正在打算从帝国\x01",
            "那里请一位钢琴家过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F哎～钢琴家啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真、真不愧是一流的餐厅，\x01",
            "规模就是不一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E9B")

    label("loc_4DEF")


    ChrTalk(
        0xFE,
        (
            "现在，我们正在寻找一位\x01",
            "能为本店弹琴的专属钢琴家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是在国内好像\x01",
            "没有什么非常出色的人才。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我已经跟老板商量过了，\x01",
            "我们正在打算从帝国\x01",
            "那里请一位钢琴家过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E9B")

    Jump("loc_52DE")

    label("loc_4E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB9")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "感谢光临本店用餐。\x01",
            "请慢走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们衷心希望\x01",
            "客人能够再次光临本店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～ \x01",
            "刚才是市长请客吧，\x01",
            "到底花了多少钱呢？\x02\x03",
            "#009F凭我们自己的工资\x01",
            "大概是消费不起的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是呀……\x01",
            "不过，味道的确很不错，\x01",
            "物有所值呢。\x02\x03",
            "真是名不虚传。\x01",
            "不愧是专家的手艺。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5003")

    label("loc_4FB9")


    ChrTalk(
        0xFE,
        (
            "感谢光临本店用餐。\x01",
            "请慢走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们衷心希望\x01",
            "客人能够再次光临本店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5003")

    Jump("loc_52DE")

    label("loc_5006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_52DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5263")
    OP_A2(0x38C)

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是安特洛丝餐厅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请问客人预约了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……没有。\x02\x03",
            "这里是饭店吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "您说得没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是老板委任的主管，\x01",
            "名叫雷克多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店时时刻刻\x01",
            "以最高级的食品和最优质的服务，\x01",
            "来期待各位客人的光临。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有自信能够为每位顾客\x01",
            "提供满意的饭菜和服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请一定要来本店体验一次。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F相当的自信呢。\x01",
            "不过确实，从店的规模就能看出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F他说让我们一定要体验一次呢。\x01",
            "　\x02\x03",
            "应该会很贵吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 0)

    ChrTalk(
        0x103,
        (
            "#020F呵呵，那是肯定的了。\x02\x03",
            "如果想享受一次正餐的话……\x01",
            "　\x02\x03",
            "至少要消灭三十只通缉魔兽\x01",
            "得到的报酬才够吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    ChrTalk(
        0x101,
        "#007F唉，这里和我没有缘分呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_52DE")

    label("loc_5263")


    ChrTalk(
        0xFE,
        (
            "本店时时刻刻\x01",
            "以最高级的食品和最优质的服务，\x01",
            "来期待各位客人的光临。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我有自信能够为每位顾客\x01",
            "提供满意的饭菜和服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52DE")

    TalkEnd(0xF)
    Return()

    # Function_14_4807 end

    def Function_15_52E2(): pass

    label("Function_15_52E2")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5341")

    ChrTalk(
        0xFE,
        (
            "终于把要采购的\x01",
            "食物材料都买齐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这下就可以试做\x01",
            "考虑了很久的新菜式了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5759")

    label("loc_5341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_53B2")

    ChrTalk(
        0xFE,
        "格露娜那家伙很有前途……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定会在她身上发现\x01",
            "与我不同的可能性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "她给我的就是这种感觉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5759")

    label("loc_53B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_547F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_543B")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚才我好像听到主管的尖叫声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "新的工作人员刚来的时候，\x01",
            "我经常听到那个声音。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547C")

    label("loc_543B")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚才我好像听到主管的尖叫声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()

    label("loc_547C")

    Jump("loc_5759")

    label("loc_547F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5535")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "之前的店主\x01",
            "根本就听不进我的意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，现在的老板\x01",
            "却能热心地听取我的建议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的要感谢老板……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老板和我素昧平生，\x01",
            "但是却让我做上餐厅的主厨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5574")

    label("loc_5535")


    ChrTalk(
        0xFE,
        (
            "老板能够那么热心地\x01",
            "听取我的建议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真的很感谢她……\x02",
    )

    CloseMessageWindow()

    label("loc_5574")

    Jump("loc_5759")

    label("loc_5577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_55CA")

    ChrTalk(
        0xFE,
        "烹饪是一种文化艺术。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此独创性是必须的，\x01",
            "而且绝对不允许妥协。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5759")

    label("loc_55CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5608")

    ChrTalk(
        0xFE,
        "……你们享受到料理的乐趣了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "欢迎再来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5759")

    label("loc_5608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_5759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56FF")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "……作为一个厨师，\x01",
            "在自己金盆洗手之前\x01",
            "应该每天都在追求新的味道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "绝对不能自我满足。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有这样的心境，\x01",
            "就没有资格当厨师长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F总、总觉得他是个\x01",
            "有一股恐怖压迫感的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，因为是专业人士嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5759")

    label("loc_56FF")


    ChrTalk(
        0xFE,
        (
            "作为一个厨师，\x01",
            "在自己金盆洗手之前\x01",
            "应该每天都在追求新的味道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "绝对不能自我满足。\x02",
    )

    CloseMessageWindow()

    label("loc_5759")

    TalkEnd(0x10)
    Return()

    # Function_15_52E2 end

    def Function_16_575D(): pass

    label("Function_16_575D")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_57AD")

    ChrTalk(
        0xFE,
        "今天真是有劳了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请你们有空也到本店\x01",
            "来享受料理的乐趣哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D59")

    label("loc_57AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_582C")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "听我说听我说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "厨师长吩咐我\x01",
            "让我来做今天的汤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我每晚都在练习做汤，\x01",
            "这份辛苦终于有回报啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5851")

    label("loc_582C")


    ChrTalk(
        0xFE,
        (
            "厨师长吩咐我\x01",
            "让我来做今天的汤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5851")

    Jump("loc_5D59")

    label("loc_5854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58EF")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "前几天，\x01",
            "厨师长让我做了一锅汤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这可是自从我来到这里以来的第一次。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我不停地不停地重做，\x01",
            "但是直到深夜他仍然陪着我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_590E")

    label("loc_58EF")


    ChrTalk(
        0xFE,
        (
            "好！\x01",
            "我要更加更加地努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590E")

    Jump("loc_5D59")

    label("loc_5911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_5A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A0F")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "秘藏的『格兰·夏利拿』\x01",
            "就这样被别人白喝了，\x01",
            "老板竟然不把这当回事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明年纪和我差不多，\x01",
            "为什么能够如此心胸开阔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "相对而言，\x01",
            "主管就会面色苍白大发雷霆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过那也是理所当然的。\x01",
            "相对来说主管的境地还是比较可怜呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A8C")

    label("loc_5A0F")


    ChrTalk(
        0xFE,
        (
            "秘藏的『格兰·夏利拿』\x01",
            "就这样被别人白喝了，\x01",
            "老板竟然不把这当回事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明年纪和我差不多，\x01",
            "为什么能够如此心胸开阔呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A8C")

    Jump("loc_5D59")

    label("loc_5A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AB3")
    Call(1, 0)
    Jump("loc_5D59")

    label("loc_5AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2B")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "我本来是在\x01",
            "卢安的酒店当厨师的，\x01",
            "受老板的邀请来到这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是因为她\x01",
            "特别喜欢我做的点心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B64")

    label("loc_5B2B")


    ChrTalk(
        0xFE,
        (
            "虽然现在我还只是见习厨师，\x01",
            "不过一定要坚持努力下去！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B64")

    Jump("loc_5D59")

    label("loc_5B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_5C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE9")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        "厨师长是一位非常严格的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，他不愧为\x01",
            "利贝尔首屈一指的高级厨师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "味感和技术都是超一流的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C2C")

    label("loc_5BE9")


    ChrTalk(
        0xFE,
        (
            "厨师长是一位非常严格的人。\x01",
            "但是，他的味感和技术都是超一流的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C2C")

    Jump("loc_5D59")

    label("loc_5C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5CB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9A")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "土豆削好了，\x01",
            "接下来是洋葱……吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了不拖厨师长的后腿，\x01",
            "我得加快速度才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CAE")

    label("loc_5C9A")


    ChrTalk(
        0xFE,
        "忙死了忙死了。\x02",
    )

    CloseMessageWindow()

    label("loc_5CAE")

    Jump("loc_5D59")

    label("loc_5CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_5D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D28")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "厨师长对于味道的执念\x01",
            "还真不是一般的厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前为了考虑新的汤点，\x01",
            "曾经住在这个厨房里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D59")

    label("loc_5D28")


    ChrTalk(
        0xFE,
        (
            "厨师长对于味道的执念\x01",
            "还真不是一般的厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D59")

    TalkEnd(0x11)
    Return()

    # Function_16_575D end

    def Function_17_5D5D(): pass

    label("Function_17_5D5D")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5E1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DCD")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "以前订的红酒\x01",
            "终于空运过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "红酒的存货\x01",
            "已经快见底了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是千钧一发啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E19")

    label("loc_5DCD")


    ChrTalk(
        0xFE,
        (
            "以前订的红酒\x01",
            "终于空运过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "库存已经快用完了，\x01",
            "真是千钧一发啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E19")

    Jump("loc_6272")

    label("loc_5E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5E95")

    ChrTalk(
        0xFE,
        (
            "飞艇重新开始起航了，\x01",
            "终于能够订购到酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明订购单上有的，\x01",
            "但是却偏偏这时候断货了，\x01",
            "我好不甘心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6272")

    label("loc_5E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_5F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F44")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "麻烦了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我休息的时候，\x01",
            "那瓶『格兰·夏利拿』\x01",
            "竟然被人白喝掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然老板没有怪我，\x01",
            "还对我面带微笑，\x01",
            "但我还是觉得自己要负一定的责任。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F94")

    label("loc_5F44")


    ChrTalk(
        0xFE,
        "麻烦了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我休息的时候，\x01",
            "那瓶『格兰·夏利拿』\x01",
            "竟然被人白喝掉了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F94")

    Jump("loc_6272")

    label("loc_5F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_60F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6091")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "我本来是帝国的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有一天，\x01",
            "这里的老板到我工作的饭店用餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时她特别喜欢\x01",
            "我所调制的酒。\x01",
            "后来就给我写信了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "问我愿不愿意到她的店工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一开始我只是想来利贝尔\x01",
            "看看这家店的情况，\x01",
            "没想到就一直工作到了现在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60ED")

    label("loc_6091")


    ChrTalk(
        0xFE,
        (
            "老板邀请我来工作的时候\x01",
            "我还苦恼了一阵子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "她确实有一种不可思议的魅力呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60ED")

    Jump("loc_6272")

    label("loc_60F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_61DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6199")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "糟糕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为定期船停航了，\x01",
            "就不能向外面订购酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过现在酒库里还有些存货，\x01",
            "我想应该没什么问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么时候才能恢复原状呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_61D8")

    label("loc_6199")


    ChrTalk(
        0xFE,
        "糟糕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为定期船停航了，\x01",
            "就不能向外面订购酒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D8")

    Jump("loc_6272")

    label("loc_61DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6226")

    ChrTalk(
        0xFE,
        "谢谢光临本店用餐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们随时期待着\x01",
            "各位客人的再次光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6272")

    label("loc_6226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6272")

    ChrTalk(
        0xFE,
        "我是这家店的斟酒服务生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "凡是和酒有关的事情\x01",
            "都可以来问我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6272")

    TalkEnd(0x12)
    Return()

    # Function_17_5D5D end

    def Function_18_6276(): pass

    label("Function_18_6276")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D7")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您要就餐的话，\x01",
            "我会带您去一个环境比较好的位子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6310")

    label("loc_62D7")


    ChrTalk(
        0xFE,
        (
            "如果您要就餐的话，\x01",
            "我会带您去一个环境比较好的位子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6310")

    Jump("loc_669A")

    label("loc_6313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6356")

    ChrTalk(
        0xFE,
        "厨师长拜托我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一会儿要去\x01",
            "柏斯超市买点东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_669A")

    label("loc_6356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_642B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63E2")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "前不久，\x01",
            "有一瓶非常珍贵的酒被客人喝掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可是听到了主管\x01",
            "久违了的尖叫声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就像是\x01",
            "女人的声音一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6428")

    label("loc_63E2")


    ChrTalk(
        0xFE,
        (
            "我可是听到了主管\x01",
            "久违了的尖叫声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就像是\x01",
            "女人的声音一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6428")

    Jump("loc_669A")

    label("loc_642B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_653E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64FC")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我本来在蔡斯的\x01",
            "一家饭店当服务员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在的老板去蔡斯\x01",
            "谈生意的时候看中了我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她提出的工资很不错，\x01",
            "而且分配的工作也很轻松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且对我提出的要求\x01",
            "也毫不犹豫地就答应了下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_653B")

    label("loc_64FC")


    ChrTalk(
        0xFE,
        (
            "老板真是一个\x01",
            "当机立断的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "和主管的性格正好相反。\x02",
    )

    CloseMessageWindow()

    label("loc_653B")

    Jump("loc_669A")

    label("loc_653E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_660E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D8")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "这家店自从被\x01",
            "现在的老板买下之后，\x01",
            "人气就越来越旺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "几乎所有的工作人员\x01",
            "都是老板自己带过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过我是自己找过来的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_660B")

    label("loc_65D8")


    ChrTalk(
        0xFE,
        (
            "这里几乎所有的工作人员\x01",
            "都是老板自己带过来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_660B")

    Jump("loc_669A")

    label("loc_660E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_664A")

    ChrTalk(
        0xFE,
        "啊，刚才的客人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有什么东西忘拿了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_669A")

    label("loc_664A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_669A")

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您要就餐的话，\x01",
            "我会带您去一个环境比较好的位子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_669A")

    TalkEnd(0x13)
    Return()

    # Function_18_6276 end

    def Function_19_669E(): pass

    label("Function_19_669E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6700")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        "定期船恢复开航了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们在柏斯\x01",
            "也玩得差不多了，\x01",
            "该回王都了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6730")

    label("loc_6700")


    ChrTalk(
        0xFE,
        (
            "我们在柏斯\x01",
            "也玩得差不多了，\x01",
            "该回王都了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6730")

    Jump("loc_6C65")

    label("loc_6733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E7")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "我们从王都到这里来的时候，\x01",
            "是坐船从瓦雷利亚湖上渡过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "湖的旁边\x01",
            "有一家非常不错的旅馆呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也去那里住了一晚。\x01",
            "嗯，旅馆的名字叫什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_684F")

    label("loc_67E7")


    ChrTalk(
        0xFE,
        (
            "我们从王都到这里来的时候，\x01",
            "是坐船从瓦雷利亚湖上渡过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "湖的旁边\x01",
            "有一家非常不错的旅馆呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684F")

    Jump("loc_6C65")

    label("loc_6852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_693D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68F8")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "我对军队的人\x01",
            "没有什么好感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不识风趣，又盛气凌人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么不能\x01",
            "放下这个架子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然我也不是说\x01",
            "所有的军人都是这个样子的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_693A")

    label("loc_68F8")


    ChrTalk(
        0xFE,
        (
            "我对军队的人\x01",
            "没有什么好感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么不能\x01",
            "放下这个架子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_693A")

    Jump("loc_6C65")

    label("loc_693D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C8")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "在这个城市的西北方\x01",
            "有一个盛产美味水果的村子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是因为在山里，\x01",
            "所以靠我们的脚力是去不了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真遗憾……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A0D")

    label("loc_69C8")


    ChrTalk(
        0xFE,
        (
            "对了，买水果的话，\x01",
            "超市里不就有很多吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "待会儿过去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6A0D")

    Jump("loc_6C65")

    label("loc_6A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_6B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AEC")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "定期船的运营停止了，\x01",
            "是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过就这样\x01",
            "在这个城市里多呆两天也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为嘛，\x01",
            "我自己都不知道该怎么做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想慢慢品尝美食，\x01",
            "尽情到超市购物，\x01",
            "敞开胸怀在这片土地上惬意地享受生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B3B")

    label("loc_6AEC")


    ChrTalk(
        0xFE,
        "听说定期船停航了，是真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过就这样\x01",
            "在这个城市里多呆两天也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B3B")

    Jump("loc_6C65")

    label("loc_6B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB4")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "这家餐厅在格兰赛尔\x01",
            "口碑也相当不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我就是为了\x01",
            "品尝这里的饭菜，\x01",
            "才从王都专门过来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BF7")

    label("loc_6BB4")


    ChrTalk(
        0xFE,
        "真是名不虚传啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是第一次吃到\x01",
            "如此美味的利贝尔料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF7")

    Jump("loc_6C65")

    label("loc_6BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6C65")

    ChrTalk(
        0xFE,
        (
            "我们是从王都\x01",
            "到这里来购物和品尝美食的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然王都也很热闹，\x01",
            "但是这个城市也丝毫不比王都差。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C65")

    TalkEnd(0x14)
    Return()

    # Function_19_669E end

    def Function_20_6C69(): pass

    label("Function_20_6C69")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6D81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D1A")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "下一次，\x01",
            "我想去埃雷波尼亚帝国旅行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既是个有悠久历史的国家，\x01",
            "值得去看的地方也不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然一想到１０年前的事情，\x01",
            "也会让人觉得有点恐怖……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D7E")

    label("loc_6D1A")


    ChrTalk(
        0xFE,
        (
            "下一次，\x01",
            "我想去埃雷波尼亚帝国旅行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然一想到１０年前的事情，\x01",
            "也会让人觉得有点恐怖……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D7E")

    Jump("loc_7190")

    label("loc_6D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6DF7")

    ChrTalk(
        0xFE,
        (
            "没想到因为定期船失踪事件，\x01",
            "我要长期滞留在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，正好趁此机会，\x01",
            "可以放慢脚步，慢慢游玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7190")

    label("loc_6DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E72")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "玛丽安所说的\x01",
            "我也非常赞同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "同样是军队，还是女王陛下的亲卫队\x01",
            "礼仪更加端庄，举止更加优雅……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB7")

    label("loc_6E72")


    ChrTalk(
        0xFE,
        (
            "同样是军队，还是女王陛下的亲卫队\x01",
            "礼仪更加端庄，举止更加优雅……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EB7")

    Jump("loc_7190")

    label("loc_6EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5C")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "玛丽安对美味的食物\x01",
            "完全没有抵抗力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要听说有好吃的，\x01",
            "就立刻会说\x01",
            "『我们去尝尝吧』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为这样，\x01",
            "我也没少跟着她饱口福。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FC2")

    label("loc_6F5C")


    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "玛丽安对美味的食物\x01",
            "完全没有抵抗力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要听说有好吃的，\x01",
            "就立刻会说\x01",
            "『我们去尝尝吧』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FC2")

    Jump("loc_7190")

    label("loc_6FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_70A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_704A")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "这家店不仅是饭菜，\x01",
            "工作人员的服务态度也非常好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你看看就知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "员工把老板的精神\x01",
            "都传达到位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A4")

    label("loc_704A")


    ChrTalk(
        0xFE,
        (
            "这家店不仅是饭菜，\x01",
            "工作人员的服务态度也非常好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "员工把老板的精神\x01",
            "都传达到位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A4")

    Jump("loc_7190")

    label("loc_70A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7101")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "真是太好吃了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "格兰赛尔有没有\x01",
            "能做出这样美味饭菜的店呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7132")

    label("loc_7101")


    ChrTalk(
        0xFE,
        (
            "格兰赛尔有没有\x01",
            "能做出这样美味饭菜的店呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7132")

    Jump("loc_7190")

    label("loc_7135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7190")

    ChrTalk(
        0xFE,
        (
            "我和玛丽安\x01",
            "经常外出到各地去旅行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次，要我选择的话，\x01",
            "我打算去超市购物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7190")

    TalkEnd(0x15)
    Return()

    # Function_20_6C69 end

    def Function_21_7194(): pass

    label("Function_21_7194")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71E5")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "我最喜欢的红酒\x01",
            "终于进货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我都等得不耐烦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7206")

    label("loc_71E5")


    ChrTalk(
        0xFE,
        (
            "我最喜欢的红酒\x01",
            "终于进货了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7206")

    Jump("loc_7808")

    label("loc_7209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_72E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_729A")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "只要去柏斯超市，\x01",
            "就会想起以前的种种画面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在柏斯商人的血统\x01",
            "仍然流淌在年轻人的身体里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我还是觉得很高兴的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_72E1")

    label("loc_729A")


    ChrTalk(
        0xFE,
        (
            "现在柏斯商人的血统\x01",
            "仍然流淌在年轻人的身体里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我觉得很高兴。\x02",
    )

    CloseMessageWindow()

    label("loc_72E1")

    Jump("loc_7808")

    label("loc_72E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_748F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7412")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "百日战役时这座城市也成为了废墟，\x01",
            "但它却是五大都市中\x01",
            "最早复兴起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "会这样也是有原因的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "商人们团结一心，集聚资金，\x01",
            "使这个城市重新兴盛起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯商人虽然崇尚自由，\x01",
            "但是必要的时刻他们仍会团结一致……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我作为这座城市的商人，\x01",
            "觉得能够生活在这里是一种骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_748C")

    label("loc_7412")


    ChrTalk(
        0xFE,
        (
            "柏斯商人虽然崇尚自由，\x01",
            "但是必要的时刻他们仍会团结一致……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我作为这座城市的商人，\x01",
            "觉得能够生活在这里是一种骄傲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_748C")

    Jump("loc_7808")

    label("loc_748F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_75EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7583")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "超市变得正规和气派起来\x01",
            "还是小姐的父亲当市长的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他推行了各种各样\x01",
            "划时代的商业振兴政策。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且如今这些都被小姐\x01",
            "继承和发展了下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一开始觉得她太年轻，\x01",
            "还有点看不起她。\x01",
            "不过她的商业手段真是相当的厉害。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75E9")

    label("loc_7583")


    ChrTalk(
        0xFE,
        (
            "超市变得正规和气派起来\x01",
            "还是小姐的父亲当市长的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他推行了各种各样\x01",
            "划时代的商业振兴政策。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75E9")

    Jump("loc_7808")

    label("loc_75EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_7757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E8")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "在超市还没有建立起来的时候，\x01",
            "那里有一个由空地上的小摊\x01",
            "所组成的大型青空市场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那时商人的朝气和气派\x01",
            "比现在还要高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在有权势的商人如市长家，\x01",
            "以及贸易商人特里诺家、博尔德家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们都是从那个青空市场\x01",
            "开始起家的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7754")

    label("loc_76E8")


    ChrTalk(
        0xFE,
        (
            "现在有权势的商人如市长家，\x01",
            "以及贸易商人特里诺家、博尔德家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们都是从那个青空市场\x01",
            "开始起家的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7754")

    Jump("loc_7808")

    label("loc_7757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_77A2")

    ChrTalk(
        0xFE,
        (
            "我年轻的时候\x01",
            "也在柏斯超市做生意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在已经退休归隐啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7808")

    label("loc_77A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77F6")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        "呼～呼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这烤鸭配上香菜，\x01",
            "简直是太勾引人食欲了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7808")

    label("loc_77F6")


    ChrTalk(
        0xFE,
        "呼～呼～……\x02",
    )

    CloseMessageWindow()

    label("loc_7808")

    TalkEnd(0x16)
    Return()

    # Function_21_7194 end

    def Function_22_780C(): pass

    label("Function_22_780C")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_78F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78A7")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "啊呀，我觉得今天的汤\x01",
            "和以前的味道不太一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有点粗糙，\x01",
            "但是材料的风味都被活用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "店里是不是\x01",
            "来了新的厨师？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78ED")

    label("loc_78A7")


    ChrTalk(
        0xFE,
        (
            "今天的汤\x01",
            "和以前的味道不太一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "店里是不是\x01",
            "来了新的厨师？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78ED")

    Jump("loc_7C96")

    label("loc_78F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_7946")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "我在这里吃饭的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总觉得桌子对面那个人\x01",
            "在对着我微笑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C96")

    label("loc_7946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_799F")

    ChrTalk(
        0xFE,
        (
            "只要一看到街上有穿着军服的人，\x01",
            "我就会回忆起过去的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好痛苦啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C96")

    label("loc_799F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7A0D")

    ChrTalk(
        0xFE,
        (
            "战争的时候，不只是这个城市，\x01",
            "连拉文努村也受害了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和我怀有同样心情的人\x01",
            "现在也会有很多吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C96")

    label("loc_7A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_7B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ACC")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "现在连帝国的人\x01",
            "都可以来柏斯超市购物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对我来说，这还真是让人百感交集的时代啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那场战争中我最重要的亲人被夺去了性命，\x01",
            "不管时代怎么变，历史是不会变的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B2A")

    label("loc_7ACC")


    ChrTalk(
        0xFE,
        (
            "现在这个年代，\x01",
            "连帝国的人都可以\x01",
            "来柏斯超市购物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过对我来说，还真是百感交集啊。\x02",
    )

    CloseMessageWindow()

    label("loc_7B2A")

    Jump("loc_7C96")

    label("loc_7B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7B81")

    ChrTalk(
        0xFE,
        (
            "以前和老伴\x01",
            "经常来这家饭店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……是啊，\x01",
            "那已经是十年前的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C96")

    label("loc_7B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C3A")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "嗯，这里的饭菜\x01",
            "还是和以前一样无可挑剔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我听说几年前\x01",
            "这里的老板换了，\x01",
            "但是我还是很放心地来这里吃饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我甚至觉得换了老板之后，\x01",
            "饭菜的味道更好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C96")

    label("loc_7C3A")


    ChrTalk(
        0xFE,
        (
            "嗯，这里的饭菜\x01",
            "还是和以前一样无可挑剔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里换了老板之后，\x01",
            "饭菜的味道更加美味了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C96")

    TalkEnd(0x17)
    Return()

    # Function_22_780C end

    def Function_23_7C9A(): pass

    label("Function_23_7C9A")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7CED")

    ChrTalk(
        0xFE,
        (
            "哈啊……\x01",
            "谈判又失败了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我好像真的不适合\x01",
            "和别人谈生意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_7D26")

    ChrTalk(
        0xFE,
        (
            "也、也没有办法啊。\x01",
            "那么您看这个价格如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7D6B")

    ChrTalk(
        0xFE,
        (
            "哈啊……\x01",
            "人际关系真的好难协调啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真没用啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7DDA")

    ChrTalk(
        0xFE,
        (
            "不不不，\x01",
            "不管怎么样\x01",
            "请接受这个价格吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的上司\x01",
            "是这么要求我的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请您一定要帮帮忙！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_7E3A")

    ChrTalk(
        0xFE,
        (
            "不不不，\x01",
            "我非常明白你们的感受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，作为我这一方，\x01",
            "也要秉持商会的方针……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7E77")

    ChrTalk(
        0xFE,
        (
            "不行，这已经突破底线了。\x01",
            "这个价格我不能让步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7EE2")

    ChrTalk(
        0xFE,
        (
            "由于军队的监控以及飞艇的停航，\x01",
            "造成了范围很广的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不赶快重开\x01",
            "这次交易谈判的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EE2")

    TalkEnd(0x18)
    Return()

    # Function_23_7C9A end

    def Function_24_7EE6(): pass

    label("Function_24_7EE6")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_800F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FBA")
    OP_A2(0x12)

    ChrTalk(
        0xFE,
        (
            "虽然本来想跟您谈一下\x01",
            "关于街道封锁时的流通问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过不知道什么时候\x01",
            "所有的封锁都已经被解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "商人要敏锐地把握商机……\x01",
            "这是我的座右铭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "一不小心就沉迷于谈判了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_800C")

    label("loc_7FBA")


    ChrTalk(
        0xFE,
        (
            "商人要敏锐地把握商机……\x01",
            "这是我的座右铭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "一不小心就沉迷于谈判了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_800C")

    Jump("loc_8263")

    label("loc_800F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_803F")

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "虽然没有什么不好……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8263")

    label("loc_803F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_80AB")

    ChrTalk(
        0xFE,
        (
            "一味地逼迫对方，\x01",
            "是不会在谈判中取得好结果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据情况的不同\x01",
            "来随机应变也是十分重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8263")

    label("loc_80AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8122")

    ChrTalk(
        0xFE,
        (
            "不不不，\x01",
            "照你这么说的话，\x01",
            "我这边的损失也可能扩大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这么说，\x01",
            "不过采取更灵活的应对方式也很重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8263")

    label("loc_8122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_818B")

    ChrTalk(
        0xFE,
        (
            "不不不，\x01",
            "我们更重视\x01",
            "长期的数值变化……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "应该把眼光放长远，\x01",
            "考虑到飞艇复航之后的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8263")

    label("loc_818B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_81F1")

    ChrTalk(
        0xFE,
        (
            "不行不行，这个数字\x01",
            "我们商会是无论如何也不接受的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对你来说，\x01",
            "这也不是闹着玩的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8263")

    label("loc_81F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8263")

    ChrTalk(
        0xFE,
        (
            "柏斯能出售的商品\x01",
            "变得越来越少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "得想个办法才行，\x01",
            "就算不能回避这种状况，\x01",
            "至少能够做到缓和一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8263")

    TalkEnd(0x19)
    Return()

    # Function_24_7EE6 end

    def Function_25_8267(): pass

    label("Function_25_8267")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_82ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C3")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "因为太紧张了，\x01",
            "都没有品尝出什么味道来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "真是可惜啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_82C3")


    ChrTalk(
        0xFE,
        (
            "下次来的时候\x01",
            "一定要仔细品味一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82EA")

    Jump("loc_8416")

    label("loc_82ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_83A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8362")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "我、我穿了最漂亮的衣服过来，\x01",
            "但会不会感觉很奇怪？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一定要小心\x01",
            "不要让餐具掉在地上……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_839F")

    label("loc_8362")


    ChrTalk(
        0xFE,
        (
            "哈啊，我这种在低下阶层的人\x01",
            "穿这种服装还真是有点不搭配。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839F")

    Jump("loc_8416")

    label("loc_83A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_83F1")

    ChrTalk(
        0xFE,
        (
            "其、其实我是第一次\x01",
            "来这种高档的地方吃饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是紧张死了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8416")

    label("loc_83F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8416")

    ChrTalk(
        0xFE,
        "那、那么我们点些什么呢。\x02",
    )

    CloseMessageWindow()

    label("loc_8416")

    TalkEnd(0x1A)
    Return()

    # Function_25_8267 end

    def Function_26_841A(): pass

    label("Function_26_841A")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84B5")
    OP_A2(0x14)

    ChrTalk(
        0xFE,
        "啊～真是太好吃了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是被称为\x01",
            "利贝尔首屈一指的饭店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "存钱来这里吃饭\x01",
            "真是太值了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "偶尔这样奢侈一次\x01",
            "也不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84FF")

    label("loc_84B5")


    ChrTalk(
        0xFE,
        (
            "不愧是被称为\x01",
            "利贝尔首屈一指的饭店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "存钱来这里吃饭\x01",
            "真是太值了㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84FF")

    Jump("loc_8602")

    label("loc_8502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8568")

    ChrTalk(
        0xFE,
        (
            "我们在很久以前，\x01",
            "就想来这里吃一顿饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "两个人拼命努力地打工赚钱\x01",
            "才能来到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8602")

    label("loc_8568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_85A3")

    ChrTalk(
        0xFE,
        (
            "我说，别低着头弓着腰啦。\x01",
            "应该更放松一点嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8602")

    label("loc_85A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8602")

    ChrTalk(
        0xFE,
        (
            "啊～果然如传闻一样，\x01",
            "是一家很豪华的酒店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前我都只敢\x01",
            "在外面偷偷往里面看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8602")

    TalkEnd(0x1B)
    Return()

    # Function_26_841A end

    def Function_27_8606(): pass

    label("Function_27_8606")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-35680, 1500, 4059, 0)
    OP_67(0, 7500, -10000, 0)
    ClearChrFlags(0x8, 0x80)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x134, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x101, -53630, 1700, 4200, 270)
    SetChrPos(0x102, -54880, 1700, 2840, 0)
    SetChrPos(0x103, -54970, 1700, 5580, 180)
    SetChrPos(0x8, -56300, 1700, 4200, 90)
    SetChrPos(0x134, -56990, 1500, 5470, 135)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 21)
    SetChrChipByIndex(0x103, 22)
    FadeToBright(2000, 0)
    OP_6D(-55280, 1700, 4240, 6000)

    ChrTalk(
        0x101,
        (
            "#004F好、好豪华的饭店啊……\x01",
            "就在这种地方商量吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F就在这里慢慢谈吧。\x01",
            "这里菜色风味独特，味道也相当不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F可是，虽然柏斯市长\x01",
            "是位女性的事我早有耳闻……\x02\x03",
            "但没想到竟然如此年轻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F刚见面的时候，\x01",
            "我觉得最多只和我相差四五岁的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#611F实际上也不过是初出茅庐的年轻人而已。\x02\x03",
            "我只是一并继承了已亡故的父亲\x01",
            "作为柏斯市长和柏斯超市业主的\x01",
            "政治及商业地位而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F怎么说呢……\x01",
            "真是坦率的自我评价啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F毕竟是商人的女儿嘛，\x01",
            "不擅长装腔作势那一套。\x02\x03",
            "那么我们现在再确认一下\x01",
            "委托的内容吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#612F不用说，我委托的正是\x01",
            "调查和解决失踪定期船的事件。\x02\x03",
            "我认为像这次这样的事件，\x01",
            "游击士协会的各位会比起军方\x01",
            "更能找出事件的真相。\x02\x03",
            "因为不是要进行战争，\x01",
            "而是要揭开事件的迷雾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F啊，真荣幸。\x01",
            "市长您太看得起我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#611F所谓商人就是要有敏锐的眼光嘛。\x02\x03",
            "#615F实际上，失踪定期船的乘客中\x01",
            "有一位在柏斯很有影响力的商人。\x02\x03",
            "如果持续目前的状况，\x01",
            "王国军在柏斯上空继续实行飞行管制的话，\x01",
            "这里的商业交易就没办法进行下去了。\x02\x03",
            "在女王诞辰庆典之前，\x01",
            "难得市场的景气好了起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F原来如此。\x01",
            "是出于经济的考量吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#612F可以这样说吧，\x01",
            "不能只让军队方面负责这件事。\x02\x03",
            "怎么样，愿意接受我的委托吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F虽然我们这边也有\x01",
            "要接受这个委托的理由……\x02\x03",
            "但是关于这个事件，\x01",
            "军方已经把游击士协会排斥在外，\x01",
            "所以我们现在也无法展开调查工作。\x02\x03",
            "#020F您能不能以市长的立场\x01",
            "给我们的工作一些支持呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#612F是摩尔根将军吧……\x02\x03",
            "那位将军，\x01",
            "从很早以前就非常讨厌游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎？\x01",
            "市长姐姐也认识那个摩尔根将军？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F他是我去世父亲的朋友。\x01",
            "所以曾经见过几次面。\x02\x03",
            "因此……\x01",
            "说不定我能帮你们一些忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F您的意思是……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(500)

    ChrTalk(
        0x8,
        "#610F莉拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#620F是，小姐。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x134, 0xFFFF24D2, 0x5DC, 0x1374, 0x7D0, 0x0)
    TurnDirection(0x134, 0x8, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "莉拉从怀中拿出钢笔和信纸，\x01",
            "递给了梅贝尔市长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_8C(0x134, 315, 400)
    OP_8F(0x134, 0xFFFF2162, 0x5DC, 0x155E, 0x7D0, 0x0)
    OP_8C(0x134, 135, 400)

    ChrTalk(
        0x8,
        (
            "#612F……………………………\x02\x03",
            "……………………………\x01",
            "……………………………\x02\x03",
            "#615F……这样应该可以了。\x02\x03",
            "#610F那么，你们拿着吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x32D, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "梅贝尔市长的信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#000F这封信，是做什么的呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F是给摩尔根将军的委托信。\x02\x03",
            "我以柏斯地区的负责人身份，\x01",
            "向摩尔根将军申请\x01",
            "获得这次事件的相关情报。\x02\x03",
            "我想，从某种程度来说，\x01",
            "你们应该可以获得军方掌握的情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F原来是这样啊……\x02\x03",
            "可是，那个讨厌游击士的将军\x01",
            "会不会见我们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F当然，各位只要隐瞒一下\x01",
            "游击士的身份就没问题了。\x02\x03",
            "你们仅以市长使者的名义\x01",
            "去拜见他就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F唔，感觉有点不爽。\x01",
            "好像我们是骗子似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们这么做可不是骗人啊。\x01",
            "只是没把所有事都和盘托出而已。\x02\x03",
            "因为我们必须争分夺秒，\x01",
            "这次就暂时委屈一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯～说的也是呢。\x02\x03",
            "#000F话说回来，\x01",
            "到哪里能找到摩尔根将军呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#610F柏斯北面，帝国方向的边境\x01",
            "有座被称为『哈肯大门』的堡垒。\x02\x03",
            "摩尔根将军就在那里。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x33, 0xFF)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_8606 end

    def Function_28_915A(): pass

    label("Function_28_915A")

    Sleep(500)
    SetChrSubChip(0x102, 0)
    Sleep(200)
    SetChrSubChip(0x103, 0)
    Sleep(200)
    SetChrSubChip(0x101, 1)
    Sleep(200)
    SetChrSubChip(0x102, 1)
    Sleep(200)
    SetChrSubChip(0x103, 2)
    Return()

    # Function_28_915A end

    SaveToFile()

Try(main)
