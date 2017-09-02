from ED6ScenarioHelper import *

def main():
    # 废坑

    CreateScenaFile(
        FileName            = 'C1100   ._SN',
        MapName             = 'Bose',
        Location            = 'C1100.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
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
        Unknown_3A              = 49,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10300 ._CH',             # 00
        'ED6_DT09/CH10301 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT09/CH10300P._CP',             # 00
        'ED6_DT09/CH10301P._CP',             # 01
    )

    DeclMonster(
        X                   = 10830,
        Z                   = 0,
        Y                   = 17110,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x141,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 27540,
        Z                   = -500,
        Y                   = 33890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x141,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 46190,
        Z                   = 0,
        Y                   = 40810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x142,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 55780,
        Z                   = 0,
        Y                   = 26100,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x142,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 45070,
        Z                   = 210,
        Y                   = 9140,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x143,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -26630,
        Z                   = 0,
        Y                   = 11550,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x143,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32840,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x144,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28410,
        Z                   = -500,
        Y                   = 39950,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x144,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -57320,
        Z                   = 0,
        Y                   = 91000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x141,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -56950,
        Z                   = 0,
        Y                   = 108360,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x141,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -74060,
        Z                   = 0,
        Y                   = 64700,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x142,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -65650,
        Z                   = 0,
        Y                   = 65720,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x142,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -85050,
        Z                   = -30,
        Y                   = 75860,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x143,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -64209,
        Z                   = -480,
        Y                   = 36130,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x143,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -77410,
        Z                   = 0,
        Y                   = 32780,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x144,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14140,
        Z                   = 0,
        Y                   = 75360,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x141,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33060,
        Z                   = 0,
        Y                   = 75850,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x142,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 49560,
        Z                   = -500,
        Y                   = 62350,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x143,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 47230,
        Z                   = -500,
        Y                   = 56070,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x144,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_2CE",          # 00, 0
        "Function_1_2CF",          # 01, 1
    )


    def Function_0_2CE(): pass

    label("Function_0_2CE")

    Return()

    # Function_0_2CE end

    def Function_1_2CF(): pass

    label("Function_1_2CF")

    Return()

    # Function_1_2CF end

    SaveToFile()

Try(main)
