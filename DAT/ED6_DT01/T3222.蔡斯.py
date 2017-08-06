from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3222   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3222.x',
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
        '拜舍尔',                               # 9
        '艾德',                                 # 10
        '林',                                   # 11
        '莉西亚',                               # 12
        '希利尔',                               # 13
        '艾缇',                                 # 14
        '拉克',                                 # 15
        '希玛',                                 # 16
        '库安',                                 # 17
        '艾德尔',                               # 18
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01160 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01130 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01160P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01130P._CP',             # 09
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 2440,
        TriggerZ            = 250,
        TriggerY            = 2960,
        TriggerRange        = 400,
        ActorX              = 2550,
        ActorZ              = 1750,
        ActorY              = 4470,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25E",          # 00, 0
        "Function_1_3EA",          # 01, 1
        "Function_2_3EB",          # 02, 2
        "Function_3_401",          # 03, 3
        "Function_4_49C",          # 04, 4
        "Function_5_4A3",          # 05, 5
        "Function_6_4AA",          # 06, 6
        "Function_7_5B3",          # 07, 7
        "Function_8_5BA",          # 08, 8
        "Function_9_5C1",          # 09, 9
        "Function_10_5C8",         # 0A, 10
        "Function_11_5CF",         # 0B, 11
        "Function_12_5D4",         # 0C, 12
        "Function_13_E57",         # 0D, 13
    )


    def Function_0_25E(): pass

    label("Function_0_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_27E")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_29E")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2BE")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2F4")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -960, 250, -2580, 188)
    Jump("loc_3E9")

    label("loc_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5240, 500, -330, 108)
    Jump("loc_3E9")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_376")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 590, 250, 2540, 10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4130, 0, -2220, 291)
    Jump("loc_3E9")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_3AC")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -3250, 250, 4820, 348)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3CC")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E9")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)

    label("loc_3E9")

    Return()

    # Function_0_25E end

    def Function_1_3EA(): pass

    label("Function_1_3EA")

    Return()

    # Function_1_3EA end

    def Function_2_3EB(): pass

    label("Function_2_3EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_400")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3EB")

    label("loc_400")

    Return()

    # Function_2_3EB end

    def Function_3_401(): pass

    label("Function_3_401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_40E")
    Jump("loc_498")

    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_418")
    Jump("loc_498")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_422")
    Jump("loc_498")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_42C")
    Jump("loc_498")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_436")
    Jump("loc_498")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_440")
    Jump("loc_498")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_487")

    ChrTalk(
        0xFE,
        "嘿～真有意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个就是东方的陶器吧\x01",
            "素朴又可爱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_498")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_491")
    Jump("loc_498")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_498")

    label("loc_498")

    TalkEnd(0xFE)
    Return()

    # Function_3_401 end

    def Function_4_49C(): pass

    label("Function_4_49C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_4_49C end

    def Function_5_4A3(): pass

    label("Function_5_4A3")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_4A3 end

    def Function_6_4AA(): pass

    label("Function_6_4AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4B7")
    Jump("loc_5AF")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_5AF")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_5AF")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4D5")
    Jump("loc_5AF")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4DF")
    Jump("loc_5AF")

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_540")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "有没有其他要买的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个碟子，\x01",
            "还真是可爱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_591")

    label("loc_540")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "嗯……我记得……\x01",
            "酱油和酒都用完了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "有没有其他要买的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_591")

    Jump("loc_5AF")

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_5AF")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_5AF")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5AF")

    label("loc_5AF")

    TalkEnd(0xFE)
    Return()

    # Function_6_4AA end

    def Function_7_5B3(): pass

    label("Function_7_5B3")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_5B3 end

    def Function_8_5BA(): pass

    label("Function_8_5BA")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_5BA end

    def Function_9_5C1(): pass

    label("Function_9_5C1")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_5C1 end

    def Function_10_5C8(): pass

    label("Function_10_5C8")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_5C8 end

    def Function_11_5CF(): pass

    label("Function_11_5CF")

    Call(0, 12)
    Return()

    # Function_11_5CF end

    def Function_12_5D4(): pass

    label("Function_12_5D4")

    TalkBegin(0xF)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_632")
    OP_0D()
    OP_A9(0x44)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_632")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_643")
    TalkEnd(0xF)
    Return()

    label("loc_643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6A8")

    ChrTalk(
        0xF,
        (
            "因为女王的诞辰庆典快到了，\x01",
            "客人也越来越少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "我这个看店的\x01",
            "也困得要命……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_735")

    label("loc_6A8")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "哎呀哎呀……\x01",
            "还以为是谁，原来有客人来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "因为几乎没人来，\x01",
            "我都已经在想\x01",
            "是不是该关门了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "啊，想帮帮我的话，\x01",
            "就买点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735")

    Jump("loc_E53")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_87C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7B7")

    ChrTalk(
        0xF,
        (
            "很遗憾啊，我想在这个村子里\x01",
            "大概也不会找到什么线索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "但是难得来了，\x01",
            "不如买点温泉鸡蛋之类的特产吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_879")

    label("loc_7B7")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "啊，是你们啊……\x01",
            "工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "我从毛婆婆那里\x01",
            "听说了你们的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "我想在这个村子里\x01",
            "大概也不会找到什么线索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "算了，难得来一次，\x01",
            "至少看看这些特产，\x01",
            "挑点想买的带回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_879")

    Jump("loc_E53")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_92D")

    ChrTalk(
        0xF,
        (
            "仔细想想看，\x01",
            "还是小时候最幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "……我和妻子相遇的时候，\x01",
            "年纪正好像库安那么大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "那时候自己\x01",
            "还是个和库安一样的少年……\x01",
            "现在想想简直不敢相信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_92D")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "关于蔡斯事件的话题\x01",
            "在大人们当中引起了很大的骚动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "但是库安他们一点也没受影响，\x01",
            "还是和往常一样天真无邪地在外边玩耍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "仔细想想看，\x01",
            "还是小时候最幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "……我和妻子相遇的时候，\x01",
            "年纪正好像库安那么大呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E")

    Jump("loc_E53")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A87")

    ChrTalk(
        0xF,
        "哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "已经要回去了吗？\x01",
            "买点特产作纪念怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "来这里的游客们\x01",
            "都会买很多特产带回去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_ADB")

    ChrTalk(
        0xF,
        "呼，腰痛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "把店里收拾完以后\x01",
            "就去『红叶亭』休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2E")

    label("loc_ADB")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "咦……\x01",
            "还以为是谁，原来有客人来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "马上就关门了，\x01",
            "要买东西请尽快哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2E")

    Jump("loc_E53")

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B88")

    ChrTalk(
        0xF,
        (
            "哎呀……\x01",
            "又到天黑的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这一天\x01",
            "就这样平平淡淡地结束了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0A")

    label("loc_B88")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "我们会向观光的客人\x01",
            "推荐这里的土特产品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "当然，\x01",
            "本店里同样也卖村民的生活必需品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "因为村子里\x01",
            "没有其他的商店了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0A")

    Jump("loc_E53")

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C62")

    ChrTalk(
        0xF,
        (
            "啊，\x01",
            "终于有客人来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这些陶器很值得推荐，\x01",
            "请慢慢看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC3")

    label("loc_C62")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "等了好久，\x01",
            "终于有客人来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这些陶器很值得推荐，\x01",
            "请慢慢看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC3")

    Jump("loc_E53")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D2B")

    ChrTalk(
        0xF,
        (
            "我的儿子库安\x01",
            "性格十分活泼外向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "这一点不太像我，\x01",
            "倒更像我已经去世的妻子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_D2B")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "呼，\x01",
            "今天没什么客人光顾呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "库安那小子，\x01",
            "有没有在用心招呼客人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7A")

    Jump("loc_E53")

    label("loc_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DDF")

    ChrTalk(
        0xF,
        "欢迎～请进吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "温泉鸡蛋的食用方法\x01",
            "也有很多种哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "请一定要试试看。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_DDF")

    OP_A2(0x7)

    ChrTalk(
        0xF,
        (
            "啊啊……\x01",
            "还以为是谁，原来有客人来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "欢迎。\x01",
            "请、请慢慢看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "我个人最推荐的特产\x01",
            "就要数温泉蛋了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E53")

    TalkEnd(0xF)
    Return()

    # Function_12_5D4 end

    def Function_13_E57(): pass

    label("Function_13_E57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E64")
    Jump("loc_1076")

    label("loc_E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_E6E")
    Jump("loc_1076")

    label("loc_E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_E78")
    Jump("loc_1076")

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_EB9")

    ChrTalk(
        0xFE,
        "啊，真没劲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "店里的事做完之后\x01",
            "就去外边玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1076")

    label("loc_EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_F37")

    ChrTalk(
        0xFE,
        (
            "虽然这么说，\x01",
            "没有客人来真是不太安心。\x01",
            "爸爸让我去招揽顾客。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的爸爸就像\x01",
            "图画书里的那个没用的爸爸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC0")

    label("loc_F37")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "我的爸爸\x01",
            "对生意不很热心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是正累的时候\x01",
            "有客人前来光顾，\x01",
            "他就会摆出一副臭脸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那样可不行啊。\x01",
            "爸爸根本不适合做生意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC0")

    Jump("loc_1076")

    label("loc_FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_105B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1013")

    ChrTalk(
        0xFE,
        (
            "啊，怎么了？\x01",
            "要买温泉蛋吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咕噜咕噜的，咕噜咕噜的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1058")

    label("loc_1013")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "啊～～\x01",
            "来点温泉蛋怎么样～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "咕噜咕噜的\x01",
            "好吃的温泉蛋啊～～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1058")

    Jump("loc_1076")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1065")
    Jump("loc_1076")

    label("loc_1065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_106F")
    Jump("loc_1076")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1076")

    label("loc_1076")

    TalkEnd(0xFE)
    Return()

    # Function_13_E57 end

    SaveToFile()

Try(main)
