from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3220   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3220.x',
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
        'ED6_DT07/CH01210 ._CH',             # 09
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
        'ED6_DT07/CH01210P._CP',             # 09
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25E",          # 00, 0
        "Function_1_3EA",          # 01, 1
        "Function_2_40C",          # 02, 2
        "Function_3_422",          # 03, 3
        "Function_4_531",          # 04, 4
        "Function_5_538",          # 05, 5
        "Function_6_53F",          # 06, 6
        "Function_7_666",          # 07, 7
        "Function_8_66D",          # 08, 8
        "Function_9_674",          # 09, 9
        "Function_10_67B",         # 0A, 10
        "Function_11_682",         # 0B, 11
        "Function_12_F05",         # 0C, 12
        "Function_13_1128",        # 0D, 13
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402")
    OP_B1("t3220_y")
    Jump("loc_40B")

    label("loc_402")

    OP_B1("t3220_n")

    label("loc_40B")

    Return()

    # Function_1_3EA end

    def Function_2_40C(): pass

    label("Function_2_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_421")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_40C")

    label("loc_421")

    Return()

    # Function_2_40C end

    def Function_3_422(): pass

    label("Function_3_422")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_42F")
    Jump("loc_52D")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_439")
    Jump("loc_52D")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_443")
    Jump("loc_52D")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_44D")
    Jump("loc_52D")

    label("loc_44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_457")
    Jump("loc_52D")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_461")
    Jump("loc_52D")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_51C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4AF")

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
    Jump("loc_519")

    label("loc_4AF")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "离吃饭还早着呢，\x01",
            "温泉又因为水泵的故障不能用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……这样的话， \x01",
            "要做的事果然就是购物了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519")

    Jump("loc_52D")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_526")
    Jump("loc_52D")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_52D")

    label("loc_52D")

    TalkEnd(0xFE)
    Return()

    # Function_3_422 end

    def Function_4_531(): pass

    label("Function_4_531")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_4_531 end

    def Function_5_538(): pass

    label("Function_5_538")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_538 end

    def Function_6_53F(): pass

    label("Function_6_53F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_54C")
    Jump("loc_662")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_556")
    Jump("loc_662")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_560")
    Jump("loc_662")

    label("loc_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_56A")
    Jump("loc_662")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_574")
    Jump("loc_662")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5F3")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "有没有其他要买的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 330, 800)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

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
    Jump("loc_644")

    label("loc_5F3")

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

    label("loc_644")

    Jump("loc_662")

    label("loc_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_651")
    Jump("loc_662")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_65B")
    Jump("loc_662")

    label("loc_65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_662")

    label("loc_662")

    TalkEnd(0xFE)
    Return()

    # Function_6_53F end

    def Function_7_666(): pass

    label("Function_7_666")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_666 end

    def Function_8_66D(): pass

    label("Function_8_66D")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_66D end

    def Function_9_674(): pass

    label("Function_9_674")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_674 end

    def Function_10_67B(): pass

    label("Function_10_67B")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_67B end

    def Function_11_682(): pass

    label("Function_11_682")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0")
    OP_0D()
    OP_A9(0x44)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_6E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F1")
    TalkEnd(0xF)
    Return()

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_756")

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
    Jump("loc_7E3")

    label("loc_756")

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

    label("loc_7E3")

    Jump("loc_F01")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_92A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_865")

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
    Jump("loc_927")

    label("loc_865")

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

    label("loc_927")

    Jump("loc_F01")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_9DB")

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
    Jump("loc_ABC")

    label("loc_9DB")

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

    label("loc_ABC")

    Jump("loc_F01")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B35")

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
    Jump("loc_F01")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B89")

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
    Jump("loc_BDC")

    label("loc_B89")

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

    label("loc_BDC")

    Jump("loc_F01")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C36")

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
    Jump("loc_CB8")

    label("loc_C36")

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

    label("loc_CB8")

    Jump("loc_F01")

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D10")

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
    Jump("loc_D71")

    label("loc_D10")

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

    label("loc_D71")

    Jump("loc_F01")

    label("loc_D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DD9")

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
    Jump("loc_E28")

    label("loc_DD9")

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

    label("loc_E28")

    Jump("loc_F01")

    label("loc_E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E8D")

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
    Jump("loc_F01")

    label("loc_E8D")

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

    label("loc_F01")

    TalkEnd(0xF)
    Return()

    # Function_11_682 end

    def Function_12_F05(): pass

    label("Function_12_F05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_F12")
    Jump("loc_1124")

    label("loc_F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_F1C")
    Jump("loc_1124")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_F26")
    Jump("loc_1124")

    label("loc_F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F67")

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
    Jump("loc_1124")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_FE5")

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
    Jump("loc_106E")

    label("loc_FE5")

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

    label("loc_106E")

    Jump("loc_1124")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_10C1")

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
    Jump("loc_1106")

    label("loc_10C1")

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

    label("loc_1106")

    Jump("loc_1124")

    label("loc_1109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_1113")
    Jump("loc_1124")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_111D")
    Jump("loc_1124")

    label("loc_111D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1124")

    label("loc_1124")

    TalkEnd(0xFE)
    Return()

    # Function_12_F05 end

    def Function_13_1128(): pass

    label("Function_13_1128")

    Call(0, 11)
    Return()

    # Function_13_1128 end

    SaveToFile()

Try(main)
