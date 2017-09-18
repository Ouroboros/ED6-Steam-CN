from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4130   ._SN',
            'ED6_DT01/T4130_1 ._SN',
            'ED6_DT01/T4130_2 ._SN',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '奥利维尔',                             # 9
        '奈尔',                                 # 10
        '朵洛希',                               # 11
        '总编',                                 # 12
        '库拉茨',                               # 13
        '克鲁茨',                               # 14
        '科蕾蒂',                               # 15
        '彭萨',                                 # 16
        '金',                                   # 17
        '奥利维尔',                             # 18
        '米亚尔',                               # 19
        '戈万',                                 # 20
        '帕菲',                                 # 21
        '娜娜',                                 # 22
        '巴拉尔',                               # 23
        '科尼嘉',                               # 24
        '诺蒂亚',                               # 25
        '法尔茨',                               # 26
        '莎莉亚',                               # 27
        '士兵丹',                               # 28
        '士兵阿尔兹',                           # 29
        '阿加特',                               # 30
        '提妲',                                 # 31
        '拉赛尔',                               # 32
        '比尔爷爷',                             # 33
        '酒杯',                                 # 34
        '瓶子',                                 # 35
        '酒杯',                                 # 36
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH01023 ._CH',             # 03
        'ED6_DT07/CH01263 ._CH',             # 04
        'ED6_DT07/CH01623 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT06/CH20050 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01120 ._CH',             # 0B
        'ED6_DT07/CH02480 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01100 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01143 ._CH',             # 11
        'ED6_DT07/CH01540 ._CH',             # 12
        'ED6_DT07/CH01300 ._CH',             # 13
        'ED6_DT07/CH00053 ._CH',             # 14
        'ED6_DT07/CH00063 ._CH',             # 15
        'ED6_DT07/CH02023 ._CH',             # 16
        'ED6_DT06/CH20048 ._CH',             # 17
        'ED6_DT07/CH00003 ._CH',             # 18
        'ED6_DT07/CH00013 ._CH',             # 19
        'ED6_DT07/CH00033 ._CH',             # 1A
        'ED6_DT07/CH00073 ._CH',             # 1B
        'ED6_DT06/CH20045 ._CH',             # 1C
        'ED6_DT06/CH20039 ._CH',             # 1D
        'ED6_DT07/CH01490 ._CH',             # 1E
        'ED6_DT07/CH01020 ._CH',             # 1F
        'ED6_DT07/CH01043 ._CH',             # 20
        'ED6_DT07/CH01123 ._CH',             # 21
        'ED6_DT07/CH01260 ._CH',             # 22
        'ED6_DT06/CH20063 ._CH',             # 23
        'ED6_DT06/CH20021 ._CH',             # 24
        'ED6_DT06/CH20020 ._CH',             # 25
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH01023P._CP',             # 03
        'ED6_DT07/CH01263P._CP',             # 04
        'ED6_DT07/CH01623P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT06/CH20050P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01120P._CP',             # 0B
        'ED6_DT07/CH02480P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01100P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01143P._CP',             # 11
        'ED6_DT07/CH01540P._CP',             # 12
        'ED6_DT07/CH01300P._CP',             # 13
        'ED6_DT07/CH00053P._CP',             # 14
        'ED6_DT07/CH00063P._CP',             # 15
        'ED6_DT07/CH02023P._CP',             # 16
        'ED6_DT06/CH20048P._CP',             # 17
        'ED6_DT07/CH00003P._CP',             # 18
        'ED6_DT07/CH00013P._CP',             # 19
        'ED6_DT07/CH00033P._CP',             # 1A
        'ED6_DT07/CH00073P._CP',             # 1B
        'ED6_DT06/CH20045P._CP',             # 1C
        'ED6_DT06/CH20039P._CP',             # 1D
        'ED6_DT07/CH01490P._CP',             # 1E
        'ED6_DT07/CH01020P._CP',             # 1F
        'ED6_DT07/CH01043P._CP',             # 20
        'ED6_DT07/CH01123P._CP',             # 21
        'ED6_DT07/CH01260P._CP',             # 22
        'ED6_DT06/CH20063P._CP',             # 23
        'ED6_DT06/CH20021P._CP',             # 24
        'ED6_DT06/CH20020P._CP',             # 25
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 21,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -54100,
        Z                   = 200,
        Y                   = 61000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 5260,
        Z                   = 4130,
        Y                   = 2290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 23,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -2029,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3520,
        Z                   = 0,
        Y                   = -4540,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 58600,
        Z                   = 0,
        Y                   = -1690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 59980,
        Z                   = 0,
        Y                   = -1800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 197,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 65830,
        Z                   = 0,
        Y                   = -3420,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -57020,
        Z                   = 0,
        Y                   = 61110,
        Direction           = 327,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 1580,
        Z                   = 0,
        Y                   = 1800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2580,
        Z                   = 0,
        Y                   = 530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 260,
        Z                   = 4000,
        Y                   = 3770,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -4200,
        Z                   = 600,
        Y                   = -3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327716,
        ChipIndex           = 0x24,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 700,
        Y                   = -3350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835045,
        ChipIndex           = 0x25,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3320,
        Z                   = 600,
        Y                   = -3880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327716,
        ChipIndex           = 0x24,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -56840,
        TriggerZ            = 0,
        TriggerY            = 3500,
        TriggerRange        = 400,
        ActorX              = -56630,
        ActorZ              = 1500,
        ActorY              = 5500,
        Flags               = 0x7E,
        TalkScenaIndex      = 2,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_60E",          # 00, 0
        "Function_1_B35",          # 01, 1
        "Function_2_BB2",          # 02, 2
        "Function_3_BC8",          # 03, 3
        "Function_4_BEC",          # 04, 4
        "Function_5_C10",          # 05, 5
        "Function_6_C34",          # 06, 6
        "Function_7_1F86",         # 07, 7
        "Function_8_1FA6",         # 08, 8
        "Function_9_37E9",         # 09, 9
        "Function_10_4E1D",        # 0A, 10
        "Function_11_6FE7",        # 0B, 11
        "Function_12_8B7B",        # 0C, 12
        "Function_13_8DAF",        # 0D, 13
        "Function_14_8DE7",        # 0E, 14
        "Function_15_8E9D",        # 0F, 15
    )


    def Function_0_60E(): pass

    label("Function_0_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_630")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x48), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    SoundLoad(233)
    SoundLoad(137)
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_644")
    SoundLoad(190)
    SoundLoad(137)
    OP_A3(0x3FB)
    Event(0, 8)

    label("loc_644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_652")
    OP_A3(0x3FC)
    Event(0, 9)

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_66E")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 12)

    label("loc_66E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_67A"),
        (SWITCH_DEFAULT, "loc_6A3"),
    )


    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68D")
    OP_A2(0x627)
    Event(0, 10)

    label("loc_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A0")
    OP_A2(0x64E)
    Event(0, 11)

    label("loc_6A0")

    Jump("loc_6A3")

    label("loc_6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CA")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 5780, 0, 600, 0)

    label("loc_6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_789")
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 57680, 200, -5000, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 60140, 200, -4890, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5240, 4130, -410, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3800, 200, -2180, 180)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -3590, 200, -4680, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -55940, 0, 3500, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -54920, 0, 62590, 135)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_B34")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7E6")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -53520, 0, 123230, 98)
    OP_43(0x18, 0x0, 0x0, 0x2)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_B34")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_86C")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xC, 34)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -59890, 0, 120300, 180)
    OP_43(0x18, 0x0, 0x0, 0x2)
    SetChrPos(0x19, -54350, 0, 1120, 265)
    SetChrChipByIndex(0x19, 15)
    OP_43(0x19, 0x0, 0x0, 0x2)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x19, 0x10)
    Jump("loc_B34")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_914")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4100, -4760, 350)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -3400, 120, -4500, 0)
    SetChrChipByIndex(0x12, 32)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -3700, 150, -2180, 180)
    SetChrChipByIndex(0x13, 33)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 62780, 0, -3550, 162)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_B34")

    label("loc_914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_91E")
    Jump("loc_B34")

    label("loc_91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9E7")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 26)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -3590, 200, -4680, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3800, 200, -2180, 180)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x19, -54350, 0, 1120, 265)
    SetChrChipByIndex(0x19, 15)
    OP_43(0x19, 0x0, 0x0, 0x2)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x19, 0x10)
    SetChrPos(0x18, -60680, 0, 122710, 160)
    OP_43(0x18, 0x0, 0x0, 0x5)
    SetChrChipByIndex(0xB, 31)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x10)
    SetChrPos(0xB, 58490, 0, -630, 0)
    OP_43(0xB, 0x1, 0x0, 0x2)
    Jump("loc_B34")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9F1")
    Jump("loc_B34")

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A71")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 26)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -3590, 200, -4680, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x10, -3800, 200, -2180, 180)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x18, -63230, 0, 59560, 338)
    OP_43(0x18, 0x0, 0x0, 0x2)
    SetChrFlags(0x19, 0x80)
    Jump("loc_B34")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A7B")
    Jump("loc_B34")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B15")
    ClearChrFlags(0x20, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_B12")
    SetChrPos(0x8, 1490, 0, -3580, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x40)
    SetChrPos(0x11, 980, 0, -2990, 180)
    SetChrPos(0xE, 1410, -250, -4260, 8)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0x20, 1620, 0, -2610, 180)
    SetChrChipByIndex(0xF, 15)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x10)
    SetChrPos(0xF, 4059, 0, -2910, 215)
    OP_43(0xF, 0x1, 0x0, 0x2)

    label("loc_B12")

    Jump("loc_B34")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B34")
    SetChrPos(0x18, -59890, 0, 120300, 180)
    OP_43(0x18, 0x0, 0x0, 0x2)

    label("loc_B34")

    Return()

    # Function_0_60E end

    def Function_1_B35(): pass

    label("Function_1_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B68")
    OP_B1("t4130_y")
    Jump("loc_B71")

    label("loc_B68")

    OP_B1("t4130_n")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B81")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B81")

    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B95")
    Jump("loc_BB1")

    label("loc_B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_BA7")
    OP_64(0x0, 0x1)

    label("loc_BA7")

    Jump("loc_BB1")

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BB1")

    label("loc_BB1")

    Return()

    # Function_1_B35 end

    def Function_2_BB2(): pass

    label("Function_2_BB2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BC7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_BB2")

    label("loc_BC7")

    Return()

    # Function_2_BB2 end

    def Function_3_BC8(): pass

    label("Function_3_BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BEB")
    OP_8D(0xFE, 61240, -1420, 64280, -5700, 2500)
    Jump("Function_3_BC8")

    label("loc_BEB")

    Return()

    # Function_3_BC8 end

    def Function_4_BEC(): pass

    label("Function_4_BEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0F")
    OP_8D(0xFE, -57970, 64269, -56460, 57520, 3000)
    Jump("Function_4_BEC")

    label("loc_C0F")

    Return()

    # Function_4_BEC end

    def Function_5_C10(): pass

    label("Function_5_C10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C33")
    OP_8D(0xFE, -62670, 124500, -59560, 120770, 3000)
    Jump("Function_5_C10")

    label("loc_C33")

    Return()

    # Function_5_C10 end

    def Function_6_C34(): pass

    label("Function_6_C34")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(9550, 0, 2380, 0)
    OP_67(0, 10810, -10950, 0)
    OP_6B(3040, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2570, 200, 1820, 90)
    SetChrPos(0x101, 420, -250, -4920, 0)
    SetChrPos(0x102, 1640, -250, -4860, 0)
    TurnDirection(0xE, 0x8, 0)
    SetChrChipByIndex(0x8, 23)
    SetChrFlags(0x8, 0x2)
    OP_43(0x8, 0x1, 0x0, 0x7)
    OP_1F(0x64, 0x12C)
    SetChrFlags(0x8, 0x4)
    FadeToBright(1500, 0)
    OP_6D(560, 0, 1680, 5000)
    Fade(1500)
    OP_6D(1580, 3350, 420, 0)
    OP_67(0, 4250, -10000, 0)
    OP_6B(1430, 0)
    OP_6C(32000, 0)
    OP_6E(613, 0)
    OP_6D(1410, 0, 120, 3000)

    ChrTalk(
        0x101,
        (
            "#007F#2P（果然是大赖皮蛋奥利维尔啊。）\x02\x03",
            "#006F（不过，本来以为演奏家什么的\x01",
            "　只是他自称的而已……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P（听起来水平相当的高啊。）\x02\x03",
            "（自称职业演奏家这点应该是没错的吧。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#2P（嗯……\x01",
            "　我听得有点入迷了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-140, 0, 2720, 2500)
    Sleep(2500)
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x18)
    Sleep(1000)
    OP_22(0xE9, 0x0, 0x64)
    Sleep(1500)
    Fade(1000)
    SetChrFlags(0x8, 0x20)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x8, 0x1)
    SetChrChipByIndex(0x8, 26)
    ClearChrFlags(0x8, 0x2)
    TurnDirection(0x8, 0x101, 0)
    OP_0D()
    OP_1D(0xE)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#035F#5P……刚才的曲子是『琥珀之爱』。\x02\x03",
            "本来这是只能用于歌剧的间奏曲……\x01",
            "　\x02\x03",
            "#030F在此借用这首曲子，献上爱与真心的演奏， \x02\x03",
            "以把我无尽的爱，\x01",
            "毫无保留地赠与你们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC3():
        OP_6D(-1740, 0, 1730, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC3)

    def lambda_FDB():
        OP_8E(0xFE, 0xFFFFFC2C, 0x0, 0xFFFFF9DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FDB)
    Sleep(500)

    def lambda_FFB():
        OP_8E(0xFE, 0xFFFFFA38, 0x0, 0xFFFFFF1A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FFB)
    WaitChrThread(0x101, 0x1)

    def lambda_101B():
        OP_8E(0xFE, 0xFFFFF664, 0x0, 0xFFFFFF24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_101B)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#509F看来你还是老样子，\x01",
            "总是喜欢在别人面前自我陶醉……\x02\x03",
            "#007F唉……\x01",
            "本来很想感动一番的，气氛都被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很久不见了，奥利维尔。\x01",
            "原来你也来王都了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#031F当然，正如落入河中的人鱼眼泪\x01",
            "终究会到达大海一样……\x02\x03",
            "本人是为了与黑发王子再次感人地相逢\x01",
            "而千里迢迢从洛连特来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1200)
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#018F……真是一点也没变啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F啊～好了好了。\x01",
            "开玩笑也应该开够了吧。\x01",
            "还不赶找个位置招待我们坐下？\x02\x03",
            "就会装模作样，\x01",
            "一点也不会看人脸色。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)
    OP_62(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#034F艾丝蒂尔君……\x01",
            "不觉得这样说太过分了吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x101, 24)
    SetChrChipByIndex(0x102, 25)
    SetChrPos(0x8, -3600, 200, -2200, 180)
    SetChrPos(0x101, -3590, 200, -4680, 0)
    SetChrPos(0x102, -4940, 200, -4690, 0)
    OP_6D(-3340, 0, -3050, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_22(0xEA, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F喂喂，我记得你不是\x01",
            "和雪拉姐一起到洛连特去了吗？\x02\x03",
            "什么时候来王都的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F嗯……大概是一个月之前吧？\x02\x03",
            "和你们分别之后，\x01",
            "我与雪拉君在洛连特那里\x01",
            "度过了一段既美好又快活的时光。\x02\x03",
            "#034F可是……\x01",
            "我到底是个漂泊的诗人兼演奏家……\x02\x03",
            "最终还是狠心拒绝了雪拉君含泪的挽留，\x01",
            "漂流到这美丽的王都来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F该怎么说呢……\x01",
            "真是让人无法相信的解释啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F肯定是每天晚上被雪拉姐强迫灌酒，\x01",
            "结果实在忍受不了而逃出来了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x8,
        "#033F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F难道说……\x01",
            "是和爱娜姐姐一起喝酒吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#505F对了，\x01",
            "奥利维尔还不认识爱娜姐姐吧？\x02\x03",
            "她是雪拉姐的朋友，\x01",
            "洛连特支部的负责人。\x02\x03",
            "据说她的酒量比雪拉姐还要高……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#031F……哈哈哈，\x01",
            "真讨厌啊，艾丝蒂尔君。\x02\x03",
            "叫·这个·名字的人·\x01",
            "我·没有·见过，也·没有·听说过哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F你的声音完全把你给出卖了呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F艾丝蒂尔……\x01",
            "就这样放过他吧。\x02\x03",
            "#015F我想他一定是遇到了悲惨……\x01",
            "不，应该是非常悲惨的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#034F呜呜，没想到还有比雪拉君酒量更高的，\x01",
            "简直是无底洞……\x02\x03",
            "……啊啊啊…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#036F#3S不～要～再带着那迷人的微笑\x01",
            "给我灌酒啦～！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F回、回忆重现！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F着实沉醉于爱娜小姐的最强传说中呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#034F呼呼呼……\x01",
            "唉，这个就先别提了。\x02\x03",
            "#030F你们两个不是走遍其他地方，\x01",
            "然后来到王都了吗？\x02\x03",
            "都遇到过什么有趣的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯，这可是短时间内\x01",
            "没办法说清楚的……\x02\x03",
            "#000F而且我们现在正在找人，\x01",
            "下次见面的时候再说好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#033F哎……\x01",
            "你们是在找谁啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F一位名叫『金』的从卡尔瓦德共和国来的\x01",
            "武术家游击士。\x01",
            "　\x02\x03",
            "据说他经常来酒廊，\x01",
            "奥利维尔，你有没有见过呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F啊啊！\x01",
            "那个像熊一样高大的老兄啊。\x02\x03",
            "以前见过很多次，\x01",
            "不过今天还没有看见他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是吗……\x01",
            "今天没有来酒馆吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF6")

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "在共和国大使馆那边的可能性就很高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035F呵呵……\x01",
            "那我们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F66")

    label("loc_1EF6")


    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "在艾尔贝周游道那边的可能性就很高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035F呵呵……\x01",
            "那我们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F66")

    OP_A2(0x613)
    OP_28(0x46, 0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_C34 end

    def Function_7_1F86(): pass

    label("Function_7_1F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    OP_48()
    Jump("Function_7_1F86")

    label("loc_1F9B")

    Sleep(50)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_1F86 end

    def Function_8_1FA6(): pass

    label("Function_8_1FA6")

    EventBegin(0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x108, -3800, 0, -2180, 180)
    SetChrPos(0x101, -3590, 200, -4680, 0)
    SetChrPos(0x102, -4940, 200, -4690, 0)
    SetChrPos(0x8, -4500, 2000, 4700, 225)
    SetChrChipByIndex(0x8, 28)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xE, 4620, 0, 2500, 180)
    OP_6D(-3340, 0, -3050, 0)
    OP_22(0xEA, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrChipByIndex(0x101, 24)
    SetChrChipByIndex(0x102, 25)
    SetChrChipByIndex(0x108, 27)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x108,
        (
            "#070F……原来如此，是这样啊。\x02\x03",
            "我问你们一件事，\x01",
            "为什么要参加武术大会呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯……看过预选赛之后，\x01",
            "觉得自己身体已经按耐不住了。\x02\x03",
            "所以情不自禁地想要\x01",
            "和强大的对手大战一场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们现在以成为正游击士为目标\x01",
            "在王国各地修炼旅行。\x02\x03",
            "所以想借此机会\x01",
            "测试一下至今为止的修行成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F嗯……\x02\x03",
            "#070F可以啊。我们一起组队吧。\x01",
            "　\x02\x03",
            "在明天大会开始之前，\x01",
            "去竞技场的售票处报名就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F太好了～㈱\x02\x03",
            "#004F……嗯，\x01",
            "这么痛快地就答应，没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F你们俩的实力，我之前已见识过了。\x01",
            "　\x02\x03",
            "作为协助我的人已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿……\x01",
            "谢谢，金先生！\x02\x03",
            "我会尽全力以赴的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F彼此彼此。\x02\x03",
            "#074F不过，本来是打算挑战一下，\x01",
            "只靠一个人能够到达什么程度的……\x02\x03",
            "现在既然有了协助的人，\x01",
            "那就不能不想到要拿冠军了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F那当然了！\x01",
            "既然参加就要拿冠军！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F不过，如果这样打算的话，\x01",
            "还缺少一个人的我们还是很难办到的。\x02\x03",
            "团体赛的人数是四个啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F啊，是啊……\x01",
            "还缺少一个人呢。\x02\x03",
            "#001F不管怎么样，\x01",
            "只要鼓足干劲全力以赴就行了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F不，如果目标提高的话，\x01",
            "就要做好万全的准备。\x02\x03",
            "作战在拳脚相加之前就应该开始了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……确实是这样啊。\x02\x03",
            "这个时候，\x01",
            "如果雪拉姐在就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#006F对了，不如我们去拜托艾南哥哥\x01",
            "联络一下洛连特支部吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)

    ChrTalk(
        0x102,
        (
            "#017F嗯……\x01",
            "但是雪拉姐姐一定会很忙的。\x02\x03",
            "父亲和我们都不在，\x01",
            "洛连特支部正人手不足呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F是……是这样没错。\x02\x03",
            "#504F啊～真是的，不管是谁都好，\x01",
            "有没有能帮我们的人啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x46, 0x190)
    Sleep(400)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(2000)

    NpcTalk(
        0x8,
        "青年的声音",
        (
            "#4P呵呵……\x01",
            "我就是在等这句话。\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x64, 0x190)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x108, 2)
    OP_66(0x0)
    OP_6D(-2690, 0, 2590, 2500)

    ChrTalk(
        0x101,
        (
            "#509F果然出现了～\x01",
            "这个不要脸的赖皮演奏家。\x02\x03",
            "不会一直在二楼潜伏着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道……\x01",
            "刚才的话你都听见了？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 29)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x3, 0x7D0)
    Sleep(200)
    OP_99(0x8, 0x3, 0xA, 0x5DC)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#035F哈·哈·哈……\x01",
            "一字不漏地全都听见了。\x02\x03",
            "于是我就想『这次轮到我出场了』。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)

    def lambda_2A5A():
        OP_6D(-4170, 0, -2650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5A)
    OP_8E(0x8, 0xFFFFED2C, 0x0, 0x3DE, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xFFFFF92A, 0xBB8, 0x0)
    SetChrChipByIndex(0x8, 26)
    OP_96(0x8, 0xFFFFEC64, 0xC8, 0xFFFFF722, 0x258, 0x1388)
    OP_22(0xD1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    ChrTalk(
        0x101,
        (
            "#009F喂，等一下！\x01",
            "怎么这么随便就坐下来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F这不是弹钢琴的那个演奏家小哥嘛。\x01",
            "　\x02\x03",
            "是你们的熟人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F该说是熟人呢，还是缘分的捉弄呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F……还没有达到熟人这种程度吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#030F本人是奥利维尔·朗海姆。\x01",
            "来自埃雷波尼亚的旅行演奏家。\x02\x03",
            "和艾丝蒂尔君、约修亚君\x01",
            "是在之前的事件中认识的。\x02\x03",
            "#031F自那以后，我们的关系变得很不一般呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#582F请不要使用容易引起误会的方式说话！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，虽然不知道是怎么回事，\x01",
            "不过我也来报个名字吧。\x02\x03",
            "金·瓦赛克——\x01",
            "来自卡尔瓦德共和国的游击士，\x01",
            "以武侠之道为志向的武术家。\x02\x03",
            "你的钢琴演奏我一直很欣赏呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035F呵呵……\x01",
            "能得到夸奖真是光荣至极。\x02\x03",
            "#030F本人也听说了，\x01",
            "你在武术大会预选赛中的武勇事迹。\x02\x03",
            "面对四个对手，\x01",
            "只凭借一个人就获得压倒性胜利对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F遇到新手作为对手，只是运气好罢了。\x02\x03",
            "对了，不知道这位演奏家先生\x01",
            "找我们到底有什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#3S给我等一下～～！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F奥利维尔……\x01",
            "我想确认一件事……\x02\x03",
            "难道最近你没有事情可做吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)

    ChrTalk(
        0x8,
        (
            "#033F不愧是约修亚君，\x01",
            "这个问题还真是尖锐啊。\x02\x03",
            "#034F来到王都的这一个月……\x02\x03",
            "观光游览一遍之后，\x01",
            "只剩王城因为有士兵把守而无法进入。\x01",
            "　\x02\x03",
            "本想去别的地方看看，\x01",
            "可女王的诞辰庆典又快要到了，\x01",
            "现在还舍不得离开这个美丽的王都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F总之，就是很闲是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F不过嘛，然后突然听到了\x01",
            "你们『缺少一个队员』的谈话……\x02\x03",
            "而且最重要的是，\x01",
            "优胜者会得到豪华晚宴的款待……\x02\x03",
            "#031F简直是女神的启示！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F我就知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F就是这个原因，\x01",
            "能不能让我也成为参加武术大会的伙伴呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F为什么不呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F等、等一下金先生。\x01",
            "这么简单就让这家伙……\x02\x03",
            "你还不知道奥利维尔的战斗方法吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F他擅长的是导力枪对吗？\x02\x03",
            "这样可以采取广泛的战术，\x01",
            "我觉得能组成很好的队伍呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 1)

    ChrTalk(
        0x101,
        "#004F哎～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#033F这真是……让人吃惊啊。\x02\x03",
            "请问你是不是从腰间的鼓起\x01",
            "和走路的方式判断出来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F还有视线移动的方式。\x02\x03",
            "武术家和剑士捕捉移动的目标时\x01",
            "视线是沿着线移动的……\x02\x03",
            "而你对别人行动的把握\x01",
            "都是集中在一个一个点上的。\x02\x03",
            "这是使枪的人移动视线的特殊之处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F嘿哎，真是专业啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F原来如此……\x01",
            "确实非常有道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#035F嗯……\x01",
            "今后我要注意一点了。\x02\x03",
            "#030F那么，在你这位高手的眼光看来，\x01",
            "我已经算合格了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#071F啊，请多关照啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "虽然感觉有点不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F总之比赛时候请多多指教了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1FA6 end

    def Function_9_37E9(): pass

    label("Function_9_37E9")

    EventBegin(0x0)
    OP_6D(59950, 0, -3760, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, 59950, 0, -5070, 270)
    SetChrPos(0x101, 58770, 0, -3810, 180)
    SetChrPos(0x102, 58750, 0, -5890, 0)
    ClearChrFlags(0x9, 0x80)

    ChrTalk(
        0x101,
        (
            "#000F哈～虽然有点辣，\x01",
            "不过很好吃呢㈱\x02\x03",
            "香脆的里脊肉\x01",
            "和松软的蒸土豆，\x01",
            "真的是绝配呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F饭后的咖啡也是一级棒呢。\x02\x03",
            "虽然听说过用玻璃器具泡咖啡\x01",
            "有相当的难度……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F真是的，花别人的钱，\x01",
            "就可以这么狼吞虎咽的吃……\x02\x03",
            "以为记者那点可怜的工资能干什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F好啦好啦。\x01",
            "总之谢谢你招待我们啦。\x02\x03",
            "对了……\x01",
            "你果然在为新闻素材伤脑筋吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F哼……\x01",
            "新闻素材要多少有多少。\x02\x03",
            "不过，都是些关于亲卫队的恐怖活动、\x01",
            "女王身体欠佳之类的，\x01",
            "没有什么可信度的消息。\x02\x03",
            "明确地说，\x01",
            "我想要的是没有经过军队过滤的，\x01",
            "新鲜的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F我从朵洛希那里听说了一些\x01",
            "关于蔡斯发生的绑架事件的消息……\x02\x03",
            "就开门见山地说吧。\x02\x03",
            "你们对理查德上校\x01",
            "到底调查到什么程度了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……该怎么说呢，真是一针见血啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F能提出这样的问题，\x01",
            "应该已经有所推测了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F果然上校就是幕后黑手啊……\x02\x03",
            "我们杂志还因采访过他\x01",
            "而人气大大增长呢，\x01",
            "真是不想接受这个现实啊……\x02\x03",
            "反叛者马上就要有所行动了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F现在是否对女王陛下\x01",
            "有反叛企图，我们还不知道。\x02\x03",
            "但是，他们把杜南公爵作为傀儡，\x01",
            "在暗地企图什么是可以肯定的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F杜南公爵吗……\x02\x03",
            "趁着陛下身体欠佳，\x01",
            "把自己当成格兰赛尔城的主人，\x01",
            "肆意妄为……\x02\x03",
            "不可思议的是，\x01",
            "军队的高官为什么听之任之呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唉，那个是因为……\x02\x03",
            "……喂，约修亚。\x01",
            "这个可以说出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是呀……\x01",
            "我们也要尽可能地\x01",
            "收集相关的情报啊。\x02\x03",
            "如果是奈尔先生的话，\x01",
            "一定能帮助我们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F喂喂，怎么了。\x01",
            "你们果然知道些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我事先说好……\x02\x03",
            "接下来要说的事情，\x01",
            "是不能作为报道写出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F也就是说，先要做好心理准备。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F可恶……\x01",
            "这不是很糟糕的事情吗。\x02\x03",
            "算了，赶快说吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    FadeToBright(2000, 0)

    ChrTalk(
        0x9,
        (
            "#140F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊～\x01",
            "所以我说要做好心理准备嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F这怎么可能……\x02\x03",
            "喂……这是千真万确的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然很遗憾，不过事实就是这样。\x02\x03",
            "空贼事件、孤儿院纵火事件，\x01",
            "都是特务兵在背后操纵……\x02\x03",
            "绑架并且监禁王国第一的\x01",
            "天才科学家拉赛尔博士……\x02\x03",
            "军队上层被抓住了弱点，\x01",
            "摩尔根将军也被监禁……\x02\x03",
            "自导自演的恐怖事件，\x01",
            "并且伪装成亲卫队所为……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F啊啊～真是的！\x01",
            "怎么又是这样！\x02\x03",
            "可恶……\x01",
            "这怎么能写成报道呢。\x02\x03",
            "最近我们杂志，\x01",
            "也要受军队的检查……\x02\x03",
            "印刷的时候肯定会被拦下来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F没办法，\x01",
            "只好勉强报道一下\x01",
            "没什么关系的武术大会了……\x02\x03",
            "……啊，对了。\x02\x03",
            "你们会参加武术大会，\x01",
            "也是有什么理由的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，没错。\x02\x03",
            "虽然和委托的内容有关，\x01",
            "不能告诉你详细情况……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F知道是为了打开目前的局面\x01",
            "所采取的行动就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F是吗……\x02\x03",
            "………………………………\x02\x03",
            "……好，我决定了。\x02\x03",
            "虽然作为记者不能够做什么……\x01",
            "不过，我也来帮你们忙吧。\x02\x03",
            "游击士协会调查不到的事情，\x01",
            "就由我通过私人的途径来调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FＴｈａｎｋ　ｙｏｕ，真是帮大忙了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对手可是军队啊，\x01",
            "这件事情太危险了。\x02\x03",
            "即使这样，你也愿意帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F真啰嗦，这是我的战斗。\x02\x03",
            "作为记者，\x01",
            "我怎么能眼睁睁地看着笔输给剑呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F奈尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我明白了……\x01",
            "无论如何拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F哦，就交给我吧。\x02\x03",
            "那么，具体地来说\x01",
            "你们想知道什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这个嘛……\x01",
            "应该是军队的动向吧。\x02\x03",
            "难道他们已经\x01",
            "是不是都被逮捕了……\x02\x03",
            "摩尔根将军\x01",
            "被囚禁在哪里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F知道了，\x01",
            "我会多加注意的。\x02\x03",
            "只是调查这些事情……\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……那个……\x02\x03",
            "情报部成员的经历，\x01",
            "能调查一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#140F经历吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说具体一点，就是作为核心的\x01",
            "理查德上校、凯诺娜上尉，\x01",
            "以及洛伦斯少尉这三个人。\x02\x03",
            "因为以后要和他们对决，\x01",
            "所以想知道他们的一些详细经历……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F你的意思是，\x01",
            "『知己知彼，百战不殆』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没错，除了上校，\x01",
            "那个少尉的事情也想知道得更多一些。\x02\x03",
            "明天或者后天的比赛中\x01",
            "说不定会和他们遭遇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F奈尔先生，这件事拜托你行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F……我在军队里认识不少人。\x02\x03",
            "机密情报先不说，\x01",
            "如果是单纯的简历的话，\x01",
            "说不定能弄到手。\x02\x03",
            "好吧，我就试试看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FＴｈａｎｋ　ｙｏｕ，真是太感谢了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F哎呀，没什么大不了的啦。\x02\x03",
            "不过相对的，你们如果取得优胜，\x01",
            "被招待进格兰赛尔城的话，\x01",
            "一定要把事情都告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F果然是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F明白了。\x01",
            "只要是能说出来的都会告诉你的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "和奈尔道别之后，\x01",
            "艾丝蒂尔他们\x01",
            "回到了旅馆自己的房间。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "因为比赛的紧张和疲劳，\x01",
            "两个人早早地就休息了……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然后，第二天早晨——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_37E9 end

    def Function_10_4E1D(): pass

    label("Function_10_4E1D")

    EventBegin(0x0)
    OP_6D(-60260, 0, 66930, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, -56660, 0, 64750, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -61900, 0, 67420, 135)
    SetChrPos(0x102, -63460, 0, 66810, 135)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#006F喂～奈尔。\x02",
    )

    CloseMessageWindow()

    def lambda_4EBC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4EBC)

    ChrTalk(
        0x102,
        "#010F打扰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F……哦哦，终于来了。\x02\x03",
            "朵洛希那家伙，\x01",
            "传话难得能成功一次呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F66():
        OP_6D(-57890, 0, 65099, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F66)

    def lambda_4F7E():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4F7E)

    def lambda_4F8E():

        label("loc_4F8E")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4F8E")

    QueueWorkItem2(0x101, 1, lambda_4F8E)

    def lambda_4F9F():
        OP_8E(0xFE, 0xFFFF18F2, 0x0, 0xFC94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F9F)
    OP_8E(0x102, 0xFFFF1370, 0x0, 0x1046E, 0xBB8, 0x0)

    def lambda_4FCE():
        OP_8E(0xFE, 0xFFFF1F6E, 0x0, 0xFB9A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4FCE)
    OP_8E(0x102, 0xFFFF13B6, 0x0, 0xFC30, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFF1A28, 0x0, 0xF988, 0xBB8, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "#141F对了，今天你们也赢了吧。\x01",
            "　\x02\x03",
            "朵洛希那家伙，\x01",
            "回来的时候兴高采烈的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嘿嘿，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那么奈尔先生，\x01",
            "关于您调查的那些事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#143F哦，真是开门见山啊。\x02\x03",
            "#140F给你……\x01",
            "主要成员的简历都收集到了呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "奈尔拿出一本黑色封皮的文件夹。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F这是……王国军的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F啊，虽然机密度不是很高，\x01",
            "不过也不是随便就能拿出来的文件呢。\x02\x03",
            "好不容易说服军队中的熟人才借来的，\x01",
            "总之你们千万不要往外透露啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#06F那么，我们就在这里看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    OP_20(0x5DC)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "翻看着那本黑色封皮的文件夹。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0x22)
    FadeToDark(1500, 0, -56)
    OP_0D()
    Sleep(500)

    label("loc_530D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DA7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5395")

    Menu(
        0,
        10,
        10,
        0,
        (
            "【关于理查德上校】\x01",      # 0
            "【凯诺娜上尉】\x01",          # 1
            "【洛伦斯少尉】\x01",          # 2
            "【关闭文件】\x01",            # 3
        )
    )

    Jump("loc_53DC")

    label("loc_5395")


    Menu(
        0,
        10,
        10,
        0,
        (
            "【关于理查德上校】\x01",      # 0
            "【凯诺娜上尉】\x01",          # 1
            "【洛伦斯少尉】\x01",          # 2
        )
    )


    label("loc_53DC")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5406"),
        (1, "loc_57BB"),
        (2, "loc_5A9C"),
        (3, "loc_5D94"),
        (SWITCH_DEFAULT, "loc_5DA4"),
    )


    label("loc_5406")

    OP_AD(0x40034, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亚兰·理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１６８年，\x01",
            "生于利贝尔王国卢安地区。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "作为士官学校的主席毕业之后，\x01",
            "编入了卡西乌斯·布莱特上校率领的\x01",
            "独立机动部队。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１１９２年的百日战役中，\x01",
            "作为卡西乌斯上校的部下\x01",
            "在反攻作战中屡立战功。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡西乌斯上校退役之后，\x01",
            "被提拔为军队作战中心的成员，\x01",
            "在组织改革中建立了很多功绩。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１２０１年，作出了设立情报部的提案。\x01",
            "之后获得了艾莉茜雅女王的承认，\x01",
            "就任情报部首任指挥官。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AE")
    OP_A2(0x673)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#007F该怎么说呢……\x01",
            "这就是所谓的精英吧。\x02\x03",
            "他可是主席呢，主席。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#012F确实是个很厉害的人物。\x02\x03",
            "希德少校说得没错，\x01",
            "十年前战争的时候他确实是父亲的部下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#505F嗯，老爸真的当过上校呢……\x01",
            "　\x02\x03",
            "明明这么了不起，\x01",
            "为什么要辞掉呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_57AE")

    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_5DA4")

    label("loc_57BB")

    OP_AD(0x40035, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "凯诺娜·亚马尔迪亚上尉。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１７５年，\x01",
            "生于利贝尔王国王都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "以优秀的成绩从士官学校毕业之后，\x01",
            "被提拔为军队作战中心的成员。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１２０１年，在情报部设立的同时，\x01",
            "得到理查德上校的提拔并被调到了情报部。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，作为理查德上校的副官，\x01",
            "担当辅佐其进行作战指挥的工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A8F")
    OP_A2(0x674)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#509F『以优秀的成绩毕业』，\x01",
            "看起来又是一个精英呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#015F自从担任军官以来，\x01",
            "她好像一直在理查德上校手下做事。\x01",
            "　\x02\x03",
            "真是相当地忠诚呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5A8F")

    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_5DA4")

    label("loc_5A9C")

    OP_AD(0x40036, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "洛伦斯·博格少尉。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "年龄、国籍不明。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "原属佣兵部队『杰斯塔猎兵团』，\x01",
            "应理查德上校的征召\x01",
            "成为情报部的一员。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这之前的经历不明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D87")
    OP_A2(0x675)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#580F那个戴面具的家伙……\x01",
            "不是利贝尔人啊。\x02\x03",
            "而且没有记载他作为原佣兵时的经历，\x01",
            "……这是怎么一回事啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#013F……不知道。\x02\x03",
            "所谓『猎兵团』，\x01",
            "是只有最高级别的佣兵部队\x01",
            "才能获得的特殊称号……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(
        (
            "#505F哎～是这样啊。\x02\x03",
            "是不是因为战斗能力很强，\x01",
            "所以才得到上校提拔的？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#015F嗯……说不定。\x02\x03",
            "『杰斯塔猎兵团』……\x01",
            "这个名字好像在哪里听说过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5D87")

    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_5DA4")

    label("loc_5D94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_5DA4")

    label("loc_5DA4")

    Jump("loc_530D")

    label("loc_5DA7")

    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F谢谢你，奈尔。\x01",
            "不管怎么说，能看清敌人的底细了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F能帮上忙就再好不过了。\x02\x03",
            "我在调查资料的时候，\x01",
            "也发现了很多有趣的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#014F有趣的事情是指……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F比如，现在被通缉的\x01",
            "亲卫队队长的尤莉亚中尉……\x02\x03",
            "在士官学校就读的时候，\x01",
            "是和凯诺娜上尉是同一年级的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎～是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F不过看起来，\x01",
            "那两个人的关系好像不是很好呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F不管怎么说，\x01",
            "她们是互相竞争主席职位的对手。\x02\x03",
            "文有凯诺娜，武有尤莉亚，\x01",
            "两个人真是很好的对照呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "我大概能想象出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F一看到尤莉亚中尉威风凛凛的英姿，\x01",
            "我就觉得她好像过去的骑士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F还有……\x01",
            "虽然这个和军队没有关系。\x02\x03",
            "你们听说过\x01",
            "『科洛蒂娅公主』这个名字吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F科洛蒂娅公主……\x01",
            "好像在哪里听说过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我记得，是在海难事故中去世的\x01",
            "王太子夫妻的遗孤吧。\x02\x03",
            "是女王陛下的孙女……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F嗯，虽然不太有名，\x01",
            "不过可是直系中的直系呢。\x02\x03",
            "她好像一直生活在\x01",
            "格兰赛尔城的女王宫里……\x02\x03",
            "而且，好像某个人物正在寻找\x01",
            "那位公主殿下的相亲对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F相亲对象啊……\x02\x03",
            "虽然对大户人家来说，\x01",
            "不是什么新鲜事……\x02\x03",
            "#003F不过觉得公主有点可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，重点不在那里吧。\x02\x03",
            "#012F应该注意的字眼是『某个人物』吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#141F呵呵，真是敏锐啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎，那个人难道是……\x02",
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
            "【艾莉茜雅女王】\x01",      # 0
            "【杜南公爵】\x01",          # 1
            "【理查德上校】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6473"),
        (1, "loc_656E"),
        (2, "loc_6683"),
        (SWITCH_DEFAULT, "loc_6789"),
    )


    label("loc_6473")


    ChrTalk(
        0x9,
        (
            "#142F啊，名义上是的。\x02\x03",
            "不过实际上，\x01",
            "派人去外国寻找合适的对象的人，\x01",
            "正是那个理查德上校呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F是、是这样啊……\x02\x03",
            "#505F但是……这不是很奇怪吗？\x02\x03",
            "为什么会是理查德上校\x01",
            "来寻找公主的结婚对象呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6789")

    label("loc_656E")


    ChrTalk(
        0x9,
        (
            "#142F没错。\x02\x03",
            "不过实际上，\x01",
            "派人去外国寻找合适的对象的人，\x01",
            "正是那个理查德上校呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F是、是这样啊……\x02\x03",
            "#505F但是……这不是很奇怪吗？\x02\x03",
            "为什么会是理查德上校\x01",
            "来寻找公主的结婚对象呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x45, 0x1)
    Jump("loc_6789")

    label("loc_6683")


    ChrTalk(
        0x9,
        (
            "#141F哦，还真是聪明啊。\x02\x03",
            "其实实际上，\x01",
            "派人去外国寻找合适的对象的人，\x01",
            "正是那个理查德上校呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F果然……\x02\x03",
            "#505F但是……这不是很奇怪吗？\x02\x03",
            "为什么会是理查德上校\x01",
            "来寻找公主的结婚对象呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x45, 0x2)
    Jump("loc_6789")

    label("loc_6789")


    ChrTalk(
        0x9,
        (
            "#141F所以我说，\x01",
            "到处充满了可疑的气味呢。\x02\x03",
            "正因如此……\x01",
            "有件事情想拜托你们。\x02",
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
        (
            "#015F——如果明天的比赛能获胜，\x01",
            "被招待进王城参加晚餐的话，\x01",
            "打听一下这方面的情报。\x02\x03",
            "#010F是这样没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F啊，是这样啊……\x02\x03",
            "#007F算了，反正你也挺大方地\x01",
            "告诉了我们很多消息……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F我只是做了自己力所能及的事情罢了。\x01",
            "总之，有来有往也是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F确实帮了我们很多忙呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F没办法呢～\x01",
            "如果知道了什么，就告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#147F嘿嘿，早这样说不就好了。\x02\x03",
            "#141F不过，就算不拜托你们，\x01",
            "运气好的话今天也能……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xC3, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -55170, 2000, 64580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#143F哦……\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 90, 400)

    def lambda_6AAD():
        OP_6D(-56140, 0, 65099, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6AAD)
    OP_8E(0x9, 0xFFFF24D2, 0x0, 0xFA13, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF290A, 0x0, 0xFA13, 0xBB8, 0x0)
    OP_8C(0x9, 0, 400)
    Sleep(500)
    WaitChrThread(0x9, 0x1)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x1, 0xFF, -55170, 2000, 64580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#140F喂。\x01",
            "这里是利贝尔通讯社……\x02\x03",
            "#147F哦，是你啊！\x01",
            "我一直在等你的联络呢。\x02\x03",
            "#143F什么……现在就？\x02\x03",
            "#141F啊，知道了。\x01",
            "我立刻过去找你。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#501F怎么，发生什么事情了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    def lambda_6C20():
        OP_6D(-57890, 0, 65099, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C20)
    OP_8E(0x9, 0xFFFF2676, 0x0, 0xFA13, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF1F6E, 0x0, 0xFB9A, 0x7D0, 0x0)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        (
            "#141F稍微有点私事。\x01",
            "现在要去和别人会面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F很重要的事吗？\x01",
            "现在的天色已经这么黑了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F本来我就是个夜猫子啊。\x02\x03",
            "因为要带那个\x01",
            "我行我素的丫头进行新人研修，\x01",
            "才不得不把生物钟调整回来了……\x02\x03",
            "#142F唉，不说这件事情了。\x02\x03",
            "我要出去了，\x01",
            "你们接着干你们的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，我知道了。\x02\x03",
            "要加油工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F你们也是。\x01",
            "明天的比赛一定不能输啊！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E2B():

        label("loc_6E2B")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6E2B")

    QueueWorkItem2(0x101, 1, lambda_6E2B)

    def lambda_6E3C():

        label("loc_6E3C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6E3C")

    QueueWorkItem2(0x102, 1, lambda_6E3C)

    def lambda_6E4D():
        OP_6D(-59840, 0, 65099, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6E4D)
    OP_8E(0x9, 0xFFFF1B9A, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1564, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1258, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF0736, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_8E(0x9, 0xFFFF0736, 0xFFFFF74A, 0xF406, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x102, 0xFF)
    WaitChrThread(0x9, 0x1)
    OP_20(0x5DC)

    def lambda_6EE0():
        OP_6D(-57890, 0, 65099, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6EE0)
    WaitChrThread(0x9, 0x1)
    OP_21()
    OP_1D(0xE)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#5P接下来……\x01",
            "我们该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "总之，先顺路去协会，\x01",
            "然后就回酒店休息吧。\x02\x03",
            "最好把奈尔先生调查到的情报\x01",
            "向协会报告一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x48, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_10_4E1D end

    def Function_11_6FE7(): pass

    label("Function_11_6FE7")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -56250, 0, 60940, 90)
    SetChrPos(0x101, -60190, 0, 65280, 135)
    SetChrPos(0x102, -61190, 0, 64849, 135)
    SetChrPos(0x108, -60700, 0, 66190, 135)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    OP_4A(0xA, 255)
    OP_6D(-54490, 0, 61730, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#152F主编，真的好奇怪呢～\x02\x03",
            "已经两天没有取得联络了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "嗯，我想那家伙\x01",
            "肯定是沉浸在寻找\x01",
            "独家新闻的美梦当中了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但是，在这个戒严时期\x01",
            "不能取得联系的确有些奇怪……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "哦……\x02",
    )

    CloseMessageWindow()

    def lambda_71B7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_71B7)
    OP_6D(-56640, 0, 63970, 1500)

    ChrTalk(
        0xA,
        "#151F啊，小艾你们来了啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P你好，朵洛希。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#5P打扰了。\x02",
    )

    CloseMessageWindow()

    def lambda_7225():

        label("loc_7225")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_7225")

    QueueWorkItem2(0xA, 1, lambda_7225)

    def lambda_7236():

        label("loc_7236")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7236")

    QueueWorkItem2(0x101, 1, lambda_7236)

    def lambda_7247():

        label("loc_7247")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_7247")

    QueueWorkItem2(0x102, 1, lambda_7247)

    def lambda_7258():
        OP_6D(-55080, 0, 62180, 2000)
        ExitThread()

    QueueWorkItem(0x108, 3, lambda_7258)

    def lambda_7270():
        OP_8E(0xFE, 0xFFFF2AF4, 0x0, 0xF532, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7270)
    Sleep(300)

    def lambda_7290():
        OP_8E(0xFE, 0xFFFF25F4, 0x0, 0xF4A6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7290)
    Sleep(300)
    OP_8E(0x108, 0xFFFF16E0, 0x0, 0xFC57, 0xBB8, 0x0)

    def lambda_72C4():
        OP_8E(0xFE, 0xFFFF277A, 0x0, 0xF9F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_72C4)
    WaitChrThread(0x108, 0x2)
    OP_8C(0x108, 180, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74BB")
    OP_A2(0x67F)

    ChrTalk(
        0xB,
        "哦，武术大会的优胜者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "先自我介绍一下，\x01",
            "我是《利贝尔通讯》的主编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们二位是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#5P啊，您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5P初次见面。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "话说回来，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，是的，可以这么说……\x02",
    )

    CloseMessageWindow()
    Jump("loc_753B")

    label("loc_74BB")


    ChrTalk(
        0xB,
        (
            "是你们啊……\x01",
            "你们可总算来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F您好，打扰了～\x02\x03",
            "我们是来找奈尔的，\x01",
            "难道他出去了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_753B")


    ChrTalk(
        0xB,
        (
            "我们刚才正在\x01",
            "谈起这件事请呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "事实上奈尔他昨天和今天\x01",
            "都没有到编辑部来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "完全不能和他取得联络。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F昨天和今天都……\x02\x03",
            "我们前天傍晚还在这里和奈尔先生\x01",
            "商讨一些事情……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        "#153F真、真的吗～！？\x02",
    )

    CloseMessageWindow()

    def lambda_7658():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7658)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#007F什么真的假的啊，\x01",
            "给奈尔捎口信的不就是朵洛希你吗。\x02\x03",
            "#002F半决赛之后，\x01",
            "让我们到这里来向他打听情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#151F啊～我想起来了，\x01",
            "就～是那件事情～啊。\x02\x03",
            "#154F请问请问～\x01",
            "奈尔前辈那时是怎么说的呢～？\x02\x03",
            "他到哪里去了呢～？\x02",
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
            "【去收集新闻了】\x01",        # 0
            "【有人叫他出去】\x01",        # 1
            "【一起去吃晚餐了】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_781F"),
        (1, "loc_78D6"),
        (2, "loc_7944"),
        (SWITCH_DEFAULT, "loc_79E3"),
    )


    label("loc_781F")


    ChrTalk(
        0x102,
        (
            "#012F很有可能是到外面收集新闻了……\x01",
            "　\x02\x03",
            "准确地说，当时有人发联络叫他出去，\x01",
            "于是他就到什么地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，的确是那样的呢。\x02",
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x1)
    Jump("loc_79E3")

    label("loc_78D6")


    ChrTalk(
        0x102,
        (
            "#012F嗯，没错。\x02\x03",
            "当时有人发联络叫他出去，\x01",
            "于是他就不知道到什么地方去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x2)
    Jump("loc_79E3")

    label("loc_7944")


    ChrTalk(
        0x102,
        (
            "#017F不，那是三天前的事情了。\x02\x03",
            "#012F两天前的傍晚，\x01",
            "奈尔先生是被某个人用通信器叫出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，是这样吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_79E3")

    label("loc_79E3")


    ChrTalk(
        0xB,
        "你们说的是真的吗？\x02",
    )

    CloseMessageWindow()

    def lambda_79FF():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79FF)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x102,
        (
            "#012F是的。\x02\x03",
            "大概这就是从那时开始到现在为止\x01",
            "他都没有音信的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#152F怎、怎么会！\x01",
            "前辈你不能死啊～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#509F哎，不要说那些莫名其妙的话啦！\x01",
            "　\x02\x03",
            "#007F从今天开始定期船也停航了……\x01",
            "　\x02\x03",
            "#505F到昨天为止还是可以通航的，\x01",
            "他会不会到别的地方去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "已经到空港看过了，\x01",
            "在登机名单上没有记载。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7BAA():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BAA)

    def lambda_7BB8():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7BB8)

    ChrTalk(
        0xB,
        (
            "也就是说……\x01",
            "他应该还在王都这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F嗯～……\x02\x03",
            "#070F你们两个在和那个叫奈尔的记者\x01",
            "最后一次见面的时候……\x02\x03",
            "那个记者没有提起过，\x01",
            "说他得到了什么新闻材料吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C91():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7C91)

    def lambda_7C9F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C9F)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#004F#4P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F现在这种局势。\x02\x03",
            "大众传媒也被军队所管制吧。\x01",
            "　\x02\x03",
            "对吗，主编先生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是啊，的确如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "特别是围绕情报部的话题，\x01",
            "正处于被层层审批的状态之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "能不能登出来就取决于他们的心情好坏。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F……在这种状况下，\x01",
            "可以报道的新闻自然就少了。\x02\x03",
            "可是，作为一个记者，\x01",
            "哪怕是有一点新的消息，\x01",
            "都想尽快传达给读者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P原来如此……\x02\x03",
            "情报部的管制不成问题，\x01",
            "以新的具有话题性的消息为重……\x02\x03",
            "关于这个，奈尔先生\x01",
            "曾经是提起过什么的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P啊，对了……\x02",
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
            "【关于武术大会的优胜者】\x01",          # 0
            "【关于科洛蒂亚公主的婚姻】\x01",        # 1
            "【关于尤莉亚和凯诺娜的过去】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8036"),
        (1, "loc_8200"),
        (2, "loc_8253"),
        (SWITCH_DEFAULT, "loc_845A"),
    )


    label("loc_8036")


    ChrTalk(
        0x108,
        (
            "#072F要把这个作为新闻的话，\x01",
            "也应该是在我们取得优胜之前的事情。\x02\x03",
            "作为现在的新消息就没有时效性了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#4P这样啊……\x02\x03",
            "的确，因为特务兵他们\x01",
            "还是有取胜的可能性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P还有一个线索。\x02\x03",
            "#012F奈尔先生对科洛蒂亚公主的婚姻事情\x01",
            "似乎很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#4P啊……没错！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F哦，晚宴时公爵所说的话……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x1)
    Jump("loc_845A")

    label("loc_8200")


    ChrTalk(
        0x108,
        (
            "#073F哦，晚宴时公爵所说的话……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x2)
    Jump("loc_845A")

    label("loc_8253")


    ChrTalk(
        0x108,
        (
            "#073F理查德上校的副官和通缉中的女亲卫队员\x01",
            "在士官学校里是对手……\x01",
            " \x02\x03",
            "#070F虽然很有趣，不过对于情报部来说\x01",
            "这种事情允许取材吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4P嗯，确实……\x01",
            "不能作为报道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P还有一个线索。\x02\x03",
            "#012F奈尔先生对科洛蒂亚公主的婚姻事情\x01",
            "似乎很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F#4P啊……没错！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F哦，晚宴时公爵所说的话……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x4B, 0x1)
    Jump("loc_845A")

    label("loc_845A")


    ChrTalk(
        0xB,
        (
            "什么？\x01",
            "奈尔和你们谈到了这件事？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8487():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8487)

    def lambda_8495():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8495)

    ChrTalk(
        0xB,
        (
            "如果是真的话，\x01",
            "那就是个爆炸性的新闻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总算是可以获取\x01",
            "一些内幕了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F那个叫奈尔的记者\x01",
            "怎么会知道这些事情？\x02\x03",
            "不是说与王家无关的人员\x01",
            "都不知道这个情报的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F他可能是从那个在艾尔贝离宫工作的\x01",
            "朋友那里打听回来的吧。\x02\x03",
            "#151F还有一个不能报道的消息，\x01",
            "公主殿下也被恐怖分子列为目标了～\x02\x03",
            "因此公主殿下在艾尔贝离宫里面\x01",
            "被秘密保护了起来～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_86EA():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86EA)

    def lambda_86F8():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86F8)

    def lambda_8706():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8706)

    ChrTalk(
        0x101,
        "#005F……果然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呵呵呵，\x01",
            "得来全不费工夫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F难道那天叫奈尔出去的\x01",
            "就是他在离宫里面工作的朋友吗……\x02\x03",
            "这样一来……\x01",
            "奈尔先生在离宫的可能性就很高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "也许奈尔为了\x01",
            "去采访公主殿下，\x01",
            "强行潜入了离宫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "然后被士兵发现了，\x01",
            "抓了起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#152F呀～啊！\x01",
            "奈尔前辈死定了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F都说了不会死的……\x02\x03",
            "#002F但是，如果这是事实的话，\x01",
            "他是不会被轻易释放出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯……\x02\x03",
            "他和科洛蒂娅公主\x01",
            "处于同样境地的可能性比较高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我说年轻人啊……\x01",
            "你们究竟知道了些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "在这个王都……不，\x01",
            "在利贝尔究竟发生了什么事，\x01",
            "你们不会不知道其中的内幕吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A22():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A22)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#007F唔～对不起。\x01",
            "请恕我们无可奉告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F奈尔先生的事情，\x01",
            "请交给我们游击士协会去办吧。\x02\x03",
            "如果的确是被拘捕了，\x01",
            "那我们一定会把他解救出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我明白了，拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#154F拜、拜托了～！小艾～！\x01",
            "　\x02\x03",
            "一定要救救奈尔前辈～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        "#006F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    OP_28(0x4B, 0x1, 0x200)
    OP_43(0xA, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_11_6FE7 end

    def Function_12_8B7B(): pass

    label("Function_12_8B7B")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    SetChrFlags(0x19, 0x80)
    OP_6D(-53570, 0, 62700, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(1650, 0)
    OP_6C(58000, 0)
    OP_6E(493, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -54290, 0, 62760, 109)
    SetChrPos(0xA, -60220, 0, 62930, 197)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0xA, 35)
    OP_43(0x101, 0x0, 0x0, 0xD)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#142F嘁……\x01",
            "终于开始了吗！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C3E():
        OP_6D(-56060, 0, 62820, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8C3E)
    OP_8C(0x9, 289, 400)
    OP_8E(0x9, 0xFFFF2298, 0x0, 0xF5A0, 0xBB8, 0x0)
    TurnDirection(0x9, 0xA, 400)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x9,
        (
            "#144F#2P出发，朵洛希！\x02\x03",
            "必须要确保找到\x01",
            "可以从远处眺望这场战斗的最佳位置！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(
        0xA,
        (
            "#152F等、等一下好吗～！\x02\x03",
            "感光结晶回路马上就可以设置好了～！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "喂喂，到底是怎么回事啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这三天来你去哪里游山玩水了啊？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 109, 600)

    ChrTalk(
        0x9,
        (
            "#144F这可是独家新闻！\x02\x03",
            "『利贝尔通讯社』建社以来\x01",
            "前所未有的超级无敌独家新闻啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_8B7B end

    def Function_13_8DAF(): pass

    label("Function_13_8DAF")

    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB5, 0x0, 0x64)
    Return()

    # Function_13_8DAF end

    def Function_14_8DE7(): pass

    label("Function_14_8DE7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "巴拉尔咖啡厅名菜！\x01",
            "『巨匠咖喱饭』　　１０００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "使用秘传的香辛料精心烹制的辣味咖喱，\x01",
            "请您走过路过不要错过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_8DE7 end

    def Function_15_8E9D(): pass

    label("Function_15_8E9D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～　菜单　～\x01",
            "　混合鸡尾酒　　　７５０米拉\x01",
            "　香草派　　　　　４５０米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～　本店推荐　～\x01",
            "　劲霸浓鱼汤　　　１０００米拉\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_8E9D end

    SaveToFile()

Try(main)
