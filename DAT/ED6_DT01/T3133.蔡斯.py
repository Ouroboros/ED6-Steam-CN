from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3133   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '拉赛尔博士',                           # 9
        '玛多克工房长',                         # 10
        '黑色导力器',                           # 11
        '感应妨碍器',                           # 12
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH01250 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
        'ED6_DT06/CH20130 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH01250P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
        'ED6_DT06/CH20130P._CP',             # 06
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917506,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179650,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 28740,
        Y                   = -2000,
        Z                   = 2700,
        Range               = 30300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFF060,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 31850,
        TriggerZ            = 0,
        TriggerY            = 30290,
        TriggerRange        = 800,
        ActorX              = 31850,
        ActorZ              = 500,
        ActorY              = 30290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_2FA",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_34F",          # 03, 3
        "Function_4_4AD",          # 04, 4
        "Function_5_644",          # 05, 5
        "Function_6_D9D",          # 06, 6
        "Function_7_E67",          # 07, 7
        "Function_8_1A90",         # 08, 8
        "Function_9_2BFF",         # 09, 9
        "Function_10_2C6B",        # 0A, 10
        "Function_11_2C7D",        # 0B, 11
        "Function_12_336E",        # 0C, 12
        "Function_13_3DFD",        # 0D, 13
        "Function_14_46B0",        # 0E, 14
        "Function_15_487B",        # 0F, 15
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1B4")
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_1C2")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_1D0")
    OP_A3(0x3FC)
    Event(0, 13)

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_1E7")
    OP_A3(0x3FD)
    Event(0, 8)
    OP_B1("t3133_y")

    label("loc_1E7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1F7"),
        (106, "loc_225"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    OP_A2(0x50F)
    Event(0, 4)

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222")
    SetMapFlags(0x10000000)
    OP_A2(0x55E)
    Event(0, 14)

    label("loc_222")

    Jump("loc_238")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_235")
    Event(0, 5)

    label("loc_235")

    Jump("loc_238")

    label("loc_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_END)), "loc_242")
    Jump("loc_27F")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_262")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 31850, 0, 30290, 0)
    Jump("loc_27F")

    label("loc_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_27F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 34470, -300, 10490, 0)

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_2F9")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_2B0")
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 30000, -1000, 8900, 270)
    Jump("loc_2F9")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2D0")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28000, 0, 31400, 180)
    Jump("loc_2F9")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F9")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 29950, -1000, 8090, 269)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrFlags(0x8, 0x10)

    label("loc_2F9")

    Return()

    # Function_0_1A6 end

    def Function_1_2FA(): pass

    label("Function_1_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_312")
    OP_B1("t3133_y")
    Jump("loc_31B")

    label("loc_312")

    OP_B1("t3133_n")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32B")
    OP_64(0x0, 0x1)

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_338")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)

    label("loc_338")

    Return()

    # Function_1_2FA end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_339")

    label("loc_34E")

    Return()

    # Function_2_339 end

    def Function_3_34F(): pass

    label("Function_3_34F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_467")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC")

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔唔………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，这位老爷爷\x01",
            "好像精力十分集中地在做什么事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们又没什么事，\x01",
            "还是不要打扰他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_3FC")


    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔唔………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这位老爷爷\x01",
            "好像精力十分集中地在做什么事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们又没什么事，\x01",
            "还是不要打扰他了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464")

    Jump("loc_4A9")

    label("loc_467")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔唔………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "问题果然在这里啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_4A9")

    TalkEnd(0xFE)
    Return()

    # Function_3_34F end

    def Function_4_4AD(): pass

    label("Function_4_4AD")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-380, 0, 8170, 0)
    SetChrPos(0x107, -680, 0, -1960, 225)
    SetChrPos(0x101, -2700, 0, -3100, 0)
    SetChrPos(0x102, -1600, 0, -3600, 0)
    FadeToBright(1000, 0)
    OP_6D(-2000, 0, -600, 3000)

    ChrTalk(
        0x107,
        (
            "#067F#2P嘿嘿……\x01",
            "这里就是我家哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#001F哇～看起来很不错啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，的确很不错。\x01",
            "那么拉赛尔博士现在在哪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F#2P嗯～爷爷他嘛，\x01",
            "我想应该在工房里工作吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CA():
        OP_6D(1070, 0, -1350, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5CA)
    OP_8C(0x107, 90, 400)
    Sleep(300)
    OP_8C(0x102, 90, 400)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x107, 0x2)

    ChrTalk(
        0x107,
        "#060F进去那房间就是了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，ＯＫ。\x01",
            "那我们赶快去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_4AD end

    def Function_5_644(): pass

    label("Function_5_644")

    EventBegin(0x0)
    OP_6D(31150, 0, 36720, 0)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x107, 30900, 0, 36300, 225)
    SetChrPos(0x101, 29800, 0, 37500, 180)
    SetChrPos(0x102, 31000, 0, 37400, 225)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 27800, 500, 31400, 180)
    SetChrChipByIndex(0x8, 6)

    def lambda_6BF():

        label("loc_6BF")

        OP_99(0xFE, 0x1, 0x2, 0x3E8)
        OP_48()
        Jump("loc_6BF")

    QueueWorkItem2(0x8, 1, lambda_6BF)
    ClearChrFlags(0x107, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x101, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        "#061F爷爷，我回来了。\x02",
    )

    CloseMessageWindow()
    OP_6D(29900, 0, 34680, 1000)
    Sleep(500)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x8,
        (
            "#102F#6P……唔唔唔………\x02\x03",
            "这里这样，然后……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_760():

        label("loc_760")

        OP_99(0xFE, 0x1, 0x2, 0x5DC)
        OP_48()
        Jump("loc_760")

    QueueWorkItem2(0x8, 1, lambda_760)
    Sleep(200)

    ChrTalk(
        0x8,
        "#102F#6P………唔唔哦哦……！\x02",
    )

    OP_9E(0x8, 0x1E, 0x0, 0x190, 0x1388)
    CloseMessageWindow()

    def lambda_7A5():

        label("loc_7A5")

        OP_99(0xFE, 0x1, 0x2, 0x7D0)
        OP_48()
        Jump("loc_7A5")

    QueueWorkItem2(0x8, 1, lambda_7A5)
    Sleep(200)

    ChrTalk(
        0x8,
        "#102F#6P………喔喔喔喔……！\x02",
    )

    OP_9E(0x8, 0x32, 0x0, 0x1F4, 0x1770)
    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F……啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，就是这位吗？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)

    def lambda_835():
        OP_6D(29760, 0, 33950, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_835)

    def lambda_84D():
        OP_8E(0xFE, 0x7468, 0x0, 0x846C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84D)
    Sleep(800)

    def lambda_86D():
        OP_8E(0xFE, 0x797C, 0x0, 0x84D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_86D)
    Sleep(200)

    def lambda_88D():
        OP_8E(0xFE, 0x78B4, 0x0, 0x891C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88D)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x4)

    def lambda_8B2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B2)
    WaitChrThread(0x107, 0x1)

    def lambda_8C5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8C5)
    WaitChrThread(0x102, 0x1)

    def lambda_8D8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D8)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x101,
        (
            "#006F那个～初次见面。\x02\x03",
            "我是游击士协会的准游击士\x01",
            "艾丝蒂尔·布莱特。\x02\x03",
            "其实我们有事想找博士您……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_971():

        label("loc_971")

        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        OP_48()
        Jump("loc_971")

    QueueWorkItem2(0x8, 1, lambda_971)

    ChrTalk(
        0x8,
        (
            "#102F#6P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……谈谈……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_44(0x8, 0xFF)
    SetChrSubChip(0x8, 0)
    OP_9E(0x8, 0x32, 0x0, 0x3E8, 0x1770)
    OP_63(0x8)
    SetChrSubChip(0x8, 3)

    ChrTalk(
        0x8,
        "#103F#5S#6P完、完成啦啊啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#004F呜哇！？\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0x1E, 0x0, 0x1F4, 0x1770)

    ChrTalk(
        0x8,
        (
            "#101F#6P哇哈哈，太好了！\x01",
            "总算完成啦啊啊啊！\x02\x03",
            "真不愧是我呀！我实在是太厉害了！\x02\x03",
            "嗯，好的！\x01",
            "得快点拿它来测试。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ADD():

        label("loc_ADD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_ADD")

    QueueWorkItem2(0x102, 1, lambda_ADD)

    def lambda_AEE():

        label("loc_AEE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_AEE")

    QueueWorkItem2(0x107, 1, lambda_AEE)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_96(0x8, 0x70A8, 0x0, 0x7CCE, 0x1F4, 0x1770)

    def lambda_B2C():
        OP_6D(29900, 0, 34680, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B2C)

    def lambda_B44():
        OP_8E(0xFE, 0x7486, 0x0, 0x90BA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B44)
    Sleep(200)

    ChrTalk(
        0x101,
        "#504F#10A喂呀啊啊啊！？\x05\x02",
    )

    OP_43(0x101, 0x1, 0x0, 0x6)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x639C, 0xFFFFF830, 0x91B4, 0x1F40, 0x0)

    def lambda_BA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_BA3)
    OP_8E(0x8, 0x63B0, 0xFFFFF6A0, 0x8778, 0x1F40, 0x0)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    SetChrPos(0x8, 30000, -1000, 8900, 270)

    def lambda_BE2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE2)
    Sleep(1500)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 800)
    OP_8C(0x101, 0, 800)

    ChrTalk(
        0x101,
        "#005F怎、怎么回事啊～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F对、对不起，艾丝蒂尔姐姐。\x02\x03",
            "爷爷他，只要一进入研究状态，\x01",
            "就会旁若无人的呢……\x02\x03",
            "几天前开始制造的装置终于完成了，\x01",
            "所以爷爷他刚才这么兴奋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F原来如此……\x01",
            "真不愧是忘我的天才啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哎呀哎呀，\x01",
            "我觉得这不是问题所在吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#562F真是不好意思呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x510)
    EventEnd(0x0)
    Return()

    # Function_5_644 end

    def Function_6_D9D(): pass

    label("Function_6_D9D")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0x7D, 0x0, 0x64)
    OP_8F(0xFE, 0x7620, 0x0, 0x8480, 0x1F40, 0x0)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    OP_62(0xFE, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)
    Return()

    # Function_6_D9D end

    def Function_7_E67(): pass

    label("Function_7_E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A8F")
    EventBegin(0x0)
    SetMapFlags(0x10000000)
    Fade(1000)
    OP_4A(0x8, 255)
    OP_6D(32000, -1000, 10100, 0)
    SetChrPos(0x107, 31500, -1000, 200, 0)
    SetChrPos(0x101, 30600, -1000, -800, 0)
    SetChrPos(0x102, 31800, -1000, -1000, 0)
    OP_0D()

    def lambda_ECE():

        label("loc_ECE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_ECE")

    QueueWorkItem2(0x101, 1, lambda_ECE)

    def lambda_EDF():

        label("loc_EDF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EDF")

    QueueWorkItem2(0x102, 1, lambda_EDF)

    def lambda_EF0():

        label("loc_EF0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EF0")

    QueueWorkItem2(0x107, 1, lambda_EF0)

    def lambda_F01():
        OP_8E(0xFE, 0x7A44, 0xFFFFFC18, 0x1DB0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_F01)
    Sleep(100)

    def lambda_F21():
        OP_8E(0xFE, 0x7788, 0xFFFFFC18, 0x1838, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F21)
    Sleep(100)

    def lambda_F41():
        OP_8E(0xFE, 0x7C38, 0xFFFFFC18, 0x189C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F41)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x107,
        (
            "#560F#2P爷爷，我说啊。\x02\x03",
            "那个那个，\x01",
            "这位姐姐有事要找您呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#103F#1P嗯……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0x8,
        (
            "#101F#1P哦哦，提妲！\x01",
            "正好！你回来得正好！\x02\x03",
            "我正要做测试，\x01",
            "你马上帮我收集一下资料吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F#2P咦？但是，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F#1P这次的发明是\x01",
            "让生命感应器无效化的导力器！\x02\x03",
            "它能产生特殊的导力场，\x01",
            "使扫描不能正常地进行运行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F#2P真、真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F#1P当然是真的。\x01",
            "这可是货真价实的新发明啊！\x02\x03",
            "来来，\x01",
            "快来帮我启动测试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F#2P嗯！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)

    def lambda_11CC():
        OP_6D(32910, -1000, 8880, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11CC)

    def lambda_11E4():
        OP_8E(0xFE, 0x7EFD, 0xFFFFFC18, 0x2936, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11E4)
    Sleep(300)

    def lambda_1204():
        OP_8E(0xFE, 0x8692, 0xFFFFFC18, 0x2102, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1204)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    WaitChrThread(0x8, 0x2)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉赛尔博士和提妲\x01",
            "开始操作一部看似相当复杂的装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    LoadEffect(0x0, "map\\\\mp029_00.eff")
    LoadEffect(0x1, "map\\\\mp029_01.eff")
    LoadEffect(0x2, "map\\\\mp029_02.eff")
    PlayEffect(0x1, 0x4, 0xFF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, 33570, -400, 9620, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#509F……喂喂，我说你们两位～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈。\x01",
            "看来得等上一段时间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 800)

    ChrTalk(
        0x8,
        "#102F喂，那边那个黑头发的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F哎，是在叫我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F除了你还有谁？\x02\x03",
            "快到二楼的书架那里，\x01",
            "把那本『关于导力场的斥力值』\x01",
            "的笔记给我拿来！\x02\x03",
            "听懂了没有！还不快去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好、好的，知道了。\x02",
    )

    CloseMessageWindow()

    def lambda_14FB():

        label("loc_14FB")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_14FB")

    QueueWorkItem2(0x101, 1, lambda_14FB)
    OP_8C(0x102, 180, 600)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F等、等一下约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F对了，\x01",
            "还有那个头发像触角的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#509F#4P触、触角……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 800)

    ChrTalk(
        0x101,
        "#005F#4P你、你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F别站在那里发呆，\x01",
            "快点去给我泡杯咖啡！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F#4P为、为什么要我去！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F顺带一提，我喜欢黑咖啡。\x02\x03",
            "要泡得像泥一样浓哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#4P根本不听人家说话……\x02\x03",
            "#007F唉，真是的，知道了啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 800)
    OP_8E(0x101, 0x797C, 0xFFFFFC18, 0x3E8, 0x1770, 0x0)

    def lambda_16E0():
        OP_8E(0xFE, 0x51A4, 0x0, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16E0)
    OP_6D(34600, -1000, 10700, 2000)
    OP_22(0x9E, 0x1, 0x64)
    Sleep(200)
    PlayEffect(0x1, 0x0, 0xFF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x1, 0xFF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x2, 0xFF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x3, 0xFF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(600)

    ChrTalk(
        0x107,
        "#061F#2P……嗯，很顺利呢⊙\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 315, 400)

    ChrTalk(
        0x107,
        (
            "#560F#2P爷爷你看，\x01",
            "我这里的设定完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#101F#1P哦哦，很快嘛。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#064F#2P对了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)
    Sleep(200)
    OP_8C(0x107, 270, 400)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#065F#2P哎呀……\x01",
            "艾丝蒂尔姐姐他们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#103F#1P谁呀？\x02\x03",
            "……………………………\x02\x03",
            "对了，说起来……\x01",
            "刚才有两个以前没见过的年轻助手。\x02\x03",
            "咦……\x01",
            "不是玛多克那家伙派来的新人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#562F#2P爷、爷爷啊……\x02",
    )

    CloseMessageWindow()
    OP_23(0x9E)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，\x01",
            "艾丝蒂尔和约修亚帮博士做起了实验……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在两人的协助下实验顺利地进行，\x01",
            "当实验结束的时候，已经是傍晚的时分了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T3133   ._SN", 100, 0, 1)
    IdleLoop()

    label("loc_1A8F")

    Return()

    # Function_7_E67 end

    def Function_8_1A90(): pass

    label("Function_8_1A90")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    OP_6D(-300, 0, 2200, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 300, 0, 500, 270)
    SetChrPos(0x107, 300, 200, 1700, 270)
    SetChrPos(0x101, -2300, 200, 500, 90)
    SetChrPos(0x102, -2300, 200, 1700, 90)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x102, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 5)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrSubChip(0x102, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#101F#2P哇哈哈，抱歉抱歉。\x02\x03",
            "完全把你们俩\x01",
            "当成是中央工房的新人了。\x02\x03",
            "结果就和平常吩咐工房的员工那样，\x01",
            "把你们使来唤去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F真是的，亏您还笑得出来。\x02\x03",
            "不止是泡咖啡，\x01",
            "还要我们帮这帮那的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，我觉得挺好啊。\x01",
            "当作是宝贵的工作经验不就行了。\x02\x03",
            "而且新型导力器的启动实验\x01",
            "也不是随便就能遇到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#103F#2P哦，这个小伙子。\x01",
            "十分之明白事理嘛。\x02\x03",
            "#101F不如别再当什么游击士了，\x01",
            "投身导力技术的研究事业吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)

    ChrTalk(
        0x107,
        (
            "#063F爷爷！真是的！\x02\x03",
            "#562F对不起，\x01",
            "艾丝蒂尔姐姐、约修亚哥哥。\x02\x03",
            "刚才受到爷爷的影响，\x01",
            "结果连我也沉迷进实验里去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哎哟～不要紧。\x01",
            "提妲没有必要道歉啦。\x02\x03",
            "#007F我还在想『导力革命之父』\x01",
            "会是个怎样厉害的人呢……\x02\x03",
            "今天终于见识到了，\x01",
            "原来是个得意忘形的老爷爷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F#2P哇哈哈，过奖过奖。\x02\x03",
            "#100F不过话说回来，\x01",
            "真没想到卡西乌斯的孩子会来拜访我。\x02\x03",
            "我也吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊～\x01",
            "博士果然认识老爸吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F#2P嗯，很久以前就认识了。\x02\x03",
            "从他还在军队当兵开始，\x01",
            "我和卡西乌斯已经有２０年的交情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嘿嘿……\x01",
            "我也见过卡西乌斯叔叔哦。\x02\x03",
            "蓄着胡子，是位很有型的叔叔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～\x01",
            "说不清是有型还是古怪啦……\x02\x03",
            "#006F不过，既然这样的话，\x01",
            "我们就放心把那东西交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊，我想没问题的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#103F#2P什么，是什么东西？\x02\x03",
            "说起来，\x01",
            "你们不是说有事找我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们向博士详细地说明了有关的事情，\x01",
            "并且拿出了黑色导力器。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x35B, 1)
    Fade(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0xA, -900, 800, 270, 0)
    ClearChrFlags(0xA, 0x80)
    OP_0D()
    Sleep(500)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#103F#2P……哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F哇～\x01",
            "漆黑的导力器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F#2P嗯，这东西很有意思。\x02\x03",
            "不仅没有生产序号，\x01",
            "连个接缝都找不到。\x02\x03",
            "而且这个外壳……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉赛尔博士\x01",
            "从腰上的皮带处拿出了工作用的小刀。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "他用小刀大力地\x01",
            "往黑色导力器的表面划了下去。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F什、什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F特殊合金制的小刀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F#2P……………………………\x02\x03",
            "#104F……果然如此……\x02\x03",
            "#100F来，你们看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯、嗯……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们\x01",
            "仔细地往黑色导力器的表面看去。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F一点伤痕都没有……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F#2P看来这个外壳是用\x01",
            "一种非常特殊的素材制作出来的。\x01",
            "而这种素材比我所知的任何金属都要硬。\x02\x03",
            "要想切开它来调查内部，\x01",
            "看来是相当困难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F原、原来是\x01",
            "这么不得了的东西啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F连切开都不行的话，\x01",
            "看来的确是相当麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#104F#2P唔……\x01",
            "花点时间还是能把外壳切开的。\x02\x03",
            "不过在此之前，\x01",
            "还是先用测定装置检查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F测定装置？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F就是刚才做实验也用过的\x01",
            "那个大型装置。\x02\x03",
            "是个能对导力波的动向\x01",
            "进行实时测定的装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F不、不是很明白……\x01",
            "用了那个装置会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F#2P简单来说，\x01",
            "我们就能知道这东西是怎么工作的了。\x02\x03",
            "当然，只凭导力波动向的判断，\x01",
            "还只能停留在推测的范围里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F即使如此，\x01",
            "能得到重要线索的可能性还是很高吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#102F#2P嗯。\x02\x03",
            "#101F那么事不宜迟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F可是可是，爷爷。\x01",
            "差不多是吃饭的时间了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#103F#2P哎。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 0)

    ChrTalk(
        0x107,
        (
            "#067F艾丝蒂尔姐姐，\x01",
            "你们不嫌弃的话，也一起吃吧。\x02\x03",
            "虽然我对自己的手艺没什么自信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，那我们就不客气啦⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F可以的话我也来帮忙吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#101F#2P好，那就这样吧。\x02\x03",
            "晚饭准备好之前，\x01",
            "我就先稍微对这个……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)

    ChrTalk(
        0x107,
        (
            "#062F不、不行。\x01",
            "我也想看嘛。\x02\x03",
            "爷爷可不要耍赖先看哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#102F#2P小气。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F（怎么说呢，这两爷孙……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（血缘果然是奇妙东西啊。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1A90 end

    def Function_9_2BFF(): pass

    label("Function_9_2BFF")

    OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0x1CC, 0x1388, 0x0)
    OP_8E(0xFE, 0x5B90, 0x0, 0xBE, 0x1388, 0x0)
    OP_44(0x101, 0xFF)
    OP_8E(0xFE, 0x5A3C, 0x7D0, 0x22F6, 0x1388, 0x0)

    def lambda_2C45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C45)
    OP_8E(0xFE, 0x659A, 0xFA0, 0x23A0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_2BFF end

    def Function_10_2C6B(): pass

    label("Function_10_2C6B")

    OP_A6(0x1)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    OP_A3(0x1)
    Return()

    # Function_10_2C6B end

    def Function_11_2C7D(): pass

    label("Function_11_2C7D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(34700, -1000, 10700, 0)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x107, 32299, -1000, 10400, 0)
    SetChrPos(0x101, 32299, -1000, 8400, 45)
    SetChrPos(0x102, 32800, -1000, 7400, 45)

    ChrTalk(
        0x101,
        "#008F展示晚上的拉赛尔工房（※假定）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F咳……\x02\x03",
            "既然肚子已经吃饱了，\x01",
            "那么就快点开始吧。\x02\x03",
            "那么，艾丝蒂尔，\x01",
            "把那个导力器放到机器上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x8084, 0xFFFFFC18, 0x283C, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F这样就好了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F提妲，\x01",
            "你那边准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F嗯，很顺利哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F很好。\x02\x03",
            "那么『黑色导力器』的\x01",
            "导力波测定实验开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F『黑色导力器』？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F真是\x01",
            "马马乎乎的命名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100FSimple·is·best。\x02\x03",
            "总之\x01",
            "没有名字是很不方便的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F好紧张，好兴奋……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，提妲也\x01",
            "斗志满满呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F嘿嘿～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F好，那么开始啰！\x02\x03",
            "提妲。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F出力固定在４５％……各种测定器开始待命。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F明白……\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯。\x01",
            "各种测定器准备工作完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F那么，现在正式开始啰。\x02\x03",
            "在找不到出入力的情况下，\x01",
            "能探测到其中结晶回路产生的导力波，\x01",
            "对其发生的反应进行搜索……\x02\x03",
            "这里就是这个测定装置\x01",
            "发挥真正本领的地方！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F还真来劲了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F按下按钮。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F好、好刺眼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此，这样的话\x01",
            "就能增强结晶回路的负荷了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F对对……\x02\x03",
            "提妲，\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F唔……\x02\x03",
            "怎么回事，好奇怪呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F转速计的指针\x01",
            "在哆哆嗦嗦地震动……\x02\x03",
            "啊……\x02\x03",
            "开始骨碌骨碌地转了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F哎呀！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F这是怎么回事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F约修亚，这个是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那个时候的黑光……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#100F什么！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2C7D end

    def Function_12_336E(): pass

    label("Function_12_336E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(34700, -1000, 10700, 0)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x107, 32299, -1000, 10400, 0)
    SetChrPos(0x101, 23400, 0, 100, 0)
    SetChrPos(0x102, 23400, 0, 100, 0)

    ChrTalk(
        0x101,
        (
            "#005F夜晚以拉赛尔工房为起点\x01",
            "照明依次熄灭。（※假定）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F爷爷，\x01",
            "不能再继续了！\x02\x03",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F唔，还不能停！\x02\x03",
            "再一会就能发现点什么了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x765C, 0xFFFFFC18, 0x384, 0x32C8, 0x0)
    OP_8E(0x101, 0x8278, 0xFFFFFC18, 0x1900, 0x2710, 0x0)

    ChrTalk(
        0x101,
        (
            "#000F等一下！\x01",
            "城镇里的照明都灭了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 800)

    ChrTalk(
        0x107,
        "#060F哎！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 800)

    ChrTalk(
        0x8,
        (
            "#100F什么……\x02\x03",
            "唔，没办法了！\x01",
            "实验到此结束！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_356E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_356E)
    OP_8C(0x8, 0, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x02\x03",
            "恢复原样了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F呼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F记录器呢……\x02\x03",
            "不行，什么都没记录下来。\x02\x03",
            "这么看来，『黑色导力器』\x01",
            "上安装的本体是有生命的。\x02\x03",
            "接下来全部的东西……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_365B():
        OP_6D(33400, -1000, 10200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_365B)
    OP_8E(0x102, 0x765C, 0xFFFFFC18, 0x384, 0x32C8, 0x0)
    OP_8E(0x102, 0x7A44, 0xFFFFFC18, 0x12C0, 0x1770, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F太好了……\x01",
            "实验好像中止了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36CD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36CD)

    def lambda_36DB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_36DB)

    def lambda_36E9():

        label("loc_36E9")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_36E9")

    QueueWorkItem2(0x101, 1, lambda_36E9)

    ChrTalk(
        0x101,
        (
            "#000F啊，约修亚，\x01",
            "外面的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x7B0C, 0xFFFFFC18, 0x17D4, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "照明应该都恢复了。\x02\x03",
            "只不过大家都还没从骚动里恢复过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x02\x03",
            "但，这到底\x01",
            "是怎么一回事呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F是呀……\x02\x03",
            "硬要说的话，\x01",
            "只能说这是『导力停止现象』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F『导力停止现象』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是说导力器内部\x01",
            "运作的导力停止工作了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F果然是那个\x01",
            "『黑色导力器』的原因……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#100F嗯，不会错的。\x02\x03",
            "但竟能停止这么\x01",
            "广范围的导力器呀。\x02\x03",
            "呵呵呵呵……\x01",
            "这真是出乎意料的东西呀。\x02\x03",
            "有趣，实在是太有趣了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我想现在不是\x01",
            "说有趣的情况吧……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 23400, 0, 100, 0)

    NpcTalk(
        0x9,
        "男性的声音",
        "混蛋！！\x02",
    )

    CloseMessageWindow()

    def lambda_39DD():

        label("loc_39DD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_39DD")

    QueueWorkItem2(0x101, 1, lambda_39DD)

    def lambda_39EE():

        label("loc_39EE")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_39EE")

    QueueWorkItem2(0x107, 1, lambda_39EE)

    def lambda_39FF():

        label("loc_39FF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_39FF")

    QueueWorkItem2(0x102, 1, lambda_39FF)

    def lambda_3A10():

        label("loc_3A10")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3A10")

    QueueWorkItem2(0x8, 1, lambda_3A10)
    OP_8E(0x9, 0x765C, 0xFFFFFC18, 0x384, 0x1770, 0x0)
    OP_8E(0x9, 0x7724, 0xFFFFFC18, 0x1C20, 0x1770, 0x0)
    OP_8E(0x9, 0x7F58, 0xFFFFFC18, 0x1E78, 0x1770, 0x0)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x8,
        (
            "#100F哦，玛多克，\x01",
            "你来的真巧呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#800F一点也不巧！\x02\x03",
            "三番两次了，每次你\x01",
            "有新发明都要引起点骚动！\x02\x03",
            "这次你做了什么，\x01",
            "竟把城镇里的照明都弄灭了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B33():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B33)

    def lambda_3B41():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3B41)

    def lambda_3B4F():

        label("loc_3B4F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3B4F")

    QueueWorkItem2(0x102, 1, lambda_3B4F)

    ChrTalk(
        0x8,
        (
            "#100F真是失礼呀，\x01",
            "这次骚动可和我没关系。\x02\x03",
            "这是放在那边的\x01",
            "『黑色导力器』的杰作哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BBB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BBB)

    def lambda_3BC9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3BC9)

    def lambda_3BD7():

        label("loc_3BD7")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3BD7")

    QueueWorkItem2(0x102, 1, lambda_3BD7)

    ChrTalk(
        0x9,
        (
            "#800F那，那个就是……\x02\x03",
            "原来如此，那个就是\x01",
            "原因的话那这次异常事态就算了……\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#800F这个怎么可能\x01",
            "和你没关系嘛！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C98():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C98)

    def lambda_3CA6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3CA6)

    def lambda_3CB4():

        label("loc_3CB4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3CB4")

    QueueWorkItem2(0x102, 1, lambda_3CB4)

    ChrTalk(
        0x8,
        "#100F切，识破了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F两个人好像\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F感觉已经经常这样了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F啊……好丢人呀……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，艾丝蒂尔他们\x01",
            "慌忙地度过了来到蔡斯市的第一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于实验完成之后已经是深夜了，\x01",
            "艾丝蒂尔和约修亚就在拉赛尔工房借宿了一夜。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x511)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_336E end

    def Function_13_3DFD(): pass

    label("Function_13_3DFD")

    EventBegin(0x0)
    OP_6D(-2860, 0, 35210, 0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -2950, 0, 35300, 225)
    SetChrPos(0x101, -4360, 0, 33690, 45)
    SetChrPos(0x107, -5900, -2000, 39200, 0)
    SetChrFlags(0x107, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F#6P哎呀～\x01",
            "昨天一天真是够呛啊。\x02\x03",
            "这个城镇本身就够惊人的，\x01",
            "竟然还发生那样的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#5P哈哈，是啊。\x02\x03",
            "#013F话说回来，\x01",
            "那个『黑色导力器』……\x02\x03",
            "的确出乎意料，\x01",
            "看来是非同一般的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#6P嗯……\x02\x03",
            "实验也失败了，\x01",
            "博士打算怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#2P早上好。\x01",
            "艾丝蒂尔姐姐、约修亚哥哥。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)
    ClearChrFlags(0x107, 0x80)

    def lambda_400A():

        label("loc_400A")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_400A")

    QueueWorkItem2(0x101, 1, lambda_400A)

    def lambda_401B():

        label("loc_401B")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_401B")

    QueueWorkItem2(0x102, 1, lambda_401B)

    def lambda_402C():
        OP_6D(-2280, 0, 36270, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_402C)
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x9858, 0xBB8, 0x0)
    OP_8E(0x107, 0xFFFFF736, 0x0, 0x9042, 0x7D0, 0x0)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#501F#6P啊，早啊～\x01",
            "提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#4P早上好，\x01",
            "昨天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F嘿嘿，是呢。\x02\x03",
            "#560F艾丝蒂尔姐姐\x01",
            "你们昨晚睡得还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#6P嗯，睡得超饱哦㈱\x02\x03",
            "#000F说到这个，\x01",
            "博士也已经起床了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊～爷爷他啊，\x01",
            "一大早就赶去中央工房了。\x02\x03",
            "#061F他还对我说\x01",
            "『一定要找出黑色导力器的秘密』呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#6P哎呀哎呀～\x01",
            "昨晚被工房长先生那样训斥，\x01",
            "还是不吸取教训啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P很感谢他能帮忙调查那个导力器，\x01",
            "但是要这么麻烦他，\x01",
            "我们还真是有点过意不去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F啊哈哈，请别介意。\x02\x03",
            "爷爷他呢，\x01",
            "是自己想调查才会去调查的。\x02\x03",
            "#560F啊～对了，\x01",
            "吃完早饭我也要去中央工房。\x02\x03",
            "艾丝蒂尔姐姐，你们准备怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6P当然是跟你一起去啦。\x02\x03",
            "我也想知道那个导力器的真面目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P是啊。\x01",
            "我们也希望能帮上点忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F哇，太好了～\x01",
            "那我们这就出门吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#065F啊，不好！\x01",
            "汤还在火上呢～！\x02\x03",
            "#067F早饭马上就要做好了，\x01",
            "请姐姐你们再稍等一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x9858, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFFE8F4, 0xFFFFF830, 0x9920, 0x1388, 0x0)
    SetChrFlags(0x107, 0x80)
    OP_6D(-2860, 0, 35210, 1000)
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#008F#6P那孩子真可爱……\x02\x03",
            "好想把她带回家呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#018F#5P艾丝蒂尔，别像个大叔一样。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_3DFD end

    def Function_14_46B0(): pass

    label("Function_14_46B0")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(-1580, 0, -710, 0)
    SetChrPos(0x107, -1130, 0, -1640, 0)
    SetChrPos(0x102, -2660, 0, -2900, 0)
    SetChrPos(0x101, -2530, 0, -1500, 0)
    SetChrPos(0x106, -1330, 0, -3040, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F#5P好了……\x01",
            "开始找那个装置吧。\x02\x03",
            "会放在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4763():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4763)

    def lambda_4771():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4771)

    def lambda_477F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_477F)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        (
            "#560F#2P我想也许是在研究室的角落\x01",
            "或者是二楼的书房里吧。\x02\x03",
            "因为爷爷总是把刚发明的东西\x01",
            "随意地丢在一边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F听起来是个很奇怪的老爷子嘛。\x01",
            "　\x02\x03",
            "不管了。\x01",
            "总之快点找那东西出来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_14_46B0 end

    def Function_15_487B(): pass

    label("Function_15_487B")

    EventBegin(0x0)
    OP_A2(0x55F)
    OP_28(0x43, 0x1, 0x100)

    ChrTalk(
        0x101,
        "#006F找到啦找到啦⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这机器的确就是\x01",
            "那天我们帮忙实验的新型导力器。\x02\x03",
            "怎么样，能用吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F嗯……没问题。\x02\x03",
            "一切顺利的话，\x01",
            "能完全瞒过生命感应器哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "感应妨碍器\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x362, 1)

    ChrTalk(
        0x106,
        (
            "#051F好了，快点回协会吧。\x02\x03",
            "雾香应该也准备好\x01",
            "有关雷斯顿要塞的资料了。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Return()

    # Function_15_487B end

    SaveToFile()

Try(main)
