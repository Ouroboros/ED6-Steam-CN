from ED6ScenarioHelper import *

def main():
    # 钢壁之路

    CreateScenaFile(
        FileName            = 'R1301   ._SN',
        MapName             = 'Bose',
        Location            = 'R1301.x',
        MapIndex            = 57,
        MapDefaultBGM       = "ed60022",
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
        '东柏斯街道方向',                       # 9
        '哈肯大门方向',                         # 10
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
        Unknown_3A              = 57,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10370 ._CH',             # 00
        'ED6_DT09/CH10371 ._CH',             # 01
        'ED6_DT09/CH10360 ._CH',             # 02
        'ED6_DT09/CH10361 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10370P._CP',             # 00
        'ED6_DT09/CH10371P._CP',             # 01
        'ED6_DT09/CH10360P._CP',             # 02
        'ED6_DT09/CH10361P._CP',             # 03
    )

    DeclNpc(
        X                   = -204170,
        Z                   = 20,
        Y                   = 10080,
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

    DeclNpc(
        X                   = -222100,
        Z                   = 10,
        Y                   = 149520,
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


    DeclMonster(
        X                   = -215110,
        Z                   = 0,
        Y                   = 47900,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x109,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -212230,
        Z                   = 10,
        Y                   = 71070,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x10C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -214830,
        Z                   = -50,
        Y                   = 109950,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x10D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_15F",          # 01, 1
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Return()

    # Function_0_15E end

    def Function_1_15F(): pass

    label("Function_1_15F")

    OP_16(0x2, 0xFA0, 0xFFFACBF8, 0xFFFF63C0, 0x30014)
    Return()

    # Function_1_15F end

    SaveToFile()

Try(main)
