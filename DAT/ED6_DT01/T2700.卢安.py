from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2700   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2700   ._SN',
            'ED6_DT01/T2700_1 ._SN',
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
        '哈恩队长',                             # 9
        '管家菲利普',                           # 10
        '尤莉亚中尉',                           # 11
        '基库',                                 # 12
        '目标用摄像机',                         # 13
        '卡露娜',                               # 14
        '士兵尼克斯',                           # 15
        '士兵威尔斯',                           # 16
        '梅尔凯斯',                             # 17
        '阿伊纳街道',                           # 18
        '卡鲁迪亚隧道',                         # 19
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH02470 ._CH',             # 01
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT07/CH02090 ._CH',             # 05
        'ED6_DT07/CH02323 ._CH',             # 06
        'ED6_DT06/CH20059 ._CH',             # 07
        'ED6_DT06/CH20113 ._CH',             # 08
        'ED6_DT07/CH01220 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH02470P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT07/CH02090P._CP',             # 05
        'ED6_DT07/CH02323P._CP',             # 06
        'ED6_DT06/CH20059P._CP',             # 07
        'ED6_DT06/CH20113P._CP',             # 08
        'ED6_DT07/CH01220P._CP',             # 09
    )

    DeclNpc(
        X                   = 5500,
        Z                   = 5000,
        Y                   = 0,
        Direction           = 270,
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
        X                   = 4500,
        Z                   = 5000,
        Y                   = 0,
        Direction           = 90,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        NpcIndex            = 0x1C5,
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
        X                   = -15300,
        Z                   = 100,
        Y                   = -11300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 18400,
        Z                   = 5000,
        Y                   = 1400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -19800,
        Z                   = 0,
        Y                   = -2200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4710,
        Z                   = 5000,
        Y                   = 2490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -62340,
        Z                   = 0,
        Y                   = -1100,
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

    DeclNpc(
        X                   = 21320,
        Z                   = 5000,
        Y                   = 460,
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
        TriggerX            = 19830,
        TriggerZ            = 5000,
        TriggerY            = -50,
        TriggerRange        = 800,
        ActorX              = 19830,
        ActorZ              = 6000,
        ActorY              = -50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -45890,
        TriggerZ            = 0,
        TriggerY            = 2240,
        TriggerRange        = 1500,
        ActorX              = -45890,
        ActorZ              = 1700,
        ActorY              = 2240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A2",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_3D7",          # 02, 2
        "Function_3_3ED",          # 03, 3
        "Function_4_411",          # 04, 4
        "Function_5_685",          # 05, 5
        "Function_6_6E8",          # 06, 6
        "Function_7_101C",         # 07, 7
        "Function_8_1255",         # 08, 8
        "Function_9_12A5",         # 09, 9
        "Function_10_173E",        # 0A, 10
        "Function_11_2C3D",        # 0B, 11
        "Function_12_2C65",        # 0C, 12
        "Function_13_2CB9",        # 0D, 13
        "Function_14_2D1A",        # 0E, 14
    )


    def Function_0_2A2(): pass

    label("Function_0_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2AC")
    Jump("loc_2C8")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2BB")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2C8")

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    ClearChrFlags(0x10, 0x80)

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E3")
    SetChrFlags(0x8, 0x80)

    label("loc_2E3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_2F3"),
        (100, "loc_32A"),
        (SWITCH_DEFAULT, "loc_346"),
    )


    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_314")
    OP_28(0x23, 0x1, 0x1)
    Event(1, 0)

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_327")
    OP_A2(0x503)
    Event(0, 10)

    label("loc_327")

    Jump("loc_346")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_340")
    OP_A2(0x501)
    Event(0, 9)
    Jump("loc_343")

    label("loc_340")

    OP_A2(0x53C)

    label("loc_343")

    Jump("loc_346")

    label("loc_346")

    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_2A2 end

    def Function_1_358(): pass

    label("Function_1_358")

    OP_16(0x2, 0xFA0, 0xFFFDC5B0, 0xFFFE0C00, 0x3004F)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382")
    OP_72(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_395")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_END)), "loc_395")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 160)

    label("loc_395")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9")
    OP_28(0x2A, 0x1, 0x2000)

    label("loc_3A9")

    OP_1C(0x1, 0x0, 0xE)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C6"),
        (101, "loc_3C6"),
        (102, "loc_3CE"),
        (103, "loc_3CE"),
        (SWITCH_DEFAULT, "loc_3D6"),
    )


    label("loc_3C6")

    OP_22(0x1CE, 0x1, 0x64)
    Jump("loc_3D6")

    label("loc_3CE")

    OP_22(0x1CA, 0x1, 0x64)
    Jump("loc_3D6")

    label("loc_3D6")

    Return()

    # Function_1_358 end

    def Function_2_3D7(): pass

    label("Function_2_3D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3D7")

    label("loc_3EC")

    Return()

    # Function_2_3D7 end

    def Function_3_3ED(): pass

    label("Function_3_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_410")
    OP_8D(0xFE, 13000, 2500, 1500, 0, 1500)
    Jump("Function_3_3ED")

    label("loc_410")

    Return()

    # Function_3_3ED end

    def Function_4_411(): pass

    label("Function_4_411")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_681")

    ChrTalk(
        0xFE,
        "已经有空了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果可以的话，\x01",
            "能请你们帮帮忙吗？\x02",
        )
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
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D9"),
        (1, "loc_571"),
        (SWITCH_DEFAULT, "loc_681"),
    )


    label("loc_4D9")

    OP_28(0x23, 0x4, 0x8)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "谢谢了，真是帮大忙了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么就先到楼下去，\x01",
            "我把详细的情况告诉你们。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    NewScene("ED6_DT01/T2710   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_681")

    label("loc_571")

    OP_28(0x23, 0x1, 0x4000)

    ChrTalk(
        0x101,
        (
            "#003F抱歉，\x01",
            "现在大概不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那还真是麻烦啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那我们唯有\x01",
            "先靠自己去说服他吧，\x01",
            "虽然知道自己对这种事不是很擅长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "等办完事情，\x01",
            "就请尽快过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 0)
    Jump("loc_681")

    label("loc_681")

    TalkEnd(0x8)
    Return()

    # Function_4_411 end

    def Function_5_685(): pass

    label("Function_5_685")

    TalkBegin(0xD)

    ChrTalk(
        0xFE,
        "呼，总算是完成了任务。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里虽然很凉爽，\x01",
            "但要一直站岗就很辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_5_685 end

    def Function_6_6E8(): pass

    label("Function_6_6E8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79C")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哟，是旅行者啊，\x01",
            "还真是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在大家都去王都的时候，\x01",
            "你们却要到卢安去观光游览吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "这也许另有一番趣味呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A3")

    label("loc_79C")


    ChrTalk(
        0xFE,
        (
            "仔细想想，\x01",
            "在观光的时候如果周围的人很少，\x01",
            "行动不就更加自由了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里既有名胜古迹，\x01",
            "又有便宜旅店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，话又说回来，\x01",
            "诞辰庆典只有现在这个时间才有哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔唔，苦恼啊。\x02",
    )

    CloseMessageWindow()

    label("loc_8A3")

    Jump("loc_1018")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_98E")

    ChrTalk(
        0xFE,
        (
            "呼，这么快就解除了对旅客的盘查，\x01",
            "真是出乎预料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又要回复到\x01",
            "以往的警戒状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然不知道具体原因，\x01",
            "但应该是抓住犯人了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1018")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A21")

    ChrTalk(
        0xFE,
        "……现在关所正处于戒严状态。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "抱歉，\x01",
            "值勤期间禁止窃窃私语。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1018")

    label("loc_A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我们关所\x01",
            "也收到了联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨日，\x01",
            "蔡斯的所有导力器\x01",
            "一下子都不能使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果相同的情况\x01",
            "在卢安也发生的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "伦格兰德大桥就会\x01",
            "一直打开而不能合上了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB6")

    label("loc_B1D")


    ChrTalk(
        0xFE,
        (
            "中央工房\x01",
            "制作出了许多奇怪的东西。\x01",
            "它是个很大的建筑物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个造成导力停止的东西\x01",
            "究竟是怎么制造出来的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB6")

    Jump("loc_1018")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C7D")

    ChrTalk(
        0xFE,
        (
            "过了这门，\x01",
            "再往前走就是蔡斯地区了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里面的卡鲁迪亚隧道\x01",
            "和外面很不一样哦………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我能保证，对任何旅行者来说，\x01",
            "这都会是一次非常新奇的旅程。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1018")

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_D41")

    ChrTalk(
        0xFE,
        (
            "过了这门，\x01",
            "再往前走就是蔡斯地区了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里面的卡鲁迪亚隧道\x01",
            "和外面很不一样哦………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我能保证，对任何旅行者来说，\x01",
            "这都会是一次非常新奇的旅程。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1018")

    label("loc_D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_F9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "队长和副长都在\x01",
            "拼命写刚才的报告书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我听说过公爵的传言，\x01",
            "不过没想到会这么糟糕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天由我来站岗\x01",
            "真是太幸运了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEB")

    label("loc_E4F")


    ChrTalk(
        0xFE,
        (
            "虽然我听说过公爵的传言，\x01",
            "不过没想到会这么糟糕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天由我来站岗\x01",
            "真是太幸运了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEB")

    Jump("loc_F9B")

    label("loc_EEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_F4B")

    ChrTalk(
        0xFE,
        (
            "好像有个蛮不讲理的人\x01",
            "到关所来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9B")

    label("loc_F4B")


    ChrTalk(
        0xFE,
        (
            "好像有个蛮不讲理的人\x01",
            "到关所来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9B")

    Jump("loc_1018")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1018")

    ChrTalk(
        0xFE,
        (
            "在这里站岗可以欣赏美丽的景色，\x01",
            "空气也很清新，真是一份好差事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过到了冬天就辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_1018")

    TalkEnd(0xE)
    Return()

    # Function_6_6E8 end

    def Function_7_101C(): pass

    label("Function_7_101C")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_10A3")

    ChrTalk(
        0xFE,
        (
            "哟，欢迎你们来到\x01",
            "『艾尔·雷登』关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要办通行手续的话，\x01",
            "请到里面的柜台。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1251")

    label("loc_10A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_11DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1133")

    ChrTalk(
        0xFE,
        (
            "有个看上去挺有钱的大叔\x01",
            "一边抱怨一边走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DC")

    label("loc_1133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_118E")

    ChrTalk(
        0xFE,
        (
            "从刚才开始\x01",
            "里面就很吵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不知道发生什么事了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DC")

    label("loc_118E")


    ChrTalk(
        0xFE,
        (
            "从刚才开始\x01",
            "里面就很吵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不知道发生什么事了。\x02",
    )

    CloseMessageWindow()

    label("loc_11DC")

    Jump("loc_1251")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1251")

    ChrTalk(
        0xFE,
        (
            "刚才从雷斯顿要塞\x01",
            "有命令传达了过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是什么样的命令呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1251")

    TalkEnd(0xF)
    Return()

    # Function_7_101C end

    def Function_8_1255(): pass

    label("Function_8_1255")

    TalkBegin(0x10)

    ChrTalk(
        0xFE,
        (
            "在遗迹这样的地方还会有瀑布，\x01",
            "真是罕见啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_8_1255 end

    def Function_9_12A5(): pass

    label("Function_9_12A5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(5900, 12000, 13400, 0)
    OP_6C(85000, 0)
    OP_6B(8000, 0)
    StopSound(0x7D00, 0x3D090, 0x0)
    SetChrPos(0x101, -51400, 0, -1100, 90)
    SetChrPos(0x102, -52500, 0, -300, 90)
    SetChrPos(0x105, -52500, 0, -2100, 90)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x2EE0)

    def lambda_132B():
        OP_6B(2800, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_132B)

    def lambda_133B():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_133B)
    Sleep(3000)

    def lambda_1350():
        OP_6D(-50000, 0, -1500, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1350)
    Sleep(9000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FD")

    ChrTalk(
        0x101,
        (
            "#501F#2P哎……\x01",
            "这里的气氛真好啊。\x02\x03",
            "与其说是关所，倒不如说是观光胜地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149D")

    label("loc_13FD")


    ChrTalk(
        0x101,
        (
            "#501F#2P之前也来过这里……\x01",
            "这里的气氛真好啊。\x02\x03",
            "与其说是关所，倒不如说是观光胜地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149D")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F其实，每年慕名前来\x01",
            "观赏瀑布的观光客也不少呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14FC():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14FC)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#006F#2P啊，是这样吗？\x02\x03",
            "嗯～～\x01",
            "卢安地区的风景名胜还真不少呢。\x02\x03",
            "如果不是因为那个公爵捣乱的话，\x01",
            "我也真想在这住一段时间啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F呵呵，说得也是。\x02\x03",
            "#048F不过，我觉得洛连特\x01",
            "也是个宁静得让人舒心的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P啊，这样说……\x01",
            "科洛丝也去过洛连特吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F是的，\x01",
            "五大都市我全部都去过呢。\x02\x03",
            "#040F对了，\x01",
            "过了这里就是蔡斯市……\x02\x03",
            "那是一个非常著名的城市，\x01",
            "我想你们到了那里一定会大吃一惊的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2P哎～是吗？\x02\x03",
            "#001F嗯……\x01",
            "开始有点期待了～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F好了，\x01",
            "我们这就进去办理通行手续吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F#2P嗯，ＯＫ。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_9_12A5 end

    def Function_10_173E(): pass

    label("Function_10_173E")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-5200, 5000, 7200, 0)
    SetChrPos(0x101, -5000, 5000, 6600, 90)
    SetChrPos(0x105, -6300, 5000, 7100, 90)
    SetChrPos(0x102, -6300, 5000, 5800, 90)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 160)
    FadeToBright(1000, 0)

    def lambda_17AE():
        OP_6B(5000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17AE)

    def lambda_17BE():
        OP_6D(10900, 9200, 14500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17BE)

    def lambda_17D6():
        OP_6C(24000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17D6)
    Sleep(5000)
    SetChrPos(0xB, 10300, 6400, 3150, 0)
    SetChrPos(0xA, 900, 5000, 800, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 8300, 5000, 2500, 0)
    SetChrPos(0x105, 6800, 5000, 2500, 0)
    SetChrPos(0x102, 7700, 5000, 1000, 0)

    ChrTalk(
        0x101,
        "#001F#1P呜哇～好壮观啊！\x02",
    )

    CloseMessageWindow()

    def lambda_186A():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_186A)

    def lambda_187A():
        OP_6D(7800, 5000, 2500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_187A)
    Sleep(5000)

    ChrTalk(
        0x101,
        (
            "#501F#4P嗯～虽说是瀑布，\x01",
            "但却不是自然的河流，\x01",
            "而是从水道流下而形成的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P我记得这条水道\x01",
            "好像是叫『罗蔡水道』吧？\x02\x03",
            "是在中世纪建造的水道桥。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#040F#3P是的，这里的水可是从\x01",
            "瓦雷利亚湖直接流过来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#4P呼，在没有导力器的情况下，\x01",
            "竟然也能完成这么大的工程啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#006F#3P那么，那边的是……\x02",
    )

    CloseMessageWindow()

    def lambda_1A0E():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A0E)

    def lambda_1A1E():
        OP_6D(17680, 5000, -70, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A1E)

    def lambda_1A36():
        OP_6B(4250, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A36)

    def lambda_1A46():
        OP_67(0, 3980, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A46)

    def lambda_1A5E():
        OP_6E(345, 4000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_1A5E)

    def lambda_1A6E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A6E)

    def lambda_1A7C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A7C)
    OP_8C(0x105, 90, 400)

    def lambda_1A91():
        OP_8E(0xFE, 0x2C88, 0x1388, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A91)
    Sleep(800)

    def lambda_1AB1():
        OP_8E(0xFE, 0x2A94, 0x1388, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AB1)
    Sleep(300)

    def lambda_1AD1():
        OP_8E(0xFE, 0x2648, 0x1388, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1AD1)
    WaitChrThread(0x101, 0x2)
    OP_8C(0x101, 90, 0)
    WaitChrThread(0x102, 0x2)
    OP_8C(0x102, 90, 0)
    WaitChrThread(0x105, 0x2)
    OP_8C(0x105, 90, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#010F……看来那边就是卡鲁迪亚隧道的入口了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    Fade(1000)
    TurnDirection(0x102, 0x105, 0)
    TurnDirection(0x101, 0x105, 0)
    TurnDirection(0x105, 0x101, 0)
    OP_8C(0xB, 180, 0)
    OP_6D(11300, 5000, 540, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_21()
    OP_1D(0x58)

    ChrTalk(
        0x101,
        "#505F……差不多要告别了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F是啊……\x02\x03",
            "#040F对了，艾丝蒂尔你们\x01",
            "打算巡游整个王国一周吧？\x02\x03",
            "说不定到了王都，\x01",
            "我们还有机会再见面哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦，真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F嗯，因为我打算在\x01",
            "女王诞辰庆典举行的时候回王都。\x02\x03",
            "也算是家里的亲戚聚会吧，\x01",
            "不得不出席的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F距离女王诞辰庆典，\x01",
            "大概还有一个月吧。\x02\x03",
            "确实，\x01",
            "那时候我们也差不多该到王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，那么……\x02\x03",
            "亲戚那里的事办完之后，\x01",
            "一定要和王都的协会联络一下哦。\x02\x03",
            "那样应该就能再见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F嗯，我一定会联络的。\x02\x03",
            "#048F艾丝蒂尔、约修亚。\x02\x03",
            "实在是太感谢你们了。\x02\x03",
            "你们俩为大家所做的一切，\x01",
            "我科洛丝，绝对不会忘记的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F真、真是的～\x01",
            "你又跟我们客气起来了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F应该是我们说谢谢才对，\x01",
            "这段时间承蒙你多方照顾了。\x02\x03",
            "算是彼此彼此吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#542F哪里的话……\x02\x03",
            "…………………………\x02\x03",
            "#049F那个时候……和市长对决时……\x02\x03",
            "我说了一些自以为是的话……\x02\x03",
            "『你终究还是只在乎你自己』……\x01",
            "『真是可怜的人』什么的。\x02\x03",
            "但是……\x01",
            "我自己不也是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F那句话就是我内心的写照，\x01",
            "一直不断逃避自己的立场的写照。\x02\x03",
            "孤儿院也好，学院也好，\x01",
            "都只不过是我逃避的场所而已。\x02\x03",
            "#040F但是……\x01",
            "艾丝蒂尔你们\x01",
            "教会了我一样很重要的东西……\x02\x03",
            "无论何时\x01",
            "都要勇往直前的那份决心……\x02\x03",
            "还有，守护身边的人的那份坚强……\x02\x03",
            "#041F谢谢，多亏了你们，\x01",
            "我现在总算也有些勇气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F虽、虽然不是很明白……\x02\x03",
            "能给你帮上忙，\x01",
            "我们两个也会感到很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2171():

        label("loc_2171")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2171")

    QueueWorkItem2(0x105, 3, lambda_2171)
    OP_92(0x101, 0x105, 0x258, 0x7D0, 0x0)
    Fade(500)
    SetChrPos(0x105, 10000, 5000, 640, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x1)
    SetChrChipByIndex(0x105, 7)
    SetChrSubChip(0x105, 1)
    OP_0D()

    ChrTalk(
        0x105,
        "#540F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F#2P嘿嘿……\x01",
            "保重啦，科洛丝。\x02\x03",
            "#508F下次王都见吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F嗯……一定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#310F啾～啾～\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x105, 9800, 5000, 700, 90)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x1)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0x7D0, 0x0)
    TurnDirection(0x101, 0xB, 400)
    OP_44(0x105, 0xFF)
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#001F#2P啊哈，\x01",
            "基库也会一起到王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#311F啾～☆\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F#2P……哎，我说你\x01",
            "不会真的打算到王都来吧？\x02\x03",
            "科洛丝不是说过\x01",
            "你习惯住在这附近的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#310F啾？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F呵呵……\x01",
            "基库可是很特别的哦。\x02\x03",
            "我想一定会再见的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#2P嗯……\x01",
            "其实我只是想开个玩笑啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F哈哈，\x01",
            "到最后还被基库吓了一跳。\x02\x03",
            "#010F那么……\x01",
            "我们差不多该出发了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F#2P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    OP_8C(0x105, 90, 400)

    ChrTalk(
        0x105,
        (
            "#040F艾丝蒂尔、约修亚。\x02\x03",
            "修行之旅，要继续加油啊！\x02\x03",
            "还有的是……\x01",
            "祝愿你们早日找到卡西乌斯先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#311F啾～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#2P嗯……谢谢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，保重了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 0)

    def lambda_256C():
        OP_6D(14900, 5000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_256C)

    def lambda_2584():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2584)

    def lambda_2592():
        OP_8F(0xFE, 0x5EEC, 0x1388, 0xFFFFFED4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2592)
    Sleep(200)

    def lambda_25B2():
        OP_8F(0xFE, 0x4F4C, 0x1388, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25B2)
    Sleep(500)

    def lambda_25D2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25D2)

    def lambda_25E0():
        OP_8F(0xFE, 0x5EEC, 0x1388, 0x12C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25E0)
    Sleep(3500)
    OP_72(0x2, 0x800)
    OP_22(0xDF, 0x0, 0x64)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_71(0x2, 0x800)
    OP_6D(11300, 5000, 540, 1500)

    ChrTalk(
        0x105,
        "#049F#2P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#310F啾。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(
        0x105,
        (
            "#542F#2P嗯，是啊……\x02\x03",
            "一定，还能再见的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    OP_20(0x5DC)

    NpcTalk(
        0xA,
        "女性的声音",
        (
            "#2P——科洛丝。\x01",
            "让你久等了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0xB, 0xFF)

    def lambda_26E9():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26E9)

    def lambda_26F7():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26F7)

    def lambda_2705():
        OP_8E(0xFE, 0x19C8, 0x1388, 0x320, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2705)
    OP_6D(8800, 5000, 680, 2000)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0x105,
        (
            "#040F……尤莉亚。\x02\x03",
            "你不是要从雷斯顿要塞回去的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#170F啊啊，\x01",
            "我从行程里抽出了一点时间。\x02\x03",
            "#170F关于那件事，\x01",
            "还有一些情况要回王都汇报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F谢谢，辛苦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#311F啾～⊙\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    TurnDirection(0xA, 0xB, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_286E():
        OP_8E(0xFE, 0x17E8, 0x157C, 0x596, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_286E)
    Sleep(300)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0xA, 0x17E8, 0x1388, 0x1D6, 0x7D0, 0x0)
    WaitChrThread(0xB, 0x1)
    OP_43(0xB, 0x1, 0x0, 0xB)
    OP_A2(0x2)
    Sleep(500)
    OP_8C(0xA, 315, 300)

    def lambda_28CF():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_28CF)

    ChrTalk(
        0xA,
        (
            "#174F#4P喂、喂，基库，\x01",
            "不要这样胡闹啦。\x02\x03",
            "你啊，\x01",
            "有没有好好坚守护卫任务啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A5(0x2)
    OP_97(0xB, 0x17E8, 0x1D6, 0xFFFD40E0, 0x1770, 0x1)
    OP_97(0xB, 0x17E8, 0x1D6, 0xFFFD40E0, 0xFA0, 0x1)
    OP_97(0xB, 0x17E8, 0x1D6, 0xFFFF5038, 0x7D0, 0x1)
    SetChrFlags(0xB, 0x20)

    def lambda_2982():

        label("loc_2982")

        OP_99(0xFE, 0x0, 0x7, 0x1388)
        OP_48()
        Jump("loc_2982")

    QueueWorkItem2(0xB, 2, lambda_2982)

    def lambda_2995():
        OP_8F(0xFE, 0x16DA, 0x1450, 0x334, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2995)
    OP_8C(0xB, 180, 200)
    WaitChrThread(0xB, 0x1)
    OP_44(0xB, 0x2)
    Fade(500)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 8)
    SetChrSubChip(0xA, 0)
    OP_0D()

    ChrTalk(
        0xB,
        "#310F啾啾☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F呵呵……\x01",
            "我可是经常给基库添麻烦呢。\x02\x03",
            "是吧，基库？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#311F啾～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#176F#4P真是个得意忘形的家伙。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)
    Sleep(400)

    ChrTalk(
        0xA,
        (
            "#170F……科洛丝，\x01",
            "『埃尔赛尤号』就停在大道外面。\x02\x03",
            "到飞艇上再详细说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F我明白了。\x02\x03",
            "#049F……校园生活\x01",
            "也要暂时告一段落了啊。\x02\x03",
            "在回王都之前，\x01",
            "还是和老师他们打声招呼吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B5E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B5E)
    OP_6D(14900, 5000, 0, 1800)

    ChrTalk(
        0x105,
        (
            "#040F（艾丝蒂尔、约修亚。）\x02\x03",
            "（为了不输给你们两个……\x01",
            "　我今后一定会拼命努力的。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(2000, 0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R3400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_173E end

    def Function_11_2C3D(): pass

    label("Function_11_2C3D")

    OP_A6(0x2)

    label("loc_2C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C61")
    OP_97(0xFE, 0x17E8, 0x1D6, 0xFFFA81C0, 0x1F40, 0x1)
    OP_48()
    Jump("loc_2C40")

    label("loc_2C61")

    OP_A3(0x2)
    Return()

    # Function_11_2C3D end

    def Function_12_2C65(): pass

    label("Function_12_2C65")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧地关着，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_2C65 end

    def Function_13_2CB9(): pass

    label("Function_13_2CB9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　卢安市　１７５赛尔矩\x01",
            "东　蔡斯市　４４８赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_2CB9 end

    def Function_14_2D1A(): pass

    label("Function_14_2D1A")

    TalkBegin(0xFF)
    Sleep(200)
    TalkEnd(0xFF)
    Return()

    # Function_14_2D1A end

    SaveToFile()

Try(main)
