from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4210   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4210.x',
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
        'ED6_DT07/CH01330 ._CH',             # 06
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
        'ED6_DT07/CH01330P._CP',             # 06
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_31D",          # 01, 1
        "Function_2_32C",          # 02, 2
        "Function_3_3FA",          # 03, 3
        "Function_4_1755",         # 04, 4
        "Function_5_18D2",         # 05, 5
        "Function_6_193A",         # 06, 6
        "Function_7_2291",         # 07, 7
        "Function_8_22BA",         # 08, 8
        "Function_9_33FC",         # 09, 9
        "Function_10_3475",        # 0A, 10
        "Function_11_3607",        # 0B, 11
        "Function_12_38CC",        # 0C, 12
        "Function_13_393A",        # 0D, 13
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2A2"),
        (108, "loc_2B8"),
        (SWITCH_DEFAULT, "loc_2CE"),
    )


    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B5")
    OP_A2(0x639)
    Event(0, 3)

    label("loc_2B5")

    Jump("loc_2CE")

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB")
    OP_A2(0x641)
    Event(0, 6)

    label("loc_2CB")

    Jump("loc_2CE")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    SetChrChipByIndex(0x0, 3)
    SetChrChipByIndex(0x1, 4)
    SetChrChipByIndex(0x138, 5)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_31C")

    Return()

    # Function_0_292 end

    def Function_1_31D(): pass

    label("Function_1_31D")

    OP_71(0x0, 0x2)
    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_31D end

    def Function_2_32C(): pass

    label("Function_2_32C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3E4")

    label("loc_351")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3E4")

    label("loc_36A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_383")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3E4")

    label("loc_383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3E4")

    label("loc_39C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3E4")

    label("loc_3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3E4")

    label("loc_3CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3E4")

    label("loc_3F9")

    Return()

    # Function_2_32C end

    def Function_3_3FA(): pass

    label("Function_3_3FA")

    EventBegin(0x0)
    SetChrPos(0x101, 520, 0, -22530, 0)
    SetChrPos(0x102, -1610, 0, -22470, 0)
    SetChrPos(0x108, -290, 0, -21870, 0)
    OP_6D(-210, 0, -19730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(10000, 0)
    OP_6E(280, 0)

    def lambda_472():
        OP_6D(180, 9000, 14710, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_472)

    def lambda_48A():
        OP_67(0, 4950, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48A)

    def lambda_4A2():
        OP_6B(2190, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4A2)

    def lambda_4B2():
        OP_6C(45000, 12000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B2)

    def lambda_4C2():
        OP_6E(899, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C2)
    FadeToBright(2000, 0)
    Sleep(12000)
    Fade(1000)
    OP_6D(30, 0, -22200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#000F哇～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F虽然是理所当然的……\x02\x03",
            "这比至今为止见过的房间\x01",
            "要豪华不知道多少倍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不只是豪华，\x01",
            "还有蕴含历史和传统的壮丽。\x02\x03",
            "到处都有浓厚的\x01",
            "古代王国的传统风格呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 770, 0, -9870, 180)
    SetChrPos(0x9, -280, 0, -9260, 180)

    ChrTalk(
        0x8,
        "欢迎来到格兰赛尔城。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请问你们就是\x01",
            "金先生一行人吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_680():
        OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0xFFFFB41A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_680)

    def lambda_69B():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0xFFFFB758, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_69B)
    OP_6D(130, 0, -20310, 3000)

    ChrTalk(
        0x101,
        "#000F（哎哎……是凯诺娜上尉……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（虽然也不是没有预料到……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，没错。\x01",
            "我们受了公爵阁下的邀请。\x02\x03",
            "请问……你是？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#180F呵呵，忘了自我介绍。\x02\x03",
            "我是担任格兰赛尔城警卫工作的\x01",
            "情报部的凯诺娜上尉。\x02\x03",
            "恭喜金先生你们\x01",
            "获得武术大会的优胜。\x02\x03",
            "我看了你们的比赛，\x01",
            "真是威风凛凛，令人叹为观止啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哎呀～真是过奖了。\x02\x03",
            "我倒觉得，您这样年轻和漂亮，\x01",
            "担当军队的上尉真是让我吃惊呢。\x02\x03",
            "一定是非常优秀才能做到这样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F哎呀……\x01",
            "您真会说话。\x02\x03",
            "哦，这两位不是\x01",
            "年轻的游击士嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F………………………………\x02",
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
        "#000F……嗯，是啊。\x02",
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
            "#180F虽然很遗憾，\x01",
            "不过拉赛尔博士的事件\x01",
            "还没有完全解决。\x02\x03",
            "博士和她的孙女\x01",
            "好像被一伙暴徒绑架了呢。\x02\x03",
            "所以就让\x01",
            "有没有这方面的线索呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那、那个。\x01",
            "一点也不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个事情交给了正游击士去处理，\x01",
            "然后我们就来王都了。\x02\x03",
            "之后的事情就没再听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F是吗……呵呵。\x01",
            "那真是遗憾呢\x02\x03",
            "不过，只要借助情报部的力量，\x01",
            "逮捕绑架犯也只是时间上的问题了。\x02\x03",
            "就请你们瞧着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（这、这个狐狸精～……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我明白了，\x02\x03",
            "博士是我们的恩人，\x01",
            "所以一定请你们救出他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F那是自然……\x02\x03",
            "那么，就招待各位\x01",
            "到你们的房间去吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "#180F茜亚……\x01",
            "接下来就交给你了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "好……\x01",
            "我会好好照顾客人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F还有，请你注意……\x02\x03",
            "不要对客人没有礼貌，\x01",
            "说些不该说的话。\x02\x03",
            "记住了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好、好的……\x01",
            "我明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#180F哼哼，这样就好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)
    TurnDirection(0x8, 0x108, 400)

    ChrTalk(
        0x8,
        (
            "#180F那么各位，\x01",
            "希望你们今晚过得愉快。\x02\x03",
            "我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EA6():

        label("loc_EA6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EA6")

    QueueWorkItem2(0x108, 1, lambda_EA6)

    def lambda_EB7():

        label("loc_EB7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EB7")

    QueueWorkItem2(0x101, 1, lambda_EB7)

    def lambda_EC8():

        label("loc_EC8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EC8")

    QueueWorkItem2(0x102, 1, lambda_EC8)
    OP_8E(0x8, 0x730, 0x0, 0xFFFFC2F2, 0x7D0, 0x0)

    def lambda_EED():
        OP_8E(0xFE, 0x1CC0, 0x0, 0xFFFFD88C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EED)
    Sleep(1500)

    ChrTalk(
        0x108,
        "#070F唔～这个女人真是不错啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F金先生，你的兴趣真是奇怪啊……\x02\x03",
            "那个狐狸精，\x01",
            "有什么地方好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#010F那样的人，\x01",
            "是金先生喜欢的类型吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，只有这样\x01",
            "本质上才会纯情啊。\x02\x03",
            "就是这一点最吸引人了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#000F不行了……\x02\x03",
            "不管怎么样都好啦。\x01",
            "金先生，你好像大叔一样呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_110A():
        TurnDirection(0xFE, 0x101, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_110A)

    ChrTalk(
        0x108,
        "#070F（受到打击）\x02",
    )

    CloseMessageWindow()

    def lambda_1130():
        OP_6D(-240, 0, -20830, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1130)
    OP_8E(0x9, 0xFFFFFEFC, 0x0, 0xFFFFB186, 0x5DC, 0x0)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(
        0x9,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    def lambda_1171():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1171)

    def lambda_117F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117F)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，抱歉抱歉。\x02\x03",
            "现在可以带我们\x01",
            "去看看房间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好……\x01",
            "我来带路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "请允许我先自我介绍一下。\x01",
            "我是这里的侍女，名叫茜亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从晚宴开始到明天，\x01",
            "由我来照顾你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果有什么不便，\x01",
            "随时可以告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F啊，请多关照啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "现在带我们去房间吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，好的。\x01",
            "各位的房间在２楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_8E(0x108, 0xFFFFFF10, 0x0, 0xFFFFAEA2, 0xBB8, 0x0)
    OP_6A(0x108)
    OP_43(0x108, 0x1, 0x0, 0x4)
    Sleep(150)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(12000)
    OP_66(0x0)
    WaitChrThread(0x9, 0x1)

    def lambda_13C0():
        OP_6E(196, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13C0)

    def lambda_13D0():
        OP_8E(0xFE, 0x32, 0x2328, 0x5A6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13D0)
    WaitChrThread(0x108, 0x1)

    def lambda_13F0():
        OP_8E(0xFE, 0x410, 0x2328, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_13F0)
    WaitChrThread(0x102, 0x1)

    def lambda_1410():
        OP_8E(0xFE, 0xFFFFFB96, 0x2328, 0x524E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1410)
    WaitChrThread(0x101, 0x1)

    def lambda_1430():
        OP_8E(0xFE, 0xFFFFFF92, 0x2328, 0x4FBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1430)

    ChrTalk(
        0x101,
        (
            "#000F哇～\x02\x03",
            "那个巨大的吊灯，\x01",
            "真是豪华绚丽呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1495():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1495)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，不要大声喧哗。\x02\x03",
            "对了，那边是……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14D1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14D1)

    def lambda_14DF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14DF)

    def lambda_14ED():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_14ED)
    OP_8C(0x9, 0, 400)

    ChrTalk(
        0x9,
        "是『谒见室』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "艾莉茜雅女王陛下\x01",
            "就是在这里会见客人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "不过最近一直没有用过……\x02",
    )

    CloseMessageWindow()

    def lambda_158C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_158C)

    def lambda_159A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_159A)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F说起来，女王陛下的病情\x01",
            "有那么严重吗？\x02\x03",
            "不是就要举行生日庆典了吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_69(0x102, 0x3E8)
    OP_6A(0x102)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(
        0x9,
        "不、不是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "最近照顾陛下的，\x01",
            "是这里的女官长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "所以，我不太清楚\x01",
            "具体的情况……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(
        0x9,
        "真、真是不好意思……\x02",
    )

    CloseMessageWindow()
    OP_66(0x1)
    OP_43(0x9, 0x1, 0x0, 0x5)
    Sleep(420)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(150)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(400)
    OP_43(0x108, 0x1, 0x0, 0x5)
    Sleep(3000)
    OP_28(0x49, 0x1, 0x80)
    OP_28(0x49, 0x1, 0x100)
    OP_28(0x49, 0x1, 0x200)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4222   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3FA end

    def Function_4_1755(): pass

    label("Function_4_1755")

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

    # Function_4_1755 end

    def Function_5_18D2(): pass

    label("Function_5_18D2")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF1E6, 0x2328, 0x5DD4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE0E8, 0x2328, 0x6504, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFDA9E, 0x2328, 0x65C2, 0xBB8, 0x1)

    def lambda_1919():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1919)
    OP_8E(0xFE, 0xFFFFCD9C, 0x2328, 0x65C2, 0xBB8, 0x1)
    Return()

    # Function_5_18D2 end

    def Function_6_193A(): pass

    label("Function_6_193A")

    EventBegin(0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, -6640, 8000, 13770, 80)
    SetChrPos(0x8, -7900, 7500, 13100, 62)
    SetChrPos(0x101, -7920, 9000, 24630, 118)
    SetChrPos(0x102, -7520, 9000, 25920, 118)

    ChrTalk(
        0xA,
        "#110F哦，是你们俩啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_19BC():
        OP_6D(-3860, 9000, 20630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19BC)
    Sleep(1000)

    def lambda_19D9():
        OP_8E(0xFE, 0xFFFFF813, 0x2328, 0x3A20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19D9)

    def lambda_19F4():
        OP_8E(0xFE, 0xFFFFF72C, 0x2328, 0x35CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19F4)
    WaitChrThread(0xA, 0x1)

    def lambda_1A14():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A14)
    WaitChrThread(0x8, 0x1)

    def lambda_1A27():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A27)

    def lambda_1A35():

        label("loc_1A35")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1A35")

    QueueWorkItem2(0x101, 1, lambda_1A35)

    def lambda_1A46():

        label("loc_1A46")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1A46")

    QueueWorkItem2(0x102, 1, lambda_1A46)

    ChrTalk(
        0x102,
        "#010F理查德上校……\x02",
    )

    CloseMessageWindow()

    def lambda_1A74():
        OP_6D(-7040, 9000, 25530, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A74)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x7)
    WaitChrThread(0xA, 0x1)

    def lambda_1AA4():

        label("loc_1AA4")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1AA4")

    QueueWorkItem2(0xA, 1, lambda_1AA4)

    def lambda_1AB5():
        OP_8E(0xFE, 0xFFFFE778, 0x2328, 0x6324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1AB5)
    WaitChrThread(0x8, 0x1)

    def lambda_1AD5():

        label("loc_1AD5")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1AD5")

    QueueWorkItem2(0x8, 1, lambda_1AD5)
    WaitChrThread(0xA, 0x2)

    ChrTalk(
        0xA,
        (
            "#110F呵呵……\x01",
            "是艾丝蒂尔和约修亚啊。\x02\x03",
            "我们像这样面对面\x01",
            "的对话已经不是第一次了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们最后一次对话是在\x01",
            "戴尔蒙市长被捕之后。\x02\x03",
            "不过没有想到上校您\x01",
            "还能记起我们来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F虽然对话的机会很少，\x01",
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
        "#000F这、这件事也知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F哈哈，情报部\x01",
            "可不是浪得虚名的哦。\x02\x03",
            "……卡西乌斯上校当年\x01",
            "在军中时曾给予我许多照料。\x02\x03",
            "正因如此……\x01",
            "言语实在难表我的谢意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F怎么样，我们去稍微\x01",
            "谈谈如何呢？\x02\x03",
            "我之前就一直想\x01",
            "和你们私下谈谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(
        0x8,
        (
            "#180F对、对不起，上校……\x02\x03",
            "不是要去和公爵大人\x01",
            "商量相关事宜的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#110F稍微迟一点也没关系的吧。\x02\x03",
            "对了，要谈谈的话，\x01",
            "就借里面的谈话室一用吧。\x02\x03",
            "我只是请你们喝一些\x01",
            "不带酒精的鸡尾酒而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F只、只是这样的话，\x01",
            "就让我来吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "#110F不，这与你无关。\x02\x03",
            "你到公爵那里去，\x01",
            "把我要迟到一会儿的消息告诉他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#180F明、明白了……\x02",
    )

    CloseMessageWindow()

    def lambda_2054():

        label("loc_2054")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2054")

    QueueWorkItem2(0xA, 1, lambda_2054)

    def lambda_2065():

        label("loc_2065")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2065")

    QueueWorkItem2(0x101, 1, lambda_2065)

    def lambda_2076():

        label("loc_2076")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2076")

    QueueWorkItem2(0x102, 1, lambda_2076)
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 800)

    ChrTalk(
        0x8,
        "#180F…………………（怒视）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（我好怕怕……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#180F……那么我就先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFFF6A, 0x2328, 0x6EC8, 0xBB8, 0x0)

    def lambda_20F5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20F5)
    OP_8E(0x8, 0xFFFFFFBA, 0x2328, 0x8200, 0xBB8, 0x0)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8C(0xA, 270, 400)

    def lambda_212E():

        label("loc_212E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_212E")

    QueueWorkItem2(0x101, 1, lambda_212E)

    def lambda_213F():

        label("loc_213F")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_213F")

    QueueWorkItem2(0x102, 1, lambda_213F)

    ChrTalk(
        0xA,
        (
            "#110F我们这就到\x01",
            "谈话室去吧。\x02\x03",
            "请跟我来。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_219A():
        OP_8E(0xFE, 0x23AA, 0x2328, 0x64B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_219A)
    Sleep(300)
    OP_6D(-5680, 9000, 25260, 2000)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x02\x03",
            "我说约修亚啊，怎么办好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F只有先奉陪一下了……\x02\x03",
            "虽说会有些迟，\x01",
            "但只有稍后才去夫人那里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x1, 0x8)
    OP_28(0x4A, 0x1, 0x10)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_193A end

    def Function_7_2291(): pass

    label("Function_7_2291")

    OP_8E(0xFE, 0xFFFFF8F8, 0x2328, 0x5168, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFED7C, 0x2328, 0x5CE4, 0xBB8, 0x0)
    Return()

    # Function_7_2291 end

    def Function_8_22BA(): pass

    label("Function_8_22BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22C7")
    Return()

    label("loc_22C7")

    EventBegin(0x0)
    OP_A2(0x647)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -70, 9000, 27870, 180)
    SetChrPos(0xB, -800, 9000, 28970, 180)
    SetChrPos(0xC, 530, 9000, 28970, 180)

    ChrTalk(
        0x8,
        (
            "……这种时候\x01",
            "还在那儿做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2382():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2382)

    def lambda_2390():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2390)
    OP_6D(10, 9000, 27580, 3000)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -550, 9000, 16309, 0)
    SetChrPos(0x102, 670, 9000, 16190, 0)
    SetChrPos(0x108, 6350, 9000, 24020, 225)
    SetChrFlags(0x108, 0x80)

    def lambda_23EA():
        OP_8E(0xFE, 0x8C, 0x2328, 0x4DE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23EA)

    def lambda_2405():
        OP_8E(0xFE, 0xFFFFFDBC, 0x2328, 0x5294, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2405)

    def lambda_2420():
        OP_8E(0xFE, 0x33E, 0x2328, 0x529E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2420)
    OP_6D(100, 9000, 18910, 3000)

    ChrTalk(
        0x101,
        "#000F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F凯诺娜上尉……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#180F哼哼哼，晚上好。\x02\x03",
            "怎么说你们也是贵宾，\x01",
            "我还是对你们比较客气的。\x02\x03",
            "可要说是孩子晚上出去散步\x01",
            "不觉得也太迟了一些吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很抱歉。\x02\x03",
            "因为看见城里有许多新奇的东西，\x01",
            "所以稍微迟了一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F哎呀，倒是个不错的选择呢。\x02\x03",
            "那么你们３０分钟之前\x01",
            "在哪里参观呢？\x02\x03",
            "能不能告诉我，　\x01",
            "让我做个参考呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……\x02",
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
            "厨房\x01",              # 0
            "侍女休息室\x01",        # 1
            "行政区域\x01",          # 2
            "亲卫队值勤室\x01",      # 3
            "地下仓库\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26E1"),
        (1, "loc_2752"),
        (2, "loc_277F"),
        (3, "loc_2831"),
        (4, "loc_28EF"),
        (SWITCH_DEFAULT, "loc_297C"),
    )


    label("loc_26E1")


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
        "#000F这、这个嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_297C")

    label("loc_2752")


    ChrTalk(
        0x8,
        (
            "#180F呵呵……\x01",
            "真是老实的孩子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_297C")

    label("loc_277F")


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
        "#000F这、这个嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_297C")

    label("loc_2831")


    ChrTalk(
        0x8,
        (
            "那真是奇怪了。\x02\x03",
            "那里现在正作为我们\x01",
            "情报部的办公室使用……\x02\x03",
            "自从看到你们在\x01",
            "不可能让你们进去参观的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F这、这个嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_297C")

    label("loc_28EF")


    ChrTalk(
        0x8,
        (
            "什么……\x02\x03",
            "你们去那种地方\x01",
            "到底干了些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没、没有\x01",
            "干什么事情啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_297C")

    label("loc_297C")


    ChrTalk(
        0x8,
        (
            "#180F算了，我不准备\x01",
            "再和你们兜圈子了……\x02\x03",
            "事实上我已经收到了报告，\x01",
            "发现你们俩曾屡次在\x01",
            "侍女休息室进进出出。\x02\x03",
            "在那样的地方去参观，\x01",
            "难道一点都不可疑吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你明知故问，\x01",
            "人品也太差了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F哼哼哼，我收下\x01",
            "你的赞美之词。\x02\x03",
            "说吧，到侍女休息室\x01",
            "做什么去了啊？\x02\x03",
            "老老实实回答对你们有好处哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "喂～！\x01",
            "艾丝蒂尔、约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "原来你们还呆在那里啊～！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)

    def lambda_2BC2():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC2)

    def lambda_2BD0():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BD0)

    def lambda_2BDE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BDE)

    def lambda_2BEC():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2BEC)

    def lambda_2BFA():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2BFA)
    OP_6D(3230, 9000, 20920, 2000)

    def lambda_2C19():

        label("loc_2C19")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C19")

    QueueWorkItem2(0x101, 1, lambda_2C19)

    def lambda_2C2A():

        label("loc_2C2A")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C2A")

    QueueWorkItem2(0x102, 1, lambda_2C2A)

    def lambda_2C3B():

        label("loc_2C3B")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C3B")

    QueueWorkItem2(0x8, 1, lambda_2C3B)

    def lambda_2C4C():

        label("loc_2C4C")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C4C")

    QueueWorkItem2(0xB, 1, lambda_2C4C)

    def lambda_2C5D():

        label("loc_2C5D")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C5D")

    QueueWorkItem2(0xC, 1, lambda_2C5D)

    ChrTalk(
        0x102,
        "#010F金大哥……\x02",
    )

    CloseMessageWindow()

    def lambda_2C80():
        OP_6D(900, 9000, 19490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C80)

    def lambda_2C98():
        OP_6E(256, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C98)

    def lambda_2CA8():
        OP_9E(0xFE, 0x3C, 0x0, 0x1388, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2CA8)
    OP_8E(0x108, 0x758, 0x2328, 0x4B32, 0x7D0, 0x0)
    SetChrChipByIndex(0x108, 7)
    OP_99(0x108, 0x0, 0x7, 0x7D0)

    ChrTalk(
        0x101,
        "#000F哇，酩酊大醉……\x02",
    )

    CloseMessageWindow()
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)
    TurnDirection(0x108, 0x8, 400)

    ChrTalk(
        0x108,
        (
            "#070F哦哟，抱歉。\x02\x03",
            "我说是和谁在那儿呢，\x01",
            "原来是和美女军官在一起啊。\x02\x03",
            "哎呀啊～怎么说都\x01",
            "是美妙的偶然相遇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#180F是、是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F你看怎么样？\x02\x03",
            "我那不成熟的徒弟给您\x01",
            "添了不少麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F徒、徒弟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F没有，不过刚才他们竟然\x01",
            "呆在侍女休息室里面……\x02\x03",
            "出于保卫这里安全的理由，\x01",
            "我问问他们在里面做什么。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(
        0x108,
        (
            "#070F哦，那个是这么回事的。\x02\x03",
            "下酒的菜都没有了，\x01",
            "所以我叫他们去取一些来。\x02\x03",
            "喂，约修亚，\x01",
            "还有什么可以吃的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没有了，厨师他们好像\x01",
            "已经回去休息了……\x02\x03",
            "我又问了侍女她们，\x01",
            "虽然她们去找了一下，\x01",
            "但下酒菜是的确没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呼，没办法啦。\x01",
            "没有下酒菜就只有忍了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x108, 0x8, 400)
    Sleep(1000)

    ChrTalk(
        0x108,
        (
            "#070F呀……\x01",
            "我想到了一个好办法！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3071():
        OP_9E(0xFE, 0x64, 0x0, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3071)
    OP_92(0x108, 0x8, 0x258, 0x3E8, 0x0)

    ChrTalk(
        0x108,
        (
            "#070F你不介意的话\x01",
            "陪我喝喝酒如何呢？\x02\x03",
            "哇哈哈，美人的笑脸\x01",
            "是最好的下酒佳肴啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x258, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#180F我、我还有任务在身，\x01",
            "恕不奉陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#180F刚才的那件事\x01",
            "先姑且不问……\x02\x03",
            "你们现在就回房间去，\x01",
            "今晚不准再出来。\x02\x03",
            "如果再发现你们的可疑行动，\x01",
            "我会保留调查权利的。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_326E():

        label("loc_326E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_326E")

    QueueWorkItem2(0x101, 1, lambda_326E)

    def lambda_327F():

        label("loc_327F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_327F")

    QueueWorkItem2(0x102, 1, lambda_327F)

    def lambda_3290():

        label("loc_3290")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3290")

    QueueWorkItem2(0x108, 1, lambda_3290)

    ChrTalk(
        0x101,
        "#000F知、知道了还不行吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F已经很晚了，\x01",
            "也应该休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F哼哼，老实点好。\x02\x03",
            "那么……\x01",
            "我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x9)
    OP_6D(710, 9000, 17230, 3000)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)

    ChrTalk(
        0x108,
        (
            "#070F哎呀，这就走掉了……\x02\x03",
            "没办法了……\x01",
            "我回房间去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们也一起回去了吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4222   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_22BA end

    def Function_9_33FC(): pass

    label("Function_9_33FC")

    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x4A38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x3C6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x64, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x10E0, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2058, 0x1C52, 0x34A8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3552, 0x1194, 0x25E4, 0xBB8, 0x0)
    Return()

    # Function_9_33FC end

    def Function_10_3475(): pass

    label("Function_10_3475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3606")
    EventBegin(0x1)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354C")
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
    Jump("loc_35FB")

    label("loc_354C")

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

    label("loc_35FB")

    OP_4B(0xD, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3606")

    Return()

    # Function_10_3475 end

    def Function_11_3607(): pass

    label("Function_11_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3614")
    Return()

    label("loc_3614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_36D4")
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
    Jump("loc_38C4")

    label("loc_36D4")

    EventBegin(0x1)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C5")
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
    Jump("loc_389A")

    label("loc_37C5")

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

    label("loc_389A")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_8C(0xF, 0, 0)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)

    label("loc_38C4")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_11_3607 end

    def Function_12_38CC(): pass

    label("Function_12_38CC")

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

    # Function_12_38CC end

    def Function_13_393A(): pass

    label("Function_13_393A")

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

    # Function_13_393A end

    SaveToFile()

Try(main)
