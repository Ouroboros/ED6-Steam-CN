from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4136   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4136.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T4136   ._SN',
            'ED6_DT01/T4136_1 ._SN',
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
        '卡露娜',                               # 9
        '亚妮拉丝',                             # 10
        '库拉茨',                               # 11
        '克鲁茨',                               # 12
        '迪恩',                                 # 13
        '雷斯',                                 # 14
        '洛克',                                 # 15
        '士兵艾扎克',                           # 16
        '士兵赛恩',                             # 17
        '士兵塔里斯',                           # 18
        '士兵拜安',                             # 19
        '士兵密克里亚',                         # 20
        '士兵格古',                             # 21
        '士兵',                                 # 22
        '莱尔中尉',                             # 23
        '贝伦中尉',                             # 24
        '迪鲁队长',                             # 25
        '莱尔',                                 # 26
        '多伦',                                 # 27
        '吉尔',                                 # 28
        '乔丝特',                               # 29
        '朵洛希',                               # 30
        '克劳斯市长',                           # 31
        '理查德上校',                           # 32
        '凯诺娜上尉',                           # 33
        '洛伦斯少尉',                           # 34
        '斯妮亚',                               # 35
        '科娜克',                               # 36
        '约修亚',                               # 37
        '奥利维尔',                             # 38
        '金',                                   # 39
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
        Unknown_3A              = 186,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH01630 ._CH',             # 01
        'ED6_DT07/CH01260 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH02510 ._CH',             # 04
        'ED6_DT07/CH02520 ._CH',             # 05
        'ED6_DT07/CH02530 ._CH',             # 06
        'ED6_DT07/CH01640 ._CH',             # 07
        'ED6_DT07/CH01310 ._CH',             # 08
        'ED6_DT07/CH01380 ._CH',             # 09
        'ED6_DT07/CH02110 ._CH',             # 0A
        'ED6_DT07/CH02120 ._CH',             # 0B
        'ED6_DT07/CH02130 ._CH',             # 0C
        'ED6_DT07/CH02070 ._CH',             # 0D
        'ED6_DT07/CH02350 ._CH',             # 0E
        'ED6_DT07/CH02030 ._CH',             # 0F
        'ED6_DT07/CH02100 ._CH',             # 10
        'ED6_DT07/CH02200 ._CH',             # 11
        'ED6_DT07/CH01540 ._CH',             # 12
        'ED6_DT07/CH00010 ._CH',             # 13
        'ED6_DT07/CH00030 ._CH',             # 14
        'ED6_DT07/CH00070 ._CH',             # 15
        'ED6_DT07/CH01290 ._CH',             # 16
        'ED6_DT06/CH20142 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH01630P._CP',             # 01
        'ED6_DT07/CH01260P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH02510P._CP',             # 04
        'ED6_DT07/CH02520P._CP',             # 05
        'ED6_DT07/CH02530P._CP',             # 06
        'ED6_DT07/CH01640P._CP',             # 07
        'ED6_DT07/CH01310P._CP',             # 08
        'ED6_DT07/CH01380P._CP',             # 09
        'ED6_DT07/CH02110P._CP',             # 0A
        'ED6_DT07/CH02120P._CP',             # 0B
        'ED6_DT07/CH02130P._CP',             # 0C
        'ED6_DT07/CH02070P._CP',             # 0D
        'ED6_DT07/CH02350P._CP',             # 0E
        'ED6_DT07/CH02030P._CP',             # 0F
        'ED6_DT07/CH02100P._CP',             # 10
        'ED6_DT07/CH02200P._CP',             # 11
        'ED6_DT07/CH01540P._CP',             # 12
        'ED6_DT07/CH00010P._CP',             # 13
        'ED6_DT07/CH00030P._CP',             # 14
        'ED6_DT07/CH00070P._CP',             # 15
        'ED6_DT07/CH01290P._CP',             # 16
        'ED6_DT06/CH20142P._CP',             # 17
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
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
        TalkFunctionIndex   = 1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1850,
        Z                   = 0,
        Y                   = 13450,
        Direction           = 197,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 1440,
        Z                   = 0,
        Y                   = 13450,
        Direction           = 197,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 87000,
        TriggerZ            = 0,
        TriggerY            = 42860,
        TriggerRange        = 800,
        ActorX              = 87000,
        ActorZ              = 1000,
        ActorY              = 42860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87000,
        TriggerZ            = 0,
        TriggerY            = 42860,
        TriggerRange        = 800,
        ActorX              = -87000,
        ActorZ              = 1000,
        ActorY              = 42860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84200,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 800,
        ActorX              = 84200,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -84200,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 800,
        ActorX              = -84200,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84200,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 800,
        ActorX              = 84200,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1710,
        TriggerZ            = 0,
        TriggerY            = 11500,
        TriggerRange        = 400,
        ActorX              = -1850,
        ActorZ              = 1500,
        ActorY              = 13450,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1580,
        TriggerZ            = 0,
        TriggerY            = 11500,
        TriggerRange        = 400,
        ActorX              = 1440,
        ActorZ              = 1500,
        ActorY              = 13450,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_646",          # 00, 0
        "Function_1_801",          # 01, 1
        "Function_2_902",          # 02, 2
        "Function_3_A8A",          # 03, 3
        "Function_4_B3C",          # 04, 4
        "Function_5_CE4",          # 05, 5
        "Function_6_E73",          # 06, 6
        "Function_7_1019",         # 07, 7
        "Function_8_121B",         # 08, 8
        "Function_9_1358",         # 09, 9
        "Function_10_16A1",        # 0A, 10
        "Function_11_16A6",        # 0B, 11
        "Function_12_19B6",        # 0C, 12
        "Function_13_19BB",        # 0D, 13
        "Function_14_1CF2",        # 0E, 14
        "Function_15_1E6C",        # 0F, 15
        "Function_16_2016",        # 10, 16
        "Function_17_2262",        # 11, 17
        "Function_18_233C",        # 12, 18
        "Function_19_245D",        # 13, 19
        "Function_20_393C",        # 14, 20
        "Function_21_3995",        # 15, 21
        "Function_22_46E6",        # 16, 22
        "Function_23_4A7E",        # 17, 23
        "Function_24_4B79",        # 18, 24
        "Function_25_4F5E",        # 19, 25
        "Function_26_58A4",        # 1A, 26
        "Function_27_6050",        # 1B, 27
        "Function_28_6090",        # 1C, 28
        "Function_29_630F",        # 1D, 29
        "Function_30_6E03",        # 1E, 30
        "Function_31_6E57",        # 1F, 31
        "Function_32_7416",        # 20, 32
        "Function_33_82C5",        # 21, 33
        "Function_34_918E",        # 22, 34
        "Function_35_919B",        # 23, 35
        "Function_36_A9FD",        # 24, 36
        "Function_37_AA3D",        # 25, 37
        "Function_38_B175",        # 26, 38
        "Function_39_C1E1",        # 27, 39
        "Function_40_CD3D",        # 28, 40
        "Function_41_E44D",        # 29, 41
        "Function_42_E45A",        # 2A, 42
        "Function_43_E855",        # 2B, 43
        "Function_44_E9B1",        # 2C, 44
        "Function_45_F3EF",        # 2D, 45
        "Function_46_F590",        # 2E, 46
        "Function_47_F605",        # 2F, 47
        "Function_48_F654",        # 30, 48
        "Function_49_F896",        # 31, 49
        "Function_50_FA1F",        # 32, 50
    )


    def Function_0_646(): pass

    label("Function_0_646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_654")
    OP_A3(0x3FA)
    Event(0, 18)

    label("loc_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_662")
    OP_A3(0x3FB)
    Event(0, 22)

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_670")
    OP_A3(0x3FC)
    Event(0, 24)

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_67E")
    OP_A3(0x3FD)
    Event(0, 25)

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 6)), scpexpr(EXPR_END)), "loc_68C")
    OP_A3(0x3FE)
    Event(0, 26)

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 7)), scpexpr(EXPR_END)), "loc_69A")
    OP_A3(0x3FF)
    Event(0, 28)

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_6A8")
    OP_A3(0x3F0)
    Event(0, 29)

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_6B6")
    OP_A3(0x3F1)
    Event(0, 31)

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 2)), scpexpr(EXPR_END)), "loc_6C4")
    OP_A3(0x3F2)
    Event(0, 35)

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 3)), scpexpr(EXPR_END)), "loc_6D2")
    OP_A3(0x3F3)
    Event(0, 37)

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 4)), scpexpr(EXPR_END)), "loc_6E0")
    OP_A3(0x3F4)
    Event(0, 38)

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 5)), scpexpr(EXPR_END)), "loc_6EE")
    OP_A3(0x3F5)
    Event(0, 39)

    label("loc_6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 6)), scpexpr(EXPR_END)), "loc_6FC")
    OP_A3(0x3F6)
    Event(0, 42)

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 7)), scpexpr(EXPR_END)), "loc_70A")
    OP_A3(0x3F7)
    Event(0, 43)

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 0)), scpexpr(EXPR_END)), "loc_718")
    OP_A3(0x3F8)
    Event(0, 44)

    label("loc_718")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_730"),
        (102, "loc_730"),
        (106, "loc_74E"),
        (111, "loc_764"),
        (SWITCH_DEFAULT, "loc_78D"),
    )


    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74B")
    OP_A2(0x635)
    Event(0, 40)

    label("loc_74B")

    Jump("loc_78D")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_761")
    OP_A2(0x610)
    Event(0, 19)

    label("loc_761")

    Jump("loc_78D")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_777")
    OP_A2(0x636)
    Event(0, 41)

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78A")
    OP_A2(0x625)
    Event(0, 34)

    label("loc_78A")

    Jump("loc_78D")

    label("loc_78D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79C")
    Jump("loc_800")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB")
    Jump("loc_800")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BA")
    Jump("loc_800")

    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_800")
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x25, 80420, 0, -63670, 0)
    SetChrPos(0x26, 80420, 0, -62320, 180)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)

    label("loc_800")

    Return()

    # Function_0_646 end

    def Function_1_801(): pass

    label("Function_1_801")

    OP_1B(0x0, 0x0, 0x2D)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_71(0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_END)), "loc_822")
    OP_1B(0x5, 0x0, 0x32)
    Jump("loc_84A")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_END)), "loc_835")
    OP_72(0x3, 0x10)
    OP_65(0x2, 0x1)
    Jump("loc_84A")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_84A")
    OP_1B(0x5, 0x0, 0x32)
    OP_72(0x3, 0x10)
    OP_65(0x2, 0x1)

    label("loc_84A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_863")
    OP_1B(0xB, 0x0, 0x30)
    OP_1B(0xC, 0x0, 0x31)
    Jump("loc_8B0")

    label("loc_863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_877")
    OP_1B(0xB, 0x0, 0x30)
    Jump("loc_8B0")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88B")
    OP_1B(0xB, 0x0, 0x30)
    Jump("loc_8B0")

    label("loc_88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89F")
    OP_1B(0xC, 0x0, 0x31)
    Jump("loc_8B0")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B0")
    OP_1B(0xB, 0x0, 0x30)

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C4")
    OP_72(0x3, 0x10)
    Jump("loc_8C8")

    label("loc_8C4")

    OP_64(0x4, 0x1)

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DE")
    OP_1B(0x2, 0x0, 0x20)
    OP_1B(0x1, 0x0, 0x21)

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5")
    OP_10(0x4, 0x1)
    OP_10(0x9, 0x1)
    OP_10(0xD, 0x0)
    OP_10(0xE, 0x0)
    Jump("loc_901")

    label("loc_8F5")

    OP_10(0x4, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0xD, 0x1)
    OP_10(0xE, 0x1)

    label("loc_901")

    Return()

    # Function_1_801 end

    def Function_2_902(): pass

    label("Function_2_902")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A74")

    label("loc_932")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A74")

    label("loc_94B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_964")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A74")

    label("loc_964")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A74")

    label("loc_97D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_996")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A74")

    label("loc_996")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A74")

    label("loc_9AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A74")

    label("loc_9C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A74")

    label("loc_9E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A74")

    label("loc_9FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A13")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A74")

    label("loc_A13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A74")

    label("loc_A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A74")

    label("loc_A45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A74")

    label("loc_A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A74")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A89")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A74")

    label("loc_A89")

    Return()

    # Function_2_902 end

    def Function_3_A8A(): pass

    label("Function_3_A8A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#010F如果平静不下来的话，\x01",
            "不如去和其他组的选手谈谈话，\x01",
            "这样就能稍微让心情轻松一下。\x02\x03",
            "今天还不会和这边的小组对战嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_3_A8A end

    def Function_4_B3C(): pass

    label("Function_4_B3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_END)), "loc_C16")

    ChrTalk(
        0xFE,
        (
            "#030F哟，已经回来了吗？\x02\x03",
            "离比赛开始还有一段时间呢。\x02\x03",
            "你们两人再到其他地方转转，\x01",
            "好好放松一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F……难得你会说些正经的话，\x01",
            "感觉有点怪怪的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_C16")


    ChrTalk(
        0xFE,
        (
            "#035F呼，这种高亢的感觉……\x01",
            "就像是歌剧快要开始一样呢。\x02\x03",
            "那么，就让我更加沉醉吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Call(0, 23)

    label("loc_CE0")

    TalkEnd(0xFE)
    Return()

    # Function_4_B3C end

    def Function_5_CE4(): pass

    label("Function_5_CE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_END)), "loc_DE2")

    ChrTalk(
        0xFE,
        (
            "#070F那么，该如何与毫无破绽的\x01",
            "特务部队那些家伙们作战呢……\x02\x03",
            "无论进攻还是防守，\x01",
            "他们肯定会以那个队长\x01",
            "为核心展开战斗吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6F")

    label("loc_DE2")


    ChrTalk(
        0xFE,
        (
            "#070F这样看来，\x01",
            "不管哪一组都是很强的队伍呢。\x02\x03",
            "嘿嘿，这次特地来到利贝尔，\x01",
            "真是不虚此行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Call(0, 23)

    label("loc_E6F")

    TalkEnd(0xFE)
    Return()

    # Function_5_CE4 end

    def Function_6_E73(): pass

    label("Function_6_E73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_EF6")

    ChrTalk(
        0xFE,
        (
            "#851F回去之后，\x01",
            "一定要吃冰淇淋才行。\x02\x03",
            "#816F两位新人，你们也要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F6F")

    ChrTalk(
        0xFE,
        (
            "#816F你们是作为金先生小组的成员\x01",
            "登记参加比赛的吧。\x02\x03",
            "真期待你们的表现啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_F6F")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "#850F啊，两位新人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，亚妮拉丝姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#816F你们是为了协助金先生\x01",
            "而登记参加比赛的吧。\x02\x03",
            "真期待你们的表现啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1011")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_6_E73 end

    def Function_7_1019(): pass

    label("Function_7_1019")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1058")

    ChrTalk(
        0xFE,
        (
            "#830F终于轮到你们了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1213")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10E1")

    ChrTalk(
        0xFE,
        (
            "#835F你们也在这个休息室啊，\x01",
            "也就是说\x01",
            "我们的对战要推迟了。\x02\x03",
            "有点遗憾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1213")

    label("loc_10E1")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#831呀，艾丝蒂尔。\x02\x03",
            "你们也在这个休息室啊，\x01",
            "也就是说我们的对战要推迟了。\x02\x03",
            "#835F有点遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，期待的心情又要延长了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#830F呵呵，你还真敢说啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1213")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_7_1019 end

    def Function_8_121B(): pass

    label("Function_8_121B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(
        0xFE,
        (
            "#820F我支持你们。\x02\x03",
            "一口气解决吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_127D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12C6")

    ChrTalk(
        0xFE,
        (
            "#820F就让我们好好见识一下\x01",
            "你们的功夫吧。\x02\x03",
            "一起加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_12C6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "#821F哟！\x01",
            "你们果然来参加大会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，多亏了前辈你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#820F就让我们好好见识一下\x01",
            "你们的功夫吧。\x02\x03",
            "一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1350")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_8_121B end

    def Function_9_1358(): pass

    label("Function_9_1358")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_13E2")

    ChrTalk(
        0xFE,
        (
            "#840F只要保持平常心，\x01",
            "你们就一定没问题的。\x02\x03",
            "这场比赛会怎么样，\x01",
            "真是期待呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1699")

    label("loc_13E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14AF")

    ChrTalk(
        0xFE,
        (
            "#840F紧张的时候，\x01",
            "呼吸就会变得又浅又急。\x02\x03",
            "试着慢慢地进行深呼吸，\x01",
            "就能缓解紧张感了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1699")

    label("loc_14AF")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "#840F啊，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿，\x01",
            "稍微有点安不下心来……\x02",
        )
    )
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#840F紧张的时候，\x01",
            "呼吸就会变得又浅又急。\x02\x03",
            "试着慢慢地进行深呼吸，\x01",
            "就能缓解紧张感了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F原来是这样啊，慢慢地深呼吸……\x02\x03",
            "#500F吸～……呼～……\x02\x03",
            "吸～……呼～……\x02\x03",
            "#006F嗯，确实有点安心了呢。\x02\x03",
            "谢谢，克鲁茨先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#841F哈哈，没什么啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1699")

    Call(0, 23)
    TalkEnd(0xFE)
    Return()

    # Function_9_1358 end

    def Function_10_16A1(): pass

    label("Function_10_16A1")

    Call(0, 11)
    Return()

    # Function_10_16A1 end

    def Function_11_16A6(): pass

    label("Function_11_16A6")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16B3")
    Jump("loc_19B2")

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_16BD")
    Jump("loc_19B2")

    label("loc_16BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_16C7")
    Jump("loc_19B2")

    label("loc_16C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_16D1")
    Jump("loc_19B2")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1773")

    ChrTalk(
        0x23,
        (
            "不愧是决赛日，\x01",
            "今天一早就看见很多客人在门外等候进场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "要加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_1773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_177D")
    Jump("loc_19B2")

    label("loc_177D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_181E")

    ChrTalk(
        0x23,
        (
            "今天若是胜利的话，\x01",
            "明天就是决赛了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "要加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_181E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1863")

    ChrTalk(
        0x23,
        (
            "进入休息室之后，\x01",
            "请静候广播的通知。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18A8")

    ChrTalk(
        0x23,
        (
            "进入休息室之后，\x01",
            "请静候广播的通知。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_18A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_18E6")

    ChrTalk(
        0x23,
        (
            "今天的比赛\x01",
            "已经全部结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "期待各位的再次光临。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_19B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(
        0x23,
        (
            "今天的比赛\x01",
            "已经全部结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "期待着明天\x01",
            "各位客人的光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_192B")


    ChrTalk(
        0x23,
        (
            "如果想要观看预选赛，\x01",
            "就请抓紧时间进场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "现在去的话，\x01",
            "还可以赶上第七场比赛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B2")

    TalkEnd(0x23)
    Return()

    # Function_11_16A6 end

    def Function_12_19B6(): pass

    label("Function_12_19B6")

    Call(0, 13)
    Return()

    # Function_12_19B6 end

    def Function_13_19BB(): pass

    label("Function_13_19BB")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_19C8")
    Jump("loc_1CEE")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_19D2")
    Jump("loc_1CEE")

    label("loc_19D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_19DC")
    Jump("loc_1CEE")

    label("loc_19DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19E6")
    Jump("loc_1CEE")

    label("loc_19E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A52")

    ChrTalk(
        0x22,
        "唔，金先生的小组……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "今天也一样，\x01",
            "请进入右边『苍之组』的休息室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1A52")

    OP_A2(0x1)

    ChrTalk(
        0x22,
        "决赛就要开始了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "唔，金先生的小组……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "今天也一样，\x01",
            "请进入右边『苍之组』的休息室。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE3")

    Jump("loc_1CEE")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1AF0")
    Jump("loc_1CEE")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1B57")

    ChrTalk(
        0x22,
        "唔，金先生的小组……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "请进入右边\x01",
            "『苍之组』的休息室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEE")

    label("loc_1B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B61")
    Jump("loc_1CEE")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1BFC")

    ChrTalk(
        0x22,
        "你们是金选手一行人吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "唔～你们的休息室\x01",
            "是在右边的『苍之组』休息室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "要加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEE")

    label("loc_1BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C06")
    Jump("loc_1CEE")

    label("loc_1C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1CEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_END)), "loc_1C78")

    ChrTalk(
        0x22,
        (
            "游击士组的成员\x01",
            "还没有离开竞技场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "他们应该在\x01",
            "北边的休息室里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEE")

    label("loc_1C78")


    ChrTalk(
        0x22,
        "欢迎来到格兰竞技场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "要到观众席去观战，\x01",
            "请走里面的楼梯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEE")

    TalkEnd(0x22)
    Return()

    # Function_13_19BB end

    def Function_14_1CF2(): pass

    label("Function_14_1CF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1D75")

    ChrTalk(
        0xFE,
        (
            "#190F那些家伙，\x01",
            "到底对我做了些啥……\x02\x03",
            "哼，无论如何，\x01",
            "不教训一下那群卑鄙的家伙的话，\x01",
            "我就憋着一肚子的气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E68")

    label("loc_1D75")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "#197F在柏斯发生的那件事\x01",
            "我现在也不太记得了。\x02\x03",
            "想要强行回忆的话，\x01",
            "头就像要裂开似的疼痛异常。\x02\x03",
            "那些家伙，\x01",
            "到底对我做了些啥……\x02\x03",
            "#190F哼，无论如何，\x01",
            "不教训一下那群卑鄙的家伙的话，\x01",
            "我就憋着一肚子的气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E68")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CF2 end

    def Function_15_1E6C(): pass

    label("Function_15_1E6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_1F0E")

    ChrTalk(
        0xFE,
        (
            "#200F我现在没有闲心来理会你们。\x01",
            "　\x01",
            "　\x02\x03",
            "之前和你们打起来，\x01",
            "其实就是因为情报部的那些家伙从中作梗。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2012")

    label("loc_1F0E")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        (
            "#200F我现在没有闲心来理会你们。\x01",
            "　\x01",
            "　\x02\x03",
            "之前和你们打起来，\x01",
            "其实就是因为情报部的那些家伙从中作梗。\x01",
            "　\x02\x03",
            "虽然我没想要与你们和好，\x01",
            "不过也没必要和你们在这里打架。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2012")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E6C end

    def Function_16_2016(): pass

    label("Function_16_2016")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20BD")

    ChrTalk(
        0xFE,
        (
            "#216F啊…………\x02\x03",
            "#215F不要在我面前瞎转悠了，\x01",
            "快点走开，走开。\x02\x03",
            "我、我会尽全力给你们看的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225E")

    label("loc_20BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_214B")

    ChrTalk(
        0xFE,
        (
            "#214F什、什么呀？\x02\x03",
            "别在这里晃来晃去的了，\x01",
            "快点走开，走开。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225E")

    label("loc_214B")

    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "#213F什、什么呀？\x02\x03",
            "#214F不要在我面前瞎转悠了，\x01",
            "快点走开，走开。\x02\x03",
            "不止是情报部，\x01",
            "早晚有一天会让你们\x01",
            "也领教到本小姐的厉害！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225E")

    TalkEnd(0xFE)
    Return()

    # Function_16_2016 end

    def Function_17_2262(): pass

    label("Function_17_2262")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_22BA")

    ChrTalk(
        0xFE,
        (
            "为了还关在地牢里面的同伴，\x01",
            "能多赢一个就要多赢一个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2338")

    label("loc_22BA")

    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "我也相当痛恨那群穿黑衣服的人，\x01",
            "为了还关在地牢里面的同伴，\x01",
            "能多赢一个就要多赢一个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2338")

    TalkEnd(0xFE)
    Return()

    # Function_17_2262 end

    def Function_18_233C(): pass

    label("Function_18_233C")

    EventBegin(0x0)
    OP_6D(-570, 0, 16630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 540, 0, 2040, 0)
    SetChrPos(0x102, -550, 0, 1580, 0)
    FadeToBright(1000, 0)
    OP_6D(-40, 0, 2550, 5000)

    ChrTalk(
        0x101,
        (
            "#004F哇……\x01",
            "又是这么豪华的房间啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这里是正门大厅吧。\x02\x03",
            "看起来，观众席应该在上面二层。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，去看看吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_18_233C end

    def Function_19_245D(): pass

    label("Function_19_245D")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(-88340, 0, -60660, 0)
    SetChrPos(0x101, -89210, 0, -62630, 45)
    SetChrPos(0x102, -89130, 0, -63770, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, -87270, 0, -59540, 135)
    SetChrPos(0x9, -85710, 0, -59510, 180)
    SetChrPos(0xA, -86540, 0, -61600, 45)
    SetChrPos(0xB, -84960, 0, -60990, 315)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#001F#1P卡露娜姐姐，\x01",
            "祝贺你们通过预选赛～！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_259F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_259F)

    def lambda_25AD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25AD)

    def lambda_25BB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_25BB)

    def lambda_25C9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_25C9)

    ChrTalk(
        0x9,
        "#850F#2P啊，是两位新人啊！\x02",
    )

    CloseMessageWindow()

    def lambda_25FC():

        label("loc_25FC")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_25FC")

    QueueWorkItem2(0x8, 1, lambda_25FC)

    def lambda_260D():

        label("loc_260D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_260D")

    QueueWorkItem2(0x9, 1, lambda_260D)

    def lambda_261E():

        label("loc_261E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_261E")

    QueueWorkItem2(0xA, 1, lambda_261E)

    def lambda_262F():

        label("loc_262F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_262F")

    QueueWorkItem2(0xB, 1, lambda_262F)

    def lambda_2640():

        label("loc_2640")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2640")

    QueueWorkItem2(0x101, 1, lambda_2640)

    def lambda_2651():

        label("loc_2651")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2651")

    QueueWorkItem2(0x102, 1, lambda_2651)

    def lambda_2662():
        OP_6D(-87430, 0, -59810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2662)

    def lambda_267A():
        OP_8E(0xFE, 0xFFFEA69C, 0x0, 0xFFFF14C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_267A)
    Sleep(500)

    def lambda_269A():
        OP_8E(0xFE, 0xFFFEA7AA, 0x0, 0xFFFF100A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_269A)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        "#831F哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#821F#6P嘿嘿。\x01",
            "难道你们是特地来看比赛的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P嗯，是的。\x01",
            "正好看到了前辈你们的比赛。\x02\x03",
            "比赛真是精彩啊。\x02",
        )
    )
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841F谢谢，\x01",
            "听到你们这么说真是高兴啊。\x02\x03",
            "不过这次突然变成团体赛，\x01",
            "正觉得奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#819F#2P嗯嗯，\x01",
            "真是紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#835F我们还算好啦。\x01",
            "不管怎么说集齐了队友。\x02\x03",
            "老实说，\x01",
            "金大人的情况可真是不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊～～\x01",
            "卡露娜姐姐你们也认识金先生吗？\x02",
        )
    )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#830F啊，不算认识，\x01",
            "仅仅是知道名字而已。\x02\x03",
            "他被称为『不动金』，\x01",
            "是共和国著名的游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#840F好像是专门为参加武术大会\x01",
            "而来到利贝尔王国的……\x02\x03",
            "就像刚才所说的，\x01",
            "今年的武术大会突然从\x01",
            "个人赛改成了团体赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#825F#6P这么大胆的主意大概是\x01",
            "那个杜南公爵想出来的吧。\x02\x03",
            "#6P金大人没有办法，\x01",
            "只能落到一个人出场的境地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是吗……\x02\x03",
            "#009F真是的……\x01",
            "那个公爵净爱搞一些无聊的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841F哈哈，没错。\x02\x03",
            "#844F可是，这样他的实力没办法全部发挥，\x01",
            "真是太替他可惜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#823F#6P不过，如果有实力不俗的人来协助他，\x01",
            "就算那些人没有什么名气也好啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#821F#6P……哦！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#831F……哎呀…………\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xB)

    ChrTalk(
        0xB,
        "#841F…………嗯。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#2P……或许能行…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F？？？\x02\x03",
            "怎、怎么了？\x01",
            "这样盯着我们看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#840F没什么，我们在想……\x02\x03",
            "你们愿不愿意\x01",
            "协助金先生参加正式赛呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F哎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#004F#3S哎～～～～～～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#1P从正式赛开始参加……\x01",
            "这样也可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#835F本来就是突然\x01",
            "从个人赛变成团体赛的嘛。\x02\x03",
            "规矩也不是死的，\x01",
            "应该能多少通融一下的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820F#6P而且金大人\x01",
            "也曾经问过艾南有没有\x01",
            "能够协助他的游击士呢。\x02\x03",
            "#6P不过雪拉扎德忙得脱不开身，\x01",
            "阿加特那家伙也联系不上。\x02\x03",
            "#6P别的人也都是类似的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#856F#2P至于卡西乌斯先生，\x01",
            "好像也不在国内呢。\x02\x03",
            "#819F#2P不过，他和金先生组合的话，\x01",
            "好像违反规定了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841F哈哈，如果这样的话，\x01",
            "我们可是连一点胜算也没有了。\x02\x03",
            "#840F……就是这样，\x01",
            "你们好好考虑一下吧。\x02\x03",
            "今天和金先生达成一致意见的话，\x01",
            "就能赶上明天的选手报名了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F嗯，好……\x02",
    )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#830F哎呀……\x01",
            "聊天的时间太长了。\x02\x03",
            "我们还有很多的委托要做，\x01",
            "抱歉，就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#850F#2P拜拜了，两位新人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#821F#6P嘿嘿。\x01",
            "期待能在比赛场上和你们交手。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)

    def lambda_31AC():

        label("loc_31AC")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_31AC")

    QueueWorkItem2(0x101, 1, lambda_31AC)

    def lambda_31BD():

        label("loc_31BD")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_31BD")

    QueueWorkItem2(0x102, 1, lambda_31BD)
    OP_43(0xA, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xB, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_72(0x5, 0x10)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1D)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x14)
    Sleep(2000)
    WaitChrThread(0x8, 0x1)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x5, 0x1D)
    OP_70(0x5, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(-89000, 0, -60260, 1000)
    OP_71(0x5, 0x800)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F……怎么办，艾丝蒂尔？\x02\x03",
            "本来是要谈和工作有关的事情，\x01",
            "结果变成这个样子……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008F#2P……嘿嘿…………\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x190, 0xFA0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#502F#2P………哼哼……………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔，你、你没事吧？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 23)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#582F#2P来了来了……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    Sleep(400)
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        "#508F#2P#3S终于来了～～～！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F#2P对了，就是这样！\x01",
            "果然果然就是这样！！\x02\x03",
            "#502F啊啊，女神！\x01",
            "感谢您的保佑！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F………………………………\x02\x03",
            "#013F艾、艾丝蒂尔疯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#2P你想想看！\x01",
            "我们可以参加武术大会了！\x02\x03",
            "#582F可以帮助遇到困难的金先生……\x02\x03",
            "可以光明正大地进入王城……\x02\x03",
            "而且可以体验白热化的战斗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#508F#2P#3S这真是一石三鸟啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F能、能做到这一步吗……\x02\x03",
            "#010F不过，\x01",
            "虽然还不知道能不能获胜……\x02\x03",
            "有靠自己就能完成委托的可能性，\x01",
            "这个主意还真非常不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#2P嗯嗯⊙\x01",
            "不管怎么说，这是最重要的！\x02\x03",
            "#005F……就这么决定了，\x01",
            "赶快去拜托金先生吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F话说回来，\x01",
            "你知道金先生在哪里吗？\x02",
        )
    )


    def lambda_37E5():

        label("loc_37E5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_37E5")

    QueueWorkItem2(0x102, 1, lambda_37E5)

    def lambda_37F6():
        OP_8E(0x101, 0xFFFEA1E2, 0x0, 0xFFFF0A1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37F6)
    Sleep(600)
    OP_44(0x101, 0xFF)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F#1P……这么说的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#2P真是的……\x01",
            "稍微冷静一点嘛。\x02\x03",
            "#010F总之先回协会\x01",
            "向艾南先生报告一下吧。\x02\x03",
            "如果是他的话，\x01",
            "肯定会知道金先生在哪儿的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_245D end

    def Function_20_393C(): pass

    label("Function_20_393C")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFEAA98, 0x0, 0xFFFF0A06, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEA020, 0x0, 0xFFFF09FC, 0xBB8, 0x0)

    def lambda_396F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_396F)
    OP_8E(0xFE, 0xFFFE9B84, 0x0, 0xFFFF0B14, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_393C end

    def Function_21_3995(): pass

    label("Function_21_3995")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 84960, 0, 33240, 270)
    SetChrPos(0x102, 84840, 0, 32159, 270)
    SetChrPos(0x101, 85910, 0, 32400, 270)
    SetChrPos(0x108, 86160, 0, 33600, 270)
    SetChrPos(0xC, 87840, 0, 24750, 0)
    SetChrPos(0xD, 86780, 0, 23680, 0)
    SetChrPos(0xE, 88160, 0, 23360, 0)
    OP_6D(84240, 0, 32960, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#010F右边的『苍之组』休息室，\x01",
            "应该就是这里对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F哈·哈·哈。\x01",
            "在比赛之前就让我们悠闲地休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不管什么时候，\x01",
            "你不都是一样地悠闲吗……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "青年的声音",
        (
            "#2P嘿嘿……\x01",
            "还真是一点也不紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3B79():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B79)

    def lambda_3B87():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B87)

    def lambda_3B95():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3B95)

    def lambda_3BA3():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BA3)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6D(86060, 0, 28650, 2000)

    ChrTalk(
        0x101,
        "#004F你、你们是……！\x02",
    )

    CloseMessageWindow()

    def lambda_3BE8():

        label("loc_3BE8")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_3BE8")

    QueueWorkItem2(0x101, 1, lambda_3BE8)

    def lambda_3BF9():

        label("loc_3BF9")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_3BF9")

    QueueWorkItem2(0x102, 1, lambda_3BF9)

    def lambda_3C0A():

        label("loc_3C0A")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_3C0A")

    QueueWorkItem2(0x108, 1, lambda_3C0A)

    def lambda_3C1B():

        label("loc_3C1B")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_3C1B")

    QueueWorkItem2(0x104, 1, lambda_3C1B)

    def lambda_3C2C():

        label("loc_3C2C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3C2C")

    QueueWorkItem2(0xC, 1, lambda_3C2C)

    def lambda_3C3D():

        label("loc_3C3D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3C3D")

    QueueWorkItem2(0xD, 1, lambda_3C3D)

    def lambda_3C4E():

        label("loc_3C4E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3C4E")

    QueueWorkItem2(0xE, 1, lambda_3C4E)

    def lambda_3C5F():
        OP_6D(84900, 0, 32229, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C5F)

    def lambda_3C77():
        OP_8E(0xFE, 0x15040, 0x0, 0x79AE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3C77)
    Sleep(200)

    def lambda_3C97():
        OP_8E(0xFE, 0x1552C, 0x0, 0x7706, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3C97)
    Sleep(200)

    def lambda_3CB7():
        OP_8E(0xFE, 0x1500E, 0x0, 0x744A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3CB7)
    WaitChrThread(0xE, 0x2)

    ChrTalk(
        0xE,
        (
            "哼……\x01",
            "没想到在这种地方见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "嘻哈哈。\x01",
            "在这里遇见你们，还真是走运啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#2P……你们是谁啊？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0xC,
        (
            "#1P我们可是卢安\x01",
            "大名鼎鼎的『渡鸦帮』！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xE,
        "不要说你已经忘了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#2P开玩笑，是开玩笑的啦。\x02\x03",
            "#006F昨天已经观看了你们同伴参加的预选赛，\x01",
            "就知道你们几个肯定也来了王都。\x01",
            "　\x02\x03",
            "那么，这次你们来，\x01",
            "又是想不知悔改地找我们麻烦对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哼·哼·哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "嘿·嘿·嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "呼·呼·呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#2P什、什么啊，真是恶心……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F难道说，你们也参加正式赛吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "喂，干嘛露出那么吃惊的表情啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我们可是在预选赛中取胜，\x01",
            "才走到这一步的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "可不像半途参加的某些家伙那样，\x01",
            "这么厚脸皮的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P哎～这不是很厉害嘛！\x02\x03",
            "#001F像你们这种业余的人也能胜出，\x01",
            "干得不错嘛。\x02\x03",
            "肯定进行了相当辛苦的特训吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "说什么呢，这个小丫头……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P本来以为你们只是普通的小混混呢，\x01",
            "没想到这么有毅力啊。\x02\x03",
            "#502F嗯嗯，要对你们刮目相看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "没什么啦……嘿嘿……\x02",
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    TurnDirection(0xC, 0xD, 600)

    ChrTalk(
        0xC,
        "#2P别、别被迷惑了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "总、总之，\x01",
            "之前被你们给捉弄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "趁这个机会，\x01",
            "一定要把这笔账算回来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 600)

    ChrTalk(
        0x101,
        (
            "#006F#2P哼哼，正合我意。\x02\x03",
            "对了，\x01",
            "你们也在这边的休息室？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不，是另外一边……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P那么，我们很有可能\x01",
            "会在今天的比赛中就碰面哦。\x02\x03",
            "#001F如果这样的话，\x01",
            "我们就来堂堂正正地较量一番吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xD, 0xFF)

    ChrTalk(
        0xC,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#2P哎？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(
        0xC,
        "#2P喂，我们走吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "嗯……\x01",
            "她好像有点不正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "比赛之前我们去吃点东西吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    def lambda_4469():
        OP_8E(0xFE, 0x1500E, 0x0, 0x5B04, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4469)
    OP_8C(0xE, 180, 400)

    def lambda_448B():
        OP_8E(0xFE, 0x1552C, 0x0, 0x5B04, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_448B)
    Sleep(300)

    def lambda_44AB():
        OP_8E(0xFE, 0x15040, 0x0, 0x5B04, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_44AB)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)
    OP_6D(84900, 0, 33240, 2000)

    ChrTalk(
        0x101,
        "#580F#2P什、什么呀……真是不给面子。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F喂，我说了什么奇怪的话吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x108, 0x101, 0)
    TurnDirection(0x104, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F#1P不……没有啊。\x02\x03",
            "#019F你也真是厉害啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#071F#2P哈哈，算了，不要在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5P对自己的优点毫不关心，\x01",
            "这才是艾丝蒂尔君的本色嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F怎么感觉像是被看猴戏了一样……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#1P没有这种事啦。\x02\x03",
            "#010F我们赶快进休息室，\x01",
            "等待比赛开始吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x61C)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3995 end

    def Function_22_46E6(): pass

    label("Function_22_46E6")

    EventBegin(0x0)
    OP_6D(82890, 0, -58910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 82240, 0, -59590, 90)
    SetChrPos(0x102, 83290, 0, -60620, 0)
    SetChrPos(0x108, 84060, 0, -58500, 180)
    SetChrPos(0x104, 84330, 0, -59900, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, 80230, 0, -59410, 180)
    SetChrPos(0xA, 79030, 0, -59770, 90)
    SetChrPos(0xB, 81100, 0, -61130, 315)
    SetChrPos(0x9, 79590, 0, -60950, 0)
    SetChrPos(0x16, 77000, 0, -64940, 135)
    SetChrPos(0xF, 77450, 0, -66680, 352)
    SetChrPos(0x10, 78200, 0, -66090, 315)
    SetChrPos(0x11, 78970, 0, -65300, 247)
    SetChrPos(0x17, 82830, 0, -65010, 270)
    SetChrPos(0x13, 81290, 0, -65700, 90)
    SetChrPos(0x12, 83000, 0, -66520, 16)
    SetChrPos(0x14, 81230, 0, -64459, 98)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#503F好、好像快要开始了……\x02\x03",
            "怎么办……\x01",
            "心一直在扑通扑通地乱跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F要保持镇静啊，艾丝蒂尔。\x02\x03",
            "轮到我们的时候会有通知的，\x01",
            "在那之前就安心等待吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯～就算这么说，\x01",
            "我也平静不下来啊～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x3, 0xFF)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x24, 83160, 0, -59400, 180)
    SetChrPos(0x26, 84060, 0, -58500, 180)
    SetChrPos(0x25, 85350, 0, -58540, 180)
    OP_6D(84180, 0, -61020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 84180, 0, -61020, 0)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_22_46E6 end

    def Function_23_4A7E(): pass

    label("Function_23_4A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B78")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "各位……\x01",
            "让你们久等了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我宣布，武术大会正式赛，现在开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMapFlags(0x100000)
    OP_22(0xAF, 0x0, 0x64)
    OP_22(0xBF, 0x0, 0x64)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4B78")

    Return()

    # Function_23_4A7E end

    def Function_24_4B79(): pass

    label("Function_24_4B79")

    EventBegin(0x0)
    OP_6D(79600, 0, -59790, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 82240, 0, -59590, 90)
    SetChrPos(0x102, 83290, 0, -60620, 0)
    SetChrPos(0x108, 84060, 0, -58500, 180)
    SetChrPos(0x104, 84330, 0, -59900, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, 80230, 0, -59410, 180)
    SetChrPos(0xA, 79030, 0, -59770, 90)
    SetChrPos(0xB, 81100, 0, -61130, 315)
    SetChrPos(0x9, 79590, 0, -60950, 0)
    SetChrPos(0x16, 77000, 0, -64940, 135)
    SetChrPos(0xF, 77450, 0, -66680, 352)
    SetChrPos(0x10, 78200, 0, -66090, 315)
    SetChrPos(0x11, 78970, 0, -65300, 247)
    SetChrPos(0x17, 82830, 0, -65010, 270)
    SetChrPos(0x13, 81290, 0, -65700, 90)
    SetChrPos(0x12, 83000, 0, -66520, 16)
    SetChrPos(0x14, 81230, 0, -64459, 98)

    def lambda_4D0A():

        label("loc_4D0A")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D0A")

    QueueWorkItem2(0x16, 1, lambda_4D0A)

    def lambda_4D1B():

        label("loc_4D1B")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D1B")

    QueueWorkItem2(0xF, 1, lambda_4D1B)

    def lambda_4D2C():

        label("loc_4D2C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D2C")

    QueueWorkItem2(0x10, 1, lambda_4D2C)

    def lambda_4D3D():

        label("loc_4D3D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D3D")

    QueueWorkItem2(0x11, 1, lambda_4D3D)

    def lambda_4D4E():

        label("loc_4D4E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D4E")

    QueueWorkItem2(0x17, 1, lambda_4D4E)

    def lambda_4D5F():

        label("loc_4D5F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D5F")

    QueueWorkItem2(0x12, 1, lambda_4D5F)

    def lambda_4D70():

        label("loc_4D70")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D70")

    QueueWorkItem2(0x13, 1, lambda_4D70)

    def lambda_4D81():

        label("loc_4D81")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D81")

    QueueWorkItem2(0x14, 1, lambda_4D81)

    def lambda_4D92():

        label("loc_4D92")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4D92")

    QueueWorkItem2(0x101, 1, lambda_4D92)

    def lambda_4DA3():

        label("loc_4DA3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4DA3")

    QueueWorkItem2(0x102, 1, lambda_4DA3)

    def lambda_4DB4():

        label("loc_4DB4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4DB4")

    QueueWorkItem2(0x108, 1, lambda_4DB4)

    def lambda_4DC5():

        label("loc_4DC5")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4DC5")

    QueueWorkItem2(0x104, 1, lambda_4DC5)
    Sleep(1000)

    ChrTalk(
        0xB,
        "好……该出场了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820F被称为突击骑兵队的，\x01",
            "肯定是相当勇猛的王国军将士。\x02\x03",
            "作为对手来说够格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F卡露娜姐姐，你们要加油哦！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#831F啊，看我们的吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "#816F那么我们上吧！\x02",
    )

    CloseMessageWindow()

    def lambda_4ED2():
        OP_8E(0xFE, 0x11D8C, 0x0, 0xFFFF0916, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4ED2)
    Sleep(200)

    def lambda_4EF2():
        OP_8E(0xFE, 0x11D8C, 0x0, 0xFFFF0916, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4EF2)

    def lambda_4F0D():
        OP_8E(0xFE, 0x11D8C, 0x0, 0xFFFF0916, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F0D)
    Sleep(200)

    def lambda_4F2D():
        OP_8E(0xFE, 0x11D8C, 0x0, 0xFFFF0916, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4F2D)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_4B79 end

    def Function_25_4F5E(): pass

    label("Function_25_4F5E")

    EventBegin(0x0)
    OP_6D(77930, 0, -60800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 78520, 0, -61710, 270)
    SetChrPos(0x102, 79300, 0, -62840, 270)
    SetChrPos(0x108, 79800, 0, -61660, 270)
    SetChrPos(0x104, 79010, 0, -60670, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x16, 77000, 0, -64940, 135)
    SetChrPos(0xF, 77450, 0, -66680, 352)
    SetChrPos(0x10, 78200, 0, -66090, 315)
    SetChrPos(0x11, 78970, 0, -65300, 247)
    SetChrPos(0x17, 82830, 0, -65010, 270)
    SetChrPos(0x13, 81290, 0, -65700, 90)
    SetChrPos(0x12, 83000, 0, -66520, 16)
    SetChrPos(0x14, 81230, 0, -64459, 98)
    SetChrPos(0x8, 72110, 0, -61480, 90)
    SetChrPos(0xA, 72060, 0, -62470, 90)
    SetChrPos(0xB, 71980, 0, -63590, 90)
    SetChrPos(0x9, 72090, 0, -64519, 90)

    def lambda_50DB():

        label("loc_50DB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50DB")

    QueueWorkItem2(0x16, 1, lambda_50DB)

    def lambda_50EC():

        label("loc_50EC")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50EC")

    QueueWorkItem2(0xF, 1, lambda_50EC)

    def lambda_50FD():

        label("loc_50FD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_50FD")

    QueueWorkItem2(0x10, 1, lambda_50FD)

    def lambda_510E():

        label("loc_510E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_510E")

    QueueWorkItem2(0x11, 1, lambda_510E)

    def lambda_511F():

        label("loc_511F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_511F")

    QueueWorkItem2(0x17, 1, lambda_511F)

    def lambda_5130():

        label("loc_5130")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5130")

    QueueWorkItem2(0x12, 1, lambda_5130)

    def lambda_5141():

        label("loc_5141")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5141")

    QueueWorkItem2(0x13, 1, lambda_5141)

    def lambda_5152():

        label("loc_5152")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5152")

    QueueWorkItem2(0x14, 1, lambda_5152)

    def lambda_5163():

        label("loc_5163")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5163")

    QueueWorkItem2(0x101, 1, lambda_5163)

    def lambda_5174():

        label("loc_5174")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5174")

    QueueWorkItem2(0x102, 1, lambda_5174)

    def lambda_5185():

        label("loc_5185")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5185")

    QueueWorkItem2(0x108, 1, lambda_5185)

    def lambda_5196():

        label("loc_5196")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5196")

    QueueWorkItem2(0x104, 1, lambda_5196)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F#5P太好了！\x01",
            "卡露娜姐姐他们赢了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不愧是利贝尔的游击士啊。\x01",
            "  \x02\x03",
            "联手作战能厉害到如此程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F就算在人少的时候，\x01",
            "各自也能做到以一敌百呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果碰上他们，\x01",
            "肯定要进行一番苦战了。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x40)

    def lambda_5333():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5333)

    def lambda_5345():

        label("loc_5345")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_5345")

    QueueWorkItem2(0x8, 2, lambda_5345)

    def lambda_5356():
        OP_8E(0xFE, 0x12CDC, 0x0, 0xFFFF12A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5356)
    Sleep(100)

    def lambda_5376():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5376)

    def lambda_5388():

        label("loc_5388")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_5388")

    QueueWorkItem2(0xA, 2, lambda_5388)

    def lambda_5399():
        OP_8E(0xFE, 0x12ACA, 0x0, 0xFFFF0E7A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_5399)
    Sleep(100)

    def lambda_53B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_53B9)

    def lambda_53CB():

        label("loc_53CB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_53CB")

    QueueWorkItem2(0xB, 2, lambda_53CB)

    def lambda_53DC():
        OP_8E(0xFE, 0x12ED0, 0x0, 0xFFFF0C7C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_53DC)
    Sleep(100)

    def lambda_53FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_53FC)

    def lambda_540E():

        label("loc_540E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_540E")

    QueueWorkItem2(0x9, 2, lambda_540E)

    def lambda_541F():
        OP_8E(0xFE, 0x129E4, 0x0, 0xFFFF17F8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_541F)
    WaitChrThread(0x9, 0x3)

    def lambda_543F():
        OP_8E(0xFE, 0x12F7A, 0x0, 0xFFFF160E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_543F)

    ChrTalk(
        0x101,
        "#508F各位前辈，打得真漂亮！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F哟，真是精彩的比赛啊。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x3)

    ChrTalk(
        0xB,
        (
            "#841F哈哈，能被『不动金』这样称赞，\x01",
            "真是光荣之至啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x3)

    ChrTalk(
        0xA,
        (
            "#825F果然和预选赛不一样，\x01",
            "不能有丝毫懈怠呢。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "下面宣布第二场比赛的\x01",
            "对阵双方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南边，苍之组——\x01",
            "来自卡尔瓦德共和国的武术家，\x01",
            "金选手等四人组！\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北边，红之组——\x01",
            "『渡鸦帮』所属，\x01",
            "迪恩选手等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)

    def lambda_564D():
        OP_6D(78520, 0, -60920, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_564D)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#006F#5P轮到我们了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#015F而且对手是渡鸦帮那些人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F哼哼，虽然是有欠优雅的对手，\x01",
            "不过会是场有趣的比赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#076F好，我们出场吧！\x02",
    )

    CloseMessageWindow()
    OP_44(0x16, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(77750, 0, -62490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 77750, 0, -62490, 270)
    SetChrPos(0x102, 77750, 0, -62490, 270)
    SetChrPos(0x108, 77750, 0, -62490, 270)
    SetChrPos(0x104, 77750, 0, -62490, 270)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrPos(0x8, 76870, 0, -60150, 180)
    SetChrPos(0xA, 79050, 0, -59930, 180)
    SetChrPos(0x9, 77910, 0, -59730, 180)
    SetChrPos(0xB, 75670, 0, -60330, 180)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_A2(0x61D)
    OP_1B(0xB, 0x0, 0x30)
    OP_1B(0xC, 0x0, 0xFFFF)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0x9, 0x40)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_25_4F5E end

    def Function_26_58A4(): pass

    label("Function_26_58A4")

    EventBegin(0x0)
    OP_6D(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 81880, 0, -59420, 225)
    SetChrPos(0x102, 82470, 0, -60720, 270)
    SetChrPos(0x108, 82960, 0, -59440, 225)
    SetChrPos(0x104, 82020, 0, -61450, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, 80230, 0, -59410, 90)
    SetChrPos(0xA, 79030, 0, -59770, 90)
    SetChrPos(0xB, 80710, 0, -61590, 45)
    SetChrPos(0x9, 79590, 0, -60950, 90)
    SetChrPos(0x16, 77000, 0, -64940, 135)
    SetChrPos(0xF, 77450, 0, -66680, 352)
    SetChrPos(0x10, 78200, 0, -66090, 315)
    SetChrPos(0x11, 78970, 0, -65300, 247)
    SetChrPos(0x17, 82830, 0, -65010, 270)
    SetChrPos(0x13, 81290, 0, -65700, 90)
    SetChrPos(0x12, 83000, 0, -66520, 16)
    SetChrPos(0x14, 81230, 0, -64459, 98)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#830F哈哈……\x01",
            "那些小混混也能做到如此程度啊。\x02\x03",
            "看来人真是可以改变的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然胜负已分，\x01",
            "不过真是精彩的比赛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈，谢谢了。\x02\x03",
            "他们能洗心革面，\x01",
            "全是拜我的仁德所赐哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哎～是吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#007F#2P一个完全不知情的人，\x01",
            "又在别人面前信口开河起来了……\x02\x03",
            "#509F说起来，\x01",
            "你根本不认识那些流氓呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F坠入爱河只是一瞬间的事，\x01",
            "但加速度可是无限大的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F越来越听不懂了……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "下面宣布第三场比赛的\x01",
            "对阵双方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南边，苍之组——\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "王国军空降部队３连，\x01",
            "莱尔中尉等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_5D86():

        label("loc_5D86")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5D86")

    QueueWorkItem2(0x8, 1, lambda_5D86)

    def lambda_5D97():

        label("loc_5D97")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5D97")

    QueueWorkItem2(0xA, 1, lambda_5D97)

    def lambda_5DA8():

        label("loc_5DA8")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5DA8")

    QueueWorkItem2(0xB, 1, lambda_5DA8)

    def lambda_5DB9():

        label("loc_5DB9")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5DB9")

    QueueWorkItem2(0x9, 1, lambda_5DB9)

    def lambda_5DCA():

        label("loc_5DCA")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5DCA")

    QueueWorkItem2(0x101, 1, lambda_5DCA)

    def lambda_5DDB():

        label("loc_5DDB")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5DDB")

    QueueWorkItem2(0x102, 1, lambda_5DDB)

    def lambda_5DEC():

        label("loc_5DEC")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5DEC")

    QueueWorkItem2(0x108, 1, lambda_5DEC)

    def lambda_5DFD():

        label("loc_5DFD")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5DFD")

    QueueWorkItem2(0x104, 1, lambda_5DFD)

    def lambda_5E0E():

        label("loc_5E0E")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5E0E")

    QueueWorkItem2(0x17, 1, lambda_5E0E)

    def lambda_5E1F():

        label("loc_5E1F")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5E1F")

    QueueWorkItem2(0x12, 1, lambda_5E1F)

    def lambda_5E30():

        label("loc_5E30")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5E30")

    QueueWorkItem2(0x13, 1, lambda_5E30)

    def lambda_5E41():

        label("loc_5E41")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_5E41")

    QueueWorkItem2(0x14, 1, lambda_5E41)
    OP_6D(78750, 0, -62500, 1500)

    ChrTalk(
        0x16,
        "#5P好……该我们出场了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P打起精神来上场吧，小子们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "是的，长官！\x02",
    )

    CloseMessageWindow()
    OP_43(0x16, 0x1, 0x0, 0x1B)
    Sleep(300)
    OP_43(0xF, 0x1, 0x0, 0x1B)
    Sleep(300)
    OP_43(0x11, 0x1, 0x0, 0x1B)
    Sleep(600)
    OP_43(0x10, 0x1, 0x0, 0x1B)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北边，红之组——\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "空贼团『卡普亚一家』所属，\x01",
            "多伦选手等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(82090, 0, -59990, 1000)
    Sleep(400)

    ChrTalk(
        0x101,
        "#580F#2P#3S哎！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F『卡普亚一家』不是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F哎呀哎呀，\x01",
            "好像在哪里听说过这名字呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_58A4 end

    def Function_27_6050(): pass

    label("Function_27_6050")

    OP_8E(0xFE, 0x12282, 0x0, 0xFFFF0A1A, 0xBB8, 0x0)

    def lambda_606A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_606A)
    OP_8E(0xFE, 0x11A3A, 0x0, 0xFFFF0A92, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_6050 end

    def Function_28_6090(): pass

    label("Function_28_6090")

    EventBegin(0x0)
    OP_6D(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 81880, 0, -59420, 270)
    SetChrPos(0x102, 82470, 0, -60720, 270)
    SetChrPos(0x108, 82960, 0, -59440, 270)
    SetChrPos(0x104, 82020, 0, -61450, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x8, 80230, 0, -59410, 270)
    SetChrPos(0xA, 79030, 0, -59770, 270)
    SetChrPos(0xB, 80710, 0, -61590, 270)
    SetChrPos(0x9, 79590, 0, -60950, 270)
    SetChrPos(0x17, 82830, 0, -65010, 270)
    SetChrPos(0x13, 81290, 0, -65700, 270)
    SetChrPos(0x12, 83000, 0, -66520, 270)
    SetChrPos(0x14, 81230, 0, -64459, 270)
    Sleep(1000)

    ChrTalk(
        0x108,
        (
            "#074F规则变为团体赛，\x01",
            "又破例允许罪犯参加比赛……\x02\x03",
            "#070F真是什么事情都可能发生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "真是宽容的公爵大人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#2P不、不是笑的时候吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F我也觉得不应该变成这样……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FE)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_6090 end

    def Function_29_630F(): pass

    label("Function_29_630F")

    EventBegin(0x0)
    OP_6D(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 81880, 0, -59420, 270)
    SetChrPos(0x102, 82470, 0, -60720, 270)
    SetChrPos(0x108, 82960, 0, -59440, 270)
    SetChrPos(0x104, 82020, 0, -61450, 270)
    SetChrPos(0x8, 80230, 0, -59410, 270)
    SetChrPos(0xA, 79030, 0, -59770, 270)
    SetChrPos(0xB, 80710, 0, -61590, 270)
    SetChrPos(0x9, 79590, 0, -60950, 270)
    SetChrPos(0x16, 72110, 0, -61480, 90)
    SetChrPos(0xF, 72060, 0, -62470, 90)
    SetChrPos(0x10, 71980, 0, -63590, 90)
    SetChrPos(0x11, 72090, 0, -64519, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x17, 82830, 0, -65010, 270)
    SetChrPos(0x13, 81290, 0, -65700, 270)
    SetChrPos(0x12, 83000, 0, -66520, 270)
    SetChrPos(0x14, 81790, 0, -63840, 270)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#505F#2P哈啊～……\x01",
            "那些空贼真的赢了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F按他们的实力来说，\x01",
            "这也是合理的结果啊。\x02\x03",
            "#017F不过，万一他们获得冠军，\x01",
            "那该怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "招待空贼进城参加晚宴吗。\x02\x03",
            "一定会是很有趣的情景呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#2P这种事在发生之前，\x01",
            "一定会被我们阻止的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不管怎么说，强敌又多了一组啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6651():
        OP_6D(79710, 0, -62800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6651)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    def lambda_66A9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_66A9)

    def lambda_66BB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_66BB)

    def lambda_66CD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_66CD)

    def lambda_66DF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_66DF)

    def lambda_66F1():

        label("loc_66F1")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_66F1")

    QueueWorkItem2(0x16, 2, lambda_66F1)

    def lambda_6702():
        OP_8E(0xFE, 0x1325E, 0x0, 0xFFFEFF8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_6702)
    Sleep(300)

    def lambda_6722():

        label("loc_6722")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_6722")

    QueueWorkItem2(0xF, 2, lambda_6722)

    def lambda_6733():
        OP_8E(0xFE, 0x12D9A, 0x0, 0xFFFEFEB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_6733)
    Sleep(300)

    def lambda_6753():

        label("loc_6753")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_6753")

    QueueWorkItem2(0x10, 2, lambda_6753)

    def lambda_6764():
        OP_8E(0xFE, 0x12DCC, 0x0, 0xFFFF033B, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_6764)
    Sleep(300)

    def lambda_6784():

        label("loc_6784")

        TurnDirection(0xFE, 0x16, 0)
        OP_48()
        Jump("loc_6784")

    QueueWorkItem2(0x11, 2, lambda_6784)
    SetChrFlags(0x11, 0x40)

    def lambda_679A():
        OP_8E(0xFE, 0x131AA, 0x0, 0xFFFF0560, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_679A)

    def lambda_67B5():

        label("loc_67B5")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_67B5")

    QueueWorkItem2(0x8, 1, lambda_67B5)

    def lambda_67C6():

        label("loc_67C6")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_67C6")

    QueueWorkItem2(0xA, 1, lambda_67C6)

    def lambda_67D7():

        label("loc_67D7")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_67D7")

    QueueWorkItem2(0xB, 1, lambda_67D7)

    def lambda_67E8():

        label("loc_67E8")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_67E8")

    QueueWorkItem2(0x9, 1, lambda_67E8)

    def lambda_67F9():

        label("loc_67F9")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_67F9")

    QueueWorkItem2(0x101, 1, lambda_67F9)

    def lambda_680A():

        label("loc_680A")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_680A")

    QueueWorkItem2(0x102, 1, lambda_680A)

    def lambda_681B():

        label("loc_681B")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_681B")

    QueueWorkItem2(0x108, 1, lambda_681B)

    def lambda_682C():

        label("loc_682C")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_682C")

    QueueWorkItem2(0x104, 1, lambda_682C)

    def lambda_683D():

        label("loc_683D")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_683D")

    QueueWorkItem2(0x17, 1, lambda_683D)

    def lambda_684E():

        label("loc_684E")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_684E")

    QueueWorkItem2(0x12, 1, lambda_684E)

    def lambda_685F():

        label("loc_685F")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_685F")

    QueueWorkItem2(0x13, 1, lambda_685F)

    def lambda_6870():

        label("loc_6870")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6870")

    QueueWorkItem2(0x14, 1, lambda_6870)
    WaitChrThread(0x16, 0x3)

    ChrTalk(
        0x16,
        (
            "#5P可恶……\x01",
            "竟然输给了罪犯……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x17, 0xFF)
    OP_8E(0x17, 0x13A10, 0x0, 0xFFFF033B, 0x7D0, 0x0)

    ChrTalk(
        0x17,
        "#2P哎，别这么泄气了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2P只是因为他们擅长小队作战罢了，\x01",
            "在这点上我们还是有差距的。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x16, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)

    def lambda_6959():

        label("loc_6959")

        TurnDirection(0xFE, 0x17, 400)
        OP_48()
        Jump("loc_6959")

    QueueWorkItem2(0xF, 1, lambda_6959)

    def lambda_696A():

        label("loc_696A")

        TurnDirection(0xFE, 0x17, 400)
        OP_48()
        Jump("loc_696A")

    QueueWorkItem2(0x10, 1, lambda_696A)

    def lambda_697B():

        label("loc_697B")

        TurnDirection(0xFE, 0x17, 400)
        OP_48()
        Jump("loc_697B")

    QueueWorkItem2(0x11, 1, lambda_697B)
    OP_8C(0x16, 90, 400)

    ChrTalk(
        0x16,
        (
            "#5P不……\x01",
            "问题在于我们的实力不够。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P回到部队之后，\x01",
            "训练量要增加了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "下面宣布第四场比赛的\x01",
            "对阵双方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南边，苍之组——\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国境警卫队７连所属，\x01",
            "贝伦中尉等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_6AD6():

        label("loc_6AD6")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6AD6")

    QueueWorkItem2(0x8, 1, lambda_6AD6)

    def lambda_6AE7():

        label("loc_6AE7")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6AE7")

    QueueWorkItem2(0xA, 1, lambda_6AE7)

    def lambda_6AF8():

        label("loc_6AF8")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6AF8")

    QueueWorkItem2(0xB, 1, lambda_6AF8)

    def lambda_6B09():

        label("loc_6B09")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6B09")

    QueueWorkItem2(0x9, 1, lambda_6B09)

    def lambda_6B1A():

        label("loc_6B1A")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6B1A")

    QueueWorkItem2(0x101, 1, lambda_6B1A)

    def lambda_6B2B():

        label("loc_6B2B")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6B2B")

    QueueWorkItem2(0x102, 1, lambda_6B2B)

    def lambda_6B3C():

        label("loc_6B3C")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6B3C")

    QueueWorkItem2(0x108, 1, lambda_6B3C)

    def lambda_6B4D():

        label("loc_6B4D")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6B4D")

    QueueWorkItem2(0x104, 1, lambda_6B4D)

    ChrTalk(
        0x16,
        "#5P该你们出场了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P剩下的对手只有那些家伙了。\x01",
            "一定不要输给他们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2P知道了……\x01",
            "就让他们看看我们正规军的军魂吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x17, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_8C(0x17, 90, 400)

    ChrTalk(
        0x17,
        "#5P伙计们，上吧！\x02",
    )

    CloseMessageWindow()

    def lambda_6C40():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6C40)

    def lambda_6C4E():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6C4E)
    TurnDirection(0x14, 0x17, 400)

    ChrTalk(
        0x12,
        "#2P#1K是的，长官！\x02",
    )


    ChrTalk(
        0x13,
        "#1P#1K是的，长官！\x02",
    )


    ChrTalk(
        0x14,
        "#2P#1K是的，长官！\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    def lambda_6CA7():

        label("loc_6CA7")

        TurnDirection(0xFE, 0x17, 400)
        OP_48()
        Jump("loc_6CA7")

    QueueWorkItem2(0x16, 1, lambda_6CA7)
    OP_43(0x17, 0x1, 0x0, 0x1E)
    Sleep(300)
    OP_43(0x14, 0x1, 0x0, 0x1E)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x1E)
    OP_43(0x12, 0x1, 0x0, 0x1E)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北边，红之组——\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "王国军情报部特务部队所属，\x01",
            "洛伦斯少尉等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x104, 0xFF)
    OP_6D(82090, 0, -59990, 1000)

    ChrTalk(
        0x101,
        "#005F#2P是他们……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F洛伦斯少尉……\x01",
            "难道是那个时候的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_630F end

    def Function_30_6E03(): pass

    label("Function_30_6E03")

    OP_8E(0xFE, 0x1359C, 0x0, 0xFFFF0B00, 0xBB8, 0x0)
    OP_8E(0xFE, 0x12282, 0x0, 0xFFFF0A1A, 0xBB8, 0x0)

    def lambda_6E31():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6E31)
    OP_8E(0xFE, 0x11A3A, 0x0, 0xFFFF0A92, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_6E03 end

    def Function_31_6E57(): pass

    label("Function_31_6E57")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(76690, 0, -61440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 76260, 0, -60960, 270)
    SetChrPos(0x108, 77340, 0, -60400, 270)
    SetChrPos(0x101, 76310, 0, -62260, 270)
    SetChrPos(0x104, 77550, 0, -61920, 270)
    SetChrPos(0x8, 80230, 0, -59410, 270)
    SetChrPos(0xA, 79030, 0, -59770, 270)
    SetChrPos(0xB, 80710, 0, -61590, 270)
    SetChrPos(0x9, 79590, 0, -60950, 270)
    SetChrPos(0x16, 77000, 0, -64940, 270)
    SetChrPos(0xF, 77630, 0, -66970, 270)
    SetChrPos(0x10, 78610, 0, -66490, 270)
    SetChrPos(0x11, 79150, 0, -65459, 270)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#005F#1P怎、怎么会……\x01",
            "简直是压倒性的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F哦～真强啊。\x02\x03",
            "那个小组，\x01",
            "预选赛的时候是三个人参赛的。\x01",
            "也曾想到他们会增加一个人……\x02\x03",
            "原来还准备了这样的王牌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#032F与我和艾丝蒂尔君他们一样，\x01",
            "是从正式赛才开始参赛的呢。\x02\x03",
            "#035F呵呵……\x01",
            "还有这样的隐藏人物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#514F……刚才的剑法……是………\x02",
    )

    CloseMessageWindow()

    def lambda_7137():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7137)

    def lambda_7145():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7145)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F哎……？\x02\x03",
            "约修亚，你怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F难道………………\x01",
            "………可是………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F约修亚……………？\x01",
            "……………约修亚！\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F啊……\x02\x03",
            "#019F没关系……什么事也没有。\x02\x03",
            "那个的剑法太漂亮了，\x01",
            "所以看得有点入迷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵，不愧是约修亚。\x01",
            "感性还真是丰富啊。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "经过刚才的激战，\x01",
            "武术大会正式赛首日的比赛就全部结束了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "晋级第二轮的队伍是——\x01",
            "克鲁茨、多伦、\x01",
            "金以及洛伦斯四个小组！\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "期待他们以后的精彩表现！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到奖金\x07\x04",
            "２００００\x07\x00",
            "米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    AddMira(20000)
    ClearMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6E57 end

    def Function_32_7416(): pass

    label("Function_32_7416")

    EventBegin(0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 320, 0, -470, 0)

    NpcTalk(
        0x1D,
        "女孩的声音",
        "#2P啊，是小艾你们啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(560, 0, 3040, 0)
    SetChrPos(0x101, 9740, 0, 4610, 0)
    SetChrPos(0x102, 10040, 0, 5710, 0)
    SetChrPos(0x108, 10970, 0, 5750, 0)
    SetChrPos(0x104, 10990, 0, 4550, 0)
    OP_8E(0x1D, 0x104, 0x0, 0xBC2, 0xBB8, 0x0)
    TurnDirection(0x1D, 0x101, 400)

    ChrTalk(
        0x101,
        "#501F#1P啊，这不是朵洛希嘛！\x02",
    )

    CloseMessageWindow()

    def lambda_754C():
        OP_8E(0xFE, 0x582, 0x0, 0x9D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_754C)
    Sleep(300)

    def lambda_756C():
        OP_8E(0xFE, 0x550, 0x0, 0xDE8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_756C)
    Sleep(300)

    def lambda_758C():
        OP_8E(0xFE, 0xA78, 0x0, 0xA50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_758C)
    Sleep(300)

    def lambda_75AC():
        OP_8E(0xFE, 0xA46, 0x0, 0xE9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_75AC)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F好久不见了……\x01",
            "其实也没有相隔多长时间吧。\x02\x03",
            "在蔡斯还碰见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F是啊是啊～\x02\x03",
            "还能够活着见到你们，\x01",
            "真是做梦也没有想到呢～\x02\x03",
            "因为你们好像乘坐工房的飞艇，\x01",
            "到十分危险的地方去了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F危险的地方……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#030F哦～真是有趣嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F哇哇，朵洛希！\x01",
            "这件事以后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153F哎……？\x02\x03",
            "对了对了，\x01",
            "这两位好像在哪里见过呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F呵呵……\x01",
            "我们在柏斯市里见过一次面哦。\x02\x03",
            "能再见面真是让人高兴呢。\x01",
            "这位富有个性魅力的小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F至于我，则是在温泉村附近\x01",
            "曾和你擦肩而过的那个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F啊啊～我想起来了！\x02\x03",
            "喝霸王酒的客人先生，\x01",
            "和东方装束的熊先生！\x02\x03",
            "#150F小艾，你们就是\x01",
            "和他们一起参加武术大会的吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是拜托过这位金先生，\x01",
            "才从正式赛开始参加的。\x02\x03",
            "对了，朵洛希小姐。\x01",
            "今天你也是来取材的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150F嗯～直到昨天\x01",
            "都在对别的事情进行取材呢～\x02\x03",
            "今天早上碰到奈尔前辈，\x01",
            "才听说小艾你们来参加武术大会的事～\x01",
            "　\x02\x03",
            "#151F不过，真是和前辈所说的一样，\x01",
            "真是很强的小组呢！\x02\x03",
            "这下说不定能拍出很棒的照片呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈哈，那真是让人期待啊。\x02\x03",
            "#004F哎……说起来，\x01",
            "奈尔没和你一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#154F嗯，奈尔前辈嘛～\x01",
            "好像有非常重要的事情要调查呢～\x02\x03",
            "昨天整个晚上好像\x01",
            "都在和大堆大堆的资料作战呢～\x02\x03",
            "今天又去找老朋友谈话去了～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150F啊，对了对了，\x01",
            "我带来了前辈给小艾你们的口信哦。\x02\x03",
            "说是让你们今天傍晚的时候，\x01",
            "到编辑部来一趟～\x02\x03",
            "看起来，好像是很重要的事情吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯……我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F比赛结束之后就去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#037F很重要的事情……\x01",
            "嘿嘿～～感觉有点可疑呢。\x02\x03",
            "#031F真是让人在意啊。\x01",
            "咕噜咕噜咕噜～喵喵～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(
        0x101,
        (
            "#580F这、这可不行。\x01",
            "这件事跟大赖皮蛋没有关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F真无情啊，艾丝蒂尔君！\x02\x03",
            "昨天的比赛中，\x01",
            "我们俩的感情明明那样激情地燃烧……\x02\x03",
            "用不到我的时候，\x01",
            "就像扔垃圾一样把我抛弃掉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#582F我都说啦！\x01",
            "不要用那种容易让人误解的说话方式！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153F哇哇，小艾，\x01",
            "你什么时候和这位帅哥……？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)

    ChrTalk(
        0x101,
        "#509F这种鬼话你也相信！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F啊，这样的话～\x01",
            "为了能找到好的摄影位置，\x01",
            "我现在就去观众席了～\x02\x03",
            "我支持小艾你们，\x01",
            "一定要加油啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 270, 400)

    def lambda_801D():
        OP_6D(-2000, 0, 3110, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_801D)

    def lambda_8035():
        OP_8E(0xFE, 0xFFFFD3DC, 0x0, 0x1716, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_8035)
    WaitChrThread(0x1D, 0x3)
    Sleep(1500)
    OP_6D(1820, 0, 2900, 1500)

    ChrTalk(
        0x108,
        (
            "#073F怎么说呢……\x01",
            "真是有个性的小姑娘啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80A7():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80A7)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼～……\x02\x03",
            "要同时对付奥利维尔和朵洛希，\x01",
            "还真是够累人的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈，这也是为了\x01",
            "缓解一下比赛前的紧张气氛嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F朵洛希小姐，\x01",
            "作为摄影师可是相当的厉害哦。\x02\x03",
            "最近《利贝尔通讯》上的照片\x01",
            "都是她亲手拍摄的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F哦，这还真是厉害啊。\x02\x03",
            "#071F那么，我们就在照相机前\x01",
            "好好地表现一番给他们看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯……没错。\x02\x03",
            "虽然还不知道会和谁相遇，\x01",
            "不过不打起十分的精神来不行啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x624)
    OP_28(0x48, 0x1, 0x8)
    OP_1B(0x1, 0x0, 0xFFFF)
    OP_1B(0x2, 0x0, 0xFFFF)
    SetChrFlags(0x1D, 0x80)
    EventEnd(0x0)
    Return()

    # Function_32_7416 end

    def Function_33_82C5(): pass

    label("Function_33_82C5")

    EventBegin(0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -320, 0, -470, 0)

    NpcTalk(
        0x1D,
        "女孩的声音",
        "#1P啊，是小艾你们啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(-2000, 0, 3040, 0)
    SetChrPos(0x101, -9740, 0, 4610, 90)
    SetChrPos(0x102, -10040, 0, 5710, 90)
    SetChrPos(0x108, -10970, 0, 5750, 90)
    SetChrPos(0x104, -10990, 0, 4550, 90)
    OP_8E(0x1D, 0xFFFFFEFC, 0x0, 0xBC2, 0xBB8, 0x0)
    TurnDirection(0x1D, 0x101, 400)

    ChrTalk(
        0x101,
        "#501F#4P啊，这不是朵洛希嘛！\x02",
    )

    CloseMessageWindow()

    def lambda_83FB():
        OP_8E(0xFE, 0xFFFFFA7E, 0x0, 0x9D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_83FB)
    Sleep(300)

    def lambda_841B():
        OP_8E(0xFE, 0xFFFFFAB0, 0x0, 0xDE8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_841B)
    Sleep(300)

    def lambda_843B():
        OP_8E(0xFE, 0xFFFFF588, 0x0, 0xA50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_843B)
    Sleep(300)

    def lambda_845B():
        OP_8E(0xFE, 0xFFFFF5BA, 0x0, 0xE9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_845B)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F#5P好久不见了……\x01",
            "其实也没有相隔多长时间吧。\x02\x03",
            "在蔡斯还碰见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F#4P是啊是啊～\x02\x03",
            "还能够活着见到你们，\x01",
            "真是做梦也没有想到呢～\x02\x03",
            "因为你们好像乘坐工房的飞艇，\x01",
            "到十分危险的地方去了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F#5P危险的地方……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#030F#5P哦～真是有趣嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#5P哇哇，朵洛希！\x01",
            "这件事以后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153F#4P哎……？\x02\x03",
            "对了对了，\x01",
            "这两位好像在哪里见过呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#5P呵呵……\x01",
            "我们在柏斯市里见过一次面哦。\x02\x03",
            "能再见面真是让人高兴呢。\x01",
            "这位富有个性魅力的小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#5P至于我，则是在温泉村附近\x01",
            "曾和你擦肩而过的那个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F#4P啊啊～我想起来了！\x02\x03",
            "喝霸王酒的客人先生，\x01",
            "和东方装束的熊先生！\x02\x03",
            "#150F小艾，你们就是\x01",
            "和他们一起参加武术大会的吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5P我们是拜托过这位金先生，\x01",
            "才从正式赛开始参加的。\x02\x03",
            "对了，朵洛希小姐。\x01",
            "今天你也是来取材的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150F#4P嗯～直到昨天\x01",
            "都在对别的事情进行取材呢～\x02\x03",
            "今天早上碰到奈尔前辈，\x01",
            "才听说小艾你们来参加武术大会的事～\x01",
            "　\x02\x03",
            "#151F不过，真是和前辈所说的一样，\x01",
            "真是很强的小组呢！\x02\x03",
            "这下说不定能拍出很棒的照片呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#5P啊哈哈，那真是让人期待啊。\x02\x03",
            "#004F哎……说起来，\x01",
            "奈尔没和你一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#154F#4P嗯，奈尔前辈嘛～\x01",
            "好像有非常重要的事情要调查呢～\x02\x03",
            "昨天整个晚上好像\x01",
            "都在和大堆大堆的资料作战呢～\x02\x03",
            "今天又去找老朋友谈话去了～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150F#4P啊，对了对了，\x01",
            "我带来了前辈给小艾你们的口信哦。\x02\x03",
            "说是让你们今天傍晚的时候，\x01",
            "到编辑部来一趟～\x02\x03",
            "看起来，好像是很重要的事情吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P嗯……我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#5P比赛结束之后就去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#037F#5P很重要的事情……\x01",
            "嘿嘿～～感觉有点可疑呢。\x02\x03",
            "#031F真是让人在意啊。\x01",
            "咕噜咕噜咕噜～喵喵～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(
        0x101,
        (
            "#580F#6P这、这可不行。\x01",
            "这件事跟大赖皮蛋没有关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#5P真无情啊，艾丝蒂尔君！\x02\x03",
            "昨天的比赛中，\x01",
            "我们俩的感情明明那样激情地燃烧……\x02\x03",
            "用不到我的时候，\x01",
            "就像扔垃圾一样把我抛弃掉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#582F#6P我都说啦！\x01",
            "不要用那种容易让人误解的说话方式！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153F#4P哇哇，小艾，\x01",
            "你什么时候和这位帅哥……？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 600)

    ChrTalk(
        0x101,
        "#509F#5P这种鬼话你也相信！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F#4P啊，这样的话～\x01",
            "为了能找到好的摄影位置，\x01",
            "我现在就去观众席了～\x02\x03",
            "我支持小艾你们，\x01",
            "一定要加油啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 90, 400)

    def lambda_8F17():
        OP_6D(2000, 0, 3110, 2000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_8F17)

    def lambda_8F2F():
        OP_8E(0xFE, 0x2C24, 0x0, 0x1716, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_8F2F)
    WaitChrThread(0x1D, 0x3)
    Sleep(1500)
    OP_6D(-1920, 0, 3060, 1500)

    ChrTalk(
        0x108,
        (
            "#073F怎么说呢……\x01",
            "真是有个性的小姑娘啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FA1():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FA1)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼～……\x02\x03",
            "要同时对付奥利维尔和朵洛希，\x01",
            "还真是够累人的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈，这也是为了\x01",
            "缓解一下比赛前的紧张气氛嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F朵洛希小姐，\x01",
            "作为摄影师可是相当的厉害哦。\x02\x03",
            "最近《利贝尔通讯》上的照片\x01",
            "都是她亲手拍摄的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F哦，这还真是厉害啊。\x02\x03",
            "#071F那么，我们就在照相机前\x01",
            "好好地表现一番给他们看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯……没错。\x02\x03",
            "虽然还不知道会和谁相遇，\x01",
            "不过不打起十分的精神来不行啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x624)
    OP_28(0x48, 0x1, 0x8)
    OP_1B(0x1, 0x0, 0xFFFF)
    OP_1B(0x2, 0x0, 0xFFFF)
    SetChrFlags(0x1D, 0x80)
    EventEnd(0x0)
    Return()

    # Function_33_82C5 end

    def Function_34_918E(): pass

    label("Function_34_918E")

    OP_A2(0x3F0)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_918E end

    def Function_35_919B(): pass

    label("Function_35_919B")

    EventBegin(0x0)
    OP_6D(74460, 0, -62460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF, 87610, 0, -63640, 270)
    SetChrPos(0x10, 87610, 0, -62310, 270)
    SetChrPos(0x1A, 87610, 0, -63200, 270)
    SetChrPos(0x1B, 87610, 0, -63200, 270)
    SetChrPos(0x1C, 87610, 0, -63200, 270)
    SetChrPos(0x19, 87610, 0, -63200, 270)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x101, 81280, 0, -63460, 270)
    SetChrPos(0x102, 81350, 0, -62190, 270)
    SetChrPos(0x108, 80030, 0, -62140, 135)
    SetChrPos(0x104, 79980, 0, -63500, 90)
    FadeToBright(1000, 0)
    OP_6D(79710, 0, -62840, 2500)

    ChrTalk(
        0x101,
        (
            "#505F嗯……动作真是慢啊。\x02\x03",
            "比赛马上就要开始了，\x01",
            "另外一组的队员怎么还不来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F确实很奇怪。\x02\x03",
            "是因为有事情迟到了，\x01",
            "还是……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "男人的声音",
        "#1P喂，还不赶快走！\x02",
    )

    CloseMessageWindow()

    def lambda_93B2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_93B2)

    def lambda_93C0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93C0)

    def lambda_93CE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_93CE)

    NpcTalk(
        0x1A,
        "粗鲁的声音",
        (
            "#1P真是罗嗦呀。\x01",
            "也不用这么急吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "青年的声音",
        (
            "#1P啊啊……\x01",
            "为什么会变成这个样子呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "女孩的声音",
        "#1P吉尔哥，打起精神来啊！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "女孩的声音",
        (
            "#1P遇到那些家伙的时候，\x01",
            "你这个样子该怎么办啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x19, 0x80)

    def lambda_958D():
        OP_6D(81720, 0, -62380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_958D)

    def lambda_95A5():
        OP_8E(0xFE, 0x142DA, 0x0, 0xFFFF0EA2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_95A5)

    def lambda_95C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_95C0)
    Sleep(300)

    def lambda_95D7():
        OP_8E(0xFE, 0x1449C, 0x0, 0xFFFF0A42, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_95D7)

    def lambda_95F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_95F2)
    Sleep(300)

    def lambda_9609():
        OP_8E(0xFE, 0x142DA, 0x0, 0xFFFF065A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9609)

    def lambda_9624():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_9624)
    Sleep(300)

    def lambda_963B():
        OP_8E(0xFE, 0x14654, 0x0, 0xFFFF123A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_963B)

    def lambda_9656():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_9656)
    Sleep(500)

    def lambda_966D():
        OP_8E(0xFE, 0x14E10, 0x0, 0xFFFF0768, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_966D)

    def lambda_9688():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_9688)
    Sleep(300)

    def lambda_969F():
        OP_8E(0xFE, 0x14E10, 0x0, 0xFFFF0C9A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_969F)

    def lambda_96BA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_96BA)
    WaitChrThread(0x19, 0x1)
    TurnDirection(0x19, 0x108, 0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#004F#5P啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1A, 0x2)

    ChrTalk(
        0x1A,
        "#192F#4P你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#5P是你们这一组啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5P呵呵，\x01",
            "所以才会来得这么晚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#200F#4P哼……\x01",
            "今天的对手原来不是你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#210F#4P哼……运气真不错啊。\x02\x03",
            "本来还想如果碰上你们的话，\x01",
            "一定要让那个没脑子的女人\x01",
            "知道我们的厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        (
            "喂！\x01",
            "不要乱说话！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "警卫兵",
        (
            "多亏了公爵大人的好意，\x01",
            "你们才能来参加比赛，难道忘了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_990D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_990D)

    def lambda_991B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_991B)

    def lambda_9929():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9929)
    OP_8C(0x1A, 90, 400)

    ChrTalk(
        0x1A,
        (
            "#191F#5P哎呀哎呀，士兵小哥。\x01",
            "不要这么生气嘛。\x02\x03",
            "自从被你们带到这里来，\x01",
            "我们不是一直老老实实的吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        (
            "希望你们在回到牢房之前，\x01",
            "最好给我保持这个态度。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        (
            "你们也是，\x01",
            "不要让这些家伙随便乱说话啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        "如果弄出麻烦的事情来就坏了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P本来就不是在弄麻烦的事情……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "警卫兵",
        (
            "你们最好给我记住，\x01",
            "竞技场可是有一个中队的兵力在警备着。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "警卫兵",
        "别想打逃跑的主意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#202F#5P知道啦。\x01",
            "我们不会做这种愚蠢的事情的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#211F#5P哼～\x01",
            "真是碍眼啊，还不赶快走？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        "你这个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    NpcTalk(
        0x10,
        "警卫兵",
        "不要中了小鬼的挑衅啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)

    NpcTalk(
        0x10,
        "警卫兵",
        (
            "听好了，\x01",
            "不要动奇怪的心思哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)

    def lambda_9C84():
        OP_8E(0xFE, 0x1563A, 0x0, 0xFFFF0768, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9C84)

    def lambda_9C9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_9C9F)
    OP_8C(0x10, 90, 400)

    def lambda_9CB8():
        OP_8E(0xFE, 0x1563A, 0x0, 0xFFFF0C9A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9CB8)

    def lambda_9CD3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9CD3)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_6D(80720, 0, -62380, 1000)

    ChrTalk(
        0x101,
        (
            "#505F#5P喂……\x01",
            "到底是怎么回事？\x02\x03",
            "为什么你们会来参加武术大会？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D63():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9D63)

    def lambda_9D71():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9D71)

    def lambda_9D7F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9D7F)

    def lambda_9D8D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9D8D)

    ChrTalk(
        0x102,
        (
            "#012F#5P真的是杜南公爵让你们参加的吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#200F没错，让我们参加比赛的就是\x01",
            "那个头发秀逗身材胖胖的什么公爵。\x01",
            "　\x02\x03",
            "如果取得武术大会的优胜，\x01",
            "我们就可以减刑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P真、真是难以置信啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F嗯～没想到在这个法治国家，\x01",
            "也有这样的独断专制啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#5P哈·哈·哈，\x01",
            "真是乱来的公爵大人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#197F算了，好不容易得到的批准。\x02\x03",
            "在判决执行，进棺材之前，\x01",
            "至少能做些什么事情。\x02\x03",
            "当然……\x01",
            "不仅仅是为了这个理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P哎……怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#214F真罗嗦，这和你们没有关系吧。\x01",
            "　\x02\x03",
            "是对我们来说有着特殊意义的事情。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5P不是为了和我们交战\x01",
            "才来参加这次武术大会的话……\x02\x03",
            "是打算和特务兵的人交手吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#213F为、为什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#196F唔……你说得没错。\x02\x03",
            "那些家伙装作我们的同伴，\x01",
            "但却陷害我们、让我们落到这种田地。\x02\x03",
            "为了扩大他们情报部的势力而利用我们，\x01",
            "等我们没有利用价值之后就过河拆桥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#203F虽然这次被骗，\x01",
            "使我们可以称得上是白痴中的白痴……\x02\x03",
            "不过，实在是令人不爽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#5P嗯～没错……\x02\x03",
            "这样想的话，\x01",
            "你们也真是可怜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#214F所以～\x01",
            "别用那么哀怜的眼神看着我们啦！\x02\x03",
            "你们还欠了我们人情呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#5P哎？\x02\x03",
            "欠了你们人情……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#200F哼哼，是说之前的事情啦。\x02\x03",
            "如果我们把要塞里的事情告诉那些家伙，\x01",
            "我看你们还能站在这里比赛吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#191F就是因为痛恨那些家伙，\x01",
            "所以才没有把你们的事情说出去。\x02\x03",
            "哇哈哈，感谢我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#5P呜～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#5P确实如此啊……\x01",
            "十分感谢你们能对那件事保持沉默。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#5P好像是很有趣的事情呢。\x02\x03",
            "到底是什么好玩的事情，\x01",
            "也快点和哥哥我说说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#582F#6P哼，什么事也没有！\x02",
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A519():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A519)
    OP_6D(79710, 0, -62380, 1000)

    ChrTalk(
        0x108,
        (
            "#073F哦……\x02\x03",
            "那边开始嘈杂起来了，\x01",
            "比赛应该马上就要开始了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A586():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A586)

    def lambda_A594():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A594)

    def lambda_A5A2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A5A2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "各位……\x01",
            "让你们久等了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我宣布，武术大会正式赛，\x01",
            "第二天的比赛现在开始！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那么，我们立刻公布\x01",
            "参加第五场比赛的小组吧。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南边，苍之组——\x01",
            "来自卡尔瓦德共和国的武术家，\x01",
            "金选手等四人组！\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北边，红之组——\x01",
            "游击士协会格兰赛尔支部，\x01",
            "克鲁茨选手等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x101,
        (
            "#005F来了！\x02\x03",
            "而且对手是卡露娜姐姐他们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……强敌啊。\x02\x03",
            "希望我们不会拖金先生的后腿就好了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F不要想得那么多。\x02\x03",
            "你们的实力，\x01",
            "已经非常接近正游击士了。\x02\x03",
            "剩下的就是胜利的气势了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A896():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A896)

    def lambda_A8A4():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8A4)

    def lambda_A8B2():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A8B2)

    ChrTalk(
        0x101,
        "#006F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会努力的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F哈·哈·哈。\x01",
            "那么我们向战场上进发吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1A, 0x40)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x19, 0x40)
    OP_8C(0x1A, 270, 0)
    OP_8C(0x1C, 270, 0)
    OP_43(0x1A, 0x0, 0x0, 0x2)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    OP_43(0x1C, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    OP_6D(80480, 0, -62830, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 80480, 0, -62830, 270)
    SetChrPos(0x102, 80480, 0, -62830, 270)
    SetChrPos(0x108, 80480, 0, -62830, 270)
    SetChrPos(0x104, 80480, 0, -62830, 270)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_35_919B end

    def Function_36_A9FD(): pass

    label("Function_36_A9FD")

    OP_8E(0xFE, 0x14E10, 0x0, 0xFFFF095C, 0xBB8, 0x0)

    def lambda_AA17():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_AA17)
    OP_8E(0xFE, 0x1568A, 0x0, 0xFFFF09DE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_A9FD end

    def Function_37_AA3D(): pass

    label("Function_37_AA3D")

    EventBegin(0x0)
    OP_6D(80720, 0, -62380, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 81280, 0, -63460, 90)
    SetChrPos(0x102, 81350, 0, -62190, 90)
    SetChrPos(0x108, 80030, 0, -62140, 90)
    SetChrPos(0x104, 79980, 0, -63500, 90)
    SetChrPos(0x1A, 82650, 0, -61790, 270)
    SetChrPos(0x1B, 83100, 0, -62910, 270)
    SetChrPos(0x1C, 82650, 0, -63910, 270)
    SetChrPos(0x19, 84010, 0, -62350, 270)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x19, 0x80)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        "#192F哦～干得不错嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#202F嗯嗯。\x01",
            "光是看看就让我很兴奋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#212F哼……\x01",
            "这场比赛打得还可以嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#5P啊哈哈，多谢⊙\x02\x03",
            "#004F哎，怎么了？\x01",
            "你也会说称赞的话啊。\x02\x03",
            "难道是发烧了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#214F我、我才不会\x01",
            "称赞你这种黄毛丫头呢！\x02\x03",
            "我只是不想看到把我们逼到绝境的家伙\x01",
            "就这么随便地输掉而已！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#5P哼……\x01",
            "还真是个嘴硬的丫头啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F#5P算了算了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1C, 400)

    ChrTalk(
        0x102,
        (
            "#019F#5P……谢谢你们。\x02\x03",
            "不管怎么说，\x01",
            "你们是在支持我们啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x102, 400)

    ChrTalk(
        0x1C,
        "#414F……啊…………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x1C,
        (
            "#216F我、我刚才不是说了吗！？\x01",
            "不是在支持你们啦！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#5P（嗯……？）\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "下面宣布第六场比赛的\x01",
            "对阵双方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南边，苍之组——\x01",
            "空贼团『卡普亚一家』所属，\x01",
            "多伦选手等四人组！\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北边，红之组——\x01",
            "王国军情报部特务部队所属，\x01",
            "洛伦斯少尉等四人组！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TurnDirection(0x1A, 0x1C, 400)

    ChrTalk(
        0x1A,
        "#196F哦，终于来啦！\x02",
    )

    CloseMessageWindow()

    def lambda_AF96():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_AF96)

    def lambda_AFA4():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_AFA4)

    def lambda_AFB2():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_AFB2)
    Sleep(400)

    ChrTalk(
        0x1B,
        (
            "#201F要让那些嚣张的黑小子\x01",
            "好好见识一下我们的厉害！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P这也是一种缘分吧。\x02\x03",
            "我支持你们，一定要加油哦！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B069():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_B069)

    def lambda_B077():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_B077)

    def lambda_B085():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B085)

    def lambda_B093():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B093)

    ChrTalk(
        0x102,
        (
            "#012F#5P要小心对方的队长。\x02\x03",
            "只要能限制他的自由行动，\x01",
            "就一定会有胜算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#414F嗯、嗯……\x02\x03",
            "#214F……不对！\x01",
            "谁、谁要你关心了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3F1)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_AA3D end

    def Function_38_B175(): pass

    label("Function_38_B175")

    EventBegin(0x0)
    OP_6D(75020, 0, -60990, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 75990, 0, -61820, 270)
    SetChrPos(0x102, 75110, 0, -61050, 270)
    SetChrPos(0x108, 75980, 0, -60520, 270)
    SetChrPos(0x104, 77190, 0, -60900, 270)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F啊啊……还是输了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F比赛进行到一半之前，\x01",
            "那些空贼的形势还是不错的。\x02\x03",
            "在那个红面具的队长出动之后，\x01",
            "他们就开始溃败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F嗯……不知道底细的对手啊。\x02\x03",
            "而且他肯定没有尽全力，\x01",
            "以免被别人知道他真正的实力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F哎……\x01",
            "刚才那不是他的全部实力吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……应该不是。\x02\x03",
            "最后的剑技收招之后，\x01",
            "集中的剑气也没有因此而衰弱。\x02\x03",
            "肯定还留有余力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F真、真是难以相信……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x19, 0x40)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1A, 72050, 0, -63520, 90)
    SetChrPos(0x1B, 72050, 0, -63520, 90)
    SetChrPos(0x1C, 72050, 0, -63520, 90)
    SetChrPos(0x19, 72050, 0, -63520, 90)

    def lambda_B4AE():

        label("loc_B4AE")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_B4AE")

    QueueWorkItem2(0x101, 2, lambda_B4AE)

    def lambda_B4BF():

        label("loc_B4BF")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_B4BF")

    QueueWorkItem2(0x102, 2, lambda_B4BF)

    def lambda_B4D0():

        label("loc_B4D0")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_B4D0")

    QueueWorkItem2(0x108, 2, lambda_B4D0)

    def lambda_B4E1():

        label("loc_B4E1")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_B4E1")

    QueueWorkItem2(0x104, 2, lambda_B4E1)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x19, 0x80)

    def lambda_B506():
        OP_6D(75100, 0, -62310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B506)

    def lambda_B51E():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_B51E)

    def lambda_B52E():
        OP_8E(0xFE, 0x12E12, 0x0, 0xFFFF01B5, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_B52E)

    def lambda_B549():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_B549)
    Sleep(500)

    def lambda_B560():
        OP_8E(0xFE, 0x12B56, 0x0, 0xFFFF060A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_B560)

    def lambda_B57B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B57B)
    Sleep(400)

    def lambda_B592():
        OP_8E(0xFE, 0x12728, 0x0, 0xFFFF0506, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_B592)

    def lambda_B5AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_B5AD)
    Sleep(800)

    def lambda_B5C4():
        OP_8E(0xFE, 0x129E4, 0x0, 0xFFFF00A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_B5C4)

    def lambda_B5DF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B5DF)

    def lambda_B5F1():

        label("loc_B5F1")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_B5F1")

    QueueWorkItem2(0x19, 2, lambda_B5F1)
    WaitChrThread(0x1A, 0x3)

    ChrTalk(
        0x1A,
        "#197F#6P…………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 0x3)

    ChrTalk(
        0x1B,
        "#204F#5P…………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0x3)

    ChrTalk(
        0x1C,
        "#215F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#2P啊，那个……真是可惜呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#197F#6P不要说安慰的话……\x02\x03",
            "我们彻底失败了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#205F#5P可恶……\x01",
            "都是因为我的支援还太不成熟了……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x19, 0xFF)
    TurnDirection(0x1C, 0x1B, 400)

    ChrTalk(
        0x1C,
        (
            "#216F#2P不是吉尔哥的责任……！\x02\x03",
            "都是因为我没有阻止住\x01",
            "那家伙的突击啊……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#2P…………………………\x02\x03",
            "#007F哎，这也是没有办法的事。\x01",
            "胜负有时候也要看运气的。\x02\x03",
            "#006F你们三兄妹的仇，\x01",
            "明天的比赛里我们一定会帮忙讨回来的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B819():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_B819)

    def lambda_B827():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_B827)

    def lambda_B835():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_B835)

    def lambda_B843():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_B843)
    TurnDirection(0x1A, 0x101, 400)

    ChrTalk(
        0x1A,
        "#192F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#201F#6P喂喂……\x01",
            "不要说得这么轻巧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F虽然我不认为\x01",
            "他们是可以随便挑战的对手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F不过，如果没有干劲的话，\x01",
            "本来能赢也会赢不了的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#2P呵呵，说些没来由的话\x01",
            "还真是艾丝蒂尔君的性格啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, 84120, 0, -64660, 270)
    SetChrPos(0x10, 84380, 0, -65750, 270)
    SetChrPos(0x11, 85120, 0, -64170, 270)
    SetChrPos(0x12, 85370, 0, -65269, 270)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    NpcTalk(
        0xF,
        "警卫兵",
        (
            "#1P哼……\x01",
            "终于结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA47():

        label("loc_BA47")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_BA47")

    QueueWorkItem2(0x1A, 2, lambda_BA47)

    def lambda_BA58():

        label("loc_BA58")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_BA58")

    QueueWorkItem2(0x1B, 2, lambda_BA58)

    def lambda_BA69():

        label("loc_BA69")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BA69")

    QueueWorkItem2(0x1C, 2, lambda_BA69)

    def lambda_BA7A():

        label("loc_BA7A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_BA7A")

    QueueWorkItem2(0x19, 2, lambda_BA7A)

    def lambda_BA8B():

        label("loc_BA8B")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BA8B")

    QueueWorkItem2(0x101, 2, lambda_BA8B)

    def lambda_BA9C():

        label("loc_BA9C")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BA9C")

    QueueWorkItem2(0x102, 2, lambda_BA9C)

    def lambda_BAAD():

        label("loc_BAAD")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BAAD")

    QueueWorkItem2(0x108, 2, lambda_BAAD)

    def lambda_BABE():

        label("loc_BABE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BABE")

    QueueWorkItem2(0x104, 2, lambda_BABE)
    OP_6D(79330, 0, -63550, 1000)

    def lambda_BAE0():

        label("loc_BAE0")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_BAE0")

    QueueWorkItem2(0xF, 1, lambda_BAE0)

    def lambda_BAF1():

        label("loc_BAF1")

        TurnDirection(0xFE, 0x1A, 0)
        OP_48()
        Jump("loc_BAF1")

    QueueWorkItem2(0x10, 1, lambda_BAF1)

    def lambda_BB02():

        label("loc_BB02")

        TurnDirection(0xFE, 0x1A, 0)
        OP_48()
        Jump("loc_BB02")

    QueueWorkItem2(0x11, 1, lambda_BB02)

    def lambda_BB13():

        label("loc_BB13")

        TurnDirection(0xFE, 0x1A, 0)
        OP_48()
        Jump("loc_BB13")

    QueueWorkItem2(0x12, 1, lambda_BB13)

    def lambda_BB24():
        OP_8E(0xFE, 0x12A48, 0x0, 0xFFFF0AA6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BB24)
    Sleep(300)

    def lambda_BB44():
        OP_8E(0xFE, 0x12BD8, 0x0, 0xFFFEFC14, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BB44)

    def lambda_BB5F():
        OP_6D(75030, 0, -62490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BB5F)
    Sleep(300)

    def lambda_BB7C():
        OP_8E(0xFE, 0x12F7A, 0x0, 0xFFFF06F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_BB7C)
    Sleep(100)

    def lambda_BB9C():
        OP_8E(0xFE, 0x13146, 0x0, 0xFFFEFF0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_BB9C)
    WaitChrThread(0xF, 0x2)

    def lambda_BBBC():
        OP_8E(0xFE, 0x1241C, 0x0, 0xFFFF081C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BBBC)
    WaitChrThread(0x10, 0x2)

    def lambda_BBDC():
        OP_8E(0xFE, 0x124D0, 0x0, 0xFFFF011E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BBDC)

    NpcTalk(
        0x11,
        "警卫兵",
        (
            "好了，别磨磨蹭蹭的！\x01",
            "赶快回港口去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#192F#5P喂喂，别开玩笑了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#202F刚刚比赛完，\x01",
            "让我们稍微休息一会儿嘛～\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        (
            "#5P哼……\x01",
            "罪犯还要求这么多。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "警卫兵",
        "喂，赶快走！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#197F#5P哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#203F啊啊，好累啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#215F#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x19, 0xFF)

    def lambda_BD88():
        OP_90(0xFE, 0x1B58, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BD88)

    def lambda_BDA3():
        OP_90(0xFE, 0x1B58, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BDA3)

    def lambda_BDBE():
        OP_6D(78790, 0, -61860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BDBE)
    Sleep(300)

    def lambda_BDDB():
        OP_90(0xFE, 0x1B58, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_BDDB)

    def lambda_BDF6():
        OP_90(0xFE, 0x18EC, 0x0, 0x6E0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BDF6)
    Sleep(200)

    def lambda_BE16():
        OP_90(0xFE, 0x1770, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BE16)

    def lambda_BE31():
        OP_90(0xFE, 0x1770, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_BE31)
    Sleep(200)

    def lambda_BE51():
        OP_90(0xFE, 0x1770, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BE51)

    def lambda_BE6C():
        OP_90(0xFE, 0x1770, 0x0, 0x6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BE6C)
    WaitChrThread(0x1C, 0x1)
    Sleep(600)

    ChrTalk(
        0x1C,
        "#212F#1P喂，你们……\x02",
    )


    def lambda_BEB2():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BEB2)

    def lambda_BEC0():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BEC0)

    def lambda_BECE():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_BECE)

    def lambda_BEDC():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BEDC)

    def lambda_BEEA():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_BEEA)

    def lambda_BEF8():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BEF8)

    def lambda_BF06():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BF06)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x102, 400)

    ChrTalk(
        0x1C,
        (
            "#215F#2P虽然我们明天不能来这里看比赛了……\x01",
            "　\x02\x03",
            "#214F但是你们，一定要赢哦！\x02\x03",
            "如果输给那些家伙，\x01",
            "我可饶不了你们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3P啊……\x02\x03",
            "#001F当然啦！就交给我们吧！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F绝对……会赢给你们看的。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "警卫兵",
        "#5P……说完了吗。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "警卫兵",
        "#5P走吧，不要浪费时间了。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)

    def lambda_C09C():
        OP_90(0xFE, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C09C)

    def lambda_C0B7():
        OP_90(0xFE, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C0B7)
    Sleep(300)

    def lambda_C0D7():
        OP_90(0xFE, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_C0D7)

    def lambda_C0F2():
        OP_90(0xFE, 0x18EC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C0F2)
    Sleep(300)

    def lambda_C112():
        OP_90(0xFE, 0x18EC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_C112)

    def lambda_C12D():
        OP_90(0xFE, 0x18EC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_C12D)
    Sleep(300)

    def lambda_C14D():
        OP_90(0xFE, 0x18EC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C14D)

    def lambda_C168():
        OP_90(0xFE, 0x18EC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C168)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到奖金\x07\x04",
            "４００００\x07\x00",
            "米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    AddMira(40000)
    ClearMapFlags(0x100000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_B175 end

    def Function_39_C1E1(): pass

    label("Function_39_C1E1")

    EventBegin(0x0)
    OP_6D(79580, 0, -62340, 0)
    OP_67(0, 6570, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(314000, 0)
    OP_6E(371, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrPos(0x101, 81740, 0, -63700, 270)
    SetChrPos(0x102, 82090, 0, -62760, 270)
    SetChrPos(0x104, 80420, 0, -63500, 270)
    SetChrPos(0x108, 80850, 0, -62320, 270)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#008F哈～现在这里只有我们，\x01",
            "显得真是宽敞啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这里是为团体竞技、马戏表演等活动\x01",
            "而建造的建筑设施啊。\x02\x03",
            "以前，好像还曾经举行过\x01",
            "人和大型魔兽战斗的表演呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哎～是这样啊，\x01",
            "所以才有这么大的休息室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5P虽然和帝都的歌剧院比起来，\x01",
            "这里的设施还略显不足……\x02\x03",
            "不过这里也有这里的特色，\x01",
            "举办一场室外音乐会也不是不可以的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#509F这是什么话啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x108, 135, 400)

    ChrTalk(
        0x108,
        (
            "#070F#2P话说回来，\x01",
            "今天我们好像来得太早了。\x02\x03",
            "仔细想想，只剩一场比赛了，\x01",
            "开始时间应该会晚一些。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5DD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C5DD)

    def lambda_C5EB():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5EB)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#004F哎，是这样吗？\x02\x03",
            "#007F嗯……就这样只是等着比赛开始，\x01",
            "我还是会有点紧张呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么在比赛开始之前，\x01",
            "我们就在场内散散步吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F嗯，好啊。\x02",
    )

    CloseMessageWindow()

    def lambda_C6DE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C6DE)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#006F金先生，奥利维尔。\x01",
            "那我们就去散步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#2P好，到时间就赶快回来哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C76A():

        label("loc_C76A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_C76A")

    QueueWorkItem2(0x104, 1, lambda_C76A)

    def lambda_C77B():

        label("loc_C77B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_C77B")

    QueueWorkItem2(0x108, 1, lambda_C77B)

    def lambda_C78C():
        OP_6D(81340, 0, -62730, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C78C)

    def lambda_C7A4():
        OP_6E(314, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_C7A4)
    OP_8C(0x101, 90, 400)

    def lambda_C7BB():
        OP_8E(0xFE, 0x14D84, 0x0, 0xFFFF07F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7BB)
    Sleep(400)
    OP_8C(0x102, 90, 400)

    def lambda_C7E2():
        OP_8E(0xFE, 0x14DFC, 0x0, 0xFFFF0CA4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C7E2)
    WaitChrThread(0x101, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(50)

    def lambda_C80C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C80C)

    def lambda_C81E():
        OP_8E(0xFE, 0x15572, 0x0, 0xFFFF07F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C81E)
    WaitChrThread(0x102, 0x1)

    def lambda_C83E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C83E)

    def lambda_C850():
        OP_8E(0xFE, 0x155D6, 0x0, 0xFFFF0CA4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C850)
    WaitChrThread(0x102, 0x2)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x104,
        "#030F……………………………\x02",
    )

    CloseMessageWindow()

    def lambda_C888():
        OP_6D(80340, 0, -62730, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C888)
    Sleep(400)
    OP_44(0x108, 0xFF)
    TurnDirection(0x108, 0x104, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x108,
        (
            "#073F#2P哎。今天这是吹的什么风啊？\x01",
            "　\x02\x03",
            "我还以为你肯定会粘着他们一起去的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x104, 0xFF)
    TurnDirection(0x104, 0x108, 400)

    ChrTalk(
        0x104,
        (
            "#035F#6P没什么，我只是觉得\x01",
            "他们两个之间的气氛稍微有点改变。\x02\x03",
            "好像有所进展呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F#2P哈哈，你很了解嘛。\x02\x03",
            "#070F确实，他们两个看起来在大会上\x01",
            "承受着奇怪的压力……\x01",
            "　\x02\x03",
            "不过今天从他们的表情看来，\x01",
            "这种压力好像烟消云散了。\x02\x03",
            "#071F哎呀，真是羡慕年轻人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#6P不过，他们两个嘛……\x01",
            "需要加深感情的地方还有很多呢。\x02\x03",
            "如果能有进一步发展的话，\x01",
            "相信他们会享受到爱情甜蜜的喜悦。\x02\x03",
            "#037F呵呵……\x01",
            "看来我善意的讥讽还是挺有效的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#075F#2P哎呀哎呀，真是恶趣味……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(84790, 0, 33020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 85160, 0, 32390, 90)
    SetChrPos(0x102, 85170, 0, 33380, 90)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x25, 80420, 0, -63670, 0)
    SetChrPos(0x26, 80420, 0, -62320, 180)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#009F……（哆嗦）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F怎么了？\x02\x03",
            "是不是身体不舒服？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#509F没什么……\x01",
            "只是感觉到有股邪恶的意念……\x02\x03",
            "老是把别人的隐私当作自己的乐趣，\x01",
            "一想起他那副玩世不恭的模样我就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F……呵呵，\x01",
            "我大概能想象得出是谁在作怪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_39_C1E1 end

    def Function_40_CD3D(): pass

    label("Function_40_CD3D")

    EventBegin(0x0)
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD97")
    SetChrPos(0x101, 11050, 0, 5180, 270)
    SetChrPos(0x102, 11120, 0, 6310, 270)
    SetChrPos(0x1E, 1660, 0, 3830, 90)
    OP_6D(10420, 0, 6050, 0)
    Jump("loc_CDDB")

    label("loc_CD97")

    SetChrPos(0x101, -11040, 0, 5190, 90)
    SetChrPos(0x102, -10950, 0, 6290, 90)
    SetChrPos(0x1E, -2060, 0, 5520, 270)
    OP_6D(-10910, 0, 5550, 0)

    label("loc_CDDB")

    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D822")

    NpcTalk(
        0x1E,
        "老人的声音",
        "#4P哦哦……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "老人的声音",
        (
            "#4P你们……\x01",
            "这不是艾丝蒂尔和约修亚嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6D(6960, 0, 4810, 2000)

    ChrTalk(
        0x101,
        "#004F啊啊，是克劳斯市长！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F为什么您会在这里……\x02",
    )

    CloseMessageWindow()

    def lambda_CEC9():

        label("loc_CEC9")

        TurnDirection(0xFE, 0x1E, 0)
        OP_48()
        Jump("loc_CEC9")

    QueueWorkItem2(0x101, 1, lambda_CEC9)

    def lambda_CEDA():

        label("loc_CEDA")

        TurnDirection(0xFE, 0x1E, 0)
        OP_48()
        Jump("loc_CEDA")

    QueueWorkItem2(0x102, 1, lambda_CEDA)

    def lambda_CEEB():
        OP_8E(0xFE, 0x1798, 0x0, 0x128E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_CEEB)
    Sleep(300)

    def lambda_CF0B():
        OP_8E(0xFE, 0x1D92, 0x0, 0x1176, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CF0B)
    Sleep(300)

    def lambda_CF2B():
        OP_8E(0xFE, 0x1BF8, 0x0, 0x15FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF2B)
    WaitChrThread(0x1E, 0x2)
    OP_8C(0x1E, 90, 400)

    ChrTalk(
        0x1E,
        (
            "#601F哎呀，真是好久不见了。\x02\x03",
            "我听雪拉扎德说了，\x01",
            "你们为了成为正游击士\x01",
            "在王国各地旅行的事情……\x02\x03",
            "这么长时间不见，\x01",
            "你们都成熟了不少嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～～\x01",
            "我自己倒没有什么感觉……\x02\x03",
            "#501F市长爷爷还是这么有精神呢。\x01",
            "　\x02\x03",
            "这样我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#601F哈哈，\x01",
            "我可是还不会输给年轻人的哦。\x02\x03",
            "对了，\x01",
            "你们不是闯进决赛了嘛。\x02\x03",
            "所以我不顾这一把老骨头\x01",
            "就赶来观看比赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎，您是为了看比赛\x01",
            "从洛连特过来的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600F不，不是的。\x02\x03",
            "其实，是突然收到了\x01",
            "格兰赛尔城的晚宴的邀请信。\x02\x03",
            "所以今天早上才乘定期船\x01",
            "刚刚到达王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F王城的晚宴！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F原来如此……\x01",
            "是这样啊。\x02\x03",
            "#010F那个晚宴，\x01",
            "是不是杜南公爵举办的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#604F原来你知道啊？\x02\x03",
            "#600F本来我们夫妇是要在\x01",
            "诞辰庆典的仪式上出席的，\x01",
            "所以最近肯定会来王都……\x02\x03",
            "不过突然有一位军队的女性军官\x01",
            "来邀请我们参加晚餐会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（那个女性军官……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（一定就是凯诺娜上尉了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#603F不过，\x01",
            "米蕾奴还没有做好旅行的准备。\x02\x03",
            "所以没办法，\x01",
            "我就一个人先来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是吗……\x01",
            "米蕾奴婶婶没有来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，市长爷爷。\x02\x03",
            "其实，\x01",
            "我们说不定也会出席晚宴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#604F哦……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚向克劳斯市长说明了\x01",
            "因公爵的提案，武术大会优胜者会被招待参加晚宴的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x1E,
        (
            "#604F原来如此……\x01",
            "还有这样的事啊。\x02\x03",
            "#600F本来在陛下身体欠佳的时候，\x01",
            "不太想出席晚晚宴什么的……\x02\x03",
            "和你们一起的话，\x01",
            "也就可以转换一下心情了。\x02\x03",
            "#601F这下子，\x01",
            "你们就更必须得赢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈……\x01",
            "嗯，我知道了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定会努力，不辜负您的期待的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600F那么，\x01",
            "我就到观众席去了。\x02\x03",
            "加油啊。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x1E, 0x1F67, 0x0, 0x9F6, 0xBB8, 0x0)
    OP_8E(0x1E, 0x2D6E, 0x0, 0x16A8, 0xBB8, 0x0)

    def lambda_D7FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D7FA)
    OP_8E(0x1E, 0x357A, 0x0, 0x16A8, 0xBB8, 0x0)
    OP_22(0x7, 0x0, 0x64)
    Jump("loc_E266")

    label("loc_D822")


    NpcTalk(
        0x1E,
        "老人的声音",
        "#1P哦哦……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "老人的声音",
        (
            "#1P你们……\x01",
            "这不是艾丝蒂尔和约修亚嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-6910, 0, 5920, 2000)

    ChrTalk(
        0x101,
        "#004F啊啊，是克劳斯市长！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F为什么您会在这里……\x02",
    )

    CloseMessageWindow()

    def lambda_D8FA():

        label("loc_D8FA")

        TurnDirection(0xFE, 0x1E, 0)
        OP_48()
        Jump("loc_D8FA")

    QueueWorkItem2(0x101, 1, lambda_D8FA)

    def lambda_D90B():

        label("loc_D90B")

        TurnDirection(0xFE, 0x1E, 0)
        OP_48()
        Jump("loc_D90B")

    QueueWorkItem2(0x102, 1, lambda_D90B)

    def lambda_D91C():
        OP_8E(0xFE, 0xFFFFE8F4, 0x0, 0x1680, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_D91C)
    Sleep(300)

    def lambda_D93C():
        OP_8E(0xFE, 0xFFFFE250, 0x0, 0x14C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D93C)
    Sleep(300)

    def lambda_D95C():
        OP_8E(0xFE, 0xFFFFE296, 0x0, 0x19B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D95C)
    WaitChrThread(0x1E, 0x2)

    ChrTalk(
        0x1E,
        (
            "#601F哎呀，真是好久不见了。\x02\x03",
            "我听雪拉扎德说了，\x01",
            "你们为了成为正游击士\x01",
            "在王国各地旅行的事情……\x02\x03",
            "这么长时间不见，\x01",
            "你们都成熟了不少嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～～\x01",
            "我自己倒没有什么感觉……\x02\x03",
            "#501F市长爷爷还是这么有精神呢。\x01",
            "　\x02\x03",
            "这样我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#601F哈哈，\x01",
            "我可是还不会输给年轻人的哦。\x02\x03",
            "对了，\x01",
            "你们不是闯进决赛了嘛。\x02\x03",
            "所以我不顾这一把老骨头\x01",
            "就赶来观看比赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎，您是为了看比赛\x01",
            "从洛连特过来的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600F不，不是的。\x02\x03",
            "其实，是突然收到了\x01",
            "格兰赛尔城的晚宴的邀请信。\x02\x03",
            "所以今天早上才乘定期船\x01",
            "刚刚到达王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F王城的晚宴！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F原来如此……\x01",
            "是这样啊。\x02\x03",
            "#010F那个晚宴，\x01",
            "是不是杜南公爵举办的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#604F原来你知道啊？\x02\x03",
            "#600F本来我们夫妇是要在\x01",
            "诞辰庆典的仪式上出席的，\x01",
            "所以最近肯定会来王都……\x02\x03",
            "不过突然有一位军队的女性军官\x01",
            "来邀请我们参加晚餐会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F（那个女性军官……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（一定就是凯诺娜上尉了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#603F不过，\x01",
            "米蕾奴还没有做好旅行的准备。\x02\x03",
            "所以没办法，\x01",
            "我就一个人先来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F是吗……\x01",
            "米蕾奴婶婶没有来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，市长爷爷。\x02\x03",
            "其实，\x01",
            "我们说不定也会出席晚宴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#604F哦……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚向克劳斯市长说明了\x01",
            "因公爵的提案，武术大会优胜者会被招待参加晚宴的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x1E,
        (
            "#604F原来如此……\x01",
            "还有这样的事啊。\x02\x03",
            "#600F本来在陛下身体欠佳的时候，\x01",
            "不太想出席晚晚宴什么的……\x02\x03",
            "和你们一起的话，\x01",
            "也就可以转换一下心情了。\x02\x03",
            "#601F这下子，\x01",
            "你们就更必须得赢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈……\x01",
            "嗯，我知道了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定会努力，不辜负您的期待的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600F那么，\x01",
            "我就到观众席去了。\x02\x03",
            "加油啊。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x1E, 0xFFFFE340, 0x0, 0x1018, 0xBB8, 0x0)
    OP_8E(0x1E, 0xFFFFD3BE, 0x0, 0x166C, 0xBB8, 0x0)
    OP_8C(0x1E, 270, 400)
    OP_70(0x1, 0x1E)
    OP_73(0x1)

    def lambda_E235():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_E235)
    OP_8E(0x1E, 0xFFFFCCCA, 0x0, 0x1784, 0xBB8, 0x0)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)

    label("loc_E266")

    Sleep(500)
    OP_71(0x1, 0x800)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F没想到克劳斯市长\x01",
            "也要出席晚宴啊……\x02\x03",
            "那么，梅贝尔市长她们\x01",
            "是不是也被邀请了呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F很有可能。\x02\x03",
            "把这些有权力的官员们集中在一起，\x01",
            "是不是有什么重要的事情宣布啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……算了。\x02\x03",
            "#006F不管怎么说先把比赛赢下来，\x01",
            "只要能参加晚宴，一切不就知道了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，也是。\x02\x03",
            "我们也该回休息室了吧。\x01",
            "快要到开场的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，知道了！\x02",
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_40_CD3D end

    def Function_41_E44D(): pass

    label("Function_41_E44D")

    OP_A2(0x3F2)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_41_E44D end

    def Function_42_E45A(): pass

    label("Function_42_E45A")

    EventBegin(0x0)
    OP_6D(75070, 0, -63440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, 75600, 0, -63280, 270)
    SetChrPos(0x102, 76550, 0, -62310, 270)
    SetChrPos(0x104, 76600, 0, -64489, 270)
    SetChrPos(0x108, 77680, 0, -63300, 270)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#580F啊……\x02\x03",
            "今天理查德上校也和公爵一起来了啊！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊……\x02\x03",
            "是作为公爵的随行人员，\x01",
            "顺道来看自己部下的比赛的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，那就是街头巷尾很有人气的\x01",
            "王国军情报部的首领啊。\x02\x03",
            "仪表堂堂，又有风度，\x01",
            "看起来是个相当厉害的人物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……\x01",
            "这样说也没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F唔～那个男人……\x01",
            "比在柏斯见到的时候更加风度翩翩了呢。\x01",
            "　\x02\x03",
            "#035F哼，真没有办法。\x02\x03",
            "只好承认他为\x01",
            "我奥利维尔·朗海姆的对手了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#509F#5P谁也没有要把你当成对手吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F……好像要开始了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("主持人的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "各位……\x01",
            "让你们久等了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我宣布，武术大会正式赛，\x01",
            "最后的决赛现在开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x3F3)
    NewScene("ED6_DT01/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_E45A end

    def Function_43_E855(): pass

    label("Function_43_E855")

    EventBegin(0x0)
    OP_6D(76480, 0, -63310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 75600, 0, -63280, 90)
    SetChrPos(0x102, 76550, 0, -62310, 180)
    SetChrPos(0x104, 76600, 0, -64489, 0)
    SetChrPos(0x108, 77680, 0, -63300, 270)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#508F好，我们上场吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F终于……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F哼～\x01",
            "这次我就认真一回吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F不管结果是哭还是笑，\x01",
            "这都是战斗的最后时刻了……\x02\x03",
            "#076F鼓足干劲上吧！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_1B(0xC, 0x0, 0xFFFF)
    OP_1B(0xB, 0x0, 0x30)
    Return()

    # Function_43_E855 end

    def Function_44_E9B1(): pass

    label("Function_44_E9B1")

    EventBegin(0x0)
    OP_24(0xAE, 0x50)
    OP_6D(-80090, 0, -63100, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1F, -82950, 0, -63110, 90)
    SetChrPos(0x20, -82500, 0, -64220, 90)
    SetChrPos(0x21, -82420, 0, -61920, 180)
    ClearMapFlags(0x100000)
    OP_6D(-82600, 0, -63080, 2000)

    ChrTalk(
        0x1F,
        (
            "#111F呵呵，那些有趣的家伙取得优胜了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x21, 400)

    ChrTalk(
        0x20,
        (
            "#183F真是的……\x01",
            "你也应该知道耻辱了吧，洛伦斯少尉。\x02\x03",
            "让那样初出茅庐的小孩子占了上风，\x01",
            "实在是给上校的脸上抹黑……\x02\x03",
            "平时那种狂妄自大的态度\x01",
            "难道都是装出来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#281F……抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110F哈哈，凯诺娜。\x01",
            "不要这么责怪洛伦斯嘛。\x02\x03",
            "其实是我拜托他不要使出全力的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#184F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#115F情报部因为本身的性质，\x01",
            "不能这么容易摆脱黑子的角色。\x02\x03",
            "就这样让众星云集的小组获得优胜\x01",
            "应该是众望所归的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#180F原来如此……\x02\x03",
            "#181F看起来公爵大人对那个东方人\x01",
            "比我们想象中的更感兴趣呢……\x02\x03",
            "说不定想拿回王城当作玩具熊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110F不过……\x01",
            "今年的大会有点遗憾啊。\x02\x03",
            "王室亲卫队队长的舒华兹中尉\x01",
            "还有摩尔根将军如果能来参加的话，\x01",
            "就会更加精彩纷呈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#182F呵呵，请不要开玩笑……\x02\x03",
            "如果这样的话，\x01",
            "上校您亲自参加不是更好吗。\x02\x03",
            "那个狂妄的尤莉亚什么的\x01",
            "根本连您的一个脚趾头都比不上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#111F哈哈，我可不打算\x01",
            "变成这样一个自信家啊。\x02\x03",
            "如果洛伦斯使出全力的话，\x01",
            "我也不一定能胜过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#281F……请不要开玩笑了。\x02\x03",
            "上校您实在是太抬举我了。\x01",
            "　\x02\x03",
            "我有幸徒得军人的名号，\x01",
            "实际上不过是个所谓猎兵的草莽匹夫罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110F就算你说得这么谦虚，\x01",
            "我理查德也是绝对不会看错人的。\x02\x03",
            "真正能做你的对手也只有那个男人吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#281F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#183F是指『他』吗……\x02\x03",
            "这样下去的话，\x01",
            "他的孩子就要进入格兰赛尔城了。\x02\x03",
            "要不要采取什么措施？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110F不用管了。\x01",
            "这是杜南公爵定下的事情。\x02\x03",
            "#115F现在就算游击士协会出面干涉，\x01",
            "也不可能阻止我们计划的进行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#184F可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#112F……洛伦斯。\x01",
            "计划进展得如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#280F现在已经超过９０％了。\x02\x03",
            "再过一两天应该就可以\x01",
            "带上校到最后的地方去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#110F好，太好了。\x02",
    )

    CloseMessageWindow()

    def lambda_F29D():
        OP_6D(-80600, 0, -63080, 1500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_F29D)

    def lambda_F2B5():
        OP_8E(0xFE, 0xFFFEC4C4, 0x0, 0xFFFF097A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_F2B5)
    Sleep(400)

    def lambda_F2D5():

        label("loc_F2D5")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_F2D5")

    QueueWorkItem2(0x21, 1, lambda_F2D5)

    def lambda_F2E6():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_F2E6)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x1F, 0x2)
    Sleep(400)

    ChrTalk(
        0x1F,
        (
            "#115F……王国的黎明就要来到了。\x02\x03",
            "#111F就算背负上逆贼的罪名，\x01",
            "也一定要用我这双手开拓未来。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_24(0xAE, 0x5A)
    Sleep(100)
    OP_24(0xAE, 0x50)
    Sleep(100)
    OP_24(0xAE, 0x46)
    Sleep(100)
    OP_24(0xAE, 0x3C)
    Sleep(100)
    OP_24(0xAE, 0x28)
    Sleep(100)
    OP_23(0xAE)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FE)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_44_E9B1 end

    def Function_45_F3EF(): pass

    label("Function_45_F3EF")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F468")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔，这里是出口啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎呀……\x01",
            "现在这个时候不能走呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F48D")

    label("loc_F468")


    ChrTalk(
        0x101,
        (
            "#002F好像一旦出去\x01",
            "就不能再进来了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F48D")

    Jump("loc_F574")

    label("loc_F490")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4D5")

    ChrTalk(
        0x102,
        (
            "#010F这里是出口吧。\x02\x03",
            "现在还不能出去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F574")

    label("loc_F4D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F515")
    OP_A2(0x0)

    ChrTalk(
        0x108,
        "#074F哦，这边是出口。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F53E")

    label("loc_F515")


    ChrTalk(
        0x108,
        (
            "#070F唔，\x01",
            "现在还不能回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F53E")

    Jump("loc_F574")

    label("loc_F541")


    ChrTalk(
        0x104,
        "#030F唔，这边是出口呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F574")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_45_F3EF end

    def Function_46_F590(): pass

    label("Function_46_F590")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贵宾席，无关人等禁止入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_F590 end

    def Function_47_F605(): pass

    label("Function_47_F605")

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
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_F605 end

    def Function_48_F654(): pass

    label("Function_48_F654")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F68C")

    ChrTalk(
        0x101,
        "#501F啊，往这边去是走廊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F68C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F717")
    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F喂，那里是走廊啊。\x02\x03",
            "去比赛场地，\x01",
            "要走对面那个出口才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F717")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78E")
    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F喂，那里是走廊啊。\x02\x03",
            "去比赛场地，\x01",
            "要走对面那个出口才对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F78E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C5")

    ChrTalk(
        0x108,
        "#070F哦，这边是走廊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F7C5")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070F喂，那里是走廊啊。\x02\x03",
            "去比赛场地，\x01",
            "要走对面那个出口才对。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x108, 400)

    ChrTalk(
        0x104,
        (
            "#035F呼，我当然知道。\x01",
            "开个玩笑而已嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F87A")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_48_F654 end

    def Function_49_F896(): pass

    label("Function_49_F896")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8FB")

    ChrTalk(
        0x101,
        (
            "#002F这里就是比赛场的入口了……\x02\x03",
            "#003F唔～冷静不下来啊。\x01",
            "还没轮到我们出场吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA03")

    label("loc_F8FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F988")

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "就算进了比赛场也没用。\x02\x03",
            "还有一些时间，\x01",
            "我们就在竞技场内散散步吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA03")

    label("loc_F988")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA03")

    ChrTalk(
        0x102,
        (
            "#010F这边是场内……\x02\x03",
            "到比赛开始还有些时间，\x01",
            "在这附近散散步吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA03")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_49_F896 end

    def Function_50_FA1F(): pass

    label("Function_50_FA1F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_END)), "loc_FB68")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAB3")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，我们走错地方了吧。\x02\x03",
            "我们的休息室\x01",
            "是在另外一边的房间才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F啊，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB65")

    label("loc_FAB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB10")

    ChrTalk(
        0x102,
        (
            "#010F这里是『红之组』的房间……\x02\x03",
            "我们的休息室应该是\x01",
            "另外一边的『苍之组』的房间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB65")

    label("loc_FB10")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F这里是『红之组』的休息室。\x02\x03",
            "我们的休息室应该是\x01",
            "另外一边的『苍之组』的房间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB65")

    Jump("loc_FBEF")

    label("loc_FB68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_FBEF")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这里应该就是选手休息室了。\x02\x03",
            "不能打扰选手，\x01",
            "我们还是别进去了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBEF")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_50_FA1F end

    SaveToFile()

Try(main)
