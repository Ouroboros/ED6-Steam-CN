from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4220   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4220.x',
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
        '卡西乌斯',                             # 15
        '摩尔根将军',                           # 16
        '艾莉茜雅女王',                         # 17
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
        'ED6_DT07/CH01330 ._CH',             # 05
        'ED6_DT07/CH02000 ._CH',             # 06
        'ED6_DT07/CH02080 ._CH',             # 07
        'ED6_DT07/CH02013 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT07/CH02200P._CP',             # 04
        'ED6_DT07/CH01330P._CP',             # 05
        'ED6_DT07/CH02000P._CP',             # 06
        'ED6_DT07/CH02080P._CP',             # 07
        'ED6_DT07/CH02013P._CP',             # 08
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 40,
        Z                   = 750,
        Y                   = 155220,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_2B5",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_43C",          # 03, 3
        "Function_4_5C3",          # 04, 4
        "Function_5_71E",          # 05, 5
        "Function_6_A26",          # 06, 6
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_220")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_254")
    Jump("loc_2B4")

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_28F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xE, 530, 0, 150340, 0)
    SetChrPos(0xF, -400, 0, 150340, 0)
    Jump("loc_2B4")

    label("loc_28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_299")
    Jump("loc_2B4")

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2A3")
    Jump("loc_2B4")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2AD")
    Jump("loc_2B4")

    label("loc_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2B4")

    label("loc_2B4")

    Return()

    # Function_0_212 end

    def Function_1_2B5(): pass

    label("Function_1_2B5")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2B5 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_426")

    label("loc_2E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_426")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_426")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_426")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_426")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_426")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_426")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_426")

    label("loc_393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_426")

    label("loc_3AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_426")

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_426")

    label("loc_3DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_426")

    label("loc_3F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_426")

    label("loc_410")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_426")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_426")

    label("loc_43B")

    Return()

    # Function_2_2BF end

    def Function_3_43C(): pass

    label("Function_3_43C")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_461")
    SetChrSubChip(0xFE, 1)
    Jump("loc_47C")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_477")
    SetChrSubChip(0xFE, 0)
    Jump("loc_47C")

    label("loc_477")

    SetChrSubChip(0xFE, 2)

    label("loc_47C")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x10,
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
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_43C end

    def Function_4_5C3(): pass

    label("Function_4_5C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_652")

    ChrTalk(
        0xE,
        (
            "#080F我一会儿要去参加预定的会议。\x01",
            "　\x02\x03",
            "你们两个就在王都里面\x01",
            "好好地玩一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A")

    label("loc_652")

    OP_A2(0x0)

    ChrTalk(
        0xE,
        (
            "#080F大街那边很热闹吧？\x02\x03",
            "我一会儿要去参加预定的会议。\x01",
            "　\x02\x03",
            "你们两个就在王都里面\x01",
            "好好地玩一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A")

    TalkEnd(0xFE)
    Return()

    # Function_4_5C3 end

    def Function_5_71E(): pass

    label("Function_5_71E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(
        0xF,
        (
            "#163F理查德……\x01",
            "……那个愚蠢的小子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A22")

    label("loc_74E")

    OP_A2(0x1)

    ChrTalk(
        0xF,
        "#161F是你们俩啊……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……摩尔根将军？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#163F是你们在艾尔贝离宫救了我的孙女吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F艾尔贝离宫……\x02\x03",
            "#001F啊，是莉安妮小妹妹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那是我们理应要做的事情。\x02\x03",
            "因为保证市民的安全是游击士的义务。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F哼，还是那么能说会道……\x02\x03",
            "不过你们不仅解放了离宫，\x01",
            "而且还救出了女王陛下，\x01",
            "并夺回了格兰赛尔城……\x02\x03",
            "这回我真的要向你们表示感激。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F摩尔根将军……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#160F作为游击士，\x01",
            "你们做得很不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F怎、怎么感觉您话中有话呢～\x01",
            "　\x02\x03",
            "#000F算了，这样也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A22")

    TalkEnd(0xFE)
    Return()

    # Function_5_71E end

    def Function_6_A26(): pass

    label("Function_6_A26")

    EventBegin(0x0)
    OP_6D(-400, 500, 150910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 380, 500, 150540, 270)
    SetChrPos(0x9, -1300, 500, 151320, 138)
    SetChrPos(0xA, -1070, 0, 147120, 0)
    SetChrPos(0xB, 750, 0, 147120, 0)
    SetChrPos(0xC, -1190, 0, 145180, 0)
    SetChrPos(0xD, 820, 0, 145210, 0)

    ChrTalk(
        0x8,
        (
            "#180F这、这究竟是怎么回事！？\x02\x03",
            "与『艾尔贝离宫』\x01",
            "的联络竟然中断了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#280F亲卫队和游击士协会……\x02\x03",
            "很有可能被其中\x01",
            "之一给攻陷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F厚、厚颜无耻……\x02\x03",
            "指挥那里的部队的……\x01",
            "少尉，不就是你吗！　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#280F我真是颜面尽失啊。\x02\x03",
            "不过，既然事已至此\x01",
            "怎么埋怨都也已经没用了。\x02\x03",
            "而且我们还必须坚守王城，\x01",
            "不能让陛下被他们劫走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F不、不用你说，\x01",
            "我也明白这一点！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D0F():
        OP_6D(520, 0, 148610, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0F)
    OP_8C(0x8, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#180F彻底封锁城门！\x01",
            "无论是谁都不许入内！\x02\x03",
            "然后只要准备对抗\x01",
            "从空中而来的袭击就可以了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F还有，联络各地的部队\x01",
            "让他们向艾尔贝离宫进发！\x02\x03",
            "理由是：镇压假冒\x01",
            "王族的恐怖集团！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ｙｅｓ，Ｍａｄａｍ！\x02",
    )

    CloseMessageWindow()

    def lambda_EC7():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EC7)

    def lambda_EE2():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EE2)
    Sleep(300)

    def lambda_F02():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F02)

    def lambda_F1D():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F1D)
    Sleep(1000)
    OP_6D(-400, 500, 150910, 1000)

    ChrTalk(
        0x9,
        "#280F呵呵，很有一手嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#180F哼哼，那是当然。\x01",
            "不要把我和你这个新来的相提并论。\x02\x03",
            "……阁下不在，我们\x01",
            "一定要把这里守住！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_A26 end

    SaveToFile()

Try(main)
