from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2132   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '亚内斯特',                             # 9
        '奈尔',                                 # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '鲁特尔',                               # 13
        '兰达老人',                             # 14
        '米优',                                 # 15
        '西加罗',                               # 16
        '艾德尔',                               # 17
        '西蒙',                                 # 18
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
        'ED6_DT07/CH02470 ._CH',             # 00
        'ED6_DT07/CH01570 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT06/CH20086 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02470P._CP',             # 00
        'ED6_DT07/CH01570P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT06/CH20086P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
    )

    DeclNpc(
        X                   = -1900,
        Z                   = 0,
        Y                   = 11500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -42540,
        Z                   = 0,
        Y                   = 1360,
        Direction           = 286,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -47700,
        Z                   = 0,
        Y                   = 1570,
        Direction           = 265,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -45810,
        Z                   = 0,
        Y                   = 3660,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -43270,
        Z                   = 0,
        Y                   = 28470,
        Direction           = 79,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -45290,
        Z                   = 0,
        Y                   = 26250,
        Direction           = 269,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 27950,
        Z                   = 0,
        Y                   = 49500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = -2020,
        TriggerZ            = 0,
        TriggerY            = 10280,
        TriggerRange        = 400,
        ActorX              = -1900,
        ActorZ              = 1500,
        ActorY              = 11500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_38E",          # 01, 1
        "Function_2_3CA",          # 02, 2
        "Function_3_3E0",          # 03, 3
        "Function_4_3E5",          # 04, 4
        "Function_5_1453",         # 05, 5
        "Function_6_1454",         # 06, 6
        "Function_7_15DA",         # 07, 7
        "Function_8_163B",         # 08, 8
        "Function_9_169B",         # 09, 9
        "Function_10_16C7",        # 0A, 10
        "Function_11_1708",        # 0B, 11
        "Function_12_1744",        # 0C, 12
        "Function_13_179E",        # 0D, 13
        "Function_14_1895",        # 0E, 14
        "Function_15_1B49",        # 0F, 15
        "Function_16_1B77",        # 10, 16
        "Function_17_3970",        # 11, 17
        "Function_18_4825",        # 12, 18
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_274")
    Jump("loc_2DE")

    label("loc_274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_283")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_2DE")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_28D")
    Jump("loc_2DE")

    label("loc_28D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_2DE")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -5790, 0, 84500, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8410, 0, 83450, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_2DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB")
    SetChrPos(0x0, -8880, 0, 930, 45)

    label("loc_2FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")
    SetChrPos(0x0, -12970, 0, 4970, 45)

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335")
    SetChrPos(0x0, -11310, 0, 41790, 45)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_351")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_351")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (112, "loc_361"),
        (115, "loc_377"),
        (SWITCH_DEFAULT, "loc_38D"),
    )


    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_374")
    OP_A2(0x41A)
    Event(0, 14)

    label("loc_374")

    Jump("loc_38D")

    label("loc_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38A")
    OP_A2(0x41B)
    Event(0, 17)

    label("loc_38A")

    Jump("loc_38D")

    label("loc_38D")

    Return()

    # Function_0_26A end

    def Function_1_38E(): pass

    label("Function_1_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AF")
    OP_B1("t2132_y")
    Jump("loc_3B8")

    label("loc_3AF")

    OP_B1("t2132_n")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    OP_1B(0x0, 0x0, 0x12)

    label("loc_3C9")

    Return()

    # Function_1_38E end

    def Function_2_3CA(): pass

    label("Function_2_3CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3CA")

    label("loc_3DF")

    Return()

    # Function_2_3CA end

    def Function_3_3E0(): pass

    label("Function_3_3E0")

    Call(0, 4)
    Return()

    # Function_3_3E0 end

    def Function_4_3E5(): pass

    label("Function_4_3E5")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_445")
    OP_0D()
    OP_A9(0x21)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_456")
    TalkEnd(0x8)
    Return()

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F3")

    ChrTalk(
        0x8,
        (
            "市长被逮捕了，\x01",
            "给本市的政务也带来了麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且，\x01",
            "对旅游业也会造成许多影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_59B")

    ChrTalk(
        0x8,
        (
            "本酒店的主人\x01",
            "名字叫做诺曼，\x01",
            "他住在城市的南街区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他是一个在观光事业的发展上\x01",
            "费尽心思的实业家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62B")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "杜南公爵还要在\x01",
            "卢安停留一段日子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他好像非常\x01",
            "喜欢这个城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呼……\x02",
    )

    CloseMessageWindow()
    Jump("loc_66D")

    label("loc_62B")


    ChrTalk(
        0x8,
        (
            "杜南公爵还要在\x01",
            "卢安停留一段日子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呼……\x02",
    )

    CloseMessageWindow()

    label("loc_66D")

    Jump("loc_144F")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_74A")

    ChrTalk(
        0x8,
        (
            "马上就要到王立学院\x01",
            "举行学园祭的时候了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "学园祭每年都能吸引\x01",
            "很多毕业的学生回来参加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "毕业生中也有很多知名人士，\x01",
            "每到这个时候他们都会\x01",
            "过来光顾我们的酒店呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_8BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "公爵原本准备\x01",
            "乘船出去戏水的，\x01",
            "却被告知小船正在整修中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还是请他先去\x01",
            "艾尔·雷登的瀑布观光吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……呼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B9")

    label("loc_812")


    ChrTalk(
        0x8,
        (
            "公爵原本准备\x01",
            "乘船出去戏水的，\x01",
            "却被告知小船正在整修中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还是请他先去\x01",
            "艾尔·雷登的瀑布观光吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    Jump("loc_144F")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_END)), "loc_A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EE")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "怎么了？你们好像很着急的样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "出什么事了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#002F对不起，主管先生。\x02\x03",
            "有一件事想请问您，\x01",
            "酒店提供租船的服务对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，要租船的话，\x01",
            "请从那边的楼梯下去，\x01",
            "然后从右边的门口出去就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F下楼后右拐是吧。\x02\x03",
            "谢了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C")

    label("loc_9EE")


    ChrTalk(
        0x8,
        (
            "要租船的话\x01",
            "请从楼下右边出口出去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3C")

    Jump("loc_144F")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "两位客人，\x01",
            "昨天给你们添了非常大的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请两位放心，\x01",
            "下次绝对不会再发生同样的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "真是非常抱歉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B41")

    label("loc_AD6")


    ChrTalk(
        0x8,
        (
            "两位客人，\x01",
            "昨天给你们添了非常大的麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请两位放心，\x01",
            "下次绝对不会再发生同样的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41")

    Jump("loc_144F")

    label("loc_B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C73")
    OP_A2(0x4CD)

    ChrTalk(
        0x8,
        (
            "两位客人，这次由于我们的招待不周\x01",
            "而给你们带了诸多不便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可以的话，\x01",
            "请先在这里喝些饮料吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x1A2, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "鲜榨果汁\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "至少请接受我们的歉意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们原想为你们提供优质的服务，\x01",
            "但是居然发生了这样的事情，\x01",
            "真是十分抱歉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_C73")


    ChrTalk(
        0x8,
        (
            "我们原想为你们提供优质的服务，\x01",
            "但是居然发生了这样的事情，\x01",
            "真是十分抱歉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    Jump("loc_144F")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_END)), "loc_D24")

    ChrTalk(
        0x8,
        (
            "二位的房间\x01",
            "就在本酒店的顶楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想你们\x01",
            "一定会称心如意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "请二位好好休息吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1286")
    EventBegin(0x0)
    Fade(1000)
    OP_69(0x8, 0x0)
    OP_6B(2800, 0)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, -1830, 0, 9580, 354)
    SetChrPos(0x102, -2920, 0, 9310, 354)
    SetChrPos(0x136, -2370, 0, 8090, 354)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "这里是布朗西酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "请问客人是否已经预订了房间？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～\x01",
            "还没有呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请问现在还能订吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "几位来得真凑巧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就在刚才，\x01",
            "顶楼房间的预订被取消了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果可以的话，\x01",
            "我这就带几位过去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F顶楼房间……\x01",
            "嗯，听起来不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F但是……\x01",
            "顶楼房间的住宿费会贵很多吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为是取消预订后多出来的，\x01",
            "所以只需付普通房间的费用就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且看起来，\x01",
            "几位似乎是游击士吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "平时一直承蒙你们的照顾，\x01",
            "这次就请让我为你们打个折吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，既然您这么说，\x01",
            "那我们就恭敬不如从命啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那好，\x01",
            "我们就要了这房间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵，太好了。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10DB():
        OP_69(0x101, 0x4B0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_10DB)
    TurnDirection(0x101, 0x136, 400)
    TurnDirection(0x102, 0x136, 400)
    WaitChrThread(0x136, 0x2)

    ChrTalk(
        0x136,
        (
            "#040F那么我也\x01",
            "差不多该回学院去了。\x02\x03",
            "再不快点回去的话，\x01",
            "就赶不上宿舍的门限时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2P啊，对啊。\x01",
            "你是说过只能陪我们到傍晚。\x02\x03",
            "#007F嗯……\x01",
            "虽然舍不得，不过也没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#1P不介意的话，我们送你回学院吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵，不用了。\x01",
            "这条路我已经走惯了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x419)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1315")

    label("loc_1286")


    ChrTalk(
        0x8,
        (
            "这个时期\x01",
            "前来旅游的客人很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果要在本酒店住宿，\x01",
            "我建议你们\x01",
            "尽早预定好房间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1315")

    Jump("loc_144F")

    label("loc_1318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_144F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D4")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "这里是布朗西酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "本酒店的所有房间\x01",
            "都能够望到大海，\x01",
            "是个观景的好地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "请务必住在我们这里。\x02",
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_13D4")


    ChrTalk(
        0x8,
        (
            "本酒店的所有房间\x01",
            "都能够望到大海，\x01",
            "是个观景的好地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "请务必住在我们这里。\x02",
    )

    CloseMessageWindow()

    label("loc_144F")

    TalkEnd(0x8)
    Return()

    # Function_4_3E5 end

    def Function_5_1453(): pass

    label("Function_5_1453")

    Return()

    # Function_5_1453 end

    def Function_6_1454(): pass

    label("Function_6_1454")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1554")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "#221F哈哈哈～真是绝美的风景。\x02\x03",
            "#220F我非常喜欢！\x01",
            "这房间和作为下任国王的我非常相称。\x02\x03",
            "如果拉旺塔尔赌吧在营业的话，\x01",
            "我就没什么好说的了……\x02\x03",
            "#222F竟然在我来视察的时候改建，\x01",
            "真是岂有此理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D6")

    label("loc_1554")


    ChrTalk(
        0xFE,
        (
            "#220F如果拉旺塔尔赌吧在营业的话，\x01",
            "我就没什么好说的了……\x02\x03",
            "#222F竟然在我来视察的时候改建，\x01",
            "真是岂有此理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D6")

    TalkEnd(0xA)
    Return()

    # Function_6_1454 end

    def Function_7_15DA(): pass

    label("Function_7_15DA")

    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "#720F给小姐你们添了这么多的麻烦。\x01",
            "　\x02\x03",
            "我菲利普绝对不会忘记这份恩情。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_7_15DA end

    def Function_8_163B(): pass

    label("Function_8_163B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "没有让我睡觉的地方啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来只能去请求他们\x01",
            "再搬一张床进来了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_163B end

    def Function_9_169B(): pass

    label("Function_9_169B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "这下我可有睡意了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_169B end

    def Function_10_16C7(): pass

    label("Function_10_16C7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哇，我好高～兴呢㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们可以住在\x01",
            "这么棒的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_16C7 end

    def Function_11_1708(): pass

    label("Function_11_1708")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "虽然屋子很漂亮，\x01",
            "但反而让我平静不下来。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1708 end

    def Function_12_1744(): pass

    label("Function_12_1744")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哎呀，很漂亮的屋子呢。\x01",
            "我好喜欢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "从这边很难看到大海的……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1744 end

    def Function_13_179E(): pass

    label("Function_13_179E")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_183D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1805")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "呼，接下来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "差不多该收拾行李，\x01",
            "准备回柏斯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183A")

    label("loc_1805")


    ChrTalk(
        0xFE,
        (
            "差不多该收拾行李，\x01",
            "准备回柏斯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183A")

    Jump("loc_1891")

    label("loc_183D")


    ChrTalk(
        0xFE,
        (
            "不愧是米拉诺小姐的熟人\x01",
            "经营的酒店啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1891")

    TalkEnd(0x11)
    Return()

    # Function_13_179E end

    def Function_14_1895(): pass

    label("Function_14_1895")

    EventBegin(0x0)
    OP_6D(-2330, 0, 81840, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x102, -1600, 0, 75980, 270)
    SetChrPos(0x101, -1210, 0, 76950, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F#1P哇～好大啊！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFF68C, 0x0, 0x13074, 0x1388, 0x0)

    def lambda_1959():
        OP_8E(0xFE, 0xFFFFF272, 0x0, 0x1375E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1959)
    OP_8E(0x101, 0xFFFFFBE6, 0x0, 0x13C2C, 0x1388, 0x0)
    OP_8E(0x101, 0x5D2, 0x0, 0x14320, 0x1388, 0x0)
    OP_8C(0x101, 90, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 45, 400)
    Sleep(1000)
    ClearMapFlags(0x1)

    def lambda_19D0():
        OP_6D(-13470, 0, 74920, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19D0)

    def lambda_19E8():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19E8)

    def lambda_19F8():
        OP_8E(0xFE, 0xFFFFE660, 0x0, 0x142B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19F8)
    Sleep(500)
    OP_8C(0x102, 315, 400)
    OP_43(0x102, 0x1, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)
    OP_8E(0x101, 0xFFFFD094, 0x0, 0x12AE8, 0x1388, 0x0)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F哦～这边是卧室啊。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F而且还是独立套间。\x02\x03",
            "只需付普通房间的费用，\x01",
            "想起来还真是有点不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F呵呵，难得人家这么提议，\x01",
            "我们好好享受一下也无妨啦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1895 end

    def Function_15_1B49(): pass

    label("Function_15_1B49")

    Sleep(1000)
    OP_8E(0xFE, 0xFFFFE53E, 0x0, 0x13826, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFD616, 0x0, 0x128C2, 0x7D0, 0x0)
    Return()

    # Function_15_1B49 end

    def Function_16_1B77(): pass

    label("Function_16_1B77")

    EventBegin(0x0)
    OP_6D(-13860, 0, 75700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, -12490, 0, 76470, 225)
    SetChrPos(0xB, -11080, 0, 76600, 225)
    SetChrPos(0x101, -6200, 0, 83040, 225)
    SetChrPos(0x102, -5190, 0, 82770, 225)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        (
            "#220F#1P房间够大，家具也不错。\x02\x03",
            "嗯，我很满意。\x01",
            "在卢安逗留期间就住这里好了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "黑衣老人",
        (
            "#722F#4P公爵大人，请您再稍等一下。\x02\x03",
            "这个顶楼房间\x01",
            "已经有其他客人住下了……\x02\x03",
            "不如就按照之前的计划，\x01",
            "在市长大人的官邸下榻可好？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        (
            "#224F#1P闭嘴，菲利普！\x01",
            "难道住在那里能看见海吗？\x02\x03",
            "#225F这间海边酒店风景又好，\x01",
            "又能享受到如此清爽的海风。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0xA, 45, 400)

    def lambda_1DFF():

        label("loc_1DFF")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_1DFF")

    QueueWorkItem2(0xB, 1, lambda_1DFF)

    def lambda_1E10():
        OP_6D(-7270, 0, 83010, 2000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E10)
    OP_8E(0xA, 0xFFFFE2D2, 0x0, 0x13D62, 0xBB8, 0x0)
    WaitChrThread(0xB, 0x2)

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        "#221F#3P而且又可以在露台……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x2)
    OP_44(0xB, 0xFF)
    OP_63(0x101)
    OP_63(0x102)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x1770)
    OP_8F(0xA, 0xFFFFE020, 0x0, 0x13B6E, 0x1388, 0x0)

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        (
            "#226F你、你们是什么人！？\x02\x03",
            "强盗吗！？\x01",
            "想行刺我的强盗吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P你在说些什么\x01",
            "乱七八糟的话啊。\x02\x03",
            "#009F倒是大叔你们是什么人？\x01",
            "为什么擅自闯进我们的房间？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        (
            "#224F不、不许叫我大叔！\x02\x03",
            "#220F哼，算了……\x01",
            "你们就是住这个房间的人吧？\x02\x03",
            "这里已经成为\x01",
            "我在卢安逗留期间的私人房间。\x02\x03",
            "你们赶快给我出去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P啊？我可完全\x01",
            "听不懂你在说什么。\x02\x03",
            "凭什么要我们\x01",
            "把房间让给你啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#2P请给我们一个解释。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        (
            "#225F哼，所以我就说嘛，\x01",
            "无知愚昧的平民最麻烦了……\x02\x03",
            "你们不知道本公爵是谁吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P嗯，完全不知道。\x02\x03",
            "不过怎么看，\x01",
            "都只是个头脑秀逗的大叔。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        "#226F头、头脑秀逗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P艾丝蒂尔……\x01",
            "这样说似乎有点失礼吧。\x02\x03",
            "说他很有个性之类的就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#2P就是就是，还是你最会说话⊙\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "贵族打扮的男子",
        (
            "#222F呜呜呜呜……\x02\x03",
            "#225F哼，算了。\x01",
            "给我竖起耳朵听好了。\x02\x03",
            "#224F……我的名字是\x01",
            "杜南·冯·奥赛雷丝！\x02\x03",
            "利贝尔女王艾莉茜雅Ⅱ世的侄子、\x01",
            "王国现任的公爵！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#225F哼哼哼……\x01",
            "吃惊得说不出话了吧。\x02\x03",
            "总之，现在你们明白\x01",
            "将房间让给本公爵的理由了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#2P噗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#2P哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#2P#5S啊哈哈哈哈哈哈！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#2P大叔，太有趣了！\x01",
            "笑得我肚子好痛哦！\x02\x03",
            "你为什么不说其他，\x01",
            "偏偏说是女王陛下的侄子～！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011F#2P呵呵，艾丝蒂尔。\x01",
            "用不着笑成这个样子吧。\x02\x03",
            "人家也许是为了调节气氛，\x01",
            "才说些笑话让大家轻松一下哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#226F这、这、这两个家伙……\x02",
    )

    CloseMessageWindow()
    OP_8E(0xB, 0xFFFFE16A, 0x0, 0x1372C, 0xBB8, 0x0)

    NpcTalk(
        0xB,
        "黑衣老人",
        (
            "#722F……虽然十分抱歉，\x01",
            "不过公爵大人所说的是事实。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)
    TurnDirection(0x102, 0xB, 400)

    ChrTalk(
        0x101,
        "#004F#2P哎……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "黑衣老人",
        (
            "#720F对不起，还没自我介绍。\x02\x03",
            "我是负责照顾\x01",
            "公爵大人起居生活的管家。\x01",
            "我叫菲利普……\x02\x03",
            "自公爵大人出生以来\x01",
            "我就一直随侍他的左右。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F#2P啊，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#721F我以管家的名誉\x01",
            "对此做出万分的保证。\x02\x03",
            "站在你们面前的这位杜南公爵……\x01",
            "的的确确就是艾莉茜雅女王的侄子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        (
            "#002F#2P（虽、虽然很难让人信服……）\x02\x03",
            "（不过，先不说这个大叔，\x01",
            "　那位管家看样子倒是不会假的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P（说起来，\x01",
            "　嘉恩先生之前也说过……）\x02\x03",
            "（有王族成员\x01",
            "　要来卢安视察……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#221F哇哈哈，知道错了吧！\x02\x03",
            "把房间让给已被定为下任国王的我，\x01",
            "对你们来说，简直是天大的荣誉啊。\x02\x03",
            "要知道，\x01",
            "这种机会可不是随便就能有的哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        (
            "#005F#2P开、开什么玩笑！\x02\x03",
            "就算真的是王族，\x01",
            "像大叔你这样傲慢无礼的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0xFFFFE7F0, 0x0, 0x14050, 0xFA0, 0x0)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "#723F#3P慢着，小姐！\x01",
            "请您等一下可以吗！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)
    TurnDirection(0x102, 0xB, 400)

    ChrTalk(
        0x101,
        "#004F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#720F#3P还请借一步说话……\x02",
    )

    CloseMessageWindow()

    def lambda_2ACE():
        OP_6D(-5790, 0, 84490, 1000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2ACE)

    def lambda_2AE6():

        label("loc_2AE6")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2AE6")

    QueueWorkItem2(0x101, 1, lambda_2AE6)

    def lambda_2AF7():

        label("loc_2AF7")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_2AF7")

    QueueWorkItem2(0x102, 1, lambda_2AF7)
    SetChrFlags(0x101, 0x4)

    def lambda_2B0D():
        OP_8E(0xFE, 0xFFFFE962, 0x0, 0x148AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B0D)

    def lambda_2B28():
        OP_8E(0xFE, 0xFFFFEC14, 0x0, 0x14924, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B28)
    OP_8E(0xB, 0xFFFFEA7A, 0x0, 0x1442E, 0x7D0, 0x0)
    OP_8C(0xB, 0, 400)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(
        0xB,
        (
            "#720F#3P虽然这样说很失礼，\x01",
            "但是我有事想请求两位。\x02\x03",
            "这样能把房间让给我们了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "老管家菲利普\x01",
            "从怀里取出一大叠的米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#004F#1P管、管家先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#2P怎么说也用不着这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#722F#3P公爵大人是那种\x01",
            "一言既出就绝不收回的人……\x02\x03",
            "这一切都是抚养公爵大人长大的\x01",
            "我无德无能所造成的……\x02\x03",
            "求求你们，拜托了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "老管家菲利普低下头，\x01",
            "做出一副准备下跪的姿势。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(
        0x101,
        (
            "#007F#1P哎，没办法了……\x02\x03",
            "其实我们\x01",
            "也不想让管家太为难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P房间就让给你们吧。\x02\x03",
            "不过，这米拉我们不能收。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#721F#3P但、但这样的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P没关系没关系⊙\x02\x03",
            "对我们来说，\x01",
            "这房间本来就太豪华了。\x02\x03",
            "#001F您要照看那位大叔一定很辛苦吧，\x01",
            "不管怎样，要加油哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#722F#3P小、小姐您……\x02\x03",
            "真是太谢谢两位了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFE552, 0x0, 0x14064, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        (
            "#224F喂喂，你们背着我\x01",
            "嘀嘀咕咕地说些什么呀？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FA5():
        OP_8E(0xFE, 0xFFFFEC1E, 0x0, 0x1419A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FA5)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)
    WaitChrThread(0xB, 0x1)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0x101,
        "#006F#1P没～什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P打扰你们了。\x02\x03",
            "房间这就让给公爵大人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F哦哦，是吗！\x02\x03",
            "#221F哇哈哈， \x01",
            "一开始就老老实实这么说不就好了⊙\x02\x03",
            "做人一定要谦虚才行，\x01",
            "你们这些小的千万别忘记这点哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#1P真是受不了他……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#2P那么我们告辞了。\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x8, 0x0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    SetChrPos(0x101, -1830, 0, 9580, 354)
    SetChrPos(0x102, -2920, 0, 9310, 354)
    OP_4A(0x8, 255)
    Sleep(500)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_21()
    OP_1E()
    OP_0D()

    ChrTalk(
        0x8,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "早知如此，我刚才就该出面\x01",
            "向公爵说明情况并断然拒绝他的要求……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真是十分抱歉。\x01",
            "事情变成现在这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没事没事。\x02\x03",
            "全都是那个\x01",
            "任性的公爵不好嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了……\x01",
            "请问你们还有其他的房间吗？\x02\x03",
            "普通房间就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就在刚才，\x01",
            "所有的房间都住满了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F我们倒是没考虑到这一点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请二位放心。\x01",
            "这次的事都是因为我处理不当引起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我会负起全责，\x01",
            "为二位在其他地方安排住宿……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2230, 0, 3110, 0)

    NpcTalk(
        0x9,
        "男人的声音",
        "#1P哟，是不是碰到麻烦了啊？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3480():
        OP_6D(-2200, 0, 9820, 1200)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3480)

    def lambda_3498():
        OP_8E(0xFE, 0xFFFFF66E, 0x0, 0x1D42, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3498)
    OP_8C(0x101, 225, 400)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x9,
        (
            "#141F#4P艾丝蒂尔、约修亚。\x01",
            "空贼基地一别之后好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P啊，奈尔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P晚上好。\x01",
            "真没想到会在这里见到您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F#4P这句话该我说才是。\x02\x03",
            "我也没想到\x01",
            "你们俩也到卢安来了。\x02\x03",
            "先不说这个，怎么了？\x01",
            "是不是遇到了什么麻烦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#2P其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔说明了刚才发生的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "#147F#4P哈哈哈！\x02\x03",
            "你们还是老样子，\x01",
            "又碰到了一些有趣的事情！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#2P我说啊……\x01",
            "这没什么好笑的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F#4P这事好办。\x01",
            "你们就和我住一个房间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#2P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F#4P我房间正好有空着的床位。\x02\x03",
            "哟，主管先生。\x01",
            "我们一起住也没关系吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当然了。\x01",
            "您可是帮了大忙啊。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F#4P好，那就这么定了。\x02\x03",
            "地下一层最里面的房间。\x01",
            "不必客气，尽管跟着来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_8E(0x9, 0xFFFFF83A, 0x0, 0x15AE, 0xBB8, 0x1)
    OP_8E(0x9, 0x8B6, 0x0, 0x816, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F#2P啊，这样好吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#1P难得他这样提议，\x01",
            "我们就照他说的办吧。\x02\x03",
            "不过，作为收留我们的条件，\x01",
            "多半会向我们挖点什么新闻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P嗯……\x01",
            "的确很有这种可能。\x02\x03",
            "#006F不过，这点小事也无所谓啦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_16_1B77 end

    def Function_17_3970(): pass

    label("Function_17_3970")

    EventBegin(0x0)
    OP_6D(-43860, 0, 53790, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(1236, 0)
    OP_6C(72000, 0)
    OP_6E(627, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0x9, 5)
    SetChrSubChip(0x9, 1)
    SetChrPos(0x9, -47650, 200, 55350, 197)
    SetChrPos(0x101, -43080, 0, 53380, 290)
    SetChrPos(0x102, -42750, -200, 52630, 296)
    OP_6F(0x7, 30)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#141F哦，来了啊。\x02\x03",
            "这些空着的床\x01",
            "你们就随便用吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x7, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x7, 0x0)
    OP_66(0x0)

    def lambda_3A80():
        OP_6D(-46290, 0, 55390, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A80)

    def lambda_3A98():
        OP_6B(1100, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A98)

    def lambda_3AA8():
        OP_8E(0xFE, 0xFFFF42FA, 0x0, 0xD20A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AA8)
    Sleep(500)

    def lambda_3AC8():
        OP_8E(0xFE, 0xFFFF46E2, 0x0, 0xD070, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AC8)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x9, 0)

    def lambda_3AED():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AED)
    WaitChrThread(0x102, 0x1)

    def lambda_3B00():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B00)

    ChrTalk(
        0x101,
        (
            "#006F虽然很感谢\x01",
            "你能收留我们……\x02\x03",
            "不过这样做好像也\x01",
            "服务得太过周到了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#143F#1P哦？\x01",
            "你在瞎猜什么呀？\x02\x03",
            "先前都是多亏了你们，\x01",
            "我才能写出那么爆炸性的报道。\x02\x03",
            "只是表示一点感谢啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是空贼逮捕的特讯吧。\x02\x03",
            "反响如何呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F#1P那还用说，简直卖疯了！\x02\x03",
            "而且，关于理查德上校和\x01",
            "情报部活动的新闻尤为反响热烈。\x02\x03",
            "可以说，上校的新闻\x01",
            "简直比空贼事件本身还有看头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F是吗……\x01",
            "那个人那么受欢迎吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F#1P据说因为这次事件的解决，\x01",
            "他甚至得到了陛下颁发的勋章。\x02\x03",
            "在王都一带的市民心中，\x01",
            "他的人气可是直线上升啊。\x02\x03",
            "下次我们也准备刊登\x01",
            "理查德上校的独家专访。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F那真是厉害啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F#1P无论从他的外表，还是他的举止，\x01",
            "都能给人一种沉稳而又可靠的感觉。\x02\x03",
            "之前我也跟他聊了聊，\x01",
            "觉得他确实是个很有气质的人。\x02\x03",
            "#145F只是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F只是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F#1P没什么……\x01",
            "算了，无所谓啦。\x02\x03",
            "#147F托这次报道的福，奖金也领到了，\x01",
            "监护人的工作也总算熬到头了。\x02\x03",
            "多亏了理查德上校啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F『监护人的工作熬到头了』，\x01",
            "难道你是指朵洛希吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F说起来……\x01",
            "她没和你在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F#1P本来就是带新人实习的性质，\x01",
            "让她在社会上多吸收一下实践经验。\x02\x03",
            "完成这次特讯之后，\x01",
            "当然就是可喜可贺地解除合作关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x02\x03",
            "#506F不过……\x01",
            "她一个人单独行动才更叫人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F#1P别提了……\x01",
            "我已经尽量不去多想她的事了。\x02\x03",
            "#141F总之，正因为这样，\x01",
            "我现在可以花自己的奖金，\x01",
            "逍遥快活地享受属于自己的假期。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F说得倒是好听，\x01",
            "反正肯定又是在追什么新闻吧。\x02\x03",
            "#006F啊，难道说……\x01",
            "是在为了那个公爵吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F#1P啊，杜南公爵吗。\x01",
            "你们还真是倒霉啊。\x02\x03",
            "据我所知，他在王族当中\x01",
            "是以胡作非为举止出格而出名的。\x02\x03",
            "听说艾莉茜雅女王\x01",
            "也经常为这个公爵大伤脑筋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这话听起来倒是满有可信度的。\x02\x03",
            "不过，照他本人说，\x01",
            "他会是利贝尔的下任国王……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F哎～那是真的吗？\x02\x03",
            "我可不想叫那种大叔\x01",
            "『国王陛下』哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F#1P这个嘛，陛下年事已高了，\x01",
            "他的确是继承王位的有力竞争者。\x02\x03",
            "毕竟陛下的儿子\x01",
            "很久以前就已经去世了。\x02\x03",
            "不过，周围的反对呼声也不少啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来奈尔先生\x01",
            "所知道的也不是很多啊。\x02\x03",
            "也就是说……\x01",
            "你在调查的是其它的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#143F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，看来被说中了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F#1P真是的……\x01",
            "你这小子还是那么敏锐啊。\x02\x03",
            "#141F我承认是有别的事。\x01",
            "不过只能到此为止，不能再多说什么了。\x02\x03",
            "因为这是条相～当大的新闻哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F你这么一说，\x01",
            "反而惹得我们更想知道了……\x02\x03",
            "不过算了。\x01",
            "反正我们又不是媒体的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就期待着您的报道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#147F#1P没问题，包在我身上。\x02\x03",
            "#141F对了，\x01",
            "你们还没吃晚饭吧？\x02\x03",
            "一块儿去吧，我请客。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F哎？真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就不客气了。\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当晚，由奈尔请客，\x01",
            "艾丝蒂尔和约修亚他们\x01",
            "在拉旺塔尔赌吧吃了一顿晚餐。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在品尝了各种各样\x01",
            "亚瑟利亚湾的海鲜菜肴之后……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们将醉倒的\x01",
            "奈尔抬回布朗西酒店，\x01",
            "然后就各自就寝了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2403   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3970 end

    def Function_18_4825(): pass

    label("Function_18_4825")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EC")
    OP_A2(0x3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4848")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_484F")

    label("loc_4848")

    TurnDirection(0x102, 0x0, 400)

    label("loc_484F")


    ChrTalk(
        0x102,
        (
            "#010F赶快去奈尔先生的房间吧。\x02\x03",
            "他这么热情招待我们，\x01",
            "再让他等着就太没礼貌了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F他说的房间\x01",
            "是在地下一层里面吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4953")

    label("loc_48EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4902")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_4909")

    label("loc_4902")

    TurnDirection(0x102, 0x0, 400)

    label("loc_4909")


    ChrTalk(
        0x102,
        (
            "#010F赶快去奈尔先生的房间吧。\x02\x03",
            "是在地下一层里面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4953")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_4825 end

    SaveToFile()

Try(main)
