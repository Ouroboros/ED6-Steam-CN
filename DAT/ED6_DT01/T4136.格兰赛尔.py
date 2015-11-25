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
        'Carna',                                # 9
        'Anelace',                              # 10
        'Grant',                                # 11
        'Kurt',                                 # 12
        'Deen',                                 # 13
        'Rais',                                 # 14
        'Rocco',                                # 15
        'Private Issac',                        # 16
        'Private Zain',                         # 17
        'Specialist Taris',                     # 18
        'Private Bian',                         # 19
        'Private Micria',                       # 20
        'Specialist Gorg',                      # 21
        'Soldier',                              # 22
        '1st Lieutenant Riel',                  # 23
        '1st Lieutenant Bern',                  # 24
        'Commander Dale',                       # 25
        'Lyall',                                # 26
        'Don',                                  # 27
        'Kyle',                                 # 28
        'Josette',                              # 29
        'Dorothy',                              # 30
        'Mayor Klaus',                          # 31
        'Colonel Richard',                      # 32
        'Captain Amalthea',                     # 33
        '2nd Lieutenant Lorence',               # 34
        'Sunia',                                # 35
        'Clark',                                # 36
        'Joshua',                               # 37
        'Olivier',                              # 38
        'Zane',                                 # 39
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
            "#010FMaybe talking to the other teams\x01",
            "will help calm some nerves.\x02\x03",
            "After all, we're not fighting\x01",
            "anyone in this room today, so\x01",
            "we can all get along just fine!\x02",
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
            "#030FBack already?\x02\x03",
            "There's still time before the\x01",
            "match begins, you know.\x02\x03",
            "Go. Make the most of the next \x01",
            "few hours. Explore. Discover.\x01",
            "Experience...together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F...I need to go wash up now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_C16")


    ChrTalk(
        0xFE,
        (
            "#035FI'm in the moments just after the\x01",
            "curtain rises, but before the diva\x01",
            "sounds her first refrains!\x02\x03",
            "Quick! Hand me a glass, that\x01",
            "I may catch this feeling and \x01",
            "drink deep its bitter malt! \x02",
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
            "#070FSo...how do you propose we go after\x01",
            "those Special Ops guys? They're not\x01",
            "going to give us any openings...\x02\x03",
            "The only chance we have, I believe, is to\x01",
            "target their commanding officer. If we take\x01",
            "him down, openings are sure to follow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6F")

    label("loc_DE2")


    ChrTalk(
        0xFE,
        (
            "#070FNo matter how you look at it,\x01",
            "these are some strong teams.\x02\x03",
            "Heh. Glad I came to Liberl. This\x01",
            "place seems right up my alley.\x02",
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
            "#851FThat worked up a good sweat.\x02\x03",
            "I could sure go for an ice cream\x01",
            "right about now...\x02\x03",
            "#816FGood luck, newbies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F6F")

    ChrTalk(
        0xFE,
        (
            "#816FLooks like you got onto Zane's\x01",
            "team. Not too shabby!\x02\x03",
            "I'm looking forward to seeing\x01",
            "what you've got.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_F6F")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "#850FHeya, newbies!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FHi, Anelace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#816FLooks like you got onto Zane's\x01",
            "team. Not too shabby!\x02\x03",
            "I'm looking forward to seeing\x01",
            "what you've got.\x02",
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
            "#830FLooks like you're up next.\x02\x03",
            "Go get 'em!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1213")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10E1")

    ChrTalk(
        0xFE,
        (
            "#835FSince we're in the same room, that\x01",
            "means we won't be pitted against\x01",
            "each other in today's matches.\x02\x03",
            "...Too bad, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1213")

    label("loc_10E1")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#831FHey, Estelle.\x02\x03",
            "Since we're in the same room, that\x01",
            "means we won't be pitted against\x01",
            "each other in today's matches.\x02\x03",
            "#835F...Too bad, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001FYeah, it is. But, that just means\x01",
            "the fun gets to last longer for\x01",
            "you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#830FHeh. If nothing else, you sure\x01",
            "do know how to trash talk!\x02",
        )
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
            "#820FWe'll be cheering for you.\x02\x03",
            "Go knock 'em dead. Or down, at\x01",
            "the very least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_127D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12C6")

    ChrTalk(
        0xFE,
        (
            "#820FShow us what you can do.\x02\x03",
            "And may the best team win.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_12C6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "#821FLooks like you're in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FYep, sure are! Thanks to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#820FShow us what you can do.\x02\x03",
            "And may the best team win.\x02",
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
            "#840FJust stay cool, and you'll do\x01",
            "fine.\x02\x03",
            "I'm actually quite anxious to\x01",
            "see you guys in action. Should\x01",
            "be pretty grand!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1699")

    label("loc_13E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14AF")

    ChrTalk(
        0xFE,
        (
            "#840FIf you get nervous, you'll start\x01",
            "taking short, shallow breaths.\x01",
            "And that's bad news!\x02\x03",
            "Force yourself to breathe slow and deep,\x01",
            "and you'll find yourself feeling like a\x01",
            "whole new person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1699")

    label("loc_14AF")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "#840FHey, champs. How are you feeling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FA little nervous and...kinda\x01",
            "panicky, to be honest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#840FIf you get nervous, you'll start\x01",
            "taking short, shallow breaths.\x01",
            "And that's bad news!\x02\x03",
            "Force yourself to breathe slow and deep,\x01",
            "and you'll find yourself feeling like a\x01",
            "whole new person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FGot it. Shallow breaths. I-I mean,\x01",
            "deep breaths. Deep breaths!\x02\x03",
            "#500F*inhale*\x02\x03",
            "*exhale*\x02\x03",
            "#006FWow, that...actually helped,\x01",
            "I think!\x02\x03",
            "Thanks, Kurt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#841FHa ha, no problem.\x02",
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
            "There are a lot of people watching\x01",
            "you out there. No pressure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Just do what you're gonna do,\x01",
            "and do it well. And good things\x01",
            "will come of it.\x02",
        )
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
            "If you win today, you'll be in\x01",
            "tomorrow's championship match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Just do what you're gonna do,\x01",
            "and do it well. And good things\x01",
            "will come of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_181E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1863")

    ChrTalk(
        0x23,
        (
            "Please wait in your room for\x01",
            "your names to be called.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18A8")

    ChrTalk(
        0x23,
        (
            "Please wait in your room for\x01",
            "your names to be called.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_18A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_18E6")

    ChrTalk(
        0x23,
        "Today's matches are finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "Come again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_19B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(
        0x23,
        "Today's matches are finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "Come again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_192B")


    ChrTalk(
        0x23,
        (
            "If you want to watch the preliminaries,\x01",
            "you'd best hurry up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "I believe you MIGHT just be in\x01",
            "time to catch the seventh match.\x02",
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
        "Zane's team...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "...You're in the 'Blue Team Room,'\x01",
            "on the right side of the hall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE3")

    label("loc_1A52")

    OP_A2(0x1)

    ChrTalk(
        0x22,
        (
            "The time has finally come.\x01",
            "Break a leg, guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Zane's team...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "...You're in the 'Blue Team Room,'\x01",
            "on the right side of the hall.\x02",
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
        "Zane's team...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Please wait in the 'Blue Team Room,'\x01",
            "on the right side of the hall.\x02",
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
        "Zane's team, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "...Today you'll be in the room\x01",
            "on the right side of the hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The time has finally come.\x01",
            "Break a leg, guys!\x02",
        )
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
            "The bracer team should still\x01",
            "be on the grounds, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Try the north waiting room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEE")

    label("loc_1C78")


    ChrTalk(
        0x22,
        "Welcome to the Grand Arena.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Spectators may use the stairwell\x01",
            "through either door to reach\x01",
            "audience seating.\x02",
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
            "#190FWhat did they do to me...?\x02\x03",
            "...Doesn't matter. I won't\x01",
            "be able to calm down till I\x01",
            "kick their skinny butts!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E68")

    label("loc_1D75")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "#197FI can't...quite...remember what\x01",
            "happened in Bose...\x02\x03",
            "Every time I try, my head feels\x01",
            "like it's going to split open.\x02\x03",
            "What did they do to me...?\x02\x03",
            "#190F...Doesn't matter. I won't\x01",
            "be able to calm down till I\x01",
            "kick their skinny butts!\x02",
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
            "#200FI have no intention of playing\x01",
            "dirty pool, don't worry.\x02\x03",
            "It was almost certainly the\x01",
            "Intelligence Division who set\x01",
            "us against one another.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2012")

    label("loc_1F0E")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        (
            "#200FI have no intention of playing\x01",
            "dirty pool, don't worry.\x02\x03",
            "It was almost certainly the\x01",
            "Intelligence Division who set\x01",
            "us against one another.\x02\x03",
            "And while I'm not suggesting we become\x01",
            "good buddies or anything, I also don't\x01",
            "think we need to be enemies.\x02",
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
            "#216FHey...\x02\x03",
            "#215FWhat say instead of just loafing\x01",
            "around here like idiots, you go\x01",
            "out there and do some fighting?\x02\x03",
            "Go on. Shoo! I mean, fight!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225E")

    label("loc_20BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_214B")

    ChrTalk(
        0xFE,
        (
            "#214FWhat? What do you want?\x02\x03",
            "What say instead of just loafing\x01",
            "around here like idiots, you go\x01",
            "out there and do some fighting?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225E")

    label("loc_214B")

    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "#213FWhat? What do you want?\x02\x03",
            "#214FWhat say instead of just loafing\x01",
            "around here like idiots, you go\x01",
            "out there and do some fighting?\x02\x03",
            "It's not just the Intelligence Division I plan\x01",
            "to give what's what to...it's you guys, too!\x01",
            "So you'd better be prepared for my wrath!\x02",
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
            "I'm gonna go win one for all\x01",
            "my compatriots locked up in\x01",
            "the dungeon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2338")

    label("loc_22BA")

    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "I owe those guys in black a good pop on\x01",
            "the nose, but right now, I'm fighting for\x01",
            "everybody locked up in the dungeon!\x02",
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
            "#004FOh, WOW...\x01",
            "This room is gorgeous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThis is the entrance hall.\x02\x03",
            "Audience seats are on the second\x01",
            "floor, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FLet's take a look.\x02",
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
            "#001F#3PCarna! Hi, everyone! Congrats\x01",
            "on making it through the\x01",
            "preliminaries!\x02",
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
        "#850F#4PHey, it's the new kids!\x02",
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
        "#831FOh, hey, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#821F#2PYo. You here to watch\x01",
            "the fights?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3PYes, and we had a chance\x01",
            "to see yours.\x02\x03",
            "That was a great match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841FThanks.\x01",
            "I'm glad to hear you say that.\x02\x03",
            "I don't get the sudden change\x01",
            "to make it a team competition,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#819F#4PYeah, me neither. It's weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#835FBut it's been okay so far. All of\x01",
            "our members are in one piece.\x02\x03",
            "Master Zane must be worried, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FOh, you know Zane, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#830FI don't know if I'd say that,\x01",
            "but I know the name.\x02\x03",
            "He's a famous bracer in the\x01",
            "Republic. People call him,\x01",
            "'Zane the Immovable.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#840FHe apparently came to Liberl\x01",
            "specifically to be in this\x01",
            "tournament.\x02\x03",
            "Then the promoters threw a wrench\x01",
            "in the works and changed it from\x01",
            "single to team competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#825F#2PAnd I'm betting that His\x01",
            "Excellency's the one behind\x01",
            "that idea.\x02\x03",
            "#2PEither way, Master Zane still\x01",
            "had no choice but to register\x01",
            "as a one man team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FAhh, okay...\x02\x03",
            "#009FUgh. The duke is a pain in the\x01",
            "ass no matter where he goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841FHa ha. No argument there.\x02\x03",
            "#844FStill, this is going to make it\x01",
            "hard for him to really show\x01",
            "what he can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#823F#2PNo kidding. It's too bad no\x01",
            "one's around to fight beside\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#821F#2P...Saaaay!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#831FWell...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xB)

    ChrTalk(
        0xB,
        "#841F...Hmm.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#850F#4PMaybe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F???\x02\x03",
            "Uh, what just happened? You all\x01",
            "got this creepy, serious look...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#840FNo, we were just thinking...\x02\x03",
            "What would you say to teaming\x01",
            "up with Zane in the later, no-\x01",
            "holds-barred fights?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FWell, I...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#004F#3SWait, WHAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#3PHmm... Teaming up with him...\x01",
            "Is that even allowed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#835FIt's not HIS fault that the rules\x01",
            "of the competition were changed\x01",
            "at the last minute.\x02\x03",
            "If one of the core rules can be\x01",
            "changed, then I think we've got\x01",
            "some wiggle room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820F#2PThere really are no other bracers\x01",
            "available that we could ask.\x02\x03",
            "#2PScherazard's busy, and we haven't\x01",
            "been able to contact Agate.\x02\x03",
            "#2PSimilar story for everyone\x01",
            "else, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#856F#4PI don't think Cassius is even\x01",
            "in the country.\x02\x03",
            "#819F#4PHeh... If those two joined up,\x01",
            "they'd probably be accused of\x01",
            "cheating, on general principle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#841FHa ha. Our chances of beating\x01",
            "THAT team would be something\x01",
            "like 10000:1.\x02\x03",
            "#840FAnyway, we should focus on what's\x01",
            "ahead, rather than what-ifs.\x02\x03",
            "Find Zane before the day's out, and if he\x01",
            "agrees to let you join him, you should still\x01",
            "have plenty of time to register.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FO-Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#830FOops...\x01",
            "Listen to us go on.\x02\x03",
            "I hope you'll give this some\x01",
            "serious thought, but for\x01",
            "now, we have to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#850F#4PBye-bye, newbies!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#821F#2PHeh heh... Here's hoping we\x01",
            "see you in the ring.\x02",
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
            "#010F#6PWhat do you think, Estelle?\x02\x03",
            "That sure went from talking shop\x01",
            "to something else entirely...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008F#4PHmm-hmm-hmm...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x190, 0xFA0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#502F#4PHeh heh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F#6PUhh...\x01",
            "Are you okay?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 23)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#582F#4PYeah, yeah...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    Sleep(400)
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        "#508F#4P#3SYYYYEEEEAAAHHHH!!\x02",
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
            "#006F#4PThat's IT! That's IT!! Now that's\x01",
            "what I'm TALKING about!!\x02\x03",
            "#502FOh, almighty Aidios! Thank you\x01",
            "so much for your bountiful favor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#6P...\x02\x03",
            "#013FYou're cracked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#4PThink about it! We can be in\x01",
            "THE Martial Arts Competition!\x02\x03",
            "#582FAnd we can help Zane in\x01",
            "the process!\x02\x03",
            "Not to mention, check out\x01",
            "that awesome castle...\x02\x03",
            "AND be a part of the big,\x01",
            "final, ultimate, super-duper\x01",
            "intense battle royale!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#508F#4P#3SWe can kill three birds with\x01",
            "one stone!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#6PYou, uh...you really want\x01",
            "to do this that badly?\x02\x03",
            "#010FWe haven't even entered yet, much\x01",
            "less made it into the final match.\x02\x03",
            "It WOULD be nice to be able to handle the\x01",
            "professor's request by ourselves, though.\x01",
            "Assuming we even made it through, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#4PYeah!侓 And think of how awesome\x01",
            "it would be to win!\x02\x03",
            "#005FPlus we can't just leave Zane twisting\x01",
            "in the wind! Let's go find him and ask\x01",
            "to join his team!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FWould you happen to have any idea\x01",
            "of where he actually IS...?\x02",
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
        (
            "#505F#1PDon't confuse the issue\x01",
            "with the facts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#2P*groan* Would you settle down\x01",
            "for two seconds, please?\x02\x03",
            "#010FLet's go back to the guild\x01",
            "and report in to Elnan.\x02\x03",
            "He's also the one who's most\x01",
            "likely to know where Zane is.\x02",
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
            "#010F...The blue team is on the\x01",
            "right, so this must be the\x01",
            "waiting room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070FYeah, has to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FWell, why don't we just relax\x01",
            "until it's time for the match?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FDo you ever do anything OTHER\x01",
            "than relaxing?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Young Man's Voice",
        (
            "#2PHeh... Look at you guys, all\x01",
            "calm and collected.\x02",
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
        "#004FIt's you...!\x02",
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
            "Hmph. We really gotta stop\x01",
            "meeting like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ha ha ha...\x01",
            "Too bad for you, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#4PHmmm...\x01",
            "Who are you guys, again?\x02",
        )
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
            "#1PWe're the Ravens! We had all of\x01",
            "Ruan pissing their collective\x01",
            "pants in fear of us!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Don't tell us you forgot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#4PGuys. I was KIDDING.\x02\x03",
            "#006FI knew you guys were in Grancel\x01",
            "yesterday to watch your buddies\x01",
            "fight in the preliminaries.\x02\x03",
            "And you're back again today to\x01",
            "pick a fight with us. Didn't you\x01",
            "learn your lesson the last time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1PHeh heh heh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ha ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hee hee hee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#4POkay, that's just creepy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014FAre you planning to participate\x01",
            "in the no-holds-barred matches?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1PHey, what's with the shocked look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We won the prelims and made it\x01",
            "here, fair and square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't remember you guys showing\x01",
            "your faces before we'd made it\x01",
            "halfway through, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#4PWell, how do you like that!\x02\x03",
            "#001FNot bad, for amateurs.\x02\x03",
            "Must've been some special\x01",
            "training, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1PGuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "What the hell...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PI had you figured for just another\x01",
            "bunch of punks, but you've got\x01",
            "some real spirit to you.\x02\x03",
            "#502FNice going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, it was nothing, really...\x02",
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    TurnDirection(0xC, 0xD, 600)

    ChrTalk(
        0xC,
        "#1P#2PDon't be taken in by that act!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A-Anyway...\x01",
            "You beat us before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We ain't gonna miss our chance\x01",
            "to get back at you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 600)

    ChrTalk(
        0x101,
        (
            "#006F#4PHa ha.\x01",
            "Any time you're ready.\x02\x03",
            "Though I guess not today, if\x01",
            "you guys are in the blue team\x01",
            "room with us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1PWell, we're supposed to be\x01",
            "on the other side, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#4PBut you couldn't wait to confront\x01",
            "your opponents, could you?\x02\x03",
            "#001FWell, best of luck!\x01",
            "May the better team win!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xD, 0xFF)

    ChrTalk(
        0xC,
        "#1P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#4PHuh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(
        0xC,
        "#1P#2PHey, let's get outta here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah...\x01",
            "The mood's all off, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let's go get something to\x01",
            "eat before the fight.\x02",
        )
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
        (
            "#580F#2PWell, what the hell?\x01",
            "That's just rude.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F#2PDid I say something wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x108, 0x101, 0)
    TurnDirection(0x104, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F#3PNo...not at all.\x02\x03",
            "#019FYou really are something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#4PHa ha...\x01",
            "Well, don't worry about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#6PI'm impressed that she's so\x01",
            "nonchalant about her own talents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#2PDid I miss something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#3PHa ha. Don't worry about it.\x02\x03",
            "#010FC'mon. Let's just get in the\x01",
            "waiting room and wait for\x01",
            "our match to start.\x02",
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
            "#503FAlmost time to start...\x02\x03",
            "My heart feels like it's gonna\x01",
            "break right out of my chest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FCalm down.\x02\x03",
            "All we have to do is wait\x01",
            "patiently until it's our\x01",
            "turn. They'll call for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FThat doesn't calm me down at all!\x02",
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
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We must apologize to everyone\x01",
            "for the long wait.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But we will now commence with\x01",
            "the no-holds-barred matches!\x02",
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
        "#840FOkay, we're up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820FThe Assault Cavalry is made up of\x01",
            "the best men of the uniform.\x02\x03",
            "They won't be easy to beat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000FGood luck, guys!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#831F#3PYou just leave the heavy\x01",
            "lifting to us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "#816FLet's goooooo!\x02",
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
        "#001F#6PAll right! They did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PLiberl's bracers are not to\x01",
            "be trifled with.\x02\x03",
            "They all demonstrated great skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FIndeed, they may be few in number,\x01",
            "but one of them could likely take\x01",
            "on a thousand foes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FIf we have to face them in a match,\x01",
            "we'll have a tough time of it.\x02",
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
        "#508FGreat match, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F#4PYo! Nice fight.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x3)

    ChrTalk(
        0xB,
        (
            "#841FHa ha... It's an honor to be\x01",
            "told so by 'Zane the Immovable.'\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x3)

    ChrTalk(
        0xA,
        (
            "#825FIt feels different from the\x01",
            "prelim matches. Much harder\x01",
            "to stay focused.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Here's the lineup for the 2nd match...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team: From the\x01",
            "Calvard Republic... Captained\x01",
            "by martial arts master, Zane!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team: Team\x01",
            "Raven, captained by Deen!\x02",
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
        "#006F#6PThat's us!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#015FAnd look who we're facing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FHa ha. Facing such louts ought to\x01",
            "prove most interesting, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#076F#4PAll right, to the arena!\x02",
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
            "#830FHa ha. I never thought those\x01",
            "delinquents would ever fight\x01",
            "that hard for anything.\x02\x03",
            "Just goes to show you that change\x01",
            "is the only constant in life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#820FI watched the fight closely.\x01",
            "It wasn't bad! Not bad at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa ha ha... Thank you.\x02\x03",
            "I like to think that their change\x01",
            "of heart is born of a desire to\x01",
            "follow my shining moral example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#814FWow...\x01",
            "You really think so?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#007F#4PWould you quit with your bullshit?\x01",
            "You don't even know their situation.\x02\x03",
            "#509FYou don't even really know\x01",
            "who we're talking about!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FThe moment one falls in love is\x01",
            "as quick as infinity itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018FYou're not...'normal', are you?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Here's the lineup for the 3rd match...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the Royal Army's 3rd Regiment...\x01",
            "Captained by 1st. Lieutenant Riel!\x02",
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
        "#5POkay, that's our cue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PLet's show 'em how it's\x01",
            "done, people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Aye-aye, sir!\x02",
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
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Capua Family, a.k.a. the Sky\x01",
            "Bandits... Captained by Don Capua!\x02",
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
        "#580F#4P#3SHuh?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FThe Capuas...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033FHmmm...\x01",
            "That name rings a few bells...\x02",
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
            "#074F#4PYou know, I somehow get the feeling...\x02\x03",
            "#070F...that this new 'team play'\x01",
            "rule was enacted so that those\x01",
            "criminals could participate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa ha ha... The duke is\x01",
            "certainly a generous man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#4PThis is no laughing matter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017FI kind of expected something\x01",
            "crazy, but this is just...\x02",
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
            "#505F#4P*sigh*\x01",
            "They won...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWell, they ARE pretty strong.\x02\x03",
            "#017FBut if worse comes to worst, and\x01",
            "they actually win the championship...\x01",
            "THEN what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FHa ha ha. Would they actually\x01",
            "invite pirates into the castle for\x01",
            "a dinner party?\x02\x03",
            "Oh, to be a fly on the wall for\x01",
            "THAT little soiree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#4PWe need to make sure that it\x01",
            "doesn't come to that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#4PRegardless, this means that\x01",
            "we have a tough opponent to\x01",
            "deal with.\x02",
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
            "#6PDamn it... I can't believe that\x01",
            "those thugs got the better of us...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x17, 0xFF)
    OP_8E(0x17, 0x13A10, 0x0, 0xFFFF033B, 0x7D0, 0x0)

    ChrTalk(
        0x17,
        "#2PWell, don't get so depressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2PThey're used to fighting as a\x01",
            "group. That's all.\x02",
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
            "#5PIt's not their strength, so\x01",
            "much as our weakness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhich means we need to do some\x01",
            "more training when we get back\x01",
            "to our unit.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Here's the lineup for the 4th match...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the Border Patrol, 7th\x01",
            "Regiment... Captained by 1st\x01",
            "Lieutenant Bern!\x02",
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
        "#5PLooks like you're up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThis is the last fight of the day,\x01",
            "so you better make it count.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#2PUnderstood. We'll give them twelve\x01",
            "kinds of hell, army-style.\x02",
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
        "#5PLet's do this, people!\x02",
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
        "#2P#1KYes, sir!\x02",
    )


    ChrTalk(
        0x13,
        "#1P#1KYes, sir!\x02",
    )


    ChrTalk(
        0x14,
        "#2P#1KYes, sir!\x02",
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
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From the Royal Army Intelligence\x01",
            "Division, captained by 2nd\x01",
            "Lieutenant Lorence!\x02",
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
        "#005F#4PHey, it's them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4PLieutenant Lorence...\x01",
            "Wasn't he the one who...\x02",
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
            "#005F#3PH-Holy...\x01",
            "That was a massacre!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F*whistle* Impressive.\x02\x03",
            "Given that they were a man short\x01",
            "in the prelims, I figured they'd\x01",
            "have another join in.\x02\x03",
            "I guess they had an ace in the hole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#032FEstelle, Joshua and I are also aces\x01",
            "in that same hole, then, since we\x01",
            "too missed the preliminaries.\x02\x03",
            "#035FHa ha. Perhaps that bodes well for\x01",
            "us. The trick is to come late!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#514FThat fighting style...\x02",
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
            "#505FHuh?\x02\x03",
            "Joshua? What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013FIt can't be...but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FJoshua? Joshua!\x02",
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F#4POh...\x02\x03",
            "#019FI'm okay...\x01",
            "No need to worry.\x02\x03",
            "I was...just kind of taken aback at\x01",
            "how good that guy's swordsmanship is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FI'm impressed. You've got a\x01",
            "good eye, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And that concludes our first\x01",
            "day of full-contact matches.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Today's winners were Kurt's\x01",
            "Team, Don's Team, Zane's Team\x01",
            "and Lorence's Team!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Who among them will be crowned\x01",
            "the king of fighters? Stay with\x01",
            "us to find out!\x02",
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
            "Received \x07\x04",
            "20000\x07\x00",
            " mira cash prize.\x02",
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
        "Girl's Voice",
        "#2POh, there you are!\x02",
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
        "#501F#1PHi, Dorothy!\x02",
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
            "#010FShort time no see.\x02\x03",
            "Seeing as how we only just\x01",
            "saw each other in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151FYeah, I know...\x02\x03",
            "I never dreamed we'd meet again\x01",
            "in this life...\x02\x03",
            "I mean, since you got in so much\x01",
            "trouble after you boarded that\x01",
            "factory ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F'So much trouble'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030FWell, well...\x01",
            "This bears investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580FWhoa, whoa, wait! Dorothy, can\x01",
            "we maybe save that conversation\x01",
            "for later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153FHuh...?\x02\x03",
            "Anyway, I was going to say,\x01",
            "your friends here look kind\x01",
            "of familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FI seem to recall encountering\x01",
            "you once, in the city of Bose.\x02\x03",
            "It's a pleasure to make your\x01",
            "acquaintance once more, my\x01",
            "uniquely charming lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071FWe passed by each other near \x01",
            "the hot spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151FOhhhhhh, I remember now.\x02\x03",
            "It's the drink-and-run guy,\x01",
            "and the bear in Eastern clothing!\x02\x03",
            "#150FSo, Estelle, are you and Joshua\x01",
            "fighting alongside these two in\x01",
            "the competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FYep, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe're on Zane's team. The 'bear\x01",
            "in Eastern clothing,' as you put it.\x02\x03",
            "So what about you? Are you covering\x01",
            "the event for the newspaper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150FWeeeell... Until yesterday, I\x01",
            "was working on another story.\x02\x03",
            "Nial told me this morning that\x01",
            "I should check out the Martial\x01",
            "Arts Competition to see you guys.\x02\x03",
            "#151FYou're as strong as he\x01",
            "said you were.\x02\x03",
            "This is gonna make for some\x01",
            "great pictures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FHa ha ha...\x01",
            "I hope so.\x02\x03",
            "#004FOh, yeah...\x01",
            "Isn't Nial with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#154FNah, I guess he had something\x01",
            "important to check up on.\x02\x03",
            "I think he was up all last night,\x01",
            "wrestling with a bunch of papers\x01",
            "or something.\x02\x03",
            "He told me today that he was going\x01",
            "to talk to an old acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150FOh, and he wanted me to pass\x01",
            "a message on to you.\x02\x03",
            "He wants you to come by the editorial\x01",
            "department this evening.\x02\x03",
            "Whatever it is, he made it\x01",
            "sound serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FHmmm... Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll go after today's matches.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#037FAh, serious conversation!\x01",
            "My old nemesis!\x02\x03",
            "#031FWell, don't let it get you down...\x01",
            "*purrrr* Meeoooww.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(
        0x101,
        (
            "#580FOh, would you stop? It doesn't\x01",
            "even have anything to do with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034FHow very cruel, Estelle...!\x02\x03",
            "And after our passions burned\x01",
            "so strongly together just\x01",
            "yesterday!\x02\x03",
            "Am I merely refuse, to be\x01",
            "discarded when circumstance\x01",
            "affords me no immediate use?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#582FWould you PLEASE stop\x01",
            "talking like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153FWow, Estelle. I had no idea!\x01",
            "Isn't he a little old for\x01",
            "you, though...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)

    ChrTalk(
        0x101,
        (
            "#509FHe's talking about the tournament.\x01",
            "But you're better off just ignoring\x01",
            "everything he says, either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151FI'm gonna go ahead and find a\x01",
            "good seat, so I can get the\x01",
            "best shots.\x02\x03",
            "I'll be rooting for you guys.\x01",
            "Good luck!\x02",
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
            "#073FShe's quite the...unique sort\x01",
            "of girl, isn't she?\x02",
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
            "#007F*sigh*...\x02\x03",
            "Between her and Olivier,\x01",
            "I just get so drained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FThat just means we're relieving\x01",
            "your stress before the match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FShe IS a pretty skilled photographer,\x01",
            "at least.\x02\x03",
            "Most of the photographs that have been\x01",
            "published in the Liberl News lately were\x01",
            "taken by her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073FHmm... Impressive.\x02\x03",
            "#071FIn that case, we'll have to make\x01",
            "sure that our fight is one worth\x01",
            "taking pictures of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah, no kidding.\x02\x03",
            "I dunno who we're facing, but\x01",
            "we need to get psyched!\x02",
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
        "Girl's Voice",
        "#1POh, there you are!\x02",
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
        "#501F#4PHi, Dorothy!\x02",
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
            "#010F#6PShort time no see.\x02\x03",
            "Seeing as how we only just\x01",
            "saw each other in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F#4PYeah, I know...\x02\x03",
            "I never dreamed we'd meet again\x01",
            "in this life...\x02\x03",
            "I mean, since you got in so much\x01",
            "trouble after you boarded that\x01",
            "factory ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F#6P'So much trouble'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F#6PWell, well...\x01",
            "This bears investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F#6PWhoa, whoa, wait! Dorothy, can\x01",
            "we maybe save that conversation\x01",
            "for later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153F#4PHuh...?\x02\x03",
            "Anyway, I was going to say,\x01",
            "your friends here look kind\x01",
            "of familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#6PI seem to recall encountering\x01",
            "you once, in the city of Bose.\x02\x03",
            "It's a pleasure to make your\x01",
            "acquaintance once more, my\x01",
            "uniquely charming lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#6PWe passed by each other near \x01",
            "the hot spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F#4POhhhhhh, I remember now.\x02\x03",
            "It's the drink-and-run guy,\x01",
            "and the bear in Eastern clothing!\x02\x03",
            "#150FSo, Estelle, are you and Joshua\x01",
            "fighting alongside these two in\x01",
            "the competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#6PYep, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6PWe're on Zane's team. The 'bear\x01",
            "in Eastern clothing,' as you\x01",
            "put it.\x02\x03",
            "So what about you? Are you covering\x01",
            "the event for the newspaper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150F#4PWeeeell... Until yesterday, I\x01",
            "was working on another story.\x02\x03",
            "Nial told me this morning that\x01",
            "I should check out the Martial\x01",
            "Arts Competition to see you guys.\x02\x03",
            "#151FYou're as strong as he\x01",
            "said you were.\x02\x03",
            "This is gonna make for some\x01",
            "great pictures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#6PHa ha ha...\x01",
            "I hope so.\x02\x03",
            "#004FOh, yeah...\x01",
            "Isn't Nial with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#154F#4PNah, I guess he had something\x01",
            "important to check up on.\x02\x03",
            "I think he was up all last night,\x01",
            "wrestling with a bunch of papers\x01",
            "or something.\x02\x03",
            "He told me today that he was going\x01",
            "to talk to an old acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#150F#4POh, and he wanted me to pass\x01",
            "a message on to you.\x02\x03",
            "He wants you to come by the editorial\x01",
            "department this evening.\x02\x03",
            "Whatever it is, he made it\x01",
            "sound serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#6PHmmm... Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#6PWe'll go after today's matches.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#037F#6PAh, serious conversation!\x01",
            "My old nemesis!\x02\x03",
            "#031FWell, don't let it get you down...\x01",
            "*purrrr* Meeoooww.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(
        0x101,
        (
            "#580F#6POh, would you stop? It doesn't\x01",
            "even have anything to do with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#034F#6PHow very cruel, Estelle...!\x02\x03",
            "And after our passions burned\x01",
            "so strongly together just\x01",
            "yesterday!\x02\x03",
            "Am I merely refuse, to be\x01",
            "discarded when circumstance\x01",
            "affords me no immediate use?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#582F#6PWould you PLEASE stop\x01",
            "talking like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#153F#4PWow, Estelle. I had no idea!\x01",
            "Isn't he a little old for\x01",
            "you, though...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 600)

    ChrTalk(
        0x101,
        (
            "#509F#6PHe's talking about the tournament.\x01",
            "But you're better off just ignoring\x01",
            "everything he says, either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#151F#4PI'm gonna go ahead and find a\x01",
            "good seat, so I can get the\x01",
            "best shots.\x02\x03",
            "I'll be rooting for you guys.\x01",
            "Good luck!\x02",
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
            "#073FShe's quite the...unique sort\x01",
            "of girl, isn't she?\x02",
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
            "#007F*sigh*...\x02\x03",
            "Between her and Olivier,\x01",
            "I just get so drained...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031FThat just means we're relieving\x01",
            "your stress before the match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FShe IS a pretty skilled\x01",
            "photographer, at least.\x02\x03",
            "The latest Liberl News was full\x01",
            "of her work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073FHmm... Impressive.\x02\x03",
            "#071FIn that case, we'll have to make\x01",
            "sure that our fight is one worth\x01",
            "taking pictures of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah, no kidding.\x02\x03",
            "I dunno who we're facing, but\x01",
            "we need to get psyched!\x02",
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
            "#505FUgh... They're late.\x02\x03",
            "The match is due to start soon,\x01",
            "so where's the other team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FIt is kind of strange.\x02\x03",
            "Maybe something's holding\x01",
            "them up, or...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Man's Voice",
        "#1PCome on, get a move on!\x02",
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
        "Audacious Voice",
        (
            "#1PWe're moving, we're moving! Quit rushing us,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Young Man's Voice",
        (
            "#1PUgh... Why did things have to turn out like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Girl's Voice",
        (
            "#1PC'mon, bro...\x01",
            "C'mon, bro, don't be getting all sad on us now!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Girl's Voice",
        (
            "#1PWe need to keep our spirits up in case we end\x01",
            "up fighting THEM today!\x02",
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
        "#004F#6PBuh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1A, 0x2)

    ChrTalk(
        0x1A,
        "#192F#4PYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6PSo it was your team...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#6PHeh. I should have known\x01",
            "they wouldn't show up in a\x01",
            "timely fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#200F#2PHmph, guess we won't be fighting you lot\x01",
            "today after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#210F#2PHmph. Looks like you got lucky this time.\x02\x03",
            "I'd been hoping we'd get matched\x01",
            "up with you, so we could give\x01",
            "the she-man there a lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6POh...you did NOT...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        "Hey! No idle chatter!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Guard",
        (
            "Or did you forget that it's only by\x01",
            "His Excellency's generosity that\x01",
            "you're even in this competition?\x02",
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
            "#191F#6PCome now, soldier. You don't\x01",
            "need to worry about this.\x02\x03",
            "Have we not been well-behaved\x01",
            "so far?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        (
            "And I just hope you decide to\x01",
            "keep that up until you go back\x01",
            "to jail.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        "Don't even talk to them.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        (
            "You don't make any trouble, and\x01",
            "we won't make trouble for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6PI don't think there'll be a\x01",
            "problem. They want to clobber\x01",
            "us tomorrow, after all.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Guard",
        (
            "I think you know this, but there's\x01",
            "a full company of soldiers here\x01",
            "on security detail.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Guard",
        (
            "#2PDon't even start imagining that\x01",
            "you have any chance of escaping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#202F#5PWe know already.\x01",
            "We're not idiots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#211F#5PHmph. You guys are a real eyesore,\x01",
            "so why don't you just go already?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        "You little...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    NpcTalk(
        0x10,
        "Guard",
        "#2PDon't let this kid provoke you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)

    NpcTalk(
        0x10,
        "Guard",
        "Just don't try any funny business.\x02",
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
            "#505F#6PHey...\x01",
            "What's going on?\x02\x03",
            "How'd you guys wind up in the\x01",
            "Martial Arts Competition?\x02",
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
            "#012F#6PIs it really because Duke Dunan\x01",
            "allowed it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#200FYeah, seems that way. He\x01",
            "supposedly called for us\x01",
            "specifically to participate.\x02\x03",
            "The better we do, the lighter\x01",
            "our sentence gets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6PY-You've got to be kidding me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074FHmmm... That's a little strange\x01",
            "for a constitutional monarchy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#6PHa ha ha. It seems the\x01",
            "duke is a mischievous sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#197FWell, you won't see us complaining.\x02\x03",
            "I'd rather work off my sentence\x01",
            "than spend it in prison.\x02\x03",
            "But then...\x01",
            "That's not the only reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6PWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#214F#2PAh, shut it. It ain't any of\x01",
            "your business, anyhow.\x02\x03",
            "It matters to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6PSo, if you're not here to fight us...\x02\x03",
            "Then are you here to take on\x01",
            "the Special Ops soldiers?\x02",
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
        "#213F#2PWha... How...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#196FDamn straight we are!\x02\x03",
            "They were supposed to be our\x01",
            "allies, and they screwed us over!\x02\x03",
            "They used us to help expand the\x01",
            "Intelligence Division's influence,\x01",
            "then tossed us aside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#203FWe're idiots, plain and simple.\x01",
            "We got double-crossed.\x02\x03",
            "And that really sucks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6PYeah, I suppose so...\x02\x03",
            "Come to think of it, I even feel\x01",
            "kind of bad for you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#214F#2PListen, we don't want your\x01",
            "damn pity!\x02\x03",
            "You owe US,\x01",
            "and don't you forget it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#6PHuh?\x02\x03",
            "What do you mean by that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#200FHa ha... Don't you remember\x01",
            "the last time we met?\x02\x03",
            "It'd be a bad thing if you-know-\x01",
            "who found out that you snuck\x01",
            "into Leiston Fortress, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#191FWe don't like those jerks too\x01",
            "much, either, so we didn't say\x01",
            "anything about you.\x02\x03",
            "Ha ha ha!\x01",
            "You ought to thank us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F#6PGrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#6PIndeed... Thank you for keeping\x01",
            "it to yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#6PThis certainly sounds interesting.\x02\x03",
            "I'd LOOOOVE to hear more.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#582F#6PYou hush! It was nothing!\x02",
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
            "#073FWhoops...\x02\x03",
            "I hate to interrupt, but I think\x01",
            "we're starting shortly.\x02",
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
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We must apologize to everyone\x01",
            "for the long wait.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We now open the second day of\x01",
            "the Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Let's start up by announcing the\x01",
            "fight card for the 5th match!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team: From the\x01",
            "Calvard Republic... Captained\x01",
            "by martial arts master, Zane!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team: From the\x01",
            "Bracer Guild, Grancel branch...\x01",
            "Kurt's team!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x101,
        (
            "#005FHere we go!\x02\x03",
            "We're gonna actually be fighting\x01",
            "against Carna's crew!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FThis won't be easy.\x02\x03",
            "We need to make sure that we\x01",
            "don't get in Zane's way...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070FNo need to be so cautious.\x02\x03",
            "Your assistance will be just\x01",
            "as good as any full-fledged\x01",
            "bracers.\x02\x03",
            "All we need to do is focus\x01",
            "on winning.\x02",
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
        "#006FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll do our best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FHeh...\x01",
            "Let us be off...to GLORY!\x02",
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
        "#192FWell, well. Not bad at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#202FNo kidding. That was a pretty\x01",
            "exciting match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2P#212FH-Heh...\x01",
            "I suppose it wasn't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#5PHa ha ha!\x01",
            "Why, thank you. 侓\x02\x03",
            "#004FSo, what's the deal? Why are\x01",
            "YOU guys congratulating us?\x02\x03",
            "Got a fever or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2P#214FW-We're not congratulating you,\x01",
            "you little punk!\x02\x03",
            "It's just that it would be annoying\x01",
            "to lose so easily to the group that\x01",
            "drove us up a wall!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#5PYou've got a snappy comeback\x01",
            "for everything, don't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F#4PCome on, Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1C, 400)

    ChrTalk(
        0x102,
        (
            "#019F#4PThank you very much.\x02\x03",
            "I know a lot's happened between\x01",
            "us, and still you cheered us on.\x01",
            "We appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x102, 400)

    ChrTalk(
        0x1C,
        "#414FWha...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x1C,
        (
            "#216FI-I'm trying to tell you that\x01",
            "we're NOT cheering you on!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#5P(Hm...?)\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Next up is the 6th match...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South side, blue team: The Sky\x01",
            "Bandits, a.k.a. the Capua Family...\x01",
            "captained by Don Capua!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "North side, red team: From the Royal\x01",
            "Army Intelligence Division, captained\x01",
            "by 2nd Lieutenant Lorence!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TurnDirection(0x1A, 0x1C, 400)

    ChrTalk(
        0x1A,
        "#196FAll right, it's finally time!\x02",
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
            "#5P#201FTime to teach those sneaky\x01",
            "assholes a lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5PMaybe this is how it was\x01",
            "destined to play out.\x02\x03",
            "Our fingers are crossed for\x01",
            "you. Good luck!\x02",
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
            "#012F#4PWatch out for their commanding officer.\x02\x03",
            "Keep him pinned down, and you'll\x01",
            "have a fighting chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#414FO-Okay...\x02\x03",
            "#214FI mean, uh, shut up! It's none\x01",
            "of your business, anyway!\x02",
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
        (
            "#007FAwww, man...\x01",
            "They lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033FThey were doing pretty\x01",
            "well, at first.\x02\x03",
            "It all fell apart when that\x01",
            "fellow in red started in on\x01",
            "them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072FHmmm... Definitely not an opponent\x01",
            "to be trifled with.\x02\x03",
            "I don't think he was even trying\x01",
            "as hard as he could. I can't get a\x01",
            "decent read on his real strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FPLEASE tell me you're joking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FNo, I think it's the truth.\x02\x03",
            "That last technique just didn't\x01",
            "feel like it was even all that\x01",
            "focused.\x02\x03",
            "He's still got plenty we haven't\x01",
            "seen yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009FTh-That's just crazy...\x02",
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
        "#197F#5P...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 0x3)

    ChrTalk(
        0x1B,
        "#204F#5P...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0x3)

    ChrTalk(
        0x1C,
        "#215F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#4PUh...\x01",
            "I'm sorry, you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#197F#5PDon't try to cheer us up, please.\x02\x03",
            "We got slaughtered out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#205F#5PDamn it! If my support tactics\x01",
            "weren't so worthless...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x19, 0xFF)
    TurnDirection(0x1C, 0x1B, 400)

    ChrTalk(
        0x1C,
        (
            "#216F#2PIt wasn't your fault!\x02\x03",
            "I'm the one who wasted all that\x01",
            "energy on attacks that didn't\x01",
            "do anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#4P...\x02\x03",
            "#007FWell, hey. Sometimes it comes\x01",
            "down to more than just who's\x01",
            "stronger.\x02\x03",
            "#006FWe're gonna get him back for\x01",
            "you when we fight him tomorrow!\x02",
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
        "#192F#5PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#201F#5PHeh...\x01",
            "You make it sound so simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3P#017FI'm not fond of promising what\x01",
            "I'm not sure I can deliver...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071FA battle has to be won in the\x01",
            "mind before it can be won in\x01",
            "the flesh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#4PWhat a fine saying! 'Tis as if you and\x01",
            "Estelle speak with the same mind...but\x01",
            "you, sir, with a more golden tongue!\x02",
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
        "Guard",
        (
            "#1PHmph...\x01",
            "Looks like you're finally done.\x02",
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
        "Guard",
        (
            "All right, no hanging about!\x01",
            "Back to the docks with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#192F#5PYou've gotta be kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#202FWe JUST got done fighting...\x01",
            "Can't you give us a few minutes\x01",
            "to rest?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        (
            "#5PYou know, for hardened criminals,\x01",
            "you sure act like spoiled brats.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "Guard",
        "Come on, now get moving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#197F#5PBah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#203FI'm so worn out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#215F#5P...\x02",
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
        "#212F#1PHey, bracer jerks...\x02",
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
        "#004F#6PWha...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x102, 400)

    ChrTalk(
        0x1C,
        (
            "#215F#2PWe aren't gonna be here tomorrow...\x02\x03",
            "#214F...but you'd damn well better win!\x02\x03",
            "If you let those assholes beat\x01",
            "you, then you're gonna have\x01",
            "hell to pay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3P...\x02\x03",
            "#001FOf course we're gonna win!\x01",
            "Who do you think you're\x01",
            "talking to here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll win...\x01",
            "I swear it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Guard",
        "#5PAre you done?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Guard",
        "#5PEnough stalling.\x02",
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
            "Received \x07\x04",
            "40000\x07\x00",
            " mira cash prize.\x02",
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
            "#008F*sigh* Looks like it's just us\x01",
            "in here. This waiting room feels\x01",
            "awfully big right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWell, it actually IS a pretty big\x01",
            "room. Team sports events and circuses\x01",
            "alike used to be held here.\x02\x03",
            "But that was back in a time when\x01",
            "gladiators fighting monsters was\x01",
            "a man's only source of entertainment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FInteresting... I guess that would\x01",
            "explain the size, if there were\x01",
            "circus animals in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F#5PI must say, it certainly doesn't\x01",
            "measure up to an Imperial opera\x01",
            "house, but even so...\x02\x03",
            "...it's about the size of an\x01",
            "outdoor concert venue. And\x01",
            "that's...certainly acceptable!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#509FExcuse us for being less gaudy\x01",
            "than you Imperialists.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 135, 400)

    ChrTalk(
        0x108,
        (
            "#070F#6PI think we may have gotten here\x01",
            "a little too early, though.\x02\x03",
            "We've still got a sizable chunk\x01",
            "of time before the match starts.\x02",
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
            "#5P#004FReally?\x02\x03",
            "#007FUgh... Waiting around for your\x01",
            "match to start really does get\x01",
            "kind of boring.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FSo why don't we walk around the\x01",
            "grounds for a little while, then?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#5P#001FWorks for me.\x02",
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
            "#5P#006FWe're gonna go out for\x01",
            "a walk, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#6PSure. Just make sure you're\x01",
            "here in time for the match.\x02",
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
        "#030F...\x02",
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
            "#073F#4PWell, well. What new turn\x01",
            "of events is this?\x02\x03",
            "I thought for sure that you'd\x01",
            "go with them.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x104, 0xFF)
    TurnDirection(0x104, 0x108, 400)

    ChrTalk(
        0x104,
        (
            "#035F#6PHmmm... I just get the feeling\x01",
            "that something's changed between\x01",
            "the two of them.\x02\x03",
            "Some type of step forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F#4PHello, Mr. Observant.\x02\x03",
            "#070FThey've definitely been feeling \x01",
            "some pressure from the matches...\x02\x03",
            "But today, they seem a\x01",
            "lot more relaxed.\x02\x03",
            "#071FOh, to be that young again, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#6PBut...are they ready for the feelings\x01",
            "that well up from within them?\x02\x03",
            "Even if they are not...the feelings\x01",
            "are surely ready for them!\x02\x03",
            "#037FHa ha...\x01",
            "Such delightful awkwardness!\x01",
            "I look forward to what comes of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#075F#4PI really just don't get you.\x02",
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
        "#009F*shudder*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014FSomething wrong?\x02\x03",
            "Are you feeling all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#509FI'm okay... I just got the chills\x01",
            "all of a sudden.\x02\x03",
            "Like someone is talking about\x01",
            "us or plotting something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017FI think I can guess who that is...\x02",
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
        "Old Man's Voice",
        "#4POh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Man's Voice",
        (
            "#4PEstelle? Joshua?\x01",
            "Is that you?\x02",
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
        "#004FMayor Klaus!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhat brings you here...?\x02",
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
            "#601FIt's good to see you both again.\x02\x03",
            "Scherazard told me that you'd\x01",
            "gone traveling all over the\x01",
            "kingdom.\x02\x03",
            "You've certainly grown up\x01",
            "nicely in the time since we\x01",
            "last met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FWeeeell, I can't speak for\x01",
            "myself, really...\x02\x03",
            "#501FBut you certainly seem as\x01",
            "chipper as ever, Mr. Mayor.\x02\x03",
            "It's kind of refreshing to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#601FHa ha. Well, I won't let you\x01",
            "young folk beat me just yet.\x02\x03",
            "So...I hear that you two made it all\x01",
            "the way to the championship in this\x01",
            "big Martial Arts Competition!\x02\x03",
            "I may be a little old for such\x01",
            "things, but I came to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FYou came all the way from\x01",
            "Rolent for THAT?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600FNo, no...\x02\x03",
            "Actually, I got an invitation\x01",
            "out of the blue to a dinner\x01",
            "party at Grancel Castle.\x02\x03",
            "I only arrived in Grancel this morning.\x01",
            "Came by way of an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FNo way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FAhh, I think I get it.\x02\x03",
            "#010FThe invitation came from\x01",
            "Duke Dunan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#604FOh, you know of it?\x02\x03",
            "#600FI was originally planning to attend\x01",
            "a birth ceremony for this married\x01",
            "couple and then journey here...\x02\x03",
            "But this lady officer approached\x01",
            "me out of nowhere, and told me that\x01",
            "I was invited to this dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F(One guess as to who that was...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F(Yeah, it had to be Captain Amalthea...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#603FSadly, my wife's just not much\x01",
            "of the traveling sort.\x02\x03",
            "So, I didn't have much choice\x01",
            "but to come here by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FAww...\x01",
            "She's not here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FPardon me, Mayor.\x02\x03",
            "There is a chance that we may also\x01",
            "be attending that dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#604FOhh...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua explained that the duke had stated that the winner of the\x01",
            "competition would receive a formal invitation to the party.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x1E,
        (
            "#604FAhh, I see.\x01",
            "Well, that explains it.\x02\x03",
            "#600FIt hardly seems appropriate to\x01",
            "call for a dinner party when\x01",
            "Her Majesty has taken ill...\x02\x03",
            "But if you two will be there, I\x01",
            "might not feel quite so awkward.\x02\x03",
            "#601FSo that just means that you'll have\x01",
            "to try that much harder to win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FHa ha ha... You bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll try our best to meet\x01",
            "your expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600FI think I'm going to find\x01",
            "myself a seat, then.\x02\x03",
            "Best of luck to the both of you.\x02",
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
        "Old Man's Voice",
        "#1POh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1E,
        "Old Man's Voice",
        (
            "#1PEstelle? Joshua?\x01",
            "Is that you?\x02",
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
        "#004FMayor Klaus!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhat brings you here...?\x02",
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
            "#601FIt's good to see you both again.\x02\x03",
            "Scherazard told me that you'd\x01",
            "gone traveling all over the\x01",
            "kingdom.\x02\x03",
            "You've certainly grown up\x01",
            "nicely in the time since we\x01",
            "last met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019FHa ha...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FWeeeell, I can't speak for\x01",
            "myself, really...\x02\x03",
            "#501FBut you certainly seem as\x01",
            "chipper as ever, Mr. Mayor.\x02\x03",
            "It's kind of refreshing to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#601FHa ha. Well, I won't let you\x01",
            "young folk beat me just yet.\x02\x03",
            "So...I hear that you two made it all\x01",
            "the way to the championship in this\x01",
            "big Martial Arts Competition!\x02\x03",
            "I may be a little old for such\x01",
            "things, but I came to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FYou came all the way from\x01",
            "Rolent for THAT?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600FNo, no...\x02\x03",
            "Actually, I got an invitation\x01",
            "out of the blue to a dinner\x01",
            "party at Grancel Castle.\x02\x03",
            "I only arrived in Grancel this morning.\x01",
            "Came by way of an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580FNo way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015FAhh, I think I get it.\x02\x03",
            "#010FThe invitation came from\x01",
            "Duke Dunan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#604FOh, you know of it?\x02\x03",
            "#600FI was originally planning to attend\x01",
            "a birth ceremony for this married\x01",
            "couple and then journey here...\x02\x03",
            "But this lady officer approached\x01",
            "me out of nowhere, and told me that\x01",
            "I was invited to this dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F(One guess as to who that was...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F(Yeah, it had to be Captain Amalthea...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#603FSadly, my wife's just not much\x01",
            "of the traveling sort.\x02\x03",
            "So, I didn't have much choice\x01",
            "but to come here by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FAww...\x01",
            "She's not here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FPardon me, Mayor.\x02\x03",
            "There is a chance that we may also\x01",
            "be attending that dinner party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#604FOhh...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Estelle and Joshua explained that the duke had\x01",
            "stated that the winner of the competition would\x01",
            "receive a formal invitation to the party.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x1E,
        (
            "#604FAhh, I see.\x01",
            "Well, that explains it.\x02\x03",
            "#600FIt hardly seems appropriate to\x01",
            "call for a dinner party when\x01",
            "Her Majesty has taken ill...\x02\x03",
            "But if you two will be there, I\x01",
            "might not feel quite so awkward.\x02\x03",
            "#601FSo that just means that you'll have\x01",
            "to try that much harder to win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001FHa ha ha... You bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll try our best to meet\x01",
            "your expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#600FI think I'm going to find\x01",
            "myself a seat, then.\x02\x03",
            "Best of luck to the both of you.\x02",
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
            "#505FI can't believe he's going to\x01",
            "be at the dinner party, too...\x02\x03",
            "You think Mayor Maybelle will\x01",
            "be there, as well?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#4P#012FIt seems likely.\x02\x03",
            "There will probably be a lot of\x01",
            "influential people in attendance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007FHmmm... Ah, well.\x02\x03",
            "#006FWe just need to focus on winning\x01",
            "our match, and then we'll see\x01",
            "everyone there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4P#010FSounds good.\x02\x03",
            "Speaking of which, it's almost\x01",
            "time. Let's return to the\x01",
            "waiting room. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay!\x02",
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
            "#580FOh...\x02\x03",
            "It looks like the duke and Colonel\x01",
            "Richard are showing up together today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FIndeed...\x02\x03",
            "Maybe he's here to watch his\x01",
            "subordinates compete...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070FOh, so that's the Royal Army's\x01",
            "darling of the public, eh?\x02\x03",
            "He's handsome enough, and well-groomed.\x01",
            "He looks like the capable sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007FYeah... I guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033FHmm... He doesn't seem to bear much\x01",
            "resemblance to when I saw him in Bose,\x01",
            "at least in terms of character.\x02\x03",
            "#035FHeh... But what, indeed,\x01",
            "can one do?\x02\x03",
            "I suppose that he is worthy of\x01",
            "being considered a rival to the\x01",
            "great Olivier Lenheim.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#509F#6PI doubt he's worried about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F...Looks like it's starting.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Chairman's voice")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We must apologize to everyone\x01",
            "for the long wait.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We now open the final day of the\x01",
            "Martial Arts Competition's full-\x01",
            "contact matches.\x02",
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
        "#508FAll right! We're up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FFinally...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035FHeh... I trust everyone is ready\x01",
            "to put everything into this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074FFor tears or for laughter,\x01",
            "this is it...\x02\x03",
            "#076FGame faces, guys!\x02",
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
            "#111FHa ha... An interesting conclusion,\x01",
            "I'd say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x21, 400)

    ChrTalk(
        0x20,
        (
            "#183FHmph. Lieutenant Lorence, you\x01",
            "truly have no shame.\x02\x03",
            "His Excellency must surely be\x01",
            "ashamed to see his men beaten\x01",
            "by such rabble.\x02\x03",
            "Was all that posturing just\x01",
            "for show?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#281F...I am, indeed, shamed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110FHa ha... Come now, Amalthea.\x01",
            "You needn't criticize him so.\x02\x03",
            "Truth be told, I myself asked\x01",
            "Lorence to hold back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#184FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#115FIt would behoove any member of the\x01",
            "Intelligence Division not to put\x01",
            "ALL of his strengths on display.\x02\x03",
            "And in this instance, it works\x01",
            "to our benefit that the others\x01",
            "win the championship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#180FI see...\x02\x03",
            "#181FHis Excellency, too, seems taken\x01",
            "with the Easterner...\x02\x03",
            "He'll serve as an ample distraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110FStill... It is a pity.\x02\x03",
            "If Lieutenant Schwarz or General\x01",
            "Morgan had participated, the show\x01",
            "would have been far more dynamic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#182FHa ha... Surely you jest, sir.\x02\x03",
            "If you truly wanted the tournament to be more\x01",
            "dynamic, perhaps you should have participated\x01",
            "yourself?\x02\x03",
            "The likes of Julia are no match for your\x01",
            "strength, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#111FHa ha, I don't think quite that highly of\x01",
            "my skill with a sword.\x02\x03",
            "I doubt I would be able to defeat the 2nd\x01",
            "Lieutenant here if he fought as hard as he\x01",
            "could, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#281FHardly, sir.\x02\x03",
            "I believe you somewhat overestimate my\x01",
            "strength.\x02\x03",
            "I'm nothing but a unrefined former jaeger in a\x01",
            "soldier's uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110FI beg to differ. I have confidence in my\x01",
            "ability to judge the strength of others.\x02\x03",
            "And about the only person I could see being\x01",
            "able to fight you on equal terms would be\x01",
            "'him'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#281F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#183FSpeaking of whom...\x02\x03",
            "His children will shortly be\x01",
            "entering Grancel Castle.\x02\x03",
            "Shouldn't we be taking some sort\x01",
            "of steps to deal with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#110FLeave them be. We'll honor the\x01",
            "arrangement with the duke.\x02\x03",
            "#115FAnd besides, it's far too late\x01",
            "for the Bracer Guild to cause\x01",
            "us any real trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#184FB-But, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#112FLorence, how far along would\x01",
            "you gauge the plan's progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#280FJust over 90%, sir.\x02\x03",
            "I am certain I will be able to guide you to\x01",
            "our destination within the next few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#110FExcellent.\x02",
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
            "#115F...A new dawn fast approaches\x01",
            "for this kingdom.\x02\x03",
            "#111FAnd even if I must endure the stigma\x01",
            "of treason...I shall pave the way\x01",
            "for the glorious morrow!\x02",
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
        "#014FThat's the exit, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004FOops... Don't want to leave\x01",
            "yet, do we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F48D")

    label("loc_F468")


    ChrTalk(
        0x101,
        "#002FNo need to leave just yet.\x02",
    )

    CloseMessageWindow()

    label("loc_F48D")

    Jump("loc_F574")

    label("loc_F490")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4D5")

    ChrTalk(
        0x102,
        (
            "#010FThis is the exit.\x02\x03",
            "We can't leave just yet.\x02",
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
        (
            "#074FWhoops...\x01",
            "This is the exit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F53E")

    label("loc_F515")


    ChrTalk(
        0x108,
        (
            "#070FHm.\x01",
            "No need to leave just yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F53E")

    Jump("loc_F574")

    label("loc_F541")


    ChrTalk(
        0x104,
        (
            "#030FHmm...\x01",
            "This would appear to be the exit.\x02",
        )
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
            "Reserved for Guests of Honor\x01",
            "- \x01",
            "No Unauthorized Personnel\x02",
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
            "The door is locked.\x02",
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
        "#501FOh, this leads to the hallway...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F68C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F717")
    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070FHey, that's the hallway.\x02\x03",
            "If you're looking for the ring,\x01",
            "it's through the other door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FOh, okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F717")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78E")
    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070FHey, that's the hallway.\x02\x03",
            "If you're looking for the ring,\x01",
            "it's through the other door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F78E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C5")

    ChrTalk(
        0x108,
        "#070FWhoops... That's the hallway.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F87A")

    label("loc_F7C5")

    TurnDirection(0x108, 0x0, 400)

    ChrTalk(
        0x108,
        (
            "#070FHey, that's the hallway.\x02\x03",
            "If you're looking for the ring,\x01",
            "it's through the other door.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x108, 400)

    ChrTalk(
        0x104,
        (
            "#035FHeh... I knew that, obviously.\x01",
            "I was merely playing a joke.\x02",
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
            "#002FThis is the stadium entrance...\x02\x03",
            "#003FUgh...\x01",
            "I've gotta get a hold of myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA03")

    label("loc_F8FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F988")

    ChrTalk(
        0x101,
        (
            "#000FOops... It's not time for\x01",
            "the match yet!\x02\x03",
            "I suppose it can't hurt to walk\x01",
            "around the grounds a bit. We've\x01",
            "got time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA03")

    label("loc_F988")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA03")

    ChrTalk(
        0x102,
        (
            "#010FThis way is the arena...\x02\x03",
            "There's still time before our\x01",
            "match. Maybe we can walk around\x01",
            "the grounds.\x02",
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
            "#014FIsn't this the wrong room?\x02\x03",
            "I'm pretty sure that our room\x01",
            "is on the right-hand side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FOh, yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB65")

    label("loc_FAB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB10")

    ChrTalk(
        0x102,
        (
            "#010FThis is the red team's room...\x02\x03",
            "Our room must be on the other side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB65")

    label("loc_FB10")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010FThis is the red team's room...\x02\x03",
            "Our room must be on the other side.\x02",
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
            "#010FI think this is the waiting room\x01",
            "for one of the teams.\x02\x03",
            "I don't think they'd appreciate\x01",
            "us barging in on them.\x02",
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
