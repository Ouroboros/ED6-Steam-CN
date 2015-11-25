from ED6ScenarioHelper import *

def main():
    # 翡翠之塔

    CreateScenaFile(
        FileName            = 'C0401   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0401.x',
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
        '波波',                                 # 10
        '波波',                                 # 11
        '岩溶捕猎手',                           # 12
        '竹刀飞鱼',                             # 13
        '食人鲨',                               # 14
        '食人鲨',                               # 15
        '食人鲨',                               # 16
        '波波',                                 # 17
        '波波',                                 # 18
        '食人鲨',                               # 19
        '食人鲨',                               # 20
        '竹刀飞鱼',                             # 21
        '竹刀飞鱼',                             # 22
        '竹刀飞鱼',                             # 23
        '竹刀飞鱼',                             # 24
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
        X                   = 0,
        Z                   = 0,
        Y                   = 11000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8000,
        Z                   = 0,
        Y                   = 19000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8000,
        Z                   = 0,
        Y                   = 19000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = 27000,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 0,
        Z                   = 0,
        Y                   = 19000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x36,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8000,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20000,
        Z                   = 0,
        Y                   = 27000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19000,
        Z                   = 0,
        Y                   = 13000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 63000,
        Z                   = 0,
        Y                   = 7000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 55000,
        Z                   = 0,
        Y                   = 7000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 46000,
        Z                   = 0,
        Y                   = -10000,
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
        X                   = 73000,
        Z                   = 0,
        Y                   = -9000,
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
        X                   = 71000,
        Z                   = 0,
        Y                   = 7000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x36,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 47000,
        Z                   = 0,
        Y                   = 2000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x36,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 65000,
        Z                   = 0,
        Y                   = 18000,
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
        X                   = 52000,
        Z                   = 0,
        Y                   = 18000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 43000,
        Y                   = -200,
        Z                   = 11000,
        Range               = 45000,
        Unknown_10          = 0x708,
        Unknown_14          = 0x32C8,
        Unknown_18          = 0x10,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 43000,
        Y                   = -200,
        Z                   = 6000,
        Range               = 45000,
        Unknown_10          = 0x708,
        Unknown_14          = 0x1F40,
        Unknown_18          = 0x10,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = 72800,
        Y                   = -200,
        Z                   = 11000,
        Range               = 74800,
        Unknown_10          = 0x708,
        Unknown_14          = 0x32C8,
        Unknown_18          = 0x10,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 72800,
        Y                   = -200,
        Z                   = 1000,
        Range               = 74800,
        Unknown_10          = 0x708,
        Unknown_14          = 0xBB8,
        Unknown_18          = 0x10,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_32B",          # 01, 1
        "Function_2_32C",          # 02, 2
        "Function_3_334",          # 03, 3
        "Function_4_33C",          # 04, 4
        "Function_5_344",          # 05, 5
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Return()

    # Function_0_32A end

    def Function_1_32B(): pass

    label("Function_1_32B")

    Return()

    # Function_1_32B end

    def Function_2_32C(): pass

    label("Function_2_32C")

    OP_70(0x4, 0x3C)
    Return()

    # Function_2_32C end

    def Function_3_334(): pass

    label("Function_3_334")

    OP_70(0x5, 0x3C)
    Return()

    # Function_3_334 end

    def Function_4_33C(): pass

    label("Function_4_33C")

    OP_70(0x9, 0x3C)
    Return()

    # Function_4_33C end

    def Function_5_344(): pass

    label("Function_5_344")

    OP_70(0x7, 0x3C)
    Return()

    # Function_5_344 end

    SaveToFile()

Try(main)
