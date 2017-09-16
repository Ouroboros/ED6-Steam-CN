from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3300   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3300   ._SN',
            'ED6_DT01/T3300_1 ._SN',
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
        '加雷利',                               # 9
        '王',                                   # 10
        '布鲁诺',                               # 11
        '士兵布拉姆',                           # 12
        '士兵赫宁',                             # 13
        '派斯队长',                             # 14
        '格温副长',                             # 15
        '伦法',                                 # 16
        '鸡',                                   # 17
        '鸡',                                   # 18
        '鸡',                                   # 19
        '鸡',                                   # 20
        '托兰特平原道方向',                     # 21
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01760 ._CH',             # 01
        'ED6_DT07/CH01530 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01310 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01270 ._CH',             # 07
        'ED6_DT07/CH01720 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01760P._CP',             # 01
        'ED6_DT07/CH01530P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01310P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01270P._CP',             # 07
        'ED6_DT07/CH01720P._CP',             # 08
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
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1990,
        Z                   = -500,
        Y                   = -280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 8039,
        TriggerZ            = 0,
        TriggerY            = 21240,
        TriggerRange        = 1500,
        ActorX              = 8039,
        ActorZ              = 2000,
        ActorY              = 21240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_53F",          # 01, 1
        "Function_2_5A8",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_5E2",          # 04, 4
        "Function_5_606",          # 05, 5
        "Function_6_754",          # 06, 6
        "Function_7_8A2",          # 07, 7
        "Function_8_92E",          # 08, 8
        "Function_9_954",          # 09, 9
        "Function_10_11A3",        # 0A, 10
        "Function_11_12C1",        # 0B, 11
        "Function_12_12C8",        # 0C, 12
        "Function_13_190C",        # 0D, 13
        "Function_14_1913",        # 0E, 14
        "Function_15_223B",        # 0F, 15
        "Function_16_23D8",        # 10, 16
        "Function_17_289D",        # 11, 17
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2C0")
    Jump("loc_3B6")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FD")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 11760, 20, 31780, 236)
    OP_43(0x8, 0x0, 0x0, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 7490, -60, 24130, 273)
    Jump("loc_3B6")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_3B6")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_311")
    Jump("loc_3B6")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_331")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 11890, 0, 41360, 226)
    Jump("loc_3B6")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 11890, 0, 41360, 226)
    Jump("loc_3B6")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_391")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_38E")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13100, 0, 38170, 53)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16420, 0, 38700, 351)

    label("loc_38E")

    Jump("loc_3B6")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_39B")
    Jump("loc_3B6")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3A5")
    Jump("loc_3B6")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3AF")
    Jump("loc_3B6")

    label("loc_3AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B6")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3FC")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)
    Jump("loc_53E")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_41C")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    Jump("loc_53E")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_478")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6340, 0, 48700, 159)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)
    Jump("loc_53E")

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4BE")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)
    Jump("loc_53E")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4FB")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F8")
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x10)

    label("loc_4F8")

    Jump("loc_53E")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_53E")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 790, 0, 48280, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)

    label("loc_53E")

    Return()

    # Function_0_2B6 end

    def Function_1_53F(): pass

    label("Function_1_53F")

    OP_16(0x2, 0xFA0, 0xFFFE1BA0, 0xFFFEB7E0, 0x30055)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_560")
    OP_71(0x4, 0x4)
    Jump("loc_593")

    label("loc_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_56A")
    Jump("loc_593")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_574")
    Jump("loc_593")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_58E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B")
    OP_71(0x4, 0x4)

    label("loc_58B")

    Jump("loc_593")

    label("loc_58E")

    OP_71(0x4, 0x4)

    label("loc_593")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_28(0x2A, 0x1, 0x1000)

    label("loc_5A7")

    Return()

    # Function_1_53F end

    def Function_2_5A8(): pass

    label("Function_2_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A8")

    label("loc_5BD")

    Return()

    # Function_2_5A8 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E1")
    OP_8D(0xFE, 8640, 35670, 14490, 27640, 2000)
    Jump("Function_3_5BE")

    label("loc_5E1")

    Return()

    # Function_3_5BE end

    def Function_4_5E2(): pass

    label("Function_4_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_605")
    OP_8D(0xFE, -9410, 54290, -4840, 47630, 2000)
    Jump("Function_4_5E2")

    label("loc_605")

    Return()

    # Function_4_5E2 end

    def Function_5_606(): pass

    label("Function_5_606")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -4320, 30420, 16309, 38200, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_753")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x10E0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x76D4), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x3FB5), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x9538), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ED")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_6DA():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DA)
    Jump("loc_710")

    label("loc_6ED")


    def lambda_6F3():
        OP_8D(0xFE, -4320, 30420, 16309, 38200, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F3)
    Sleep(200)

    label("loc_710")

    Sleep(30)
    Jump("loc_750")

    label("loc_718")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_750")
    OP_44(0xFE, 0x2)

    def lambda_738():
        OP_8D(0xFE, -4320, 30420, 16309, 38200, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_738)

    label("loc_750")

    Jump("loc_62F")

    label("loc_753")

    Return()

    # Function_5_606 end

    def Function_6_754(): pass

    label("Function_6_754")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -780, 24910, 8900, 46240, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A1")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_866")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x30C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x614E), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x22C4), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xB4A0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83B")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_828():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_828)
    Jump("loc_85E")

    label("loc_83B")


    def lambda_841():
        OP_8D(0xFE, -780, 24910, 8900, 46240, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_841)
    Sleep(200)

    label("loc_85E")

    Sleep(30)
    Jump("loc_89E")

    label("loc_866")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E")
    OP_44(0xFE, 0x2)

    def lambda_886():
        OP_8D(0xFE, -780, 24910, 8900, 46240, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_886)

    label("loc_89E")

    Jump("loc_77D")

    label("loc_8A1")

    Return()

    # Function_6_754 end

    def Function_7_8A2(): pass

    label("Function_7_8A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    OP_43(0xFE, 0x2, 0x0, 0x8)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_92D")
    TalkBegin(0xFE)
    OP_A2(0xA)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "新鲜鸡蛋\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_92D")

    Return()

    # Function_7_8A2 end

    def Function_8_92E(): pass

    label("Function_8_92E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_949")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_8_92E")

    label("loc_949")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_92E end

    def Function_9_954(): pass

    label("Function_9_954")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_992")

    ChrTalk(
        0xFE,
        (
            "那我就由衷地\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是期待啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_119F")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9C6")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_A93")

    label("loc_9C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2C")
    OP_A2(0x3)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……哦哦，菲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "原……原谅……\x01",
            "……我……………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_A93")

    label("loc_A2C")

    OP_A2(0x3)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……哦哦，菲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我太高兴了……\x01",
            "……明白……我的心意……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)

    label("loc_A93")

    Jump("loc_119F")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_B14")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "菲已经读了我的信吧…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……总、总觉得\x01",
            "紧张得脖子都快僵硬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼啊啊～啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DCA")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_B8F")

    ChrTalk(
        0xFE,
        (
            "一想再过不久， \x01",
            "菲就要看我的信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就、就紧张得\x01",
            "脖子都要僵硬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼啊啊～啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DCA")

    label("loc_B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_D0C")

    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎、怎么样？\x01",
            "信、信送到了没有？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x80)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C25")

    ChrTalk(
        0x101,
        (
            "#001F嗯，送到了哦。\x02\x03",
            "当然啦，还有礼物。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3D")

    label("loc_C25")


    ChrTalk(
        0x101,
        "#001F嗯，送到了哦。\x02",
    )

    CloseMessageWindow()

    label("loc_C3D")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是、是吗。\x01",
            "谢谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那、那么\x01",
            "她现在应该在看了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……为、为什么\x01",
            "感觉这么紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x591)
    Jump("loc_D09")

    label("loc_CB5")


    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "还没有送去呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "呼，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_D09")

    Jump("loc_DCA")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(
        0xFE,
        "呼，还是困啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天也早点睡吧。\x01",
            "呼啊啊啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCA")

    label("loc_D60")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "唔，好奇怪啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总觉得\x01",
            "刚才周围一直很乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "正好把我给吵醒了。\x02",
    )

    CloseMessageWindow()

    label("loc_DCA")

    Jump("loc_119F")

    label("loc_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_E08")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "ＺＺＺ～……ＺＺＺ～……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_119F")

    label("loc_E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E65")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯、嗯嗯～嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "菲……\x01",
            "对……不起……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_119F")

    label("loc_E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_110C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_EFB")

    ChrTalk(
        0xFE,
        (
            "现在菲说不定\x01",
            "正在看我的信呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……总、总觉得\x01",
            "紧张得脖子都快僵硬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼啊啊～啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1003")

    label("loc_EFB")

    OP_A2(0x3)
    OP_A2(0x591)

    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎、怎么样？\x01",
            "信、信送到了没有？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x80)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(
        0x101,
        (
            "#001F嗯，送到了哦。\x02\x03",
            "当然啦，还有礼物。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9B")

    label("loc_F83")


    ChrTalk(
        0x101,
        "#001F嗯，送到了哦。\x02",
    )

    CloseMessageWindow()

    label("loc_F9B")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是、是吗。\x01",
            "谢谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那、那么\x01",
            "她现在应该在看了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……为、为什么\x01",
            "感觉这么紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1003")

    Jump("loc_1109")

    label("loc_1006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1081")

    ChrTalk(
        0xFE,
        (
            "一想再过不久， \x01",
            "菲就要看我的信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就、就紧张得\x01",
            "脖子都要僵硬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼啊啊～啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1109")

    label("loc_1081")


    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎、怎么样？\x01",
            "信、信送到了没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "还没有送去呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "呼，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1109")

    Jump("loc_1110")

    label("loc_110C")

    Call(1, 2)

    label("loc_1110")

    Jump("loc_119F")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_119F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1147")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_119F")

    label("loc_1147")

    OP_A2(0x3)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有～……\x01",
            "……异常…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)

    label("loc_119F")

    TalkEnd(0xFE)
    Return()

    # Function_9_954 end

    def Function_10_11A3(): pass

    label("Function_10_11A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_12BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1217")

    ChrTalk(
        0xFE,
        (
            "……哈，\x01",
            "你们可别理旁边那家伙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个家伙\x01",
            "可是这个守备队的大笑料呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BD")

    label("loc_1217")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "现在正在进行盘查。\x01",
            "因为蔡斯出了事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在的出入境检查\x01",
            "比平时更加严格哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BD")

    TalkEnd(0xFE)
    Return()

    # Function_10_11A3 end

    def Function_11_12C1(): pass

    label("Function_11_12C1")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_12C1 end

    def Function_12_12C8(): pass

    label("Function_12_12C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1357")

    ChrTalk(
        0xFE,
        (
            "还是没有找到\x01",
            "袭击工房犯人的下落。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "事到如今，\x01",
            "下令再次盘查根本就没有意义了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1411")

    label("loc_1357")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "那些工房袭击犯\x01",
            "一点下落也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也是理所当然的结果吧。\x01",
            "因为盘查被解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许那些犯人\x01",
            "早已经逃亡到国外去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1411")

    Jump("loc_1908")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_15D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_14D4")

    ChrTalk(
        0xFE,
        (
            "现在，\x01",
            "这个沃尔费堡垒也实行了严格的盘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在事件的真相明了之前\x01",
            "这个态势还将维持下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D1")

    label("loc_14D4")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "之前收到了紧急的联络。\x01",
            "现在这个堡垒也进入了警戒状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从已知的线索来判断，\x01",
            "蔡斯事件应该是训练有素的犯罪者所为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……说不定，\x01",
            "也有可能是来自他国的不速之客所为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D1")

    Jump("loc_1908")

    label("loc_15D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_178E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_16B5")

    ChrTalk(
        0xFE,
        (
            "如果情势有变化，\x01",
            "现在与我们保持和平的共和国\x01",
            "可能也会对我们虎视眈眈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对他们来说，\x01",
            "王国的七耀石资源非常诱人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以我认为守卫国境\x01",
            "是非常重要的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178B")

    label("loc_16B5")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "乍一看，卡尔瓦德共和国\x01",
            "好像是利贝尔的友好的盟国……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实站在他们的角度来看，\x01",
            "是因为有埃雷波尼亚帝国在\x01",
            "他们才愿意和王国合作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "也就是所谓的『敌人的敌人就是朋友』。\x02",
    )

    CloseMessageWindow()

    label("loc_178B")

    Jump("loc_1908")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1842")

    ChrTalk(
        0xFE,
        (
            "有人打瞌睡有人偷懒……\x01",
            "这里的守备队还真是过分啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个样子下去\x01",
            "万一发生什么事情怎么应对得了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少我自己要\x01",
            "尽职地完成本分工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_1842")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "这里的守备队还真是过分啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有人打瞌睡有人偷懒……\x01",
            "士兵们随心所欲，\x01",
            "队长也都装没看见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，至少我自己要\x01",
            "尽职地完成本分工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1908")

    TalkEnd(0xFE)
    Return()

    # Function_12_12C8 end

    def Function_13_190C(): pass

    label("Function_13_190C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_190C end

    def Function_14_1913(): pass

    label("Function_14_1913")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 0)), scpexpr(EXPR_END)), "loc_19FB")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "怎么会突然要检查啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能在交接货物\x01",
            "完成之后进行就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "商品要是不能\x01",
            "运到共和国那边，\x01",
            "我不就白来了一趟吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7A")

    label("loc_19FB")


    ChrTalk(
        0xFE,
        (
            "好像因为在蔡斯发生了事件，\x01",
            "这里开始对过往行人进行盘查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "我还是等会儿就回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前，\x01",
            "就用看书来打发时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……你们几位也想看书吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不介意的话，\x01",
            "我可以把看完的书送给你们哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5D0)
    OP_3E(0x218, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第７卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "这本小说很有意思的，\x01",
            "推荐给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7A")

    Jump("loc_2237")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_209A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C14")

    ChrTalk(
        0xFE,
        "还是要三思而后行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然雇游击士要花点钱，\x01",
            "不过万一死了就什么也没有了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D01")

    label("loc_1C14")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀……\x01",
            "这次的工作真是倒霉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从蔡斯来这里的途中，\x01",
            "搬运车在托兰特平原\x01",
            "正中央发生了故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "担任护卫的游击士\x01",
            "回去拿来了替换的零件，\x01",
            "总算是得救了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……如果只有我自己，\x01",
            "也许就糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D01")

    Jump("loc_2097")

    label("loc_1D04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D8A")

    ChrTalk(
        0xFE,
        (
            "下次有工作的话，\x01",
            "一定要再带那位\x01",
            "游击士兄弟一起去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他真是个热心工作的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EAB")

    label("loc_1D8A")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上次发生危险的时候\x01",
            "真是多亏了你们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，叔叔。\x02\x03",
            "你没事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "后来那个游击士兄弟\x01",
            "回城里取来了零件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏了他，\x01",
            "我才能平安地到这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "游击士果然值得信赖啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们也辛苦了。\x01",
            "路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAB")

    Jump("loc_2097")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F22")

    ChrTalk(
        0xFE,
        (
            "下次有工作的话，\x01",
            "一定要再带那位\x01",
            "游击士兄弟一起去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他真是个热心工作的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2097")

    label("loc_1F22")

    OP_A2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF3")

    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "这段时间多亏你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么了？\x01",
            "亚尔摩那里的工作完成了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，完成了。\x01",
            "我们正准备回去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么你们多保重。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2097")

    label("loc_1FF3")


    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "亚尔摩那里的工作完成了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这边\x01",
            "总算也交接完货物了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望你们回去的路上\x01",
            "也能够轻松愉快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2097")

    Jump("loc_2237")

    label("loc_209A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_2107")

    ChrTalk(
        0xFE,
        (
            "呼，之后只要等着领取\x01",
            "从共和国运来的货物就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "趁现在好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_2107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_21B1")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "这段时间多亏你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还要在这里\x01",
            "等待共和国那边\x01",
            "送过来的货物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "趁现在好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_21B1")

    OP_A2(0x2)
    OP_A2(0x580)

    ChrTalk(
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么了？\x01",
            "你们不是去亚尔摩吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯。\x01",
            "我们正准备去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么你们多保重。\x02",
    )

    CloseMessageWindow()

    label("loc_2237")

    TalkEnd(0xFE)
    Return()

    # Function_14_1913 end

    def Function_15_223B(): pass

    label("Function_15_223B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_23D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22C8")

    ChrTalk(
        0xFE,
        (
            "担任我的护卫的\x01",
            "那个叫王的游击士\x01",
            "好像是个东方人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "共和国的人\x01",
            "如果都像他这样亲切就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D4")

    label("loc_22C8")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "因为蔡斯事件的调查，\x01",
            "游击士们都很忙，\x01",
            "我想委托可能会被推辞吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过出乎意料的是\x01",
            "委托被接受了。\x01",
            "真是让我吃了一惊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种时候\x01",
            "竟然也能接受\x01",
            "我这样的委托啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士协会\x01",
            "果然很伟大啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D4")

    TalkEnd(0xFE)
    Return()

    # Function_15_223B end

    def Function_16_23D8(): pass

    label("Function_16_23D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_281A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_245B")

    ChrTalk(
        0xFE,
        (
            "现在我能做的事\x01",
            "就是尽心尽责地\x01",
            "完成分配下来的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我相信这是给予\x01",
            "调查活动的最好支持。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2817")

    label("loc_245B")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_2663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24CC")

    ChrTalk(
        0xFE,
        (
            "现在冈多夫先生\x01",
            "也不在蔡斯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们的事\x01",
            "就交给我来照顾吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "互相加油吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2660")

    label("loc_24CC")


    ChrTalk(
        0xFE,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "调查得怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～马马虎虎啦。\x02\x03",
            "王先生你这边呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔡斯事件之后， \x01",
            "雾香接到了一大堆的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此我连\x01",
            "轻松一下的空闲也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也打算用自己的方式\x01",
            "来协助你们的调查啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "不能再耽误你们的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，我们互相加油吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，你就放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F王先生也要保重啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2660")

    Jump("loc_2817")

    label("loc_2663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26E7")

    ChrTalk(
        0xFE,
        (
            "现在冈多夫先生也不在，\x01",
            "我要更加努力才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "稍微休息会儿就开始下一个工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2817")

    label("loc_26E7")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "竟然袭击中央工房，\x01",
            "实在是无法无天呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔡斯事件之后， \x01",
            "雾香接到了一大堆的工作。\x01",
            "因此我连放松的空闲都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在我能做的事\x01",
            "就是尽心尽责地\x01",
            "完成分配下来的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也打算用自己的方式\x01",
            "来协助你们的调查啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2817")

    Jump("loc_2899")

    label("loc_281A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2899")

    ChrTalk(
        0xFE,
        (
            "啊，是你们。\x01",
            "谢谢，刚才你们帮了大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们能到堡垒来\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2899")

    TalkEnd(0xFE)
    Return()

    # Function_16_23D8 end

    def Function_17_289D(): pass

    label("Function_17_289D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　卡尔瓦德共和国\x01",
            "西　蔡斯市　２８０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_289D end

    SaveToFile()

Try(main)
