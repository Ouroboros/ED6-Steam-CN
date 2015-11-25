from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2403   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2403.x',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_D9",           # 01, 1
        "Function_2_EC",           # 02, 2
        "Function_3_16A",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_C1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 2)

    label("loc_C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_D8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 3)

    label("loc_D8")

    Return()

    # Function_0_AA end

    def Function_1_D9(): pass

    label("Function_1_D9")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x30067)
    Return()

    # Function_1_D9 end

    def Function_2_EC(): pass

    label("Function_2_EC")

    OP_79(0x0, 0x2)
    OP_7B()
    EventBegin(0x0)
    OP_6D(310, 0, -160, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_79(0x0, 0x2)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    FadeToBright(2000, 0)
    OP_6D(1900, 0, 36890, 10000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_EC end

    def Function_3_16A(): pass

    label("Function_3_16A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(3610, 0, 34400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    OP_22(0x87, 0x1, 0x50)
    LoadEffect(0x0, "map\\\\mpfire0.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 3450, 2000, 34330, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 3650, 1000, 33330, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_6C(351000, 4000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_16A end

    SaveToFile()

Try(main)
