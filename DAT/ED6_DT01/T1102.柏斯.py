from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1102   ._SN',
        MapName             = 'Bose',
        Location            = 'T1102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '售票员泰德',                           # 9
        '拉克斯',                               # 10
        '诺尔姆',                               # 11
        '阿尔丹',                               # 12
        '哈尔德',                               # 13
        '贝尔娜',                               # 14
        '飞空艇',                               # 15
        '飞空艇影子',                           # 16
        '柏斯市·北街区',                       # 17
    )

    DeclEntryPoint(
        Unknown_00              = 46000,
        Unknown_04              = 0,
        Unknown_08              = 16500,
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT06/CH20038 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT06/CH20038P._CP',             # 05
    )

    DeclNpc(
        X                   = 46050,
        Z                   = 0,
        Y                   = 19400,
        Direction           = 180,
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
        X                   = 27300,
        Z                   = -10000,
        Y                   = 26800,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 48500,
        Z                   = 1500,
        Y                   = 36800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 1500,
        Y                   = 47600,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 29100,
        Z                   = -3000,
        Y                   = 17200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 51400,
        Z                   = 0,
        Y                   = 14100,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 0,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48090,
        Z                   = 3000,
        Y                   = -20910,
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


    DeclActor(
        TriggerX            = 46070,
        TriggerZ            = 0,
        TriggerY            = 18140,
        TriggerRange        = 600,
        ActorX              = 46050,
        ActorZ              = 1500,
        ActorY              = 19400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47780,
        TriggerZ            = 0,
        TriggerY            = 15880,
        TriggerRange        = 800,
        ActorX              = 47780,
        ActorZ              = 2200,
        ActorY              = 15880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34950,
        TriggerZ            = -10000,
        TriggerY            = 24520,
        TriggerRange        = 800,
        ActorX              = 34950,
        ActorZ              = -7800,
        ActorY              = 24520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60000,
        TriggerZ            = 0,
        TriggerY            = 17090,
        TriggerRange        = 800,
        ActorX              = 60000,
        ActorZ              = 1500,
        ActorY              = 17090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_368",          # 01, 1
        "Function_2_44B",          # 02, 2
        "Function_3_5C8",          # 03, 3
        "Function_4_5CD",          # 04, 4
        "Function_5_10B4",         # 05, 5
        "Function_6_1957",         # 06, 6
        "Function_7_251D",         # 07, 7
        "Function_8_2FBF",         # 08, 8
        "Function_9_37AE",         # 09, 9
        "Function_10_3DA9",        # 0A, 10
        "Function_11_51D6",        # 0B, 11
        "Function_12_521F",        # 0C, 12
        "Function_13_527B",        # 0D, 13
        "Function_14_52F1",        # 0E, 14
        "Function_15_5370",        # 0F, 15
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2E7")
    SetChrPos(0xA, 33980, -9750, 27260, 0)
    SetChrPos(0x9, 51270, 1800, 37990, 90)
    SetChrPos(0xB, 51220, 1500, 51120, 90)
    SetChrPos(0xC, 45170, 0, 17540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E4")
    SetChrFlags(0xC, 0x80)

    label("loc_2E4")

    Jump("loc_350")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_344")
    SetChrPos(0xA, 33980, -9750, 27260, 0)
    SetChrPos(0x9, 51270, 1800, 37990, 90)
    SetChrPos(0xB, 48710, 1500, 33310, 315)
    SetChrPos(0xC, 45170, 0, 17540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xC, 0x80)

    label("loc_341")

    Jump("loc_350")

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_350")
    SetChrFlags(0xC, 0x80)

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_367")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_367")

    Return()

    # Function_0_28A end

    def Function_1_368(): pass

    label("Function_1_368")

    OP_16(0x2, 0xFA0, 0xFFFE8518, 0xFFFE98A0, 0x30042)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C5")
    OP_B1("T1102_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    Jump("loc_44A")

    label("loc_3C5")

    OP_B1("T1102_2")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_6F(0xB, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402")
    OP_72(0x7, 0x4)
    OP_72(0x8, 0x4)
    Jump("loc_413")

    label("loc_402")

    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_6F(0xC, 100)

    label("loc_413")

    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_436")
    OP_72(0x9, 0x4)
    OP_72(0xA, 0x4)
    Jump("loc_440")

    label("loc_436")

    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)

    label("loc_440")

    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)

    label("loc_44A")

    Return()

    # Function_1_368 end

    def Function_2_44B(): pass

    label("Function_2_44B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_470")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B2")

    label("loc_470")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_489")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5B2")

    label("loc_489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5B2")

    label("loc_4A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5B2")

    label("loc_4BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5B2")

    label("loc_4D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5B2")

    label("loc_4ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_506")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5B2")

    label("loc_506")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5B2")

    label("loc_51F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_538")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5B2")

    label("loc_538")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_551")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5B2")

    label("loc_551")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5B2")

    label("loc_56A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_583")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5B2")

    label("loc_583")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5B2")

    label("loc_59C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B2")

    label("loc_5C7")

    Return()

    # Function_2_44B end

    def Function_3_5C8(): pass

    label("Function_3_5C8")

    Call(0, 4)
    Return()

    # Function_3_5C8 end

    def Function_4_5CD(): pass

    label("Function_4_5CD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "虽然犯人们终于被抓获了，\x01",
            "不过这样的事件\x01",
            "毕竟还是发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "乘客之中也有人\x01",
            "提出了各种各样的疑虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们得重新审视一下\x01",
            "定期船的安保方案才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_777")

    label("loc_6DE")


    ChrTalk(
        0x8,
        (
            "虽然犯人们已经被抓获，\x01",
            "不过这样的事件毕竟还是发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们得重新审视一下\x01",
            "定期船的安保方案才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_777")

    Jump("loc_10B0")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "『赛希莉亚号』\x01",
            "刚才往卢安方向飞走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呼……之后就是\x01",
            "东向航线的『林德号』了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然飞艇被发现的时候没出什么问题，\x01",
            "但听说现在仍然在军队的监控下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想可能要等它回到公社之后，\x01",
            "才可以决定能否重新起航吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_923")

    label("loc_8B6")


    ChrTalk(
        0x8,
        (
            "我想可能要等\x01",
            "东向航线的『林德号』回到公社之后，\x01",
            "才可以决定能否重新起航吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_923")

    Jump("loc_10B0")

    label("loc_926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D3")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "虽然只有『赛希莉亚号』能投入运营，\x01",
            "但是定期船恢复通航也算是个好消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "各位搭乘本飞艇的旅客，\x01",
            "请从这边的门进入！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC4")

    label("loc_9D3")


    ChrTalk(
        0x8,
        (
            "梅贝尔市长\x01",
            "终于将一系列的案件说明清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "原来『林德号』失踪等等事情\x01",
            "都是空贼所为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我非常担心\x01",
            "那些乘客是否安全……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC4")

    Jump("loc_10B0")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "如果再这样继续停航下去，\x01",
            "公社的信用就丧失殆尽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以前没有发生过这样的事故，\x01",
            "也不曾处理过这样的问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果能尽快\x01",
            "把情况说明清楚就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C91")

    label("loc_BE4")


    ChrTalk(
        0x8,
        (
            "如果再这样继续停航下去，\x01",
            "公社的信用就丧失殆尽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果能尽快\x01",
            "把情况说明清楚就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C91")

    Jump("loc_10B0")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAA")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "公社那边也还没有\x01",
            "收到来自军队的任何说明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "超市那边进货出货等事宜\x01",
            "也停滞下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从各个地方都相继\x01",
            "传来了不满和抱怨啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5A")

    label("loc_DAA")


    ChrTalk(
        0x8,
        (
            "超市那边进货出货等事宜\x01",
            "也停滞下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从各个地方都相继\x01",
            "传来了不满和抱怨啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5A")

    Jump("loc_10B0")

    label("loc_E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "现在，\x01",
            "定期船的航行计划被无限期推迟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且非常抱歉的是， \x01",
            "这停航的状态不知道何时能解除。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCF")

    label("loc_F02")


    ChrTalk(
        0x8,
        (
            "虽然我对乘客们说明了情况，\x01",
            "但是连我自己也不知道\x01",
            "定期船失踪的真正原因……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "王国军队的搜索，\x01",
            "到底进行得怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCF")

    Jump("loc_10B0")

    label("loc_FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(
        0x8,
        (
            "定期船现在仍然处于停航状态，\x01",
            "重新开航的期限到现在也没有确定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对一直在空港等候的各位，\x01",
            "我代表公社表示万分的歉意……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B0")

    TalkEnd(0x8)
    Return()

    # Function_4_5CD end

    def Function_5_10B4(): pass

    label("Function_5_10B4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AB")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "经历了这样的事件之后，\x01",
            "检修工作要更加用心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了恢复公社的信誉，\x01",
            "必须要努力工作才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1210")

    label("loc_11AB")


    ChrTalk(
        0xFE,
        (
            "经历了这样的事件之后，\x01",
            "检修工作要更加用心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1210")

    Jump("loc_1953")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_13BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1317")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "被发现的『林德号』\x01",
            "好像还不能重新起航。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也难怪，机长、乘务员\x01",
            "还有乘客一个都没有找到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是急人啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_13BB")

    label("loc_1317")


    ChrTalk(
        0xFE,
        (
            "被发现的『林德号』\x01",
            "好像还不能重新起航。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这也难怪，机长、乘务员\x01",
            "还有乘客一个都没有找到呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BB")

    Jump("loc_1953")

    label("loc_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_1483")

    ChrTalk(
        0xFE,
        (
            "因为王国军的警备飞艇要优先考虑，\x01",
            "『赛希莉亚号』的检修只能晚一些进行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此，\x01",
            "定期船的出发时间也只能推迟了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A2")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "在卢安待命的\x01",
            "『赛希莉亚号』来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且没有想到的是，\x01",
            "连雷斯顿要塞的警备飞艇也出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也要摩拳擦掌啦……\x01",
            "虽然这么说，\x01",
            "不过感觉手艺生疏了很多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_15A2")


    ChrTalk(
        0xFE,
        (
            "在卢安待命的\x01",
            "『赛希莉亚号』来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且没有想到的是，\x01",
            "连雷斯顿要塞的警备飞艇也出动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1642")

    Jump("loc_1953")

    label("loc_1645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1732")

    ChrTalk(
        0xFE,
        (
            "我觉得至少让西向航线的\x01",
            "『赛希莉亚号』能够起航也好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "警戒如此的森严，\x01",
            "看来事态还真是严重啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1791")

    ChrTalk(
        0xFE,
        "啊呀啊呀，真是辛苦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "光在这里等着就很辛苦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1953")

    label("loc_1791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_190E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "让我们在此待命，\x01",
            "到底是因为公社也还没弄清情况呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是说，\x01",
            "已经派飞艇过来了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……已经这么久了，\x01",
            "连个说明也没有，\x01",
            "大概公社也搞不清现状吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190B")

    label("loc_189C")


    ChrTalk(
        0xFE,
        (
            "这么久了也没有联络。\x01",
            "大概公社也搞不清现状吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190B")

    Jump("loc_1953")

    label("loc_190E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(
        0xFE,
        "飞艇还是没有来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底是怎么一回事……\x02",
    )

    CloseMessageWindow()

    label("loc_1953")

    TalkEnd(0x9)
    Return()

    # Function_5_10B4 end

    def Function_6_1957(): pass

    label("Function_6_1957")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_19C8")

    ChrTalk(
        0xFE,
        (
            "飞往帝国的国际航线\x01",
            "也一直处于停航状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果能赶快恢复就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B05")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "虽然今天没有来，\x01",
            "不过这里还是帝国商用飞艇停靠的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它们都是为了运送货物\x01",
            "而到柏斯超市来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因为如此，\x01",
            "这里的飞艇坪有两个跑道哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有两个跑道的城市，\x01",
            "除了这里就只有王都格兰赛尔了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF6")

    label("loc_1B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2E")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "因为有两个跑道，\x01",
            "所以要比其他的飞艇坪繁忙多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，干这项工作，\x01",
            "在飞艇平安起飞的瞬间，\x01",
            "我们能得到非常大的充实感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有时候会很辛苦，\x01",
            "但是我还是觉得自己很适合这份工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF6")

    label("loc_1C2E")


    ChrTalk(
        0xFE,
        (
            "干这项工作，\x01",
            "在飞艇平安起飞的瞬间，\x01",
            "我们能得到非常大的充实感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有时候会很辛苦，\x01",
            "但是我还是觉得自己很适合这份工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF6")

    Jump("loc_2519")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_1DDC")

    ChrTalk(
        0xFE,
        (
            "就在刚才，\x01",
            "王国军的警备飞艇飞走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有一个看上去虽然很年轻\x01",
            "却有着显赫地位的将校乘上去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来，要去给正在检修\x01",
            "『赛希莉亚号』的主任帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_1DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF0")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "在主任检查『赛希莉亚号』的时候，\x01",
            "我必须要赶快完成\x01",
            "对警备飞艇的基础检查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不快点完成的话，\x01",
            "又要被臭骂一顿了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管是空着还是忙着，\x01",
            "我总是会被他痛骂。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F66")

    label("loc_1EF0")


    ChrTalk(
        0xFE,
        (
            "在主任检查『赛希莉亚号』的时候，\x01",
            "我必须要赶快完成\x01",
            "对警备飞艇的基础检查……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F66")

    Jump("loc_2519")

    label("loc_1F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_20A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2061")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "虽然现在没事可干，\x01",
            "但是就这样闲着肯定又要挨骂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是去找点事情做吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明很清闲却要装成忙碌的样子，\x01",
            "还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_2061")


    ChrTalk(
        0xFE,
        (
            "明明很清闲却要装成忙碌的样子，\x01",
            "还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A1")

    Jump("loc_2519")

    label("loc_20A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_213D")

    ChrTalk(
        0xFE,
        (
            "拉克斯主任看上去\x01",
            "也非常急躁不安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平常就是一幅严肃的面孔，\x01",
            "现在显得更加可怕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_247C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2418")
    OP_A2(0x2)
    ClearMapFlags(0x1)

    ChrTalk(
        0xFE,
        (
            "拉克斯主任在\x01",
            "定期船开始运营之前，\x01",
            "就已经是飞艇的修理员了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "说起来，还是我的老前辈呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算这样，他也太过于严厉了。\x01",
            "每天都要挨他的骂……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 0)

    ChrTalk(
        0x9,
        "喂，诺尔姆！！\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D8")

    def lambda_22C4():
        OP_6C(135000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C4)
    OP_69(0x9, 0x1388)
    Jump("loc_230E")

    label("loc_22D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2307")

    def lambda_22F3():
        OP_6C(225000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22F3)
    OP_69(0x9, 0x1388)
    Jump("loc_230E")

    label("loc_2307")

    OP_69(0x9, 0xBB8)

    label("loc_230E")


    ChrTalk(
        0x9,
        (
            "我不是告诉你如果闲着\x01",
            "就去自己找点工作做吗！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "有聊天的功夫，\x01",
            "还不如去整理一下工具！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 0)
    OP_69(0x0, 0xBB8)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "好、好的……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 0)
    SetMapFlags(0x1)
    Jump("loc_2479")

    label("loc_2418")


    ChrTalk(
        0xFE,
        "对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正说着话呢，\x01",
            "又被他给骂了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2479")

    Jump("loc_2519")

    label("loc_247C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2519")

    ChrTalk(
        0xFE,
        (
            "根据公社的指示，\x01",
            "我们维修员也将马上到空港待命了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要等到什么时候呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2519")

    TalkEnd(0xA)
    Return()

    # Function_6_1957 end

    def Function_7_251D(): pass

    label("Function_7_251D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_25A7")

    ChrTalk(
        0xFE,
        (
            "终于拍到了我的目标——\x01",
            "『林德号』的照片了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，赶快去把\x01",
            "它的勇猛身姿显像出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FBB")

    label("loc_25A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B8")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "接下来就是在这里\x01",
            "等『林德号』来了……\x01",
            "怎么还不来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是啊，\x01",
            "其实我最想拍的还是\x01",
            "王家的『埃尔赛尤号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说也是最新型的飞艇，\x01",
            "听说设计方面做得相当有水准。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2776")

    label("loc_26B8")


    ChrTalk(
        0xFE,
        (
            "接下来就是在这里\x01",
            "等『林德号』来了……\x01",
            "怎么还不来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是啊，\x01",
            "其实我最想拍的还是\x01",
            "王家的『埃尔赛尤号』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2776")

    Jump("loc_2FBB")

    label("loc_2779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_28B5")

    ChrTalk(
        0xFE,
        (
            "虽然有点偶然，\x01",
            "不过今天亲眼看到了\x01",
            "王国军配备的新锐机型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且，\x01",
            "还完整地用照相机拍了下来，\x01",
            "真是意外的大收获啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这个飞艇坪等候着，\x01",
            "这个决定真是太英明了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FBB")

    label("loc_28B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2A8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DA")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "那、那部飞艇是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难不成那就是\x01",
            "王国军的警备飞艇？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起军队的警备飞艇，\x01",
            "它们在十年前的战争中被投入使用，\x01",
            "结果带来了丰硕的战果而一举成名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "厉害～\x01",
            "飞艇真是棒啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A87")

    label("loc_29DA")


    ChrTalk(
        0xFE,
        (
            "说起军队的警备飞艇，\x01",
            "它们在十年前的战争中被投入使用，\x01",
            "结果带来了丰硕的战果而一举成名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "厉害～\x01",
            "飞艇真是棒啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A87")

    Jump("loc_2FBB")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEE")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "在利贝尔国内运营的定期船\x01",
            "现在一共有两艘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "东向航线的『林德号』，\x01",
            "以及西向航线的『赛希莉亚号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然是同一年开始启用的，\x01",
            "不过外观的颜色却完全不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且『林德号』的导力引擎\x01",
            "年代也比较古老。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA4")

    label("loc_2BEE")


    ChrTalk(
        0xFE,
        (
            "在利贝尔国内运营的定期船\x01",
            "现在一共有两艘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "东向航线的『林德号』，\x01",
            "以及西向航线的『赛希莉亚号』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA4")

    Jump("loc_2FBB")

    label("loc_2CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8C")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这里每周一次，\x01",
            "都会接待从帝国来的货船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯超市的货物\x01",
            "就是由它们运走出口的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个稍微有点压迫感的设计\x01",
            "倒有点像帝国的风格呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2D8C")


    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "军队的禁令能不能早点解除啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCD")

    Jump("loc_2FBB")

    label("loc_2DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB5")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "柏斯的空港因为是国际空港，\x01",
            "所以会有各种各样的飞艇来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来是打算把它们\x01",
            "都拍进这个导力照相机的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是一艘也没有来，\x01",
            "到底是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F44")

    label("loc_2EB5")


    ChrTalk(
        0xFE,
        (
            "我本来是打算\x01",
            "来这里拍摄\x01",
            "各种各样的飞艇的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是一艘也没有来，\x01",
            "到底是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F44")

    Jump("loc_2FBB")

    label("loc_2F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2FBB")

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "这里可是最好的摄影场所哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，飞艇啊，\x01",
            "快点到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBB")

    TalkEnd(0xB)
    Return()

    # Function_7_251D end

    def Function_8_2FBF(): pass

    label("Function_8_2FBF")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_347B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3256")
    OP_28(0x10, 0x1, 0x2000)

    ChrTalk(
        0xFE,
        "啊，是你们…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实在很抱歉，\x01",
            "到古罗尼山顶的护卫委托\x01",
            "已经取消了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为定期船复航了，\x01",
            "我打算乘坐定期船\x01",
            "到卢安去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F对不起，\x01",
            "我们没有完成委托……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "没关系没关系，\x01",
            "你们也有很忙的事情嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们现在不是在搜查\x01",
            "南街区的强盗事件吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士真的很辛苦阿。\x01",
            "连休息的时间也没有。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "你们可要好好努力\x01",
            "把空贼集团一网打尽哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33B4")

    label("loc_3256")


    ChrTalk(
        0xFE,
        (
            "实在很抱歉，\x01",
            "到古罗尼山顶的护卫委托\x01",
            "已经取消了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为定期船复航了，\x01",
            "我打算乘坐定期船\x01",
            "到卢安去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "这下子终于能够去谈判了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过耽误了这么长时间，\x01",
            "交易也应该告吹了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B4")

    Jump("loc_3478")

    label("loc_33B7")


    ChrTalk(
        0xFE,
        (
            "我都快等得不耐烦了。\x01",
            "这下终于能够到卢安去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "此次的商谈估计已经告吹了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    label("loc_3478")

    Jump("loc_37AA")

    label("loc_347B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3506")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "竟然不向乘客说明事情的原因，\x01",
            "这究竟是怎么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再怎么说，\x01",
            "这也有点太过分了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AA")

    label("loc_3506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3589")

    ChrTalk(
        0xFE,
        (
            "也不知道什么时候\x01",
            "定期船才能够重新开航……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在只能在空港\x01",
            "乖乖地等下去啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AA")

    label("loc_3589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369C")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "真是糟糕……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来打算去卢安的，\x01",
            "定期船竟然停止运营了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，虽说是无法避免的事情，\x01",
            "但是商谈迟到的话\x01",
            "是会丢柏斯商人的脸的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_370E")

    label("loc_369C")


    ChrTalk(
        0xFE,
        (
            "唉，虽说是无法避免的事情，\x01",
            "但是商谈迟到的话\x01",
            "是会丢柏斯商人的脸的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370E")

    Jump("loc_37AA")

    label("loc_3711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_37AA")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "我是为了坐定期船才来这儿的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过飞船完全没有要来的样子啊。\x02",
    )

    CloseMessageWindow()

    label("loc_37AA")

    TalkEnd(0xC)
    Return()

    # Function_8_2FBF end

    def Function_9_37AE(): pass

    label("Function_9_37AE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D3")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "空贼被逮捕了，\x01",
            "失踪的船员和乘客\x01",
            "也都平安返回了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空港的接待员说，\x01",
            "西向航线的客船\x01",
            "马上就可以恢复运行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "真是让我等好久了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_38D3")


    ChrTalk(
        0xFE,
        (
            "空贼被逮捕了，\x01",
            "失踪的船员和乘客\x01",
            "也都平安返回了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空港的接待员说，\x01",
            "西向航线的客船\x01",
            "马上就可以恢复运行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399E")

    Jump("loc_3DA5")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3A5A")

    ChrTalk(
        0xFE,
        (
            "东向航线的飞艇\x01",
            "好像暂时还无法起飞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有点绕远路，\x01",
            "但是坐西向航线的飞艇\x01",
            "来绕道去王都可能比较快一点吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_3B1C")

    ChrTalk(
        0xFE,
        (
            "卢安那边的飞艇\x01",
            "好像已经到达了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且，\x01",
            "王国军的飞艇好像也来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们是来调查\x01",
            "那件强盗案件的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_3BAA")

    ChrTalk(
        0xFE,
        (
            "这样干等着\x01",
            "还真不是一般的累啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要不要\x01",
            "先回家一趟呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3C4A")

    ChrTalk(
        0xFE,
        (
            "空港的工作人员好像\x01",
            "对具体的情况也不是很熟悉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说飞行船\x01",
            "碰到什么事故了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3D27")

    ChrTalk(
        0xFE,
        (
            "现在乘坐飞艇\x01",
            "好像是不太可能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然目前没什么急事，\x01",
            "不会感到很难办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "至少让我知道什么时候\x01",
            "运营能够恢复正常啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA5")

    label("loc_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3DA5")

    ChrTalk(
        0xFE,
        (
            "我曾经想过到王都旅行的，\x01",
            "但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要搭乘的飞艇\x01",
            "却一直没有来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA5")

    TalkEnd(0xD)
    Return()

    # Function_9_37AE end

    def Function_10_3DA9(): pass

    label("Function_10_3DA9")

    EventBegin(0x0)
    OP_6D(26480, 1500, 26090, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(45000, 0)
    OP_6E(534, 0)
    SetChrPos(0x104, 49846, 1500, 40813, 0)
    SetChrPos(0x103, 48769, 1500, 40913, 0)
    SetChrPos(0x101, 49846, 1500, 43000, 180)
    SetChrPos(0x102, 48769, 1500, 43000, 180)
    SetChrPos(0x9, 51290, 1500, 48590, 90)
    OP_72(0x7, 0x4)
    OP_71(0x7, 0x2)
    OP_72(0x8, 0x4)
    OP_71(0x8, 0x2)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x1)
    OP_22(0x75, 0x0, 0x64)
    FadeToBright(2000, 0)
    OP_6D(49700, 1500, 42500, 5000)
    OP_0D()
    Fade(1000)
    OP_6B(1370, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#022F那么我就\x01",
            "先回洛连特了……\x02\x03",
            "#025F唔～我还是有点担心啊。\x01",
            "真的不用我陪你们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F都说了～没关系啦。\x02\x03",
            "#006F这可是以正游击士为目标的旅行，\x01",
            "雪拉姐在的话就不算是修行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P雪拉姐姐再不回去的话，\x01",
            "洛连特支部就要一团糟了。\x02\x03",
            "放心吧，我们能办得到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F唔，你们这么说的话……\x02\x03",
            "#020F在你们这种年纪\x01",
            "就以正游击士为目标已经实在难得。\x01",
            "不管怎么说，千万不能太蛮干哦。\x02\x03",
            "要是遇到什么麻烦的话，\x01",
            "记得马上联络洛连特支部。\x02\x03",
            "无论你们在哪，\x01",
            "我都会火速赶到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嗯……谢谢，雪拉姐。\x02\x03",
            "#506F雪拉姐也是，\x01",
            "记得不要喝太多酒哦。\x02\x03",
            "我可是只担心这个呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#520F哈哈……\x01",
            "嗯，我会有分寸呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵，你们就不用担心嘛。\x02\x03",
            "无论发生什么事，\x01",
            "我都会陪在雪拉君身边的！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#509F……为、为什么\x01",
            "你这家伙也要去洛连特？\x02\x03",
            "而且是和雪拉姐一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哈·哈·哈。\x01",
            "因为本人已经尝尽了柏斯的乡土料理。\x02\x03",
            "正想着差不多\x01",
            "该到其他地方看看了。\x02\x03",
            "#031F听说洛连特的蔬菜是极品中的极品，\x01",
            "而且雪拉君说过会带我去品尝一番呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F你在胡扯什么呀，\x01",
            "我可从没打算为你介绍什么美味的饭店。\x02\x03",
            "#027F因为你太缠人了，\x01",
            "所以我才勉强以陪我去酒馆喝酒为条件，\x01",
            "特别准许你跟我去洛连特的哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F呜哇～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#1P奥利维尔……\x01",
            "你真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F呵呵，我奥利维尔为了佳人和美食，\x01",
            "可是万死不辞的。\x02\x03",
            "#034F不过其实……\x01",
            "我也很想可以陪着约修亚君你呢。\x02\x03",
            "这真是让人难以迷茫的抉择……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#1P你迷茫的话我会很困惑的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真是个超级胡来的家伙……\x01",
            "别扰乱洛连特的治安就好了。\x02\x03",
            "#006F工作之后的雪拉姐\x01",
            "可完全是个无～底洞哦。\x02\x03",
            "你还是先做好准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F什么呀，真没礼貌。\x01",
            "反正爱娜也会陪着我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F有她在更危险啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#033F无底洞？\x02\x03",
            "那个，难道说……\x01",
            "有比雪拉君更厉害的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#1P……这个嘛。\x01",
            "我想根本无法相提并论吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#033F哈～是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x104)

    ChrTalk(
        0x104,
        "#036F#3S咦！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_4A14():
        OP_6B(1500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A14)

    def lambda_4A24():
        OP_6D(51410, 1600, 40400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A24)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开往洛连特的\x01",
            "定期船马上就要起飞了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请尚未登机的乘客尽快登机。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(
        0x103,
        (
            "#023F啊，要出发了。\x02\x03",
            "#021F好了奥利维尔，要快点了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xBF92, 0x5DC, 0x9D90, 0xBB8, 0x0)

    ChrTalk(
        0x104,
        (
            "#036F雪、雪拉君，\x01",
            "再稍稍等一下嘛。\x02\x03",
            "再给我点时间考虑，\x01",
            "求求你～了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F都要马上登机了，\x01",
            "你还想说些什～么呀？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x103,
        "#024F#5S是男人就不要吞吞吐吐！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x104,
        "#036F呜啊啊啊～～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4CBE():

        label("loc_4CBE")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_4CBE")

    QueueWorkItem2(0x101, 2, lambda_4CBE)

    def lambda_4CCF():

        label("loc_4CCF")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_4CCF")

    QueueWorkItem2(0x102, 2, lambda_4CCF)

    def lambda_4CE0():
        OP_8E(0x101, 0xC2B6, 0x5DC, 0x9F6D, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CE0)

    def lambda_4CFB():
        OP_8E(0x102, 0xBE81, 0x5DC, 0x9FD1, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4CFB)
    OP_43(0x104, 0x1, 0x0, 0xC)
    OP_43(0x103, 0x1, 0x0, 0xB)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#001F雪拉姐，再见了～！\x02\x03",
            "帮我向洛连特的各位问好哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F你们两个都要保重哦！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(1000)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x104, 0x1)
    OP_A1(0xE, 0x7)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    SetChrPos(0xE, 62250, -5650, 41990, 0)
    SetChrFlags(0xE, 0x4)
    OP_A1(0xF, 0x8)
    OP_72(0x8, 0x4)
    SetChrPos(0xF, 62250, -5500, 41990, 0)
    SetChrFlags(0xF, 0x4)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_70(0x9, 0x64)
    OP_70(0xA, 0x64)
    OP_73(0x9)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x3C)
    OP_73(0x7)
    Fade(2000)
    OP_6D(60000, -1550, 51540, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(550, 0)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    Sleep(2000)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0x7, 61)
    OP_70(0x7, 0xA0)
    OP_73(0x7)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 161)
    OP_70(0x7, 0x104)

    def lambda_4EAF():
        OP_6D(60000, -1550, 51540, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EAF)

    def lambda_4EC7():
        OP_67(0, 11230, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EC7)

    def lambda_4EDF():
        OP_6B(2260, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4EDF)

    def lambda_4EEF():
        OP_6C(204000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4EEF)

    def lambda_4EFF():
        OP_6E(801, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4EFF)
    OP_91(0xE, 0x0, 0x1F4, 0x0, 0x12C, 0x0)
    OP_91(0xE, 0x0, 0x3E8, 0x0, 0x258, 0x0)
    Sleep(2000)

    def lambda_4F3C():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F3C)
    OP_94(0x1, 0xE, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_4F61():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F61)
    OP_94(0x1, 0xE, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_4F86():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F86)
    OP_94(0x1, 0xE, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_4FAB():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FAB)
    OP_94(0x1, 0xE, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_4FD0():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FD0)
    OP_94(0x1, 0xE, 0x0, 0x708, 0x1388, 0x0)

    def lambda_4FF5():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4FF5)
    OP_94(0x1, 0xE, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_501A():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_501A)
    OP_20(0xBB8)
    FadeToDark(4000, 0, -1)
    OP_94(0x1, 0xE, 0x0, 0x898, 0x1B58, 0x0)

    def lambda_504E():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_504E)

    def lambda_5064():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5064)
    OP_0D()
    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(100)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(100)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(100)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(100)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(100)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x75, 0x14)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x75, 0xA)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_23(0x75)
    OP_23(0x77)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x40042, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x12, 0x0)
    OP_A2(0x391)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517C")
    ShowSaveMenu()

    label("loc_517C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x392)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3DA9 end

    def Function_11_51D6(): pass

    label("Function_11_51D6")

    OP_8E(0xFE, 0xC011, 0x5DC, 0x9537, 0xBB8, 0x0)
    OP_8E(0xFE, 0xE120, 0x5DC, 0x9537, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xE7C2, 0x5DC, 0x98DA, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_11_51D6 end

    def Function_12_521F(): pass

    label("Function_12_521F")

    OP_8C(0xFE, 0, 0)
    OP_8F(0xFE, 0xC011, 0x5DC, 0x9537, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xE120, 0x5DC, 0x9537, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0xE5F6, 0x5DC, 0x9538, 0xBB8, 0x0)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_12_521F end

    def Function_13_527B(): pass

    label("Function_13_527B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往洛连特市\x01",
            "≡　开往卢安市\x01",
            "≡　开往埃雷波尼亚帝国\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_527B end

    def Function_14_52F1(): pass

    label("Function_14_52F1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_52F1 end

    def Function_15_5370(): pass

    label("Function_15_5370")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　飞艇坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "『利贝尔飞艇公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_5370 end

    SaveToFile()

Try(main)
