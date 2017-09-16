from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4252   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4252.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '赫穆特',                               # 9
        '达扬',                                 # 10
        '托克斯',                               # 11
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH01220 ._CH',             # 03
        'ED6_DT07/CH01570 ._CH',             # 04
        'ED6_DT07/CH01560 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH01220P._CP',             # 03
        'ED6_DT07/CH01570P._CP',             # 04
        'ED6_DT07/CH01560P._CP',             # 05
    )

    DeclNpc(
        X                   = -63080,
        Z                   = 0,
        Y                   = -37950,
        Direction           = 260,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -61160,
        Z                   = 0,
        Y                   = -35120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -67120,
        Z                   = 0,
        Y                   = -32000,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_236",          # 01, 1
        "Function_2_250",          # 02, 2
        "Function_3_266",          # 03, 3
        "Function_4_414",          # 04, 4
        "Function_5_797",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_164")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_178")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_1BB")

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_182")
    Jump("loc_1BB")

    label("loc_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_196")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_1BB")

    label("loc_196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1AA")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_1BB")

    label("loc_1AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1B4")
    Jump("loc_1BB")

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_1BB")

    label("loc_1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1C5")
    Jump("loc_235")

    label("loc_1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1D4")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_235")

    label("loc_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1DE")
    Jump("loc_235")

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_235")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1F2")
    Jump("loc_235")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1FC")
    Jump("loc_235")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_206")
    Jump("loc_235")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_210")
    Jump("loc_235")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_235")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_224")
    Jump("loc_235")

    label("loc_224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_22E")
    Jump("loc_235")

    label("loc_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_235")

    label("loc_235")

    Return()

    # Function_0_13A end

    def Function_1_236(): pass

    label("Function_1_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_246")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_246")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_236 end

    def Function_2_250(): pass

    label("Function_2_250")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_265")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_250")

    label("loc_265")

    Return()

    # Function_2_250 end

    def Function_3_266(): pass

    label("Function_3_266")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_273")
    Jump("loc_410")

    label("loc_273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_31F")

    ChrTalk(
        0xFE,
        (
            "外出休假的人员\x01",
            "终于回到城里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在开始可有的忙了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_410")

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_329")
    Jump("loc_410")

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_333")
    Jump("loc_410")

    label("loc_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_35A")

    ChrTalk(
        0xFE,
        "呼，今天又要加班了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_410")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_410")

    ChrTalk(
        0xFE,
        (
            "唉，不管怎么说，\x01",
            "现在的人手是不足以完成任务的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其他的人\x01",
            "都被公爵以休假的名义\x01",
            "给赶出城去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410")

    TalkEnd(0xFE)
    Return()

    # Function_3_266 end

    def Function_4_414(): pass

    label("Function_4_414")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_421")
    Jump("loc_793")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4C3")

    ChrTalk(
        0xFE,
        (
            "呼，政变残留问题的处理\x01",
            "和一些手头的工作简直堆积如山。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天又只有加班了……\x01",
            "在王城里做事太辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_793")

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_4CD")
    Jump("loc_793")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_793")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_63F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_569")

    ChrTalk(
        0xFE,
        (
            "呜呜……\x01",
            "只是想象一下公爵大权在握的样子，\x01",
            "就感到一阵寒意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C")

    label("loc_569")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "虽说公爵是女王陛下的代理人，\x01",
            "但做出决定性指示的却是情报部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有理查德上校的话，\x01",
            "还不知道会变成什么样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C")

    Jump("loc_793")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_793")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6DD")

    ChrTalk(
        0xFE,
        (
            "这里是处理利贝尔王国\x01",
            "政务的重要办公地点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在女王陛下病了，\x01",
            "但仍然接受杜南公爵的指示\x01",
            "来执行公务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_793")

    label("loc_6DD")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "这里是行政区域。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是处理利贝尔王国\x01",
            "政务的重要办公地点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在女王陛下病了，\x01",
            "但仍然接受杜南公爵的指示\x01",
            "来执行公务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_793")

    TalkEnd(0xFE)
    Return()

    # Function_4_414 end

    def Function_5_797(): pass

    label("Function_5_797")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7F6")

    ChrTalk(
        0xFE,
        (
            "唉，我最喜欢的钓鱼\x01",
            "看来也暂时没空去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B9")

    label("loc_7F6")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "今天开始\x01",
            "又要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为公爵经常无所事事，\x01",
            "我还以为可以一直休息了，\x01",
            "没想到竟然发生了那么多事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来要收拾残局\x01",
            "可是要花相当的功夫呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    Jump("loc_91D")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8C6")
    Jump("loc_91D")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_91D")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8DA")
    Jump("loc_91D")

    label("loc_8DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8E4")
    Jump("loc_91D")

    label("loc_8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8EE")
    Jump("loc_91D")

    label("loc_8EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8F8")
    Jump("loc_91D")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_902")
    Jump("loc_91D")

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_90C")
    Jump("loc_91D")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_916")
    Jump("loc_91D")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_91D")

    label("loc_91D")

    TalkEnd(0xFE)
    Return()

    # Function_5_797 end

    SaveToFile()

Try(main)
