from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4260   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4260.x',
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
        '凯诺娜上尉',                           # 9
        '洛伦斯少尉',                           # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '特务兵',                               # 16
        '特务兵',                               # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
        '特务兵',                               # 20
        '特务兵',                               # 21
        '特务兵',                               # 22
        '卡西乌斯',                             # 23
        '摩尔根将军',                           # 24
        '艾莉茜雅女王',                         # 25
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
        'ED6_DT07/CH02100 ._CH',             # 03
        'ED6_DT07/CH02200 ._CH',             # 04
        'ED6_DT07/CH01610 ._CH',             # 05
        'ED6_DT07/CH02000 ._CH',             # 06
        'ED6_DT07/CH02080 ._CH',             # 07
        'ED6_DT07/CH02010 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT07/CH02200P._CP',             # 04
        'ED6_DT07/CH01610P._CP',             # 05
        'ED6_DT07/CH02000P._CP',             # 06
        'ED6_DT07/CH02080P._CP',             # 07
        'ED6_DT07/CH02010P._CP',             # 08
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_312",          # 00, 0
        "Function_1_3CF",          # 01, 1
        "Function_2_3F2",          # 02, 2
        "Function_3_408",          # 03, 3
        "Function_4_541",          # 04, 4
        "Function_5_69C",          # 05, 5
        "Function_6_93C",          # 06, 6
        "Function_7_113C",         # 07, 7
        "Function_8_1158",         # 08, 8
    )


    def Function_0_312(): pass

    label("Function_0_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_329")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_3CE")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3A9")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 60, 500, 154950, 168)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 60, 0, 150270, 7)
    SetChrPos(0x17, -800, 0, 149980, 356)
    Jump("loc_3CE")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_3B3")
    Jump("loc_3CE")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_3BD")
    Jump("loc_3CE")

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_3C7")
    Jump("loc_3CE")

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_3CE")

    label("loc_3CE")

    Return()

    # Function_0_312 end

    def Function_1_3CF(): pass

    label("Function_1_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E8")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3CF end

    def Function_2_3F2(): pass

    label("Function_2_3F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_407")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F2")

    label("loc_407")

    Return()

    # Function_2_3F2 end

    def Function_3_408(): pass

    label("Function_3_408")

    TalkBegin(0xFE)

    ChrTalk(
        0x18,
        (
            "#090F让曾经辞退了军衔的\x01",
            "卡西乌斯阁下恢复原职，\x01",
            "我心里很是过意不去啊……\x02\x03",
            "不过有他在的话，\x01",
            "我也安心了不少。\x02\x03",
            "虽然对你们深感抱歉，\x01",
            "但请暂时让你们的父亲助我一臂之力吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_408 end

    def Function_4_541(): pass

    label("Function_4_541")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(
        0x16,
        (
            "#080F我很快就要\x01",
            "参加预定的会议了。\x02\x03",
            "你们两个在王都里面\x01",
            "好好地玩一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_698")

    label("loc_5D0")

    OP_A2(0x0)

    ChrTalk(
        0x16,
        (
            "#080F大街那边很热闹吧？\x02\x03",
            "我很快就要\x01",
            "参加预定的会议了。\x02\x03",
            "你们两个在王都里面\x01",
            "好好地玩一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698")

    TalkEnd(0xFE)
    Return()

    # Function_4_541 end

    def Function_5_69C(): pass

    label("Function_5_69C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6CC")

    ChrTalk(
        0x17,
        (
            "#160F理查德……\x01",
            "……那个愚蠢的小子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_938")

    label("loc_6CC")

    OP_A2(0x1)

    ChrTalk(
        0x17,
        "#160F是你们俩啊……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……摩尔根将军？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#160F你们在艾尔贝离宫\x01",
            "救了我的孙女吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F艾尔贝离宫……\x01",
            "啊，是莉安妮小妹妹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那是我们理应要做的事情。\x01",
            "作为游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#160F哼，还是那么能说会道……\x02\x03",
            "不过，这回我真的要\x01",
            "向你们表示感激。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F摩尔根将军……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#160F作为游击士，\x01",
            "你们做得很不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F怎、怎么感觉\x01",
            "这不是您的说话方式呢～\x02\x03",
            "算了，这样也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_938")

    TalkEnd(0xFE)
    Return()

    # Function_5_69C end

    def Function_6_93C(): pass

    label("Function_6_93C")

    EventBegin(0x0)
    OP_6D(-20, 0, 140000, 0)
    OP_67(0, 8189, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(45000, 0)
    OP_6E(473, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x8, 620, 500, 152930, 270)
    SetChrPos(0x9, -790, 500, 152790, 90)
    SetChrPos(0xA, -730, 0, 148500, 0)
    SetChrPos(0xB, 620, 0, 148500, 0)
    SetChrPos(0xC, -730, 0, 146900, 0)
    SetChrPos(0xD, 620, 0, 146900, 0)
    SetChrPos(0xE, -730, 0, 145500, 0)
    SetChrPos(0xF, 620, 0, 145500, 0)
    SetChrPos(0x10, -730, 0, 143900, 0)
    SetChrPos(0x11, 620, 0, 143900, 0)
    SetChrPos(0x12, -730, 0, 142300, 0)
    SetChrPos(0x13, 620, 0, 142300, 0)
    SetChrPos(0x14, -730, 0, 140700, 0)
    SetChrPos(0x15, 620, 0, 140700, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(2000, 0)
    OP_6D(-60, 500, 152860, 5000)
    Fade(1000)
    OP_6D(-60, 500, 152860, 0)
    OP_67(0, 8189, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(45000, 0)
    OP_6E(473, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#187F这、这究竟是怎么回事！？\x02\x03",
            "与『艾尔贝离宫』的联络竟然中断了！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#281F亲卫队和游击士协会……\x02\x03",
            "很有可能被他们那伙人攻陷了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#186F厚、厚颜无耻……\x02\x03",
            "指挥那里的部队的……\x01",
            "少尉，不就是你吗！　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#280F我真是颜面尽失啊。\x02\x03",
            "不过，既然事已至此，\x01",
            "怎么埋怨也都已经没用吧。\x02\x03",
            "而且我们还必须坚守王城，\x01",
            "不能让陛下被他们劫走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#187F不、不用你说，\x01",
            "我也明白这一点！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D43():
        OP_6D(-20, 500, 151500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D43)
    OP_8C(0x8, 180, 400)
    OP_8E(0x8, 0x136, 0x1F4, 0x25206, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        (
            "#185F彻底封锁城门！\x01",
            "无论是谁都不许入内！\x02\x03",
            "然后只要准备迎击\x01",
            "从空中而来的突袭就可以了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P了解！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#185F还有，联络各地的部队，\x01",
            "让他们向艾尔贝离宫进发！\x02\x03",
            "理由是——\x01",
            "镇压假冒王族的恐怖集团！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(350, 250, -1, -1)
    SetChrName("特务兵们")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5SYes，Madam！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0xE, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xD, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xB, 0x1, 0x0, 0x8)
    Sleep(1000)

    def lambda_F9B():
        OP_6D(-250, 500, 152390, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F9B)
    Sleep(500)

    def lambda_FB8():

        label("loc_FB8")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FB8")

    QueueWorkItem2(0x9, 1, lambda_FB8)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x9,
        "#280F呵呵，很有一手嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "#180F哼哼，那是当然。\x01",
            "不要把我和你这个新来的相提并论。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_104E():
        OP_6D(-1270, 2700, 154040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104E)

    def lambda_1066():
        OP_67(0, 3190, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1066)

    def lambda_107E():
        OP_6C(38000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_107E)

    def lambda_108E():
        OP_6B(1600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_108E)
    OP_8C(0x8, 0, 400)
    OP_8E(0x8, 0x15E, 0x1F4, 0x255C6, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        (
            "#183F#2P……上校不在，\x01",
            "我们一定要把这里守住。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4302   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_93C end

    def Function_7_113C(): pass

    label("Function_7_113C")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFFD26, 0x0, 0x1AE8C, 0xFA0, 0x0)
    Return()

    # Function_7_113C end

    def Function_8_1158(): pass

    label("Function_8_1158")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x26C, 0x0, 0x1AE8C, 0xFA0, 0x0)
    Return()

    # Function_8_1158 end

    SaveToFile()

Try(main)
