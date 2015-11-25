from ED6ScenarioHelper import *

def main():
    # 翡翠之塔

    CreateScenaFile(
        FileName            = 'C0402   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0402.x',
        MapIndex            = 16,
        MapDefaultBGM       = "ed60033",
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
        '波波',                                 # 9
        '食人鲨',                               # 10
        '波波',                                 # 11
        '食人鲨',                               # 12
        '波波',                                 # 13
        '食人鲨',                               # 14
        '波波',                                 # 15
        '竹刀飞鱼',                             # 16
        '竹刀飞鱼',                             # 17
        '竹刀飞鱼',                             # 18
        '岩溶捕猎手',                           # 19
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
        Unknown_3A              = 16,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10150 ._CH',             # 02
        'ED6_DT09/CH10151 ._CH',             # 03
        'ED6_DT09/CH10040 ._CH',             # 04
        'ED6_DT09/CH10041 ._CH',             # 05
        'ED6_DT09/CH10190 ._CH',             # 06
        'ED6_DT09/CH10191 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10150P._CP',             # 02
        'ED6_DT09/CH10151P._CP',             # 03
        'ED6_DT09/CH10040P._CP',             # 04
        'ED6_DT09/CH10041P._CP',             # 05
        'ED6_DT09/CH10190P._CP',             # 06
        'ED6_DT09/CH10191P._CP',             # 07
    )

    DeclMonster(
        X                   = -51000,
        Z                   = 0,
        Y                   = 1000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42000,
        Z                   = 0,
        Y                   = 11000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42000,
        Z                   = 0,
        Y                   = 27000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -52000,
        Z                   = 0,
        Y                   = 37000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -68000,
        Z                   = 0,
        Y                   = 37000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78000,
        Z                   = 0,
        Y                   = 27000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x39,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78000,
        Z                   = 0,
        Y                   = 11000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -48000,
        Z                   = 0,
        Y                   = 19000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -59000,
        Z                   = 0,
        Y                   = 7000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x37,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -72000,
        Z                   = 0,
        Y                   = 19000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x37,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60000,
        Z                   = 0,
        Y                   = 19000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -46000,
        Y                   = -1000,
        Z                   = 5000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -58000,
        Y                   = -1000,
        Z                   = 3400,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -44200,
        Y                   = -1000,
        Z                   = 17000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -44200,
        Y                   = -1000,
        Z                   = 21000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -46000,
        Y                   = -1000,
        Z                   = 33000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -60000,
        Y                   = -1000,
        Z                   = 39000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = -62000,
        Y                   = -1000,
        Z                   = 34800,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -75800,
        Y                   = -1000,
        Z                   = 21000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -80000,
        Y                   = -1000,
        Z                   = 19000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = -68600,
        Y                   = -1000,
        Z                   = 10300,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -51300,
        Y                   = -1000,
        Z                   = 10300,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -68700,
        Y                   = -1000,
        Z                   = 27700,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -51500,
        Y                   = -1000,
        Z                   = 27700,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = -75800,
        Y                   = -1000,
        Z                   = 17000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -66000,
        Y                   = -1000,
        Z                   = 19000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -54000,
        Y                   = -1000,
        Z                   = 19000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -60000,
        Y                   = -1000,
        Z                   = 13000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -60000,
        Y                   = -1000,
        Z                   = 25000,
        Range               = 2000,
        Unknown_10          = 0x1F4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )


    DeclActor(
        TriggerX            = -54300,
        TriggerZ            = 800,
        TriggerY            = 33000,
        TriggerRange        = 1000,
        ActorX              = -54300,
        ActorZ              = 800,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_482",          # 00, 0
        "Function_1_488",          # 01, 1
        "Function_2_489",          # 02, 2
        "Function_3_5B9",          # 03, 3
        "Function_4_5F3",          # 04, 4
        "Function_5_622",          # 05, 5
        "Function_6_651",          # 06, 6
        "Function_7_680",          # 07, 7
        "Function_8_6AF",          # 08, 8
        "Function_9_6DE",          # 09, 9
        "Function_10_70D",         # 0A, 10
        "Function_11_73C",         # 0B, 11
        "Function_12_76F",         # 0C, 12
        "Function_13_79E",         # 0D, 13
        "Function_14_7CD",         # 0E, 14
        "Function_15_7FC",         # 0F, 15
        "Function_16_82B",         # 10, 16
        "Function_17_85A",         # 11, 17
        "Function_18_889",         # 12, 18
        "Function_19_8B8",         # 13, 19
        "Function_20_8E7",         # 14, 20
        "Function_21_916",         # 15, 21
    )


    def Function_0_482(): pass

    label("Function_0_482")

    OP_72(0x0, 0x10)
    Return()

    # Function_0_482 end

    def Function_1_488(): pass

    label("Function_1_488")

    Return()

    # Function_1_488 end

    def Function_2_489(): pass

    label("Function_2_489")

    OP_75(0x1, 0x0, 0x0)
    OP_75(0x2, 0x0, 0x0)
    OP_75(0x3, 0x0, 0x0)
    OP_75(0x4, 0x0, 0x0)
    OP_75(0x5, 0x0, 0x0)
    OP_75(0x6, 0x0, 0x0)
    OP_75(0x7, 0x0, 0x0)
    OP_75(0x8, 0x0, 0x0)
    OP_75(0x9, 0x0, 0x0)
    OP_75(0xA, 0x0, 0x0)
    OP_75(0xB, 0x0, 0x0)
    OP_75(0xC, 0x0, 0x0)
    OP_75(0xD, 0x0, 0x0)
    OP_75(0xE, 0x0, 0x0)
    OP_75(0xF, 0x0, 0x0)
    OP_75(0x10, 0x0, 0x0)
    OP_75(0x11, 0x0, 0x0)
    OP_75(0x12, 0x0, 0x0)
    OP_75(0x13, 0x0, 0x0)
    OP_75(0x14, 0x0, 0x0)
    OP_75(0x15, 0x0, 0x0)
    OP_75(0x16, 0x0, 0x0)
    OP_75(0x17, 0x0, 0x0)
    OP_75(0x18, 0x0, 0x0)
    OP_75(0x19, 0x0, 0x0)
    OP_75(0x1A, 0x0, 0x0)
    OP_75(0x1B, 0x0, 0x0)
    OP_75(0x1C, 0x0, 0x0)
    OP_75(0x1D, 0x0, 0x0)
    OP_75(0x1E, 0x0, 0x0)
    OP_75(0x1F, 0x0, 0x0)
    OP_75(0x20, 0x0, 0x0)
    OP_75(0x21, 0x0, 0x0)
    OP_75(0x22, 0x0, 0x0)
    OP_75(0x23, 0x0, 0x0)
    OP_75(0x24, 0x0, 0x0)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    OP_A3(0xA)
    OP_A3(0xB)
    OP_A3(0xC)
    OP_A3(0xD)
    OP_A3(0xE)
    OP_A3(0xF)
    OP_A3(0x10)
    OP_A3(0x11)
    Return()

    # Function_2_489 end

    def Function_3_5B9(): pass

    label("Function_3_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2")
    OP_76(0x1, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x22, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    OP_A2(0x0)

    label("loc_5F2")

    Return()

    # Function_3_5B9 end

    def Function_4_5F3(): pass

    label("Function_4_5F3")

    OP_76(0x2, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x23, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_4_5F3 end

    def Function_5_622(): pass

    label("Function_5_622")

    OP_76(0x3, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x21, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_5_622 end

    def Function_6_651(): pass

    label("Function_6_651")

    OP_76(0x4, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x20, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_6_651 end

    def Function_7_680(): pass

    label("Function_7_680")

    OP_76(0x5, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x1F, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_7_680 end

    def Function_8_6AF(): pass

    label("Function_8_6AF")

    OP_76(0x6, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x1E, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_8_6AF end

    def Function_9_6DE(): pass

    label("Function_9_6DE")

    OP_76(0x7, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x1D, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_9_6DE end

    def Function_10_70D(): pass

    label("Function_10_70D")

    OP_76(0x8, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x1B, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_10_70D end

    def Function_11_73C(): pass

    label("Function_11_73C")

    OP_76(0x9, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x1C, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Call(0, 21)
    Return()

    # Function_11_73C end

    def Function_12_76F(): pass

    label("Function_12_76F")

    OP_76(0xA, 0x0, 0x2, 0x8, 0x8, 0x64, 0x8, 0xF)
    OP_76(0x24, 0x0, 0x2, 0x4, 0x4, 0x64, 0x8, 0xF)
    Return()

    # Function_12_76F end

    def Function_13_79E(): pass

    label("Function_13_79E")

    OP_76(0xB, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x19, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_13_79E end

    def Function_14_7CD(): pass

    label("Function_14_7CD")

    OP_76(0xC, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x17, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_14_7CD end

    def Function_15_7FC(): pass

    label("Function_15_7FC")

    OP_76(0xD, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x18, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_15_7FC end

    def Function_16_82B(): pass

    label("Function_16_82B")

    OP_76(0xE, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x1A, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_16_82B end

    def Function_17_85A(): pass

    label("Function_17_85A")

    OP_76(0xF, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x16, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_17_85A end

    def Function_18_889(): pass

    label("Function_18_889")

    OP_76(0x10, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x14, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_18_889 end

    def Function_19_8B8(): pass

    label("Function_19_8B8")

    OP_76(0x11, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x13, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_19_8B8 end

    def Function_20_8E7(): pass

    label("Function_20_8E7")

    OP_76(0x12, 0x0, 0x2, 0x8, 0x8, 0x64, 0x0, 0x7)
    OP_76(0x15, 0x0, 0x2, 0x4, 0x4, 0x64, 0x0, 0x7)
    Return()

    # Function_20_8E7 end

    def Function_21_916(): pass

    label("Function_21_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_91E")
    Return()

    label("loc_91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_926")
    Return()

    label("loc_926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_92E")
    Return()

    label("loc_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_936")
    Return()

    label("loc_936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_93E")
    Return()

    label("loc_93E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_946")
    Return()

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_94E")
    Return()

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_956")
    Return()

    label("loc_956")

    Return()

    # Function_21_916 end

    SaveToFile()

Try(main)
