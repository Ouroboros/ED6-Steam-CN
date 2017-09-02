from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2512   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '乔儿',                                 # 9
        '碧欧拉老师',                           # 10
        '艾福托老师',                           # 11
        '雅莉丝',                               # 12
        '帕布尔',                               # 13
        '亚吉鲁',                               # 14
        '德尼斯',                               # 15
        '芙拉瑟',                               # 16
        '蕾娜',                                 # 17
        'CH22000',                              # 18
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH01210 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01590 ._CH',             # 03
        'ED6_DT07/CH01090 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01370 ._CH',             # 07
        'ED6_DT06/CH20100 ._CH',             # 08
        'ED6_DT06/CH20109 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH01210P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01590P._CP',             # 03
        'ED6_DT07/CH01090P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01370P._CP',             # 07
        'ED6_DT06/CH20100P._CP',             # 08
        'ED6_DT06/CH20109P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
        Direction           = 90,
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
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -60350,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 0,
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
        X                   = -60450,
        Z                   = 0,
        Y                   = 30850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28710,
        Z                   = 0,
        Y                   = 25280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -31400,
        Z                   = 0,
        Y                   = -800,
        Direction           = 90,
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
        X                   = -63000,
        Z                   = 0,
        Y                   = -3700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -61500,
        Z                   = 0,
        Y                   = -3700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -28640,
        Z                   = 700,
        Y                   = 31090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835018,
        ChipIndex           = 0xA,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -28640,
        TriggerZ            = 700,
        TriggerY            = 31090,
        TriggerRange        = 1000,
        ActorX              = -28640,
        ActorZ              = 1000,
        ActorY              = 31090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_3D6",          # 01, 1
        "Function_2_423",          # 02, 2
        "Function_3_5A0",          # 03, 3
        "Function_4_691",          # 04, 4
        "Function_5_956",          # 05, 5
        "Function_6_99D",          # 06, 6
        "Function_7_AB9",          # 07, 7
        "Function_8_E61",          # 08, 8
        "Function_9_FE7",          # 09, 9
        "Function_10_14C0",        # 0A, 10
        "Function_11_1989",        # 0B, 11
        "Function_12_2979",        # 0C, 12
        "Function_13_2C7B",        # 0D, 13
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2AB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58560, 0, -1150, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -60740, 0, 750, 180)
    Jump("loc_380")

    label("loc_2AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2B5")
    Jump("loc_380")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2BF")
    Jump("loc_380")

    label("loc_2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2C9")
    Jump("loc_380")

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_322")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -119550, 0, 30420, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 29320, 0, 27850, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_380")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 29790, 0, 30750, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_380")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_35B")
    Jump("loc_380")

    label("loc_35B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_365")
    Jump("loc_380")

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_374")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_380")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_380")
    ClearChrFlags(0xC, 0x80)

    label("loc_380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_390")
    SetChrFlags(0x11, 0x80)

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 11)
    OP_B1("T2512_k")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 12)
    OP_B1("t2512_n")

    label("loc_3D5")

    Return()

    # Function_0_266 end

    def Function_1_3D6(): pass

    label("Function_1_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F7")
    OP_B1("t2512_y")
    Jump("loc_400")

    label("loc_3F7")

    OP_B1("t2512_n")

    label("loc_400")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_413")
    OP_65(0x0, 0x1)

    label("loc_413")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_422")
    OP_64(0x0, 0x1)

    label("loc_422")

    Return()

    # Function_1_3D6 end

    def Function_2_423(): pass

    label("Function_2_423")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_58A")

    label("loc_448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_58A")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_58A")

    label("loc_47A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_58A")

    label("loc_493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_58A")

    label("loc_4AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_58A")

    label("loc_4C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_58A")

    label("loc_4DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_58A")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_58A")

    label("loc_510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_58A")

    label("loc_529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_58A")

    label("loc_542")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_58A")

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_58A")

    label("loc_574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_58A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58A")

    label("loc_59F")

    Return()

    # Function_2_423 end

    def Function_3_5A0(): pass

    label("Function_3_5A0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "难道大家都还在练习吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "差不多该回房间休息，\x01",
            "为明天做准备了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68D")

    label("loc_60D")


    ChrTalk(
        0xFE,
        (
            "难道他们\x01",
            "还留在校园里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "还有一些同学\x01",
            "没回宿舍去呢………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D")

    TalkEnd(0x9)
    Return()

    # Function_3_5A0 end

    def Function_4_691(): pass

    label("Function_4_691")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_8DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_793")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_712")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哦，刚才辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在事态扩大之前解决了，\x01",
            "实在太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790")

    label("loc_712")


    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "真拿米克那家伙没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，在下次体育课上\x01",
            "我要好好锻炼他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790")

    Jump("loc_8D9")

    label("loc_793")


    ChrTalk(
        0xFE,
        (
            "刚才有个学生\x01",
            "说要找大道具的材料，\x01",
            "来借走了旧校舍的钥匙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "已经有段时间了，\x01",
            "怎么还没回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没回房间的住宿生还有很多，\x01",
            "在宿舍关门之前还是去巡视一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D9")

    Jump("loc_952")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_952")

    ChrTalk(
        0xFE,
        (
            "学院的宿舍\x01",
            "都是由老师担当宿管的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "咳咳！\x01",
            "男生宿舍的宿管就是我了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_952")

    TalkEnd(0xA)
    Return()

    # Function_4_691 end

    def Function_5_956(): pass

    label("Function_5_956")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "今天一天又要结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "接下来做什么呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_5_956 end

    def Function_6_99D(): pass

    label("Function_6_99D")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F9")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "啊，科洛丝前辈，还有艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "明天的舞台剧，你们要好好加油啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A35")

    label("loc_9F9")


    ChrTalk(
        0xFE,
        (
            "我很喜欢历史，\x01",
            "而且对戏剧的背景设定很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A35")

    Jump("loc_AB5")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_AB5")

    ChrTalk(
        0xFE,
        (
            "今天刚买的小说，\x01",
            "一定要好好读一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的理想是做个小说家，\x01",
            "所以选择了人文系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB5")

    TalkEnd(0xC)
    Return()

    # Function_6_99D end

    def Function_7_AB9(): pass

    label("Function_7_AB9")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_C05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCB")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼呼，\x01",
            "快点到晚上吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我偏好安静，\x01",
            "所以特别喜欢黑暗的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "洗澡时我也喜欢\x01",
            "漆黑一片的浴室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为让我感到很安静。\x01",
            "有机会你们也试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C02")

    label("loc_BCB")


    ChrTalk(
        0xFE,
        (
            "呼呼，\x01",
            "快点到晚上吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C02")

    Jump("loc_E5D")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D55")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼呼呼……\x01",
            "天马上就要黑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们知道吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从这里向北走\x01",
            "有一间学院的旧校舍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "旧校舍是用以前的要塞改建的，\x01",
            "原来好像是个战场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……你不觉得\x01",
            "那里也许会出现鬼怪吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506F………是吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DDB")

    label("loc_D55")


    ChrTalk(
        0xFE,
        (
            "旧校舍是用\x01",
            "以前的要塞改建的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你不觉得\x01",
            "那里也许会出现鬼怪吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDB")

    Jump("loc_E5D")

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_E5D")

    ChrTalk(
        0xFE,
        "学园祭快要到了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须要开始准备\x01",
            "社团的摊位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D")

    TalkEnd(0xD)
    Return()

    # Function_7_AB9 end

    def Function_8_E61(): pass

    label("Function_8_E61")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_F06")

    ChrTalk(
        0xFE,
        (
            "照我的经验来看，\x01",
            "复习比预习更有效果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "复习三小时，\x01",
            "预习两小时是我每天的必修课。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE3")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_F56")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我差不多该去休息了哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "糟、糟了……\x01",
            "不知不觉就用上演戏的语气了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE3")

    label("loc_F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_FE3")

    ChrTalk(
        0xFE,
        (
            "我一直专心于学习，\x01",
            "舞台剧方面都没怎么排练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～而且我还是演员，\x01",
            "不会出洋相吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE3")

    TalkEnd(0xE)
    Return()

    # Function_8_E61 end

    def Function_9_FE7(): pass

    label("Function_9_FE7")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_112D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AB")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "现在开始是美术部的活动时间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正要回宿舍\x01",
            "去拿道具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……这可不能忘了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_112A")

    label("loc_10AB")


    ChrTalk(
        0xFE,
        (
            "我正要回宿舍\x01",
            "去拿道具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……这可不能忘了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_112A")

    Jump("loc_14BC")

    label("loc_112D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_14BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146A")
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0x10, 255)

    ChrTalk(
        0xF,
        (
            "呼，\x01",
            "果然是激动人心的一周啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "戏剧的练习，美术社团的摊位准备，\x01",
            "还有帮忙班级展示………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "全部都处理完了呀，\x01",
            "哇，好棒，很厉害嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "……这还不都是\x01",
            "被你逼着做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "舞台剧方面\x01",
            "我本来还想拒绝的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "可是，\x01",
            "是你自己抢下主教这个角色的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "这是当然的啦！\x01",
            "难道让我演一般平民？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "要干就要好好干。\x01",
            "可惜主角已经有人选了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "哇哇，真是伟大。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "……真是的，\x01",
            "蕾娜老是这样为难我。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0x10, 255)
    Jump("loc_14BC")

    label("loc_146A")


    ChrTalk(
        0xFE,
        (
            "……真是的，\x01",
            "蕾娜老是这样为难我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BC")

    TalkEnd(0xF)
    Return()

    # Function_9_FE7 end

    def Function_10_14C0(): pass

    label("Function_10_14C0")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_15DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A4")
    OP_A2(0x7)
    OP_4A(0xF, 255)

    ChrTalk(
        0x10,
        (
            "嗯，只要是人，\x01",
            "总会有忘记的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_153E():
        TurnDirection(0xF, 0x10, 1500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_153E)

    ChrTalk(
        0xF,
        "哎呀！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "呼，不快点的话\x01",
            "活动时间就要结束了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xF, 255)
    OP_8C(0xF, 90, 6000)
    Jump("loc_15DB")

    label("loc_15A4")


    ChrTalk(
        0xFE,
        (
            "只要是人，\x01",
            "总会有忘记的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DB")

    Jump("loc_1985")

    label("loc_15DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1985")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191B")
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0xF, 255)

    ChrTalk(
        0xF,
        (
            "呼，\x01",
            "果然是激动人心的一周啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "戏剧的练习，美术社团的摊位准备，\x01",
            "还有帮忙班级展示………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "全部都处理完了呀，\x01",
            "哇，好棒，很厉害嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "……这还不都是\x01",
            "被你逼着做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "舞台剧方面\x01",
            "我本来还想拒绝的呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "演出不是更好吗，\x01",
            "你自己抢下主教这个角色的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "这是当然的啦！\x01",
            "难道让我演一般平民？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "要干就要好好干。\x01",
            "可惜主角已经有人选了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "哇哇，不错不错。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "……真是的，\x01",
            "蕾娜老是这样为难我。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_1985")

    label("loc_191B")


    ChrTalk(
        0xFE,
        (
            "看着芙拉瑟的成长\x01",
            "是我的一种乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1985")

    TalkEnd(0x10)
    Return()

    # Function_10_14C0 end

    def Function_11_1989(): pass

    label("Function_11_1989")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(-120390, 0, -2060, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -121640, 0, -4360, 0)
    SetChrPos(0x105, -122120, 0, -3050, 180)
    SetChrPos(0x8, -121110, 0, -2820, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#040F#3P……那么，艾丝蒂尔。\x01",
            "这段时间你就睡这张床吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F谢啦⊙\x02\x03",
            "#501F不过，原来科洛丝和\x01",
            "乔儿会长是住同一房间的啊。\x02\x03",
            "难怪关系这么好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#041F#3P呵呵……\x01",
            "自从来了学院之后，我们就是朋友了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F#1P不过呢，作为室友来说，\x01",
            "我们恐怕算是一对冤家哦。\x02\x03",
            "#644F对了，艾丝蒂尔。\x01",
            "我这里有一个提议……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#648F#1P你呢，以后直接\x01",
            "叫我乔儿就可以了。\x02\x03",
            "加上『会长』的话，\x01",
            "听起来总觉得好见外～\x02\x03",
            "我也直接叫你艾丝蒂尔，\x01",
            "以后大家就是好朋友哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈……\x01",
            "嗯，那我们以后就是好朋友啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F#3P我觉得这提议也不错，\x01",
            "大家以后就互相直呼名字吧。\x02\x03",
            "那样感觉比较自然……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F是吗，那我就不客气了……\x02\x03",
            "#001F乔儿，科洛丝。\x01",
            "这段时间就请你们多多关照啦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F#3P嗯，也请你多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#641F#1P反正这里全是女生，\x01",
            "我们就过得随意一点行了。\x02\x03",
            "只要是在这幢楼里，\x01",
            "就不用担心会被男生看到哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        (
            "#045F虽然话是这么说，\x01",
            "不过太随意的话也不太好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(
        0x8,
        (
            "#645F#1P哎～所以我就说，\x01",
            "好孩子是最麻烦的了。\x02\x03",
            "成天在装正经。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F啊，你好过分呢。\x02\x03",
            "会说这种话的孩子，\x01",
            "我就算做了糕点也不会分给她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#643F#1P啊，不要啊不要啊。\x02\x03",
            "科洛丝大人。\x01",
            "请饶恕在下刚才的无礼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F不～行，要好好反省。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#044F#3P哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#640F#1P怎么了，艾丝蒂尔？\x01",
            "这样呆呆地盯着我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊哈哈，没什么～……\x01",
            "其实我挺羡慕你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#643F#1P羡慕？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我在洛连特\x01",
            "虽然也有很要好的朋友……\x02\x03",
            "不过顶多也就是\x01",
            "到对方的家里过过夜罢了。\x02\x03",
            "#001F像你们这样，可以和\x01",
            "意气相投的朋友一起生活真好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)
    OP_63(0x105)

    ChrTalk(
        0x8,
        "#642F#1P……科洛丝，你怎么想？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#3P要我该怎么说好呢……\x02\x03",
            "被艾丝蒂尔羡慕，\x01",
            "我觉得有点不能理解啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#646F#1P啊，果然是吧。\x02\x03",
            "你知道自己在说什么吗。\x01",
            "我都不明白你要羡慕些什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F为、为什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#645F#1P我说你啊……\x02\x03",
            "你知道自己\x01",
            "是在跟谁一起旅行吗？\x02\x03",
            "在家里的时候，\x01",
            "是在跟谁住在同一屋檐下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎？……这个。\x02\x03",
            "难道是在说约修亚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#045F#3P用不着难道你也知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#644F#1P和那样棒的帅哥形影不离，\x01",
            "却还要来羡慕女生宿舍，\x01",
            "艾丝蒂尔你也真是的……\x02\x03",
            "不觉得太暴殄天物了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F真是的～你们说什么呀。\x02\x03",
            "#006F其实我和约修亚\x01",
            "纯粹是情同姐弟的关系。\x02\x03",
            "这么多年来，\x01",
            "我们都是像家人一样生活在一起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#649F#1P嘿嘿，像家人一样吗……\x02\x03",
            "就算你这么认为，\x01",
            "那约修亚又是怎么想的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#659F#1P像他这种年纪的男孩，\x01",
            "太过压抑自己的感情可是不好哦。\x02\x03",
            "更何况身边有一个\x01",
            "又健康又漂亮的女孩子，\x01",
            "我想他一定忍得很辛苦吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        "#043F说够了没有，乔儿！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#045F#3P不好意思，艾丝蒂尔。\x02\x03",
            "她一得意起来就会拿别人开玩笑,\x01",
            "这是她的坏习惯，你要多多包涵哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(
        0x8,
        (
            "#646F#1P哼～哼～\x01",
            "那什么才不叫坏习惯啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        "#042F你有意见吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#641F#1P哎呀，一点都没有呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊、啊哈哈……\x02\x03",
            "真是的～别吓我嘛。\x02\x03",
            "#503F这种事，怎么可能嘛。\x01",
            "居然说约修亚他会对我……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#649F#1P意识到了、意识到了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F乔儿！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        (
            "#643F#1P啊，我忘记了。\x01",
            "睡前得把当日报告交给老师。\x02\x03",
            "#648F那么，晚安。\x01",
            "你们两个先睡好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_271D():
        OP_6D(-121140, 0, -5760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_271D)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrFlags(0x8, 0x4)

    def lambda_274C():

        label("loc_274C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_274C")

    QueueWorkItem2(0x101, 2, lambda_274C)

    def lambda_275D():

        label("loc_275D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_275D")

    QueueWorkItem2(0x105, 2, lambda_275D)
    OP_8E(0x8, 0xFFFE27BC, 0x0, 0xFFFFF18C, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFE2906, 0x0, 0xFFFFDECC, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_279B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_279B)
    OP_8E(0x8, 0xFFFE28FC, 0x0, 0xFFFFD9A4, 0xBB8, 0x0)
    Sleep(200)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x105,
        "#043F真是的……\x02",
    )

    CloseMessageWindow()
    OP_6D(-120390, 0, -2060, 1500)

    ChrTalk(
        0x105,
        (
            "#045F#1P对了，艾丝蒂尔。\x02\x03",
            "如果不介意的话，\x01",
            "你这段时间就穿我的睡衣吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#503F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F#1P艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    OP_9E(0x101, 0x32, 0x0, 0x12C, 0x1770)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 350, 400)

    ChrTalk(
        0x101,
        (
            "#008F啊，啊啊，睡衣是吧。\x02\x03",
            "嗯，就随便借一件给我行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，艾丝蒂尔和约修亚的校园生活\x01",
            "以一种意想不到的形式展开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapFlags(0x10000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2512   ._SN", 115, 0, 1)
    IdleLoop()
    Return()

    # Function_11_1989 end

    def Function_12_2979(): pass

    label("Function_12_2979")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_72(0x8, 0x20)
    OP_6F(0x8, 15)
    OP_72(0xA, 0x20)
    OP_6F(0xA, 15)
    OP_6D(-118900, 0, -2700, 0)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x101, 0x258, 1200, 0x1C, 0x21, 0xFA, 0x0)
    OP_62(0x8, 0x12C, 1750, 0x1C, 0x21, 0xFA, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x105, -118840, 0, -3930, 180)
    SetChrPos(0x101, -118500, 500, -5400, 0)
    SetChrPos(0x8, -118550, 100, 300, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x8, 8)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101)
    SetChrSubChip(0x101, 15)
    Sleep(50)
    SetChrSubChip(0x101, 16)
    Sleep(1000)

    def lambda_2A6F():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A6F)
    Sleep(50)
    OP_6F(0xA, 15)
    OP_70(0xA, 0x14)
    Sleep(1000)
    OP_62(0x101, 0x64, 1500, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x105, 270, 400)

    def lambda_2AB0():
        OP_6D(-118800, 0, -930, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2AB0)
    OP_8E(0x105, 0xFFFE297E, 0x0, 0xFFFFF060, 0xBB8, 0x0)
    OP_8E(0x105, 0xFFFE29A6, 0x0, 0xFFFFFBF0, 0xBB8, 0x0)
    OP_8E(0x105, 0xFFFE2FBE, 0x0, 0xFFFFFC0E, 0xBB8, 0x0)
    OP_8C(0x105, 0, 400)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101)
    Sleep(1000)

    def lambda_2B2A():
        OP_99(0xFE, 0x7, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B2A)
    Sleep(100)
    OP_6F(0xA, 20)
    OP_70(0xA, 0xF)
    WaitChrThread(0x101, 0x1)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_62(0x101, 0x258, 1200, 0x1C, 0x21, 0xFA, 0x0)
    TurnDirection(0x105, 0x101, 400)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1200)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x105, 270, 400)
    FadeToDark(2000, 0, -1)

    def lambda_2BBC():
        OP_6D(-118900, 0, -2700, 1500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2BBC)
    OP_8E(0x105, 0xFFFE29A6, 0x0, 0xFFFFFBF0, 0xDAC, 0x0)
    OP_8E(0x105, 0xFFFE297E, 0x0, 0xFFFFF060, 0xDAC, 0x0)
    OP_8E(0x105, 0xFFFE2FC8, 0x0, 0xFFFFF0A6, 0xDAC, 0x0)
    OP_8C(0x105, 180, 400)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "早上，他们和学院的同辈伙伴们\x01",
            "一起起床，然后一起上学……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2510   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2979 end

    def Function_13_2C7B(): pass

    label("Function_13_2C7B")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x11, 0x80)
    OP_64(0x0, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "卢安经济史·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33F, 1)
    OP_28(0x27, 0x1, 0x100)
    TalkEnd(0xFF)
    Return()

    # Function_13_2C7B end

    SaveToFile()

Try(main)
