from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2103   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2103.x',
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
        '戴尔蒙市长',                           # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
        ' ',                                    # 13
        ' ',                                    # 14
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
        'ED6_DT07/CH02410 ._CH',             # 00
        'ED6_DT06/CH20083 ._CH',             # 01
        'ED6_DT07/CH00005 ._CH',             # 02
        'ED6_DT07/CH00015 ._CH',             # 03
        'ED6_DT07/CH00045 ._CH',             # 04
        'ED6_DT07/CH00107 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
        'ED6_DT06/CH20083P._CP',             # 01
        'ED6_DT07/CH00005P._CP',             # 02
        'ED6_DT07/CH00015P._CP',             # 03
        'ED6_DT07/CH00045P._CP',             # 04
        'ED6_DT07/CH00107P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_1B9",          # 02, 2
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_1A2 end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    OP_22(0x1C4, 0x1, 0x64)
    Return()

    # Function_1_1B3 end

    def Function_2_1B9(): pass

    label("Function_2_1B9")

    EventBegin(0x0)
    OP_22(0xDA, 0x1, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x4, 0xA, 0, 50, 2700, 180, 0, 0, 2500, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x9, 0, 50, 2400, 180, 0, 0, 1600, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x9, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(27900, -2990, 4040, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(1410, 0)
    OP_6C(270000, 0)
    OP_6E(713, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x105, 4)
    OP_89(0x101, 6290, -2000, -10, 270)
    OP_89(0x102, 8650, -2000, -420, 270)
    OP_89(0x105, 7180, -2000, 320, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    OP_89(0x8, -180, -2000, 370, 270)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x20)
    OP_71(0x0, 0x40)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x20)
    OP_71(0x1, 0x40)
    OP_6F(0x1, 301)
    OP_70(0x1, 0x168)
    OP_A1(0xA, 0x0)
    OP_A1(0x9, 0x1)
    SetChrPos(0xA, 0, -2950, 0, 90)
    SetChrPos(0x9, 27900, -2990, 4040, 90)

    def lambda_3D6():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D6)

    def lambda_3F1():
        OP_6D(6770, -2990, 360, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F1)

    def lambda_409():
        OP_6C(225000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_409)
    Sleep(4600)

    def lambda_41E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_41E)
    Sleep(200)

    def lambda_43E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_43E)
    Sleep(180)

    def lambda_45E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_45E)
    Sleep(160)

    def lambda_47E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47E)
    Sleep(140)

    def lambda_49E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_49E)
    Sleep(120)

    def lambda_4BE():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BE)
    Sleep(100)

    def lambda_4DE():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4DE)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x101,
        "#508F好～了，终于追上了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F因为我们坐的是小型艇，\x01",
            "船体比较轻。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_573():
        OP_8C(0x8, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_573)

    def lambda_581():
        OP_6D(6770, -2990, 290, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_581)

    def lambda_599():
        OP_6C(122000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_599)
    Sleep(1000)
    SetChrChipByIndex(0x8, 1)

    def lambda_5B3():
        OP_8E(0x8, 0x64A, 0xFFFFF4F2, 0xB4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B3)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#666F呜……\x01",
            "真是缠人的家伙……\x02\x03",
            "#665F尝尝这个！\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp008_00.eff")
    SetChrChipByIndex(0x101, 65535)
    Sleep(100)
    SetChrChipByIndex(0x101, 6)
    Sleep(100)
    SetChrChipByIndex(0x101, 5)
    OP_22(0x7E, 0x1, 0x64)

    def lambda_638():

        label("loc_638")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_638")

    QueueWorkItem2(0x101, 0, lambda_638)
    SetChrPos(0xD, 9550, -1900, 1300, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)

    def lambda_691():
        OP_6D(10040, -2600, 1040, 1300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_691)

    def lambda_6A9():
        OP_6C(102000, 1300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A9)
    Sleep(250)
    SetChrPos(0xD, 9550, -1300, 1000, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(250)
    Sleep(300)
    SetChrPos(0xD, 9550, -1500, 1600, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(200)
    SetChrPos(0xD, 9550, -1900, 1300, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(300)

    def lambda_7A4():
        OP_6C(225000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A4)
    SetChrPos(0xD, 9550, -1300, 1000, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#005F#20A#3S喝啊！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    SetChrPos(0xD, 9550, -1500, 1600, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(700)

    def lambda_876():
        OP_6D(6660, -2990, 520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_876)
    OP_44(0x101, 0x0)
    OP_23(0x7E)
    OP_99(0x101, 0x0, 0x13, 0xBB8)
    Sleep(500)
    OP_99(0x101, 0x13, 0x8, 0xBB8)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 6)

    ChrTalk(
        0x8,
        "#668F什、什么！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿～\x01",
            "市长你太小看游击士了！\x02\x03",
            "#005F约修亚，\x01",
            "就这样从右边靠上去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_936():
        OP_94(0x1, 0xA, 0xB4, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_936)

    ChrTalk(
        0x102,
        (
            "#012F明白。\x02\x03",
            "#014F……咦？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_970():
        OP_6D(4890, -2990, 200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_970)
    OP_22(0x96, 0x0, 0x64)

    def lambda_98D():
        OP_94(0x1, 0x9, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_98D)
    Sleep(250)

    def lambda_9A8():
        OP_94(0x1, 0x9, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9A8)
    Sleep(250)
    OP_B0(0x0, 0x64)

    def lambda_9C7():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9C7)

    def lambda_9DD():
        OP_94(0x1, 0x9, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9DD)
    Sleep(200)

    def lambda_9F8():
        OP_94(0x1, 0x9, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9F8)

    def lambda_A0E():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A0E)
    Sleep(300)

    def lambda_A29():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A29)
    Sleep(200)

    def lambda_A44():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A44)
    Sleep(200)

    def lambda_A5F():
        OP_94(0x1, 0xA, 0xB4, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A5F)

    ChrTalk(
        0x101,
        "#580F怎、怎么忽然变快了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F这是……\x01",
            "从海岸吹来的海风！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F糟了，\x01",
            "这下帆船就大占优势了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0)

    ChrTalk(
        0x8,
        (
            "#667F哇哈哈！！\x01",
            "看来女神也向我这边微笑了啊！\x02\x03",
            "那么再见了，小丫头们！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BD9():
        OP_8C(0x8, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BD9)
    OP_B0(0x0, 0x1E)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 240)
    OP_70(0x0, 0x12C)

    def lambda_BFE():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BFE)
    Sleep(200)

    def lambda_C19():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C19)
    Sleep(300)

    def lambda_C34():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C34)
    Sleep(300)

    def lambda_C4F():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C4F)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)

    def lambda_C7B():
        OP_94(0x1, 0xA, 0xB4, 0x4E20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C7B)
    Sleep(300)

    def lambda_C96():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C96)
    Sleep(300)

    def lambda_CB1():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CB1)
    Sleep(300)

    def lambda_CCC():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CCC)
    Sleep(300)

    def lambda_CE7():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CE7)
    Sleep(300)

    def lambda_D02():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D02)

    ChrTalk(
        0x101,
        (
            "#005F开什么玩笑！\x01",
            "就只差那么一步了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这样下去恐怕只能\x01",
            "眼睁睁地看他远走高飞了……\x02\x03",
            "要是还有什么办法的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_DB3():
        OP_6D(11720, -2900, 1060, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB3)
    SetChrPos(0xB, 60000, 2950, 2000, 270)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0xB, 800)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0xB, 800)
    SetChrChipByIndex(0x105, 65535)
    TurnDirection(0x105, 0xB, 800)

    ChrTalk(
        0x101,
        "#580F什、什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F#1S……来了。\x02",
    )

    CloseMessageWindow()

    def lambda_E40():

        label("loc_E40")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_E40")

    QueueWorkItem2(0x101, 1, lambda_E40)

    def lambda_E51():

        label("loc_E51")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_E51")

    QueueWorkItem2(0x102, 1, lambda_E51)

    def lambda_E62():

        label("loc_E62")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_E62")

    QueueWorkItem2(0x105, 1, lambda_E62)
    OP_72(0x2, 0x4)
    OP_A1(0xB, 0x2)
    SetChrPos(0xB, 60000, 2950, 2000, 270)
    OP_22(0xDB, 0x0, 0x64)

    def lambda_E93():
        OP_94(0x1, 0xB, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E93)

    def lambda_EA9():
        OP_6B(2300, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EA9)
    Sleep(3000)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_24(0xDA, 0x5F)
    Sleep(200)
    OP_24(0xDA, 0x5A)
    Sleep(200)
    OP_24(0xDA, 0x55)
    Sleep(200)
    OP_24(0xDA, 0x50)
    Sleep(200)
    OP_24(0xDA, 0x4B)
    Sleep(200)
    OP_24(0xDA, 0x46)
    Sleep(200)
    OP_24(0xDA, 0x41)
    Sleep(200)
    OP_23(0xDA)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    FadeToBright(1000, 0)
    OP_6D(-33030, -2950, 110, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(315000, 0)
    OP_6E(710, 0)
    OP_82(0x3, 0x0)
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, -33030, -2950, 110, 90)
    OP_44(0xB, 0xFF)
    SetChrPos(0xB, 34720, 0, 18480, 270)
    SetChrPos(0xC, 34720, 30000, 18480, 270)
    OP_22(0xDA, 0x1, 0x64)
    OP_24(0xDA, 0x41)
    Sleep(100)
    OP_24(0xDA, 0x46)
    Sleep(100)
    OP_24(0xDA, 0x4B)
    Sleep(100)
    OP_24(0xDA, 0x50)
    Sleep(100)
    OP_24(0xDA, 0x55)
    Sleep(100)
    OP_24(0xDA, 0x5A)
    Sleep(100)
    OP_24(0xDA, 0x5F)
    Sleep(100)
    OP_24(0xDA, 0x64)
    OP_0D()
    OP_B0(0x3, 0x1E)
    OP_72(0x3, 0x4)
    OP_A1(0xC, 0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 900)
    OP_70(0x3, 0x514)
    OP_B0(0x3, 0x3C)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)

    ChrTalk(
        0x8,
        (
            "#664F呀，总算逃出来了。\x01",
            "不过从今往后该怎么办呢……\x02\x03",
            "果然，唯有在军队插手之前，\x01",
            "尽早逃到帝国去吧。\x02\x03",
            "#667F算了，只要稍微忍耐一阵，\x01",
            "『他』肯定会帮我想办法的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)
    OP_22(0x79, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x65)

    def lambda_10FD():

        label("loc_10FD")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_10FD")

    QueueWorkItem2(0x8, 1, lambda_10FD)
    SetChrPos(0xB, 28720, 0, 18000, 270)
    SetChrPos(0xC, 34720, 15000, 18000, 270)
    SetChrPos(0x9, 300000, 300000, 300000, 0)

    def lambda_1141():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1141)

    def lambda_115C():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_115C)

    def lambda_1177():
        OP_6D(-31420, -2990, 9180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1177)

    def lambda_118F():
        OP_67(0, 11900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_118F)

    def lambda_11A7():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11A7)

    def lambda_11B7():
        OP_6B(3210, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11B7)
    Sleep(2200)

    def lambda_11CC():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11CC)

    def lambda_11E7():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11E7)
    Sleep(300)

    def lambda_1207():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1207)

    def lambda_1222():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1222)
    Sleep(300)

    def lambda_1242():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1242)

    def lambda_125D():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_125D)
    Sleep(300)

    def lambda_127D():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_127D)

    def lambda_1298():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1298)
    Sleep(300)

    def lambda_12B8():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12B8)

    def lambda_12D3():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12D3)
    Sleep(300)

    def lambda_12F3():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12F3)

    def lambda_130E():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_130E)
    Sleep(300)

    def lambda_132E():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_132E)

    def lambda_1349():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1349)
    Sleep(300)

    def lambda_1369():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1369)

    def lambda_1384():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1384)
    Sleep(300)

    def lambda_13A4():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13A4)

    def lambda_13BF():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13BF)
    Sleep(300)

    def lambda_13DF():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13DF)

    def lambda_13FA():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13FA)
    Sleep(300)

    def lambda_141A():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_141A)

    def lambda_1435():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1435)
    Sleep(300)

    def lambda_1455():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1455)

    def lambda_1470():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1470)

    ChrTalk(
        0x8,
        "#668F#3S什、什、什么————！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_14C0():
        OP_6D(-39220, -2900, 9180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14C0)

    def lambda_14D8():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14D8)

    def lambda_14F3():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14F3)
    Sleep(300)

    def lambda_1513():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1513)

    def lambda_152E():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_152E)
    OP_72(0x3, 0x20)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1300)
    OP_70(0x3, 0x604)
    Sleep(300)

    def lambda_1565():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1565)

    def lambda_1580():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1580)
    Sleep(300)

    def lambda_15A0():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15A0)

    def lambda_15BB():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_15BB)
    Sleep(300)

    def lambda_15DB():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15DB)

    def lambda_15F6():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_15F6)
    WaitChrThread(0xC, 0x1)

    def lambda_1616():
        OP_67(0, 7250, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1616)

    def lambda_162E():
        OP_6D(-35670, 4660, 3490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_162E)

    def lambda_1646():
        OP_6C(179000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1646)

    def lambda_1656():
        OP_8C(0xFE, 180, 2)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1656)

    def lambda_1664():
        OP_8C(0xFE, 180, 2)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1664)

    def lambda_1672():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1672)

    def lambda_168E():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_168E)

    def lambda_16AA():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16AA)
    Sleep(150)

    def lambda_16C5():
        OP_8C(0xFE, 180, 7)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_16C5)

    def lambda_16D3():
        OP_8C(0xFE, 180, 7)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_16D3)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1540)
    OP_70(0x3, 0x640)
    Sleep(150)

    def lambda_16F8():
        OP_8C(0xFE, 180, 11)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_16F8)

    def lambda_1706():
        OP_8C(0xFE, 180, 11)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1706)

    def lambda_1714():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1714)

    def lambda_1730():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1730)

    def lambda_174C():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_174C)
    Sleep(200)

    def lambda_1767():
        OP_8C(0xFE, 180, 16)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1767)

    def lambda_1775():
        OP_8C(0xFE, 180, 16)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1775)
    Sleep(200)

    def lambda_1788():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1788)

    def lambda_1796():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1796)

    def lambda_17A4():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17A4)

    def lambda_17C0():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17C0)

    def lambda_17DC():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17DC)
    Sleep(400)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 1595)
    OP_70(0x3, 0x640)

    def lambda_180A():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_180A)

    def lambda_1818():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1818)

    def lambda_1826():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1826)

    def lambda_1842():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1842)

    def lambda_185E():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_185E)
    Sleep(400)

    def lambda_1879():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1879)

    def lambda_1887():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1887)

    def lambda_1895():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1895)

    def lambda_18B1():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18B1)

    def lambda_18CD():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18CD)
    Sleep(400)

    def lambda_18E8():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18E8)

    def lambda_18F6():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_18F6)

    def lambda_1904():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1904)

    def lambda_1920():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1920)

    def lambda_193C():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_193C)
    Sleep(400)

    def lambda_1957():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1957)

    def lambda_1965():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1965)

    def lambda_1973():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1973)

    def lambda_198F():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_198F)

    def lambda_19AB():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19AB)
    Sleep(400)

    def lambda_19C6():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_19C6)

    def lambda_19D4():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_19D4)

    def lambda_19E2():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19E2)

    def lambda_19FE():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19FE)

    def lambda_1A1A():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A1A)
    Sleep(300)

    def lambda_1A35():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A35)

    def lambda_1A43():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1A43)

    def lambda_1A51():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A51)

    def lambda_1A6D():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A6D)

    def lambda_1A89():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A89)
    Sleep(200)

    def lambda_1AA4():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1AA4)

    def lambda_1AB2():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1AB2)

    def lambda_1AC0():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AC0)

    def lambda_1ADC():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1ADC)

    def lambda_1AF8():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1AF8)
    Sleep(100)

    def lambda_1B13():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B13)

    def lambda_1B21():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1B21)

    def lambda_1B2F():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B2F)

    def lambda_1B4B():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1B4B)

    def lambda_1B67():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B67)
    Sleep(100)

    def lambda_1B82():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B82)

    def lambda_1B9E():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1B9E)

    def lambda_1BBA():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BBA)
    Sleep(100)

    def lambda_1BD5():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1BD5)

    def lambda_1BF1():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1BF1)
    Sleep(200)
    OP_44(0xC, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 1600)
    OP_70(0x3, 0x686)

    ChrTalk(
        0x8,
        "#668F#10A#5P什、什、什……\x05\x02",
    )


    def lambda_1C4E():
        OP_6D(46000, -2990, -4059, 8100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C4E)

    def lambda_1C66():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1C66)

    def lambda_1C81():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1C81)

    def lambda_1C9C():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1C9C)
    Sleep(200)

    def lambda_1CBC():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1CBC)

    def lambda_1CD7():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1CD7)

    def lambda_1CF2():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1CF2)
    Sleep(200)

    def lambda_1D12():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1D12)

    def lambda_1D2D():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1D2D)

    def lambda_1D48():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1D48)
    Sleep(200)

    def lambda_1D68():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1D68)

    def lambda_1D83():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1D83)

    def lambda_1D9E():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1D9E)
    Sleep(200)

    def lambda_1DBE():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1DBE)

    def lambda_1DD9():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1DD9)

    def lambda_1DF4():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1DF4)
    Sleep(200)

    def lambda_1E14():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1E14)

    def lambda_1E2F():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1E2F)

    def lambda_1E4A():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1E4A)
    Sleep(200)

    def lambda_1E6A():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xE95, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1E6A)

    def lambda_1E85():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1E85)

    def lambda_1EA0():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1EA0)
    Sleep(200)

    def lambda_1EC0():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1EC0)

    def lambda_1EDB():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1EDB)

    def lambda_1EF6():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1EF6)
    Sleep(200)

    def lambda_1F16():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1F16)

    def lambda_1F31():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1F31)
    Sleep(200)

    def lambda_1F51():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1F51)

    def lambda_1F6C():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1F6C)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1670)
    OP_70(0x3, 0x708)

    def lambda_1F99():
        OP_8C(0xFE, 180, 33)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F99)
    OP_82(0x4, 0x2)
    PlayEffect(0x4, 0x5, 0xA, 0, 0, 2300, 180, 0, 0, 2000, 100, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        "#668F#10A#5P呜哇啊啊啊啊！！\x05\x02",
    )

    OP_B0(0x0, 0xC8)
    OP_23(0xDA)
    OP_23(0xDC)
    OP_22(0xDC, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mpsibuk.eff")
    PlayEffect(0x0, 0xFF, 0xC, 3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x12C, 0x1388, 0x7D0)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    Sleep(500)

    def lambda_25A3():
        OP_91(0xFE, 0x493E0, 0xFFFF8AD0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_25A3)

    def lambda_25BE():
        OP_91(0xFE, 0x493E0, 0xFFFF8AD0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_25BE)

    def lambda_25D9():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4C2C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_25D9)
    Sleep(150)

    def lambda_25F9():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_25F9)
    Sleep(150)

    def lambda_2619():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2619)
    Sleep(150)

    def lambda_2639():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2639)
    Sleep(150)

    def lambda_2659():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2659)
    Sleep(150)

    def lambda_2679():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2679)
    Sleep(150)

    def lambda_2699():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2699)
    Sleep(900)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2104   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1B9 end

    SaveToFile()

Try(main)
