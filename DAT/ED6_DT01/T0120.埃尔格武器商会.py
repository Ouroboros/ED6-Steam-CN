from ED6ScenarioHelper import *

def main():
    # 埃尔格武器商会

    CreateScenaFile(
        FileName            = 'T0120   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0120.x',
        MapIndex            = 4,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0120   ._SN',
            'ED6_DT01/T0120_1 ._SN',
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
        '佛莱迪',                               # 9
        '梅尔达斯',                             # 10
        '埃尔格',                               # 11
        '斯蒂娜',                               # 12
        '雪拉扎德',                             # 13
        '朵洛希',                               # 14
        '目标用摄像机',                         # 15
    )

    DeclEntryPoint(
        Unknown_00              = -39000,
        Unknown_04              = 0,
        Unknown_08              = -4000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 4,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -39000,
        Unknown_04              = 0,
        Unknown_08              = -5000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 6,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -43000,
        Unknown_04              = 0,
        Unknown_08              = 2000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 6,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -37000,
        Unknown_04              = 0,
        Unknown_08              = 66000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 4,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01690 ._CH',             # 03
        'ED6_DT07/CH00020 ._CH',             # 04
        'ED6_DT07/CH02070 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01690P._CP',             # 03
        'ED6_DT07/CH00020P._CP',             # 04
        'ED6_DT07/CH02070P._CP',             # 05
    )

    DeclNpc(
        X                   = -38180,
        Z                   = 0,
        Y                   = -497,
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
        X                   = -39499,
        Z                   = 0,
        Y                   = 678,
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
        X                   = -36678,
        Z                   = 0,
        Y                   = 73751,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -86132,
        Z                   = 0,
        Y                   = 71210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 0,
        Y                   = -360,
        Direction           = 279,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -41900,
        Y                   = 0,
        Z                   = 1877,
        Range               = -44000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x10A4,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -37700,
        Y                   = 0,
        Z                   = -5500,
        Range               = -40500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFDF76,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = -38537,
        TriggerZ            = 0,
        TriggerY            = -1845,
        TriggerRange        = 400,
        ActorX              = -38180,
        ActorZ              = 1500,
        ActorY              = -497,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41599,
        TriggerZ            = 0,
        TriggerY            = 299,
        TriggerRange        = 1000,
        ActorX              = -39499,
        ActorZ              = 1500,
        ActorY              = 678,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36170,
        TriggerZ            = 0,
        TriggerY            = 71651,
        TriggerRange        = 1000,
        ActorX              = -36678,
        ActorZ              = 1500,
        ActorY              = 73751,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_39E",          # 01, 1
        "Function_2_3C0",          # 02, 2
        "Function_3_3D6",          # 03, 3
        "Function_4_3DB",          # 04, 4
        "Function_5_1A51",         # 05, 5
        "Function_6_1A56",         # 06, 6
        "Function_7_2BC0",         # 07, 7
        "Function_8_2BC5",         # 08, 8
        "Function_9_4C17",         # 09, 9
        "Function_10_6771",        # 0A, 10
        "Function_11_7BAA",        # 0B, 11
        "Function_12_7BE8",        # 0C, 12
        "Function_13_7C18",        # 0D, 13
        "Function_14_7CC4",        # 0E, 14
        "Function_15_7D70",        # 0F, 15
        "Function_16_91D4",        # 10, 16
        "Function_17_A0C1",        # 11, 17
        "Function_18_A0F3",        # 12, 18
        "Function_19_A15B",        # 13, 19
        "Function_20_A177",        # 14, 20
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_340")
    OP_8C(0x9, 90, 0)

    label("loc_340")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_350"),
        (102, "loc_363"),
        (SWITCH_DEFAULT, "loc_376"),
    )


    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 15)

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_373")
    Event(0, 16)

    label("loc_373")

    Jump("loc_376")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39D")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xD, -44500, 0, -320, 283)

    label("loc_39D")

    Return()

    # Function_0_332 end

    def Function_1_39E(): pass

    label("Function_1_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B6")
    OP_B1("t0120_y")
    Jump("loc_3BF")

    label("loc_3B6")

    OP_B1("t0120_n")

    label("loc_3BF")

    Return()

    # Function_1_39E end

    def Function_2_3C0(): pass

    label("Function_2_3C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3C0")

    label("loc_3D5")

    Return()

    # Function_2_3C0 end

    def Function_3_3D6(): pass

    label("Function_3_3D6")

    Call(0, 4)
    Return()

    # Function_3_3D6 end

    def Function_4_3DB(): pass

    label("Function_4_3DB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_478")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_44F")
    OP_A9(0x0)
    Jump("loc_45E")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C")
    OP_A9(0x9)
    Jump("loc_45E")

    label("loc_45C")

    OP_A9(0x70)

    label("loc_45E")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478")
    TalkEnd(0x8)
    Return()

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5CA")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "市长先生委托\x01",
            "我们加工的七耀石\x01",
            "终于送到工房这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我还是第一次见到\x01",
            "这么漂亮的翠耀石呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在父亲正在\x01",
            "对那块翠耀石进行加工。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C7")

    label("loc_56A")


    ChrTalk(
        0x8,
        (
            "要制造七耀石的工艺品，\x01",
            "这种活儿也只有父亲才能胜任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7")

    Jump("loc_1A46")

    label("loc_5CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EF")
    OP_A2(0x228)
    Call(1, 3)
    Jump("loc_1A46")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_71F")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "虽然市长先生委托\x01",
            "我们加工七耀石……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但最关键的翠耀石\x01",
            "却到现在还没有送来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是不是出什么事了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_71C")

    label("loc_6A4")


    ChrTalk(
        0x8,
        (
            "市长先生委托\x01",
            "我们加工七耀石……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但最关键的翠耀石\x01",
            "却到现在还没有送来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71C")

    Jump("loc_1A46")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_8A7")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_809")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "市长先生委托\x01",
            "我们加工七耀石。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在还没送来，\x01",
            "不过听说是极品的翠耀石。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不知道是什么样的东西呢，\x01",
            "有点期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A4")

    label("loc_809")


    ChrTalk(
        0x8,
        (
            "市长先生委托\x01",
            "我们加工七耀石。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在还没送来，\x01",
            "不过听说是极品的翠耀石。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A4")

    Jump("loc_1A46")

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_C4E")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A47")
    OP_A2(0x0)
    TurnDirection(0x8, 0x110, 400)

    ChrTalk(
        0x8,
        (
            "朵洛希小姐的相机是最新款的，\x01",
            "货色相当不错的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过那是专业型的，\x01",
            "不是两三下就能\x01",
            "操作的东西吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#150F呵呵呵，\x01",
            "你是说这小不点么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "小、小不点？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#151F它是个好孩子，\x01",
            "很听话的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哦、哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#145F认认真真听这家伙说话\x01",
            "纯粹只是白费力气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA3")

    label("loc_A47")


    ChrTalk(
        0x8,
        (
            "哈哈，生意做久了\x01",
            "就会碰到各种各样的客人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_C4B")

    label("loc_AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8E")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "矿山的新矿脉中\x01",
            "好像发现了巨大的七耀石呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这种等级的东西\x01",
            "想必应该非常昂贵，\x01",
            "不过听说很快就找到买主了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不知道是谁买的呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4B")

    label("loc_B8E")


    ChrTalk(
        0x8,
        (
            "矿山的新矿脉中\x01",
            "好像发现了巨大的七耀石呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这种等级的东西\x01",
            "想必应该非常昂贵，\x01",
            "不过听说很快就找到买主了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4B")

    Jump("loc_1A46")

    label("loc_C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_E84")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(
        0x8,
        (
            "啊，是你们两个。\x01",
            "路灯的修理辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "有什么关于导力器的问题的话\x01",
            "就随时找我来谈好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后我们工房的生意\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4C")
    OP_A2(0x228)
    Call(1, 0)
    Jump("loc_E81")

    label("loc_D4C")

    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "导力器的运用\x01",
            "都掌握得差不多了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "想使用新的结晶回路，\x01",
            "改造这个步骤是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "想改造的时候，\x01",
            "你们来这里找我就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E81")

    label("loc_E07")


    ChrTalk(
        0x8,
        (
            "想使用新的结晶回路，\x01",
            "改造这个步骤是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "想改造的时候，\x01",
            "你们来这里找我就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E81")

    Jump("loc_1A46")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_F3A")
    OP_A2(0x228)

    ChrTalk(
        0x8,
        (
            "从柏斯飞往王都的定期船\x01",
            "似乎已经到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过今天反正也没采购什么东西，\x01",
            "就在店里好好地集中精神工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A46")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_10AD")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1032")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "要想成为一流的游击士，\x01",
            "就必须娴熟细致\x01",
            "使用导力魔法才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这个小店常常有\x01",
            "各种不同的游击士光顾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们看看自己的导力器，\x01",
            "仔细考虑一下该怎么改造。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA")

    label("loc_1032")


    ChrTalk(
        0x8,
        (
            "这个小店常常有\x01",
            "各种不同的游击士光顾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们看看自己的导力器，\x01",
            "仔细考虑一下该怎么改造。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    Jump("loc_1A46")

    label("loc_10AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_143D")
    OP_A2(0x228)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")
    OP_A2(0x2A2)

    ChrTalk(
        0x8,
        "是你们啊，研修辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……哦！你们胸前那枚徽章是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "恭喜你们俩！\x01",
            "终于成为游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哈哈哈，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F艾丝蒂尔从刚才开始\x01",
            "就一直高兴得像要飞上天了一样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#001F约修亚真是够古板的，开心些不好吗？\x01",
            "我们可是很辛苦才得到这成绩呢。\x02\x03",
            "#502F不过今天我很高兴，就不和你计较这么多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F唉，真拿她没办法啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "对了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "既然成为游击士了，那就要克服\x01",
            "不擅长导力魔法这一点才行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈哈～\x01",
            "以后我们工房的生意\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_143A")

    label("loc_13C7")


    ChrTalk(
        0x8,
        "两位游击士新人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后我们工房的生意\x01",
            "还要请你们多多关照啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_143A")

    Jump("loc_1A46")

    label("loc_143D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_14E5")

    ChrTalk(
        0x8,
        "你们研修要好好加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果要改造导力器的话，\x01",
            "在菜单上选择『改造·换钱』就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A46")

    label("loc_14E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198D")
    OP_A2(0x0)
    OP_A2(0x20D)
    OP_A2(0x228)

    ChrTalk(
        0x8,
        (
            "哟，\x01",
            "原来是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "之前调整了导力器\x01",
            "现在使用起来习惯吗？\x01",
            "我想对你们来说应该不难吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#017F对艾丝蒂尔来说，\x01",
            "比起导力器的好坏问题，\x01",
            "还是使用方法比较让她难懂。\x02\x03",
            "#017F不管讲解得怎样通俗易懂，\x01",
            "她理解起来总是会有困难。\x02\x03",
            "#010F同样要领悟一点，\x01",
            "就要比别人多花几倍精力……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#002F哼，不好意思啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "没关系啦，\x01",
            "一开始谁都会有些困惑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过一旦掌握了诀窍，\x01",
            "就可以很快精通了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对呀，就是嘛！\x02\x03",
            "#001F只要等我习惯之后，\x01",
            "就可以比约修亚运用得更加娴熟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在我刚进蔡斯的\x01",
            "中央工房的时候\x01",
            "也是完全不会使用导力器的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x101,
        "#004F佛莱迪先生以前也是那样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊，不断使用不断熟悉，\x01",
            "现在连技术师也当上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔也要以\x01",
            "游击士为目标而努力加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F好啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A46")

    label("loc_198D")


    ChrTalk(
        0x8,
        (
            "对于战术导力器的运用\x01",
            "一开始谁都会有些困惑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过一旦掌握了诀窍，\x01",
            "对于艾丝蒂尔来说肯定可以很快精通的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A46")

    OP_56(0x0)
    TalkEnd(0x8)
    Sleep(300)
    Return()

    # Function_4_3DB end

    def Function_5_1A51(): pass

    label("Function_5_1A51")

    Call(0, 6)
    Return()

    # Function_5_1A51 end

    def Function_6_1A56(): pass

    label("Function_6_1A56")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6D")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "市长的七耀石\x01",
            "终于送过来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "这可是一块不得了的东西啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而且听说还是\x01",
            "送给女王陛下的生日礼物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好久都没做工艺品的加工了，\x01",
            "我已经跃跃欲试了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB2")

    label("loc_1B6D")


    ChrTalk(
        0x9,
        (
            "要完成这种活儿，\x01",
            "暂时还不能交给佛莱迪单独去做。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")

    Jump("loc_2BBC")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1CEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C81")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "我们从市长那里\x01",
            "接了一份活儿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但都已经过了约好的时间了，\x01",
            "他却还没把东西送来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他应该向来\x01",
            "都是遵守时间的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEB")

    label("loc_1C81")


    ChrTalk(
        0x9,
        (
            "我们从市长那里\x01",
            "接了一份活儿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但都已经过了约好的时间了，\x01",
            "他却还没把东西送来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEB")

    Jump("loc_2BBC")

    label("loc_1CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB1")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "导力器似乎是\x01",
            "以远古时期的工具\x01",
            "为参考而发明出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "也就是说了不起的不是现代人，\x01",
            "而是古代人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "真有点不甘心哪。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E39")

    label("loc_1DB1")


    ChrTalk(
        0x9,
        (
            "导力器似乎是\x01",
            "以远古时期的工具\x01",
            "为参考而发明出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "也就是说了不起的不是现代人，\x01",
            "而是古代人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E39")

    Jump("loc_2BBC")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_1EB2")

    ChrTalk(
        0x9,
        (
            "真是的，佛莱迪也\x01",
            "在那里喳喳呼呼的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "真不像话。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8B")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "刚才我看见了市长，\x01",
            "他看上去出奇地心神不定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是的， \x01",
            "他一直都是个不够沉着的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "身为市长应该\x01",
            "表现得更沉稳一些嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1F8B")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "刚才我看见了市长，\x01",
            "他看上去出奇地心神不定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是的， \x01",
            "他一直都是个不够沉着的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2004")

    Jump("loc_2BBC")

    label("loc_2007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_21CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2133")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "听说飞艇上都装有\x01",
            "一种叫做导力引擎的巨型机械。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那是一种利用了\x01",
            "导力器原理制成的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "全都是蔡斯的伟大学者们\x01",
            "开发出来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哎？扯得没边了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C9")

    label("loc_2133")


    ChrTalk(
        0x9,
        (
            "听说飞艇上都装有\x01",
            "一种叫做导力引擎的巨型机械。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哎？扯得没边了。\x02",
    )

    CloseMessageWindow()

    label("loc_21C9")

    Jump("loc_2BBC")

    label("loc_21CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_234C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DF")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "是艾丝蒂尔和约修亚啊。\x01",
            "可别妨碍我们工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……不过你们也已经不是那种爱捣乱的年纪了。\x01",
            "都已经成了游击士了是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真了不起呢，\x01",
            "让人刮目相看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_22DF")


    ChrTalk(
        0x9,
        "都已经成了游击士了是吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真了不起呢，\x01",
            "让人刮目相看了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2349")

    Jump("loc_2BBC")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_23EA")

    ChrTalk(
        0x9,
        (
            "哦，到时间了，\x01",
            "差不多该关门了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你们俩也不要\x01",
            "在这里晃来晃去的了，\x01",
            "早点回去吧，回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBC")

    label("loc_23EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2553")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "现在的导力器\x01",
            "都是以钟表的结构而制成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "所以老一辈的技术人员\x01",
            "还是可以摆弄一下它们的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我可是非常\x01",
            "精通结晶回路的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "也不知道这东西是\x01",
            "哪里的什么人发明的，\x01",
            "真是个很复杂的机械啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2605")

    label("loc_2553")


    ChrTalk(
        0x9,
        (
            "我可是非常\x01",
            "精通结晶回路的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "也不知道这东西是\x01",
            "哪里的什么人发明的，\x01",
            "真是个很复杂的机械啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2605")

    Jump("loc_2BBC")

    label("loc_2608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2679")

    ChrTalk(
        0x9,
        "哦，研修辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要使用工房的话，\x01",
            "和佛莱迪说一声就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBC")

    label("loc_2679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE8")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "喂！现在还没有开始营业呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……哦，原来是艾丝蒂尔和约修亚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "今天怎么这么早啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F早上好，\x01",
            "梅尔达斯爷爷。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)

    ChrTalk(
        0x102,
        (
            "#010F早上好。\x02\x03",
            "#010F不久之前您帮我们\x01",
            "修理了家外面的导力灯，\x01",
            "真是太感谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我们家外面的导力灯坏了？\x02\x03",
            "#001F导力器果然是日常生活中\x01",
            "不可缺少的必需品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……想当年我们\x01",
            "这一代还小的时候，\x01",
            "哪里有这样的导力器卖啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "到了现在什么灯呀火呀\x01",
            "简简单单地就点着了，\x01",
            "天上还有飞艇在到处乱飞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是让人觉得不习惯啊，\x01",
            "是不是有些方便得过头了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F（糟糕……\x01",
            "　又开始说个不停了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#017F（……谁叫你刚才\x01",
            "　说了多余的话啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们年轻的时候拼死拼活，\x01",
            "流血流汗地让今天的一切得以实现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而现在的年轻人根本就不愿意去做\x01",
            "稍微有一点辛苦的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008F哈～哈哈～说、说得对呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BBC")

    label("loc_2AE8")


    ChrTalk(
        0x9,
        (
            "因为导力器带来的便利，年轻一代\x01",
            "连稍微辛苦一点的事情都不愿去做，\x01",
            "我真有些为他们感到担忧啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我说得对吗，艾丝蒂尔、约修亚。\x01",
            "不要忘记要用你们自己的双手去开拓未来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBC")

    TalkEnd(0x9)
    Return()

    # Function_6_1A56 end

    def Function_7_2BC0(): pass

    label("Function_7_2BC0")

    Call(0, 8)
    Return()

    # Function_7_2BC0 end

    def Function_8_2BC5(): pass

    label("Function_8_2BC5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_END)), "loc_2C3D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2C")
    OP_0D()
    OP_A9(0x1)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_2C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C3D")
    TalkEnd(0xA)
    Return()

    label("loc_2C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2F76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF0")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "哟，是约修亚和艾丝蒂尔啊。\x01",
            "怎么了？两个人都拿着行李。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "向埃尔格说明了事情的来龙去脉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "卡西乌斯他……！？\x01",
            "所以你们就要去柏斯吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过没想到\x01",
            "那家伙坐的那艘飞艇会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊，我们已经决定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F所以呢，\x01",
            "我们打算去柏斯那里调查一下。\x02\x03",
            "呆在这里什么都不做\x01",
            "也的确不舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "原来如此啊。\x01",
            "这样做才像你们啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "也好，\x01",
            "雪拉扎德和你们一起的话我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "总之你们一路上要小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，那我们出发了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F73")

    label("loc_2EF0")


    ChrTalk(
        0xA,
        (
            "对了，你们的事情\x01",
            "还是由我来和斯蒂娜说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "要不然她又会\x01",
            "放心不下唠唠叨叨的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F73")

    Jump("loc_4C0C")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_31FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316E")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "啊，艾丝蒂尔和约修亚，\x01",
            "……雪拉扎德也在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F我们正好一起工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是吗，\x01",
            "我这里本来预定进新鞭子的，\x01",
            "不凑巧到现在还没送来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……说起来雪拉姐\x01",
            "在训练的时候也用剑的，\x01",
            "为什么工作时候用鞭子呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是啊……\x01",
            "从小时候起\x01",
            "我就比较习惯用近身武器啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（……鞭子是近身武器？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_316E")


    ChrTalk(
        0xA,
        (
            "工作前要好好地\x01",
            "检查自己的装备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯，我想这个\x01",
            "应该不需要我说了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FB")

    Jump("loc_4C0C")

    label("loc_31FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_334D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32ED")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "哟，我听说\x01",
            "你们两个很活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "好像解决了\x01",
            "一个又一个的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "约修亚，\x01",
            "你已经从我这里的打工锻炼出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334A")

    label("loc_32ED")


    ChrTalk(
        0xA,
        (
            "卡西乌斯也好，\x01",
            "雪拉扎德也好，\x01",
            "洛连特的游击士就是很优秀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334A")

    Jump("loc_4C0C")

    label("loc_334D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3413")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "哟，你们两个\x01",
            "看起来好像很忙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "有空就去见见斯蒂娜，\x01",
            "和她聊聊天吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不管怎么说，\x01",
            "她就是对你们放不下心来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3490")

    label("loc_3413")


    ChrTalk(
        0xA,
        (
            "有空就去见见斯蒂娜，\x01",
            "和她聊聊天吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不管怎么说，\x01",
            "她就是对你们放不下心来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3490")

    Jump("loc_4C0C")

    label("loc_3493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_36EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3663")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "哟，我听说了哦。\x01",
            "你们那么快就\x01",
            "开始游击士的工作了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "做得怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F还行，总算还应付得来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F总之帕赛尔农场的任务\x01",
            "算是完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是这样吗……\x01",
            "虽说只是暂时顶替卡西乌斯先生，\x01",
            "不过你们已经是出色的游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔，可别莽莽撞撞的，\x01",
            "老是给约修亚添麻烦可不好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真是的，大叔干嘛啦，\x01",
            "总是只针对我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36EB")

    label("loc_3663")


    ChrTalk(
        0xA,
        (
            "是吗，你们也已经是\x01",
            "出色的游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔，可别莽莽撞撞的，\x01",
            "老是给约修亚添麻烦可不好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36EB")

    Jump("loc_4C0C")

    label("loc_36EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0C")
    OP_A2(0x2A1)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "哟，新人游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "卡西乌斯这家伙\x01",
            "是不是又要出一阵门啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们刚刚去送他。\x02\x03",
            "大叔的消息还真灵通呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哈哈，还好啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xA,
        (
            "以前卡西乌斯出门的时候，\x01",
            "经常把艾丝蒂尔送到我家托我照看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过自从你来了之后，\x01",
            "就一直是你们俩一起看家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想不到艾丝蒂尔\x01",
            "还挺怕寂寞的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "来我家时，\x01",
            "刚开始总是像\x01",
            "借来的小猫似的老实呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F真是的～大叔。\x01",
            "哪儿有这种事嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过过个两三天\x01",
            "她就完全放松了，\x01",
            "开始吃得好玩得好睡得好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哈哈，这个可以想象。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3A0C")


    ChrTalk(
        0xA,
        (
            "卡西乌斯那家伙不在，\x01",
            "你们家挺冷清的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们俩现在\x01",
            "也可以来我家住哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "用不着客气。\x01",
            "我想斯蒂娜也会高兴的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADB")

    Jump("loc_4C0C")

    label("loc_3ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_404D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD3")
    OP_A2(0x2)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        (
            "唔，已经到时间了，\x01",
            "今天一天的工作还算不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "接下来就该关门了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔、约修亚。\x01",
            "我很期待你们今后有活跃的表现哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C37")

    label("loc_3BD3")


    ChrTalk(
        0xA,
        (
            "艾丝蒂尔、约修亚，\x01",
            "我很期待你们\x01",
            "今后有活跃的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C37")

    Jump("loc_404A")

    label("loc_3C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD2")
    OP_A2(0x2A0)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "你们好，艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F晚上好～\x01",
            "埃尔格大叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F晚上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦～对啦，今天不是\x01",
            "你们研修的最后一天吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "约修亚，\x01",
            "不久之前你来这里的时候\x01",
            "我好像听到你这么说过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那，研修如何了？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "你们胸前那个徽章是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不愧是卡西乌斯的孩子……\x01",
            "真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过我们还处于见习阶段。\x01",
            "和前辈比起来还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是这样啊。\x01",
            "不过，这样的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "看起来，\x01",
            "你以后就不能来这里打工了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F实在很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没事，不要放在心上，\x01",
            "之前我就知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你对于武器的挑选很有眼光。\x01",
            "不能来打工还是让我有些遗憾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但是你也有你自己选择的道路。\x01",
            "从现在开始你一定要努力，\x01",
            "成为一名优秀的游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404A")

    label("loc_3FD2")


    ChrTalk(
        0xA,
        (
            "约修亚不到我这里来打工\x01",
            "虽然让我有些遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过嘛，我以前就知道会这样的，\x01",
            "这也是没有办法的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404A")

    Jump("loc_4C0C")

    label("loc_404D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_47D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_439D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4322")
    OP_A2(0x2A0)
    OP_A2(0x226)

    ChrTalk(
        0x101,
        "#001F您好啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "哦，艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "课上得怎么样了？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "你们胸前那个徽章是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不愧是卡西乌斯的孩子……\x01",
            "真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过我们还处于见习阶段。\x01",
            "和前辈比起来还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是这样啊。\x01",
            "不过，这样的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "看起来，\x01",
            "你以后就不能来这里打工了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F实在很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没事，不要放在心上，\x01",
            "之前我就知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你对于武器的挑选很有眼光。\x01",
            "不能来打工还是让我有些遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但是你也有你自己选择的道路。\x01",
            "从现在开始你一定要努力，\x01",
            "成为一名优秀的游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_439A")

    label("loc_4322")


    ChrTalk(
        0xA,
        (
            "约修亚不到我这里来打工\x01",
            "虽然让我有些遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过嘛，我以前就知道会这样的，\x01",
            "这也是没有办法的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_439A")

    Jump("loc_47D0")

    label("loc_439D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4758")
    OP_A2(0x225)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "哟，艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F您好啊～\x01",
            "埃尔格大叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦～对啦，今天不是\x01",
            "你们研修的最后一天吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "约修亚，\x01",
            "不久之前你来这里的时候\x01",
            "我好像听到你这么说过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那，研修如何了？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "你们胸前那个徽章是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不愧是卡西乌斯的孩子……\x01",
            "真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过我们还处于见习阶段。\x01",
            "和前辈比起来还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是这样啊。\x01",
            "不过，这样的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "看起来，\x01",
            "你以后就不能来这里打工了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F实在很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没事，不要放在心上，\x01",
            "之前我就知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你对于武器的挑选很有眼光。\x01",
            "不能来打工还是让我有些遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但是你也有你自己选择的道路。\x01",
            "从现在开始你一定要努力，\x01",
            "成为一名优秀的游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D0")

    label("loc_4758")


    ChrTalk(
        0xA,
        (
            "约修亚不到我这里来打工\x01",
            "虽然让我有些遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过嘛，我以前就知道会这样的，\x01",
            "这也是没有办法的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D0")

    Jump("loc_4C0C")

    label("loc_47D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B83")
    OP_A2(0x20E)
    OP_A2(0x226)

    ChrTalk(
        0xA,
        "哦～早上好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F早上好～\x01",
            "埃尔格大叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "今天你们怎么来得这么早啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦～对啦，今天不是\x01",
            "你们研修的最后一天吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "约修亚，\x01",
            "不久之前你来这里的时候\x01",
            "我好像听到你这么说过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，对啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这样啊，\x01",
            "约修亚你肯定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过，艾丝蒂尔\x01",
            "就让我有些不放心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "从小时候开始\x01",
            "就总是冒冒失失的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F是啊……\x02\x03",
            "她从小时候起\x01",
            "就一直是个冒失鬼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#009F喂～！ 说够了没有！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#009F冒冒失失，冒冒失失，\x01",
            "有完没完！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "好了，别吵架了，\x01",
            "还是早点去游击士协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C0C")

    label("loc_4B83")


    ChrTalk(
        0xA,
        (
            "哎呀～那个不久之前\x01",
            "还抓住卡西乌斯裤腿不放的小艾丝蒂尔\x01",
            "就要成为游击士了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "岁月真是不饶人啊～\x02",
    )

    CloseMessageWindow()

    label("loc_4C0C")

    OP_56(0x0)
    TalkEnd(0xA)
    Sleep(300)
    Return()

    # Function_8_2BC5 end

    def Function_9_4C17(): pass

    label("Function_9_4C17")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D29")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "哎唷，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵呵，有没有去认真工作呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F（……我们的事\x01",
            "　还是不要告诉阿姨比较好吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F（唔、嗯，的确是……）\x02\x03",
            "#007F（我怕又会让她哭起来……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7D")

    label("loc_4D29")


    ChrTalk(
        0xFE,
        "大家，有没有去认真工作呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太蛮干的话可是不行的哦。\x02",
    )

    CloseMessageWindow()

    label("loc_4D7D")

    Jump("loc_676D")

    label("loc_4D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_5080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5026")
    OP_A2(0x2B0)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "呀，小雪拉。\x01",
            "今天三个人一起？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F嗯，是啊。\x02\x03",
            "今天我们正好一起工作。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，是这样啊……\x01",
            "三个人要是能好好合作的话，\x01",
            "阿姨我会非常高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，小雪拉啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是让艾丝蒂尔和约修亚\x01",
            "学坏可不行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F真过分呢，阿姨。\x01",
            "把人家说得像坏人一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为小雪拉你啊，\x01",
            "就算平常是好孩子，\x01",
            "坏习惯也是一大堆呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听好了，别教这两个孩子\x01",
            "一些奇怪的东西哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……我会伤心的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#025F……好，好，我知道啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_507D")

    label("loc_5026")


    ChrTalk(
        0xFE,
        (
            "你们也别学\x01",
            "小雪拉那些坏习惯哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_507D")

    Jump("loc_676D")

    label("loc_5080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_5204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5180")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "欢迎。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们两个\x01",
            "真是血气方刚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我还是希望\x01",
            "艾丝蒂尔能够更像女孩子点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哈哈哈……\x01",
            "嗯，我会注意的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5201")

    label("loc_5180")


    ChrTalk(
        0xFE,
        (
            "你们两个\x01",
            "真是血气方刚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我还是希望\x01",
            "艾丝蒂尔能够更像女孩子点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5201")

    Jump("loc_676D")

    label("loc_5204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_53FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B8")
    OP_A2(0x2AF)
    TurnDirection(0xB, 0x101, 400)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "……呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F怎、怎么啦，阿姨？\x02\x03",
            "我刚洗过脸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "艾丝蒂尔呀，你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你看起来长得\x01",
            "越来越像莱娜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎…………\x02\x03",
            "真、真的？\x02\x03",
            "#008F那真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，好怀念呀……\x01",
            "让我想起了过去的很多事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_53FC")

    label("loc_53B8")


    ChrTalk(
        0xFE,
        (
            "你们两个可要\x01",
            "认认真真地工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FC")

    Jump("loc_676D")

    label("loc_53FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_576B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D6")
    OP_A2(0x2AE)

    ChrTalk(
        0xFE,
        (
            "你们俩都要努力啊，\x01",
            "要争取让卡西乌斯先生\x01",
            "看到好成绩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，太拼命了也不行。\x01",
            "最重要的是量力而行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们还是新手，\x01",
            "有麻烦的话只管向周围求助，\x01",
            "没什么可害羞的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤其是约修亚，\x01",
            "你是那种有烦恼也自己一个人扛的类型吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "在我看来，这最叫人担心了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这一点上艾丝蒂尔\x01",
            "倒是完全不用操心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F就是！\x02\x03",
            "#009F……唔？阿姨您\x01",
            "这是夸我还是损我啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "不过反正不是什么坏事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5768")

    label("loc_56D6")


    ChrTalk(
        0xFE,
        (
            "你们还是新手，\x01",
            "有麻烦的话只管向周围求助，\x01",
            "没什么可害羞的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有需要的话，\x01",
            "可以随时来找阿姨谈谈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5768")

    Jump("loc_676D")

    label("loc_576B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_59BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F1")
    OP_A2(0x2AD)

    ChrTalk(
        0xFE,
        "欢迎，两位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡西乌斯先生\x01",
            "要出门一阵是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是有用得着的地方\x01",
            "就随时向我们开口哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们认识\x01",
            "也不是一天两天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太客气的话我可是要生气的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，\x01",
            "谢谢阿姨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59B8")

    label("loc_58F1")


    ChrTalk(
        0xFE,
        (
            "卡西乌斯先生\x01",
            "要出门一阵是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是有用得着的地方\x01",
            "就随时向我们开口哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太客气的话我可是要生气的哦。\x02",
    )

    CloseMessageWindow()

    label("loc_59B8")

    Jump("loc_676D")

    label("loc_59BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_5D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59FF")

    ChrTalk(
        0xFE,
        (
            "如果你们有空了，\x01",
            "随时都欢迎你们来吃饭哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6D")

    label("loc_59FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 4)), scpexpr(EXPR_END)), "loc_5ABB")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "如果你们有空了，\x01",
            "随时都欢迎你们来吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "做游击士很需要体力的，\x01",
            "一定要保证营养才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小雪拉也\x01",
            "常常到这里吃饭的，\x01",
            "要不你们一起过来也行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6D")

    label("loc_5ABB")

    OP_A2(0x2AC)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "我马上就开始准备晚餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔你们\x01",
            "也一起来吃如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "让我好好给你们做一顿饭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，今天就算了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么，\x01",
            "不喜欢阿姨做的料理吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F……哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小时候明明\x01",
            "那么喜欢吃的。\x01",
            "呜呜呜呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F不、不是啦，阿姨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F抱歉，阿姨，\x01",
            "因为今天父亲在家里等我们回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "卡西乌斯先生一个人在家的话，\x01",
            "那也很可怜的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D6D")

    Jump("loc_676D")

    label("loc_5D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_60DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6032")
    OP_A2(0x2AB)

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F阿姨，听我说！听我说！\x02\x03",
            "我终于成为\x01",
            "一名游击士了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀呀，真的吗？\x01",
            "这么说来约修亚也是了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是的。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "呵呵，恭喜！\x01",
            "你们俩真不赖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哈哈哈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不·过·啊，\x01",
            "小艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能因为成为游击士了\x01",
            "而高兴过头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为这还只是开始而已。\x01",
            "以后的路还长着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，嗯，我明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从现在开始\x01",
            "你们两个要好好积累\x01",
            "作为游击士的经验哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从你们选择了游击士\x01",
            "这条道路开始，\x01",
            "就要为之感到自豪才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "从现在开始就好好努力吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_60DB")

    label("loc_6032")


    ChrTalk(
        0xFE,
        (
            "从现在开始\x01",
            "你们两个要好好积累\x01",
            "作为游击士的经验哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从你们选择了游击士\x01",
            "这条道路开始，\x01",
            "就要为之感到自豪才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60DB")

    Jump("loc_676D")

    label("loc_60DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66C0")
    OP_A2(0x3)
    OP_A2(0x20F)

    ChrTalk(
        0x101,
        (
            "#000F斯蒂娜阿姨，\x01",
            "早上好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "啊……\x01",
            "是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "待会儿还要去做游击士训练吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯。\x01",
            "阿姨，您看好了。\x02\x03",
            "#502F在经过严格的训练之后\x01",
            "我一定会成为不输给\x01",
            "雪拉姐的女游击士的哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "呵呵，真让人欣慰啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "咦？艾丝蒂尔啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F什、什么事？\x01",
            "为什么这样盯着人家的脸看？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你～洗脸了吗？\x01",
            "好好刷牙了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你和约修亚不一样，\x01",
            "女孩子要懂得礼仪才行哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F真是的，\x01",
            "阿姨您又老生常谈了啦。\x02\x03",
            "现在我已经不是以前那样啦。\x01",
            "是吧，约修亚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F对了，说起这个来……\x02\x03",
            "#017F你之前不是急急忙忙头发蓬乱地\x01",
            "从家里跑出去吗～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#008F啊～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x101, 0x102, 1000)

    ChrTalk(
        0x101,
        (
            "#008F那、那是因为有很急的事情嘛！\x02\x03",
            "#008F因为那时里农老板的店里\x01",
            "进了『斯托雷加』运动鞋的新品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4S艾－丝－蒂－尔！#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F怎、怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 800)

    ChrTalk(
        0xB,
        "你觉得你这么做行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "怎么说你也已经到了要嫁人的年龄了，\x01",
            "至少也应该注意一下仪表了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "衣冠不整的话，就算作为一个游击士\x01",
            "也不会让别人觉得可靠，你说是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而且衣冠整齐也是\x01",
            "精神状态良好的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F好、好的，\x01",
            "我会注意的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "这才对嘛，\x01",
            "要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F（呼～斯蒂娜阿姨\x01",
            "　还是那么啰里啰嗦啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_676D")

    label("loc_66C0")


    ChrTalk(
        0xB,
        (
            "衣冠不整的话，就算作为一个游击士\x01",
            "也不会让别人觉得可靠呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而且衣冠整齐也是\x01",
            "精神状态良好的表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676D")

    TalkEnd(0xB)
    Return()

    # Function_9_4C17 end

    def Function_10_6771(): pass

    label("Function_10_6771")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6852")
    OP_A2(0x29F)

    ChrTalk(
        0xC,
        (
            "#020F打开的是艾丝蒂尔的结晶孔呢。\x02\x03",
            "艾丝蒂尔中间的结晶孔是全属性类型的，\x01",
            "所以安装任何一种结晶回路都可以。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B8")

    label("loc_6852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_691E")
    OP_A2(0x29F)

    ChrTalk(
        0xC,
        (
            "#020F打开的是约修亚的结晶孔呢。\x02\x03",
            "约修亚中间的结晶孔是限定属性类型的，\x01",
            "所以还是早点打开其他结晶孔比较好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B8")

    label("loc_691E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_END)), "loc_69B8")

    ChrTalk(
        0xC,
        (
            "#020F先到前台那里，\x01",
            "然后在工房菜单中选择『结晶孔』，\x01",
            "这样就可以开封新的结晶孔的了。\x02\x03",
            "到底打开谁的结晶孔，\x01",
            "你们就自己商量着决定吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_69B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69D5")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_69D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x14)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69EA")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_69EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x1E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69FF")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_69FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x32)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A14")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x41)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A29")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A3E")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A53")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x14)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A68")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x1E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A7D")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x32)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A92")
    OP_A2(0x6)
    Jump("loc_6AA4")

    label("loc_6A92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x41)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AA4")
    OP_A2(0x6)

    label("loc_6AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_774C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7146")
    OP_A2(0x29E)
    OP_A2(0x29D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6D0E")

    ChrTalk(
        0xC,
        (
            "#023F怎么，已经设定好结晶回路了吗？\x02\x03",
            "#020F嗯，看来你们已经\x01",
            "可以使用回复和攻击的魔法了。\x01",
            "不用我再说明什么了吧。\x02\x03",
            "平衡好两个人能使用的魔法，\x01",
            "这样战斗起来会更加得心应手的。\x02\x03",
            "顺便一提，\x01",
            "结晶回路所具有的功能和魔法效果，\x01",
            "都在游击士手册里有详细的记载。 \x02\x03",
            "如果想使用更强力的魔法，\x01",
            "自己多花点功夫研究手册里的\x01",
            "魔法列表和结晶回路列表就行了。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 20)
    Jump("loc_7143")

    label("loc_6D0E")


    ChrTalk(
        0xC,
        (
            "#020F嗯，看来你们已经\x01",
            "可以使用回复和攻击的魔法了。\x02\x03",
            "平衡好两个人能使用的魔法，\x01",
            "这样战斗起来会更加得心应手的。\x02\x03",
            "顺便一提，\x01",
            "结晶回路所具有的功能和魔法效果，\x01",
            "都在游击士手册里有详细的记载。 \x02\x03",
            "如果想使用更强力的魔法，\x01",
            "自己多花点功夫研究手册里的\x01",
            "魔法列表和结晶回路列表就行了。\x02\x03",
            "——那么，\x01",
            "在工房的研修也接近尾声了。\x02\x03",
            "最后要做的就是\x01",
            "让你们试试开封新的结晶孔。\x02\x03",
            "结晶孔数增加的话，\x01",
            "可供使用的魔法也就更加多样。\x02\x03",
            "使用魔法时所消耗的ＥＰ值上限\x01",
            "也由打开的结晶孔数量决定，\x01",
            "所以早点开封既有利又方便自己。\x02\x03",
            "那么，就用试试这些耀晶片\x01",
            "开封导力器上的结晶孔吧。\x02\x03",
            "打开谁的结晶孔都没关系，\x01",
            "你们两人自己决定吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7143")

    Jump("loc_76D1")

    label("loc_7146")

    OP_A2(0x29E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_731D")

    ChrTalk(
        0xC,
        (
            "#020F嗯，看来你们已经\x01",
            "可以使用回复和攻击的魔法了。\x02\x03",
            "平衡好两个人能使用的魔法，\x01",
            "这样战斗起来会更加得心应手的。\x02\x03",
            "顺便一提，\x01",
            "结晶回路所具有的功能和魔法效果，\x01",
            "都在游击士手册里有详细的记载。 \x02\x03",
            "如果想使用更强力的魔法，\x01",
            "自己多花点功夫研究手册里的\x01",
            "魔法列表和结晶回路列表就行了。\x02\x03",
        )
    )

    CloseMessageWindow()
    Call(0, 20)
    Jump("loc_76D1")

    label("loc_731D")


    ChrTalk(
        0xC,
        (
            "#020F嗯，看来你们已经\x01",
            "可以使用回复和攻击的魔法了。\x02\x03",
            "平衡好两个人能使用的魔法，\x01",
            "这样战斗起来会更加得心应手的。\x02\x03",
            "顺便一提，\x01",
            "结晶回路所具有的功能和魔法效果，\x01",
            "都在游击士手册里有详细的记载。 \x02\x03",
            "如果想使用更强力的魔法，\x01",
            "自己多花点功夫研究手册里的\x01",
            "魔法列表和结晶回路列表就行了。\x02\x03",
            "——那么，\x01",
            "在工房的研修也接近尾声了。\x02\x03",
            "最后要做的就是\x01",
            "让你们试试开封新的结晶孔。\x02\x03",
            "结晶孔数增加的话，\x01",
            "可供使用的魔法也就更加多样。\x02\x03",
            "使用魔法时所消耗的ＥＰ值上限\x01",
            "也由打开的结晶孔数量决定，\x01",
            "所以早点开封既有利又方便自己。\x02\x03",
            "那么，就用试试这些耀晶片\x01",
            "开封导力器上的结晶孔吧。\x02\x03",
            "打开谁的结晶孔都没关系，\x01",
            "你们两人自己决定吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得到各种属性的耀晶片。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 0x1E)
    AddSepith(0x1, 0x1E)
    AddSepith(0x2, 0x1E)
    AddSepith(0x3, 0x1E)
    TalkEnd(0xC)
    Return()

    label("loc_774C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7757")
    Jump("loc_790F")

    label("loc_7757")


    ChrTalk(
        0xC,
        (
            "#020F把结晶回路安装在导力器上，\x01",
            "保证可以使用回复魔法和攻击魔法。\x02\x03",
            "观察自己的导力器，\x01",
            "合理分配回复魔法和攻击魔法的比例。\x02\x03",
            "要安装哪个结晶回路，\x01",
            "可以先看看游击士手册中的\x01",
            "魔法列表和结晶回路列表后再决定。\x02\x03",
            "必要的结晶回路不够的话，\x01",
            "凑够耀晶片到工房合成就行了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_790F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x273)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x258)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x25E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x261)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x26D)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AB4")
    OP_A2(0x29D)

    ChrTalk(
        0xC,
        (
            "#020F嗯，看来合成好了。\x02\x03",
            "那么，接下来就试试\x01",
            "增加可供使用的魔法吧。\x02\x03",
            "把结晶回路安装在导力器上，\x01",
            "设定好回复类和攻击类的魔法吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※结晶回路的安装在[Orbment]界面进行。\x01",
            "　要开启[Orbment]界面\x01",
            "　只需在Camp中点击[Orbment]即可。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xC)
    Return()

    label("loc_7AB4")


    ChrTalk(
        0xC,
        (
            "#020F试试合成结晶回路吧。\x02\x03",
            "艾丝蒂尔任何属性的都ＯＫ，\x01",
            "不过约修亚不能安装时属性以外的，\x01",
            "所以这点要注意一下哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_7BA5")

    Call(0, 20)
    Return()

    # Function_10_6771 end

    def Function_11_7BAA(): pass

    label("Function_11_7BAA")

    TalkBegin(0xD)

    NpcTalk(
        0xD,
        "戴眼镜的女性",
        "#0151F哇～～好可爱呢～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_11_7BAA end

    def Function_12_7BE8(): pass

    label("Function_12_7BE8")

    OP_8F(0x101, 0xFFFF63D3, 0x0, 0xFFFFED2B, 0xBB8, 0x0)
    OP_8C(0x101, 0, 0)
    OP_8F(0x101, 0xFFFF66E7, 0x0, 0xFFFFE49E, 0xBB8, 0x0)
    Return()

    # Function_12_7BE8 end

    def Function_13_7C18(): pass

    label("Function_13_7C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CC3")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0xC, 0x320)

    def lambda_7C38():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7C38)

    def lambda_7C46():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7C46)

    ChrTalk(
        0xC,
        (
            "#024F怎么了，想出去吗？\x01",
            "研修还没结束呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7CC3")

    Return()

    # Function_13_7C18 end

    def Function_14_7CC4(): pass

    label("Function_14_7CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D6F")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0xC, 0x320)

    def lambda_7CE4():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7CE4)

    def lambda_7CF2():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7CF2)

    ChrTalk(
        0xC,
        (
            "#024F怎么了，想出去吗？\x01",
            "研修还没结束呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7D6F")

    Return()

    # Function_14_7CC4 end

    def Function_15_7D70(): pass

    label("Function_15_7D70")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x0, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D97")
    OP_A2(0x29F)
    OP_A2(0x7)
    Jump("loc_7DAA")

    label("loc_7D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_BB(0x1, 0x5)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DAA")
    OP_A2(0x29F)
    OP_A2(0x7)

    label("loc_7DAA")

    SetChrPos(0xC, -41600, 0, -1337, 270)
    SetChrPos(0x101, -43651, 0, -651, 90)
    SetChrPos(0x102, -43651, 0, -2165, 90)
    OP_6D(-43106, 0, -929, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0xC,
        (
            "#020F在这里学习一下\x01",
            "有关工房的主要用途和具体操作。\x02\x03",
            "#020F在工房里，\x01",
            "可以改造驱动导力魔法所专用的导力器，\x01",
            "以及合成功能各异的结晶回路。\x02\x03",
            "#020F魔法能发挥各种不同的效果，\x01",
            "熟练掌握的话会给工作带来种种的便利。\x02\x03",
            "#020F游击士是一种经常伴随着危险的职业，\x01",
            "因此每一个游击士都会\x01",
            "长时间和各地的工房打交道。\x02\x03",
            "#020F……嗯，\x01",
            "我能说的也只有这些了。\x02\x03",
            "#020F关于导力器技术方面的内容\x01",
            "就要由专家为你们解释了。\x02\x03",
            "#020F……就是这样了。\x01",
            "梅尔达斯先生，之后就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8046():

        label("loc_8046")

        TurnDirection(0xC, 0x0, 0)
        OP_48()
        Jump("loc_8046")

    QueueWorkItem2(0xC, 1, lambda_8046)
    OP_4A(0x9, 0)
    OP_6D(-41136, 0, -889, 800)

    ChrTalk(
        0x9,
        "嗯，交给我吧。\x02",
    )

    CloseMessageWindow()

    def lambda_8095():
        OP_69(0x9, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8095)

    def lambda_80A3():
        OP_8E(0x102, 0xFFFF5D77, 0x0, 0xFFFFFE70, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80A3)
    OP_8E(0x101, 0xFFFF5D77, 0x0, 0x1A7, 0xBB8, 0x0)
    OP_8C(0x101, 90, 400)
    OP_8C(0x102, 90, 400)

    label("loc_80DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DE6")

    ChrTalk(
        0x9,
        "那么，想知道什么呢？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8176")

    Menu(
        0,
        10,
        100,
        0,
        (
            "【导力器】\x01",                # 0
            "【导力魔法（魔法）】\x01",      # 1
            "【结晶回路】\x01",              # 2
            "【耀晶片】\x01",                # 3
            "【放弃】\x01",                  # 4
        )
    )

    Jump("loc_81A9")

    label("loc_8176")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【导力器】\x01",                # 0
            "【导力魔法（魔法）】\x01",      # 1
            "【结晶回路】\x01",              # 2
            "【耀晶片】\x01",                # 3
        )
    )


    label("loc_81A9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_81E3"),
        (1, "loc_85EC"),
        (2, "loc_8A02"),
        (3, "loc_8C34"),
        (4, "loc_8DD1"),
        (SWITCH_DEFAULT, "loc_8DE1"),
    )


    label("loc_81E3")


    ChrTalk(
        0x9,
        (
            "导力器就是\x01",
            "通过设定结晶回路来\x01",
            "发挥各种各样效果的机械部件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "按照这个定义，\x01",
            "照明用具、飞艇引擎等物品\x01",
            "都是用导力器制成的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过这里所说的导力器是指\x01\x07\x04",
            "提高持有者身体能力、使其能够使用魔法\x01\x07\x00",
            "的『战术导力器』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这是按照各人实际情况而定制的一种导力器，\x01",
            "也是最适合个人使用的战斗工具。\x01\x07\x04",
            "持有者不同，其结构也会有所差异\x07\x00",
            "的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "具体来说，限定属性的结晶孔和\x01",
            "连接结晶孔的结晶链形状都有所不同……\x01",
            "不过，现在还不需要讲得太深奥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要想设定结晶回路，\x01",
            "就要先开封结晶孔才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "中间的结晶孔一开始就是打开的，\x01",
            "其余的就必须要在工房进行开封。\x01",
            "要注意，开封的时候需要耀晶片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "用来发动导力魔法的ＥＰ值上限，\x01\x07\x04",
            "会随着开封的结晶孔数增加\x07\x00",
            "而不断上升。\x01",
            "所以尽快把结晶孔全部打开是很有益处的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_85EC")


    ChrTalk(
        0x9,
        (
            "这个嘛……\x01",
            "说得通俗点说就是\x01",
            "使用专用的『战术导力器』来发动的魔法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "也就是使用导力器中蓄积的\x01",
            "一种叫做『导力』的能量，\x01",
            "来引起各种各样奇妙的现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为导力魔法这个名字念起来太拗口，\x01",
            "所以现在大家都魔法、魔法这样地称呼。\x01",
            "真是的，一开始就这么叫不就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "魔法有很多不同的种类，\x01",
            "想要使用的话，\x01",
            "先得在工房合成结晶回路才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "然后把合成好的结晶回路\x01",
            "安装在导力器的结晶孔里面，\x01",
            "这样就可以使用魔法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "可供使用的魔法\x01\x07\x04",
            "会依照安装在导力器里的\x01\x07\x00",
            "结晶回路的属性组合而变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "想使用水系的魔法，\x01",
            "将带有水属性值的结晶回路\x01",
            "安装在导力器里面就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……嗯，老实说，\x01",
            "实际操作要比单纯解释原理更加复杂，\x01",
            "不过目前掌握这些知识就够用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_8A02")


    ChrTalk(
        0x9,
        (
            "结晶回路其实就是\x01",
            "用耀晶片加工而成的回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x4),
            "提升持有者各项能力\x07\x00",
            "的同时，\x01\x07\x04",
            "使其能够使用各种魔法\x07\x00",
            "是结晶回路最重要的作用。\x01",
            "这种回路拥有的效果实在是非常之多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "结晶回路必须安装在导力器的结晶孔里\x01",
            "才能发挥作用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而根据结晶孔的不同，也有些\x07\x04",
            "只能安装\x01",
            "某种属性结晶回路\x07\x00",
            "的具有限定属性的结晶孔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "合成新的结晶回路之前，\x01",
            "最好先考虑好要把它\x01",
            "安装在导力器的哪一个位置上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_8C34")


    ChrTalk(
        0x9,
        (
            "耀晶片指的是\x01",
            "魔兽身上掉落的七耀石碎片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "颜色和属性相对，一共分为\x01",
            "#182I地（棕色）、#56I水（蓝色）、火（红色）、风（绿色）、\x01",
            "时（黑色）、空（金色）、幻（银色）\x01",
            "７种耀晶片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽说在王国每个城市里都有很多\x01\x07\x04",
            "可以把耀晶片换成流通货币米拉\x07\x00",
            "的店铺……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过在工房里可以用它来\x01",
            "合成具有各种不同属性的结晶回路，\x01",
            "以及开封用来安装结晶回路的结晶孔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE1")

    label("loc_8DD1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_8DE1")

    label("loc_8DE1")

    OP_56(0x0)
    Jump("loc_80DA")

    label("loc_8DE6")


    def lambda_8DEC():
        TurnDirection(0x0, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8DEC)

    def lambda_8DFA():
        TurnDirection(0x1, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8DFA)
    OP_69(0xC, 0x3E8)

    ChrTalk(
        0xC,
        (
            "#020F看起来没什么问题了吧。\x02\x03",
            "那么，\x01",
            "接下来就要动手自己操作一下了。\x02\x03",
            "为了让你们动手试试，\x01",
            "我给你们准备了一些必要的耀晶片。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得到各种属性的耀晶片。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x14)
    AddSepith(0x3, 0x14)
    AddSepith(0x4, 0x14)
    AddSepith(0x5, 0x14)
    AddSepith(0x6, 0x14)

    ChrTalk(
        0xC,
        (
            "#020F有了这些耀晶片，\x01",
            "就可以合成几个结晶回路了。\x02\x03",
            "先合成与自己的导力器\x01",
            "相应属性的结晶回路看看吧。\x02\x03",
            "艾丝蒂尔任何属性的都ＯＫ，\x01",
            "不过约修亚只能安装时属性的哦。\x02\x03",
            "本来在商店可以把耀晶片换成钱，\x01",
            "不过考虑到现在是研修中，\x01",
            "所以暂时还不能让你们换。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※站在柜台附近时会出现『TALK』的标记，\x01",
            "　用右键点击会出现选择菜单。\x01",
            "　选择工房菜单中的『改造·换钱』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    OP_4B(0x9, 0)
    Return()

    # Function_15_7D70 end

    def Function_16_91D4(): pass

    label("Function_16_91D4")

    OP_A2(0x253)
    OP_28(0x19, 0x1, 0x40)
    EventBegin(0x0)
    AddParty(0xF, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9224")
    SetChrPos(0x101, -42590, 0, 1660, 135)
    SetChrPos(0x102, -43440, 0, 1640, 135)
    SetChrPos(0x2, -42910, 0, 520, 135)
    Jump("loc_9257")

    label("loc_9224")

    SetChrPos(0x101, -38220, 0, -5030, 0)
    SetChrPos(0x102, -39380, 0, -5260, 0)
    SetChrPos(0x2, -38890, 0, -4019, 0)

    label("loc_9257")

    SetChrPos(0x3, -38530, 0, -2400, 0)
    OP_4A(0x8, 0)
    TurnDirection(0x8, 0x3, 0)
    ClearMapFlags(0x1)
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_69(0xE, 0x7D0)
    OP_0D()
    OP_62(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(
        0x3,
        "戴眼镜的女性",
        (
            "#152F啊啊，求求您～！\x02\x03",
            "#152F我什么都愿意做，\x01",
            "只要能把照相机还我！\x02\x03",
            "#152F那可是比我的生命还宝贵的东西啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "真、真伤脑筋啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "老爹，该怎么办好呢？\x02",
    )

    CloseMessageWindow()
    OP_4A(0x9, 0)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "那是你接下的工作，\x01",
            "你自己处理吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_4B(0x9, 0)
    TurnDirection(0x8, 0x3, 400)
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xE, 0x320)

    ChrTalk(
        0x101,
        "#004F大家好像在争吵什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F难道，就是那个人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        "#145F……………………就是她。\x02",
    )

    CloseMessageWindow()
    OP_43(0xE, 0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952A")
    OP_8E(0x2, 0xFFFF5CF9, 0x0, 0xFFFFF6A0, 0xBB8, 0x0)
    OP_8E(0x2, 0xFFFF6582, 0x0, 0xFFFFF6A0, 0xBB8, 0x0)
    Jump("loc_953E")

    label("loc_952A")

    OP_8E(0x2, 0xFFFF6582, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)

    label("loc_953E")

    TurnDirection(0x2, 0x3, 400)

    ChrTalk(
        0x2,
        (
            "#144F#3P喂，朵洛希！\x01",
            "你要我等到什么时候啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x3, 0x2, 400)
    TurnDirection(0x8, 0x2, 400)

    ChrTalk(
        0x3,
        (
            "#153F#2P啊啊，奈尔前辈！\x01",
            "你来得正好！\x02\x03",
            "#152F呜呜，赶快帮帮我呀～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#142F#3P这次你又干了些什么？\x02\x03",
            "#142F是不是乱花钱，\x01",
            "结果照相机的修理费不够了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x3,
        (
            "#153F#2P哇，真是太厉害了！\x01",
            "你怎么会知道的？\x02\x03",
            "#153F前辈，难道你有超能力？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#144F#3P老是重复又重复地做同样的蠢事，\x01",
            "白痴也会知道啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "客人，您认识这位小姐吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果认识的话……\x01",
            "可以麻烦您替她垫付一下修理费吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x8, 400)

    ChrTalk(
        0x2,
        (
            "#145F#3P没办法……\x01",
            "就算在经费里吧。\x02\x03",
            "#145F多少钱？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "照相机和装饰用钟表的修理费\x01",
            "一共是２０００米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x2, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x2,
        (
            "#144F#3P等一下！\x02\x03",
            "#144F照相机就算了，\x01",
            "那个装饰用钟表是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        (
            "#151F#2P那个，你听我说，\x01",
            "修理相机的时候我在店里参观。\x02\x03",
            "#151F然后发现一个漂亮的座钟，\x01",
            "可是我拿起来看的时候却弄坏了……\x02\x03",
            "#151F不过不过，你来了就好了㈱\x01",
            "那个也可以算在经费里～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x3, 400)

    ChrTalk(
        0x2,
        (
            "#144F#3P这种东西怎可以算在经费里！\x02\x03",
            "#145F可、可恶……\x01",
            "只能先自掏腰包垫上了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x8, 400)

    ChrTalk(
        0x2,
        "#142F#3P给，２０００米拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "好的，这是收据。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B0C")
    OP_6D(-42770, 0, 1380, 1500)
    Jump("loc_9B1D")

    label("loc_9B0C")

    OP_6D(-38130, 0, -4670, 1500)

    label("loc_9B1D")


    ChrTalk(
        0x101,
        (
            "#008F（看、看起来……\x01",
            "　这对记者组合挺有趣的呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（确实是……）\x02\x03",
            "#010F（虽然那个男的脾气不太好，\x01",
            "　不过看起来也很会照顾人啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x3, 0xFF)
    OP_43(0x2, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5C")
    OP_8E(0x3, 0xFFFF5D62, 0x0, 0xFFFFF66E, 0xBB8, 0x0)
    OP_8E(0x3, 0xFFFF58F8, 0x0, 0xFFFFFD26, 0xBB8, 0x0)
    OP_8C(0x3, 0, 400)
    Jump("loc_9C77")

    label("loc_9C5C")

    OP_8C(0x3, 180, 400)
    OP_8E(0x3, 0xFFFF699C, 0x0, 0xFFFFF164, 0x7D0, 0x0)

    label("loc_9C77")


    ChrTalk(
        0x2,
        (
            "#145F哦哦，久等了。\x01",
            "稍微遇到了点麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        "#150F咦，前辈，这些孩子是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#140F他们是给我们护卫兼带路的。\x02\x03",
            "#140F代替卡西乌斯·布莱特\x01",
            "接受我们委托的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        "#153F哇，这么年轻的孩子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F我叫艾丝蒂尔，请多关照哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我叫约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        (
            "#151F是小艾和小约啊。\x01",
            "虽然很年轻，不过看起来很可靠啊。\x02\x03",
            "#151F我叫朵洛希·海娅特。\x02\x03",
            "#151F是刚进入《利贝尔通讯》的新人摄影师哦。\x01",
            "　\x02\x03",
            "#151F正在奈尔前辈的指导下努力工作，\x01",
            "也请你们多多指教哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2,
        (
            "#145F为什么非要我照顾\x01",
            "这么一个脱线的女生呢……\x02\x03",
            "#145F真是的，那个大胡子总编……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        (
            "#151F算啦算啦～\x01",
            "努力到最后一定会有好报的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x3, 400)

    ChrTalk(
        0x2,
        (
            "#144F你给我住嘴，你呀！\x02\x03",
            "#145F唉、算了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2, 0x102, 400)

    ChrTalk(
        0x2,
        (
            "#140F人已经到齐了，\x01",
            "我们赶快出发去取材吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F目的地是城外的『翡翠之塔』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F好的～我们出发吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3,
        "#151F噢！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_91D4 end

    def Function_17_A0C1(): pass

    label("Function_17_A0C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E1")
    OP_6D(-39730, 0, -1830, 2000)
    Jump("loc_A0F2")

    label("loc_A0E1")

    OP_6D(-37205, 0, -2234, 2000)

    label("loc_A0F2")

    Return()

    # Function_17_A0C1 end

    def Function_18_A0F3(): pass

    label("Function_18_A0F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A13F")
    OP_8E(0x2, 0xFFFF5D62, 0x0, 0xFFFFF66E, 0xBB8, 0x0)
    OP_8E(0x2, 0xFFFF55D8, 0x0, 0x1E, 0xBB8, 0x0)
    OP_8C(0x2, 0, 400)
    OP_8C(0x101, 180, 400)
    OP_8C(0x102, 180, 400)
    Jump("loc_A15A")

    label("loc_A13F")

    OP_8C(0x2, 180, 400)
    OP_8E(0x2, 0xFFFF65F0, 0x0, 0xFFFFF092, 0x7D0, 0x0)

    label("loc_A15A")

    Return()

    # Function_18_A0F3 end

    def Function_19_A15B(): pass

    label("Function_19_A15B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A176")
    TurnDirection(0x3, 0x2, 0)
    TurnDirection(0x8, 0x2, 0)
    OP_48()
    Jump("Function_19_A15B")

    label("loc_A176")

    Return()

    # Function_19_A15B end

    def Function_20_A177(): pass

    label("Function_20_A177")

    Sleep(100)
    Fade(1000)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_44(0xC, 0x1)
    OP_8C(0xC, 270, 0)
    SetChrPos(0x101, -42760, 0, -2149, 45)
    SetChrPos(0x102, -42760, 0, -936, 135)
    OP_6D(-42964, 0, -712, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#020F这么一来，\x01",
            "在工房的研修就结束了。\x02\x03",
            "那么，接下来终于轮到\x01",
            "你们期盼已久的认定考试了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F……哎？\x02\x03",
            "#004F考、考试，是什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    def lambda_A2C1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2C1)

    ChrTalk(
        0x102,
        (
            "#018F……不会吧，你真的忘了吗？\x02\x03",
            "今天早上才刚和你说过啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊……\x02\x03",
            "这么说来，\x01",
            "好像听说过，又好像没有……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3D2():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3D2)

    ChrTalk(
        0xC,
        (
            "#025F唉……\x01",
            "你还真是个不负众望的孩子啊。\x02\x03",
            "#020F算了。\x01",
            "不管了，赶快去考场再说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#004F哎！？这、这就！？\x02\x03",
            "#004F等、等一下，\x01",
            "我还没做好心理准备呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#024F好啦好啦，\x01",
            "乖乖地跟着我走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_8E(0xC, 0xFFFF5AF3, 0x0, 0xFFFFF60B, 0xBB8, 0x0)
    TurnDirection(0x102, 0x101, 0)
    OP_8C(0xC, 315, 400)
    OP_8C(0x101, 315, 1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x101, 0x1, 0x0, 0xC)
    OP_8E(0xC, 0xFFFF63D3, 0x0, 0xFFFFED2B, 0xBB8, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0xC, 0xFFFF66E7, 0x0, 0xFFFFE49E, 0xBB8, 0x0)
    Sleep(200)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0xBE)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(300)

    ChrTalk(
        0x101,
        "#003F约修亚，救命啊～\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    OP_63(0x102)
    Sleep(100)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F梅尔达斯先生、弗莱迪先生，\x01",
            "非常感谢你们的指点。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x9, 0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        "不客气，考试考好点就行了。\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "好好加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F喂～约修亚！\x01",
            "你给我记住～！！\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_20_A177 end

    SaveToFile()

Try(main)
