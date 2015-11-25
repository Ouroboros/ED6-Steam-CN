from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1122   ._SN',
        MapName             = 'Bose',
        Location            = 'T1122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1122   ._SN',
            'ED6_DT01/T1122_1 ._SN',
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
        '帕克',                                 # 9
        '德拉多',                               # 10
        '普蕾沙',                               # 11
        '波波',                                 # 12
        '思潘斯老人',                           # 13
        '卡特丽亚',                             # 14
        '泊尔',                                 # 15
        '米蕾婆婆',                             # 16
        '丽露露',                               # 17
        '卡洛',                                 # 18
        '里布罗',                               # 19
        '刚茨',                                 # 20
        '格蕾娅',                               # 21
        '玛依森老人',                           # 22
        '艾米',                                 # 23
        '西加罗',                               # 24
        '艾德尔',                               # 25
        '马尔科',                               # 26
        '西蒙',                                 # 27
        '年轻女性',                             # 28
        '米拉诺',                               # 29
        '莉拉',                                 # 30
        '萨拉',                                 # 31
        '朵洛希',                               # 32
        '芬尼尔',                               # 33
        '奥利维尔',                             # 34
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH02490 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH01010 ._CH',             # 07
        'ED6_DT07/CH01070 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT07/CH01270 ._CH',             # 0B
        'ED6_DT07/CH01150 ._CH',             # 0C
        'ED6_DT07/CH01200 ._CH',             # 0D
        'ED6_DT07/CH01050 ._CH',             # 0E
        'ED6_DT07/CH01040 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH02360 ._CH',             # 13
        'ED6_DT07/CH01140 ._CH',             # 14
        'ED6_DT07/CH01230 ._CH',             # 15
        'ED6_DT07/CH01350 ._CH',             # 16
        'ED6_DT06/CH20063 ._CH',             # 17
        'ED6_DT07/CH02370 ._CH',             # 18
        'ED6_DT07/CH01040 ._CH',             # 19
        'ED6_DT06/CH20064 ._CH',             # 1A
        'ED6_DT07/CH00030 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH02490P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH01010P._CP',             # 07
        'ED6_DT07/CH01070P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT07/CH01270P._CP',             # 0B
        'ED6_DT07/CH01150P._CP',             # 0C
        'ED6_DT07/CH01200P._CP',             # 0D
        'ED6_DT07/CH01050P._CP',             # 0E
        'ED6_DT07/CH01040P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH02360P._CP',             # 13
        'ED6_DT07/CH01140P._CP',             # 14
        'ED6_DT07/CH01230P._CP',             # 15
        'ED6_DT07/CH01350P._CP',             # 16
        'ED6_DT06/CH20063P._CP',             # 17
        'ED6_DT07/CH02370P._CP',             # 18
        'ED6_DT07/CH01040P._CP',             # 19
        'ED6_DT06/CH20064P._CP',             # 1A
        'ED6_DT07/CH00030P._CP',             # 1B
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = -12700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 8500,
        Z                   = 0,
        Y                   = -8300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 4100,
        Z                   = 0,
        Y                   = 13650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = 13600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 9300,
        Z                   = 0,
        Y                   = 6900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -13400,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -16700,
        Z                   = 0,
        Y                   = -8600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -13600,
        Z                   = 0,
        Y                   = 10700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -9150,
        Z                   = -1000,
        Y                   = 340,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 0,
        Y                   = -5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -11100,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -18120,
        Z                   = 0,
        Y                   = 5130,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = 12500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = -1000,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -7700,
        Z                   = 0,
        Y                   = 14700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -15200,
        Z                   = 0,
        Y                   = 15700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 6610,
        Z                   = 0,
        Y                   = 2340,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 700,
        Z                   = -1000,
        Y                   = 4900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 350,
        Z                   = -1000,
        Y                   = 480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 6400,
        Z                   = 0,
        Y                   = 7700,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 12300,
        Z                   = 0,
        Y                   = -8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 7180,
        Z                   = 0,
        Y                   = 540,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -1430,
        Z                   = 0,
        Y                   = 9040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = -12050,
        Z                   = 0,
        Y                   = -2230,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )


    DeclActor(
        TriggerX            = 7540,
        TriggerZ            = 0,
        TriggerY            = 6450,
        TriggerRange        = 400,
        ActorX              = 9300,
        ActorZ              = 1500,
        ActorY              = 6900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6830,
        TriggerZ            = 0,
        TriggerY            = -8820,
        TriggerRange        = 400,
        ActorX              = 8360,
        ActorZ              = 1500,
        ActorY              = -8430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15120,
        TriggerZ            = 0,
        TriggerY            = -8860,
        TriggerRange        = 400,
        ActorX              = -16700,
        ActorZ              = 1500,
        ActorY              = -8600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_536",          # 00, 0
        "Function_1_7D1",          # 01, 1
        "Function_2_7EE",          # 02, 2
        "Function_3_804",          # 03, 3
        "Function_4_851",          # 04, 4
        "Function_5_8FC",          # 05, 5
        "Function_6_920",          # 06, 6
        "Function_7_944",          # 07, 7
        "Function_8_9B4",          # 08, 8
        "Function_9_B19",          # 09, 9
        "Function_10_B3D",         # 0A, 10
        "Function_11_B42",         # 0B, 11
        "Function_12_1667",        # 0C, 12
        "Function_13_166C",        # 0D, 13
        "Function_14_2049",        # 0E, 14
        "Function_15_28D9",        # 0F, 15
        "Function_16_2ECE",        # 10, 16
        "Function_17_2F4E",        # 11, 17
        "Function_18_311E",        # 12, 18
        "Function_19_3B82",        # 13, 19
        "Function_20_3B87",        # 14, 20
        "Function_21_4897",        # 15, 21
        "Function_22_489C",        # 16, 22
        "Function_23_560D",        # 17, 23
        "Function_24_6286",        # 18, 24
        "Function_25_6902",        # 19, 25
        "Function_26_70F4",        # 1A, 26
        "Function_27_77D6",        # 1B, 27
        "Function_28_7DFA",        # 1C, 28
        "Function_29_85DC",        # 1D, 29
        "Function_30_8CE0",        # 1E, 30
        "Function_31_9363",        # 1F, 31
        "Function_32_969A",        # 20, 32
        "Function_33_9CC8",        # 21, 33
        "Function_34_A0E1",        # 22, 34
        "Function_35_A2CB",        # 23, 35
        "Function_36_A480",        # 24, 36
        "Function_37_A5AB",        # 25, 37
        "Function_38_A737",        # 26, 38
        "Function_39_AAA5",        # 27, 39
        "Function_40_AC8F",        # 28, 40
        "Function_41_ADAA",        # 29, 41
        "Function_42_B8AF",        # 2A, 42
    )


    def Function_0_536(): pass

    label("Function_0_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_580")
    SetChrPos(0x10, 1100, 0, -7600, 0)
    ClearChrFlags(0x12, 0x10)
    SetChrPos(0x13, -14500, 0, 4500, 90)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_7A2")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0x10, 1100, 0, -7600, 0)
    ClearChrFlags(0x12, 0x10)
    SetChrPos(0x13, -14500, 0, 4500, 90)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -19400, 0, 3600, 180)
    Jump("loc_7A2")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_64B")
    SetChrPos(0x12, -12200, 0, 14900, 225)
    SetChrPos(0x16, 5000, 0, 4700, 315)
    SetChrPos(0x13, -11680, 0, -2590, 315)
    SetChrPos(0x17, -7400, -1000, -320, 90)
    SetChrPos(0x18, -7400, 0, 900, 90)
    SetChrPos(0x10, 1100, 0, -7600, 0)
    Jump("loc_7A2")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6CD")
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x10, 1100, 0, -7600, 0)
    SetChrPos(0x16, -11800, 0, 7900, 315)
    SetChrPos(0x12, -12200, 0, 14900, 225)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrPos(0x18, -15400, 0, 8900, 45)
    SetChrPos(0x17, -13100, 0, 5900, 315)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_7A2")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_72F")
    SetChrPos(0x10, 1100, 0, -7600, 0)
    SetChrPos(0x16, 6500, 0, -7100, 90)
    SetChrFlags(0x18, 0x10)
    SetChrPos(0x18, -14500, 0, -6300, 270)
    SetChrPos(0x17, -11700, 0, -7190, 215)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_7A2")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_77D")
    ClearChrFlags(0x12, 0x10)
    SetChrChipByIndex(0x1F, 26)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -11600, 0, -7100, 225)
    SetChrChipByIndex(0x17, 17)
    OP_44(0x17, 0xFF)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    SetChrPos(0x17, -8600, 0, 8600, 0)
    Jump("loc_7A2")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7A2")
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)

    label("loc_7A2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_7BA"),
        (101, "loc_7BA"),
        (102, "loc_7BA"),
        (103, "loc_7BA"),
        (SWITCH_DEFAULT, "loc_7D0"),
    )


    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CD")
    OP_A2(0x30B)
    Event(0, 41)

    label("loc_7CD")

    Jump("loc_7D0")

    label("loc_7D0")

    Return()

    # Function_0_536 end

    def Function_1_7D1(): pass

    label("Function_1_7D1")

    SoundDistance(0x1CB, 0xFFFFEF98, 0xFFFFFC18, 0x276, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_7D1 end

    def Function_2_7EE(): pass

    label("Function_2_7EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_803")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7EE")

    label("loc_803")

    Return()

    # Function_2_7EE end

    def Function_3_804(): pass

    label("Function_3_804")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_850")
    OP_8E(0xFE, 0x1798, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x203A, 0x0, 0x3520, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_3_804")

    label("loc_850")

    Return()

    # Function_3_804 end

    def Function_4_851(): pass

    label("Function_4_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_87E")

    label("loc_858")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87B")
    OP_8D(0xFE, -800, -7100, 4200, -8700, 2000)
    Jump("loc_858")

    label("loc_87B")

    Jump("loc_8FB")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_8AB")

    label("loc_885")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A8")
    OP_8D(0xFE, -800, -7100, 4200, -8700, 2000)
    Jump("loc_885")

    label("loc_8A8")

    Jump("loc_8FB")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8D8")

    label("loc_8B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D5")
    OP_8D(0xFE, -800, -7100, 4200, -8700, 2000)
    Jump("loc_8B2")

    label("loc_8D5")

    Jump("loc_8FB")

    label("loc_8D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FB")
    OP_8D(0xFE, -10160, 3020, -8050, -1770, 2000)
    Jump("loc_8D8")

    label("loc_8FB")

    Return()

    # Function_4_851 end

    def Function_5_8FC(): pass

    label("Function_5_8FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91F")
    OP_8D(0xFE, 6800, -2300, 4700, -12100, 2000)
    Jump("Function_5_8FC")

    label("loc_91F")

    Return()

    # Function_5_8FC end

    def Function_6_920(): pass

    label("Function_6_920")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_943")
    OP_8D(0xFE, 200, 14800, -7900, 10300, 2000)
    Jump("Function_6_920")

    label("loc_943")

    Return()

    # Function_6_920 end

    def Function_7_944(): pass

    label("Function_7_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_971")

    label("loc_94B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96E")
    OP_8D(0xFE, 6700, 3600, 4600, -9900, 2000)
    Jump("loc_94B")

    label("loc_96E")

    Jump("loc_9B3")

    label("loc_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_990")

    label("loc_978")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_978")

    label("loc_98D")

    Jump("loc_9B3")

    label("loc_990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B3")
    OP_8D(0xFE, 2100, 4700, -900, -5100, 2000)
    Jump("loc_990")

    label("loc_9B3")

    Return()

    # Function_7_944 end

    def Function_8_9B4(): pass

    label("Function_8_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9D3")

    label("loc_9BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_9BB")

    label("loc_9D0")

    Jump("loc_B18")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_AF5")

    label("loc_9DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF2")
    OP_8E(0xFE, 0xFFFFC75C, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFC7C0, 0x0, 0xFFFFF510, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBD98, 0x0, 0xFFFFF510, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB94C, 0x0, 0xFFFFDF30, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFD24C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 200)
    Sleep(4000)
    OP_8E(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFCC70, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFD2B0, 0x0, 0xFFFFCEC8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(4000)
    OP_8E(0xFE, 0xFFFFDECC, 0x0, 0xFFFFCEC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDECC, 0x0, 0xFFFFD954, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFCC70, 0x0, 0xFFFFDC74, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC75C, 0x0, 0xFFFFE764, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 200)
    Sleep(5000)
    Jump("loc_9DA")

    label("loc_AF2")

    Jump("loc_B18")

    label("loc_AF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B18")
    OP_8D(0xFE, -12100, 16600, -16600, 14400, 2000)
    Jump("loc_AF5")

    label("loc_B18")

    Return()

    # Function_8_9B4 end

    def Function_9_B19(): pass

    label("Function_9_B19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3C")
    OP_8D(0xFE, -100, 500, 2300, 6000, 2000)
    Jump("Function_9_B19")

    label("loc_B3C")

    Return()

    # Function_9_B19 end

    def Function_10_B3D(): pass

    label("Function_10_B3D")

    Call(0, 11)
    Return()

    # Function_10_B3D end

    def Function_11_B42(): pass

    label("Function_11_B42")

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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA2")
    OP_0D()
    OP_A9(0x11)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_BA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB3")
    TalkEnd(0x8)
    Return()

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C29")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "那些可恶的空贼\x01",
            "终于被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这么长时间\x01",
            "一直让柏斯蒙受着损失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C83")

    label("loc_C29")


    ChrTalk(
        0x8,
        "空贼吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不管有什么理由，\x01",
            "也不应该随便夺取别人的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C83")

    Jump("loc_1663")

    label("loc_C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(
        0x8,
        (
            "道路封锁也解除了，\x01",
            "虽然只有往西航行的定期船，\x01",
            "不过空运也总算恢复了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我的店的状况\x01",
            "也有了非常大的好转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "好～我要更加努力哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4D")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "往西航行的飞行船\x01",
            "终于再次起航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样我就能够\x01",
            "去采购洛连特的蔬菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好～多多采购，\x01",
            "多多卖出～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF2")

    label("loc_E4D")


    ChrTalk(
        0x8,
        (
            "我现在对挑选蔬菜的眼力\x01",
            "可是十分有信心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "特别是帕赛尔农场的蔬菜，可谓绝品。\x01",
            "在这里的销售状况非常好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_1663")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_F9A")

    ChrTalk(
        0x8,
        (
            "这家店的所有水果\x01",
            "都是从拉文努村采购的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个村子以前\x01",
            "虽然是因为矿山而热闹起来的，\x01",
            "但是现在却以果园闻名。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_113C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A2")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "柏斯商人崇尚\x01",
            "自由的商业风气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以前这里曾经有一个\x01",
            "人们各做各的生意、\x01",
            "互不关心的时代。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "全靠前任市长和现任市长小姐\x01",
            "把商人们都团结起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1139")

    label("loc_10A2")


    ChrTalk(
        0x8,
        (
            "钢壁之路的检查哨\x01",
            "好像被撤掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样的话，\x01",
            "进货应该能够恢复了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1139")

    Jump("loc_1663")

    label("loc_113C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_13FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133D")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我们刚开始做生意的时候\x01",
            "受到了市政府的很多援助呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哇～\x01",
            "柏斯真的是商业都市呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是啊，\x01",
            "从梅贝尔市长父亲在的那个时候起， \x01",
            "政府就一直作为我们的后援呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们能够拥有自己的店铺，\x01",
            "也是多亏了大小姐\x01",
            "和前任市长呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "正因如此，\x01",
            "如果我们再让大小姐为难的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "就会给柏斯商人丢脸呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_133D")


    ChrTalk(
        0x8,
        (
            "这里刚开始做生意的时候\x01",
            "受到了市政府的很多援助呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们能够拥有自己的店铺，\x01",
            "也是多亏了大小姐\x01",
            "和前任市长呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_1663")

    label("loc_13FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BB")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "都是军队制定各式各样的规则，\x01",
            "让我四处碰壁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "考虑到进货时的成本，\x01",
            "再这样下去，我的生意就完蛋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（总、总感到一股危险的气氛。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（嗯，飞艇继续停航，\x01",
            "　钢壁之路被封锁……）\x02\x03",
            "（应该给做生意的商人\x01",
            "　带来了许多影响啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_15BB")


    ChrTalk(
        0x8,
        (
            "我这么辛苦，\x01",
            "好不容易才使营业额上升……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在却变成这个样子，\x01",
            "唯一的对策就只有将价格继续提高了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1663")

    TalkEnd(0x8)
    Return()

    # Function_11_B42 end

    def Function_12_1667(): pass

    label("Function_12_1667")

    Call(0, 13)
    Return()

    # Function_12_1667 end

    def Function_13_166C(): pass

    label("Function_13_166C")

    TalkBegin(0x9)
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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CC")
    OP_0D()
    OP_A9(0x10)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_16CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16DD")
    TalkEnd(0x9)
    Return()

    label("loc_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_184F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BC")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "我想从卢安\x01",
            "进一批鱼类产品过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那里过去就以\x01",
            "王国水产量第一而著称。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不愧是被称为\x01",
            "『海港都市』的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184C")

    label("loc_17BC")


    ChrTalk(
        0x9,
        (
            "我想从卢安\x01",
            "进一批鱼类产品过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那里过去就以\x01",
            "王国水产量第一而著称。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184C")

    Jump("loc_2045")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1926")

    ChrTalk(
        0x9,
        (
            "飞艇事件也好，强盗案件也好，\x01",
            "最近让人不安的话题还真多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，这个城市有市长小姐坐镇。\x01",
            "她一定会想出办法来解决的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(
        0x9,
        "听说南街区出现了强盗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那里有许多\x01",
            "非常高档的商店啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0B")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "在这个柏斯市中，\x01",
            "要说起实力仅次于市长的名商人，\x01",
            "就是特里诺和博尔德了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说到这个，最近特里诺的女儿\x01",
            "表现得也越来越抢眼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯嗯……\x01",
            "她的名字好像叫米拉诺？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "总之，她是一个\x01",
            "毫不逊色于她父亲的商业奇才。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1B0B")


    ChrTalk(
        0x9,
        (
            "父女一起上阵，\x01",
            "精明能干的商人真令人羡慕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对了对了，\x01",
            "米拉诺和市长小姐的关系非常好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAD")

    Jump("loc_2045")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D52")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "我和帕克为了在柏斯\x01",
            "能够独树一帜而努力工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "将来开一间超大型的\x01",
            "综合食品店是我们的梦想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在我们的店里能够买到\x01",
            "各种各样又便宜又新鲜的食品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是不是梦幻般的店啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "多亏了有定期船，\x01",
            "流通也变得方便了，\x01",
            "我们的目标肯定能达成的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC7")

    label("loc_1D52")


    ChrTalk(
        0x9,
        (
            "我和帕克\x01",
            "为了在柏斯能够独树一帜，\x01",
            "每天都在努力工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "将来开一间超大型的\x01",
            "综合食品店是我们的梦想。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC7")

    Jump("loc_2045")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8E")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "我们只看到了\x01",
            "自己眼前的蝇头小利……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "小姐所说的\x01",
            "确实很有道理啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们差一点就在\x01",
            "商人的道路上迷失方向了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFA")

    label("loc_1E8E")


    ChrTalk(
        0x9,
        (
            "我们只看到了\x01",
            "自己眼前的蝇头小利……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们差一点就在\x01",
            "商人的道路上迷失方向了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFA")

    Jump("loc_2045")

    label("loc_1EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC7")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "我的同伴帕克\x01",
            "开始哄抬价格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "考虑一下现在的状况，\x01",
            "那样做也是迫不得已啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，\x01",
            "我觉得价格好像也太高了点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1FC7")


    ChrTalk(
        0x9,
        (
            "我的同伴帕克\x01",
            "开始哄抬价格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "考虑一下现在的状况，\x01",
            "那样做也是迫不得已啊。\x01",
            "不过也不能太过分了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2045")

    TalkEnd(0x9)
    Return()

    # Function_13_166C end

    def Function_14_2049(): pass

    label("Function_14_2049")

    TalkBegin(0xA)
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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A9")
    OP_0D()
    OP_A9(0x13)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_20A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20BA")
    TalkEnd(0xA)
    Return()

    label("loc_20BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219C")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "那个人跟过去相比一点都没变……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明是为了和家人一起\x01",
            "在柏斯生活才开始做生意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有什么问题的话\x01",
            "说清楚不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_219C")


    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "那个人跟过去相比一点都没变……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明是为了和家人一起\x01",
            "在柏斯生活才开始做生意的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220C")

    Jump("loc_28D5")

    label("loc_220F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_22BD")

    ChrTalk(
        0xFE,
        (
            "真是的，偶尔也该担心一下这里，\x01",
            "过来露个脸也好啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是薄情的丈夫。\x01",
            "为什么我当初会选他呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_22BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2402")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "这家店本来\x01",
            "是老公首先提出要开的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是店才刚开张，\x01",
            "他就把店强推给我打理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而他自己却\x01",
            "马上回到村里种树去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他脑子里到底在想些什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2495")

    label("loc_2402")


    ChrTalk(
        0xFE,
        (
            "这家店本来\x01",
            "是老公首先提出要开的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是他却把店强推给我打理，\x01",
            "自己回到村里种树去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2495")

    Jump("loc_28D5")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_255F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2517")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "呼，再加一把劲儿吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不知道留在村里的老公\x01",
            "现在是不是在很有精神地干活呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255C")

    label("loc_2517")


    ChrTalk(
        0xFE,
        (
            "不知道留在村里的老公\x01",
            "现在是不是在很有精神地干活呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255C")

    Jump("loc_28D5")

    label("loc_255F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_262C")

    ChrTalk(
        0xFE,
        (
            "最近店面扩大了，\x01",
            "事情也变多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "波波能经常过来帮忙真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是个好孩子。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_262C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_26AC")

    ChrTalk(
        0xFE,
        (
            "我这店的商品都是一些\x01",
            "融入了女性智慧的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "可不会输给别人的哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_26AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_28D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288A")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "#4S您好，欢迎光临！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的小妹妹与小兄弟！\x01",
            "我这里可是有很多好货哦！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(700)

    ChrTalk(
        0x101,
        (
            "#004F吓、吓死我了～\x01",
            "这里的声音还真响呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F和传闻一样，这里是个充满活力的地方啊。\x01",
            "在这里转了一天带给我的就是这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F就是啊。\x02\x03",
            "因为超市聚集了\x01",
            "从利贝尔各地前来的\x01",
            "想在商界有一番作为的人们啊。\x02\x03",
            "这份干劲与热情\x01",
            "可不是假的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D5")

    label("loc_288A")


    ChrTalk(
        0xFE,
        (
            "如果有您喜欢的物品，\x01",
            "您可以放心地拿起来观赏。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D5")

    TalkEnd(0xA)
    Return()

    # Function_14_2049 end

    def Function_15_28D9(): pass

    label("Function_15_28D9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2930")

    ChrTalk(
        0xFE,
        (
            "留在拉文努村的爸爸\x01",
            "现在正在干什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_29E5")

    ChrTalk(
        0xFE,
        (
            "我觉得爸爸回到村里，\x01",
            "这其中肯定是有什么原因的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为，\x01",
            "爸爸对于开店是最有兴趣的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_29E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A63")

    ChrTalk(
        0xFE,
        (
            "妈妈，\x01",
            "是不是很想见爸爸呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经常能看到她\x01",
            "一脸寂寞的样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2B64")

    ChrTalk(
        0xFE,
        (
            "我的爸爸啊，\x01",
            "是在村里种水果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里出售的水果\x01",
            "也有可能是我爸爸种出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实他本应该和我们\x01",
            "一起经营这家小店的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECA")

    label("loc_2B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5D")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈真是的，\x01",
            "拿餐具这么不小心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我光是看着\x01",
            "就已经很紧张了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么重要的商品\x01",
            "应该轻拿轻放才对啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDF")

    label("loc_2C5D")


    ChrTalk(
        0xFE,
        (
            "妈妈真是的，\x01",
            "拿餐具这么不小心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我光是看着\x01",
            "就已经很紧张了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDF")

    Jump("loc_2ECA")

    label("loc_2CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEC")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "刚才市长姐姐来了，\x01",
            "给了我们很多的建议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "关于商品的排列和招待客人的方式，\x01",
            "就算对还是小孩子的我也很认真地传授着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后还在我们这儿\x01",
            "买了一些餐具。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2E")

    label("loc_2DEC")


    ChrTalk(
        0xFE,
        (
            "市长姐姐\x01",
            "经常在超市巡视呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2E")

    Jump("loc_2ECA")

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2ECA")

    ChrTalk(
        0xFE,
        (
            "我也算是这里的店员了。\x01",
            "在帮我妈妈的忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可绝对不是\x01",
            "在这里玩耍哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ECA")

    TalkEnd(0xB)
    Return()

    # Function_15_28D9 end

    def Function_16_2ECE(): pass

    label("Function_16_2ECE")

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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2E")
    OP_0D()
    TalkBegin(0xC)
    OP_A9(0xC)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_2F2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3F")
    TalkEnd(0xC)
    Return()

    label("loc_2F3F")

    OP_A2(0x6)
    Call(0, 17)
    OP_8C(0xC, 270, 0)
    Return()

    # Function_16_2ECE end

    def Function_17_2F4E(): pass

    label("Function_17_2F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2FE3")
    TalkBegin(0xC)

    ChrTalk(
        0xC,
        "各位，真是谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这下我就可以放心地\x01",
            "进行新药的调配了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE7")

    label("loc_2FE3")

    Call(0, 18)

    label("loc_2FE7")

    Jump("loc_3113")

    label("loc_2FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x4000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_303B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_302C")
    Call(1, 2)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_302C")

    Call(1, 1)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_303B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3066")
    Call(1, 1)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_3066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30F9")
    TalkBegin(0xC)

    ChrTalk(
        0xC,
        (
            "那么各位，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "请小心行事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30FD")

    label("loc_30F9")

    Call(0, 18)

    label("loc_30FD")

    Jump("loc_310C")

    label("loc_3100")

    Call(1, 0)
    OP_8C(0xC, 270, 0)
    Return()

    label("loc_310C")

    Jump("loc_3113")

    label("loc_310F")

    Call(0, 18)

    label("loc_3113")

    TalkEnd(0xC)
    OP_8C(0xC, 270, 0)
    Return()

    # Function_17_2F4E end

    def Function_18_311E(): pass

    label("Function_18_311E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E4")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        (
            "扰乱柏斯治安的坏人\x01",
            "终于被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这下子又可以\x01",
            "安心地做买卖了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3244")

    label("loc_31E4")


    ChrTalk(
        0xC,
        (
            "坏人被逮捕了，\x01",
            "又可以安心地做买卖了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3244")

    Jump("loc_3B74")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_33DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3350")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        (
            "最近我的店里\x01",
            "也渐渐忙起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我在考虑是不是要\x01",
            "多请一个人过来帮忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "可是我又想和顾客接触，\x01",
            "亲自沟通一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "真是伤脑筋啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33DB")

    label("loc_3350")


    ChrTalk(
        0xC,
        (
            "我在考虑是不是要\x01",
            "多请一个人过来帮忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "可是我又想和顾客接触，\x01",
            "亲自沟通一下，\x01",
            "真是伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DB")

    Jump("loc_3B74")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_346B")

    ChrTalk(
        0xC,
        (
            "哎呀，\x01",
            "王国军好像也来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "是不是发生什么事情了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B74")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3549")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        (
            "即使飞艇停航了，\x01",
            "柏斯商人也不会这么简单屈服的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "因为我们总会\x01",
            "想出办法来应付的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "呵·呵·呵。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3603")

    label("loc_3549")


    ChrTalk(
        0xC,
        (
            "即使飞艇停航了，\x01",
            "柏斯商人也不会这么简单屈服的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "因为我们总会\x01",
            "想出办法来应付的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3603")

    Jump("loc_3B74")

    label("loc_3606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3701")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        (
            "我会针对病人各自的症状\x01",
            "来调配药剂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "最近我从东方\x01",
            "订购了一些中药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "买卖的手段也是很重要的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37AF")

    label("loc_3701")


    ChrTalk(
        0xC,
        (
            "我会针对病人各自的症状\x01",
            "来调配药剂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "最近我从东方\x01",
            "订购了一些中药。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AF")

    Jump("loc_3B74")

    label("loc_37B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_39D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3962")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        (
            "市长每月都会从超市的店铺中\x01",
            "挑选出一家进行表彰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "上个月，\x01",
            "本店就被评选为『信得过的好商店』。   \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哎呀哎呀～\x01",
            "真是充满了干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F原来如此，\x01",
            "市长真的是下了很大功夫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，市长虽然年轻，\x01",
            "但是深受市民的爱戴和支持。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D6")

    label("loc_3962")


    ChrTalk(
        0xC,
        (
            "上个月，\x01",
            "本店被评选为超市中\x01",
            "『信得过的好商店』。   \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哎呀哎呀～\x01",
            "真是充满了干劲啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D6")

    Jump("loc_3B74")

    label("loc_39D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B22")
    OP_A2(0x4)

    ChrTalk(
        0xC,
        "想买点什么东西吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我店里的药都是很有效的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～连药都有卖吗？\x02\x03",
            "在柏斯超市\x01",
            "真是想买什么就能买到什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，的确……\x01",
            "出售各式的商品才是这里的特点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B74")

    label("loc_3B22")


    ChrTalk(
        0xC,
        (
            "想买点什么东西吗？\x01",
            "我店里的药都是很有效的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B74")

    OP_A3(0x6)
    TalkEnd(0xC)
    OP_8C(0xC, 270, 0)
    Return()

    # Function_18_311E end

    def Function_19_3B82(): pass

    label("Function_19_3B82")

    Call(0, 20)
    Return()

    # Function_19_3B82 end

    def Function_20_3B87(): pass

    label("Function_20_3B87")

    TalkBegin(0xD)
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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE7")
    OP_0D()
    OP_A9(0x12)
    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_3BE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BF8")
    TalkEnd(0xD)
    Return()

    label("loc_3BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8C")
    OP_A2(0x7)

    ChrTalk(
        0xD,
        (
            "空贼被逮捕了，\x01",
            "我的未婚夫也回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不过他却自己\x01",
            "开了另一家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "大概是因为自己不在的时候\x01",
            "这家店的经营状况很好，\x01",
            "有点不甘心吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "呵呵，还是老样子，\x01",
            "又顽固又不会轻易认输呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "以后我们之间就要竞争了。\x01",
            "为了不输给他，我还要加油才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E35")

    label("loc_3D8C")


    ChrTalk(
        0xD,
        (
            "呵呵，还是老样子，\x01",
            "又顽固又不会轻易认输呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "以后我们之间就要竞争了。\x01",
            "为了不输给他，我还要加油才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E35")

    Jump("loc_4893")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0F")
    OP_A2(0x7)

    ChrTalk(
        0xD,
        (
            "嘿嘿，\x01",
            "来这里的客人正在慢慢增加哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "他一定会很高兴的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "不知道他能不能早点回来呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F9F")

    label("loc_3F0F")


    ChrTalk(
        0xD,
        (
            "……明明已经找到了定期船，\x01",
            "为什么他还没有回来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "我……一定要加油。\x02",
    )

    CloseMessageWindow()

    label("loc_3F9F")

    Jump("loc_4893")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4046")

    ChrTalk(
        0xD,
        (
            "听说军队找到\x01",
            "失踪的定期船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "那么他……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不知道飞艇上的乘客们\x01",
            "现在怎样了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4893")

    label("loc_4046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_43C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_40DE")

    ChrTalk(
        0xD,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "柏斯超市的名产——\x01",
            "软绵绵香蛋糕，\x01",
            "客人要来一块吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C6")

    label("loc_40DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4351")
    OP_A2(0x8)

    ChrTalk(
        0xD,
        (
            "……这家店，\x01",
            "其实是我的未婚夫开设的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "他乘坐了那艘\x01",
            "如今已经成为话题的消失的定期船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "但是，\x01",
            "我一直坚信他一定会回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "在他回来之前，\x01",
            "我一定要守护好这家店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        "#012F艾丝蒂尔，你怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……说的是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F失踪的飞艇上\x01",
            "不单有自己的亲人乘坐啊，\x01",
            "还有其他的百姓的亲人也在里面。\x02\x03",
            "#009F那么，\x01",
            "我就要更加努力才行呢……\x02\x03",
            "作为游击士协会的一员，\x01",
            "也作为父亲的女儿！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔……\x02\x03",
            "嗯，说得对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C6")

    label("loc_4351")

    OP_A2(0x7)

    ChrTalk(
        0xD,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F？？\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "啊，对、对不起。\x01",
            "欢迎光临！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C6")

    Jump("loc_4893")

    label("loc_43C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_44AF")

    ChrTalk(
        0xD,
        (
            "嘿嘿，\x01",
            "刚开始稍微有点迷茫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不过现在终于开始\x01",
            "能够顺利地卖出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "总之带着微笑努力吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4893")

    label("loc_44AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_467B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C6")
    OP_A2(0x7)

    ChrTalk(
        0xD,
        (
            "我最近开始\x01",
            "帮忙经营这家店，\x01",
            "不过还是很不习惯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "招呼客人的时候\x01",
            "也觉得非常害羞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "唉～不行啊。\x01",
            "再这样下去的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4678")

    label("loc_45C6")


    ChrTalk(
        0xD,
        (
            "我最近开始\x01",
            "帮忙经营这家店，\x01",
            "不过还是很不习惯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "招呼客人的时候\x01",
            "也觉得非常害羞呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4678")

    Jump("loc_4893")

    label("loc_467B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4830")
    OP_A2(0x7)

    ChrTalk(
        0xD,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "柏斯超市的名产——\x01",
            "软绵绵香蛋糕，\x01",
            "客人要来一份吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哇，看上去很好吃呢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真的……\x01",
            "味道很香呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F约修亚，找到父亲之后，\x01",
            "我们一起来这里吃蛋糕吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F……嗯，好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F真的？\x01",
            "那就说定了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4893")

    label("loc_4830")


    ChrTalk(
        0xD,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "柏斯超市的名产——\x01",
            "软绵绵香蛋糕，\x01",
            "客人要来一份吗～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4893")

    TalkEnd(0xD)
    Return()

    # Function_20_3B87 end

    def Function_21_4897(): pass

    label("Function_21_4897")

    Call(0, 22)
    Return()

    # Function_21_4897 end

    def Function_22_489C(): pass

    label("Function_22_489C")

    TalkBegin(0xE)
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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48FC")
    OP_0D()
    OP_A9(0x19)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_48FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_490D")
    TalkEnd(0xE)
    Return()

    label("loc_490D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3C")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "因为飞艇停运，\x01",
            "服装等商品还是很难进到货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过相反的，\x01",
            "本店自己设计的服装\x01",
            "比预想中卖得还要好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "好～为了我的家人，\x01",
            "一定要更加努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B04")

    label("loc_4A3C")


    ChrTalk(
        0xE,
        (
            "作为试验的\x01",
            "本店原创服装\x01",
            "比预想中卖的还要好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "好～为了我的家人，\x01",
            "一定要更加努力才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B04")

    Jump("loc_5609")

    label("loc_4B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE7")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "那件事有没有\x01",
            "让她和女儿感到心有余悸呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "嗯～\x01",
            "我觉得强盗还是会再来，\x01",
            "担心得无法好好工作呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C47")

    label("loc_4BE7")


    ChrTalk(
        0xE,
        "……好，我决定了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "今天就不营业了，\x01",
            "我还是早点回家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C47")

    Jump("loc_5609")

    label("loc_4C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D95")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "昨晚，\x01",
            "有强盗擅自闯入我家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "正好那个时候，\x01",
            "家里只有我妻子和女儿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "虽然两个人都没什么事，\x01",
            "但是她们好像受到了不小的惊吓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "今天早上，\x01",
            "虽然妻子微笑着送我出门，\x01",
            "但是我还是很担心家里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E33")

    label("loc_4D95")


    ChrTalk(
        0xE,
        "昨晚有强盗擅自闯入我家。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "今天早上，\x01",
            "虽然妻子微笑着送我出门，\x01",
            "但是我还是很担心家里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E33")

    Jump("loc_5609")

    label("loc_4E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED9")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "自己设计并且自己缝制的衣服\x01",
            "卖得也相当不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "好，\x01",
            "我还要多设计几种样式才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F87")

    label("loc_4ED9")


    ChrTalk(
        0xE,
        (
            "对于原创的衣服，\x01",
            "来这里询问的女性顾客比较多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "下次我试着以女性服装\x01",
            "为中心来设计看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F87")

    Jump("loc_5609")

    label("loc_4F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_513E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5096")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "在王都发行的新款服装\x01",
            "没办法进到货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "而且店里的存货\x01",
            "也渐渐少起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这下子只能大幅增加\x01",
            "原创服装的数量了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_513B")

    label("loc_5096")


    ChrTalk(
        0xE,
        (
            "其实之前就曾经尝试过\x01",
            "增加本店的原创服装数量，\x01",
            "效果还不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "趁这个机会再试一下\x01",
            "也不是什么坏事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_513B")

    Jump("loc_5609")

    label("loc_513E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_535D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B3")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "我本来是\x01",
            "王国军的一名军官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过因为怎么也放不下梦想，\x01",
            "所以就开了这样一家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过妻子却很反对我这么做。\x01",
            "为了得到她的理解，我要更加努力才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "自从我回来做生意，\x01",
            "女儿也很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_535A")

    label("loc_52B3")


    ChrTalk(
        0xE,
        (
            "我本来是\x01",
            "王国军的一名军官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过因为怎么也放不下梦想，\x01",
            "所以就开了这样一家店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_535A")

    Jump("loc_5609")

    label("loc_535D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_5609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5550")
    OP_A2(0x9)

    ChrTalk(
        0xE,
        (
            "欢迎光临。\x01",
            "今天想要买些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "本店能够订购到\x01",
            "王都的品牌服饰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "可以的话，就多看看吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这里好像是卖衣服的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我很喜欢这套衣服啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(
        0xE,
        (
            "有自己喜欢的款式的话，\x01",
            "还可以专门给您订制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "欢迎再来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5609")

    label("loc_5550")


    ChrTalk(
        0xE,
        (
            "有自己喜欢的款式的话，\x01",
            "还可以专门给您订制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "欢迎再来。\x02",
    )

    CloseMessageWindow()

    label("loc_5609")

    TalkEnd(0xE)
    Return()

    # Function_22_489C end

    def Function_23_560D(): pass

    label("Function_23_560D")

    TalkBegin(0xF)
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
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5685")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_END)), "loc_566E")
    OP_A9(0x6E)
    Jump("loc_567C")

    label("loc_566E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_567A")
    OP_A9(0x1B)
    Jump("loc_567C")

    label("loc_567A")

    OP_A9(0x1A)

    label("loc_567C")

    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_5685")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5696")
    TalkEnd(0xF)
    Return()

    label("loc_5696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_572D")

    ChrTalk(
        0xFE,
        (
            "顾客需要的商品\x01",
            "经常会有变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须要摸清楚规律\x01",
            "来进货才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6282")

    label("loc_572D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_581A")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "商品的采购终于\x01",
            "能够恢复原来的样子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁这个机会\x01",
            "再增加一些实用性商品吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可是那种跌倒了\x01",
            "也不会轻易认输的性格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5871")

    label("loc_581A")


    ChrTalk(
        0xFE,
        (
            "我可是那种跌倒了\x01",
            "也不会轻易认输的性格。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5871")

    Jump("loc_6282")

    label("loc_5874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_5949")

    ChrTalk(
        0xFE,
        (
            "听说城里被\x01",
            "强盗洗劫了是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把别人的东西占为己有，\x01",
            "真不像话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望有人能够快点\x01",
            "把那些家伙抓住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6282")

    label("loc_5949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5BBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2B")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "您好，欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "顺便过来看看吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就现在！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "共和国产的高级绒毯\x01",
            "只要５００米拉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只要５００米拉哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平时要卖\x01",
            "１５００米拉的商品\x01",
            "现在只要５００米拉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "先到先得哦！\x01",
            "而且现在还赠送一条\x01",
            "相同模样的挂毯哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB9")

    label("loc_5B2B")


    ChrTalk(
        0xFE,
        (
            "共和国产的高级绒毯\x01",
            "只要５００米拉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只要５００米拉哦！\x02",
    )

    CloseMessageWindow()

    label("loc_5BB9")

    Jump("loc_6282")

    label("loc_5BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_5D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC3")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "真是的，军队打算把道路\x01",
            "和国际空港封锁到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本应从帝国送过来的商品\x01",
            "现在也到达不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是难办啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D67")

    label("loc_5CC3")


    ChrTalk(
        0xFE,
        (
            "真是的，军队打算把道路\x01",
            "和国际空港封锁到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本应从帝国送过来的商品\x01",
            "现在也到达不了了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D67")

    Jump("loc_6282")

    label("loc_5D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_602C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F66")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "我从青空市场时代开始\x01",
            "就在这里开店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "算是现在超市中最老的店铺吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哇，您的资历真老啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多谢夸奖……\x01",
            "不过这都是４０多年前的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个时候，\x01",
            "这里还没有这么漂亮的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯也起了翻天覆地的变化，\x01",
            "不过人们的热情却一直没变。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6029")

    label("loc_5F66")


    ChrTalk(
        0xFE,
        (
            "这个市场建起来之前，\x01",
            "在那个青空市场时代\x01",
            "我就在这里开店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "算是现在超市中最老的店铺吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6029")

    Jump("loc_6282")

    label("loc_602C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_6282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_620A")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从古书到织品，还有日用品，\x01",
            "米蕾婆婆的杂货店应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哇哇，有好多东西呀。\x02\x03",
            "同样是杂货店，\x01",
            "比里农叔叔店里的\x01",
            "东西要多得多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，真不愧是超市里开的店，\x01",
            "感觉就是不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这里可是有许多从\x01",
            "帝国与共和国带来的舶来品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我对自家店的商品还是很有信心的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6282")

    label("loc_620A")


    ChrTalk(
        0xFE,
        (
            "我这里可是有许多从\x01",
            "帝国与共和国带来的舶来品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我对自家店的商品还是很有信心的。\x02",
    )

    CloseMessageWindow()

    label("loc_6282")

    TalkEnd(0xF)
    Return()

    # Function_23_560D end

    def Function_24_6286(): pass

    label("Function_24_6286")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6466")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BA")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "洋葱和胡萝卜\x01",
            "还有还有……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "洋葱和胡萝卜\x01",
            "还有还有……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，好像还有肉吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6463")

    label("loc_63BA")


    ChrTalk(
        0xFE,
        (
            "洋葱～胡萝卜～\x01",
            "还·有·肉⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "编成歌就很容易记住了。\x02",
    )

    CloseMessageWindow()

    label("loc_6463")

    Jump("loc_68FE")

    label("loc_6466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6509")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "我终于能够独自一人出来买东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很厉害吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "我只买过卷心菜，\x01",
            "除此之外就没有试过其他的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6533")

    label("loc_6509")


    ChrTalk(
        0xFE,
        (
            "我要努力\x01",
            "早点成为大人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6533")

    Jump("loc_68FE")

    label("loc_6536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6589")

    ChrTalk(
        0xFE,
        (
            "外面有很多\x01",
            "好可怕的叔叔呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_6589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6626")

    ChrTalk(
        0xFE,
        (
            "这个蛋糕\x01",
            "看起来好好吃啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "出来买东西的钱\x01",
            "不能乱花呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_6626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_67B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6726")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "卷心菜、卷心菜……\x01",
            "是我妈妈让我买的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和不认识的人说话\x01",
            "总觉得有点可怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好不容易\x01",
            "来到商店前面了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67AE")

    label("loc_6726")


    ChrTalk(
        0xFE,
        "对了，先练习一下吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请给我１棵卷心菜……\x01",
            "请给我１棵卷心菜……\x01",
            "请给我１棵卷心菜……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67AE")

    Jump("loc_68FE")

    label("loc_67B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6863")

    ChrTalk(
        0xFE,
        (
            "呜～\x01",
            "忘记该买什么东西了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "难得妈妈拜托我买东西……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是回家问问吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_68FE")

    label("loc_6863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_68FE")

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "这可是我出生以来第一次自己出来办事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……嗯，\x01",
            "我要买什么来着？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68FE")

    TalkEnd(0x10)
    Return()

    # Function_24_6286 end

    def Function_25_6902(): pass

    label("Function_25_6902")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D9")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "偶尔也奢侈一次，\x01",
            "买点牛排尝尝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果决定要大吃一顿的话，\x01",
            "做什么菜也就容易考虑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A4B")

    label("loc_69D9")


    ChrTalk(
        0xFE,
        (
            "如果决定要大吃一顿的话，\x01",
            "做什么菜也就容易考虑了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A4B")

    Jump("loc_70F0")

    label("loc_6A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B3B")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "啊啊～干脆让我们家的人\x01",
            "轮流来考虑每天吃什么好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "或者，\x01",
            "事先决定好一个星期的安排，\x01",
            "然后不断重复怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_6B3B")


    ChrTalk(
        0xFE,
        (
            "啊啊～干脆让我们家的人\x01",
            "轮流来考虑每天吃什么好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BA1")

    Jump("loc_70F0")

    label("loc_6BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6D81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D01")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "肉、蔬菜、鱼……\x01",
            "嗯～今天做什么好呢。\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管是强盗来，\x01",
            "还是王国军来，\x01",
            "都要考虑做什么菜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "女王陛下能不能让我有一天\x01",
            "可以不用为做什么菜而烦恼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D7E")

    label("loc_6D01")


    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "女王陛下能不能让我有一天\x01",
            "可以不用为做什么菜而烦恼呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D7E")

    Jump("loc_70F0")

    label("loc_6D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_6E65")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "今天做什么菜比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是伤脑筋啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来想来店里之后再决定的，\x01",
            "不过好像还是决定不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70F0")

    label("loc_6E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_6F7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F4A")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        "今天轮到吃肉了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底是做牛排呢，\x01",
            "还是炖肉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～真伤脑筋……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "考虑每天的菜单\x01",
            "真是一件痛苦的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F7B")

    label("loc_6F4A")


    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "还是改做鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F7B")

    Jump("loc_70F0")

    label("loc_6F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_705D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701B")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "好，决定了！\x01",
            "今天就做鱼好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，到底是烧着吃呢，\x01",
            "还是煮着吃呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_705A")

    label("loc_701B")


    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我想还是改做肉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_705A")

    Jump("loc_70F0")

    label("loc_705D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_70F0")

    ChrTalk(
        0xFE,
        (
            "那～么，\x01",
            "今天做些什么菜比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是烧肉呢，\x01",
            "还是煮鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70F0")

    TalkEnd(0x11)
    Return()

    # Function_25_6902 end

    def Function_26_70F4(): pass

    label("Function_26_70F4")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C5")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "为了攒够买书的钱，\x01",
            "我决定在这里打工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我倒是没想到会在\x01",
            "经常光顾的店打工。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722E")

    label("loc_71C5")


    ChrTalk(
        0xFE,
        (
            "不过我倒是没想到会在\x01",
            "经常光顾的店打工。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_722E")

    Jump("loc_77D2")

    label("loc_7231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_74C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7423")
    OP_A2(0x394)

    ChrTalk(
        0xFE,
        (
            "我是想来买小说的续篇的，\x01",
            "果然还是没有进货呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我对于一本已经读过一遍的书，\x01",
            "基本上不会再去看第二遍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这本书就送给你们了。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x215, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第４卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "店里的老婆婆问我\x01",
            "是不是想在这里工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是因为我总是\x01",
            "在询问商品的缘故呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74BF")

    label("loc_7423")


    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "店里的老婆婆问我\x01",
            "是不是想在这里工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是因为我总是\x01",
            "在询问商品的缘故呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74BF")

    Jump("loc_77D2")

    label("loc_74C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7556")

    ChrTalk(
        0xFE,
        (
            "老旧而又贵重的书籍\x01",
            "还是要悉心地保管\x01",
            "比较好啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这就去向\x01",
            "店里的老婆婆说一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_7556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7602")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "里面的书都布满灰尘了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "问店里的人借个掸子，\x01",
            "打扫一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_7602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_76A2")

    ChrTalk(
        0xFE,
        (
            "最近外国的书\x01",
            "都进不货呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是因为军队制订的那些\x01",
            "各种各样的规章制度吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_76A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7770")

    ChrTalk(
        0xFE,
        (
            "每次路过这里，\x01",
            "我都会过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为来得次数太多，\x01",
            "对于这家店，\x01",
            "我有自信比店里的人了解得更详细哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_7770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_77D2")

    ChrTalk(
        0xFE,
        "嗯～没有我看得中的书啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是找找其他的吧。\x02",
    )

    CloseMessageWindow()

    label("loc_77D2")

    TalkEnd(0x12)
    Return()

    # Function_26_70F4 end

    def Function_27_77D6(): pass

    label("Function_27_77D6")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7901")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78A7")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "啊啊～真可惜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蛋糕店的大姐\x01",
            "原来已经订婚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有点失望，\x01",
            "不过作为大姐的忠实支持者\x01",
            "我以后还会经常光顾的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FE")

    label("loc_78A7")


    ChrTalk(
        0xFE,
        (
            "啊啊～……\x01",
            "蛋糕店的大姐\x01",
            "原来已经订婚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78FE")

    Jump("loc_7DF6")

    label("loc_7901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_798C")

    ChrTalk(
        0xFE,
        (
            "果然，\x01",
            "这家店越来越受市民欢迎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和我想的一样，\x01",
            "大姐她也非常努力呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF6")

    label("loc_798C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_7A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A31")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "最近蛋糕店的大姐\x01",
            "好像没什么精神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是不是在为什么事情担心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A7C")

    label("loc_7A31")


    ChrTalk(
        0xFE,
        "最近，总是发生一些令人不安的事情。\x02",
    )

    CloseMessageWindow()

    label("loc_7A7C")

    Jump("loc_7DF6")

    label("loc_7A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B66")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "那家蛋糕店啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从大姐开始接管以来，\x01",
            "味道也变得非常好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我每天都吃，\x01",
            "不过它的味道可是一天比一天好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BDA")

    label("loc_7B66")


    ChrTalk(
        0xFE,
        "那家蛋糕店啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从大姐开始接管以来，\x01",
            "味道也变得非常好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BDA")

    Jump("loc_7DF6")

    label("loc_7BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_7CB7")

    ChrTalk(
        0xFE,
        (
            "自从大姐\x01",
            "开始接手蛋糕店，\x01",
            "蛋糕的销量也变好了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也是因为能看到\x01",
            "大姐的微笑才去买的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF6")

    label("loc_7CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_7D5F")

    ChrTalk(
        0xFE,
        (
            "那家店的大姐\x01",
            "健康的微笑真是迷人啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了能见到她的笑脸，\x01",
            "要我一天之内买多少个蛋糕都可以。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF6")

    label("loc_7D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_7DF6")

    ChrTalk(
        0xFE,
        (
            "软绵绵香蛋糕的店里的\x01",
            "服务员好像换成一位女性了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前明明是个男的，\x01",
            "难道发生什么事了吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DF6")

    TalkEnd(0x13)
    Return()

    # Function_27_77D6 end

    def Function_28_7DFA(): pass

    label("Function_28_7DFA")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ED6")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "我非常喜欢\x01",
            "这个超市给人的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算会惹父母生气，\x01",
            "我也要偷偷到这里来玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为总是呆在家里好无聊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F5A")

    label("loc_7ED6")


    ChrTalk(
        0xFE,
        (
            "我非常喜欢\x01",
            "这个超市给人的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算会惹父母生气，\x01",
            "我也要偷偷到这里来玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F5A")

    Jump("loc_85D8")

    label("loc_7F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_80EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_806E")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "虽然父母反对我来这里，\x01",
            "但是我非常喜欢\x01",
            "这个超市给人的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "我还是偷偷到这里来玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为总是呆在家里好无聊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_80E7")

    label("loc_806E")


    ChrTalk(
        0xFE,
        (
            "在这里可以听到各种各样的话题，\x01",
            "可以品尝各类食物，\x01",
            "还可以见识到许多人和事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得来这里体验生活\x01",
            "对于自己来说是非常必要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80E7")

    Jump("loc_85D8")

    label("loc_80EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_8144")

    ChrTalk(
        0xFE,
        (
            "我去超市的事情\x01",
            "被我妈妈发现了，\x01",
            "然后被狠狠地骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()
    Jump("loc_85D8")

    label("loc_8144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8286")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "我第一次尝试自己买东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是在喷水池旁边卖的\x01",
            "软绵绵的像点心那样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家好像都在\x01",
            "那个地方吃东西，\x01",
            "我就模仿他们也吃了一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "非常好吃。\x01",
            "这给了我一个非常珍贵的体验。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8310")

    label("loc_8286")


    ChrTalk(
        0xFE,
        (
            "虽然在屋外吃东西\x01",
            "感觉有损形象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我觉得只有在这个地方\x01",
            "才能品味出它的美味。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8310")

    Jump("loc_85D8")

    label("loc_8313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8388")

    ChrTalk(
        0xFE,
        (
            "总像这样只是看着\x01",
            "也不是办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就在这里\x01",
            "试着买点什么吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D8")

    label("loc_8388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8429")

    ChrTalk(
        0xFE,
        (
            "虽然是偷偷跑过来玩的，\x01",
            "不过看到了好多稀奇的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "原来大家都是在\x01",
            "这种地方买东西的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D8")

    label("loc_8429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_85D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8525")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "虽然我一直住在柏斯，\x01",
            "但这还是我第一次来到超市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "总觉得这里好像乱糟糟的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且……咳咳……\x01",
            "怎么会有这么脏的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85D8")

    label("loc_8525")


    ChrTalk(
        0xFE,
        (
            "虽然我一直住在柏斯，\x01",
            "但这还是我第一次来到超市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "总觉得这里好像乱糟糟的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D8")

    TalkEnd(0x14)
    Return()

    # Function_28_7DFA end

    def Function_29_85DC(): pass

    label("Function_29_85DC")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_86AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8670")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "今天又进了一些餐具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "这才是东方的精品啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86AB")

    label("loc_8670")


    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "这才是东方的精品啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86AB")

    Jump("loc_8CDC")

    label("loc_86AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_8765")

    ChrTalk(
        0xFE,
        (
            "我听说，\x01",
            "共和国东边有许多国家\x01",
            "也制作各式各样的陶器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一直想找个时间\x01",
            "进行探求陶器之旅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CDC")

    label("loc_8765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_8806")

    ChrTalk(
        0xFE,
        (
            "不知道为什么\x01",
            "有许多军人在城里出入……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "给人一种盛气凌人的感觉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CDC")

    label("loc_8806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_895A")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "帝国产的陶器拥有豪华绚烂的装饰，\x01",
            "非常具有艺术性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "相反，\x01",
            "共和国的陶器颜色与装饰都非常朴素，\x01",
            "但是会让人有种一直想用下去的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真的是各有特色啊。\x01",
            "正因为如此，陶器这种东西才会让人觉得很有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A04")

    label("loc_895A")


    ChrTalk(
        0xFE,
        (
            "顺便提一下，\x01",
            "利贝尔的陶器在外形和装饰上都非常简单，\x01",
            "但是充满高雅气质。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……我是这么感觉的。\x02",
    )

    CloseMessageWindow()

    label("loc_8A04")

    Jump("loc_8CDC")

    label("loc_8A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_8C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B80")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "发现它潜在的价值，\x01",
            "然后低价购进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在越来越体会到\x01",
            "买卖古董的最大乐趣了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "虽说本来我还是一个门外汉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一挑一选、一买一卖，\x01",
            "呵呵，就可以将大半的破烂化成钱财。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C39")

    label("loc_8B80")


    ChrTalk(
        0xFE,
        (
            "发现它潜在的价值，\x01",
            "然后低价购进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在越来越体会到\x01",
            "买卖古董的最大乐趣了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C39")

    Jump("loc_8CDC")

    label("loc_8C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_8CAE")

    ChrTalk(
        0xFE,
        (
            "我喜欢去淘一些\x01",
            "被挖掘出来的古董。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要看到品种各异的古董摆在面前，\x01",
            "我整个人就会坐立不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CDC")

    label("loc_8CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8CDC")

    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "这个东西有点……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CDC")

    TalkEnd(0x15)
    Return()

    # Function_29_85DC end

    def Function_30_8CE0(): pass

    label("Function_30_8CE0")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_8E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DAB")
    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "买不到新鲜的东西\x01",
            "真是很痛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果在便宜的时候\x01",
            "能够多买一些的话，\x01",
            "就能改善家庭财政状况了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DFE")

    label("loc_8DAB")


    ChrTalk(
        0xFE,
        (
            "买不到新鲜的东西\x01",
            "真是很痛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DFE")

    Jump("loc_935F")

    label("loc_8E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_8F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE6")
    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "我有今天的打折券哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用什么手段\x01",
            "才能买到便宜好货……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这已经成为\x01",
            "我的生存价值之一了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "现在开始履行主妇的本分吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F39")

    label("loc_8EE6")


    ChrTalk(
        0xFE,
        (
            "用什么手段\x01",
            "才能买到便宜好货……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这已经成为\x01",
            "我的生存价值之一了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F39")

    Jump("loc_935F")

    label("loc_8F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_903F")

    ChrTalk(
        0xFE,
        (
            "今天没有哪家商店\x01",
            "进行特价大甩卖呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，绝不能疏忽对情报的收集。\x01",
            "为了我家明天的帐簿着想！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定明天\x01",
            "就会有什么出乎意料的\x01",
            "绝世珍宝被我发现呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_935F")

    label("loc_903F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_910A")
    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "哼，我不甘心！\x01",
            "这算什么意思！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天，\x01",
            "我已经身无分文了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我对这家店大甩卖的时机\x01",
            "竟然预测失误……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_917F")

    label("loc_910A")


    ChrTalk(
        0xFE,
        (
            "哼，我不甘心！\x01",
            "这算什么意思！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天，\x01",
            "我已经身无分文了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_917F")

    Jump("loc_935F")

    label("loc_9182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_921D")

    ChrTalk(
        0xFE,
        (
            "今天从三点开始\x01",
            "一定会有减价肉卖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "得赶快去商店前面\x01",
            "占个好位置等着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_935F")

    label("loc_921D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_92E2")

    ChrTalk(
        0xFE,
        (
            "如果想买到广告促销品，\x01",
            "就一定要在超市开业前去排队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这是基本中的基本。\x02",
    )

    CloseMessageWindow()
    Jump("loc_935F")

    label("loc_92E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_935F")

    ChrTalk(
        0xFE,
        (
            "那么～\x01",
            "今天哪家店会有促销呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "赶快记下来……\x02",
    )

    CloseMessageWindow()

    label("loc_935F")

    TalkEnd(0x16)
    Return()

    # Function_30_8CE0 end

    def Function_31_9363(): pass

    label("Function_31_9363")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_9426")

    ChrTalk(
        0xFE,
        (
            "多亏了飞艇停航，\x01",
            "让我能够称心如意地\x01",
            "在周围抢购一番了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我丈夫都被我吓傻了吧，\x01",
            "嘿嘿嘿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9696")

    label("loc_9426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_9508")

    ChrTalk(
        0xFE,
        "好便宜啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是买了那个的话，\x01",
            "就会成为我旅途的负担了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是让他把东西送到\x01",
            "我在王都的家里吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9696")

    label("loc_9508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_95FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95B1")
    OP_A2(0x12)

    ChrTalk(
        0xFE,
        "好～接下来去哪家呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是为了今天，\x01",
            "我才和丈夫一起出来巡礼的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F7")

    label("loc_95B1")


    ChrTalk(
        0xFE,
        "好～接下来去哪家呢。\x02",
    )

    CloseMessageWindow()

    label("loc_95F7")

    Jump("loc_9696")

    label("loc_95FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_9696")

    ChrTalk(
        0xFE,
        (
            "呵呵，虽然有点对不起丈夫，\x01",
            "不过飞艇停航了还真是一件好事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话就可以\x01",
            "慢慢享受购物的乐趣了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9696")

    TalkEnd(0x18)
    Return()

    # Function_31_9363 end

    def Function_32_969A(): pass

    label("Function_32_969A")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_9854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B0")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "定期船的航运\x01",
            "终于恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这下终于可以去卢安了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到时候一定要密切注意\x01",
            "妻子的购物癖呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得人嘛，\x01",
            "还是要稍微勤俭节约一点的好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9851")

    label("loc_97B0")


    ChrTalk(
        0xFE,
        (
            "到时候一定要密切注意\x01",
            "妻子的购物癖呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得人嘛，\x01",
            "还是要稍微勤俭节约一点的好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9851")

    Jump("loc_9CC4")

    label("loc_9854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_99C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_993D")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "艾德尔那家伙又想去买东西啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "她不是刚刚才来过这家店吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "定期船的航运赶快恢复吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C4")

    label("loc_993D")


    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "艾德尔那家伙又想去买东西啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "她不是刚刚才来过这家店吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C4")

    Jump("loc_9CC4")

    label("loc_99C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_9B3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AA5")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "妻子买东西的气势\x01",
            "真是强悍啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从来了这里之后，\x01",
            "好像就在一直不停地购物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得，\x01",
            "就算再有钱也应该\x01",
            "保持勤俭节约的习惯才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B37")

    label("loc_9AA5")


    ChrTalk(
        0xFE,
        (
            "妻子买东西的气势\x01",
            "真是强悍啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得，\x01",
            "就算再有钱也应该\x01",
            "保持勤俭节约的习惯才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B37")

    Jump("loc_9CC4")

    label("loc_9B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_9CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C31")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要步行到卢安去\x01",
            "就必须要翻越山峰……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过妻子\x01",
            "肯定会反对这样做的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是这样下去\x01",
            "留在这里就会花掉更多的住宿费。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CC4")

    label("loc_9C31")


    ChrTalk(
        0xFE,
        (
            "嗯～又不能步行去卢安，\x01",
            "到底该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是这样下去\x01",
            "留在这里就会花掉更多的住宿费。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CC4")

    TalkEnd(0x17)
    Return()

    # Function_32_969A end

    def Function_33_9CC8(): pass

    label("Function_33_9CC8")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_9F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E70")
    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "在被袭击的工房\x01",
            "恢复营业之前，\x01",
            "我都会一直呆在柏斯的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "利贝尔的导力器\x01",
            "十分吸引我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是自从我来到利贝尔之后，\x01",
            "就光是在等啊等……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，商人必须学会忍耐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在还是静下心来\x01",
            "慢慢等着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F52")

    label("loc_9E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F06")
    OP_A2(0x15)

    ChrTalk(
        0xFE,
        "不过，商人必须学会忍耐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在还是静下心来\x01",
            "慢慢等着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F52")

    label("loc_9F06")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "那个工房的店主……\x01",
            "好像有点坐立不安呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F52")

    Jump("loc_A0DD")

    label("loc_9F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_A0DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A032")
    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "这就是柏斯超市吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还真是出人意料啊……\x01",
            "作为一个小国家的超市，\x01",
            "居然这么热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁谈判的空档，\x01",
            "就顺便参观一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0DD")

    label("loc_A032")


    ChrTalk(
        0xFE,
        (
            "还真是出人意料啊……\x01",
            "作为一个小国家的超市，\x01",
            "居然这么热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁谈判的空档，\x01",
            "就顺便参观一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0DD")

    TalkEnd(0x19)
    Return()

    # Function_33_9CC8 end

    def Function_34_A0E1(): pass

    label("Function_34_A0E1")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A209")
    OP_A2(0x16)

    ChrTalk(
        0xFE,
        (
            "没想到特里诺先生\x01",
            "连同飞艇一起行踪不明了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米拉诺小姐代替父亲\x01",
            "去处理了谈判工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真厉害呀……\x01",
            "但是，我很担心这样会不会累垮小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2C7")

    label("loc_A209")


    ChrTalk(
        0xFE,
        (
            "米拉诺小姐代替父亲\x01",
            "去处理了谈判工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真厉害呀……\x01",
            "但是，我很担心这样会不会累垮小姐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2C7")

    TalkEnd(0x1A)
    Return()

    # Function_34_A0E1 end

    def Function_35_A2CB(): pass

    label("Function_35_A2CB")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3F5")
    OP_A2(0x17)

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "本来想把父亲的工作委任给西蒙的，\x01",
            "不过他还差得很远呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是被博尔德大叔\x01",
            "占了上风就糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我必须得有一个助手。\x01",
            "还是把他叫上吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A47C")

    label("loc_A3F5")


    ChrTalk(
        0xFE,
        "……行商最重要就是信用第一。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算自己的业绩不好，\x01",
            "也不能连累其他人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A47C")

    TalkEnd(0x1C)
    Return()

    # Function_35_A2CB end

    def Function_36_A480(): pass

    label("Function_36_A480")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A535")
    OP_A2(0x18)

    ChrTalk(
        0xFE,
        (
            "#620F小姐就是那种自己越忙\x01",
            "就越有干劲的类型。\x02\x03",
            "#621F这可能是继承了前市长……\x01",
            "她父亲血统的原因吧。\x02\x03",
            "#620F可是，\x01",
            "我却非常担心小姐的身体状况……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5A7")

    label("loc_A535")


    ChrTalk(
        0xFE,
        (
            "#620F小姐就是那种自己越忙\x01",
            "就越有干劲的类型。\x02\x03",
            "#620F可是，\x01",
            "我却非常担心小姐的身体状况……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5A7")

    TalkEnd(0x1D)
    Return()

    # Function_36_A480 end

    def Function_37_A5AB(): pass

    label("Function_37_A5AB")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6CC")
    OP_A2(0x19)

    ChrTalk(
        0xFE,
        (
            "别看我这样，\x01",
            "我可是市长官邸的厨师呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然没办法做出\x01",
            "像安特洛丝餐厅那样高级的料理，\x01",
            "不过手艺也算可以啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小姐最近十分繁忙，\x01",
            "不知道营养能跟得上吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A733")

    label("loc_A6CC")


    ChrTalk(
        0xFE,
        (
            "小姐最近十分繁忙，\x01",
            "不知道营养能跟得上吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A733")

    TalkEnd(0x1E)
    Return()

    # Function_37_A5AB end

    def Function_38_A737(): pass

    label("Function_38_A737")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_A8B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A863")
    OP_A2(0x1A)

    ChrTalk(
        0x102,
        (
            "#010F啊，是朵洛希。\x01",
            "在干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 270, 100)
    OP_8C(0x1F, 180, 100)
    OP_8C(0x1F, 225, 100)

    ChrTalk(
        0x1F,
        (
            "#151F大家，要摆出最好的表情哦～\x02\x03",
            "好～向这边微笑一下㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F好像听不见我说话呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F嗯，是啊……\x01",
            "集中力还是那么厉害。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8B4")

    label("loc_A863")


    ChrTalk(
        0x1F,
        (
            "#150F那么……\x02\x03",
            "接下来照前辈的指示，\x01",
            "去拍一些资料用的照片吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8B4")

    Jump("loc_AAA1")

    label("loc_A8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_AAA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA14")
    OP_A2(0x1A)

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "这不是朵洛希吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1F, 90, 100)
    OP_8C(0x1F, 180, 100)
    OP_8C(0x1F, 270, 100)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)

    ChrTalk(
        0x1F,
        (
            "#151F哇～～\x01",
            "真的是什么东西都有卖的啊。\x02\x03",
            "东西太多了，\x01",
            "我都看花眼了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F好像沉浸在梦里一样，\x01",
            "完全听不到别人说话呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F啊哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAA1")

    label("loc_AA14")


    ChrTalk(
        0x1F,
        (
            "#151F哇～～\x01",
            "真的是什么东西都有卖的啊。\x02\x03",
            "东西太多了，\x01",
            "我都看花眼了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAA1")

    TalkEnd(0x1F)
    Return()

    # Function_38_A737 end

    def Function_39_AAA5(): pass

    label("Function_39_AAA5")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_AC8B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABD7")
    OP_A2(0x1B)

    ChrTalk(
        0xFE,
        (
            "我被空贼抓起来这段时间，\x01",
            "我的未婚妻卡特丽亚\x01",
            "一直打理着小店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "她把小店经营得那么好，\x01",
            "我真是没有脸面接手回来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要做我自己，\x01",
            "一切从零开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC8B")

    label("loc_ABD7")


    ChrTalk(
        0xFE,
        (
            "她把小店经营得那么好，\x01",
            "我真是没有脸面接手回来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要做我自己，\x01",
            "一切从零开始吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC8B")

    TalkEnd(0x20)
    Return()

    # Function_39_AAA5 end

    def Function_40_AC8F(): pass

    label("Function_40_AC8F")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_AD2F")

    ChrTalk(
        0xFE,
        (
            "#030F那么，\x01",
            "这就去传说中的安特洛丝餐厅看看吧。\x02\x03",
            "#035F一定得仔细品尝利贝尔料理的精髓。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADA6")

    label("loc_AD2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_ADA6")

    ChrTalk(
        0xFE,
        (
            "#030F哦～这里比想象中要繁华很多嘛。\x01",
            "有很多地方值得参观一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADA6")

    TalkEnd(0x21)
    Return()

    # Function_40_AC8F end

    def Function_41_ADAA(): pass

    label("Function_41_ADAA")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_9F(0x101, 0xC8, 0xFF, 0xFF, 0xFF, 0x0)
    OP_67(0, 9500, -10000, 0)
    SetChrPos(0x8, -84, -1000, -4656, 0)
    SetChrPos(0x9, 1100, -1000, -3970, 270)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_8C(0x1B, 135, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x16, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_AE24"),
        (103, "loc_AE6B"),
        (101, "loc_AEB2"),
        (100, "loc_AF0A"),
        (SWITCH_DEFAULT, "loc_AF62"),
    )


    label("loc_AE24")

    SetChrPos(0x134, -4819, 0, 15920, 180)
    SetChrPos(0x101, -3723, 0, 16050, 180)
    SetChrPos(0x102, -3383, 0, 17070, 180)
    SetChrPos(0x103, -5216, 0, 17120, 180)
    Jump("loc_AF62")

    label("loc_AE6B")

    SetChrPos(0x134, 11560, 0, -630, 270)
    SetChrPos(0x101, 11200, 0, 680, 270)
    SetChrPos(0x102, 11974, 0, 1065, 270)
    SetChrPos(0x103, 12448, 0, 181, 270)
    Jump("loc_AF62")

    label("loc_AEB2")

    OP_6D(-17200, 0, 1000, 0)
    SetChrPos(0x134, -19570, 0, 1459, 90)
    SetChrPos(0x101, -19730, 0, 487, 90)
    SetChrPos(0x102, -20300, 0, 1991, 90)
    SetChrPos(0x103, -20600, 0, -237, 90)
    Jump("loc_AF62")

    label("loc_AF0A")

    OP_6D(-3530, 0, -11850, 0)
    SetChrPos(0x134, -2950, 0, -15160, 0)
    SetChrPos(0x101, -4030, 0, -15400, 0)
    SetChrPos(0x102, -4400, 0, -16490, 0)
    SetChrPos(0x103, -3060, 0, -16480, 0)
    Jump("loc_AF62")

    label("loc_AF62")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#000F哇～地方好大啊。\x02\x03",
            "市长会在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#620F那么引人注目的人物，\x01",
            "应该很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x134, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x134,
        "#623F……啊，果然如我所想。\x02",
    )

    CloseMessageWindow()
    OP_69(0x1B, 0x7D0)

    NpcTalk(
        0x1B,
        "年轻女性",
        (
            "#612F我说你们，还知不知道什么叫做廉耻？\x02\x03",
            "在这么紧张的时候，\x01",
            "竟然囤积居奇、哄抬食品价格……\x02\x03",
            "柏斯商人的名誉都让你们给败坏了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "可、可是，大小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们只是为了提高柏斯超市的销售额，\x01",
            "所以才……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "年轻女性",
        (
            "#614F给我闭嘴！\x02\x03",
            "其它的商品也就不说了，\x01",
            "连生活必需品都用来牟取暴利，\x01",
            "会给我们的市场带来很坏的影响！\x02\x03",
            "赶快给我恢复原来的价格！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "好、好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我明白了……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "年轻女性",
        (
            "#615F……要知道，\x01",
            "我从来没怀疑过\x01",
            "你们对柏斯超市付出的热情。\x02\x03",
            "但是，我想让你们明白。\x01",
            "所谓的买卖就是一种建立\x01",
            "人与人之间信赖关系的过程。\x02\x03",
            "#610F不要气馁，\x01",
            "我相信你们一定能成为杰出的柏斯商人！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "大、大小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "明白，我们一定努力！\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x2A)
    OP_8C(0x1B, 90, 300)
    Sleep(3000)

    NpcTalk(
        0x1B,
        "年轻女性",
        "#610F呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        "#620F小姐……\x02",
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_B4AB"),
        (103, "loc_B4AB"),
        (101, "loc_B57F"),
        (100, "loc_B57F"),
        (SWITCH_DEFAULT, "loc_B653"),
    )


    label("loc_B4AB")

    SetChrPos(0x134, 4913, -250, 1250, 0)
    SetChrPos(0x101, 4913, -250, 1250, 0)
    SetChrPos(0x102, 4913, -250, 1250, 0)
    SetChrPos(0x103, 4913, -250, 1250, 0)
    OP_8C(0x1B, 45, 400)

    def lambda_B4FC():
        OP_6D(920, -1000, -2130, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B4FC)

    def lambda_B514():
        OP_92(0xFE, 0x1B, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x134, 1, lambda_B514)
    Sleep(400)

    def lambda_B52E():
        OP_8E(0xFE, 0x884, 0xFFFFFC18, 0xFFFFF79A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B52E)
    Sleep(400)

    def lambda_B54E():
        OP_8E(0xFE, 0x668, 0xFFFFFC18, 0xFFFFFAD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B54E)
    Sleep(400)
    OP_8E(0x103, 0xB54, 0xFFFFFC18, 0xFFFFFC18, 0xBB8, 0x0)
    Jump("loc_B653")

    label("loc_B57F")

    SetChrPos(0x134, -6440, 0, -10600, 0)
    SetChrPos(0x101, -6440, 0, -10600, 0)
    SetChrPos(0x102, -6440, 0, -10600, 0)
    SetChrPos(0x103, -6440, 0, -10600, 0)
    OP_8C(0x1B, 225, 400)

    def lambda_B5D0():
        OP_6D(-1270, -1000, -4770, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5D0)

    def lambda_B5E8():
        OP_92(0xFE, 0x1B, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x134, 1, lambda_B5E8)
    Sleep(400)

    def lambda_B602():
        OP_8E(0xFE, 0xFFFFF43E, 0xFFFFFC18, 0xFFFFEA34, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B602)
    Sleep(400)

    def lambda_B622():
        OP_8E(0xFE, 0xFFFFF740, 0xFFFFFC18, 0xFFFFE732, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B622)
    Sleep(400)
    OP_8E(0x103, 0xFFFFF3E4, 0xFFFFFC18, 0xFFFFE5DE, 0xBB8, 0x0)
    Jump("loc_B653")

    label("loc_B653")

    WaitChrThread(0x134, 0x1)

    NpcTalk(
        0x1B,
        "年轻女性",
        (
            "#610F莉拉……你来了啊。\x02\x03",
            "#617F又让你看到我丢脸的样子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x134,
        (
            "#621F不……\x01",
            "还是一如既往地表现出色啊。\x02\x03",
            "不说这个了，小姐。\x01",
            "这边几位客人有事想和您商谈。\x02\x03",
            "请您赶快回官邸吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "年轻女性",
        (
            "#610F啊，那个徽章……\x02\x03",
            "#610F难道你们就是\x01",
            "游击士协会派来的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，正是。可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F难道您就是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "年轻女性",
        (
            "#611F呵呵，请允许我先自我介绍一下。\x02\x03",
            "我的名字叫梅贝尔。\x02\x03",
            "是这座超市的拥有者，\x01",
            "也是担任柏斯地区管理职务的市长。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x20)
    OP_28(0x35, 0x1, 0x40)
    OP_28(0x35, 0x1, 0x80)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_41_ADAA end

    def Function_42_B8AF(): pass

    label("Function_42_B8AF")

    OP_8C(0xFE, 45, 400)
    OP_8E(0xFE, 0x7CB, 0xFFFFFC18, 0xFFFFF844, 0xBB8, 0x0)
    OP_8E(0xFE, 0x13B7, 0x0, 0x8C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x23B2, 0x0, 0xFFFFF31C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_B8AF end

    SaveToFile()

Try(main)
