from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3114   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3114.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '阿加特',                               # 9
        '提妲',                                 # 10
        '拉赛尔博士',                           # 11
        '地图物体0',                            # 12
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
        'ED6_DT07/CH00050 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH02020 ._CH',             # 02
        'ED6_DT07/CH00005 ._CH',             # 03
        'ED6_DT07/CH00015 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00050P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH02020P._CP',             # 02
        'ED6_DT07/CH00005P._CP',             # 03
        'ED6_DT07/CH00015P._CP',             # 04
    )

    DeclNpc(
        X                   = 3380,
        Z                   = -1100,
        Y                   = 12290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2780,
        Z                   = -1100,
        Y                   = 12440,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2780,
        Z                   = -1100,
        Y                   = 11260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3000,
        Z                   = -1000,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x8,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 2680,
        Y                   = -1000,
        Z                   = 12450,
        Range               = 5000,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_186",          # 01, 1
        "Function_2_218",          # 02, 2
        "Function_3_452",          # 03, 3
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_185")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_185")

    Return()

    # Function_0_172 end

    def Function_1_186(): pass

    label("Function_1_186")


    def lambda_18C():

        label("loc_18C")

        TurnDirection(0xFE, 0x0, 0)
        OP_48()
        Jump("loc_18C")

    QueueWorkItem2(0x9, 2, lambda_18C)

    def lambda_19D():

        label("loc_19D")

        TurnDirection(0xFE, 0x0, 0)
        OP_48()
        Jump("loc_19D")

    QueueWorkItem2(0x8, 2, lambda_19D)

    def lambda_1AE():

        label("loc_1AE")

        TurnDirection(0xFE, 0x0, 0)
        OP_48()
        Jump("loc_1AE")

    QueueWorkItem2(0xA, 2, lambda_1AE)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x4)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    OP_89(0x9, 3380, 1000, 12290, 180)
    OP_89(0x8, 2780, 1000, 12440, 180)
    OP_89(0xA, 2780, 1000, 11260, 180)
    OP_A1(0xB, 0x0)
    OP_10(0x0, 0x0)
    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_186 end

    def Function_2_218(): pass

    label("Function_2_218")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(6310, 0, -12430, 0)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0xA, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x101, 8300, 1980, -14000, 270)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x102, 8300, 1980, -14000, 270)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x101,
        "艾丝蒂尔的声音",
        "#10A#3P#1S呜哇啊啊啊！？\x05\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearChrFlags(0x101, 0x80)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAD, 0x0, 0x64)
    OP_8F(0x101, 0x1612, 0x0, 0xFFFFC662, 0x32C8, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_96(0x101, 0x12C0, 0x0, 0xFFFFC4D2, 0x320, 0x1388)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    Sleep(200)

    def lambda_32D():

        label("loc_32D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_32D")

    QueueWorkItem2(0x101, 2, lambda_32D)
    Sleep(500)

    def lambda_343():
        OP_8F(0xFE, 0x14AA, 0x0, 0xFFFFC9BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_343)
    ClearChrFlags(0x102, 0x80)
    OP_22(0xAD, 0x0, 0x64)
    OP_8E(0x102, 0x1612, 0x0, 0xFFFFC662, 0x32C8, 0x0)
    ClearChrFlags(0x102, 0x4)
    OP_96(0x102, 0x12C0, 0x0, 0xFFFFC4D2, 0x320, 0x1B58)
    SetChrChipByIndex(0x102, 65535)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#008F呼～吓了我一大跳！\x01",
            "没想到会是这样滑下来的设计。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来已经到达秘密水道了。\x01",
            "　\x02\x03",
            "走，快点追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_2_218 end

    def Function_3_452(): pass

    label("Function_3_452")

    EventBegin(0x0)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x4)

    def lambda_464():

        label("loc_464")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_464")

    QueueWorkItem2(0x101, 1, lambda_464)

    def lambda_475():

        label("loc_475")

        TurnDirection(0x102, 0x9, 0)
        OP_48()
        Jump("loc_475")

    QueueWorkItem2(0x102, 1, lambda_475)

    def lambda_486():
        OP_8E(0x101, 0x1234, 0x0, 0x3494, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_486)

    def lambda_4A1():
        OP_8E(0x102, 0x1266, 0x0, 0x30C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A1)
    OP_6D(4330, 0, 12390, 1000)

    ChrTalk(
        0xA,
        "#103F哦，好像来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#560F姐姐，这边！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#054F太慢了！\x01",
            "在磨蹭什么呢？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#506F不好意思。\x01",
            "刚才稍微谈了点老爸的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x4)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x102, 0x1000)
    OP_8C(0x102, 270, 0)
    SetChrSubChip(0x102, 2)

    def lambda_59C():
        OP_99(0xFE, 0x2, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_59C)
    OP_96(0x102, 0xD34, 0xFFFFFBB4, 0x35F2, 0x3E8, 0x1770)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x1000)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x4)
    OP_8E(0x102, 0xA6E, 0xFFFFFBB4, 0x35F2, 0xBB8, 0x0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    TurnDirection(0x102, 0x101, 400)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x1000)
    OP_8C(0x101, 270, 0)
    SetChrSubChip(0x101, 4)

    def lambda_61E():
        OP_99(0xFE, 0x4, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_61E)
    OP_96(0x101, 0xD34, 0xFFFFFBB4, 0x35F2, 0x3E8, 0x1770)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0)
    TurnDirection(0x101, 0xA, 400)
    ClearChrFlags(0x101, 0x4)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x102,
        (
            "#012F让你们久等了。\x01",
            "我们这就出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#105F好……\x01",
            "你们抓紧了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6DF)
    Sleep(400)

    def lambda_6F2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F2)

    def lambda_700():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_700)

    def lambda_70E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_70E)

    def lambda_71C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_71C)

    def lambda_72A():
        OP_6D(890, 0, 18340, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72A)

    def lambda_742():
        OP_67(0, 3790, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_742)

    def lambda_75A():
        OP_6C(60000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_75A)
    OP_22(0x92, 0x0, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0xB, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0xB, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    def lambda_806():
        OP_8C(0xFE, 135, 5)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_806)

    def lambda_814():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_814)
    Sleep(200)

    def lambda_834():
        OP_8C(0xFE, 135, 10)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_834)

    def lambda_842():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_842)
    Sleep(500)

    def lambda_862():
        OP_8C(0xFE, 135, 20)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_862)

    def lambda_870():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_870)

    def lambda_88B():
        OP_8C(0xFE, 135, 13)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_88B)
    Sleep(100)

    def lambda_89E():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_89E)
    Sleep(100)

    def lambda_8BE():
        OP_8C(0xFE, 135, 13)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8BE)

    def lambda_8CC():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8CC)
    Sleep(250)

    def lambda_8EC():
        OP_8C(0xFE, 135, 8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8EC)

    def lambda_8FA():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8FA)
    Sleep(250)

    def lambda_91A():
        OP_8C(0xFE, 135, 5)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_91A)

    def lambda_928():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_928)
    Sleep(250)

    def lambda_948():
        OP_8C(0xFE, 180, 5)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_948)

    def lambda_956():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_956)
    Sleep(300)

    def lambda_976():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_976)

    def lambda_984():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_984)
    Sleep(100)

    def lambda_9A4():
        OP_8C(0xFE, 180, 15)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9A4)

    def lambda_9B2():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9B2)
    Sleep(100)

    def lambda_9D2():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9D2)

    def lambda_9E0():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9E0)
    Sleep(300)
    PlayEffect(0x4, 0x2, 0xB, 0, 0, 2200, 180, 0, 0, 1000, 100, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_A35():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A35)

    def lambda_A43():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A43)
    Sleep(300)

    def lambda_A63():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A63)

    def lambda_A7E():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A7E)
    Sleep(300)

    def lambda_A91():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A91)

    def lambda_A9F():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A9F)
    Sleep(1000)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_452 end

    SaveToFile()

Try(main)
