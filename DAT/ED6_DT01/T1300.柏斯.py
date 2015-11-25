from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1300   ._SN',
        MapName             = 'Bose',
        Location            = 'T1300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1300   ._SN',
            'ED6_DT01/T1300_1 ._SN',
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
        '士兵卡多尔斯',                         # 9
        '斯丁克',                               # 10
        '哈尔德',                               # 11
        '梅尔茨',                               # 12
        '照相机',                               # 13
        '士兵阿萨',                             # 14
        '士兵迈奇',                             # 15
        '玛诺利亚海岸方向',                     # 16
        '西柏斯街道方向',                       # 17
    )

    DeclEntryPoint(
        Unknown_00              = -42300,
        Unknown_04              = -500,
        Unknown_08              = 29000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 225,
        Unknown_32              = 180,
        Unknown_34              = 270,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT07/CH01120 ._CH',             # 02
        'ED6_DT07/CH01760 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
        'ED6_DT07/CH01760P._CP',             # 03
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = -50,
        Y                   = 16500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 99500,
        Z                   = -50,
        Y                   = 99500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = -50,
        Y                   = 16500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = -50,
        Y                   = 16500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -48000,
        Z                   = -50,
        Y                   = -10000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -47600,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -50220,
        Z                   = -500,
        Y                   = -35780,
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
        X                   = -40370,
        Z                   = -500,
        Y                   = 36990,
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


    DeclEvent(
        X                   = -51360,
        Y                   = -2000,
        Z                   = 11340,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -51690,
        TriggerZ            = -470,
        TriggerY            = 23510,
        TriggerRange        = 1500,
        ActorX              = -51690,
        ActorZ              = 1800,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53780,
        TriggerZ            = -510,
        TriggerY            = -19530,
        TriggerRange        = 1500,
        ActorX              = -53780,
        ActorZ              = 1900,
        ActorY              = -19530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_336",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_3A0",          # 03, 3
        "Function_4_C54",          # 04, 4
        "Function_5_10D7",         # 05, 5
        "Function_6_1869",         # 06, 6
        "Function_7_1B49",         # 07, 7
        "Function_8_2126",         # 08, 8
        "Function_9_26CF",         # 09, 9
        "Function_10_2965",        # 0A, 10
        "Function_11_29F5",        # 0B, 11
        "Function_12_2A85",        # 0C, 12
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_26B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_284")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_293")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2A2")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2B8")

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2AC")
    Jump("loc_2B8")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2B8")
    ClearChrFlags(0x9, 0x80)

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30D")
    RemoveParty(0x34, 0xFF)
    SetMapFlags(0x400000)
    ClearChrFlags(0xA, 0x80)
    OP_6C(270000, 0)
    OP_6B(3400, 0)
    OP_6D(-44000, 0, 24400, 0)
    Event(1, 0)

    label("loc_30D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_319"),
        (SWITCH_DEFAULT, "loc_335"),
    )


    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_332")
    OP_B1("t1300_y")
    Event(0, 7)

    label("loc_332")

    Jump("loc_335")

    label("loc_335")

    Return()

    # Function_0_252 end

    def Function_1_336(): pass

    label("Function_1_336")

    OP_16(0x2, 0xFA0, 0xFFFD48B0, 0xFFFE17B8, 0x30044)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_360")
    OP_B1("t1300_y")
    Jump("loc_369")

    label("loc_360")

    OP_B1("t1300_n")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37A")
    OP_1B(0x3, 0x0, 0x9)

    label("loc_37A")

    OP_71(0x0, 0x10)
    OP_1C(0x0, 0x0, 0xC)
    OP_1C(0x1, 0x0, 0xC)
    Return()

    # Function_1_336 end

    def Function_2_38A(): pass

    label("Function_2_38A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_38A")

    label("loc_39F")

    Return()

    # Function_2_38A end

    def Function_3_3A0(): pass

    label("Function_3_3A0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_403")

    ChrTalk(
        0xFE,
        "离值勤还有段时间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是先\x01",
            "稍微小睡一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_58B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "这里是深山老林，\x01",
            "食物的供应非常不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然也有很多东西\x01",
            "从柏斯和卢安那里运送过来，\x01",
            "不过毕竟是山路啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经常需要去迎接送货的人，\x01",
            "并且给他们顺便但当护卫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_588")

    label("loc_528")


    ChrTalk(
        0xFE,
        (
            "这里一到冬天，\x01",
            "大雪就会堆积起来，特别不方便。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_588")

    Jump("loc_C50")

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_61F")

    ChrTalk(
        0xFE,
        "差不多到训练的时间了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为发生过魔兽袭击事件，\x01",
            "大家要提高警惕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_7A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70B")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "早上好，昨天谢谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然看上去挺年轻，\x01",
            "但真不愧是游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "干得真棒。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A6")

    label("loc_70B")


    ChrTalk(
        0xFE,
        (
            "虽然看上去挺年轻，\x01",
            "但真不愧是游击士呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "昨天干得真棒。\x02",
    )

    CloseMessageWindow()

    label("loc_7A6")

    Jump("loc_C50")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_86D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "有什么事吗？\x01",
            "你们可以随便进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要使用休息室的话，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_82A")


    ChrTalk(
        0xFE,
        (
            "要使用休息室的话，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A")

    Jump("loc_C50")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_994")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "好像还是找不到\x01",
            "空贼团的所在之处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "国境守备队的那伙人\x01",
            "也经常到这里来进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯这个地方\x01",
            "就是山岳比较多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "犯人要是隐藏在这里，\x01",
            "可是最难发现的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_994")


    ChrTalk(
        0xFE,
        (
            "柏斯这个地方\x01",
            "就是山岳比较多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "犯人要是隐藏在这里，\x01",
            "可是最难发现的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E")

    Jump("loc_C50")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_AC3")

    ChrTalk(
        0xFE,
        (
            "消失的定期船\x01",
            "好像被找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为犯人还没有被抓住，\x01",
            "所以关所还要继续\x01",
            "维持盘查的制度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_BA0")

    ChrTalk(
        0xFE,
        (
            "是空贼团吗……\x01",
            "真是一群不容易对付的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，这次是由那位\x01",
            "摩尔根将军亲临指挥呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定马上就会抓到他们的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C50")

    label("loc_BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(
        0xFE,
        "要去卢安吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果是的话，\x01",
            "必须要先办通行手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为现在正处于戒严状态。\x02",
    )

    CloseMessageWindow()

    label("loc_C50")

    TalkEnd(0x8)
    Return()

    # Function_3_3A0 end

    def Function_4_C54(): pass

    label("Function_4_C54")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC8")
    OP_A2(0x35F)

    ChrTalk(
        0x101,
        (
            "#006F（咦……\x01",
            "　这个人莫非是……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，\x01",
            "　好像和我们一样都是游击士呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F喂，打扰一下？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F你还是那样不讨人喜欢呢，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "你是……\x01",
            "以前的那个见习游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F没错呢。\x02\x03",
            "托你的福，\x01",
            "现在我已经是正游击士啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……看起来的确成熟了不少。\x01",
            "在柏斯支部有工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，现在就正在工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近发生了很多事情，\x01",
            "游击士的人手远远不够呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……那就靠你们了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    ChrTalk(
        0x101,
        (
            "#002F（是雪拉姐的熟人吧。\x01",
            "　感觉有点恐怖的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（但是那走路的动作……\x01",
            "　看起来应该很厉害吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D3")

    label("loc_FC8")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0x103,
        (
            "#020F斯丁克，\x01",
            "这附近是不是出什么事情了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是雪拉扎德啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我接到通报说在这一带\x01",
            "有人看到了没见过的魔兽，\x01",
            "所以前来调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F辛苦你了。\x01",
            "我们彼此加油吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    label("loc_10D3")

    TalkEnd(0x9)
    Return()

    # Function_4_C54 end

    def Function_5_10D7(): pass

    label("Function_5_10D7")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(
        0xFE,
        (
            "堡垒的人最近\x01",
            "总是谈论市长被捕这个话题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EC")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "今天该轮到\x01",
            "我来炒菜做饭了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过刚才副长来，\x01",
            "说要代替我做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个人，\x01",
            "真的非常喜欢烹饪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126D")

    label("loc_11EC")


    ChrTalk(
        0xFE,
        (
            "刚才副长来了，\x01",
            "说要代替我做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个人，\x01",
            "真的非常喜欢烹饪啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126D")

    Jump("loc_1865")

    label("loc_1270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_136F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1319")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "自从空贼被逮捕以来，\x01",
            "柏斯地区就非常和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，要是接连不断发生事件\x01",
            "那真是很难办啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136C")

    label("loc_1319")


    ChrTalk(
        0xFE,
        (
            "自从空贼被逮捕以来，\x01",
            "柏斯地区就非常和平。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136C")

    Jump("loc_1865")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1403")

    ChrTalk(
        0xFE,
        (
            "之前来的魔兽\x01",
            "比想象中的要厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也必须\x01",
            "加紧训练才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_14A0")

    ChrTalk(
        0xFE,
        (
            "昨天的袭击\x01",
            "真是个很好的教训。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来平时\x01",
            "就要做好充分准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(
        0xFE,
        (
            "搜索这样持续下去，\x01",
            "国境师团的家伙们也相当累吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果有什么新的进展就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1606")

    ChrTalk(
        0xFE,
        (
            "这一带\x01",
            "越往山中走魔兽越多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且被通缉的魔兽\x01",
            "也越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "每天的训练是必不可少的啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_1606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169F")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "这座古罗尼连峰的地形\x01",
            "也是起伏频繁的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难不成……\x01",
            "空贼团那些家伙们\x01",
            "都隐藏在这一带？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FF")

    label("loc_169F")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "国境师团的搜查队\x01",
            "已经在这里调查好几次了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FF")

    Jump("loc_1865")

    label("loc_1702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "这么险峻的山道，\x01",
            "一般来说旅行的人\x01",
            "是根本不会走的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为现在飞艇还在停航，\x01",
            "急着去卢安和柏斯的人们\x01",
            "不得不从这里通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1865")

    label("loc_17D9")


    ChrTalk(
        0xFE,
        (
            "但是不管怎么说，\x01",
            "还是应该尽量避免\x01",
            "在晚上翻越这座山峰啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对一般人来说太危险了。\x02",
    )

    CloseMessageWindow()

    label("loc_1865")

    TalkEnd(0xD)
    Return()

    # Function_5_10D7 end

    def Function_6_1869(): pass

    label("Function_6_1869")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18E5")

    ChrTalk(
        0xFE,
        (
            "听说卢安的市长\x01",
            "被逮捕了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "竟然有这种事情。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_18E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1980")

    ChrTalk(
        0xFE,
        (
            "被魔兽打伤的地方\x01",
            "终于痊愈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要尽量避免以后再发生这类事情，\x01",
            "所以要加紧训练。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1A17")

    ChrTalk(
        0xFE,
        "副长还真是喜欢烹饪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时候明明不是他当班，\x01",
            "但是他却在厨房做饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1AB3")

    ChrTalk(
        0xFE,
        "柴火差不多要用完了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "训练结束后去报告一下，\x01",
            "然后就去砍些柴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_1AEB")

    ChrTalk(
        0xFE,
        "痛痛痛痛痛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是失策。\x01",
            "被魔兽打伤的地方好痛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_1AEB")


    ChrTalk(
        0xFE,
        "一会儿就轮到我值班了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "趁现在赶快吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B45")

    TalkEnd(0xE)
    Return()

    # Function_6_1869 end

    def Function_7_1B49(): pass

    label("Function_7_1B49")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, -43430, -550, 25300, 225)
    SetChrPos(0x102, -43600, -600, 26890, 225)
    OP_6D(-46560, -50, -15120, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(5140, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_6D(-48090, -50, 16940, 8000)
    Fade(500)
    OP_6D(-44280, -480, 24940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 3)), scpexpr(EXPR_END)), "loc_1D46")

    ChrTalk(
        0x101,
        (
            "#501F#1P呼～～总算到了。\x02\x03",
            "只要过了这个关所，\x01",
            "就可以进入卢安地区了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，应该是这样。\x02\x03",
            "#013F不过不好办啊……太阳快要下山了。\x02\x03",
            "今天我们还是\x01",
            "在这里借宿一晚吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E75")

    label("loc_1D46")


    ChrTalk(
        0x101,
        (
            "#501F#1P呼～～总算到了。\x02\x03",
            "那就是关所吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像是。\x01",
            "只要过了这里就是卢安地区了。\x02\x03",
            "#013F不过不好办啊……太阳快要下山了。\x02\x03",
            "今天我们还是\x01",
            "在这里借宿一晚吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E75")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1P我倒没意见……\x02\x03",
            "不过，我们赶路下山，\x01",
            "然后找家旅馆落脚不也行吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F晚上下山很危险的。\x01",
            "光线暗，走起路来也很麻烦。\x02\x03",
            "要是被夜行性的魔兽袭击的话，\x01",
            "可能会从山崖上掉下去的。\x02\x03",
            "#010F所以还是不要这样比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F#1P呜啊啊～听起来真的好危险。\x02\x03",
            "总之还是先问问\x01",
            "关所的士兵能不能借宿吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMapFlags(0x1)
    Fade(1000)
    OP_6D(-43600, -554, 24000, 0)
    SetChrPos(0x0, -43600, -550, 26890, 180)
    SetChrPos(0x1, -43600, -550, 26890, 180)
    OP_0D()
    EventEnd(0x2)
    OP_A2(0x402)
    OP_1B(0x3, 0x0, 0x9)
    Return()

    # Function_7_1B49 end

    def Function_8_2126(): pass

    label("Function_8_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26CE")
    OP_A2(0x403)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    TurnDirection(0x0, 0x8, 0)
    TurnDirection(0x1, 0x8, 0)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    ClearMapFlags(0x1)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "哟，真少见。\x01",
            "这么晚了还有客人来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "客人是来郊游的吧。\x01",
            "难道你们迷了路？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呵呵，不是呢。\x02\x03",
            "我们两个可是\x01",
            "从洛连特来的游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔向士兵出示准游击士的徽章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "哎～这种年纪就当了游击士，\x01",
            "真让人吃惊呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那么你们是来工作的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也不是，其实我们是为了成为\x01",
            "正游击士而打算到王国各地旅行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F因此我们没乘坐定期船，\x01",
            "一边修行一边走路过来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "绕着王国走一圈啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈～真不知该说你们太年轻呢，\x01",
            "还是该称赞你们很有干劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嘿嘿～～这没什么啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过不管怎么说，\x01",
            "现在下山是非常危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且最近这附近\x01",
            "又发生过魔兽暴动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "关所里有旅行者专用的休息室，\x01",
            "你们今晚还是在这里过夜吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F太好了，谢谢你啦☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是帮了我们的大忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "小意思小意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要使用休息室的话，\x01",
            "和我们队长打声招呼就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "他就在里面的值勤室。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_4B(0x8, 255)
    EventEnd(0x1)

    label("loc_26CE")

    Return()

    # Function_8_2126 end

    def Function_9_26CF(): pass

    label("Function_9_26CF")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2819")
    OP_A2(0xA)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BC")

    ChrTalk(
        0x102,
        (
            "#010F天色已经晚了，\x01",
            "街道上会很危险的。\x02\x03",
            "向关所的士兵说明情况，\x01",
            "今天就在这里过夜吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2816")

    label("loc_27BC")


    ChrTalk(
        0x102,
        (
            "#010F天色已经晚了，\x01",
            "今天就在关所的休息室过夜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2816")

    Jump("loc_293A")

    label("loc_2819")

    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E0")

    ChrTalk(
        0x102,
        (
            "#010F天色已经晚了，\x01",
            "街道上会很危险的。\x02\x03",
            "向关所的士兵说明情况，\x01",
            "今天就在这里过夜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_28E0")


    ChrTalk(
        0x102,
        (
            "#010F天色已经晚了，\x01",
            "今天就在关所的休息室过夜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293A")

    Fade(1000)
    SetChrPos(0x0, -43600, -550, 26890, 180)
    SetChrPos(0x1, -43600, -550, 26890, 180)
    OP_0D()
    EventEnd(0x2)
    Return()

    # Function_9_26CF end

    def Function_10_2965(): pass

    label("Function_10_2965")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东北　柏斯市　　　４４１塞尔矩\x01",
            "西南　卢安市　　　６６９塞尔矩\x01",
            "　　　玛诺利亚村　３５７塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_2965 end

    def Function_11_29F5(): pass

    label("Function_11_29F5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西南　卢安市　　　６６９塞尔矩\x01",
            "　　　玛诺利亚村　３５７塞尔矩\x01",
            "东北　柏斯市　　　４４１塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_29F5 end

    def Function_12_2A85(): pass

    label("Function_12_2A85")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_12_2A85 end

    SaveToFile()

Try(main)
