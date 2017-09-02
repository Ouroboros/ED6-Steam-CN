from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1401   ._SN',
        MapName             = 'Bose',
        Location            = 'T1401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '卫兵',                                 # 9
        '卫兵',                                 # 10
        '王国军士兵',                           # 11
        '王国军士兵',                           # 12
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = -12000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2400,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_149",          # 01, 1
        "Function_2_15C",          # 02, 2
        "Function_3_172",          # 03, 3
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_148")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_148")

    Return()

    # Function_0_13A end

    def Function_1_149(): pass

    label("Function_1_149")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFE0430, 0x30045)
    Return()

    # Function_1_149 end

    def Function_2_15C(): pass

    label("Function_2_15C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_171")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_15C")

    label("loc_171")

    Return()

    # Function_2_15C end

    def Function_3_172(): pass

    label("Function_3_172")

    EventBegin(0x0)
    OP_6D(180, -10, -36520, 0)
    OP_67(0, 15350, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(711, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    FadeToBright(2000, 0)

    def lambda_1CF():
        OP_6D(180, 0, -6800, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CF)

    def lambda_1E7():
        OP_67(0, 10940, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E7)

    def lambda_1FF():
        OP_6C(44000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FF)
    Sleep(5000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_172 end

    SaveToFile()

Try(main)
