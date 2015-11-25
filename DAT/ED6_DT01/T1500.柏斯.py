from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1500   ._SN',
        MapName             = 'Bose',
        Location            = 'T1500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '罗伊德',                               # 9
        '艾露凯',                               # 10
        '阿妮特',                               # 11
        '努西',                                 # 12
        '约修亚',                               # 13
        '书',                                   # 14
        '目标用摄像机',                         # 15
        '小船',                                 # 16
        '安塞尔新街方向',                       # 17
    )

    DeclEntryPoint(
        Unknown_00              = -7000,
        Unknown_04              = 0,
        Unknown_08              = 82000,
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
        Unknown_30              = 225,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 50,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01180 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT09/CH10040 ._CH',             # 03
        'ED6_DT07/CH00010 ._CH',             # 04
        'ED6_DT07/CH00013 ._CH',             # 05
        'ED6_DT06/CH20032 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
        'ED6_DT06/CH20030 ._CH',             # 08
        'ED6_DT07/CH00003 ._CH',             # 09
        'ED6_DT06/CH20092 ._CH',             # 0A
        'ED6_DT06/CH20161 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01180P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT09/CH10040P._CP',             # 03
        'ED6_DT07/CH00010P._CP',             # 04
        'ED6_DT07/CH00013P._CP',             # 05
        'ED6_DT06/CH20032P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
        'ED6_DT06/CH20030P._CP',             # 08
        'ED6_DT07/CH00003P._CP',             # 09
        'ED6_DT06/CH20092P._CP',             # 0A
        'ED6_DT06/CH20161P._CP',             # 0B
    )

    DeclNpc(
        X                   = -44990,
        Z                   = -1970,
        Y                   = 38500,
        Direction           = 190,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -9420,
        Z                   = 400,
        Y                   = 41260,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3200,
        Z                   = -2000,
        Y                   = 42700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -45026,
        Z                   = -4000,
        Y                   = 32900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3882,
        Z                   = 500,
        Y                   = 41320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4990,
        Z                   = 900,
        Y                   = 41500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703943,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
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


    DeclEvent(
        X                   = -34266,
        Y                   = -3000,
        Z                   = 54198,
        Range               = -31910,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC274,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -29829,
        Y                   = -3000,
        Z                   = 55042,
        Range               = -27300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC5B2,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -5850,
        Y                   = -1000,
        Z                   = 80880,
        Range               = -10140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x14438,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = -2900,
        TriggerZ            = -3000,
        TriggerY            = 30600,
        TriggerRange        = 3000,
        ActorX              = -2900,
        ActorZ              = -3000,
        ActorY              = 30600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_40E",          # 01, 1
        "Function_2_46C",          # 02, 2
        "Function_3_482",          # 03, 3
        "Function_4_4A6",          # 04, 4
        "Function_5_2843",         # 05, 5
        "Function_6_29AF",         # 06, 6
        "Function_7_2A9A",         # 07, 7
        "Function_8_2C05",         # 08, 8
        "Function_9_31C8",         # 09, 9
        "Function_10_37A2",        # 0A, 10
        "Function_11_4A4F",        # 0B, 11
        "Function_12_4E9B",        # 0C, 12
        "Function_13_580B",        # 0D, 13
        "Function_14_63B3",        # 0E, 14
        "Function_15_67D4",        # 0F, 15
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2C2")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_3A5")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_2CC")
    Jump("loc_3A5")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_2E5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_71(0x3, 0x4)
    Jump("loc_3A5")

    label("loc_2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_319")
    SetChrChipByIndex(0xC, 5)
    SetChrPos(0xC, -6920, 700, 41300, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_71(0x3, 0x4)
    Jump("loc_3A5")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_332")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_71(0x3, 0x4)
    Jump("loc_3A5")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_END)), "loc_345")
    SetChrChipByIndex(0x8, 10)
    OP_44(0x8, 0xFF)
    Jump("loc_3A5")

    label("loc_345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_35D")
    SetChrChipByIndex(0x8, 10)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x10)
    Jump("loc_3A5")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_376")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_3A5")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_38A")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_3A5")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3A5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B3")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3CF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_3EB")
    SetMapFlags(0x10000000)
    OP_A3(0x3FC)
    Event(0, 11)
    OP_B1("t1500_y")

    label("loc_3EB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3F7"),
        (SWITCH_DEFAULT, "loc_40D"),
    )


    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40A")
    OP_A2(0x33B)
    Event(0, 8)

    label("loc_40A")

    Jump("loc_40D")

    label("loc_40D")

    Return()

    # Function_0_2AE end

    def Function_1_40E(): pass

    label("Function_1_40E")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x30046)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43D")
    OP_B1("t1500_y")
    Jump("loc_446")

    label("loc_43D")

    OP_B1("t1500_n")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45A")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_466")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466")
    OP_64(0x0, 0x1)

    label("loc_466")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_40E end

    def Function_2_46C(): pass

    label("Function_2_46C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_481")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_46C")

    label("loc_481")

    Return()

    # Function_2_46C end

    def Function_3_482(): pass

    label("Function_3_482")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A5")
    OP_8D(0xFE, 2000, 45800, 3600, 39900, 2000)
    Jump("Function_3_482")

    label("loc_4A5")

    Return()

    # Function_3_482 end

    def Function_4_4A6(): pass

    label("Function_4_4A6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_68A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "虽然只是看了一下，\x01",
            "不过我觉得你的天分还是挺高的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，真的吗？\x02\x03",
            "其实我从小就很喜欢钓鱼的呢。\x02\x03",
            "不过和罗伊德叔叔比起来，\x01",
            "我也只是玩玩的程度而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也不能这么说，\x01",
            "如果你认真锻炼下去，\x01",
            "要进入我们『钓公师团』也不是件难事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_687")

    label("loc_615")


    ChrTalk(
        0xFE,
        (
            "看来湖里的动静\x01",
            "也越来越小了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在已经傍晚了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_687")

    Jump("loc_283F")

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_6CF")

    ChrTalk(
        0xFE,
        "哟，小姑娘你也想钓鱼吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_76B")

    ChrTalk(
        0xFE,
        (
            "今天又让那家伙\x01",
            "逃过了我的追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要选择一个更好的位置才行，\x01",
            "再努力一下试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_283F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_END)), "loc_2659")
    OP_A2(0x33D)
    OP_28(0x38, 0x1, 0x4)
    OP_28(0x38, 0x1, 0x8)
    OP_28(0x38, 0x1, 0x10)
    OP_28(0x38, 0x1, 0x20)
    OP_8C(0xFE, 180, 0)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-44970, -1970, 39550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, -44510, -1970, 39560, 180)
    SetChrPos(0x102, -44260, -1970, 40650, 180)
    SetChrPos(0x103, -45160, -1970, 40920, 180)
    SetChrPos(0x104, -45360, -1970, 39650, 180)
    OP_0D()

    NpcTalk(
        0xFE,
        "拿着钓鱼竿的男人",
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……\x02\x03",
            "叔叔，您是不是那个\x01",
            "从王都过来的罗伊德先生呢？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "拿着钓鱼竿的男人",
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F好厉害的集中力……\x01",
            "除了鱼之外，眼中简直容不下任何东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F呵呵，真没办法。\x01",
            "看来要我亲自出马才行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x104, 0x4)
    OP_8E(0x104, 0xFFFF4E8A, 0xFFFFF84E, 0x96AA, 0x7D0, 0x0)
    OP_8C(0x104, 135, 400)
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    ChrTalk(
        0x104,
        "#035F……呼～……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "奥利维尔向男人的耳朵里吹了一口气。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0x1F40)

    NpcTalk(
        0xFE,
        "拿着钓鱼竿的男人",
        "#5S哎呀呀呀啊～！？\x02",
    )

    CloseMessageWindow()

    def lambda_AC1():
        OP_8E(0xFE, 0xFFFF4E44, 0xFFFFF84E, 0x9A24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC1)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 135, 400)
    SetChrChipByIndex(0xFE, 0)
    TurnDirection(0xFE, 0x104, 400)
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x4)

    NpcTalk(
        0xFE,
        "中年男子",
        "你、你们是谁！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        "什、什么时候站在这里的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F好、好下流～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F这种动作也敢做出来，\x01",
            "光是看到就起了一身鸡皮疙瘩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哎呀，没办法嘛。\x02\x03",
            "刚才叫他的时候一点反应也没有，\x01",
            "看来集中力不是一般的强哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请问您是罗伊德先生吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，啊啊，就是我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，你们怎么知道我的名字？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F其实是一位住在\x01",
            "柏斯的老伯告诉我们的。\x02\x03",
            "可以打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-44670, -2000, 43660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0xFE, -44640, -2000, 42760, 0)
    SetChrPos(0x101, -44550, -2000, 44760, 180)
    SetChrPos(0x102, -45710, -2000, 44500, 135)
    SetChrPos(0x103, -43620, -2000, 44550, 225)
    SetChrPos(0x104, -44920, -2000, 45730, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P原来如此……\x01",
            "你们是从库瓦诺那儿听说我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P啊啊，我的确是看到了。\x01",
            "就在前天夜晚，几个奇怪的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F果然是……\x02\x03",
            "可以把那天看到的事情\x01",
            "详细地告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P……在此之前我想问一句。\x01",
            "你们是不是游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P我说的话是不是牵涉到什么案件？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F现在还不能断定。\x01",
            "不过，相关联的可能性还是有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我知道了……\x01",
            "既然是这样，我一定会协助你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P前天晚上……\x01",
            "也就是我在小艇上夜钓的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P因为和努西苦战了一整天，\x01",
            "累得不行了所以想回旅馆休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P天色也已经晚了，\x01",
            "住宿的客人也都休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F请等一下。\x01",
            "……你说的『努西』是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(
        0x8,
        "#5P#3S你可要认真听好了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P所谓的努西，\x01",
            "是生活在这个瓦雷利亚湖的\x01",
            "一种十分巨大的鱼精。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P十年来，努西一直都是\x01",
            "我们这些钓鱼爱好者最热衷的话题，\x01",
            "但它同时也是一种让人难以捉摸的鱼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#522F（不妙……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（不小心让他兴致高昂起来了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F有、有这么厉害的鱼吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#5P对啊，要知道这五年来，\x01",
            "我一直在追踪那家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过，那家伙的脾性反复无常，\x01",
            "一时游到这来一时游到那去，\x01",
            "一时吃这种鱼饵一时吃那种鱼饵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P最近，我听说那家伙在这附近出现，\x01",
            "就急忙从王都追了过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵，多么狂热的激情啊。\x01",
            "对于你的心情我非常地理解。\x02\x03",
            "若是看到了中意的东西，\x01",
            "我也一定会想尽办法得到它。\x02\x03",
            "譬如说『格兰·夏利拿』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F那样也叫得到吗？\x01",
            "应该是不问自取偷偷喝完才对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F咳咳……回到正题吧。\x02\x03",
            "#020F那么罗伊德先生，\x01",
            "你夜钓回来之后又怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P啊，啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P之后，我就把小艇放好，\x01",
            "接着正要走回旅馆睡觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P就在那时，我看到了奇怪的二人组合。\x01",
            "他们从旅馆出来，走到外面的街道上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F走到街道上……\x01",
            "而且是在深夜的时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P啊啊，我不会看错的。\x01",
            "就是走到安塞尔新街那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我本来以为他们\x01",
            "是外出游玩晚归的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过深更半夜才回来也太奇怪了吧。\x01",
            "所以第二天，我向旅馆的人打听了一下，\x01",
            "不过大家都说不认识这些家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P当时我以为自己看到了幽灵，\x01",
            "不禁感觉背后发寒。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#580F幽、幽灵……\x02\x03",
            "会、会出现吗？在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P哈哈，我看到的是两人一起，\x01",
            "而且还是一男一女的年轻组合呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P或许那两人是一对得不到\x01",
            "身边的人承认因而徇情的恋人……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#504F啊～～～别、别再说了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#027F哎呀哎呀。\x01",
            "你还是怕听到幽灵这类的话题啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F就是越害怕才越想听嘛，\x01",
            "怪谭之类的，还有不可思议的故事之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F呵呵，看艾丝蒂尔君\x01",
            "害怕得尖叫起来的样子，\x01",
            "真是越看越可爱，越看越动人。\x02\x03",
            "简直就像在寒风中战栗的小猫㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x101, 0x104, 800)

    ChrTalk(
        0x101,
        "#009F#5P哼！再说这种话就小心你的门牙！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P哈哈哈……\x01",
            "幽灵什么的只是开玩笑而已。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BF2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BF2)

    def lambda_1C00():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C00)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x8,
        (
            "#5P当时我还不敢肯定，\x01",
            "不过那对男女应该不是情侣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P因为我看到那个女子穿着很怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F穿着很怪……这怎么说呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我只是看到背影，\x01",
            "也不敢肯定有没有看错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P不过看样子她穿的就是校服。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F校服？难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F杰尼丝王立学院的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P呵呵，你们知道得很清楚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我的外甥女也在那学校念书，\x01",
            "所以我看得出那就是王立学院的校服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F原来如此……\x01",
            "终于知道所谓的奇怪家伙是谁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F怪不得被人叫做奇怪的家伙！\x01",
            "肯定是那个嚣张的男人婆！\x02\x03",
            "总算抓到你的尾巴了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P怎么了……\x01",
            "难道你们认识他们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P我觉得那两个人选择在\x01",
            "深夜出现可能是出于什么目的吧，\x01",
            "这一点你们也最好注意一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P对了，我还听他们说过\x01",
            "今天半夜会再来这里一次的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F啊？真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P对对，那个年轻男子亲口说过，\x01",
            "两天后还会再来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P他的口气十分认真，让我印象很深。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F原来如此……\x02\x03",
            "这是很重要的线索啊。\x01",
            "感谢你的合作，之后就交给我们吧。\x02\x03",
            "我们绝对会好好利用这些线索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P呼，太好了……\x01",
            "有你这句话我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P突然感觉如释重负啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P……这下可安心了。\x01",
            "我又可以安安稳稳地钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P这次不会让你逃掉的！\x01",
            "各位朋友，我这就先失陪了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22D1():

        label("loc_22D1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22D1")

    QueueWorkItem2(0x101, 1, lambda_22D1)

    def lambda_22E2():

        label("loc_22E2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22E2")

    QueueWorkItem2(0x102, 1, lambda_22E2)

    def lambda_22F3():

        label("loc_22F3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22F3")

    QueueWorkItem2(0x103, 1, lambda_22F3)

    def lambda_2304():

        label("loc_2304")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2304")

    QueueWorkItem2(0x104, 1, lambda_2304)
    OP_8E(0x8, 0xFFFF59C0, 0xFFFFF830, 0xA8CA, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFF7270, 0xFFFFF830, 0xBEBE, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)

    ChrTalk(
        0x101,
        (
            "#506F#5P好一个钓鱼迷呢……\x01",
            "这样的集中力我们还真是比不上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个所谓的『钓公师团』，\x01",
            "不知道是一个什么样的组织呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(
        0x104,
        (
            "#033F听到现在，\x01",
            "我连那对男女是什么来头也还没搞清楚。\x02\x03",
            "究竟你们在调查什么事情，\x01",
            "可以向我详细地解释一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(
        0x103,
        (
            "#020F也对。\x01",
            "事情大致是这样的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雪拉扎德向奥利维尔讲解了关于\x01",
            "在洛连特出现的空贼团少女乔丝特的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x104,
        (
            "#030F原来如此……还真是\x01",
            "踏破铁鞋无觅处，得来全不费功夫。 \x02\x03",
            "这么说，今天晚上有好戏看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是啊……\x02\x03",
            "为了慎重起见，\x01",
            "我们也要租一间房间落脚比较好。\x02\x03",
            "而且必须等到今天半夜才能行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P嗯。\x01",
            "我们回柜台那里去吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_283F")

    label("loc_2659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C8")
    OP_A2(0x2)
    OP_A2(0x369)

    NpcTalk(
        0xFE,
        "拿着钓鱼竿的男人",
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F那个～能打扰一下吗？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "拿着钓鱼竿的男人",
        (
            "……………………………\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#023F（啊呀，没有反应呢……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（看上去他的精神很集中啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F（……原来如此。\x01",
            "　这就是所谓的钓鱼狂人啊。）\x02\x03",
            "#035F（呵呵，真是一个有趣的人啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F（你有立场说别人吗……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_27C8")


    NpcTalk(
        0xFE,
        "拿着钓鱼竿的男人",
        (
            "……………………………\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "男人集中精力在钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_283F")

    TalkEnd(0x8)
    Return()

    # Function_4_4A6 end

    def Function_5_2843(): pass

    label("Function_5_2843")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293E")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "这个旅馆真是适合我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "周围的景色也很优美，\x01",
            "料理也相当美味哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "假如能在这里住下去是最好不过了，\x01",
            "真是好得不会让人舍得离开这里半步啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "已经在这里住了好几天了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29AB")

    label("loc_293E")


    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "这个旅馆真是适合我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "周围的景色也很优美，\x01",
            "料理也相当美味哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AB")

    TalkEnd(0x9)
    Return()

    # Function_5_2843 end

    def Function_6_29AF(): pass

    label("Function_6_29AF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A42")

    ChrTalk(
        0xFE,
        (
            "下午打算和母亲\x01",
            "一起在湖上划划船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还能够顺便消消食。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A96")

    label("loc_2A42")


    ChrTalk(
        0xFE,
        (
            "嗯，怎么说呢，\x01",
            "这里的风真的很清爽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里散步\x01",
            "的确让人心旷神怡啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A96")

    TalkEnd(0xA)
    Return()

    # Function_6_29AF end

    def Function_7_2A9A(): pass

    label("Function_7_2A9A")

    TalkBegin(0xC)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2ABF")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2ADA")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AD5")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2ADA")

    label("loc_2AD5")

    SetChrSubChip(0xFE, 2)

    label("loc_2ADA")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xC,
        (
            "#014F你不是去钓鱼吗？\x02\x03",
            "说到钓鱼的场所，\x01",
            "我想那个码头应该很不错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F哼……\x01",
            "约修亚你也来钓一下嘛。\x02\x03",
            "你的技术不是也不错嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#019F我可不像你那么熟练。\x02\x03",
            "#010F不过让我在这里\x01",
            "看一下你平时修行的成果也好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xC)
    Return()

    # Function_7_2A9A end

    def Function_8_2C05(): pass

    label("Function_8_2C05")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-12880, 0, 26810, 0)
    OP_6B(5900, 0)
    OP_6C(45000, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    SetChrPos(0x101, -9345, 0, 78200, 180)
    SetChrPos(0x102, -10370, 0, 78100, 180)
    SetChrPos(0x104, -8638, 0, 79300, 180)
    SetChrPos(0x103, -9788, 0, 79400, 180)

    def lambda_2C86():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C86)
    Sleep(1000)

    def lambda_2C9B():
        OP_6D(-9385, 0, 77797, 9000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C9B)
    OP_6B(3000, 9000)
    StopSound(0x9470, 0x186A0, 0x1F40)

    ChrTalk(
        0x101,
        (
            "#000F#3P这里就是瓦雷利亚湖的北岸吧……\x02\x03",
            "果然是个气氛不错的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#1P是啊，住宿环境也相当好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#2P我之前因为工作关系也在这里住过。\x02\x03",
            "美酒香醇、住所一流。\x01",
            "确实是个无可挑剔的休闲胜地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#3P嗯，这我也知道。\x01",
            "可我们毕竟不是来度假的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(
        0x104,
        (
            "#033F#4P哎呀，不是吗？\x01",
            "可我确实有这个意思啊。\x02\x03",
            "#035F白天，躺在微摇的小艇上小憩，\x01",
            "夜晚，品尝各式各样的美酒佳肴……\x02\x03",
            "人生最惬意的假期莫过于此。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)
    TurnDirection(0x102, 0x104, 400)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        "#009F#3P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#027F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F#4P哈·哈·哈。\x01",
            "开个玩笑而已嘛。\x02\x03",
            "享受假期无论何时都可以，\x01",
            "现在还是先享受对付空贼……\x02\x03",
            "我奥利维尔，\x01",
            "可是一个很会分辨轻重缓急的人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#3P这可不是什么\x01",
            "享受不享受的问题啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#2P呵呵，别管他了。\x01",
            "让他一个人慢慢享受到发烂好了。\x02\x03",
            "老伯说的那位钓友就在旅馆落脚，\x01",
            "我们还是快点进去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P嗯，就是前天深夜目击到\x01",
            "可疑人物的那位旅馆客人。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x38, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_8_2C05 end

    def Function_9_31C8(): pass

    label("Function_9_31C8")

    EventBegin(0x0)
    OP_6D(1920, -2000, 40480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, -5540, 500, 43050, 180)
    SetChrPos(0x102, -5540, 500, 43050, 180)
    FadeToBright(1500, 0)
    OP_0D()

    def lambda_3239():
        OP_8E(0xFE, 0x3CA, 0xFFFFF830, 0xA60E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3239)
    Sleep(800)

    def lambda_3259():
        OP_8E(0xFE, 0x3CA, 0xFFFFF830, 0xA60E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3259)
    WaitChrThread(0x101, 0x1)

    def lambda_3279():
        OP_6D(1490, -2000, 38380, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3279)

    def lambda_3291():
        OP_8E(0xFE, 0x8D4, 0xFFFFF830, 0x9B6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3291)
    WaitChrThread(0x102, 0x1)

    def lambda_32B1():
        OP_8E(0xFE, 0x668, 0xFFFFF830, 0xA104, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32B1)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x102, 0x3)

    ChrTalk(
        0x101,
        (
            "#004F#1P呜哇～\x01",
            "#001F这里的风景好美啊。\x02\x03",
            "感觉湖水好像在发光一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F据说王都就在湖的对岸。\x01",
            "不过现在雾气比较大，暂时看不到。\x02\x03",
            "不愧为王国最大的湖啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P嗯，在这里钓鱼的话，\x01",
            "肯定会好玩得不得了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不如试一下吧？\x01",
            "难得这里的气氛这么好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#501F#1P嗯，说的也是。\x02\x03",
            "#501F那约修亚你玩什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F至于我嘛，嗯……\x02\x03",
            "我这里有本很想看的书，\x01",
            "所以会在那边的座位上呆一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#1P咦……看书一点都不好玩。\x02\x03",
            "是男孩子的话，\x01",
            "就应该多运动运动才对嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F啊哈哈……\x01",
            "运动方面交给你就行了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3636():

        label("loc_3636")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_3636")

    QueueWorkItem2(0x101, 1, lambda_3636)
    OP_8C(0x102, 270, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_8E(0x102, 0xFFFFE980, 0x1F4, 0xA708, 0xBB8, 0x0)
    SetChrChipByIndex(0xC, 5)
    SetChrPos(0xC, -6920, 700, 41300, 90)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    SetChrPos(0x101, 2260, -2000, 39790, 225)
    TurnDirection(0x101, 0xC, 0)

    ChrTalk(
        0x101,
        (
            "#007F#1P嘁……\x01",
            "约修亚真没意思。\x02\x03",
            "#006F算了算了。\x01",
            "还是马上挑一个场地吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_6D(0, -2000, 35324, 1000)

    ChrTalk(
        0x101,
        (
            "#006F嗯……\x01",
            "栈桥周围的环境好像比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x33F)
    EventEnd(0x0)
    Return()

    # Function_9_31C8 end

    def Function_10_37A2(): pass

    label("Function_10_37A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4E")
    ClearMapFlags(0x1)
    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#006F嗯……\x01",
            "还是觉得这里最好呢。\x02\x03",
            "呵呵呵，还是快点开始吧？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【开始钓鱼】\x01",      # 0
            "【再等一下】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_388E"),
        (0, "loc_390C"),
        (SWITCH_DEFAULT, "loc_4A4C"),
    )


    label("loc_388E")


    ChrTalk(
        0x101,
        (
            "#000F唔……\x01",
            "虽然觉得这里不错……\x02\x03",
            "还是去向旅馆的人\x01",
            "打听打听有没有更好的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A4C")

    label("loc_390C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_END)), "loc_49DD")
    OP_8E(0x101, 0xFFFFF48E, 0xFFFFF84E, 0x7EF4, 0x7D0, 0x0)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x1, 0x2)

    def lambda_3939():
        OP_6D(-3320, -1970, 30110, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3939)

    def lambda_3951():
        OP_6C(225000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3951)

    def lambda_3961():
        OP_6B(3290, 3500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3961)

    def lambda_3971():
        OP_67(0, 9780, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3971)
    Sleep(3500)

    label("loc_3988")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49C0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ACF")

    ChrTalk(
        0x101,
        "#000F那么，要不要换个方向呢？\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【换】\x01",        # 0
            "【不换】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A48"),
        (1, "loc_3AC9"),
        (SWITCH_DEFAULT, "loc_3ACC"),
    )


    label("loc_3A48")

    ClearChrFlags(0x101, 0x2)

    def lambda_3A53():
        OP_6D(-2930, -1970, 32500, 1200)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3A53)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_96(0x101, 0xFFFFF48E, 0xFFFFF84E, 0x7EF4, 0x258, 0xBB8)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F嗯～\x01",
            "往哪个方向钓鱼比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ACC")

    label("loc_3AC9")

    Jump("loc_3ACC")

    label("loc_3ACC")

    Jump("loc_3B47")

    label("loc_3ACF")

    OP_8C(0x101, 225, 400)
    Sleep(400)
    OP_8C(0x101, 135, 400)
    Sleep(400)
    OP_8C(0x101, 180, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F对了，在这栈桥钓鱼的话，\x01",
            "面向哪个方向比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D78")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【位于西侧的栈桥周围】\x01",            # 0
            "【太阳照耀下的南侧湖面】\x01",          # 1
            "【东侧的林木树枝延伸处附近】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C1F"),
        (1, "loc_3C6B"),
        (2, "loc_3CB7"),
        (SWITCH_DEFAULT, "loc_3D03"),
    )


    label("loc_3C1F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C2F():
        OP_8C(0x101, 253, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C2F)

    def lambda_3C3D():
        OP_6C(278000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C3D)

    def lambda_3C4D():
        OP_6B(3290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C4D)
    OP_6D(-6980, -2200, 31000, 2000)
    Jump("loc_3D03")

    label("loc_3C6B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C7B():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C7B)

    def lambda_3C89():
        OP_6C(232000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C89)

    def lambda_3C99():
        OP_6B(3290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C99)
    OP_6D(-3010, -2200, 29250, 2000)
    Jump("loc_3D03")

    label("loc_3CB7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3CC7():
        OP_8C(0x101, 100, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CC7)

    def lambda_3CD5():
        OP_6C(149000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CD5)

    def lambda_3CE5():
        OP_6B(3290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CE5)
    OP_6D(1790, -2200, 32590, 2000)
    Jump("loc_3D03")

    label("loc_3D03")

    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#006F嗯嗯，大概就选这边吧。\x02\x03",
            "#505F那么，用什么来做饵呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E98")

    label("loc_3D78")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMUL_SAVE), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3DA1"),
        (100, "loc_3DE3"),
        (200, "loc_3E25"),
        (SWITCH_DEFAULT, "loc_3E67"),
    )


    label("loc_3DA1")


    def lambda_3DA7():
        OP_8C(0x101, 253, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DA7)

    def lambda_3DB5():
        OP_6C(278000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DB5)

    def lambda_3DC5():
        OP_6B(3290, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3DC5)
    OP_6D(-6980, -2200, 31000, 1000)
    Jump("loc_3E67")

    label("loc_3DE3")


    def lambda_3DE9():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DE9)

    def lambda_3DF7():
        OP_6C(232000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DF7)

    def lambda_3E07():
        OP_6B(3290, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E07)
    OP_6D(-3010, -2200, 29250, 1000)
    Jump("loc_3E67")

    label("loc_3E25")


    def lambda_3E2B():
        OP_8C(0x101, 100, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E2B)

    def lambda_3E39():
        OP_6C(149000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E39)

    def lambda_3E49():
        OP_6B(3290, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E49)
    OP_6D(1790, -2200, 32590, 1000)
    Jump("loc_3E67")

    label("loc_3E67")


    ChrTalk(
        0x101,
        "#000F这次用什么鱼饵呢？\x02",
    )

    CloseMessageWindow()

    label("loc_3E98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【鱼拟饵】\x01",      # 0
            "【生鱼饵】\x01",      # 1
            "【虫拟饵】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F16"),
        (1, "loc_3F23"),
        (2, "loc_3F30"),
        (SWITCH_DEFAULT, "loc_3F3D"),
    )


    label("loc_3F16")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F3D")

    label("loc_3F23")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F3D")

    label("loc_3F30")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F3D")

    label("loc_3F3D")


    ChrTalk(
        0x101,
        (
            "#001F好～啦，\x01",
            "接下来就可以悠然自得地等鱼上钩了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1500)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 11)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrSubChip(0x101, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FFA")
    SetChrPos(0x101, -2950, -2200, 32080, 225)
    OP_0D()

    def lambda_3FD8():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FD8)

    def lambda_3FE8():
        OP_6D(-4440, -2200, 30770, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FE8)

    label("loc_3FFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4047")
    SetChrPos(0x101, -2960, -2200, 32049, 180)
    OP_0D()

    def lambda_4025():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4025)

    def lambda_4035():
        OP_6D(-2990, -2200, 31970, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4035)

    label("loc_4047")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4094")
    SetChrPos(0x101, -2029, -2200, 32970, 90)
    OP_0D()

    def lambda_4072():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4072)

    def lambda_4082():
        OP_6D(100, -2200, 32640, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4082)

    label("loc_4094")

    OP_22(0x84, 0x0, 0x64)
    OP_99(0x101, 0x0, 0x6, 0x5DC)
    Sleep(400)
    OP_22(0x19, 0x0, 0x64)
    Sleep(1200)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E4")
    Sleep(4000)
    Jump("loc_4120")

    label("loc_40E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F9")
    Sleep(3000)
    Jump("loc_4120")

    label("loc_40F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410E")
    Sleep(5000)
    Jump("loc_4120")

    label("loc_410E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4120")
    Sleep(2000)

    label("loc_4120")

    OP_44(0x101, 0xFF)
    Fade(1000)

    def lambda_412F():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_412F)

    def lambda_413F():

        label("loc_413F")

        OP_99(0xFE, 0x8, 0xC, 0x5DC)
        OP_48()
        Jump("loc_413F")

    QueueWorkItem2(0x101, 3, lambda_413F)
    OP_63(0x101)
    Sleep(700)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#508F太棒了，等到了！\x01",
            "终于有鱼上钩了！\x02\x03",
            "#002F好，接下来就是关键了。\x01",
            "怎么把鱼钓上来才好呢？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【一口气钓上来】\x01",          # 0
            "【再等待一会儿】\x01",          # 1
            "【慢慢地把鱼儿搞累】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#009F好！看看我的绝招！\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42BA"),
        (1, "loc_42E2"),
        (2, "loc_4367"),
        (SWITCH_DEFAULT, "loc_43DE"),
    )


    label("loc_42BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x3, 0x5DC)
    OP_22(0x18, 0x0, 0x64)
    OP_99(0x101, 0x3, 0x1, 0x5DC)
    Jump("loc_43DE")

    label("loc_42E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(300)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(200)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(300)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(200)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    OP_99(0x101, 0x6, 0x3, 0x5DC)
    OP_22(0x18, 0x0, 0x64)
    OP_99(0x101, 0x3, 0x1, 0x5DC)
    Jump("loc_43DE")

    label("loc_4367")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(300)
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    Sleep(100)
    OP_99(0x101, 0x6, 0x4, 0x5DC)
    OP_99(0x101, 0x6, 0x1, 0x5DC)
    OP_9E(0x101, 0x1E, 0x0, 0x3E8, 0x1770)
    OP_99(0x101, 0x1, 0x3, 0x9C4)
    OP_99(0x101, 0x3, 0x1, 0x9C4)
    OP_22(0x18, 0x0, 0x64)
    Jump("loc_43DE")

    label("loc_43DE")

    Sleep(1000)
    OP_99(0x101, 0x10, 0x12, 0x5DC)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (100, "loc_447B"),
        (102, "loc_447B"),
        (112, "loc_447B"),
        (121, "loc_447B"),
        (122, "loc_447B"),
        (220, "loc_447B"),
        (0, "loc_449D"),
        (10, "loc_449D"),
        (20, "loc_449D"),
        (22, "loc_449D"),
        (110, "loc_449D"),
        (111, "loc_449D"),
        (120, "loc_449D"),
        (202, "loc_449D"),
        (210, "loc_449D"),
        (1, "loc_44BB"),
        (12, "loc_44BB"),
        (101, "loc_44BB"),
        (200, "loc_44BB"),
        (212, "loc_44BB"),
        (21, "loc_44DF"),
        (201, "loc_44DF"),
        (211, "loc_44DF"),
        (221, "loc_44DF"),
        (11, "loc_4505"),
        (222, "loc_4505"),
        (2, "loc_452C"),
        (SWITCH_DEFAULT, "loc_454B"),
    )


    label("loc_447B")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "开孔长靴\x07\x00",
            "钓上来了！\x02",
        )
    )

    Jump("loc_454B")

    label("loc_449D")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "胡瓜鱼\x07\x00",
            "钓上来了！\x02",
        )
    )

    Jump("loc_454B")

    label("loc_44BB")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "利贝尔鲫鱼\x07\x00",
            "钓上来了！\x02",
        )
    )

    Jump("loc_454B")

    label("loc_44DF")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "虹鳟鱼\x07\x00",
            "钓上来了！\x02",
        )
    )

    Jump("loc_454B")

    label("loc_4505")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "橙河鱼\x07\x00",
            "钓上来了！\x02",
        )
    )

    Jump("loc_454B")

    label("loc_452C")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "拖鱼\x07\x00",
            "钓上来了！\x02",
        )
    )

    Jump("loc_454B")

    label("loc_454B")

    FadeToBright(300, 0)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (100, "loc_45DF"),
        (102, "loc_45DF"),
        (112, "loc_45DF"),
        (121, "loc_45DF"),
        (122, "loc_45DF"),
        (220, "loc_45DF"),
        (0, "loc_4624"),
        (10, "loc_4624"),
        (20, "loc_4624"),
        (22, "loc_4624"),
        (110, "loc_4624"),
        (111, "loc_4624"),
        (120, "loc_4624"),
        (202, "loc_4624"),
        (210, "loc_4624"),
        (1, "loc_46AE"),
        (12, "loc_46AE"),
        (101, "loc_46AE"),
        (200, "loc_46AE"),
        (212, "loc_46AE"),
        (21, "loc_46DD"),
        (201, "loc_46DD"),
        (211, "loc_46DD"),
        (221, "loc_46DD"),
        (11, "loc_470A"),
        (222, "loc_470A"),
        (2, "loc_4765"),
        (SWITCH_DEFAULT, "loc_4850"),
    )


    label("loc_45DF")

    OP_3E(0x11B, 1)

    ChrTalk(
        0x101,
        "#509F啊，怎么会……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_4624")

    OP_3E(0x3AC, 1)

    ChrTalk(
        0x101,
        (
            "#506F啊呀，\x01",
            "这小鱼还真可爱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_46AE")

    OP_3E(0x3AD, 1)

    ChrTalk(
        0x101,
        "#501F唉，这个就当作热身运动吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_46DD")

    OP_3E(0x3AE, 1)

    ChrTalk(
        0x101,
        "#000F嗯，这个收获还可以。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_470A")

    OP_3E(0x3AF, 1)

    ChrTalk(
        0x101,
        (
            "#508F哇，大鱼啊大鱼啊！\x01",
            "没想到今天收获这么棒⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_4765")

    OP_3E(0x3B0, 1)

    ChrTalk(
        0x101,
        (
            "#001F太好啦～！\x01",
            "很久没有钓到这么大的鱼了。\x02\x03",
            "#507F这么大的鱼，\x01",
            "说不定能打破自己的纪录了。\x02\x03",
            "#502F它一咬钩我就知道\x01",
            "不是条普通的鱼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_4850")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_486A")
    OP_83(0xD, 0x1)

    label("loc_486A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_487A")
    OP_83(0xD, 0x2)

    label("loc_487A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488A")
    OP_83(0xD, 0x3)

    label("loc_488A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_489A")
    OP_83(0xD, 0x4)

    label("loc_489A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48AA")
    OP_83(0xD, 0x5)

    label("loc_48AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48BA")
    OP_83(0xD, 0x6)

    label("loc_48BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48CA")
    OP_83(0xD, 0x7)

    label("loc_48CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48DA")
    OP_83(0xD, 0x8)

    label("loc_48DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48EA")
    OP_83(0xD, 0x9)

    label("loc_48EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48FA")
    OP_83(0xD, 0xA)

    label("loc_48FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_490D")
    Jump("loc_49C0")

    label("loc_490D")

    OP_99(0x101, 0x12, 0x10, 0x5DC)
    Sleep(50)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        (
            "#505F接下来……\x02\x03",
            "要做些什么好呢。\x01",
            "再继续钓鱼吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【继续钓鱼】\x01",      # 0
            "【不再钓了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B8")
    Jump("loc_49C0")

    label("loc_49B8")

    Sleep(100)
    Jump("loc_3988")

    label("loc_49C0")

    OP_A2(0x345)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T1500   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_4A49")

    label("loc_49DD")

    OP_A2(0x346)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "我还没有钓鱼竿呢。\x02\x03",
            "不知道能不能\x01",
            "向旅馆的人借一支呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A49")

    Jump("loc_4A4C")

    label("loc_4A4C")

    EventEnd(0x0)

    label("loc_4A4E")

    Return()

    # Function_10_37A2 end

    def Function_11_4A4F(): pass

    label("Function_11_4A4F")

    EventBegin(0x0)
    FadeToBright(5000, 0)
    OP_6D(-3320, -1970, 30110, 0)
    OP_6C(257000, 0)
    OP_6B(3290, 0)
    OP_67(0, 6980, -10000, 0)
    SetChrPos(0x101, -2930, -1970, 32500, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4850, 1140, 41360, 0)
    OP_64(0x0, 0x1)
    SetChrFlags(0xC, 0x80)

    def lambda_4AC4():
        OP_6D(-3013, -1970, 32740, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4AC4)

    def lambda_4ADC():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4ADC)

    def lambda_4AEC():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4AEC)

    def lambda_4AFC():
        OP_67(0, 11000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4AFC)
    Sleep(5000)

    ChrTalk(
        0x101,
        "#501F啊～已经傍晚了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯！\x01",
            "今天战果累累呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#001F看呀看呀，约修亚。\x01",
            "今天我钓到一条大～鱼呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BC9():
        OP_6D(-4150, 500, 37765, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BC9)

    def lambda_4BE1():
        OP_67(0, 4400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BE1)

    def lambda_4BF9():
        OP_6B(3600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4BF9)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#004F……咦。\x02",
    )

    CloseMessageWindow()

    def lambda_4C20():
        OP_6D(-3850, 500, 42640, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C20)

    def lambda_4C38():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C38)

    def lambda_4C50():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4C50)
    OP_8E(0x101, 0xFFFFF448, 0xFFFFF830, 0x9502, 0x1770, 0x0)
    OP_8E(0x101, 0x5A0, 0xFFFFF830, 0x9966, 0x1770, 0x0)
    OP_8E(0x101, 0x5A0, 0xFFFFF830, 0x9FF6, 0x1770, 0x0)
    OP_8E(0x101, 0xFFFFF0F6, 0x1F4, 0xA690, 0x1770, 0x0)

    ChrTalk(
        0x101,
        "#002F约修亚？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#004F哎呀，这是……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFEFE4, 0x1F4, 0xA433, 0x7D0, 0x0)
    SetChrFlags(0xD, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "《实录·百日战役》\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x331, 1)

    ChrTalk(
        0x101,
        (
            "#501F约修亚忘了拿吗？\x02\x03",
            "这个约修亚，虽说平时做事很稳妥，\x01",
            "不过也经常露出马虎的一面呢～\x02\x03",
            "#001F算了，我先帮他收起来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 225, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#000F话说回来，\x01",
            "约修亚到底跑到哪去了？\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_11_4A4F end

    def Function_12_4E9B(): pass

    label("Function_12_4E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_580A")
    EventBegin(0x0)
    AddParty(0x1, 0xFF)
    SetChrPos(0x102, -44990, -1970, 38500, 180)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 0)

    def lambda_4EE6():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EE6)
    OP_6D(-44640, -1970, 41750, 3000)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -40520, -2000, 48190, 194)

    ChrTalk(
        0x102,
        "#013F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "呀嗬～沉默的少年。\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    OP_8E(0x101, 0xFFFF50BA, 0xFFFFF830, 0xA846, 0xBB8, 0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F怎么站在这里\x01",
            "一动不动地发呆啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FD2():
        OP_8E(0xFE, 0xFFFF5038, 0xFFFFF84E, 0x9ECA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD2)
    TurnDirection(0x102, 0x101, 400)
    OP_6D(-45080, -2000, 39790, 1500)

    ChrTalk(
        0x102,
        (
            "#019F哈哈……\x01",
            "我并没有发呆啊。\x02\x03",
            "#010F已经钓完鱼了吗？\x01",
            "今天玩得很开心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，非常开心。\x01",
            "很久都没有这么痛快了。\x02\x03",
            "#501F啊……对了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFF501A, 0xFFFFF84E, 0x9A4C, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔把《实录·百日战役》拿了出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#006F#2P真是的～说自己想要看书，\x01",
            "看完了却不把书收拾好。\x02\x03",
            "你呀，有时候也挺马虎的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F……啊啊……\x01",
            "刚才把那本书看完了。\x02\x03",
            "#010F觉得眼睛有点累，\x01",
            "于是就在周围走走散一下心。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)
    OP_92(0x101, 0x102, 0x28A, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#007F#2P哼。\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 45, 0)
    OP_8F(0x102, 0xFFFF4E80, 0xFFFFF84E, 0x954C, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        "#014F怎、怎么了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#509F#2P难道你又开始一个人沉思，\x01",
            "想一些乱七八糟的问题？\x02\x03",
            "你这种性格啊，我可是最了解不过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#2P这样很不公平呢！\x02\x03",
            "因为你总会在我失意的时候陪伴着我，\x01",
            "在我悲伤的时候给我安慰。\x02\x03",
            "#003F虽然我也知道，\x01",
            "自己还无法像老爸那样值得依靠……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)

    def lambda_5414():
        OP_6D(-44980, -1970, 39200, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5414)
    OP_8E(0x101, 0xFFFF5196, 0xFFFFF84E, 0x9574, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F#4P不过，我至少还可以像这样呆在你身边。\x01",
            "无论何时何地，我都可以为你分担烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P………………………………\x02\x03",
            "…………抱歉…………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#4P这个时候，\x01",
            "应该是说谢谢才对吧。\x02\x03",
            "#006F虽说约修亚你头脑很聪明，\x01",
            "不过毕竟也有需要别人安慰的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P哈哈，说的也对。\x02\x03",
            "#019F谢谢你，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F#4P嗯嗯，别客气别客气。\x02\x03",
            "#004F啊……对了。\x02\x03",
            "#001F吹一曲口琴给我听吧。\x01",
            "就当作是报答我的礼物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P如你所愿……\x02\x03",
            "#010F『星之所在』，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#4P嗯。\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_56B3():
        OP_69(0x102, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_56B3)

    def lambda_56C1():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_56C1)
    OP_8F(0x101, 0xFFFF52F4, 0xFFFFF84E, 0x9524, 0x3E8, 0x0)
    Sleep(500)
    OP_96(0x101, 0xFFFF5452, 0xFFFFF9C0, 0x951A, 0x2BC, 0x1388)
    SetChrChipByIndex(0x101, 9)
    WaitChrThread(0x0, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x102, 8)
    Sleep(1000)
    OP_0D()

    def lambda_5720():

        label("loc_5720")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_5720")

    QueueWorkItem2(0x102, 1, lambda_5720)
    Sleep(500)
    OP_1D(0x46)
    Sleep(5000)
    SetChrPos(0xF, -30770, -3000, 32509, 273)
    SetChrFlags(0xF, 0x40)
    OP_A1(0xF, 0x3)
    OP_72(0x3, 0x4)
    Sleep(100)
    Fade(1000)
    OP_44(0x8, 0xFF)
    SetChrBattleFlags(0x8, 0x20)
    SetChrPos(0x8, -29670, -2900, 32420, 150)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    OP_6D(-29670, -1970, 32420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(213000, 0)
    OP_6E(307, 0)
    Sleep(2000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 2)
    Sleep(3000)
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_580A")

    Return()

    # Function_12_4E9B end

    def Function_13_580B(): pass

    label("Function_13_580B")

    SetChrFlags(0x8, 0x80)
    EventBegin(0x0)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x102, -45440, -1970, 38220, 90)
    SetChrPos(0x101, -43950, -1600, 38170, 270)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x102, 8)

    def lambda_584E():

        label("loc_584E")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_584E")

    QueueWorkItem2(0x102, 1, lambda_584E)
    OP_6D(-44980, -1970, 39200, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_21()
    OP_44(0x102, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F#4P啊……怎么说呢。\x02\x03",
            "总觉得这首曲子……\x01",
            "在夕阳之下倾听的时候，\x01",
            "有种让人忍不住流泪的悲伤意境。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x102, 180, 400)
    OP_1D(0x30)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#013F#1P………………………………\x02\x03",
            "你还是一样……\x01",
            "什么都没有问过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#4P………………………………\x02\x03",
            "#506F啊哈……我们不是约定了吗。\x02\x03",
            "直到你愿意向我倾诉之前，\x01",
            "我什么都不会问的。\x02\x03",
            "#006F而且……已经五年了。\x01",
            "我们两个，不是一直都相处得很好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P是啊……已经五年了。\x02\x03",
            "为什么你能什么都不问？\x01",
            "就这样接纳我，和我一起生活呢？\x02\x03",
            "#015F那一天，被父亲从外面抱回来、\x01",
            "满身伤痕的孩子……\x02\x03",
            "对一个从没讲过自己的过去、\x01",
            "来历不明的男孩……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 200)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#012F#1P……为什么你们可以\x01",
            "这么宽容地接纳这样一个人……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)

    def lambda_5BBC():
        OP_96(0xFE, 0xFFFF52F4, 0xFFFFF84E, 0x9524, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BBC)

    ChrTalk(
        0x101,
        "#501F#4P嘿咻。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    def lambda_5BF4():
        OP_6D(-45440, -1970, 38220, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BF4)
    OP_8E(0x101, 0xFFFF5196, 0xFFFFF84E, 0x9574, 0x3E8, 0x0)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#006F这是理所当然的啊。\x02\x03",
            "因为约修亚是我们的家人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F之前不是跟你说过吗。\x01",
            "我呢，其实一直以来\x01",
            "都非常清楚你的事情哦。\x02\x03",
            "#007F比如说喜欢看书啦，\x01",
            "平时有空就喜欢摆弄武器啦……\x02\x03",
            "虽然平时待人彬彬有礼，\x01",
            "不过也一直与别人保持距离……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F等、等一下……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#001F不过，你真的很会照顾人哦，\x01",
            "应该说是标准的居家型好男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F当然了，在我们相识之前，\x01",
            "你去过哪里做过什么我都不清楚。\x02\x03",
            "不过不单是你，\x01",
            "就连老爸以前的事情我也不是很清楚。\x02\x03",
            "#006F就算这样，我和老爸依旧是一家人，\x01",
            "这一点永远都不会改变啊。\x02\x03",
            "我很清楚老爸的性格、爱好，\x01",
            "还有料理的口味。\x02\x03",
            "正因为朝夕相处、共同生活，\x01",
            "才能够亲身感觉到这一切。\x02\x03",
            "#001F约修亚对我来说，也是一样的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F………………………………\x02\x03",
            "#011F我真的……说不过你。\x02\x03",
            "从最初见面时就知道了……\x01",
            "就在你用力使出飞踢的那一刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x02\x03",
            "我、我有做过这种事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F嗯，而且是对一个受伤的男孩。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊、啊哈哈……\x01",
            "小时候不懂事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是是。\x02\x03",
            "#015F喂，艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F怎么了，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这个案件，无论如何也要解决。\x02\x03",
            "虽然还不知道\x01",
            "父亲是不是真的被抓了……\x02\x03",
            "但我们一定要查个水落石出，绝对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯……\x02\x03",
            "那当然啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵……\x01",
            "是时候回去了。\x02\x03",
            "旅馆已经准备好饭菜了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，我饿得肚子咕咕响呢。\x02\x03",
            "#006F那我们就好好地大吃一顿，\x01",
            "为今晚的作战行动做好准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrPos(0x101, -44940, -2000, 42440, 0)
    SetChrPos(0x102, -44940, -2000, 42440, 0)
    OP_69(0x101, 0x0)
    OP_A2(0x34C)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_1D(0xF)
    EventEnd(0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearMapFlags(0x10000000)
    Return()

    # Function_13_580B end

    def Function_14_63B3(): pass

    label("Function_14_63B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67D3")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x34D)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F啊，忘记了。\x02",
    )

    CloseMessageWindow()

    def lambda_6405():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6405)

    def lambda_6413():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6413)
    OP_6D(-30910, -850, 52160, 1500)

    ChrTalk(
        0x101,
        "#000F约修亚，这本书……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F啊啊……\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0x102, 0x384, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔把《实录·百日战役》拿了出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        (
            "#010F我已经看完了。\x02\x03",
            "而且这本书挺占地方的，怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "『我也想看一下。』\x01",        # 0
            "『不如送给别人吧。』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65DB"),
        (1, "loc_674C"),
        (SWITCH_DEFAULT, "loc_67D1"),
    )


    label("loc_65DB")


    ChrTalk(
        0x101,
        (
            "#501F看起来是本很深奥的书啊。\x01",
            "不过我也想看一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我想对你来说没什么难懂的，\x01",
            "因为有很多内容你应该都知道了。\x02\x03",
            "艾丝蒂尔，就试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好的，我挑战一下吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "《实录·百日战役》\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x349)
    Jump("loc_67D1")

    label("loc_674C")

    OP_3F(0x331, 1)

    ChrTalk(
        0x101,
        (
            "#501F送给谁呢？\x01",
            "还是扔掉吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊……就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67D1")

    label("loc_67D1")

    EventEnd(0x0)

    label("loc_67D3")

    Return()

    # Function_14_63B3 end

    def Function_15_67D4(): pass

    label("Function_15_67D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_688A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_682C")
    OP_A2(0x3)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "这边是街道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6871")

    label("loc_682C")


    ChrTalk(
        0x101,
        (
            "#007F……他不可能一个人出去散步吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6871")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    EventEnd(0x0)
    Jump("loc_6A07")

    label("loc_688A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_690A")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "这边是街道。\x02\x03",
            "真是的，\x01",
            "约修亚到底跑到哪里去了？\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    EventEnd(0x0)
    Jump("loc_6A07")

    label("loc_690A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A07")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69A2")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，你去哪儿？\x02\x03",
            "我们该回房间了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明～白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69EC")

    label("loc_69A2")


    ChrTalk(
        0x102,
        (
            "#010F这边是街道。\x02\x03",
            "我们回房间去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69EC")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6A07")

    Return()

    # Function_15_67D4 end

    SaveToFile()

Try(main)
