from ED6ScenarioHelper import *

def main():
    # 洛连特市 民居

    CreateScenaFile(
        FileName            = 'T0110   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0110.x',
        MapIndex            = 11,
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
        '雷特拉',                               # 9
        '赛拉',                                 # 10
        '玛茜婆婆',                             # 11
        '鲁克',                                 # 12
        '帕特',                                 # 13
        '日记',                                 # 14
    )

    DeclEntryPoint(
        Unknown_00              = 52000,
        Unknown_04              = 0,
        Unknown_08              = 164000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 83000,
        Unknown_04              = 0,
        Unknown_08              = 116000,
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
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01120 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH01110 ._CH',             # 02
        'ED6_DT07/CH01160 ._CH',             # 03
        'ED6_DT07/CH01060 ._CH',             # 04
        'ED6_DT06/CH20021 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01120P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH01110P._CP',             # 02
        'ED6_DT07/CH01160P._CP',             # 03
        'ED6_DT07/CH01060P._CP',             # 04
        'ED6_DT06/CH20021P._CP',             # 05
    )

    DeclNpc(
        X                   = 93326,
        Z                   = 0,
        Y                   = 162898,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 58084,
        Z                   = 0,
        Y                   = 198250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 51750,
        Z                   = 0,
        Y                   = 163200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 55045,
        Z                   = 0,
        Y                   = 164193,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 88798,
        Z                   = 0,
        Y                   = 163093,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 52700,
        Z                   = 700,
        Y                   = 161650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 52860,
        TriggerZ            = 0,
        TriggerY            = 161440,
        TriggerRange        = 800,
        ActorX              = 52700,
        ActorZ              = 700,
        ActorY              = 161650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_24A",          # 02, 2
        "Function_3_260",          # 03, 3
        "Function_4_284",          # 04, 4
        "Function_5_2A8",          # 05, 5
        "Function_6_2CC",          # 06, 6
        "Function_7_FE8",          # 07, 7
        "Function_8_1905",         # 08, 8
        "Function_9_1B21",         # 09, 9
        "Function_10_233F",        # 0A, 10
        "Function_11_2453",        # 0B, 11
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_211")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_227")

    label("loc_211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_227")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_227")

    Return()

    # Function_0_202 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240")
    OP_B1("t0110_y")
    Jump("loc_249")

    label("loc_240")

    OP_B1("t0110_n")

    label("loc_249")

    Return()

    # Function_1_228 end

    def Function_2_24A(): pass

    label("Function_2_24A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_24A")

    label("loc_25F")

    Return()

    # Function_2_24A end

    def Function_3_260(): pass

    label("Function_3_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_283")
    OP_8D(0xFE, 51000, 165000, 56500, 163300, 2500)
    Jump("Function_3_260")

    label("loc_283")

    Return()

    # Function_3_260 end

    def Function_4_284(): pass

    label("Function_4_284")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A7")
    OP_8D(0xFE, 52766, 165023, 56498, 163482, 3000)
    Jump("Function_4_284")

    label("loc_2A7")

    Return()

    # Function_4_284 end

    def Function_5_2A8(): pass

    label("Function_5_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB")
    OP_8D(0xFE, 87700, 161023, 91100, 164700, 3000)
    Jump("Function_5_2A8")

    label("loc_2CB")

    Return()

    # Function_5_2A8 end

    def Function_6_2CC(): pass

    label("Function_6_2CC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_43D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "看了利贝尔通讯\x01",
            "才知道最近柏斯相继\x01",
            "发生了多宗的盗窃案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起柏斯，\x01",
            "那可是王国的经济中心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以说也有不少不法之徒\x01",
            "也喜欢在这个城市作案。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A")

    label("loc_3BB")


    ChrTalk(
        0xFE,
        (
            "说起柏斯，\x01",
            "那可是王国的经济中心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以说也有不少不法之徒\x01",
            "也喜欢在这个城市作案。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A")

    Jump("loc_FE4")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4E1")

    ChrTalk(
        0xFE,
        (
            "说起来\x01",
            "最近利贝尔通讯\x01",
            "卖得很火啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不久前原本\x01",
            "还只是仅在王都一带\x01",
            "发行的小型杂志呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "利贝尔王国\x01",
            "被两个强大势力夹在中间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "分别是北边的埃雷波尼亚帝国\x01",
            "和东边的卡尔瓦德共和国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但值得骄傲的是，\x01",
            "王国自建国以来一直保持着独立。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677")

    label("loc_5DD")


    ChrTalk(
        0xFE,
        (
            "利贝尔王国\x01",
            "被两个强大势力夹在中间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但值得骄傲的是，\x01",
            "王国自建国以来一直保持着独立。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_677")

    Jump("loc_FE4")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_87A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A8")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "这个国家共分五个地区，\x01",
            "每个地区都有各自的中心都市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "克劳斯市长就是五大都市之一的\x01",
            "洛连特的负责人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他成天优哉游哉地打理庭院，\x01",
            "还被人叫作克劳斯爷爷，\x01",
            "但其实是个很了不起的人哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_877")

    label("loc_7A8")


    ChrTalk(
        0xFE,
        (
            "克劳斯市长就是五大都市之一的\x01",
            "洛连特的负责人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他成天优哉游哉地打理庭院，\x01",
            "还被人叫作克劳斯爷爷，\x01",
            "但其实是个很了不起的人哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_877")

    Jump("loc_FE4")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_992")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "得知帕特去了翡翠之塔，\x01",
            "我可是吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这孩子虽然很乖，\x01",
            "但小孩子总是好奇心旺盛的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这本身并不是什么坏事，\x01",
            "但这次也太出格了，我狠狠骂了他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3F")

    label("loc_992")


    ChrTalk(
        0xFE,
        (
            "得知帕特去了翡翠之塔，\x01",
            "我可是吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这孩子虽然很乖，\x01",
            "但小孩子总是好奇心旺盛的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F")

    Jump("loc_FE4")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_C38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AA4")

    ChrTalk(
        0x8,
        (
            "古代文明真是\x01",
            "充满神奇的魅力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BC7")
    OP_A2(0x1)

    ChrTalk(
        0x8,
        (
            "在利贝尔王国有四座巨大的塔，\x01",
            "你们知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这四座塔非常的古老，\x01",
            "书上记载着它们和\x01",
            "古代文明有着密切的联系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "古代文明真是\x01",
            "充满神奇的魅力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_BC7")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "呼……\x01",
            "终于把这本最近一直在找的书给找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不知道为何竟然\x01",
            "和帕特的画册混在一起了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C35")

    Jump("loc_FE4")

    label("loc_C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1D")
    OP_A2(0x29B)

    ChrTalk(
        0x8,
        (
            "最近因为飞艇来往频繁的缘故，\x01",
            "洛连特这里也进了许多好书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因此我经常去店里\x01",
            "一本一本地买了来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "待会儿老婆可能又要骂我了，\x01",
            "我想我还是小心一点好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这本书是一套小说的第一卷，\x01",
            "我就把它送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x212, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第１卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_E55")

    label("loc_E1D")


    ChrTalk(
        0x8,
        (
            "嗯，我想找的那本书\x01",
            "果然不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E55")

    Jump("loc_FE4")

    label("loc_E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F80")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "《王国的荣耀》……\x01",
            "《导力器技术概论》……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "《洛连特的历程》……\x01",
            "《七耀教会和游击士协会》……\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "上次买的那本书\x01",
            "到底放在哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "看来不好好整理一下不行了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_F80")


    ChrTalk(
        0x8,
        (
            "嗯～这本是……\x01",
            "《吃遍世界之利贝尔篇》？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "怎么搞的……\x01",
            "竟然还买过这样一本书？？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE4")

    TalkEnd(0x8)
    Return()

    # Function_6_2CC end

    def Function_7_FE8(): pass

    label("Function_7_FE8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(
        0xFE,
        (
            "最近老公和帕特那孩子\x01",
            "多了很多话说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这下终于\x01",
            "有了家庭温馨的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1901")

    label("loc_1070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_11F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119C")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "救了帕特的两位游击士\x01",
            "最近好像很活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说是一对\x01",
            "年轻的男女搭档。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤其是那男孩，\x01",
            "主妇们都说他很可爱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F（……难道约修亚是传说中的主妇杀手？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F0")

    label("loc_119C")


    ChrTalk(
        0xFE,
        (
            "洛连特聚集了不少有名的游击士，\x01",
            "托他们的福，\x01",
            "我们才能安居乐业。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F0")

    Jump("loc_1901")

    label("loc_11F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D7")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "有个叫尤妮的女孩\x01",
            "和帕特很要好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她上主日学校时\x01",
            "她爸爸都会接送呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们父女感情真好，\x01",
            "真叫人有点羡慕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1326")

    label("loc_12D7")


    ChrTalk(
        0xFE,
        "我要不要也去接帕特呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但他可能不愿我去……\x02",
    )

    CloseMessageWindow()

    label("loc_1326")

    Jump("loc_1901")

    label("loc_1329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D1")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "不知我家的帕特\x01",
            "将来想做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可不希望他也像鲁克那样\x01",
            "梦想当什么游击士，\x01",
            "最好是选个安全又稳定的职业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1403")

    label("loc_13D1")


    ChrTalk(
        0xFE,
        (
            "我可不希望我家的孩子\x01",
            "梦想当什么游击士，\x01",
            "最好是选个安全又稳定的职业。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1403")

    Jump("loc_1901")

    label("loc_1406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_155F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1527")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "全家三口开了个家庭会议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老公也好好\x01",
            "批评了帕特一顿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "帕特本来\x01",
            "就是懂事的孩子，\x01",
            "也好好反省过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次对大家来说\x01",
            "也是个好教训呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_155C")

    label("loc_1527")


    ChrTalk(
        0xFE,
        (
            "我们家也终于\x01",
            "有点长进了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155C")

    Jump("loc_1901")

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_16A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165D")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "我家那孩子\x01",
            "刚才又跑到外面的街道去了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我一再的告诫他\x01",
            "外面有魔兽出没很危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "回头我一定得让老公\x01",
            "好好说说他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A2")

    label("loc_165D")


    ChrTalk(
        0x9,
        (
            "……看来我\x01",
            "必须得开一次\x01",
            "家庭会议才行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A2")

    Jump("loc_1901")

    label("loc_16A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_17FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1751")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "我家的帕特\x01",
            "一大早就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "千万不要和鲁克\x01",
            "一起去学坏了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "真是让人担心啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_17F7")

    label("loc_1751")


    ChrTalk(
        0x9,
        (
            "而且老公从来不管孩子，\x01",
            "只会呆在房间里面\x01",
            "不知道干些什么事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "女神啊……\x01",
            "家庭要面临崩溃的危机了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F7")

    Jump("loc_1901")

    label("loc_17FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        "咳咳、咳咳……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是的，\x01",
            "老公竟然把书架给弄倒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "弄得屋子里\x01",
            "到处都是灰尘。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1901")

    label("loc_188E")


    ChrTalk(
        0x9,
        (
            "老公竟然\x01",
            "把书架给弄倒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "弄得屋子里\x01",
            "到处都是灰尘。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1901")

    TalkEnd(0x9)
    Return()

    # Function_7_FE8 end

    def Function_8_1905(): pass

    label("Function_8_1905")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1972")

    ChrTalk(
        0xFE,
        (
            "之前没有发觉，\x01",
            "我的爸爸\x01",
            "懂得很多事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大人们果然\x01",
            "都很厉害啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1D")

    label("loc_1972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8D")
    OP_A2(0x5)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xC,
        (
            "艾丝蒂尔姐姐，\x01",
            "今天真是谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "如果姐姐你们\x01",
            "没有来救我们的话，\x01",
            "我们不知道会变成什么样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我想鲁克也会非常\x01",
            "感谢姐姐你们的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "姐姐就别再生他的气了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B1D")

    label("loc_1A8D")


    ChrTalk(
        0xC,
        (
            "我想鲁克也会非常\x01",
            "感谢姐姐你们的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "姐姐就别再生他的气了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1B1D")

    TalkEnd(0xC)
    Return()

    # Function_8_1905 end

    def Function_9_1B21(): pass

    label("Function_9_1B21")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BF0")

    ChrTalk(
        0xFE,
        (
            "儿子阿斯顿因为工作关系\x01",
            "一直在关所驻守而不能回家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "孙子鲁克也是\x01",
            "一天到晚只会玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连我也感到\x01",
            "真的很寂寞啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233B")

    label("loc_1BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1CA2")

    ChrTalk(
        0xFE,
        (
            "我家的鲁克和邻居家的帕特\x01",
            "性格完全是两个极端，\x01",
            "但两人却是好朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是鲁克能多学学\x01",
            "帕特的优点就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233B")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1D54")

    ChrTalk(
        0xFE,
        (
            "上次的主日学校\x01",
            "鲁克乖乖地去了，\x01",
            "这孩子很少这样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道是不是\x01",
            "有什么开心的事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233B")

    label("loc_1D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4A")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "我儿子是王国军的士兵哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前曾在王都的部队，\x01",
            "现在驻守在\x01",
            "西面的威尔特关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望他回来后\x01",
            "好好教训教训鲁克。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8F")

    label("loc_1E4A")


    ChrTalk(
        0xFE,
        (
            "希望儿子回来后\x01",
            "好好教训教训鲁克。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8F")

    Jump("loc_233B")

    label("loc_1E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(
        0xFE,
        (
            "鲁克今天还是\x01",
            "飞快地冲出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他有好好地\x01",
            "吸取上次的教训吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233B")

    label("loc_1F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_20B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2015")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "我最近太娇惯\x01",
            "鲁克这孩子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "没有想到他不仅不回家，\x01",
            "还跑到翡翠之塔去玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果不是因为有\x01",
            "游击士及时赶到……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B4")

    label("loc_2015")


    ChrTalk(
        0xA,
        (
            "这都是因为我\x01",
            "太娇惯他的缘故啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "等我儿子回来之后，\x01",
            "一定要好好商量一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B4")

    Jump("loc_233B")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_227A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BE")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "鲁克就算是回家了，\x01",
            "不一会儿又会飞跑出去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "马上就到\x01",
            "吃饭的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "真是一个静不下来的孩子啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_21BE")


    ChrTalk(
        0xA,
        (
            "鲁克就算是回家了，\x01",
            "不一会儿又会飞跑出去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "真是一个静不下来的孩子啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2277")

    Jump("loc_233B")

    label("loc_227A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EA")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        "那个孩子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "鲁克那孩子\x01",
            "到底跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "早饭也没有吃\x01",
            "就飞跑了出去……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233B")

    label("loc_22EA")


    ChrTalk(
        0xA,
        (
            "鲁克那孩子\x01",
            "到底跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "早饭也没有吃\x01",
            "就飞跑了出去……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233B")

    TalkEnd(0xA)
    Return()

    # Function_9_1B21 end

    def Function_10_233F(): pass

    label("Function_10_233F")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2413")
    OP_A2(0x4)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xB,
        "哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还是要谢谢\x01",
            "你们救了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "而且……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "虽然不服气，\x01",
            "但艾丝蒂尔你真的很厉害哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "虽然还远远比不上\x01",
            "卡西乌斯叔叔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244F")

    label("loc_2413")


    ChrTalk(
        0xB,
        "决定了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我一定要\x01",
            "成为一名游击士！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_244F")

    TalkEnd(0xB)
    Return()

    # Function_10_233F end

    def Function_11_2453(): pass

    label("Function_11_2453")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "桌子上放着一个笔记本。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2506")
    OP_B9(0x376, 0x0)

    label("loc_2506")

    TalkEnd(0xFF)
    Return()

    # Function_11_2453 end

    SaveToFile()

Try(main)
