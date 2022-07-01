from ED6ScenarioHelper import *

def main():
    # 工房船莱普尼兹号

    CreateScenaFile(
        FileName            = 'E0012   ._SN',
        MapName             = 'event',
        Location            = 'E0012.x',
        MapIndex            = 232,
        MapDefaultBGM       = "ed60001",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/E0012   ._SN',
            'ED6_DT01/E0012_1 ._SN',
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
        '格斯塔夫维修长',                       # 9
        '雷曼',                                 # 10
        '菲',                                   # 11
        '伊格尔',                               # 12
        '安东尼',                               # 13
        '威尔姆',                               # 14
        '阿加特',                               # 15
        '提妲',                                 # 16
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
        Unknown_3A              = 232,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02440 ._CH',             # 00
        'ED6_DT06/CH20078 ._CH',             # 01
        'ED6_DT07/CH01550 ._CH',             # 02
        'ED6_DT07/CH01250 ._CH',             # 03
        'ED6_DT07/CH01700 ._CH',             # 04
        'ED6_DT07/CH01450 ._CH',             # 05
        'ED6_DT07/CH00050 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02440P._CP',             # 00
        'ED6_DT06/CH20078P._CP',             # 01
        'ED6_DT07/CH01550P._CP',             # 02
        'ED6_DT07/CH01250P._CP',             # 03
        'ED6_DT07/CH01700P._CP',             # 04
        'ED6_DT07/CH01450P._CP',             # 05
        'ED6_DT07/CH00050P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
    )

    DeclNpc(
        X                   = -37000,
        Z                   = -3800,
        Y                   = 145500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 115320,
        Z                   = 0,
        Y                   = 100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 117500,
        Z                   = 0,
        Y                   = 100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_2CA",          # 01, 1
        "Function_2_2E3",          # 02, 2
        "Function_3_460",          # 03, 3
        "Function_4_537",          # 04, 4
        "Function_5_60E",          # 05, 5
        "Function_6_761",          # 06, 6
        "Function_7_8DD",          # 07, 7
        "Function_8_8F4",          # 08, 8
        "Function_9_B3F",          # 09, 9
        "Function_10_E23",         # 0A, 10
        "Function_11_106A",        # 0B, 11
        "Function_12_16B1",        # 0C, 12
        "Function_13_246B",        # 0D, 13
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1F8")
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_206")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_218")

    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58980, -2000, 54010, 5)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 28040, 0, -7450, 270)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271")
    SetChrPos(0x8, 29550, 0, 8860, 90)
    Jump("loc_282")

    label("loc_271")

    SetChrPos(0x8, 32860, 0, 7250, 180)

    label("loc_282")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60760, -2000, 53780, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60590, 0, 3070, 265)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 88670, 0, -280, 81)
    Return()

    # Function_0_1EA end

    def Function_1_2CA(): pass

    label("Function_1_2CA")

    OP_10(0x0, 0x0)
    OP_22(0x7A, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_2E2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E2")

    Return()

    # Function_1_2CA end

    def Function_2_2E3(): pass

    label("Function_2_2E3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_44A")

    label("loc_308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_44A")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_44A")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_44A")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_44A")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_44A")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_44A")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_44A")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_44A")

    label("loc_3D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_44A")

    label("loc_3E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_44A")

    label("loc_402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_44A")

    label("loc_41B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_44A")

    label("loc_434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_44A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_44A")

    label("loc_45F")

    Return()

    # Function_2_2E3 end

    def Function_3_460(): pass

    label("Function_3_460")

    OP_A2(0x5CC)
    TalkBegin(0xFE)
    OP_4A(0xF, 255)

    ChrTalk(
        0xF,
        (
            "#061F#5P我说，阿加特大哥哥。\x01",
            "让我看看你的战术导力器吧。\x02\x03",
            "用这个简易测量器，\x01",
            "就可以看出哪里出问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#052F#6P啊啊，给你……\x02\x03",
            "#051F我说你啊。\x01",
            "一看到机械，眼神立刻就变了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)
    TalkEnd(0xFE)
    Return()

    # Function_3_460 end

    def Function_4_537(): pass

    label("Function_4_537")

    OP_A2(0x5CC)
    TalkBegin(0xFE)
    OP_4A(0xE, 255)

    ChrTalk(
        0xF,
        (
            "#061F#5P我说，阿加特大哥哥。\x01",
            "让我看看你的战术导力器吧。\x02\x03",
            "用这个简易测量器，\x01",
            "就可以看出哪里出问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#052F#6P啊啊，给你……\x02\x03",
            "#051F我说你啊。\x01",
            "一看到机械，眼神立刻就变了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    TalkEnd(0xFE)
    Return()

    # Function_4_537 end

    def Function_5_60E(): pass

    label("Function_5_60E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A0")

    ChrTalk(
        0xFE,
        (
            "#690F怎么了，\x01",
            "你们就这么担心这个集装箱吗？\x02\x03",
            "#691F我会好好安排的，\x01",
            "请放心地去休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756")

    label("loc_6A0")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#691F哦，怎么了？\x02\x03",
            "到雷斯顿要塞\x01",
            "要３０分钟左右的航程。\x02\x03",
            "集装箱的伪装做好之前\x01",
            "你们就先休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756")

    Jump("loc_75D")

    label("loc_759")

    Call(0, 13)

    label("loc_75D")

    TalkEnd(0xFE)
    Return()

    # Function_5_60E end

    def Function_6_761(): pass

    label("Function_6_761")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(
        0xFE,
        "快要到了呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "果然还是很紧张啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D9")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_861")

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "一想到博士被他们绑架了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我有点不寒而栗呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为如果不请教博士的话，\x01",
            "是不可能知道关于\x01",
            "『卡佩尔』的详细情况的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D9")

    label("loc_861")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "拉赛尔博士\x01",
            "竟然被绑架了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一直瞒着我们，\x01",
            "工房长也太不够意思了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是认为\x01",
            "我们不值得信任啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D9")

    TalkEnd(0xFE)
    Return()

    # Function_6_761 end

    def Function_7_8DD(): pass

    label("Function_7_8DD")

    TalkBegin(0xFE)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_8DD end

    def Function_8_8F4(): pass

    label("Function_8_8F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_962")

    ChrTalk(
        0xFE,
        (
            "就快能看见\x01",
            "雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们一定要加把劲哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9DC")
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(
        0xFE,
        (
            "喂，雷曼。\x01",
            "赶快修正一下航线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从瓦雷利亚湖吹来的风\x01",
            "把船尾吹得有些偏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_9DC")

    OP_A2(0x3)
    OP_A2(0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(
        0xFE,
        (
            "喂，雷曼。\x01",
            "往北北东方向偏离了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，真恼火！\x01",
            "赶快修正一下航线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就在现在，\x01",
            "说不定拉赛尔那家伙\x01",
            "正遭受着危险。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "哎呀，真是的！\x01",
            "伊格尔爷爷你就别说了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这样一直抱怨着，\x01",
            "我会分心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34")

    OP_8C(0xFE, 45, 400)
    TalkEnd(0xFE)
    Return()

    # Function_8_8F4 end

    def Function_9_B3F(): pass

    label("Function_9_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BA5")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "谢谢你们\x01",
            "特地给我送过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好、好了，\x01",
            "现在必须集中精神工作。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_BA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_BCF")
    Call(1, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CFE")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_C20")

    ChrTalk(
        0xFE,
        "集装箱的伪装工作已经完成了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能和计划一样\x01",
            "顺利进行就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFB")

    label("loc_C20")

    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(
        0xFE,
        (
            "好了，菲！\x01",
            "现在正是集中精力的时刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把鲁迪和布拉姆都忘掉，\x01",
            "赶快工作啊工作！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_C98")


    ChrTalk(
        0xFE,
        (
            "好了，菲！\x01",
            "现在正是集中精力的时刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "把个人的烦恼都忘掉，\x01",
            "赶快工作啊工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF6")

    ClearChrFlags(0xA, 0x10)

    label("loc_CFB")

    Jump("loc_E1F")

    label("loc_CFE")

    TalkBegin(0xFE)
    OP_A2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_D51")

    ChrTalk(
        0xFE,
        "集装箱的伪装工作已经完成了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能和计划一样\x01",
            "顺利进行就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1F")

    label("loc_D51")


    ChrTalk(
        0xFE,
        (
            "没想到，拉赛尔博士\x01",
            "竟然是被王国军绑架的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来\x01",
            "我们的使命就太重大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是伪装的集装箱暴露了，\x01",
            "不仅救出作战会失败，\x01",
            "中央工房也会受到牵连。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "必须要仔细再仔细啊。\x02",
    )

    CloseMessageWindow()

    label("loc_E1F")

    TalkEnd(0xFE)
    Return()

    # Function_9_B3F end

    def Function_10_E23(): pass

    label("Function_10_E23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_E82")

    ChrTalk(
        0xFE,
        (
            "虽然是经常走的航路，\x01",
            "不过今天还是相当紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "可千万不要露出破绽啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1066")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EFF")

    ChrTalk(
        0xFE,
        (
            "风的流向\x01",
            "我早就知道啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我觉得\x01",
            "比起风的流向，\x01",
            "老爷子你才更让我担心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1066")

    label("loc_EFF")

    OP_A2(0x1)
    OP_A2(0x3)
    OP_4A(0xB, 255)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x9, 400)

    ChrTalk(
        0xB,
        (
            "喂，雷曼。\x01",
            "往北北东方向偏离了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "啊啊，真恼火！\x01",
            "赶快修正一下航线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "就在现在，\x01",
            "说不定拉赛尔那家伙\x01",
            "正遭受着危险。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "哎呀，真是的！\x01",
            "伊格尔爷爷你就别说了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一直抱怨着，\x01",
            "我会分心的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)
    OP_4B(0xB, 255)

    label("loc_1066")

    TalkEnd(0xFE)
    Return()

    # Function_10_E23 end

    def Function_11_106A(): pass

    label("Function_11_106A")

    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(29240, 0, 7250, 0)
    OP_67(0, 10730, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28810, 0, 8640, 90)
    SetChrPos(0x101, 29240, 0, 7250, 90)
    SetChrPos(0x102, 28260, 0, 6830, 90)
    SetChrPos(0x106, 29420, 0, 6290, 45)
    SetChrPos(0x107, 28480, 0, 6070, 45)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#691F这个就是给你们藏身的集装箱。\x01",
            "　\x02\x03",
            "藏四个人可能有点挤，\x01",
            "不过就稍微忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#6P是这样吗？\x01",
            "可是这个集装箱看起来很大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#693F哈哈～因为大部分要用来伪装，\x01",
            "所以空的地方可是连一半都不到啊。\x02\x03",
            "啊哈哈……\x01",
            "一起钻进去的话会很挤哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#6P原来是这样啊，那还真是狭小。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没关系，只要姿势协调的话，\x01",
            "用作藏身还是绰绰有余的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F这就足够了。\x01",
            "现在可不是讲究舒服的时候。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(
        0x106,
        (
            "#050F对了，大叔。\x01",
            "有修理战术导力器的设备吗？\x02\x03",
            "我的导力器有点不好使，\x01",
            "想趁现在调整一下……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13DF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13DF)

    def lambda_13ED():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13ED)

    def lambda_13FB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13FB)
    TurnDirection(0x8, 0x106, 400)

    ChrTalk(
        0x8,
        (
            "#691F啊，里面的工房设施里有，\x01",
            "你们可以随时到那去整理。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        (
            "#560F啊……\x01",
            "我也一起去调整感应阻碍器。\x02\x03",
            "阿加特大哥哥，请走这边。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    def lambda_14DE():

        label("loc_14DE")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_14DE")

    QueueWorkItem2(0x106, 1, lambda_14DE)

    ChrTalk(
        0x106,
        "#052F啊，嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_1508():

        label("loc_1508")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1508")

    QueueWorkItem2(0x101, 1, lambda_1508)

    def lambda_1519():

        label("loc_1519")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1519")

    QueueWorkItem2(0x102, 1, lambda_1519)
    OP_8E(0x107, 0x7580, 0x0, 0xEB0, 0xBB8, 0x0)

    def lambda_153E():
        OP_8E(0xFE, 0x751C, 0x0, 0xFFFFE912, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_153E)
    OP_8E(0x106, 0x751C, 0x0, 0xD98, 0xBB8, 0x0)

    def lambda_156D():
        OP_8E(0xFE, 0x751C, 0x0, 0xFFFFE912, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_156D)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_1595():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1595)

    def lambda_15A3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A3)

    ChrTalk(
        0x8,
        (
            "#691F到雷斯顿要塞的航程\x01",
            "大约需要３０分钟左右的时间。\x02\x03",
            "我也要将给集装箱做一下伪装工作，\x01",
            "在那之前，你们先休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#6P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那就有劳维修长你们了。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x106, 29240, 0, 7250, 0)
    SetChrPos(0x107, 29240, 0, 7250, 0)
    OP_4B(0x8, 255)
    OP_A2(0x561)
    EventEnd(0x0)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x6, 0xFF)
    Return()

    # Function_11_106A end

    def Function_12_16B1(): pass

    label("Function_12_16B1")

    EventBegin(0x0)
    AddParty(0x5, 0xFF)
    AddParty(0x6, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(116590, 0, 5710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x106, 115790, 0, 4200, 0)
    SetChrPos(0x107, 115590, 0, 5610, 90)
    OP_89(0x101, 113320, -2000, 7580, 0)
    OP_89(0x102, 113320, -2000, 7580, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        (
            "#061F#5P嘿咻～\x01",
            "好了，这样就没问题了。\x02\x03",
            "还好是小问题～～\x01",
            "只是结晶链连接部分的齿轮松了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F真是……\x01",
            "老爱多管闲事的小鬼。\x02\x03",
            "这种程度的修理，\x01",
            "我自己也做得到嘛。\x02\x03",
            "#051F不过，还是谢了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        (
            "#061F#5P嘿嘿……\x01",
            "你太客气了。\x02\x03",
            "#063F啊，说起来……\x01",
            "身体已经不要紧了吧？\x02\x03",
            "有没有不舒服的感觉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F啊，没事了。\x01",
            "根本用不着那么担心。\x02\x03",
            "#050F与其花时间担心别人，\x01",
            "还不如先为自己打算一下吧。\x02\x03",
            "到现在还没有回去的念头吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F#5P我、我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F不要误会了。\x01",
            "既然你决定了，我也不想再说什么。\x02\x03",
            "只是……你不觉得害怕吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F#5P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F虽说这是为了救爷爷，\x01",
            "但我们可是要私闯军事设施啊。\x02\x03",
            "要知道你只是个小鬼，\x01",
            "还没到承受这么大的重担的年纪吧。\x02\x03",
            "为什么能这样满不在乎地跟来？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#562F#5P这、这个……\x02\x03",
            "说实话，我真的很害怕……\x01",
            "　\x02\x03",
            "#560F但是但是，\x01",
            "有艾丝蒂尔姐姐和约修亚哥哥在……\x02\x03",
            "而且还有阿加特大哥哥……\x02\x03",
            "这样我就觉得安心大于害怕了。\x01",
            "　\x02\x03",
            "#067F嘿嘿……\x01",
            "可能是我有点迟钝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F…………………………\x02\x03",
            "#051F呵呵。\x01",
            "不是有点，是相当迟钝。\x02\x03",
            "看来担心你也是多余的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F#5P嘿嘿……不好意思。\x02\x03",
            "#060F……………………………\x02\x03",
            "#560F那、那个……\x01",
            "有件事我可以问问吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052F什么事，突然这么问？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F#5P嗯，那个……\x02\x03",
            "米夏，是谁呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#057F你怎么知道这个名字？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F#5P那、那个那个……\x02\x03",
            "阿加特大哥哥昨晚昏迷的时候\x01",
            "是这样叫我的呢……\x01",
            "　\x02\x03",
            "#063F……对不起，\x01",
            "是不能问的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F不……\x01",
            "也没什么好隐瞒的。\x02\x03",
            "#050F米夏……是我的妹妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F#5P哇，阿加特是哥哥啊。\x01",
            "　\x02\x03",
            "#061F那么你妹妹有多大呢？\x02\x03",
            "应该比我大吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F唔……这个嘛。\x02\x03",
            "#051F我想应该和你的年纪差不多吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F#5P？？？\x02\x03",
            "嗯……\x01",
            "你不常和妹妹见面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F啊，因为我这职业的关系。\x02\x03",
            "只有每年回乡的时候才能见她一次。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F#5P是这样啊……\x02\x03",
            "……米夏她，\x01",
            "真是有点可怜呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F怎、怎么了啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F#5P因为……我要是也有个\x01",
            "像阿加特大哥哥这样的哥哥，\x01",
            "我一定会想经常和他在一起的……\x02\x03",
            "#062F总、总之……\x01",
            "我有点同情米夏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#055F是、是吗……\x02\x03",
            "#552F不过，的确也是。\x02\x03",
            "要是我那时能像这样强的话，\x01",
            "也许大家就能一直在一起了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F#5P咦……？\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("乘务员的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本飞艇马上\x01",
            "就要到达雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请各位游击士\x01",
            "尽快到货舱集合。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x106,
        "#052F哦，差不多是时候了……\x02",
    )

    CloseMessageWindow()
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)

    def lambda_211F():

        label("loc_211F")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_211F")

    QueueWorkItem2(0x101, 1, lambda_211F)

    def lambda_2130():

        label("loc_2130")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_2130")

    QueueWorkItem2(0x102, 1, lambda_2130)

    def lambda_2141():
        OP_6D(114220, 0, 4820, 1500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2141)

    def lambda_2159():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2159)

    def lambda_216B():
        OP_8E(0xFE, 0x1BB48, 0x0, 0xD8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_216B)

    def lambda_2186():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2186)
    OP_8E(0x102, 0x1B832, 0x0, 0x10A4, 0x7D0, 0x0)

    def lambda_21AC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_21AC)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        "#501F啊，找到了。\x02",
    )

    CloseMessageWindow()

    def lambda_21DD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_21DD)

    def lambda_21EB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_21EB)

    def lambda_21F9():
        OP_8E(0xFE, 0x1BFEE, 0x0, 0xD2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_21F9)

    def lambda_2214():
        OP_8E(0xFE, 0x1BD00, 0x0, 0xF3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2214)

    def lambda_222F():

        label("loc_222F")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_222F")

    QueueWorkItem2(0x102, 1, lambda_222F)
    OP_6D(116590, 0, 5710, 1500)

    ChrTalk(
        0x107,
        "#560F#5P啊，姐姐你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F你们也听到广播了吧。\x01",
            "飞艇差不多要到要塞了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F准备好了就一起去货舱吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F#2P好，准备完毕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F提妲呢，\x01",
            "那个装置的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F#5P嗯，很好。\x01",
            "时机也测试过了。\x02\x03",
            "如果没有意外的话,\x01",
            "一定可以瞒过生命感应器的监测。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F太好了！\x01",
            "真是令人心安的话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F全靠你了，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F#5P嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#2P好了。\x01",
            "那么我们快去货舱吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1E()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x562)
    OP_28(0x44, 0x1, 0x1)
    SetMapFlags(0x2000000)
    SetMapFlags(0x800)
    EventEnd(0x0)
    Return()

    # Function_12_16B1 end

    def Function_13_246B(): pass

    label("Function_13_246B")

    EventBegin(0x0)
    ClearMapFlags(0x800)
    Fade(1000)
    OP_6D(33030, 0, 6430, 0)
    OP_67(0, 9490, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 32860, 0, 7250, 180)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x102, 32450, 0, 5900, 0)
    SetChrPos(0x101, 33410, 0, 5850, 0)
    SetChrPos(0x106, 32200, 0, 4810, 0)
    SetChrPos(0x107, 33070, 0, 4590, 0)

    def lambda_252D():

        label("loc_252D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_252D")

    QueueWorkItem2(0x102, 2, lambda_252D)

    def lambda_253E():

        label("loc_253E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_253E")

    QueueWorkItem2(0x101, 2, lambda_253E)

    def lambda_254F():

        label("loc_254F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_254F")

    QueueWorkItem2(0x107, 2, lambda_254F)

    def lambda_2560():

        label("loc_2560")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2560")

    QueueWorkItem2(0x106, 2, lambda_2560)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(
        0x8,
        "#691F哦哦，来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F准备已经完成了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#691F集装箱的伪装工作已经做好了。\x02",
    )

    CloseMessageWindow()

    def lambda_25FC():
        OP_6D(31660, 0, 8900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25FC)
    OP_8E(0x8, 0x7F25, 0x0, 0x1B9E, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_22(0xA8, 0x0, 0x64)
    OP_70(0x3, 0xB4)
    OP_73(0x3)

    ChrTalk(
        0x8,
        (
            "#691F即使他们打开普通盖子，\x01",
            "也只能看到维修船壳用的金属板……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x7F3A, 0x0, 0x22F6, 0x7D0, 0x0)
    OP_22(0xA9, 0x0, 0x64)
    OP_70(0x4, 0xB4)
    OP_73(0x4)

    ChrTalk(
        0x8,
        (
            "#693F这边还有个暗门。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2730():
        OP_6D(33030, 0, 6430, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2730)
    OP_8E(0x8, 0x82BE, 0x0, 0x1BF8, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        "#004F嘿嘿～很巧妙嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F接下来只要使生命感应器无效化，\x01",
            "应该就能顺利潜入了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F好了。\x01",
            "接下来你们就藏进去吧……\x02\x03",
            "准备好了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F当然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F随时ＯＫ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F好！\x01",
            "那么挨个儿进去吧。\x02\x03",
            "大家藏好后我就把暗门关上。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F明白了。\x01",
            "那么就由我第一个……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28F4():
        OP_6D(31660, 0, 8900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28F4)

    def lambda_290C():

        label("loc_290C")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_290C")

    QueueWorkItem2(0x101, 2, lambda_290C)

    def lambda_291D():

        label("loc_291D")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_291D")

    QueueWorkItem2(0x107, 2, lambda_291D)

    def lambda_292E():

        label("loc_292E")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_292E")

    QueueWorkItem2(0x106, 2, lambda_292E)

    def lambda_293F():

        label("loc_293F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_293F")

    QueueWorkItem2(0x8, 2, lambda_293F)
    OP_8E(0x102, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)
    OP_8E(0x102, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x102, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)
    OP_8E(0x101, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        (
            "#007F果然是太狭小了，\x01",
            "不得不紧紧地靠在一起……\x02\x03",
            "#503F…………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29EF():

        label("loc_29EF")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_29EF")

    QueueWorkItem2(0x107, 2, lambda_29EF)

    def lambda_2A00():

        label("loc_2A00")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A00")

    QueueWorkItem2(0x106, 2, lambda_2A00)

    def lambda_2A11():

        label("loc_2A11")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A11")

    QueueWorkItem2(0x8, 2, lambda_2A11)

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "艾丝蒂尔，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#504F没、没什么啦！\x02",
    )

    CloseMessageWindow()

    def lambda_2A5F():
        OP_6B(2300, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A5F)

    def lambda_2A6F():
        OP_6D(31110, 0, 9150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A6F)
    OP_8E(0x101, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x101, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#505F#2P嘿哟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P艾丝蒂尔，\x01",
            "麻烦你的头向那边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2PＯＫ。\x02\x03",
            "#004F………………啊……\x02\x03",
            "#503F我、我说约修亚……\x02\x03",
            "这个姿势，你能不能换一下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#1P忍、忍耐一下嘛。\x02\x03",
            "不这样的话，\x01",
            "没办法让四个人都挤进来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#503F#2P是、是吗……\x02\x03",
            "是啊，没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P咳咳……\x02\x03",
            "#010F下一个是提妲，\x01",
            "最后是阿加特兄。\x02\x03",
            "这样四个人应该都能进来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F#1P嗯。\x01",
            "那我进来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C73():

        label("loc_2C73")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_2C73")

    QueueWorkItem2(0x106, 2, lambda_2C73)

    def lambda_2C84():

        label("loc_2C84")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_2C84")

    QueueWorkItem2(0x8, 2, lambda_2C84)
    OP_8E(0x107, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)
    OP_8E(0x107, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x107, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)

    ChrTalk(
        0x107,
        (
            "#062F#2P嘿咻……\x01",
            "姐姐，对不起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P哇，提妲。\x01",
            "暖暖的又好～软哦。\x02\x03",
            "嗯……\x01",
            "还有好像牛奶一样的香味啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F#2P姐、姐姐……\x01",
            "不要抱得人家那么紧嘛。\x02\x03",
            "有点辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F#1P呵呵呵……\x01",
            "好啦，抱一下也没关系嘛。\x02\x03",
            "#502F嗯……\x01",
            "这小脸蛋的手感可真是好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F#2P啊嗯～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#3P艾丝蒂尔……别闹啦。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)

    ChrTalk(
        0x106,
        (
            "#551F哎呀哎呀……\x01",
            "我有种无端的不安啊。\x02\x03",
            "#054F喂喂。\x01",
            "你们就不能多让点地方给我吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EB6():

        label("loc_2EB6")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_2EB6")

    QueueWorkItem2(0x8, 2, lambda_2EB6)
    OP_8E(0x106, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x106, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)

    ChrTalk(
        0x107,
        "#065F#1P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052F#2P哎呀……很挤吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F#1P不，没事。\x01",
            "没关系的。\x02\x03",
            "我能忍耐的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#2P不要勉强啊，\x01",
            "觉得挤直接说就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F#1P啊，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F#2P好了，大叔。\x01",
            "这里的准备完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#691F知道了。\x01",
            "我这就要关上暗门了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0x7F3A, 0x0, 0x22F6, 0x7D0, 0x0)
    Sleep(500)

    def lambda_302A():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_302A)
    OP_22(0xA9, 0x0, 0x64)
    OP_6F(0x4, 180)
    OP_70(0x4, 0x0)
    OP_73(0x4)

    ChrTalk(
        0x8,
        (
            "#691F着陆之后马上就会把集装箱搬出来。\x01",
            " \x02\x03",
            "那时可能有点晃，\x01",
            "你们要稍微忍耐一下哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x7F25, 0x0, 0x1B9E, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_6F(0x3, 180)
    OP_70(0x3, 0x0)
    Sleep(600)
    OP_22(0xA8, 0x0, 0x64)
    OP_73(0x3)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_246B end

    SaveToFile()

Try(main)
