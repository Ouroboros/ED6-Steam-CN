from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3106   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3106.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60092",
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
        '人',                                   # 9
        '人',                                   # 10
        '人',                                   # 11
        '人',                                   # 12
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
        'ED6_DT07/CH01200 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01200P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_152",          # 01, 1
        "Function_2_16F",          # 02, 2
        "Function_3_759",          # 03, 3
        "Function_4_7B7",          # 04, 4
        "Function_5_804",          # 05, 5
        "Function_6_864",          # 06, 6
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_14A end

    def Function_1_152(): pass

    label("Function_1_152")

    OP_6F(0xD, 40)
    OP_70(0xD, 0x0)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x28)
    Return()

    # Function_1_152 end

    def Function_2_16F(): pass

    label("Function_2_16F")

    EventBegin(0x0)
    OP_6D(42710, 0, 50480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(9130, 0)
    OP_6C(225000, 0)
    OP_6E(369, 0)
    FadeToBright(2000, 0)
    OP_6C(235000, 4000)
    Fade(1000)
    SetMapFlags(0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x0, 0x4)
    SetChrPos(0x0, 58530, 0, 24930, 0)
    OP_6D(58530, 0, 24930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(225000, 0)
    OP_6E(369, 0)
    OP_0D()
    Fade(2000)
    OP_71(0x2E, 0x4)
    OP_71(0x37, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xC, 0x2)
    OP_7B()
    OP_0D()

    def lambda_26E():
        OP_8E(0x0, 0xE5F6, 0x0, 0xDC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26E)
    OP_72(0x26, 0x4)
    Sleep(100)

    def lambda_293():
        OP_8E(0x0, 0xE5F6, 0x0, 0xDC82, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_293)
    OP_71(0x2F, 0x4)
    Sleep(100)

    def lambda_2B8():
        OP_8E(0x0, 0xE5F6, 0x0, 0xDC82, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B8)
    OP_72(0x3D, 0x4)
    Sleep(100)

    def lambda_2DD():
        OP_8E(0x0, 0xE5F6, 0x0, 0xDC82, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2DD)
    OP_71(0x8, 0x4)
    Sleep(200)

    def lambda_302():
        OP_8E(0x0, 0xE5F6, 0x0, 0xE678, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_302)
    OP_71(0x1E, 0x4)
    Sleep(200)
    OP_72(0x27, 0x4)
    Sleep(100)
    OP_71(0x30, 0x4)
    Sleep(100)
    OP_72(0x3A, 0x4)
    Sleep(100)
    OP_71(0x5, 0x4)
    Sleep(100)
    OP_71(0x1D, 0x4)
    Sleep(200)
    OP_71(0x1C, 0x4)
    Sleep(200)
    OP_72(0x28, 0x4)
    Sleep(100)
    OP_71(0x31, 0x4)
    Sleep(100)
    OP_72(0x3F, 0x4)
    Sleep(100)
    OP_71(0xA, 0x4)
    Sleep(100)
    OP_71(0x1B, 0x4)
    Sleep(100)
    OP_71(0x1A, 0x4)
    Sleep(200)
    WaitChrThread(0x0, 0x1)
    Fade(1000)
    OP_6C(270000, 0)

    def lambda_3B2():
        OP_8E(0x0, 0x13BA, 0x0, 0xE6BE, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B2)
    Sleep(800)
    OP_72(0x29, 0x4)
    Sleep(100)
    OP_71(0x32, 0x4)
    Sleep(100)
    OP_71(0x19, 0x4)
    Sleep(200)
    OP_72(0x2A, 0x4)
    Sleep(100)
    OP_71(0x33, 0x4)
    Sleep(200)
    OP_72(0x2B, 0x4)
    Sleep(100)
    OP_71(0x34, 0x4)
    Sleep(100)
    OP_71(0x18, 0x4)
    Sleep(200)
    OP_72(0x2C, 0x4)
    Sleep(100)
    OP_71(0x35, 0x4)
    Sleep(100)
    OP_72(0x3E, 0x4)
    Sleep(100)
    OP_71(0x9, 0x4)
    Sleep(100)
    OP_71(0x17, 0x4)
    Sleep(200)
    OP_72(0x2D, 0x4)
    Sleep(100)
    OP_71(0x36, 0x4)
    Sleep(100)
    OP_72(0x2E, 0x4)
    Sleep(100)
    OP_71(0x39, 0x4)
    Sleep(100)
    OP_72(0x3B, 0x4)
    Sleep(100)
    OP_71(0x6, 0x4)
    Sleep(100)
    OP_72(0x3C, 0x4)
    Sleep(100)
    OP_71(0x7, 0x4)
    Sleep(100)
    OP_71(0x1F, 0x4)
    Sleep(200)
    OP_22(0x5B, 0x1, 0x64)
    OP_71(0x16, 0x4)
    Sleep(100)
    OP_71(0x15, 0x4)
    Sleep(200)
    OP_71(0x14, 0x4)
    Sleep(100)
    OP_71(0x13, 0x4)
    Sleep(200)

    def lambda_4DB():
        OP_8E(0x0, 0x13BA, 0x0, 0xE6BE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4DB)
    OP_71(0x12, 0x4)
    Sleep(100)

    def lambda_500():
        OP_8E(0x0, 0x13BA, 0x0, 0xE6BE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_500)
    OP_71(0x11, 0x4)
    Sleep(200)

    def lambda_525():
        OP_8E(0x0, 0x13BA, 0x0, 0xE6BE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_525)
    OP_71(0x10, 0x4)
    Sleep(100)

    def lambda_54A():
        OP_8E(0x0, 0x13BA, 0x0, 0xE6BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_54A)
    OP_71(0xF, 0x4)
    Sleep(200)

    def lambda_56F():
        OP_8E(0x0, 0x13BA, 0x0, 0xE6BE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_56F)
    Sleep(100)
    OP_44(0x0, 0x1)
    Sleep(500)
    OP_23(0x5B)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_72(0xD, 0x8)
    OP_72(0xB, 0x8)
    OP_6F(0xD, 0)
    OP_6F(0xB, 0)
    OP_70(0xD, 0x0)
    OP_70(0xB, 0x0)
    OP_72(0xD, 0x20)
    OP_72(0xB, 0x20)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x1)
    SetChrPos(0x8, 16280, 0, 62960, 309)
    SetChrPos(0x9, 17870, 0, 53190, 180)
    SetChrPos(0xA, 17870, 0, 53190, 180)
    SetChrPos(0xB, 36140, 500, 52730, 180)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_6D(31790, 0, 58850, 0)
    OP_67(0, 2430, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(264000, 0)
    OP_6E(369, 0)
    FadeToBright(1000, 0)

    def lambda_6C1():
        OP_6D(11640, 0, 59040, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6C1)

    def lambda_6D9():
        OP_6C(270000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6D9)
    OP_0D()
    Sleep(2000)
    OP_72(0x3E, 0x10)
    OP_70(0x3E, 0x64)
    Sleep(400)
    OP_43(0xB, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_72(0x3B, 0x10)
    OP_70(0x3B, 0x64)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_72(0x3C, 0x10)
    OP_70(0x3C, 0x64)
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0x5)
    Sleep(3000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_16F end

    def Function_3_759(): pass

    label("Function_3_759")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x3E12, 0x0, 0xEA38, 0xBB8, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 284, 400)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 96, 400)
    Return()

    # Function_3_759 end

    def Function_4_7B7(): pass

    label("Function_4_7B7")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x4682, 0x0, 0xD7DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3BB0, 0x0, 0xDCF0, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Return()

    # Function_4_7B7 end

    def Function_5_804(): pass

    label("Function_5_804")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x4682, 0x0, 0xD7DC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x45B0, 0x0, 0xDA7A, 0xBB8, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x9, 0xFE, 400)
    TurnDirection(0xFE, 0x9, 400)
    Return()

    # Function_5_804 end

    def Function_6_864(): pass

    label("Function_6_864")

    OP_8E(0xFE, 0x8C5A, 0x1F4, 0xD386, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x8DC2, 0x0, 0xD836, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 90, 270)
    Return()

    # Function_6_864 end

    SaveToFile()

Try(main)
