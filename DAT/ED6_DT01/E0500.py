from ED6ScenarioHelper import *

def main():
    CreateScenaFile(
        FileName            = 'E0500   ._SN',
        MapName             = 'Event',
        Location            = 'E0500.x',
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
        "Function_1_BD",           # 01, 1
        "Function_2_BE",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x0, 0x0)
    Event(0, 2)
    Return()

    # Function_0_AA end

    def Function_1_BD(): pass

    label("Function_1_BD")

    Return()

    # Function_1_BD end

    def Function_2_BE(): pass

    label("Function_2_BE")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -33360, 29260, 37770, 155)
    SetMapFlags(0x1)
    OP_66(0x0)
    OP_22(0x79, 0x0, 0x64)
    OP_24(0x79, 0x46)
    OP_6D(-33360, 29260, 37770, 0)
    OP_67(-36960, 15020, -20740, 0)
    OP_6B(1730, 0)
    OP_6C(3000, 0)
    OP_6E(697, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 700)
    OP_70(0x0, 0x30C)
    FadeToBright(2000, 0)

    def lambda_15A():
        OP_8C(0xFE, 205, 10)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_15A)

    def lambda_168():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_168)
    Sleep(400)

    def lambda_188():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_188)
    Sleep(400)
    OP_24(0x79, 0x4B)

    def lambda_1AC():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1AC)
    Sleep(800)
    OP_24(0x79, 0x50)

    def lambda_1D0():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1D0)
    Sleep(800)
    OP_24(0x79, 0x55)

    def lambda_1F4():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1F4)
    Sleep(1100)
    OP_24(0x79, 0x5A)

    def lambda_218():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_218)
    Sleep(100)

    def lambda_238():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_238)
    Sleep(100)

    def lambda_258():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_258)
    Sleep(100)

    def lambda_278():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_278)
    Sleep(100)

    def lambda_298():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_298)

    def lambda_2B3():
        OP_8C(0xFE, 285, 10)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B3)
    Sleep(100)

    def lambda_2C6():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2C6)

    def lambda_2E1():
        OP_8C(0xFE, 285, 8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2E1)
    Sleep(100)

    def lambda_2F4():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2F4)

    def lambda_30F():
        OP_8C(0xFE, 285, 6)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_30F)
    Sleep(100)

    def lambda_322():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_322)

    def lambda_33D():
        OP_8C(0xFE, 285, 4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_33D)
    Sleep(100)

    def lambda_350():
        OP_8F(0x0, 0xFFFF9732, 0x724C, 0xFFFFE386, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_350)

    def lambda_36B():
        OP_8C(0xFE, 285, 2)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_36B)
    Sleep(100)

    def lambda_37E():
        OP_8C(0xFE, 285, 10)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37E)
    OP_44(0x0, 0x2)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1021)
    OP_70(0x0, 0x41A)
    OP_73(0x0)
    OP_6F(0x0, 1051)
    OP_70(0x0, 0x456)

    def lambda_3B4():
        OP_8C(0xFE, -19536, 1)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B4)
    OP_66(0x1)

    def lambda_3C5():
        OP_67(0, -7220, -17030, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3C5)

    def lambda_3DD():
        OP_6C(22000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3DD)
    OP_24(0x79, 0x64)

    def lambda_3F1():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3F1)
    Sleep(100)

    def lambda_411():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_411)
    Sleep(100)

    def lambda_431():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_431)
    Sleep(100)

    def lambda_451():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_451)
    Sleep(100)

    def lambda_471():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_471)
    Sleep(100)

    def lambda_491():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_491)
    Sleep(700)

    def lambda_4B1():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4B1)
    Sleep(800)

    def lambda_4D1():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4D1)
    Sleep(900)

    def lambda_4F1():
        OP_8F(0x0, 0xFFFF9732, 0xFFFF8DB4, 0xFFFFDF9E, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4F1)
    FadeToDark(2000, 0, -1)
    Sleep(1000)

    def lambda_51B():
        OP_8F(0x0, 0xFFFF9732, 0xFFFE0715, 0xFFFFDF9E, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_51B)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_BE end

    SaveToFile()

Try(main)
