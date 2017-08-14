from ED6ScenarioHelper import *

def main():
    # 洛连特飞艇坪

    CreateScenaFile(
        FileName            = 'T0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0700.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60010",
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
        '斯库拉特',                             # 9
        '法布利',                               # 10
        '雪拉扎德',                             # 11
        '卡西乌斯',                             # 12
        '阿兰',                                 # 13
        '奥维德',                               # 14
        '目标用摄像机',                         # 15
        '洛连特市街道',                         # 16
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 9,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 9,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01450 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH02000 ._CH',             # 02
        'ED6_DT07/CH01290 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01450P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH02000P._CP',             # 02
        'ED6_DT07/CH01290P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
    )

    DeclNpc(
        X                   = 45064,
        Z                   = 4200,
        Y                   = 30855,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 31837,
        Z                   = 0,
        Y                   = 51534,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 43018,
        Z                   = 4000,
        Y                   = 33475,
        Direction           = 205,
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
        X                   = 42909,
        Z                   = 4000,
        Y                   = 30908,
        Direction           = 282,
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
        X                   = 36095,
        Z                   = 0,
        Y                   = 35619,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 38020,
        Z                   = 0,
        Y                   = 28750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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

    DeclNpc(
        X                   = 35320,
        Z                   = 0,
        Y                   = -13920,
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
        TriggerX            = 38000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 38000,
        ActorZ              = 2200,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 4000,
        TriggerY            = 41300,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 5500,
        ActorY              = 41800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34500,
        TriggerZ            = 0,
        TriggerY            = 46570,
        TriggerRange        = 800,
        ActorX              = 35000,
        ActorZ              = 1500,
        ActorY              = 46570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36142,
        TriggerZ            = 0,
        TriggerY            = 34342,
        TriggerRange        = 1000,
        ActorX              = 36095,
        ActorZ              = 1500,
        ActorY              = 35619,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A6",          # 00, 0
        "Function_1_390",          # 01, 1
        "Function_2_41D",          # 02, 2
        "Function_3_433",          # 03, 3
        "Function_4_457",          # 04, 4
        "Function_5_506",          # 05, 5
        "Function_6_5A4",          # 06, 6
        "Function_7_621",          # 07, 7
        "Function_8_1549",         # 08, 8
        "Function_9_1DB7",         # 09, 9
        "Function_10_1DBC",        # 0A, 10
        "Function_11_3C2E",        # 0B, 11
        "Function_12_4F6A",        # 0C, 12
        "Function_13_4F7F",        # 0D, 13
        "Function_14_4F94",        # 0E, 14
        "Function_15_4FCF",        # 0F, 15
        "Function_16_5013",        # 10, 16
        "Function_17_5062",        # 11, 17
        "Function_18_6739",        # 12, 18
    )


    def Function_0_2A6(): pass

    label("Function_0_2A6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2B2"),
        (SWITCH_DEFAULT, "loc_354"),
    )


    label("loc_2B2")

    ClearMapFlags(0x1)
    OP_B1("t0700_0")
    OP_6D(55210, -3070, 40180, 0)
    OP_6B(5870, 0)
    OP_6C(201000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 41736, 4000, 31654, 118)
    SetChrPos(0x102, 41716, 4000, 32539, 129)
    SetChrPos(0xA, 43018, 4000, 33475, 205)
    SetChrPos(0xB, 42909, 4000, 30908, 282)
    ClearMapFlags(0x10)
    FadeToBright(2000, 0)
    Event(0, 11)
    Jump("loc_354")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36B")
    SetChrFlags(0xD, 0x80)
    Jump("loc_38F")

    label("loc_36B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0xD, 0x10)
    Jump("loc_38F")

    label("loc_37D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_38F")
    ClearChrFlags(0xD, 0x10)
    Jump("loc_38F")

    label("loc_38F")

    Return()

    # Function_0_2A6 end

    def Function_1_390(): pass

    label("Function_1_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B7")
    OP_B1("t0700_1")
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    Jump("loc_3F6")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DE")
    OP_B1("t0700_y")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    Jump("loc_3F6")

    label("loc_3DE")

    OP_B1("t0700_0")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)

    label("loc_3F6")

    OP_16(0x2, 0xFA0, 0xFFFE98A0, 0xFFFE8518, 0x30007)
    OP_71(0xE, 0x4)
    OP_71(0xE, 0x2)
    OP_72(0xE, 0x400)
    OP_72(0xE, 0x40)
    Return()

    # Function_1_390 end

    def Function_2_41D(): pass

    label("Function_2_41D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_432")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_41D")

    label("loc_432")

    Return()

    # Function_2_41D end

    def Function_3_433(): pass

    label("Function_3_433")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_456")
    OP_8D(0xFE, 29021, 54795, 33637, 48557, 4000)
    Jump("Function_3_433")

    label("loc_456")

    Return()

    # Function_3_433 end

    def Function_4_457(): pass

    label("Function_4_457")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　开往柏斯市\x02",
        )
    )

    CloseMessageWindow()

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

    # Function_4_457 end

    def Function_5_506(): pass

    label("Function_5_506")


    ChrTalk(
        0x102,
        (
            "#010F这里是控制塔的入口呢。\x02\x03",
            "#010F照明装置和搭乘用的船桥\x01",
            "都是由这里来控制的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_5_506 end

    def Function_6_5A4(): pass

    label("Function_6_5A4")


    ChrTalk(
        0x102,
        (
            "#010F这里面好像\x01",
            "不许无关人员进入呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F越是说不许进入，\x01",
            "我就越是想进去看看～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_6_5A4 end

    def Function_7_621(): pass

    label("Function_7_621")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6BC")

    ChrTalk(
        0xFE,
        (
            "听说从柏斯出发的定期船\x01",
            "突然失去了行踪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公社还没有收到来自定期船的联络，\x01",
            "真是担心是不是发生了什么意外。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1545")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_789")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "好慢啊……\x01",
            "怎么了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从柏斯起飞的定期船\x01",
            "到现在还没到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我这边的准备\x01",
            "都已经做好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F6")

    label("loc_789")


    ChrTalk(
        0x8,
        (
            "好慢啊……\x01",
            "怎么了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不会是发生事故了吧……\x02",
    )

    CloseMessageWindow()

    label("loc_7F6")

    Jump("loc_1545")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_969")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "你们知道王家的专用高速巡洋舰\x01",
            "『埃尔赛尤号』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是艘拥有纯白流线型的高级飞艇，\x01",
            "无论是外形还是气质都极具王家气派。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且它还凝聚了\x01",
            "导力技术的精华，\x01",
            "号称拥有世界第一的性能呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A46")

    label("loc_969")


    ChrTalk(
        0x8,
        (
            "你们知道王家的专用高速巡洋舰\x01",
            "『埃尔赛尤号』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "它凝聚了\x01",
            "导力技术的精华，\x01",
            "号称拥有世界第一的性能呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A46")

    Jump("loc_1545")

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_C37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "这一艘是西向航线的\x01",
            "定期船『赛希莉亚号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "马上就要起飞\x01",
            "开往柏斯地区了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "目前国内还没有\x01",
            "发生过什么严重的\x01",
            "定期船事故呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为飞艇公社\x01",
            "在安全上花了很多的功夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从来不发生事故\x01",
            "也是我们维修员的骄傲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C34")

    label("loc_BCE")


    ChrTalk(
        0x8,
        (
            "好，\x01",
            "导力引擎和机体的检查完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "随时都能起飞了哦。\x02",
    )

    CloseMessageWindow()

    label("loc_C34")

    Jump("loc_1545")

    label("loc_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D56")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "每一艘飞艇上\x01",
            "都配备有一台\x01",
            "相当强力的导力引擎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "听说引擎开发的费用\x01",
            "非常的昂贵呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，正因为有了王家的出资，\x01",
            "定期船才能够这么广泛投入实用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1C")

    label("loc_D56")


    ChrTalk(
        0x8,
        (
            "听说引擎开发的费用\x01",
            "非常的昂贵呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，正因为有了王家的出资，\x01",
            "定期船才能够这么广泛投入实用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1C")

    Jump("loc_1545")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_E9A")

    ChrTalk(
        0x8,
        "呼，终于忙完一阵了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今天风和日丽，\x01",
            "遨游蓝天一定是心旷神怡吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1545")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114F")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "说起来我们王国的五大都市\x01",
            "都有各自的魅力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "首先，我们这里就是\x01",
            "风光明媚的地方都市洛连特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在我们西边的是\x01",
            "和帝国贸易往来十分频繁的\x01",
            "商业都市柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "再往西的就是\x01",
            "利贝尔的外洋窗口，\x01",
            "美丽的海港都市卢安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而王国的南部就是\x01",
            "以导力器研究而闻名的\x01",
            "工房都市蔡斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而在瓦雷利亚湖东岸的就是\x01",
            "华丽宏伟的王都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "每一个城市都很有地方特色，\x01",
            "乘坐定期船到各地旅游也非常有趣哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1204")

    label("loc_114F")


    ChrTalk(
        0x8,
        (
            "王国的五大都市\x01",
            "每一个都很有地方特色，\x01",
            "坐着定期船环游各地是非常有趣的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "有机会一定要\x01",
            "乘坐飞艇去四处旅行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1204")

    Jump("loc_1545")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1382")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "在五大都市之间\x01",
            "往返的定期船分为\x01",
            "东向航线和西向航线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "西向航线是从格兰赛尔起飞、\x01",
            "途中经过洛连特、柏斯、卢安，\x01",
            "最后到蔡斯的顺序……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而东向航线就刚刚相反了，\x01",
            "从格兰赛尔起飞后，途径蔡斯、\x01",
            "卢安、柏斯，最后达到洛连特。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_1382")


    ChrTalk(
        0x8,
        (
            "而且不相邻的地区之间\x01",
            "是没有直航飞行的航线的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "除了王国军和王家专用的飞艇，\x01",
            "也只有非法航行的飞艇\x01",
            "才会这样偏离航线飞行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1480")

    Jump("loc_1545")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1505")
    OP_A2(0x5)

    ChrTalk(
        0x8,
        (
            "从格兰赛尔来的定期船\x01",
            "很快就要到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "必须准备进行着陆导航了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1545")

    label("loc_1505")


    ChrTalk(
        0x8,
        (
            "到了下午，\x01",
            "从柏斯来的航班也会抵达这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1545")

    TalkEnd(0x8)
    Return()

    # Function_7_621 end

    def Function_8_1549(): pass

    label("Function_8_1549")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(
        0xFE,
        (
            "公社的定期船突然失踪，\x01",
            "这可是前所未闻的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望乘客和定期船\x01",
            "都平安无事就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_166A")

    ChrTalk(
        0x9,
        "……怎么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "迟到这么久，\x01",
            "肯定是出什么事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_166A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D8")
    OP_A2(0x6)

    ChrTalk(
        0x9,
        (
            "自从飞艇发明以来，\x01",
            "洛连特也出现了许多\x01",
            "各种各样的来访者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "过去基本就只有\x01",
            "来收购七耀石、\x01",
            "木材和野菜的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今时今日徒步旅行的人\x01",
            "也相应减少了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为坐飞艇比较舒服，\x01",
            "而且更重要的是速度快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187E")

    label("loc_17D8")


    ChrTalk(
        0x9,
        (
            "今时今日徒步旅行的人\x01",
            "也相应减少了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为坐飞艇比较舒服，\x01",
            "而且更重要的是速度快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187E")

    Jump("loc_1DB3")

    label("loc_1881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1A14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197D")
    OP_A2(0x6)

    ChrTalk(
        0x9,
        (
            "有没有哪种味道是\x01",
            "别人没什么感觉\x01",
            "但你自己却十分喜欢的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我很喜欢\x01",
            "引擎发动时独特的焦糊味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "还有飞艇跑道\x01",
            "被雨水打湿时的味道……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A11")

    label("loc_197D")


    ChrTalk(
        0x9,
        (
            "我很喜欢\x01",
            "引擎发动时独特的焦糊味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "还有飞艇跑道\x01",
            "被雨水打湿时的味道……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A11")

    Jump("loc_1DB3")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1ABA")

    ChrTalk(
        0x9,
        (
            "从这里运出去的货物\x01",
            "果然还是七耀石最多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "自从导力器产业迅速发展以来，\x01",
            "矿山好像就一直很景气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_1ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1B49")

    ChrTalk(
        0x9,
        (
            "刚才飞走的那班定期船\x01",
            "是卡西乌斯先生乘的那艘吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "又是上哪里出差去了吧。\x01",
            "他可真是大忙人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1BE5")

    ChrTalk(
        0x9,
        (
            "今天的飞艇航运终于结束了，\x01",
            "为了让明天的航运继续正常运作，\x01",
            "安全检查一定要做到准确无误才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "『有备无患』，\x01",
            "这是我的行为准则之一。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_1BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7C")
    OP_A2(0x6)

    ChrTalk(
        0x9,
        (
            "对于我这份工作，\x01",
            "我感到很自豪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "原本我就想做\x01",
            "调整导力引擎这样的工作呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE3")

    label("loc_1C7C")


    ChrTalk(
        0x9,
        (
            "虽然我现在还是个维修员，\x01",
            "但是我的梦想是将来\x01",
            "成为一名设计飞艇的技术人员哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE3")

    Jump("loc_1DB3")

    label("loc_1CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D58")
    OP_A2(0x6)

    ChrTalk(
        0x9,
        (
            "哼哼，\x01",
            "今天果然睡过头了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "昨天喝得太多了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB3")

    label("loc_1D58")


    ChrTalk(
        0x9,
        (
            "糟糕，\x01",
            "要快点开始检点货物了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "打起精神来！\x02",
    )

    CloseMessageWindow()

    label("loc_1DB3")

    TalkEnd(0x9)
    Return()

    # Function_8_1549 end

    def Function_9_1DB7(): pass

    label("Function_9_1DB7")

    Call(0, 10)
    Return()

    # Function_9_1DB7 end

    def Function_10_1DBC(): pass

    label("Function_10_1DBC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3A")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "王国军正在搜索\x01",
            "行踪不明的定期船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "而且，根据公社的消息，\x01",
            "暂时还没有找到定期船的下落。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "发生什么事情了……\x01",
            "看来今天没有欣赏女孩子的份了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "拜托了，王国军。\x01",
            "我可是付了税金给你们做事的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCE")

    label("loc_1F3A")


    ChrTalk(
        0xC,
        (
            "王国军正在搜索\x01",
            "行踪不明的定期船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "而且，根据公社的消息，\x01",
            "暂时还没有找到定期船的下落。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCE")

    Jump("loc_3C2A")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_2BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2A")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(35650, 0, 32590, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, 35850, 0, 33370, 0)
    SetChrPos(0x102, 36660, 0, 32180, 0)
    SetChrPos(0x103, 35060, 0, 31950, 0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "真、真是对不起！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "定期船很快就会到的，\x01",
            "麻烦您再稍等片刻吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#4P阿兰哥哥，是我们啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "怎么，是艾丝蒂尔你们啊。\x01",
            "哟，雪拉扎德小姐也在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "到底怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P你有没有看到过\x01",
            "一位穿校服的女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "穿校服的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "是哪所学校的校服呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#4P杰尼丝王立学院的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊啊！\x01",
            "王立学院的校服真的很可爱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "清纯可爱的白色短裙，\x01",
            "和蓝色的长筒袜形成鲜明的对比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嗯～真是太迷人了。\x01",
            "不过，男生的校服我可不记得哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#4P我、我们问的不是这些啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F这就是男人的天性啦。\x02\x03",
            "#027F听你的意思就是没见到\x01",
            "有王立学院的女生来过吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "没有，\x01",
            "这一个月来都没见到过呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我一直在检查乘客的出入情况，\x01",
            "至少可以肯定的是没来过飞艇坪这边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F也就是说，那女孩没有乘坐飞艇，\x01",
            "而是沿着大道走到洛连特来的……\x02\x03",
            "#022F呼，这下可麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        (
            "#012F搜索范围一下子变大了。\x02\x03",
            "#012F仔细想想的话，她也许有同伙，\x01",
            "而且可能潜伏在这附近什么地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#004F啊，对了……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        "#023F怎么了，艾丝蒂尔？\x02",
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
            "【拿出塞尔贝树叶】\x01",              # 0
            "【………………是什么呢？】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2740")
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔拿出在阁楼里发现的塞尔贝树叶。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x101,
        (
            "#006F我都忘了捡到这个了。\x01",
            "说不定这是我们的线索呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2918")

    label("loc_2740")


    ChrTalk(
        0x101,
        "#008F………………是什么呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#018F我说……\x01",
            "艾丝蒂尔，你也认真一点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F难道刚才\x01",
            "在市长官邸里发现了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，对对，就是那个！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔拿出在阁楼里发现的塞尔贝树叶。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#006F我都忘了捡到这个了。\x01",
            "说不定这是我们的线索呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2918")


    ChrTalk(
        0x102,
        (
            "#010F对啊……还有这个啊。\x02\x03",
            "#010F雪拉姐姐，\x01",
            "知道这附近哪里会有塞尔贝树吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F塞尔贝树啊……\x02\x03",
            "#020F我记得是生长在\x01",
            "洛连特南部的神秘森林里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F神秘森林……\x01",
            "那地方是在我们家正南方向吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，看来我们有必要去一趟了。\x02\x03",
            "#006F既然决定了，\x01",
            "我们就赶快从南门出城吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "真有干劲呢。\x01",
            "虽然不知道怎么回事，不过多加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x263)
    OP_28(0x1B, 0x1, 0x10)
    OP_28(0x1B, 0x1, 0x20)
    OP_28(0x1B, 0x1, 0x40)
    EventEnd(0x0)
    Jump("loc_2BDD")

    label("loc_2B2A")


    ChrTalk(
        0xC,
        (
            "杰尼丝王立学院吗……\x01",
            "王立学院的校服真的很可爱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "清纯可爱的白色短裙，\x01",
            "和蓝色的长筒袜形成鲜明的对比。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "嗯～真是太迷人了。\x02",
    )

    CloseMessageWindow()

    label("loc_2BDD")

    Jump("loc_3C2A")

    label("loc_2BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_2D41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCC")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "从柏斯起飞的定期船\x01",
            "到现在还没来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "就因为这个， \x01",
            "让我不能欣赏女孩子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊啊，那可是我唯一的乐趣……\x01",
            "真是闷得不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F真是的，这个人啊……\x01",
            "还是老样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3E")

    label("loc_2CCC")


    ChrTalk(
        0xC,
        (
            "从柏斯起飞的\x01",
            "定期船到现在还没来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "就因为这个， \x01",
            "让我不能欣赏女孩子了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3E")

    Jump("loc_3C2A")

    label("loc_2D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_305D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAA")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "听说最近柏斯地区\x01",
            "有一伙驾驶飞艇进行抢劫的空贼\x01",
            "在到处作案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "对乘客的安检\x01",
            "必须要再严格些才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "要是有罪犯混进来，\x01",
            "那可就糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦，难得听到阿兰哥哥\x01",
            "说这么正经的话啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "因为要是女孩们遇到危险的话\x01",
            "我会很伤心的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "而且顺便也能给可爱的女孩作安检，\x01",
            "一石二鸟啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F……真是白夸他了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_305A")

    label("loc_2FAA")


    ChrTalk(
        0xC,
        (
            "听说最近柏斯地区\x01",
            "有一伙驾驶飞艇进行抢劫的空贼\x01",
            "在到处作案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "对乘客的安检\x01",
            "必须要再严格些才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305A")

    Jump("loc_3C2A")

    label("loc_305D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_32CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320C")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "女王诞辰庆典前后\x01",
            "是定期船最繁忙拥挤的时期。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我要是有个女朋友的话，\x01",
            "也想和她一起去王都游览啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在各国皇帝与众将大臣面前\x01",
            "寸步不让的女王陛下，\x01",
            "无论如何我都想见上一面啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "当然，\x01",
            "也一定要见见科洛蒂娅公主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "……唔唔㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_32CC")

    label("loc_320C")


    ChrTalk(
        0xC,
        (
            "女王诞辰庆典前后\x01",
            "是定期船最繁忙拥挤的时期。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我要是有个女朋友的话，\x01",
            "也想和她一起去王都游览啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CC")

    Jump("loc_3C2A")

    label("loc_32CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_34C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3408")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "虽然纯朴的姑娘很不错，\x01",
            "不过还是王都、柏斯这些地方的美女\x01",
            "更具有成熟魅力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "说起王都，\x01",
            "艾莉茜雅女王的孙女\x01",
            "科洛蒂娅公主也在那里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "传言说她清秀文雅楚楚动人，\x01",
            "真想一睹这位传说中的公主的风采。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C1")

    label("loc_3408")


    ChrTalk(
        0xC,
        (
            "虽然王都、柏斯这些地方的美女\x01",
            "更具有成熟魅力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "但纯朴的姑娘\x01",
            "也实在难以割舍啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C1")

    Jump("loc_3C2A")

    label("loc_34C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3541")

    ChrTalk(
        0xC,
        (
            "嗯……\x01",
            "今天开了个好头啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "从目前的情况来看，\x01",
            "平均能打８３分吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C2A")

    label("loc_3541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_36E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3644")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        "真没劲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "今天的乘客里\x01",
            "连一个我喜欢的类型都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "昨天柏斯来的定期船里\x01",
            "倒是出现了一个\x01",
            "外地口音的大美女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不知道她现在还在洛连特吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DE")

    label("loc_3644")


    ChrTalk(
        0xC,
        (
            "昨天柏斯来的定期船里\x01",
            "倒是出现了一个\x01",
            "外地口音的大美女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不知道她现在还在洛连特吗？\x02",
    )

    CloseMessageWindow()

    label("loc_36DE")

    Jump("loc_3C2A")

    label("loc_36E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_396E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E3")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        "古铜色的肌肤，红宝石似的双眸……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "雪拉扎德小姐的确是一位\x01",
            "充满异国色彩的美女啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "她有着利贝尔人\x01",
            "所没有的奇特魅力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F又来了，\x01",
            "阿兰哥哥的嗜好又要开始发作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "其实我以前还和雪拉扎德小姐\x01",
            "一起去喝过酒呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不过奇怪的是\x01",
            "我完全记不起当时的情形了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哈～哈～哈，\x01",
            "下次再邀请她一起去喝酒吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)
    Jump("loc_396B")

    label("loc_38E3")


    ChrTalk(
        0xC,
        (
            "整个上午，\x01",
            "连一个可爱的女孩子都没有出现呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "唯有看下午的班次会不会有了。\x02",
    )

    CloseMessageWindow()

    label("loc_396B")

    Jump("loc_3C2A")

    label("loc_396E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BEF")
    OP_A2(0x7)

    ChrTalk(
        0xC,
        (
            "今天又有许多人\x01",
            "从这里踏上他们各自的旅途了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "同时也有许多人\x01",
            "来到洛连特这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "最重要的是有许多的女孩子\x01",
            "也会经过这里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "从远处这样看着她们来来往往，\x01",
            "我感觉到了一种很单纯的快乐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "你明白这感觉吗，约修亚？\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#010F哦，也许吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F阿兰哥哥，\x01",
            "你还真是一副老样子呢。\x02\x03",
            "#501F就因为你老说这个，\x01",
            "才会没有女朋友的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "你真是会揭人伤疤啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不过就是有这份乐趣在，\x01",
            "工作起来才觉得很有意思嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哈哈哈～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F真是无药可救了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C2A")

    label("loc_3BEF")


    ChrTalk(
        0xC,
        (
            "看着各种各样的女孩子\x01",
            "从这里经过，\x01",
            "我感觉到了一种很单纯的快乐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2A")

    TalkEnd(0xC)
    Return()

    # Function_10_1DBC end

    def Function_11_3C2E(): pass

    label("Function_11_3C2E")

    OP_1D(0x58)
    OP_71(0xA, 0x4)
    OP_71(0xA, 0x2)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    EventBegin(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_43(0x101, 0x0, 0x0, 0xC)
    OP_43(0x102, 0x0, 0x0, 0xD)
    OP_43(0xA, 0x0, 0x0, 0xF)
    OP_43(0xB, 0x0, 0x0, 0xE)
    OP_43(0xB, 0x1, 0x0, 0x10)
    OP_67(0, 4500, -10000, 0)
    OP_6B(6000, 0)

    def lambda_3CAC():
        OP_67(0, 9500, -10000, 14000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3CAC)

    def lambda_3CC4():
        OP_6B(2800, 14000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3CC4)
    OP_22(0x75, 0x0, 0x64)
    OP_A2(0x4)
    OP_6D(42820, 4000, 32330, 14000)
    OP_A5(0x4)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#080F好了……差不多到时间了。\x02\x03",
            "#080F艾丝蒂尔，我不在的时候，\x01",
            "你可不要给约修亚添麻烦哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#3P老说这个，耳朵都听出茧来了～\x02\x03",
            "#000F爸爸也是，不要老是逞强哦。\x01",
            "年纪都一大把了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#085F哼哼，\x01",
            "我才不会输给年轻人呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        (
            "#080F雪拉，突然把工作都交给你，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#027F哪里，请别介意。\x02\x03",
            "#027F我还有点担心\x01",
            "自己无法代替老师完成任务呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#080F你太谦虚了，银闪。\x02\x03",
            "#080F我不在的这段时间，\x01",
            "这两个孩子就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#021F呵呵，老师请放心吧。\x02\x03",
            "#021F毫不纵容地\x01",
            "对他们严加管教就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#081F你果然明白我的想法啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#009F#3P什么呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#3P呵呵，真是心灵相通的俩师徒。\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开往王都的定期船\x01",
            "『林德号』马上就要起飞了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "请尚未登机的乘客尽快登机。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0xB, 0, 400)
    OP_8C(0xB, 45, 400)

    ChrTalk(
        0xB,
        "#084F哦，要出发了……\x02",
    )

    CloseMessageWindow()

    def lambda_423D():
        OP_67(0, 4370, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_423D)

    def lambda_4255():
        OP_6E(365, 6000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4255)
    OP_A2(0x4)
    OP_A2(0x2)
    OP_A2(0x3)
    OP_A5(0x2)
    OP_A5(0x4)
    OP_A3(0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#010F爸爸，一路顺风。\x01",
            "我们的事情您就放心好了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "『要早点回来哦』\x01",            # 0
            "『别忘记带礼物回来哦』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_434D"),
        (1, "loc_445B"),
        (SWITCH_DEFAULT, "loc_45A8"),
    )


    label("loc_434D")


    ChrTalk(
        0x101,
        (
            "#006F工作结束之后不要到处闲逛，\x01",
            "要早点回来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#083F你就不能说点好听的话吗。\x02\x03",
            "#080F算了……\x01",
            "总之我会尽早回来的。\x02\x03",
            "#080F那我走了，你们两个多保重。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A8")

    label("loc_445B")


    ChrTalk(
        0x101,
        (
            "#501F虽然不知道你要去哪里，\x01",
            "不过别忘记带礼物回来哦。\x02\x03",
            "#001F随便买些好玩的东西就行了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#083F喂喂，\x01",
            "我又不是去游山玩水。\x02\x03",
            "#080F不过钱包还有余裕的话，\x01",
            "倒是可以考虑一下。\x02\x03",
            "#080F那我走了，你们两个多保重。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A8")

    label("loc_45A8")

    Sleep(500)
    OP_8C(0x0, 90, 0)
    OP_8C(0x1, 90, 0)

    def lambda_45C1():
        OP_67(0, 7390, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_45C1)

    def lambda_45D9():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_45D9)
    OP_22(0x78, 0x0, 0x64)
    OP_70(0xD, 0x118)
    Sleep(3000)
    OP_6F(0xB, 2)
    OP_70(0xB, 0x118)
    Sleep(700)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xB)
    WaitChrThread(0x1, 0x3)
    Fade(1500)
    OP_6D(54360, -3070, 41690, 0)
    OP_67(0, 40540, -45000, 0)
    OP_6B(740, 0)
    OP_6C(208000, 0)
    OP_6E(510, 0)
    OP_8C(0x0, 45, 0)
    OP_8C(0x1, 45, 0)
    OP_8C(0xA, 45, 0)
    SetChrFlags(0xB, 0x80)

    def lambda_4676():
        OP_6C(223000, 13000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4676)
    LoadEffect(0x0, "map\\\\mp028_00.eff")
    Play3DEffect(0x0, 0x0, 0xB, "Frame1_E0000_ground_Layer1", 0xFFFFE7C8, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Play3DEffect(0x0, 0x1, 0xB, "Frame1_E0000_ground_Layer1", 0x1838, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xB, 200)
    OP_6F(0xC, 200)
    OP_70(0xB, 0x221)
    OP_70(0xC, 0x221)
    OP_73(0xB)

    def lambda_4740():
        OP_6D(54360, 1000, 41690, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4740)
    OP_6F(0xB, 546)
    OP_6F(0xC, 546)
    OP_70(0xB, 0x320)
    OP_70(0xC, 0x320)
    OP_73(0xB)

    def lambda_4777():
        OP_67(0, 39850, -45000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4777)

    def lambda_478F():
        OP_6C(314000, 12000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_478F)
    OP_6F(0xB, 800)
    OP_6F(0xC, 800)
    OP_70(0xB, 0x384)
    OP_70(0xC, 0x384)
    OP_73(0xB)
    OP_B0(0xB, 0x28)
    OP_B0(0xC, 0x28)
    OP_6F(0xB, 901)
    OP_6F(0xC, 901)
    OP_70(0xB, 0x3B6)
    OP_70(0xC, 0x3B6)
    OP_73(0xB)
    OP_B0(0xB, 0x32)
    OP_B0(0xC, 0x32)
    OP_6F(0xB, 951)
    OP_6F(0xC, 951)
    OP_70(0xB, 0x3E8)
    OP_70(0xC, 0x3E8)
    OP_73(0xB)
    OP_B0(0xB, 0x3C)
    OP_B0(0xC, 0x3C)
    OP_6F(0xB, 1001)
    OP_6F(0xC, 1001)
    OP_70(0xB, 0x41A)
    OP_70(0xC, 0x41A)
    OP_73(0xB)
    OP_B0(0xB, 0x46)
    OP_B0(0xC, 0x46)
    OP_6F(0xB, 1051)
    OP_6F(0xC, 1051)
    OP_70(0xB, 0x44C)
    OP_70(0xC, 0x44C)
    OP_73(0xB)
    OP_B0(0xB, 0x50)
    OP_B0(0xC, 0x50)
    OP_6F(0xB, 1101)
    OP_6F(0xC, 1101)
    OP_70(0xB, 0x47E)
    OP_70(0xC, 0x47E)
    OP_73(0xB)
    OP_B0(0xB, 0x5A)
    OP_B0(0xC, 0x5A)
    OP_6F(0xB, 1151)
    OP_6F(0xC, 1151)
    OP_70(0xB, 0x4B0)
    OP_70(0xC, 0x4B0)
    OP_73(0xB)
    OP_B0(0xB, 0x64)
    OP_B0(0xC, 0x64)
    OP_6F(0xB, 1201)
    OP_6F(0xC, 1201)
    OP_70(0xB, 0x4E2)
    OP_70(0xC, 0x4E2)
    OP_73(0xB)
    OP_B0(0xB, 0x6E)
    OP_B0(0xC, 0x6E)
    OP_6F(0xB, 1251)
    OP_6F(0xC, 1251)
    OP_70(0xB, 0x514)
    OP_70(0xC, 0x514)
    OP_73(0xB)
    OP_B0(0xB, 0x78)
    OP_B0(0xC, 0x78)
    OP_6F(0xB, 1301)
    OP_6F(0xC, 1301)
    OP_70(0xB, 0x546)
    OP_70(0xC, 0x546)
    OP_73(0xB)
    OP_B0(0xB, 0x82)
    OP_B0(0xC, 0x82)
    OP_6F(0xB, 1351)
    OP_6F(0xC, 1351)
    OP_70(0xB, 0x578)
    OP_70(0xC, 0x578)
    OP_73(0xB)
    OP_B0(0xB, 0x96)
    OP_B0(0xC, 0x96)
    OP_6F(0xB, 1401)
    OP_6F(0xC, 1401)
    OP_70(0xB, 0x7D0)
    OP_70(0xC, 0x7D0)
    FadeToDark(2000, 0, -1)
    Sleep(1500)
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
    Sleep(1000)
    OP_0D()
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    SetChrPos(0x101, 41807, 4000, 39449, 170)
    SetChrPos(0x102, 42334, 4000, 37937, 315)
    SetChrPos(0xA, 40186, 4000, 39987, 158)
    OP_67(0, 8000, -10000, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_6D(41380, 5450, 39120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#010F开走了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#1P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#020F别一脸寂寞的样子嘛。\x01",
            "反正老师很快就会回来的。\x02\x03",
            "#020F虽然不知道要调查什么，\x01",
            "不过对老师来说肯定是小菜一碟。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#009F#1P我、我才不觉得寂寞呢！\x02\x03",
            "#009F反正老爸不在家是常有的事。\x01",
            "我又不是不习惯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#021F是是。\x01",
            "随你怎么说了。\x02\x03",
            "#020F好了，我也要去处理\x01",
            "老师留给我的工作了……\x02\x03",
            "#020F如果工作上遇到什么困难，\x01",
            "尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#1P嗯，不过刚开始的时候\x01",
            "还是要靠自己努力。\x02\x03",
            "#006F起码要试试能做到什么程度吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#020F呵呵，听起来挺有自信的嘛。\x02\x03",
            "#020F不过有约修亚在，\x01",
            "我也用不着太过担心了。\x02\x03",
            "#020F你们两人要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#1P嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会努力的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A5(0x3)
    SetChrFlags(0xA, 0x80)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F接下来……要做什么呢？\x02\x03",
            "#010F先到协会去吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P嗯，问一下爱娜姐姐\x01",
            "看看我们可以做些什么工作吧。 \x02\x03",
            "#001F好的～我们出发吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_20(0x5DC)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    OP_A2(0x213)
    OP_21()
    OP_1E()
    Return()

    # Function_11_3C2E end

    def Function_12_4F6A(): pass

    label("Function_12_4F6A")

    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_12_4F6A end

    def Function_13_4F7F(): pass

    label("Function_13_4F7F")

    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_13_4F7F end

    def Function_14_4F94(): pass

    label("Function_14_4F94")

    OP_A6(0x2)
    OP_8E(0xFE, 0xB3BD, 0x1068, 0x7946, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xCF15, 0x1068, 0x7946, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    OP_A3(0x2)
    Return()

    # Function_14_4F94 end

    def Function_15_4FCF(): pass

    label("Function_15_4FCF")

    OP_A6(0x3)

    label("loc_4FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4FE4")
    TurnDirection(0xFE, 0xB, 0)
    OP_48()
    Jump("loc_4FD2")

    label("loc_4FE4")

    OP_A6(0x3)
    OP_8E(0xFE, 0x96E4, 0xFA0, 0x988D, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81AC, 0x7D0, 0x988D, 0x7D0, 0x0)
    OP_A3(0x3)
    Return()

    # Function_15_4FCF end

    def Function_16_5013(): pass

    label("Function_16_5013")

    OP_A6(0x4)
    OP_6C(72000, 14000)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6D(48784, 4000, 31814, 6000)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6D(55314, 1821, 30831, 4000)
    OP_6D(55314, 6821, 30831, 4000)
    OP_A3(0x4)
    Return()

    # Function_16_5013 end

    def Function_17_5062(): pass

    label("Function_17_5062")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_50FE")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "怎么了？\x01",
            "还有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "抱歉，\x01",
            "我现在正在忙着准备交易的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请不要打扰我。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    Jump("loc_6735")

    label("loc_50FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5170")

    ChrTalk(
        0xFE,
        "嗯～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在柏斯的交易\x01",
            "无论如何也要成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6735")

    label("loc_5170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x384)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D3C")
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x5, 0x1, 0x4)
    OP_A2(0x8)
    Fade(1000)
    EventBegin(0x0)
    SetChrPos(0x101, 38840, 0, 27320, 315)
    SetChrPos(0x102, 37840, 0, 26710, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E7")
    SetChrPos(0x2, 38840, 0, 25820, 0)
    SetChrPos(0x3, 37840, 0, 25210, 0)

    label("loc_51E7")

    OP_6D(37930, 0, 27910, 0)
    OP_6C(135000, 0)
    OP_6B(2800, 0)
    OP_6E(280, 0)
    OP_4A(0xD, 255)
    OP_8C(0xD, 180, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "怎么了？\x01",
            "找到蘑菇了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 0)

    ChrTalk(
        0x101,
        "#002F找是找到了没错。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xFE,
        "噢，太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F不过呢，\x01",
            "情况和你所说的有所不同。\x02\x03",
            "#505F这个蘑菇……\x01",
            "可是会吸引魔兽的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呜。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0x102,
        (
            "#012F奥维德先生在委托我们时\x01",
            "就知道会发生这样的情况吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "这、这样的事，\x01",
            "我怎么会知道。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "况且你们不是游击士吗，\x01",
            "处理危险情况本来就是你们的工作！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)
    OP_94(0x1, 0x101, 0x0, 0x1F4, 0x1770, 0x0)

    ChrTalk(
        0x101,
        (
            "#005F那也得先让我们有所准备啊！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xD, 0x9470, 0x0, 0x70EE, 0x258, 0x2710)
    OP_96(0xD, 0x927C, 0x0, 0x731E, 0xC8, 0x2710)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F我们的事情就算了，\x01",
            "问题是奥维德先生你的目的。\x02\x03",
            "这个蘑菇，\x01",
            "是要用来做什么的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F对～呀～\x01",
            "看起来也不像是用来做武器的。\x02\x03",
            "老实交代，\x01",
            "是不是打算用来做坏事？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xD, 0x9484, 0x0, 0x704E, 0x7D0, 0x0)
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xFE,
        "是用来做什么的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "当然是用作料理啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F…………料理？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F那种危险的蘑菇\x01",
            "居然可以拿来吃？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)
    OP_62(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "……所以说嘛，\x01",
            "你们乡下人就是不懂这些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果经过优秀厨师的精心烹制，\x01",
            "特别的食材可以产生出无与伦比的美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我看来，\x01",
            "『荧光菇』就是这样特别的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "毫无疑问可以烹制出究极的菜品！\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5890")
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_5890")

    Sleep(400)

    ChrTalk(
        0x102,
        "#017F………………\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#509F那你就慢慢品尝\x01",
            "自己所说的稀奇古怪的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "吃不到葡萄就说葡萄酸。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，像你们这种平民百姓，\x01",
            "一生都不会有机会品尝到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F……随便你怎么说。\x02\x03",
            "我肯定一生都不会\x01",
            "去吃那种绿色的蘑菇的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（确实是不太好吃的样子……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了好了，\x01",
            "我要准备待会儿的交易了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "快，\x01",
            "乖乖地把蘑菇交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F好～好～\x01",
            "早就想快点给你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xD, 0x1F4, 0x7D0, 0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "荧光菇\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x384, 1)
    OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)

    ChrTalk(
        0xFE,
        (
            "嗯，好了。看在蘑菇的份上，\x01",
            "我就当作没看到你们的无理好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "报酬依然会按照约定的数额支付，\x01",
            "就算是我一丁点儿的感谢吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼，\x01",
            "那个蘑菇是绝对卖不出去的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#009F我们走，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F告辞了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【采蘑菇】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xD, 0x10)
    Fade(1000)
    OP_6B(3300, 0)
    OP_6E(262, 0)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    TalkEnd(0xD)
    Jump("loc_6735")

    label("loc_5D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_6059")

    ChrTalk(
        0xFE,
        "有什么问题吗？\x02",
    )

    CloseMessageWindow()

    label("loc_5D65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_604C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            "【确认蘑菇的特征】\x01",      # 0
            "【没什么事】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5DCD"),
        (1, "loc_6004"),
        (SWITCH_DEFAULT, "loc_6004"),
    )


    label("loc_5DCD")


    ChrTalk(
        0xFE,
        (
            "『荧光菇』据说只生长在\x01",
            "富含七耀石成份的土壤里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且通常会生长在\x01",
            "茂密的草丛里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，由于埋在土里的缘故，\x01",
            "不仔细注意是很不容易发现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果还要说有什么其他特征，\x01",
            "就是会发出和其名字相符的淡绿色光芒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……嗯，大概就这么多了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F总的说来就是去玛鲁加山道的草丛中\x01",
            "寻找发光的蘑菇吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，希望你们能够尽快找到。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6049")

    label("loc_6004")


    ChrTalk(
        0xFE,
        "那么，希望你们能够尽快找到。\x02",
    )

    CloseMessageWindow()
    OP_5F(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6049")

    label("loc_6049")

    Jump("loc_5D65")

    label("loc_604C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6735")

    label("loc_6059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6735")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6667")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_6251")
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)

    ChrTalk(
        0xFE,
        "哦哦，现在有空吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为这件事情很急，\x01",
            "所以现在就谈谈行吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6244")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            "【听他说】\x01",      # 0
            "【不听】\x01",        # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_6134"),
        (1, "loc_6171"),
        (SWITCH_DEFAULT, "loc_6241"),
    )


    label("loc_6134")


    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(0, 18)
    Jump("loc_6241")

    label("loc_6171")


    ChrTalk(
        0x101,
        (
            "#505F嗯～抱歉哦。\x02\x03",
            "现在还不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，真是没办法啊。\x01",
            "我会在这儿等着的，\x01",
            "等你们有空再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总之是越快越好。\x02",
    )

    CloseMessageWindow()
    OP_28(0x5, 0x1, 0x8000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_8C(0xD, 0, 0)
    TalkEnd(0xD)
    Jump("loc_6241")

    label("loc_6241")

    Jump("loc_60DC")

    label("loc_6244")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6664")

    label("loc_6251")

    ClearChrFlags(0xD, 0x10)

    ChrTalk(
        0xFE,
        (
            "可恶，那些游击士。\x01",
            "到底还要我再等多久啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再不快一点，\x01",
            "我就要赶不上定期船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "果然是乡下的地方…………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(400)
    TurnDirection(0xD, 0x0, 0)

    ChrTalk(
        0xFE,
        "…………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦！\x01",
            "那不是游击士徽章吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "让我等好久了。\x01",
            "因为这件事情很急，\x01",
            "所以现在就谈谈行吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 0)

    label("loc_640D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_665A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            "【听他说】\x01",      # 0
            "【不听】\x01",        # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_6465"),
        (1, "loc_655E"),
        (SWITCH_DEFAULT, "loc_6657"),
    )


    label("loc_6465")


    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "哦哦，太好了。\x01",
            "真是帮了我大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那我就立刻说明\x01",
            "委托的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6545")
    TurnDirection(0x10F, 0xD, 400)

    ChrTalk(
        0x10F,
        (
            "#0142F………………………\x02\x03",
            "……我说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6545")

    Sleep(400)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(0, 18)
    Jump("loc_6657")

    label("loc_655E")


    ChrTalk(
        0x101,
        (
            "#505F嗯～抱歉哦。\x02\x03",
            "现在还不行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "什么？没空吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，真是没办法啊。\x01",
            "我会在这儿等着的，\x01",
            "等你们有空再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总之是越快越好。\x02",
    )

    CloseMessageWindow()
    OP_28(0x5, 0x1, 0x8000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_8C(0xD, 0, 0)
    TalkEnd(0xD)
    Jump("loc_6657")

    label("loc_6657")

    Jump("loc_640D")

    label("loc_665A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6664")

    Jump("loc_6735")

    label("loc_6667")


    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "要让我等到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再不快一点，\x01",
            "我就要赶不上定期船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，\x01",
            "就因为这样我才讨厌乡下地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6735")

    TalkEnd(0xD)
    Return()

    # Function_17_5062 end

    def Function_18_6739(): pass

    label("Function_18_6739")

    Fade(1000)
    EventBegin(0x0)
    SetChrPos(0x101, 38840, 0, 27320, 315)
    SetChrPos(0x102, 37840, 0, 26710, 0)
    SetChrPos(0x2, 38840, 0, 25820, 0)
    SetChrPos(0x3, 37840, 0, 25210, 0)
    OP_6D(37930, 0, 27910, 0)
    OP_6C(135000, 0)
    OP_6B(2800, 0)
    OP_6E(280, 0)
    OP_4A(0xD, 255)
    OP_8C(0xD, 180, 0)
    OP_0D()
    OP_28(0x5, 0x4, 0x4)
    OP_28(0x5, 0x4, 0x8)
    OP_28(0x5, 0x1, 0x1)

    ChrTalk(
        0xFE,
        "先自我介绍一下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我叫奥维德，\x01",
            "是奥维德商会的代表。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我叫艾丝蒂尔，\x01",
            "旁边的这位是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0x102,
        "#010F我叫约修亚，请多指教。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "是艾丝蒂尔和约修亚啊。\x01",
            "两个人都很年轻嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿，\x01",
            "因为我们都还是游击士的新人嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xFE,
        "新人……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔，倒也无所谓。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#501F什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咳咳……没、没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在就告诉你们委托的内容，\x01",
            "再不快点可能就会来不及的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正在寻找一种叫做\x01",
            "『荧光菇』的稀有蘑菇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说这种蘑菇只生长在\x01",
            "富含七耀石成份的土壤里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "洛连特这里有过采集记录，\x01",
            "但我找遍了所有商店都没有买到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论如何\x01",
            "我都想得到这种蘑菇，\x01",
            "因此就只能拜托游击士协会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这周围能采集到耀晶片的地方\x01",
            "就只有玛鲁加山道附近了……\x02\x03",
            "#010F这种蘑菇还有什么其他的特征吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "据说它通常会生长在\x01",
            "茂密的草丛里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，由于埋在土里的缘故，\x01",
            "如果不仔细寻找，\x01",
            "就很不容易发现。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#002F唉，这岂不是很麻烦……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "不过一旦挖出来的话，\x01",
            "很简单就可以辨认出\x01",
            "是不是荧光菇了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为那种蘑菇会\x01",
            "发出淡绿色的光芒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F这就是得名『荧光菇』的原因吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xFE,
        "我的说明够清楚了吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，总之就是到玛鲁加山道的草丛中\x01",
            "寻找发光的蘑菇对吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯，就是这样。\x02\x03",
            "如果真的是生长在土壤下面的话，\x01",
            "找起来就没那么简单了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F80():
        TurnDirection(0xD, 0x0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6F80)
    Sleep(200)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，如果还有什么问题\x01",
            "就再到这儿来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，希望你们能够尽快找到。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6B(3300, 0)
    OP_6E(262, 0)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    TalkEnd(0xD)
    Return()

    # Function_18_6739 end

    SaveToFile()

Try(main)
