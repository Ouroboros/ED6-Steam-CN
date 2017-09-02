from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3150   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3150.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '雾香',                                 # 9
        '亚鲁瓦',                               # 10
        '朵洛希',                               # 11
        '玛多克工房长',                         # 12
        '斯坦因',                               # 13
        '埃尔文',                               # 14
        '艾妲',                                 # 15
        '库诺',                                 # 16
        '呆呆',                                 # 17
        '耶鲁克',                               # 18
        '冈多夫',                               # 19
        '王',                                   # 20
        '布鲁诺',                               # 21
        '莫妮卡',                               # 22
        '加鲁诺',                               # 23
        '金',                                   # 24
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02050 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH02620 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01260 ._CH',             # 0A
        'ED6_DT07/CH01760 ._CH',             # 0B
        'ED6_DT07/CH01530 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01190 ._CH',             # 0E
        'ED6_DT07/CH00070 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02050P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH02620P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01260P._CP',             # 0A
        'ED6_DT07/CH01760P._CP',             # 0B
        'ED6_DT07/CH01530P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01190P._CP',             # 0E
        'ED6_DT07/CH00070P._CP',             # 0F
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4220,
        Z                   = 0,
        Y                   = -740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3BA",          # 00, 0
        "Function_1_472",          # 01, 1
        "Function_2_473",          # 02, 2
        "Function_3_489",          # 03, 3
        "Function_4_4AD",          # 04, 4
        "Function_5_61B",          # 05, 5
        "Function_6_68F",          # 06, 6
        "Function_7_710",          # 07, 7
        "Function_8_7D3",          # 08, 8
        "Function_9_820",          # 09, 9
        "Function_10_BE4",         # 0A, 10
        "Function_11_CA5",         # 0B, 11
        "Function_12_E27",         # 0C, 12
        "Function_13_E2C",         # 0D, 13
        "Function_14_192D",        # 0E, 14
        "Function_15_2213",        # 0F, 15
        "Function_16_243F",        # 10, 16
        "Function_17_27A0",        # 11, 17
        "Function_18_27A5",        # 12, 18
        "Function_19_3553",        # 13, 19
        "Function_20_40BA",        # 14, 20
        "Function_21_4CD4",        # 15, 21
        "Function_22_5216",        # 16, 22
        "Function_23_5C8B",        # 17, 23
    )


    def Function_0_3BA(): pass

    label("Function_0_3BA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C6"),
        (SWITCH_DEFAULT, "loc_3DE"),
    )


    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_3DB")

    Jump("loc_3DE")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 4220, 0, -740, 0)

    label("loc_403")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53760, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 52110, 0, 50520, 255)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 59030, 0, 54500, 355)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)

    label("loc_471")

    Return()

    # Function_0_3BA end

    def Function_1_472(): pass

    label("Function_1_472")

    Return()

    # Function_1_472 end

    def Function_2_473(): pass

    label("Function_2_473")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_488")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_473")

    label("loc_488")

    Return()

    # Function_2_473 end

    def Function_3_489(): pass

    label("Function_3_489")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AC")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("Function_3_489")

    label("loc_4AC")

    Return()

    # Function_3_489 end

    def Function_4_4AD(): pass

    label("Function_4_4AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(
        0xFE,
        (
            "呼，说起来\x01",
            "外面还真是吵啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又是主日学校的孩子们\x01",
            "在翘课打闹吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_617")

    label("loc_510")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "这把导力枪\x01",
            "可以将内部驱动导力器的性能\x01",
            "发挥至极限呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说平衡性确实差了点，\x01",
            "很有必要加以改进，\x01",
            "不过也算是在可以忍受的范围内吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总而言之一切还算顺利。\x01",
            "这样的话，\x01",
            "应该可以比预定时间更早做出成品来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617")

    TalkEnd(0xFE)
    Return()

    # Function_4_4AD end

    def Function_5_61B(): pass

    label("Function_5_61B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_68B")

    ChrTalk(
        0x110,
        (
            "#150F小艾，\x01",
            "了解到什么的话要告诉我哦。\x02\x03",
            "我想让这次的特辑\x01",
            "有更多独家新闻。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B")

    TalkEnd(0xFE)
    Return()

    # Function_5_61B end

    def Function_6_68F(): pass

    label("Function_6_68F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_70C")

    ChrTalk(
        0xFE,
        (
            "唉，商品的说明果然\x01",
            "必须像这样写才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "射程……精度……驱动时间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，多么具体啊。\x02",
    )

    CloseMessageWindow()

    label("loc_70C")

    TalkEnd(0xFE)
    Return()

    # Function_6_68F end

    def Function_7_710(): pass

    label("Function_7_710")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_7CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(
        0xFE,
        "……杨？好像不是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那就是……汪？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不，好像两个都不对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CF")

    label("loc_773")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "之前给我担任护卫的那个兄弟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "他到底叫什么来着？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF")

    TalkEnd(0xFE)
    Return()

    # Function_7_710 end

    def Function_8_7D3(): pass

    label("Function_8_7D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_81C")

    ChrTalk(
        0x10E,
        (
            "#130F看来发生了不得了的事情啊……\x01",
            "　\x02\x03",
            "请务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81C")

    TalkEnd(0xFE)
    Return()

    # Function_8_7D3 end

    def Function_9_820(): pass

    label("Function_9_820")

    TalkBegin(0x8)
    FadeToDark(300, 0, 70)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98B")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x40)"), scpexpr(EXPR_END)), "loc_910")
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#790F辛苦了。\x01",
            "看来你们很顺利地完成了任务呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "别忘记回协会报告一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_982")

    label("loc_910")

    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#790F啊，\x01",
            "现在没有需要报告的工作呢。\x02\x03",
            "如果完成其他任务的话，\x01",
            "别忘记回协会报告一下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_982")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_98B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99C")
    TalkEnd(0x8)
    Return()

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_9FF")

    ChrTalk(
        0x8,
        (
            "#790F……已经拿到塞姆里亚苔藓了吧。\x01",
            "　\x02\x03",
            "必须分秒必争。\x01",
            "赶快去礼拜堂吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE0")

    label("loc_9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C")

    ChrTalk(
        0x8,
        (
            "#790F阿加特的情况\x01",
            "已经不容耽搁了。\x02\x03",
            "你们现在赶快去礼拜堂吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE0")

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B83")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 3400, 0, -1800, 0)
    SetChrPos(0x102, 3600, 0, -3160, 0)
    SetChrPos(0x107, 4470, 0, -2270, 0)
    TurnDirection(0x8, 0x101, 0)
    OP_8C(0x17, 180, 0)
    OP_4A(0x17, 255)
    OP_6D(3390, 0, -770, 1000)

    ChrTalk(
        0x8,
        (
            "#790F那么……\x01",
            "教区长怎么说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔说明了关于『塞姆里亚苔藓』的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x17,
        "#073F哦，苔藓吗……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 22)
    Jump("loc_BE0")

    label("loc_B83")


    ChrTalk(
        0x8,
        (
            "#790F金这家伙就供你们随便使唤吧。\x01",
            "　\x02\x03",
            "不用担心，\x01",
            "这种情况他还是能应付得来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE0")

    TalkEnd(0x8)
    Return()

    # Function_9_820 end

    def Function_10_BE4(): pass

    label("Function_10_BE4")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C36")

    ChrTalk(
        0x17,
        (
            "#070F嗯？怎么了？\x02\x03",
            "不是要去教会吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1")

    label("loc_C36")


    ChrTalk(
        0x17,
        (
            "#070F哦，怎么了？\x02\x03",
            "如果打听到什么消息，\x01",
            "赶快去向雾香报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA1")

    TalkEnd(0x17)
    Return()

    # Function_10_BE4 end

    def Function_11_CA5(): pass

    label("Function_11_CA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CF0")

    ChrTalk(
        0xFE,
        (
            "店里面也没有受到损失，\x01",
            "暂且可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E23")

    label("loc_CF0")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "昨天晚上导力停止了，\x01",
            "真是把我吓坏了呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说以前也听说过\x01",
            "只有在特殊的结晶回路中\x01",
            "才会有那种力量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想不到会产生\x01",
            "影响到那么大范围的现象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果这力量用于武器研制的话，\x01",
            "恐怕会导致各国的军力失去平衡。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E23")

    TalkEnd(0xFE)
    Return()

    # Function_11_CA5 end

    def Function_12_E27(): pass

    label("Function_12_E27")

    Call(0, 13)
    Return()

    # Function_12_E27 end

    def Function_13_E2C(): pass

    label("Function_13_E2C")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA4")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_E8D")
    OP_A9(0x4C)
    Jump("loc_E9B")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_E99")
    OP_A9(0x4B)
    Jump("loc_E9B")

    label("loc_E99")

    OP_A9(0x3E)

    label("loc_E9B")

    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_EA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB5")
    TalkEnd(0xD)
    Return()

    label("loc_EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(
        0xD,
        (
            "哦～早上好啊。\x01",
            "这里是贝尔杂货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "本店商品种类非常齐全，\x01",
            "能充分满足各位顾客的要求哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "所以……\x01",
            "想买什么就请来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "本店的经营\x01",
            "也要靠大家的支持。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1929")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FF6")

    ChrTalk(
        0xD,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "贝尔杂货店\x01",
            "今天也会以齐全的商品\x01",
            "来满足大家的要求。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1929")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_122E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10A7")

    ChrTalk(
        0xD,
        (
            "妻子她表示了\x01",
            "对我想法的理解呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "她说店里以后也要像以前那样\x01",
            "保持商品种类的齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "妻子为了我也很努力。\x01",
            "我以后也要\x01",
            "更加努力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122B")

    label("loc_10A7")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        "啊，早上好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天一大早\x01",
            "就有开心的事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "妻子头一次\x01",
            "对我的想法表示理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "她说店里以后也要像以前那样\x01",
            "保持商品种类的齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽说经营方面形势严峻，\x01",
            "但是只要节约开支的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这样的话\x01",
            "我就能安心地和顾客面对面了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122B")

    Jump("loc_1929")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1385")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12BB")

    ChrTalk(
        0xD,
        (
            "唔～通常情况下， \x01",
            "只要我擅作主张降了价，她就会生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天，她心情很不错呢，\x01",
            "发生了什么好事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_12BB")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "总觉得最近\x01",
            "妻子的态度有点奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "她应该知道，出事的时候\x01",
            "我在给镇里面的人分派商品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "……为什么她不生气呢？\x02",
    )

    CloseMessageWindow()

    label("loc_1382")

    Jump("loc_1929")

    label("loc_1385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_14F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13FD")

    ChrTalk(
        0xD,
        (
            "妻子艾妲\x01",
            "肩膀酸疼得厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天也要去\x01",
            "礼拜堂拿药呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EE")

    label("loc_13FD")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "妻子艾妲\x01",
            "肩膀酸疼得厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "今天也要去\x01",
            "礼拜堂拿药呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "中央工房里面\x01",
            "也有研究医学的老师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "但效果还是比不上\x01",
            "传统的医疗法呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EE")

    Jump("loc_1929")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1619")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_158C")

    ChrTalk(
        0xD,
        (
            "我家大儿子\x01",
            "似乎对商品陈列很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "放着他不管的话，\x01",
            "他会整整一天都在搞那些东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_158C")

    OP_A2(0x2)
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(
        0xD,
        "喂喂，库诺。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不要再动\x01",
            "那些商品了好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不是说好了\x01",
            "一天只整理一次商品吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)

    label("loc_1616")

    Jump("loc_1929")

    label("loc_1619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_17AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_169F")

    ChrTalk(
        0xD,
        (
            "整个城市的导力\x01",
            "全部都停止了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "世界上还有\x01",
            "这么不可思议的事呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AC")

    label("loc_169F")

    OP_A2(0x2)

    ChrTalk(
        0xD,
        (
            "昨天晚上\x01",
            "你们没事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我以为是照明灯出故障了，\x01",
            "打算立即去工房看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "谁知一走到外面，\x01",
            "发现整个城镇就像森林里一样漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我马上就意识到\x01",
            "这不是什么简单的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AC")

    Jump("loc_1929")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18A9")

    ChrTalk(
        0xD,
        (
            "我立志要把这个店\x01",
            "经营成受大家喜爱的店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不管什么样的人来，\x01",
            "都能在这里找到称心的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "虽然这样采购的时候会很麻烦，\x01",
            "不过毕竟不努力就不会成功啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1929")

    label("loc_18A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1929")

    ChrTalk(
        0xD,
        (
            "您好，欢迎光临。\x01",
            "这里是贝尔杂货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "从食品到日用品，\x01",
            "这里都一应俱全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1929")

    TalkEnd(0xD)
    Return()

    # Function_13_E2C end

    def Function_14_192D(): pass

    label("Function_14_192D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_19A0")

    ChrTalk(
        0xE,
        (
            "呼，这样子的话\x01",
            "下个月可能也很辛苦吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过，我早已经有思想准备了，\x01",
            "一定要努力渡过难关。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_19A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_19D4")

    ChrTalk(
        0xE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这里是贝尔杂货店。\x01",
            "请慢慢挑选喜欢的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_19D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1AEB")

    ChrTalk(
        0xE,
        (
            "今天早上，我和丈夫商量了一下，\x01",
            "制定了今后的经营方针。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我们决定努力\x01",
            "让商品种类更加齐全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "和以前不同， \x01",
            "采购的活儿由我全部负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这样做到底会怎么样。\x01",
            "不尝试一下不会知道呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_1AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C12")

    ChrTalk(
        0xE,
        (
            "我似乎也开始明白\x01",
            "丈夫的目标了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "他只会常常做梦，\x01",
            "不能说是个会做生意的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "他总想让我们的店\x01",
            "能给大家带来最大的方便和好处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果真能做成这样的店，\x01",
            "的确是很了不起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE9")

    label("loc_1C12")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "听说今天在出事现场，\x01",
            "丈夫给避难的人们\x01",
            "配发了必要物资。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这样的话， \x01",
            "这个月又会是赤字了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "唉，没办法啦。\x01",
            "就当是捐赠，算了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE9")

    Jump("loc_220F")

    label("loc_1CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D7F")

    ChrTalk(
        0xE,
        (
            "真是让人难以置信。\x01",
            "中央工房竟然会遭到袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "为什么丈夫\x01",
            "会发现这件事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2E")

    label("loc_1D7F")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "刚才听说，\x01",
            "中央工房遭到袭击了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "我丈夫也是，\x01",
            "出去后到现在还没有回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "真是让人担心啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1E2E")

    Jump("loc_220F")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1EE8")

    ChrTalk(
        0xE,
        (
            "丈夫他嘴里说着\x01",
            "出了点奇怪的事什么的，\x01",
            "就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "而且还擅自将\x01",
            "店里面的商品也带走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "唉，\x01",
            "他究竟在想什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F83")

    ChrTalk(
        0xE,
        (
            "呼呼，\x01",
            "说起来还有工作没完成呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "时间早的话，收拾一下，\x01",
            "然后去礼拜堂拿点治肩酸的药。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFE")

    label("loc_1F83")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "导力器使用不了的话，\x01",
            "我们就什么都干不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "昨天发生了那样的事情之后，\x01",
            "我们不得不考虑一下这件事情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FFE")

    Jump("loc_220F")

    label("loc_2001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_20AD")

    ChrTalk(
        0xE,
        (
            "如果不进一些好卖的商品，\x01",
            "那就谈不上有什么利润了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "啊，不但肩膀重，\x01",
            "头也开始疼了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2175")

    label("loc_20AD")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "我丈夫也不考虑\x01",
            "商品能不能卖出去，\x01",
            "只会一味地进货又进货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果不清楚这些商品能不能卖掉，\x01",
            "经营起来真的是很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "都不知道他有没有想过\x01",
            "怎么去把生意做好？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2175")

    Jump("loc_220F")

    label("loc_2178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_220F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(
        0xE,
        (
            "呼，一看见账簿\x01",
            "我就觉得肩膀好沉重……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220F")

    label("loc_21D0")

    OP_A2(0x3)

    ChrTalk(
        0xE,
        (
            "哈啊……\x01",
            "真令人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "这个月又快超支了。\x02",
    )

    CloseMessageWindow()

    label("loc_220F")

    TalkEnd(0xE)
    Return()

    # Function_14_192D end

    def Function_15_2213(): pass

    label("Function_15_2213")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2260")

    ChrTalk(
        0xFE,
        "唔，真是少见呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "妈妈她\x01",
            "竟然会表扬爸爸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_2260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_22F6")

    ChrTalk(
        0xFE,
        (
            "爸爸他为什么要拿走\x01",
            "各种各样的东西啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "药品、食品什么的也就罢了，\x01",
            "带着人偶打算干什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还一副\x01",
            "慌慌张张的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_22F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_233A")

    ChrTalk(
        0xFE,
        "……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……嗯。\x01",
            "这下就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "已经没有我\x01",
            "去帮忙的必要了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_243B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_23C4")

    ChrTalk(
        0xFE,
        (
            "虽然爸爸说\x01",
            "一天整理一次商品就行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过客人已经动过了，\x01",
            "必须按照原样放好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243B")

    label("loc_23C4")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "然后将这条鱼放回左边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯，这下就好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，终于又回到\x01",
            "最完美的陈列状态了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243B")

    TalkEnd(0xFE)
    Return()

    # Function_15_2213 end

    def Function_16_243F(): pass

    label("Function_16_243F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_24D6")

    ChrTalk(
        0xFE,
        "博士！不得了了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "妈妈的肩\x01",
            "好像开始疼起来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么！赶快啊。\x01",
            "快点和教区长联系！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_24D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2512")

    ChrTalk(
        0xFE,
        (
            "今天去\x01",
            "肯定还来得及。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_2512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2541")

    ChrTalk(
        0xFE,
        "我说，妈妈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "爸爸在哪儿呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_2541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_25A3")

    ChrTalk(
        0xFE,
        (
            "昨天晚上\x01",
            "外面好暗呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我睡在床上\x01",
            "都看见了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_25A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_276A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_265C")

    ChrTalk(
        0xFE,
        (
            "博士！\x01",
            "导力压下降了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么！\x01",
            "导力引擎的功率很正常啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2767")

    label("loc_265C")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "哇～啊，\x01",
            "是提妲姐～姐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们来玩导力技师游戏吧。\x01",
            "玩导力技师游戏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F不好意思啊，呆呆。\x01",
            "姐姐现在要给客人们带路啊。\x02\x03",
            "#061F所以呢，还是再下次玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，好吧～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我明白～了，提妲博士。\x02",
    )

    CloseMessageWindow()

    label("loc_2767")

    Jump("loc_279C")

    label("loc_276A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_279C")

    ChrTalk(
        0xFE,
        "姐姐～你们是谁～啊？\x02",
    )

    CloseMessageWindow()

    label("loc_279C")

    TalkEnd(0xFE)
    Return()

    # Function_16_243F end

    def Function_17_27A0(): pass

    label("Function_17_27A0")

    Call(0, 18)
    Return()

    # Function_17_27A0 end

    def Function_18_27A5(): pass

    label("Function_18_27A5")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2805")
    OP_0D()
    OP_A9(0x3D)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_2805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2816")
    TalkEnd(0x11)
    Return()

    label("loc_2816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_28F4")

    ChrTalk(
        0x11,
        (
            "不管怎么说\x01",
            "老板也是个成功的人，\x01",
            "值得学习的地方我也要学着点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "唉，\x01",
            "就是觉得他思想有点顽固……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "把这些也算在\x01",
            "学习范围之内吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A06")

    label("loc_28F4")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "昨天，和斯坦因老板\x01",
            "商量了一下采购的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "暂时先决定按照\x01",
            "老板的意向来选择商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过我并没有完全理解\x01",
            "这位重视可靠性的\x01",
            "斯坦因老板的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "啊，这也是需要学习的地方吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2A06")

    Jump("loc_354F")

    label("loc_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2A97")

    ChrTalk(
        0x11,
        (
            "唔，\x01",
            "那个加鲁诺竟然会这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我也渐渐觉得\x01",
            "老板的话有些合理了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "……不、不行。\x01",
            "不能受别人的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4A")

    label("loc_2A97")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "今天一大清早加鲁诺就来了，\x01",
            "只说了一句『我明白老板话里的意思了』，\x01",
            "之后就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "唔，\x01",
            "那个加鲁诺竟然会这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "老板的想法\x01",
            "到底哪里正确了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4A")

    Jump("loc_354F")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2BB0")

    ChrTalk(
        0x11,
        "唔，加鲁诺那家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不知道怎么\x01",
            "就被斯坦因老板给教唆了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C33")

    label("loc_2BB0")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "今天一大清早加鲁诺就来了，\x01",
            "只说了一句『我明白老板话里的意思了』，\x01",
            "之后就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "那家伙\x01",
            "到底怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C33")

    Jump("loc_354F")

    label("loc_2C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2C93")

    ChrTalk(
        0x11,
        "哦，这么晚还有客人来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "店还没有关门，\x01",
            "请放心挑选我们的商品吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354F")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2CFA")

    ChrTalk(
        0x11,
        "有什么损失吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "要是研究计划\x01",
            "没受影响就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D72")

    label("loc_2CFA")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "喂，你们听说了吗？\x01",
            "中央工房遭到袭击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "当时我在店里面忙着聊天，\x01",
            "一点都没有注意到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D72")

    Jump("loc_354F")

    label("loc_2D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2EF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2DE3")

    ChrTalk(
        0x11,
        (
            "哇，\x01",
            "真的是一把非常棒的导力枪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "平衡性若是再好些，\x01",
            "我想肯定会更加畅销的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2DE3")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "中央工房的加鲁诺\x01",
            "把研究中的导力枪带来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "那家伙真厉害。\x01",
            "真是把很棒的导力枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过整体的平衡性有些特殊\x01",
            "导致难以操作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "就算操作多多少少有点难，\x01",
            "不过只要威力强大就足以弥补了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF3")

    Jump("loc_354F")

    label("loc_2EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_310F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2F7A")

    ChrTalk(
        0x11,
        (
            "啊啊，加鲁诺……\x01",
            "快把试制品拿来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "最近唯一的期盼\x01",
            "就是能看到那件产品了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310C")

    label("loc_2F7A")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        "呵呵，欢迎啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "哎呀，\x01",
            "又和斯坦因老板因为采购的事\x01",
            "而发生争执了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不管我们怎么说，\x01",
            "他就是不愿意引进\x01",
            "还处于研究阶段的导力枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "虽然我已经尽可能劝说他了，\x01",
            "不过我只是个被雇来的店长，没有权利管他啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "啊啊，加鲁诺……\x01",
            "快把试制品拿来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "最近嘛，\x01",
            "只有这么点期盼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310C")

    Jump("loc_354F")

    label("loc_310F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_319B")

    ChrTalk(
        0x11,
        (
            "中央工房里面\x01",
            "现在一定乱成一团了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "因为那里\x01",
            "全都是测量用的机器呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_319B")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "昨天晚上，\x01",
            "我正在调整导力枪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "突然，\x01",
            "测量器停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "我还以为把商品弄坏了，\x01",
            "当时一下子傻了眼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")

    Jump("loc_354F")

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_348F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_32D5")

    ChrTalk(
        0x11,
        (
            "我虽然也明白老板\x01",
            "把武器的可靠性放在第一位的信条……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过稍微想想，\x01",
            "老板是否有点太过固执了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348C")

    label("loc_32D5")

    OP_A2(0x6)

    ChrTalk(
        0x11,
        (
            "我们这里的老板是斯坦因，\x01",
            "就住在这附近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "根据斯坦因先生的原则，\x01",
            "我们是绝对不会引进\x01",
            "最先进的高尖端武器的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "这好像是因为\x01",
            "过于先进的武器\x01",
            "可靠性还得不到认可……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "有个工房的研究员亲自来出售\x01",
            "正在研究中的超级导力枪，\x01",
            "也被老板拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348C")

    Jump("loc_354F")

    label("loc_348F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_354F")

    ChrTalk(
        0x11,
        (
            "哦，欢迎光临。\x01",
            "这里是斯坦因武器商会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "本店全是各种各样的好商品。\x01",
            "请慢慢地看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_354F")

    TalkEnd(0x11)
    Return()

    # Function_18_27A5 end

    def Function_19_3553(): pass

    label("Function_19_3553")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_36CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_35F3")

    ChrTalk(
        0xFE,
        (
            "虽说我也很在意博士这件事，\x01",
            "不过现在也只有相信阿加特那家伙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "毕竟我们身上也有些\x01",
            "非做不可的任务啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C8")

    label("loc_35F3")


    ChrTalk(
        0xFE,
        (
            "哦，是你们啊。\x01",
            "我听说你们的营救作战了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然事情还不算完美解决，\x01",
            "不过现在也只有相信阿加特那家伙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是那家伙出马， \x01",
            "应该能让博士他们安全逃离的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C8")

    Jump("loc_40B6")

    label("loc_36CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_END)), "loc_379F")

    ChrTalk(
        0xFE,
        (
            "王那家伙好像也是充满干劲地工作着，\x01",
            "这样我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前还担心他会因为\x01",
            "觉得自己应该对事故负责\x01",
            "而意志消沉下来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是雾香\x01",
            "用什么巧妙的办法激励他了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA3")

    label("loc_379F")

    OP_A2(0x57E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_3861")

    ChrTalk(
        0x101,
        "#000F啊，冈多夫先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是刚从王都回来的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，我刚得知了消息。\x01",
            "然后就匆匆忙忙赶回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "雾香她已经告诉我\x01",
            "这边大概的事情了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿加特那家伙\x01",
            "已经没事了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_3861")


    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们就是那两个准游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是蔡斯所属的游击士，\x01",
            "名叫冈多夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听到消息之后， \x01",
            "就从出差地王都赶了回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大体情况我已经问过雾香了……\x01",
            "呃，阿加特他没事吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3945")


    ChrTalk(
        0x101,
        (
            "#000F嗯，还好度过了危险期……\x02\x03",
            "……哎，你认识阿加特吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，因为工作的关系\x01",
            "我们已经见过很多次面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很久之前他\x01",
            "就已经是个非常有名的家伙啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……总之，\x01",
            "他没事就好啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，搜查的工作\x01",
            "就交给你们和阿加特了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而我们就尽量去\x01",
            "处理一些日常的零碎工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，谢谢。\x02\x03",
            "那就拜托您了。\x01",
            "冈多夫先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，你们要保重哦。\x02",
    )

    CloseMessageWindow()

    label("loc_3BA3")

    Jump("loc_40B6")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_40B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403A")
    OP_A2(0x57D)

    ChrTalk(
        0x13,
        "嗯？　出差！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "冈多夫先生你……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "因为军方直接点名……\x01",
            "我必须去一趟王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "又不是只剩下你一个，\x01",
            "那些准游击士也在嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们同心协力的话，\x01",
            "两三天肯定能应付过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "是啊，是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "我明白了。\x01",
            "我会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "哦……\x01",
            "总之乐观一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(
        0x12,
        (
            "……哦，\x01",
            "这就是传闻中的两个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们两个\x01",
            "来得真是时候啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E33")
    OP_A2(0x57C)

    ChrTalk(
        0x13,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "难道……\x01",
            "你们就是那些准游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……嗯？\x02\x03",
            "啊，没错。\x01",
            "我们就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面。\x01",
            "我是准游击士约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E81")

    label("loc_3E33")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "啊，\x01",
            "是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "你们来得正是时候。\x02",
    )

    CloseMessageWindow()

    label("loc_3E81")


    ChrTalk(
        0x12,
        "呵呵，果然是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "看到你们，\x01",
            "我终于明白雾香说的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "请问您要去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "啊啊，没错。\x01",
            "那边有很紧急的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "蔡斯支部的工作\x01",
            "就交给你们和王负责了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "你们就好好努力吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "……就是这样。\x01",
            "总之希望能借助你们的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好，我们会尽全力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "那就这样吧。\x01",
            "拜托你们留守了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_40B6")

    label("loc_403A")


    ChrTalk(
        0x12,
        (
            "不好意思，\x01",
            "拜托你们在这里留守了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们要和王那家伙\x01",
            "好好合作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B6")

    TalkEnd(0x12)
    Return()

    # Function_19_3553 end

    def Function_20_40BA(): pass

    label("Function_20_40BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_420A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_415A")

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "听说你们要去王都了对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没关系，\x01",
            "你们肯定能够很快成为正游击士的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后也要精力充沛地\x01",
            "努力工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4207")

    label("loc_415A")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听说了哦，\x01",
            "营救作战按照计划顺利实行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然博士他们以后会怎样\x01",
            "现在还不能放心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，很感谢你们。\x01",
            "谢谢把他们救了出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4207")

    Jump("loc_4CD0")

    label("loc_420A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_471D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469E")
    OP_A2(0x57D)

    ChrTalk(
        0x13,
        "嗯？　出差！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "冈多夫先生你……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "因为军方直接点名……\x01",
            "我必须去一趟王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "又不是只剩下你一个，\x01",
            "那些准游击士也在嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们同心协力的话，\x01",
            "两三天肯定能应付过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "是啊，是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "我明白了。\x01",
            "我会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "哦……\x01",
            "总之乐观一点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(
        0x12,
        (
            "……哦，\x01",
            "这就是传闻中的两个人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "你们两个\x01",
            "来得真是时候啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4497")
    OP_A2(0x57C)

    ChrTalk(
        0x13,
        "……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "难道……\x01",
            "你们就是那些准游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……嗯？\x02\x03",
            "啊，没错。\x01",
            "我们就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面。\x01",
            "我是准游击士约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊。\x01",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E5")

    label("loc_4497")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0x13,
        (
            "啊，\x01",
            "是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "你们来得正是时候。\x02",
    )

    CloseMessageWindow()

    label("loc_44E5")


    ChrTalk(
        0x12,
        "呵呵，果然是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "看到你们，\x01",
            "我终于明白雾香说的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "请问您要去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "啊啊，没错。\x01",
            "那边有很紧急的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "蔡斯支部的工作\x01",
            "就交给你们和王负责了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "你们就好好努力吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "……就是这样。\x01",
            "总之希望能借助你们的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好，我们会尽全力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "那就这样吧。\x01",
            "拜托你们留守了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_471A")

    label("loc_469E")


    ChrTalk(
        0xFE,
        (
            "接下来一段时间\x01",
            "冈多夫先生要到别的地方出差……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好吧，今后的工作， \x01",
            "必须更加充满干劲去做才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望你们\x01",
            "也能够协助我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471A")

    Jump("loc_4CD0")

    label("loc_471D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B09")
    OP_A2(0x57C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_477D")

    ChrTalk(
        0xFE,
        "啊啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "竟然会来武器店，真少见啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_479E")

    label("loc_477D")


    ChrTalk(
        0xFE,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "原来是提妲来了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479E")


    ChrTalk(
        0xFE,
        (
            "咦……？\x01",
            "这两位不会是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是的。\x01",
            "他们都是游击士哦。\x02\x03",
            "我现在要带他们\x01",
            "到我家里去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，果然是这样啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的名字叫做王。\x01",
            "是蔡斯支部所属的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在还是个新人，\x01",
            "和你们差不多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，是这样啊。请多关照。\x02\x03",
            "我是准游击士艾丝蒂尔。\x01",
            "旁边的那位是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是约修亚，\x02\x03",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我之前听雾香说过\x01",
            "有关你们的事情。\x01",
            "果然来了很厉害的准游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说你们在全国各地\x01",
            "都做出了相当的成绩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，就算是这样吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说到成绩，\x01",
            "我们只是尽了自己的本分而已。\x02\x03",
            "而且多亏得到了游击士前辈\x01",
            "和各地百姓的鼎力相助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "我觉得能够得到百姓信任，\x01",
            "得到他们的帮助也是一种才能呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实际上，\x01",
            "我们支部也处于人手不足的状态。\x01",
            "我相当期待你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后这段时间\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F还请以后多多指教。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B6E")

    label("loc_4B09")


    ChrTalk(
        0xFE,
        (
            "哟，艾丝蒂尔、约修亚。\x01",
            "我相当期待你们今后的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许相处时间不会太长，\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6E")

    Jump("loc_4CD0")

    label("loc_4B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4C1C")

    ChrTalk(
        0xFE,
        (
            "是选平衡性呢，\x01",
            "还是选突出的特性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，归根到底\x01",
            "还是要看使用者的本事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我大概还没有可以\x01",
            "选择武器的实力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD0")

    label("loc_4C1C")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "唔，好难啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是选性能比较平衡的武器呢，\x01",
            "还是选非常有特点的武器呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是能二者兼顾的话，\x01",
            "就不用那么烦恼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD0")

    TalkEnd(0xFE)
    Return()

    # Function_20_40BA end

    def Function_21_4CD4(): pass

    label("Function_21_4CD4")

    EventBegin(0x0)
    ClearMapFlags(0x10000000)
    OP_A2(0x58E)
    SetChrPos(0x101, 1750, 0, -4500, 53)
    SetChrPos(0x102, 730, 0, -5190, 44)
    SetChrPos(0x107, 1790, 0, -5680, 57)
    SetChrPos(0x17, 4240, 0, -800, 17)
    OP_4A(0x17, 255)
    OP_4A(0x8, 255)
    OP_6D(2460, 0, -2580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x17, 180, 400)

    ChrTalk(
        0x17,
        "#070F哦哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，金先生！\x01",
            "原来你还在这啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DF5():
        OP_6D(3390, 0, -770, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DF5)

    def lambda_4E0D():
        OP_8E(0xFE, 0xD48, 0x0, 0xFFFFF8F8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E0D)
    Sleep(300)

    def lambda_4E2D():
        OP_8E(0xFE, 0x1176, 0x0, 0xFFFFF722, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4E2D)
    Sleep(300)

    def lambda_4E4D():
        OP_8E(0xFE, 0xE10, 0x0, 0xFFFFF3A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E4D)

    def lambda_4E68():

        label("loc_4E68")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4E68")

    QueueWorkItem2(0x101, 1, lambda_4E68)

    def lambda_4E79():

        label("loc_4E79")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4E79")

    QueueWorkItem2(0x102, 1, lambda_4E79)

    def lambda_4E8A():

        label("loc_4E8A")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_4E8A")

    QueueWorkItem2(0x107, 1, lambda_4E8A)
    Sleep(2000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F刚才真是多谢\x01",
            "你帮忙把阿加特背回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是麻烦您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#071F哇哈哈，别客气。\x01",
            "同行就是要相互帮助的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#790F那么……\x01",
            "阿加特的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F那个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5144")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们把阿加特的情况\x01",
            "和皮克塞恩教区长的事情说明了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x17,
        (
            "#072F唔……\x01",
            "情况比想象的更危险啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F教会的传统医疗法吗……\x02\x03",
            "现在也只能\x01",
            "赌一赌这种可能性了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，\x01",
            "总之现在要赶快去礼拜堂看看。\x02\x03",
            "我们在这里说话的时候，\x01",
            "阿加特一直在受苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那么，\x01",
            "我们这就去七耀教会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#790F嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Jump("loc_5215")

    label("loc_5144")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们把阿加特的情况\x01",
            "和『塞姆里亚苔藓』的事情说明了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x17,
        (
            "#072F唔……\x01",
            "情况比想象的更危险啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Call(0, 22)

    label("loc_5215")

    Return()

    # Function_21_4CD4 end

    def Function_22_5216(): pass

    label("Function_22_5216")

    OP_31(0x7, 0x0, 0x1B)
    OP_B5(0x7, 0x0)
    OP_B5(0x7, 0x1)
    OP_B5(0x7, 0x2)
    OP_B5(0x7, 0x3)
    OP_B5(0x7, 0x4)
    OP_B5(0x7, 0x5)
    OP_41(0x7, 0xD3)
    OP_41(0x7, 0xF5)
    OP_41(0x7, 0x113)
    OP_41(0x7, 0x261, 0x0)
    OP_41(0x7, 0x259, 0x1)
    OP_41(0x7, 0x25E, 0x2)
    OP_41(0x7, 0x274, 0x3)
    OP_35(0x7, 0xDC)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDF)
    OP_36(0x7, 0x109)
    AddParty(0x7, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x101, 3400, 0, -1800, 0)
    SetChrPos(0x102, 3600, 0, -3160, 0)
    SetChrPos(0x107, 4470, 0, -2270, 0)
    SetChrPos(0x108, 4220, 0, -740, 180)
    OP_6D(3390, 0, -770, 1200)

    ChrTalk(
        0x8,
        (
            "#790F那个『塞姆里亚苔藓』，\x01",
            "教会以前确实委托我们采集过。\x02\x03",
            "#792F请稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_533A():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_533A)
    OP_8C(0x8, 180, 400)

    def lambda_534F():
        OP_6D(3980, 0, 800, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_534F)
    OP_8E(0x8, 0xE10, 0x0, 0x956, 0x5DC, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#790F……找到了。\x02\x03",
            "是在卡鲁迪亚钟乳洞西北区域的\x01",
            "洞窟湖的岸边采集到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F钟乳洞的西北……洞窟湖对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F在手册上记下吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#790F不过事先说明……\x01",
            "那个钟乳洞里的魔兽相当难对付。\x02\x03",
            "以前采集的时候，\x01",
            "都是由四个经验丰富的游击士\x01",
            "组成队伍在那里进行药料搜索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F四、四个游击士！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F的确很麻烦的样子。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(
        0x108,
        "#070F#4P唔，那样的话……\x02",
    )

    CloseMessageWindow()

    def lambda_55DD():
        OP_6D(3390, 0, -770, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_55DD)
    OP_8E(0x8, 0xE88, 0x0, 0x514, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "#791F就是因为这样，\x01",
            "你们就把这男人一起带去好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 0)

    ChrTalk(
        0x108,
        "#075F……（晕倒）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 600)

    ChrTalk(
        0x108,
        (
            "#072F喂，我说！\x01",
            "不要随便替我做决定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#792F怎么了，\x01",
            "你不打算陪他们去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#073F那、那倒不是……\x02\x03",
            "#075F真是的……\x01",
            "你的性格还真是一点都没变啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#791F多谢夸奖。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#072F谁夸奖你，才不是！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#506F呵呵，那个……\x02\x03",
            "关键就是说，\x01",
            "金先生也会陪我们去钟乳洞吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 180, 400)

    ChrTalk(
        0x108,
        (
            "#070F啊，是的……\x01",
            "这也是一种缘分嘛。\x02\x03",
            "明天我就要去王都，\x01",
            "所以只能在今天内为你们一尽绵力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F足够了！\x01",
            "这样已经帮了我们大忙啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那就请多多指教了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)
    OP_8C(0x107, 270, 400)

    ChrTalk(
        0x107,
        (
            "#063F#4P那、那个……\x01",
            "艾丝蒂尔姐姐、约修亚哥哥……\x02\x03",
            "我也想去……可以吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5967():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5967)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        "#004F#5P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#561F#4P我也知道……\x01",
            "自己只会碍手碍脚的……\x02\x03",
            "但是……但是呢。\x02\x03",
            "#069F阿加特大哥哥\x01",
            "是因为我才会受伤的……\x02\x03",
            "要是不能为他做点什么的话，\x01",
            "我……会恨死自己的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#5P提妲……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#005F#5P喂，约修亚。\x01",
            "就当我再次求求你了！\x02\x03",
            "让她跟着我们一起去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F真没办法……\x02\x03",
            "#012F我说，提妲……\x02\x03",
            "你能向我们保证\x01",
            "这次绝对不会再乱来吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B0A():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B0A)

    ChrTalk(
        0x107,
        "#062F#4P嗯、嗯，保证……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，就这样决定了。\x01",
            "金先生也不会介意吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊哈哈。\x01",
            "我当然不介意啦。\x02\x03",
            "#071F多指教了，小姑娘。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x108, 400)

    ChrTalk(
        0x107,
        "#560F啊……是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P好的，既然商量好的话，\x01",
            "那我们马上向钟乳洞出发吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F首先要到中央工房地下，\x01",
            "乘导力梯到卡鲁迪亚隧道吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x552)
    OP_28(0x42, 0x1, 0x20)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_22_5216 end

    def Function_23_5C8B(): pass

    label("Function_23_5C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_5CA8")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_5D37")

    label("loc_5CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_5CC5")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_5D37")

    label("loc_5CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5CE0")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_5D37")

    label("loc_5CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_5CFB")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_5D37")

    label("loc_5CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5D16")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_5D37")

    label("loc_5D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_5D29")
    OP_2A(0x2D, 0x32, 0x2A, 0xFFFF)
    Jump("loc_5D37")

    label("loc_5D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5D37")
    OP_2A(0x2D, 0x32, 0xFFFF)

    label("loc_5D37")

    TalkEnd(0xFF)
    Return()

    # Function_23_5C8B end

    SaveToFile()

Try(main)
