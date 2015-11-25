from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3303   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        '巨大企鹅',                             # 9
    )

    DeclEntryPoint(
        Unknown_00              = 12000,
        Unknown_04              = 0,
        Unknown_08              = 107000,
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
        'ED6_DT09/CH10700 ._CH',             # 00
        'ED6_DT07/CH00100 ._CH',             # 01
        'ED6_DT07/CH00101 ._CH',             # 02
        'ED6_DT07/CH00110 ._CH',             # 03
        'ED6_DT07/CH00111 ._CH',             # 04
        'ED6_DT07/CH00160 ._CH',             # 05
        'ED6_DT07/CH00161 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
        'ED6_DT07/CH00171 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT09/CH10700P._CP',             # 00
        'ED6_DT07/CH00100P._CP',             # 01
        'ED6_DT07/CH00101P._CP',             # 02
        'ED6_DT07/CH00110P._CP',             # 03
        'ED6_DT07/CH00111P._CP',             # 04
        'ED6_DT07/CH00160P._CP',             # 05
        'ED6_DT07/CH00161P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
        'ED6_DT07/CH00171P._CP',             # 08
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


    DeclActor(
        TriggerX            = 12720,
        TriggerZ            = 160,
        TriggerY            = 113900,
        TriggerRange        = 1200,
        ActorX              = 12720,
        ActorZ              = 160,
        ActorY              = 113900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_136",          # 00, 0
        "Function_1_159",          # 01, 1
        "Function_2_16F",          # 02, 2
        "Function_3_369",          # 03, 3
    )


    def Function_0_136(): pass

    label("Function_0_136")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_142"),
        (SWITCH_DEFAULT, "loc_158"),
    )


    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155")
    OP_A2(0x554)
    Event(0, 2)

    label("loc_155")

    Jump("loc_158")

    label("loc_158")

    Return()

    # Function_0_136 end

    def Function_1_159(): pass

    label("Function_1_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_169")
    OP_64(0x0, 0x1)

    label("loc_169")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_159 end

    def Function_2_16F(): pass

    label("Function_2_16F")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_28(0x42, 0x1, 0x40)
    OP_6D(12310, -50, 109720, 0)
    OP_67(0, 4019, -10000, 0)
    OP_6B(7650, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    StopSound(0x64, 0x3D090, 0x0)
    SetChrPos(0x101, 12570, 10, 89500, 0)
    SetChrPos(0x102, 13320, -60, 88210, 0)
    SetChrPos(0x107, 11270, 0, 87840, 0)
    SetChrPos(0x108, 12570, -60, 87040, 0)

    def lambda_214():
        OP_6C(8000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_214)
    Sleep(5000)
    StopSound(0x0, 0x0, 0xBB8)

    def lambda_236():
        OP_6D(13110, 20, 92050, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_236)

    def lambda_24E():
        OP_6B(3850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_24E)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#004F唔哇～……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F好漂亮……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F呵呵……\x01",
            "真是不错的景观啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯嗯！\x01",
            "想象不出我们就在洞窟里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这里应该就是洞窟湖了吧。\x02\x03",
            "『塞姆里亚苔藓』\x01",
            "也许就生长在这附近的石笋上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FＯＫ！\x01",
            "继续进行地毯式搜索！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_16F end

    def Function_3_369(): pass

    label("Function_3_369")

    OP_A2(0x555)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 12730, 160, 113310, 0)
    SetChrPos(0x102, 11580, -30, 112670, 0)
    SetChrPos(0x107, 13950, -30, 112810, 0)
    SetChrPos(0x108, 12450, -50, 111850, 0)
    OP_6D(12600, 160, 114570, 1000)
    OP_0D()
    SetChrPos(0x8, 8000, -3500, 119800, 0)

    ChrTalk(
        0x107,
        "#560F啊，这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F看来这就是我们要找的\x01",
            "『塞姆里亚苔藓』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哇～闪闪亮的……\x01",
            "真没想到竟然是这么漂亮的苔藓呢。\x02\x03",
            "为什么会发光呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也许是因为苔藓里面\x01",
            "含有大量的七耀石成分吧。\x02\x03",
            "马上采集好，\x01",
            "然后赶快返回蔡斯吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "采集到了\x07\x02",
            "塞姆里亚苔藓\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x365, 1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#006F好，任务完成！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，我们马上回去，\x01",
            "然后把这药料交给教区长吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)

    ChrTalk(
        0x101,
        "#001F嗯，就这样做吧……\x02",
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x108,
        "#072F……慢着。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 400)
    Fade(250)
    SetChrPos(0x108, 12550, -50, 111760, 315)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x108, 7)
    OP_0D()

    def lambda_64F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64F)

    def lambda_65D():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_65D)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#004F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F啊……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 800)
    Fade(500)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 3)
    OP_0D()
    Sleep(250)

    def lambda_6B2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6B2)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x108,
        "#076F小心！\x02",
    )

    CloseMessageWindow()

    def lambda_6E0():

        label("loc_6E0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6E0")

    QueueWorkItem2(0x107, 1, lambda_6E0)

    def lambda_6F1():

        label("loc_6F1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6F1")

    QueueWorkItem2(0x101, 1, lambda_6F1)

    def lambda_702():

        label("loc_702")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_702")

    QueueWorkItem2(0x102, 1, lambda_702)

    def lambda_713():

        label("loc_713")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_713")

    QueueWorkItem2(0x108, 1, lambda_713)

    def lambda_724():
        OP_6D(8400, -50, 117630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_724)

    def lambda_73C():
        OP_6B(2480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_73C)

    def lambda_74C():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_74C)
    Sleep(2000)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 160, 0)

    def lambda_772():

        label("loc_772")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_772")

    QueueWorkItem2(0x8, 3, lambda_772)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_79A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_79A)

    def lambda_7AC():
        OP_67(0, 5840, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AC)

    def lambda_7C4():
        OP_6D(9140, 60, 113530, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C4)

    def lambda_7DC():
        OP_6B(3140, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7DC)

    def lambda_7EC():
        OP_6C(334000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_7EC)
    LoadEffect(0x0, "map\\\\mp012_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 8000, -1500, 119800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xE4, 0x0, 0x64)

    def lambda_84A():
        OP_96(0xFE, 0x21A2, 0x32, 0x1BABC, 0x1F40, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_84A)
    Sleep(500)
    OP_8C(0x8, 120, 0)
    WaitChrThread(0x8, 0x0)
    OP_22(0xE5, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x107, 5)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#509F这、这是什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F哇哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呼呼……\x01",
            "看来它就是这洞窟湖的主人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这下……\x01",
            "看来不得不战斗了！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x107, 0xFF)
    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_9B2"),
        (SWITCH_DEFAULT, "loc_9B5"),
    )


    label("loc_9B2")

    OP_B4(0x0)
    Return()

    label("loc_9B5")

    EventBegin(0x0)
    SetChrPos(0x101, 7630, 40, 114200, 0)
    SetChrPos(0x102, 8980, 30, 114440, 0)
    SetChrPos(0x108, 8950, 50, 113270, 0)
    SetChrPos(0x107, 7380, -40, 112770, 0)
    OP_6D(8280, 40, 113660, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrFlags(0x8, 0x80)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#007F吓、吓了一大跳～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F虽、虽然挺可爱的，\x01",
            "不过还是有点可怕呢～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F呼……\x01",
            "总算是把魔兽击退了。\x02\x03",
            "#012F不过，再磨磨蹭蹭的话，\x01",
            "恐怕我们又会遭到袭击的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，没错。\x01",
            "尽快回城镇比较好。\x02\x03",
            "只要把刚才采到的药料\x01",
            "拿到城镇里的教会就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，快走吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x556)
    OP_28(0x42, 0x1, 0x80)
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_3_369 end

    SaveToFile()

Try(main)
