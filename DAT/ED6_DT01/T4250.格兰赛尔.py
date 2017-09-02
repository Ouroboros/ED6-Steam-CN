from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4250   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4250.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '凯诺娜上尉',                           # 9
        '茜亚',                                 # 10
        '理查德上校',                           # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '特务兵',                               # 16
        '王国军士兵',                           # 17
        '王国军士兵',                           # 18
        '特务兵',                               # 19
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
        'ED6_DT07/CH02100 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH02030 ._CH',             # 02
        'ED6_DT07/CH02460 ._CH',             # 03
        'ED6_DT07/CH02230 ._CH',             # 04
        'ED6_DT07/CH02240 ._CH',             # 05
        'ED6_DT07/CH01610 ._CH',             # 06
        'ED6_DT07/CH00177 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02100P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH02030P._CP',             # 02
        'ED6_DT07/CH02460P._CP',             # 03
        'ED6_DT07/CH02230P._CP',             # 04
        'ED6_DT07/CH02240P._CP',             # 05
        'ED6_DT07/CH01610P._CP',             # 06
        'ED6_DT07/CH00177P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21430,
        Z                   = 750,
        Y                   = -3970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2750,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2750,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 9000,
        Y                   = 29350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclEvent(
        X                   = 4010,
        Y                   = 10000,
        Z                   = 16219,
        Range               = -4330,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0x2D78,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 21060,
        Y                   = -1000,
        Z                   = -1860,
        Range               = 19780,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE854,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 4290,
        Y                   = -1000,
        Z                   = -25590,
        Range               = -4690,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFA33A,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 8000,
        Z                   = 30350,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_2D2",          # 00, 0
        "Function_1_36B",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_458",          # 03, 3
        "Function_4_18D4",         # 04, 4
        "Function_5_1A51",         # 05, 5
        "Function_6_1AB9",         # 06, 6
        "Function_7_251B",         # 07, 7
        "Function_8_2544",         # 08, 8
        "Function_9_3BF9",         # 09, 9
        "Function_10_3C72",        # 0A, 10
        "Function_11_3E04",        # 0B, 11
        "Function_12_40C9",        # 0C, 12
        "Function_13_4249",        # 0D, 13
        "Function_14_42B7",        # 0E, 14
        "Function_15_4347",        # 0F, 15
    )


    def Function_0_2D2(): pass

    label("Function_0_2D2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2E2"),
        (108, "loc_2F8"),
        (SWITCH_DEFAULT, "loc_30B"),
    )


    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F5")
    OP_A2(0x639)
    Event(0, 3)

    label("loc_2F5")

    Jump("loc_30B")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_308")
    Event(0, 6)

    label("loc_308")

    Jump("loc_30B")

    label("loc_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    SetChrChipByIndex(0x0, 3)
    SetChrChipByIndex(0x1, 4)
    SetChrChipByIndex(0x138, 5)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A")
    ClearChrFlags(0x12, 0x80)

    label("loc_36A")

    Return()

    # Function_0_2D2 end

    def Function_1_36B(): pass

    label("Function_1_36B")

    OP_71(0xC, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_380")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_380")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_36B end

    def Function_2_38A(): pass

    label("Function_2_38A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_442")

    label("loc_3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_442")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_442")

    label("loc_3E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_442")

    label("loc_3FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_442")

    label("loc_413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_442")

    label("loc_42C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_442")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_457")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_442")

    label("loc_457")

    Return()

    # Function_2_38A end

    def Function_3_458(): pass

    label("Function_3_458")

    EventBegin(0x0)
    SetChrPos(0x102, 520, 0, -22530, 0)
    SetChrPos(0x101, -1610, 0, -22470, 0)
    SetChrPos(0x108, -290, 0, -21870, 0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(-70, 14350, 22560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(12000, 0)
    OP_6E(280, 0)

    def lambda_4DA():
        OP_6D(-8920, 10250, -21440, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DA)

    def lambda_4F2():
        OP_67(0, 8000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F2)

    def lambda_50A():
        OP_6B(3920, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_50A)

    def lambda_51A():
        OP_6C(44000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51A)

    def lambda_52A():
        OP_6E(280, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_52A)
    FadeToBright(2000, 0)
    Sleep(10000)
    Fade(1000)
    OP_6D(30, 0, -22200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F哇～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然知道王城是个很华丽的地方……\x02\x03",
            "但是，这比至今为止见过的房间\x01",
            "都要豪华不知道多少倍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F不只是豪华，\x01",
            "还蕴含着历史的传统和壮丽。\x02\x03",
            "#070F到处都充满着浓厚的\x01",
            "古代王国的传统风格呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 770, 0, -9870, 180)
    SetChrPos(0x9, -280, 0, -9260, 180)

    NpcTalk(
        0x8,
        "女人的声音",
        "欢迎来到格兰赛尔城。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "女人的声音",
        (
            "请问你们就是\x01",
            "金先生一行人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_745():
        OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0xFFFFB41A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_745)

    def lambda_760():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0xFFFFB758, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_760)
    OP_6D(130, 0, -20310, 3000)

    ChrTalk(
        0x101,
        "#509F（哎哎……是凯诺娜上尉……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（虽然也不是没有预料到……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，没错。\x01",
            "我们受了公爵大人的邀请。\x02\x03",
            "请问……你是？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#182F呵呵，忘了自我介绍。\x02\x03",
            "我是担任格兰赛尔城警卫工作的\x01",
            "情报部的凯诺娜上尉。\x02\x03",
            "恭喜金先生你们获得武术大会的优胜。\x01",
            "　\x02\x03",
            "我看了你们的比赛，\x01",
            "真是威风凛凛、令人叹为观止啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F哎呀～真是过奖了。\x02\x03",
            "我倒觉得，如此年轻美丽的女性\x01",
            "能当上军队的上尉才是让人吃惊呢。\x02\x03",
            "一定是非常优秀才能做到这样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#184F哎呀……金先生您真会说话。\x01",
            "　\x02\x03",
            "#180F哦，这两位不是年轻的游击士嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……！\x02",
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
            "#180F艾丝蒂尔·布莱特，\x01",
            "以及约修亚·布莱特。\x02\x03",
            "蔡斯事件之后我们就没见过面吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F……嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F确实很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#181F虽然很遗憾，\x01",
            "不过博士的事件还没有完全解决。\x01",
            "　\x02\x03",
            "博士和他的孙女儿\x01",
            "好像被一伙不知名的暴徒绑架了呢。\x02\x03",
            "#188F艾丝蒂尔你们\x01",
            "有没有这方面的线索呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F那、那个。\x01",
            "一点也不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F那个事情交给了正游击士去处理，\x01",
            "然后我们就来王都了。\x02\x03",
            "之后的事情就没再听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#188F是吗……呵呵。\x01",
            "那真是遗憾呢。\x02\x03",
            "不过，只要借助情报部的力量，\x01",
            "逮捕绑架犯也只是时间上的问题了。\x02\x03",
            "就请你们瞧着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F（这、这只母狐狸～……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F我知道了。\x02\x03",
            "博士和他的孙女是我们的好朋友，\x01",
            "所以请你们一定要把他们救出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#181F那是当然的了……\x02\x03",
            "#182F好了，晚宴快开始了。\x01",
            "这就把你们安排到各自的房间去吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "#182F#2P茜亚小姐……\x01",
            "接下来就交给你了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "#5P是……\x01",
            "我会好好照顾客人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F#2P还有，麻烦你记住一点……\x02\x03",
            "不要对这些客人没有礼貌，\x01",
            "说些不该说的话。\x02\x03",
            "记住了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P是、是的……\x01",
            "我明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#188F#2P哼哼，这样就好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)
    TurnDirection(0x8, 0x108, 400)

    ChrTalk(
        0x8,
        (
            "#182F那么各位，\x01",
            "希望你们今晚过得愉快。\x02\x03",
            "我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F98():

        label("loc_F98")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_F98")

    QueueWorkItem2(0x108, 1, lambda_F98)

    def lambda_FA9():

        label("loc_FA9")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_FA9")

    QueueWorkItem2(0x101, 1, lambda_FA9)

    def lambda_FBA():

        label("loc_FBA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_FBA")

    QueueWorkItem2(0x102, 1, lambda_FBA)
    OP_8C(0x8, 45, 400)
    OP_8E(0x8, 0x730, 0x0, 0xFFFFC2F2, 0x7D0, 0x0)

    def lambda_FE6():
        OP_8E(0xFE, 0x1CC0, 0x0, 0xFFFFD88C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FE6)
    Sleep(1500)

    ChrTalk(
        0x108,
        "#070F唔～感觉这个女人还不错嘛。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#509F金先生，你的兴趣真是奇怪啊……\x02\x03",
            "那个母狐狸，有什么地方好啊？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#014F那样的人，是金先生喜欢的类型吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#071F#5P哈哈，只是外表那样而已，\x01",
            "但其实本质上还是很纯情的哦。\x02\x03",
            "就是这一点最吸引人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不行了……\x02\x03",
            "#006F不管怎么样都好啦。\x01",
            "金先生，你真像个大叔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#072F#5P#5S……（受到打击）\x02",
    )

    CloseMessageWindow()

    def lambda_124F():
        OP_6D(-240, 0, -20830, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_124F)
    OP_8E(0x9, 0xFFFFFEFC, 0x0, 0xFFFFB186, 0x5DC, 0x0)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(
        0x9,
        "#5P我、我说……\x02",
    )

    CloseMessageWindow()

    def lambda_1293():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1293)

    def lambda_12A1():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A1)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#506F啊，不好意思～～\x02\x03",
            "现在可以带我们去看看房间吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P好的……\x01",
            "我来带路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P还没做自我介绍，\x01",
            "我是这里的侍女，名叫茜亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P从晚宴开始到明天，\x01",
            "由我来照顾你们的起居生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P如果各位客人有什么需要，\x01",
            "随时告诉我就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F啊啊，拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，现在带我们去房间吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P啊，好的。\x01",
            "各位的房间在二楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 315, 400)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_8E(0x108, 0xFFFFFF10, 0x0, 0xFFFFAEA2, 0xBB8, 0x0)
    OP_6A(0x108)
    OP_43(0x108, 0x1, 0x0, 0x4)
    Sleep(150)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(12000)
    OP_66(0x0)
    WaitChrThread(0x9, 0x1)

    def lambda_14FB():
        OP_6E(196, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14FB)

    def lambda_150B():
        OP_8E(0xFE, 0x32, 0x2328, 0x5A6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_150B)
    WaitChrThread(0x108, 0x1)

    def lambda_152B():
        OP_8E(0xFE, 0x410, 0x2328, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_152B)
    WaitChrThread(0x101, 0x1)

    def lambda_154B():
        OP_8E(0xFE, 0xFFFFFB96, 0x2328, 0x524E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_154B)
    WaitChrThread(0x102, 0x1)

    def lambda_156B():
        OP_8E(0xFE, 0xFFFFFF92, 0x2328, 0x4FBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_156B)
    ClearMapFlags(0x1)
    OP_6D(4840, 9000, 32350, 3000)

    ChrTalk(
        0x101,
        "#004F#5S哇～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F那个巨大的吊灯，真是豪华绚丽呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，不要大声喧哗。\x02\x03",
            "#010F对了，那边是……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1625():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1625)

    def lambda_1633():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1633)

    def lambda_1641():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1641)
    OP_8C(0x9, 180, 400)

    ChrTalk(
        0x9,
        "#5P是『谒见室』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P艾莉茜雅女王陛下\x01",
            "就是在这里会见客人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P不过最近一直没有用过……\x02",
    )

    CloseMessageWindow()

    def lambda_16E8():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16E8)

    def lambda_16F6():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_16F6)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#012F……是这样啊。\x02",
    )

    CloseMessageWindow()
    OP_69(0x9, 0x5DC)
    OP_6A(0x9)

    ChrTalk(
        0x108,
        (
            "#073F#2P说起来，\x01",
            "女王陛下的病情有那么严重吗？\x02\x03",
            "不是就要举行诞辰庆典了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(
        0x9,
        "#5P不、不是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P最近照顾陛下的，\x01",
            "是这里的女官长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P所以……\x01",
            "我不太清楚具体的情况……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0x9,
        "#5P真、真是不好意思……\x02",
    )

    CloseMessageWindow()
    OP_66(0x1)
    OP_8C(0x9, 270, 400)
    OP_43(0x9, 0x1, 0x0, 0x5)
    Sleep(420)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(150)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(400)
    OP_43(0x108, 0x1, 0x0, 0x5)
    Sleep(3000)
    OP_28(0x49, 0x1, 0x80)
    OP_28(0x49, 0x1, 0x100)
    OP_28(0x49, 0x1, 0x200)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4262   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_458 end

    def Function_4_18D4(): pass

    label("Function_4_18D4")

    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xFFFFC338, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFF8BC, 0x0, 0xFFFFC694, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFF114, 0x0, 0xFFFFCF18, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE070, 0x0, 0xFFFFD7C4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE070, 0x0, 0xFFFFD7C4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFCD60, 0x0, 0xFFFFDC1A, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFC3C4, 0x0, 0xFFFFE43A, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFBBB8, 0x0, 0xFFFFFDF8, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFBCDA, 0x4E2, 0xC4E, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFC0A5, 0x9C4, 0x1662, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFC50E, 0xDAC, 0x1F18, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFCD24, 0x1388, 0x2990, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFD742, 0x186A, 0x3070, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE00C, 0x1C52, 0x3426, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE96C, 0x203A, 0x367E, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFF75E, 0x2328, 0x3868, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFFB78, 0x2328, 0x3A20, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFFE52, 0x2328, 0x3DC2, 0xBB8, 0x1)
    OP_8E(0xFE, 0x14, 0x2328, 0x44B6, 0xBB8, 0x1)
    Return()

    # Function_4_18D4 end

    def Function_5_1A51(): pass

    label("Function_5_1A51")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF1E6, 0x2328, 0x5DD4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE0E8, 0x2328, 0x6504, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFDA9E, 0x2328, 0x65C2, 0xBB8, 0x1)

    def lambda_1A98():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A98)
    OP_8E(0xFE, 0xFFFFCD9C, 0x2328, 0x65C2, 0xBB8, 0x1)
    Return()

    # Function_5_1A51 end

    def Function_6_1AB9(): pass

    label("Function_6_1AB9")

    EventBegin(0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, -6640, 8000, 13770, 80)
    SetChrPos(0x8, -7900, 7500, 13100, 62)
    SetChrPos(0x101, -7920, 9000, 24630, 90)
    SetChrPos(0x102, -7520, 9000, 25920, 90)
    OP_6D(-7580, 9000, 25280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)

    NpcTalk(
        0xA,
        "男性的声音",
        "#1P哦，是你们两个啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_1B87():
        OP_6D(-3860, 9000, 20630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B87)

    def lambda_1B9F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B9F)

    def lambda_1BAD():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BAD)
    Sleep(1000)

    def lambda_1BC0():
        OP_8E(0xFE, 0xFFFFF813, 0x2328, 0x3A20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BC0)

    def lambda_1BDB():
        OP_8E(0xFE, 0xFFFFF72C, 0x2328, 0x35CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BDB)
    WaitChrThread(0xA, 0x1)

    def lambda_1BFB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BFB)
    WaitChrThread(0x8, 0x1)

    def lambda_1C0E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C0E)

    def lambda_1C1C():

        label("loc_1C1C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1C1C")

    QueueWorkItem2(0x101, 1, lambda_1C1C)

    def lambda_1C2D():

        label("loc_1C2D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1C2D")

    QueueWorkItem2(0x102, 1, lambda_1C2D)

    ChrTalk(
        0x102,
        "#012F理查德上校……\x02",
    )

    CloseMessageWindow()

    def lambda_1C5B():
        OP_6D(-4040, 9000, 25340, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C5B)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x7)
    Sleep(2000)

    def lambda_1C8B():
        OP_8E(0xFE, 0xFFFFEB4C, 0x2328, 0x6022, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C8B)
    Sleep(300)

    def lambda_1CAB():
        OP_8E(0xFE, 0xFFFFEAFC, 0x2328, 0x646E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CAB)
    WaitChrThread(0xA, 0x1)

    def lambda_1CCB():

        label("loc_1CCB")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1CCB")

    QueueWorkItem2(0xA, 1, lambda_1CCB)

    def lambda_1CDC():
        OP_8E(0xFE, 0xFFFFF196, 0x2328, 0x62F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1CDC)
    WaitChrThread(0x8, 0x1)

    def lambda_1CFC():

        label("loc_1CFC")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1CFC")

    QueueWorkItem2(0x8, 1, lambda_1CFC)
    WaitChrThread(0xA, 0x2)

    ChrTalk(
        0xA,
        (
            "#111F#2P呵呵……\x01",
            "艾丝蒂尔和约修亚啊。\x02\x03",
            "我们像这样面对面地对话\x01",
            "已经不是第一次了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们最后一次对话\x01",
            "是在戴尔蒙市长被捕之后。\x02\x03",
            "不过没有想到上校您还能记得我们。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F#2P虽然见面的机会很少，\x01",
            "不过你们给我留下了很深的印象。\x02\x03",
            "因此我调查了一下，结果让我大吃一惊。\x02\x03",
            "没有想到你们竟然是\x01",
            "卡西乌斯上校的孩子……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#580F这、这件事也知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#111F#2P哈哈，\x01",
            "情报部可不是浪得虚名的哦。\x02\x03",
            "#115F……卡西乌斯上校当年在军中时\x01",
            "曾给予我多方的照料。\x02\x03",
            "正因如此……\x01",
            "我实在难以用言语表达我的谢意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F#2P怎么样，我们去稍微谈谈如何呢？\x01",
            "　\x02\x03",
            "我之前就一直想和你们私下聊聊了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(
        0x8,
        (
            "#184F对、对不起，上校……\x02\x03",
            "不是要去和公爵大人商量相关事宜吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#115F#2P稍微迟一会儿也没关系的吧。\x02\x03",
            "#110F对了，我们谈话的话，\x01",
            "就借里面的谈话室一用吧。\x02\x03",
            "我请你们喝不带酒精的鸡尾酒。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#187F只、只是这样的话，\x01",
            "那就让我准备吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "#112F不，这与你无关。\x02\x03",
            "你到公爵那里去，\x01",
            "把我要迟一会儿的口信转告给他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#183F明、明白了……\x02",
    )

    CloseMessageWindow()

    def lambda_22A5():

        label("loc_22A5")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22A5")

    QueueWorkItem2(0xA, 1, lambda_22A5)

    def lambda_22B6():

        label("loc_22B6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22B6")

    QueueWorkItem2(0x101, 1, lambda_22B6)

    def lambda_22C7():

        label("loc_22C7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22C7")

    QueueWorkItem2(0x102, 1, lambda_22C7)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#186F……………………（怒视）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……（我好怕怕）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#181F……那么我就先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    OP_8E(0x8, 0xFFFFFF6A, 0x2328, 0x6EC8, 0xBB8, 0x0)

    def lambda_2352():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2352)
    OP_8E(0x8, 0xFFFFFFBA, 0x2328, 0x8200, 0xBB8, 0x0)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8C(0xA, 270, 400)

    def lambda_238B():

        label("loc_238B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_238B")

    QueueWorkItem2(0x101, 1, lambda_238B)

    def lambda_239C():

        label("loc_239C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_239C")

    QueueWorkItem2(0x102, 1, lambda_239C)

    ChrTalk(
        0xA,
        (
            "#110F#2P我们这就到谈话室去吧。\x01",
            "　\x02\x03",
            "请跟我来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    def lambda_2401():
        OP_8E(0xFE, 0x23AA, 0x2328, 0x64B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2401)

    def lambda_241C():
        OP_6D(-3040, 9000, 25340, 1500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_241C)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#580F啊……\x02\x03",
            "#003F（我说约修亚啊，怎么办好呢？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F（只有先奉陪一下了……）\x02\x03",
            "（虽说会有些迟，\x01",
            "　但只有稍后才去夫人那里了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x1, 0x8)
    OP_28(0x4A, 0x1, 0x10)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4261   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1AB9 end

    def Function_7_251B(): pass

    label("Function_7_251B")

    OP_8E(0xFE, 0xFFFFF8F8, 0x2328, 0x5168, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF56A, 0x2328, 0x5F6E, 0xBB8, 0x0)
    Return()

    # Function_7_251B end

    def Function_8_2544(): pass

    label("Function_8_2544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2551")
    Return()

    label("loc_2551")

    EventBegin(0x0)
    OP_A2(0x647)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -70, 9000, 27870, 180)
    SetChrPos(0xB, -800, 9000, 28970, 180)
    SetChrPos(0xC, 530, 9000, 28970, 180)

    NpcTalk(
        0x8,
        "女性的声音",
        (
            "#4P……都这种时候了，\x01",
            "你们还在这里做什么啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)

    def lambda_2622():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2622)

    def lambda_2630():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2630)
    OP_6D(10, 9000, 27580, 2000)

    ChrTalk(
        0x101,
        "#580F#1P啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -550, 9000, 16309, 0)
    SetChrPos(0x102, 670, 9000, 16190, 0)
    SetChrFlags(0x108, 0x80)

    def lambda_2692():
        OP_8E(0xFE, 0x8C, 0x2328, 0x4DE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2692)
    Sleep(200)

    def lambda_26B2():
        OP_8E(0xFE, 0xFFFFFDBC, 0x2328, 0x5294, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26B2)
    Sleep(100)

    def lambda_26D2():
        OP_8E(0xFE, 0x33E, 0x2328, 0x529E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_26D2)
    OP_6D(100, 9000, 18910, 3000)

    ChrTalk(
        0x102,
        "#012F凯诺娜上尉……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#182F哼哼哼，晚上好。\x02\x03",
            "怎么说你们也是贵宾，\x01",
            "我还是对你们比较客气的。\x02\x03",
            "可要说是孩子晚上出去散步\x01",
            "不觉得未免太迟了一些吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F很抱歉。\x02\x03",
            "因为看见城里有许多新奇的东西，\x01",
            "所以稍微迟了一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#182F哎呀，这没什么啦。\x02\x03",
            "那么你们３０分钟之前\x01",
            "在哪里参观呢？\x02\x03",
            "能不能告诉我，　\x01",
            "让我做个参考呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【厨房】\x01",              # 0
            "【侍女休息室】\x01",        # 1
            "【行政区域】\x01",          # 2
            "【亲卫队值勤室】\x01",      # 3
            "【地下仓库】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2982"),
        (1, "loc_2AD5"),
        (2, "loc_2BD6"),
        (3, "loc_2D6A"),
        (4, "loc_2F0A"),
        (SWITCH_DEFAULT, "loc_3078"),
    )


    label("loc_2982")


    ChrTalk(
        0x8,
        (
            "#180F哎呀，很可疑呢。\x02\x03",
            "刚才我去巡视的时候\x01",
            "怎么没有看见你们呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F那是、那是因为……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#181F算了算了。\x01",
            "我不准备再和你们兜圈子了……\x02\x03",
            "#188F事实上我已经收到了报告，\x01",
            "发现你们两个曾屡次在侍女休息室进出。\x01",
            "　\x02\x03",
            "到那样的地方去参观，\x01",
            "难道不是十分可疑的行为吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2AD5")


    ChrTalk(
        0x8,
        (
            "#180F呵呵……\x01",
            "真是老实的孩子呢。\x02\x03",
            "#181F算了算了。\x01",
            "我不准备再和你们兜圈子了……\x02\x03",
            "#188F事实上我已经收到了报告，\x01",
            "发现你们两个曾屡次在侍女休息室进出。\x01",
            "　\x02\x03",
            "到那样的地方去参观，\x01",
            "难道不是十分可疑的行为吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2BD6")


    ChrTalk(
        0x8,
        (
            "#180F行政区域的值班人\x01",
            "早就已经回去了。\x02\x03",
            "你们在那种地方，\x01",
            "到底干了些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F那是、那是因为……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#181F算了算了。\x01",
            "我不准备再和你们兜圈子了……\x02\x03",
            "#188F事实上我已经收到了报告，\x01",
            "发现你们两个曾屡次在侍女休息室进出。\x01",
            "　\x02\x03",
            "到那样的地方去参观，\x01",
            "难道不是十分可疑的行为吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2D6A")


    ChrTalk(
        0x8,
        (
            "那真是奇怪了。\x02\x03",
            "那里现在正作为我们\x01",
            "情报部的办公室使用……\x02\x03",
            "是不可能让你们进去参观的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F那是、那是因为……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#181F算了算了。\x01",
            "我不准备再和你们兜圈子了……\x02\x03",
            "#188F事实上我已经收到了报告，\x01",
            "发现你们两个曾屡次在侍女休息室进出。\x01",
            "　\x02\x03",
            "到那样的地方去参观，\x01",
            "难道不是十分可疑的行为吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_2F0A")


    ChrTalk(
        0x8,
        (
            "#183F什么……\x02\x03",
            "你们去那种地方\x01",
            "到底干了些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F没、没有干什么事情啊……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#181F算了算了。\x01",
            "我不准备再和你们兜圈子了……\x02\x03",
            "#188F事实上我已经收到了报告，\x01",
            "发现你们两个曾屡次在侍女休息室进出。\x01",
            "　\x02\x03",
            "到那样的地方去参观，\x01",
            "难道不是十分可疑的行为吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3078")

    label("loc_3078")


    ChrTalk(
        0x101,
        "#005F什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F你明知故问，\x01",
            "人品也太差了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#188F哼哼哼……\x01",
            "不错的赞美之词嘛，我先收下了。\x02\x03",
            "刚才只是调和一下气氛而已。\x01",
            "说吧，去侍女休息室到底做什么？\x02\x03",
            "老老实实回答对你们有好处哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F那是……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x108, 7350, 9000, 25020, 225)

    NpcTalk(
        0x108,
        "男性的声音",
        (
            "#3P喂～～～～～！\x01",
            "艾丝蒂尔、约修亚！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x108,
        "男性的声音",
        "#3P原来你们还呆在那里啊～！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3293():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3293)

    def lambda_32A1():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32A1)

    def lambda_32AF():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_32AF)

    def lambda_32BD():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_32BD)

    def lambda_32CB():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_32CB)
    OP_6D(3730, 9000, 21420, 2000)

    def lambda_32EA():

        label("loc_32EA")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_32EA")

    QueueWorkItem2(0x101, 1, lambda_32EA)

    def lambda_32FB():

        label("loc_32FB")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_32FB")

    QueueWorkItem2(0x102, 1, lambda_32FB)

    def lambda_330C():

        label("loc_330C")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_330C")

    QueueWorkItem2(0x8, 1, lambda_330C)

    def lambda_331D():

        label("loc_331D")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_331D")

    QueueWorkItem2(0xB, 1, lambda_331D)

    def lambda_332E():

        label("loc_332E")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_332E")

    QueueWorkItem2(0xC, 1, lambda_332E)

    ChrTalk(
        0x102,
        "#014F金先生……\x02",
    )

    CloseMessageWindow()

    def lambda_3351():
        OP_6D(900, 9000, 19490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3351)

    def lambda_3369():
        OP_6E(256, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3369)

    def lambda_3379():
        OP_9E(0xFE, 0x3C, 0x0, 0xBB8, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3379)
    OP_8E(0x108, 0x758, 0x2328, 0x4B32, 0x7D0, 0x0)
    Sleep(400)
    SetChrChipByIndex(0x108, 7)
    OP_22(0xB2, 0x0, 0x64)
    SetChrSubChip(0x108, 0)
    Sleep(150)
    SetChrSubChip(0x108, 1)
    Sleep(150)
    SetChrSubChip(0x108, 2)
    Sleep(150)
    SetChrSubChip(0x108, 0)
    Sleep(150)
    SetChrSubChip(0x108, 1)
    Sleep(150)
    SetChrSubChip(0x108, 2)
    Sleep(150)
    SetChrSubChip(0x108, 0)
    Sleep(180)
    SetChrSubChip(0x108, 1)
    Sleep(180)
    SetChrSubChip(0x108, 2)
    Sleep(200)
    SetChrSubChip(0x108, 3)
    Sleep(100)
    SetChrSubChip(0x108, 4)
    Sleep(170)

    ChrTalk(
        0x108,
        "#079F哇～流到身上了！\x02",
    )

    SetChrSubChip(0x108, 5)
    Sleep(70)
    SetChrSubChip(0x108, 6)
    Sleep(70)
    SetChrSubChip(0x108, 7)
    Sleep(350)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F哇，喝得酩酊大醉的……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)
    OP_0D()
    TurnDirection(0x108, 0x8, 0)
    Sleep(400)

    ChrTalk(
        0x108,
        (
            "#570F哦，抱歉。\x02\x03",
            "我说你们是和谁在这里呢，\x01",
            "原来是和美女军官在一起啊。\x02\x03",
            "#079F哎呀啊～\x01",
            "怎么说都是美妙的邂逅啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#184F是、是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#078F怎么了？\x02\x03",
            "我那两个不成器的徒弟\x01",
            "给您添了不少麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F徒、徒弟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#183F没有，不过刚才他们竟然\x01",
            "屡次出入侍女休息室……\x02\x03",
            "出于保卫王城安全的理由，\x01",
            "我想问问他们在里面做了些什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#079F哦，原来是这么回事啊。\x02\x03",
            "下酒的菜都没有了，\x01",
            "所以我叫他们去取一些来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 225, 0)
    Sleep(400)

    ChrTalk(
        0x108,
        (
            "#078F喂，约修亚，\x01",
            "还有什么可以吃的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没有了，\x01",
            "厨师他们好像已经回去休息了……\x02\x03",
            "我又问了侍女她们，\x01",
            "虽然她们去找了一下，\x01",
            "但下酒菜是的确没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#571F呼，没办法啦。\x01",
            "没有下酒菜就只有忍了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x108,
        (
            "#570F对了……\x01",
            "我想到了一个好办法！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 0)
    Sleep(400)

    def lambda_3816():
        OP_9E(0xFE, 0x64, 0x0, 0x3E8, 0x12C)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3816)
    OP_92(0x108, 0x8, 0x320, 0x3E8, 0x0)

    ChrTalk(
        0x108,
        (
            "#079F#2P如果您不介意的话，\x01",
            "赏面陪我喝喝酒谈谈心如何呢？\x02\x03",
            "哇哈哈～～～\x01",
            "美人的笑脸是最好的下酒佳肴啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        (
            "#187F我、我还有任务在身，\x01",
            "恕我无法奉陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#183F#1P刚才的那件事姑且不问……\x01",
            "　\x02\x03",
            "你们现在就回房间去，\x01",
            "今晚不准再出来乱走。\x02\x03",
            "如果再发现你们有可疑的行动，\x01",
            "我会保留调查的权利哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_3A14():

        label("loc_3A14")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3A14")

    QueueWorkItem2(0x101, 1, lambda_3A14)

    def lambda_3A25():

        label("loc_3A25")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3A25")

    QueueWorkItem2(0x102, 1, lambda_3A25)

    def lambda_3A36():

        label("loc_3A36")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3A36")

    QueueWorkItem2(0x108, 1, lambda_3A36)

    ChrTalk(
        0x101,
        "#009F知、知道了还不行嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F已经很晚了，\x01",
            "我们也该休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F#1P哼哼，老实点好。\x02\x03",
            "#181F那么……\x01",
            "我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x9)

    def lambda_3B02():
        OP_6D(710, 9000, 17230, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3B02)
    Sleep(1500)
    OP_44(0x108, 0xFF)
    OP_8C(0x108, 180, 0)
    WaitChrThread(0x8, 0x2)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_6D(710, 9000, 18930, 1000)
    Sleep(400)

    ChrTalk(
        0x108,
        (
            "#570F哎呀，这就走掉了……\x02\x03",
            "#571F没办法了……\x01",
            "我回房间休息去了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#506F嗯、好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们也一起回去吧。\x02",
    )

    CloseMessageWindow()
    FadeToBright(1500, 0)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4262   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2544 end

    def Function_9_3BF9(): pass

    label("Function_9_3BF9")

    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x4A38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x3C6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x64, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x10E0, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2058, 0x1C52, 0x34A8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3552, 0x1194, 0x25E4, 0xBB8, 0x0)
    Return()

    # Function_9_3BF9 end

    def Function_10_3C72(): pass

    label("Function_10_3C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E03")
    EventBegin(0x1)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D49")
    TurnDirection(0xD, 0x0, 400)

    ChrTalk(
        0xD,
        (
            "哎呀呀，这不是希尔丹夫人吗……\x01",
            "到我们这儿来有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这里是情报部的值勤室。\x01",
            "请不要随随便便靠近。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xD, 270, 0)
    Jump("loc_3DF8")

    label("loc_3D49")

    TurnDirection(0xD, 0x0, 400)

    ChrTalk(
        0xD,
        (
            "这里是情报部的值勤室。\x01",
            "平民禁止入内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不想被逮捕的话，\x01",
            "就不要靠近。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xD, 270, 0)

    label("loc_3DF8")

    OP_4B(0xD, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3E03")

    Return()

    # Function_10_3C72 end

    def Function_11_3E04(): pass

    label("Function_11_3E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E11")
    Return()

    label("loc_3E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3ED1")
    EventBegin(0x1)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)

    ChrTalk(
        0x11,
        (
            "哦？有什么事吗？\x01",
            "现在不能打开城门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "很抱歉，\x01",
            "你们请在城内好好放松吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0x10, 0, 0)
    OP_8C(0x11, 0, 0)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    Jump("loc_40C1")

    label("loc_3ED1")

    EventBegin(0x1)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC2")
    TurnDirection(0xE, 0x0, 400)
    TurnDirection(0xF, 0x0, 400)

    ChrTalk(
        0xE,
        "哦，希尔丹夫人。都这么晚了还要外出吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "您也是知道的，出于安全考虑，\x01",
            "现在城门的开闭受到限制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "没有得到许可\x01",
            "是不能从这里通行的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4097")

    label("loc_3FC2")

    TurnDirection(0xE, 0x0, 400)
    TurnDirection(0xF, 0x0, 400)

    ChrTalk(
        0xF,
        (
            "出于安全考虑，\x01",
            "现在城门的开闭受到限制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "请在王城内\x01",
            "随便活动吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "你们应该不会觉得\x01",
            "有什么不自由吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4097")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_8C(0xF, 0, 0)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)

    label("loc_40C1")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_11_3E04 end

    def Function_12_40C9(): pass

    label("Function_12_40C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40D6")
    Return()

    label("loc_40D6")

    EventBegin(0x1)
    OP_4A(0x12, 255)
    TurnDirection(0x12, 0x0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4184")

    ChrTalk(
        0x12,
        (
            "现在谒见大厅里\x01",
            "正在进行一个重要会议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "非常抱歉，\x01",
            "目前还不能进入，请稍等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_4184")


    ChrTalk(
        0x12,
        (
            "现在谒见大厅里\x01",
            "正在进行一个重要会议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果想参观的话，\x01",
            "以后还有的是机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4222")

    OP_8C(0x12, 180, 0)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_4B(0x12, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_12_40C9 end

    def Function_13_4249(): pass

    label("Function_13_4249")

    TalkBegin(0xFE)

    ChrTalk(
        0x10,
        (
            "哎呀～\x01",
            "感觉就像回到自己的家里一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "王城的警备\x01",
            "还是应该由我们正规军来担当。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_4249 end

    def Function_14_42B7(): pass

    label("Function_14_42B7")

    TalkBegin(0xFE)

    ChrTalk(
        0x11,
        (
            "那位理查德上校\x01",
            "竟然是政变的主谋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "作为王国军一员的我，\x01",
            "委实感觉心情难以言表。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_42B7 end

    def Function_15_4347(): pass

    label("Function_15_4347")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43E6")

    ChrTalk(
        0x12,
        (
            "现在谒见大厅里\x01",
            "正在进行一个重要会议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "非常抱歉，\x01",
            "目前还不能进入，请稍等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4484")

    label("loc_43E6")


    ChrTalk(
        0x12,
        "现在谒见大厅里正在进行一个重要会议。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果想参观的话，\x01",
            "以后还有的是机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4484")

    TalkEnd(0xFE)
    Return()

    # Function_15_4347 end

    SaveToFile()

Try(main)
