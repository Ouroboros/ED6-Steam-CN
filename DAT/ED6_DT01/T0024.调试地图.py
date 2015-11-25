from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0024   ._SN',
        MapName             = 'map24',
        Location            = 'map.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        Unknown_00              = -14000,
        Unknown_04              = 0,
        Unknown_08              = -11000,
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

    DeclEntryPoint(
        Unknown_00              = 10900,
        Unknown_04              = -200,
        Unknown_08              = -14400,
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
        Unknown_30              = 180,
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

    DeclEntryPoint(
        Unknown_00              = 11000,
        Unknown_04              = -200,
        Unknown_08              = -21400,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
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

    DeclEntryPoint(
        Unknown_00              = 7000,
        Unknown_04              = -200,
        Unknown_08              = -18000,
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
        Unknown_30              = 270,
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

    DeclEntryPoint(
        Unknown_00              = 11000,
        Unknown_04              = 0,
        Unknown_08              = 53000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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

    DeclEntryPoint(
        Unknown_00              = -29300,
        Unknown_04              = -100,
        Unknown_08              = -26000,
        Unknown_0C              = 4,
        Unknown_0E              = 45,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 270,
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


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_1FF",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_218",          # 03, 3
        "Function_4_230",          # 04, 4
        "Function_5_248",          # 05, 5
        "Function_6_260",          # 06, 6
        "Function_7_278",          # 07, 7
        "Function_8_290",          # 08, 8
        "Function_9_29A",          # 09, 9
        "Function_10_2A4",         # 0A, 10
        "Function_11_2AE",         # 0B, 11
        "Function_12_2BA",         # 0C, 12
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Return()

    # Function_0_1FE end

    def Function_1_1FF(): pass

    label("Function_1_1FF")

    Return()

    # Function_1_1FF end

    def Function_2_200(): pass

    label("Function_2_200")

    Fade(500)
    SetChrPos(0x0, -13500, 0, 47000, 270)
    OP_0D()
    Return()

    # Function_2_200 end

    def Function_3_218(): pass

    label("Function_3_218")

    Fade(500)
    SetChrPos(0x0, 53000, 0, 50200, 90)
    OP_0D()
    Return()

    # Function_3_218 end

    def Function_4_230(): pass

    label("Function_4_230")

    Fade(500)
    SetChrPos(0x0, 12000, -250, 45600, 0)
    OP_0D()
    Return()

    # Function_4_230 end

    def Function_5_248(): pass

    label("Function_5_248")

    Fade(500)
    SetChrPos(0x0, -18000, 2850, 46600, 0)
    OP_0D()
    Return()

    # Function_5_248 end

    def Function_6_260(): pass

    label("Function_6_260")

    Fade(500)
    SetChrPos(0x0, 52000, 5000, 50500, 7)
    OP_0D()
    Return()

    # Function_6_260 end

    def Function_7_278(): pass

    label("Function_7_278")

    Fade(500)
    SetChrPos(0x0, 17000, 0, 47000, 0)
    OP_0D()
    Return()

    # Function_7_278 end

    def Function_8_290(): pass

    label("Function_8_290")

    NewScene("ED6_DT01/T0100   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_8_290 end

    def Function_9_29A(): pass

    label("Function_9_29A")

    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_9_29A end

    def Function_10_2A4(): pass

    label("Function_10_2A4")

    NewScene("ED6_DT01/T0100   ._SN", 3, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2A4 end

    def Function_11_2AE(): pass

    label("Function_11_2AE")

    EventBegin(0x0)
    NewScene("ED6_DT01/T0020   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2AE end

    def Function_12_2BA(): pass

    label("Function_12_2BA")

    EventBegin(0x0)
    NewScene("ED6_DT01/T0022   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2BA end

    SaveToFile()

Try(main)
