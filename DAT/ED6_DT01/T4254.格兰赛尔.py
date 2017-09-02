from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4254   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4254.x',
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
        '希尔丹夫人',                           # 9
        '茜亚',                                 # 10
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
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
        'ED6_DT07/CH02463 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
        'ED6_DT07/CH02463P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_2D3",          # 02, 2
        "Function_3_450",          # 03, 3
        "Function_4_81C",          # 04, 4
        "Function_5_C18",          # 05, 5
        "Function_6_1387",         # 06, 6
        "Function_7_2F59",         # 07, 7
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_15A")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_168")
    OP_A3(0x3FB)
    Event(0, 7)

    label("loc_168")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_174"),
        (SWITCH_DEFAULT, "loc_18A"),
    )


    label("loc_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_187")
    OP_A2(0x642)
    Event(0, 6)

    label("loc_187")

    Jump("loc_18A")

    label("loc_18A")

    OP_A2(0x639)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1B4")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 72500, 0, 68560, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1DB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64129, 0, 99150, 167)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_21F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 72500, 0, 68560, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 62980, 0, 65500, 180)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_246")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_250")
    Jump("loc_2B8")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_294")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 72490, 0, 68540, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2B8")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_2B8")

    Return()

    # Function_0_122 end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_2C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2B9 end

    def Function_2_2D3(): pass

    label("Function_2_2D3")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_43A")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_43A")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_43A")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_43A")

    label("loc_343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_43A")

    label("loc_35C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_43A")

    label("loc_375")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_43A")

    label("loc_38E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_43A")

    label("loc_3A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_43A")

    label("loc_3C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_43A")

    label("loc_3D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_43A")

    label("loc_3F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_43A")

    label("loc_40B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_43A")

    label("loc_424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_43A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_43A")

    label("loc_44F")

    Return()

    # Function_2_2D3 end

    def Function_3_450(): pass

    label("Function_3_450")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_45D")
    Jump("loc_818")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_818")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_4C9")

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "希望公主殿下能够平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果我能够\x01",
            "陪在她身边就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_559")
    TurnDirection(0xFE, 0x138, 0)

    ChrTalk(
        0xFE,
        (
            "约修亚先生的肌肤\x01",
            "和女性一样细腻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要化妆得当，\x01",
            "就会变得相当漂亮哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_563")
    Jump("loc_818")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60D")

    ChrTalk(
        0xFE,
        (
            "晚宴招待的客人们\x01",
            "应该都在各自的房间里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "晚宴的准备工作结束之前\x01",
            "请二位耐心等待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660")

    label("loc_60D")


    ChrTalk(
        0xFE,
        (
            "晚宴的准备就快做完了。\x01",
            "请你们再稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_660")

    Jump("loc_818")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6FF")

    ChrTalk(
        0xFE,
        (
            "距晚宴开始\x01",
            "还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请慢慢在城里参观。\x02",
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_6FF")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么了？\x01",
            "是不是有什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，没什么，\x01",
            "我们正在城里参观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "距晚宴开始\x01",
            "还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请慢慢在城里参观。\x02",
    )

    CloseMessageWindow()

    label("loc_818")

    TalkEnd(0xFE)
    Return()

    # Function_3_450 end

    def Function_4_81C(): pass

    label("Function_4_81C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_896")

    ChrTalk(
        0x8,
        (
            "#711F在诞辰庆典上玩累了吗？\x01",
            "　\x02\x03",
            "如果有什么难处，\x01",
            "尽管告诉我就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913")

    label("loc_896")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#711F艾丝蒂尔。\x02\x03",
            "在诞辰庆典上玩累了吗？\x01",
            "　\x02\x03",
            "如果有什么难处，\x01",
            "尽管告诉我就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913")

    Jump("loc_C14")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_995")

    ChrTalk(
        0x8,
        (
            "#710F因为诞辰庆典，\x01",
            "现在街上变得很热闹。\x02\x03",
            "你们就去好好玩玩吧，\x01",
            "要注意安全哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A24")

    label("loc_995")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "#710F啊，\x01",
            "你们两个打算出去吗？\x02\x03",
            "因为诞辰庆典，\x01",
            "现在王都变得很热闹。\x02\x03",
            "你们就去好好玩玩吧，\x01",
            "要注意安全哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A24")

    Jump("loc_C14")

    label("loc_A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_AF5")

    ChrTalk(
        0x8,
        (
            "#714F因为没有出现什么破绽，\x01",
            "所以我想应该不会被发现……\x02\x03",
            "不过在回到房间之前\x01",
            "还是要千万小心才行。\x02\x03",
            "情报部的耳目\x01",
            "可是遍布各个角落的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_AFF")
    Jump("loc_C14")

    label("loc_AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_B09")
    Jump("loc_C14")

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")

    ChrTalk(
        0x8,
        (
            "#711F是问晚宴吗……\x02\x03",
            "因为料理还在准备，\x01",
            "请再稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_B7E")


    ChrTalk(
        0x8,
        (
            "#711F料理准备完毕之后，\x01",
            "晚宴就会立刻开始。\x02\x03",
            "你们就请先回房间休息一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_C14")

    TalkEnd(0xFE)
    Return()

    # Function_4_81C end

    def Function_5_C18(): pass

    label("Function_5_C18")

    EventBegin(0x0)
    OP_6D(62970, 640, 71000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x8, 0xFF)
    SetChrChipByIndex(0x8, 4)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64390, 200, 71030, 270)
    SetChrPos(0x101, 61580, 200, 71540, 90)
    SetChrPos(0x102, 61580, 200, 70620, 90)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#713F……你们要说的我都明白了。\x02\x03",
            "想要把拉赛尔博士的传话\x01",
            "直接禀告给女王陛下吧……\x02\x03",
            "#714F就是这件事对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F对……就是这样的。\x02\x03",
            "如果女王陛下真的是身体不适，\x01",
            "我们就再重新想其他的办法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#715F那并不是问题所在……\x02\x03",
            "女王宫正处于刚才那些特务兵的\x01",
            "２４小时监控状态。\x02\x03",
            "能够进去的只有公爵大人和上校，\x01",
            "以及照料女王的我和一些侍女。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F这么说来，\x01",
            "想要去见女王果真是非常困难的了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#012F怎么办，艾丝蒂尔？\x02\x03",
            "看来唯有拜托希尔丹夫人\x01",
            "将博士的传话禀告给女王陛下了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#505F唔～～～\x01",
            "可是还是直接去和女王谈谈更好……\x02\x03",
            "杜南公爵的目的和理查德上校的企图……\x01",
            "　\x02\x03",
            "不清楚的事情还有很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#713F……艾丝蒂尔、约修亚。\x02\x03",
            "#714F我已经有些打算了。\x02\x03",
            "晚宴结束之后\x01",
            "你们可以再来这里一趟吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)
    Sleep(200)
    SetChrSubChip(0x101, 0)

    ChrTalk(
        0x101,
        "#004F咦，这么说来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F我们和女王见面的方法已经有了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#711F这么想也是可以的。\x02\x03",
            "虽然可能比较困难……\x01",
            "但还是有试一试的价值。\x02\x03",
            "因为还要做一些准备的工作，\x01",
            "所以请等到晚宴结束再来可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F好～的，太幸运了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我明白了。\x01",
            "晚宴一结束就来向您请教。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(
        0x8,
        (
            "#713F我会等候你们的到来。\x02\x03",
            "#711F啊，说到晚宴的事情……\x02\x03",
            "料理还在准备中，请稍等片刻。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D6")

    label("loc_123D")


    ChrTalk(
        0x8,
        (
            "#713F我会等候你们的到来。\x02\x03",
            "#711F料理准备完毕之后，\x01",
            "晚宴就会立刻开始。\x02\x03",
            "你们可以先回房间休息一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_12D6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 66930, 0, 66430, 180)
    SetChrPos(0x102, 66930, 0, 66430, 180)
    SetChrPos(0x8, 72490, 0, 68540, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x800)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_6D(66930, 0, 66430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_C18 end

    def Function_6_1387(): pass

    label("Function_6_1387")

    EventBegin(0x0)
    OP_6D(67590, 0, 65319, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 70120, 0, 69770, 225)
    SetChrPos(0x101, 66580, 0, 64769, 45)
    SetChrPos(0x102, 67630, 0, 64590, 45)

    def lambda_13D8():
        OP_6D(69520, 0, 68800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13D8)

    def lambda_13F0():
        OP_8E(0xFE, 0x10B6C, 0x0, 0x10BE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13F0)

    def lambda_140B():
        OP_8E(0xFE, 0x1113E, 0x0, 0x1095A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_140B)
    WaitChrThread(0x102, 0x2)
    TurnDirection(0x102, 0x8, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        (
            "#710F艾丝蒂尔、约修亚。\x01",
            "我一直在等你们哦。\x02\x03",
            "不觉得迟到了很久吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F这个……对不起。\x02\x03",
            "刚才不巧被理查德上校抓住了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#712F上校……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F只是谈了一些关于我们父亲过去的事情。\x01",
            "　\x02\x03",
            "与这边的行动无关，\x01",
            "请夫人您不用在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#713F是这样啊……\x02\x03",
            "#710F根据尤莉亚的介绍信来看，\x01",
            "你们两位是卡西乌斯先生的孩子吧。\x01",
            "　\x02\x03",
            "理查德上校会有\x01",
            "一些感慨也是理所当然的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F那个～请问一下，\x01",
            "希尔丹夫人也知道父亲的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#711F曾经作为摩尔根将军副官的卡西乌斯上校\x01",
            "经常到王城这里来。\x02\x03",
            "他也是去世的王子……\x01",
            "也就是陛下的儿子以前的校友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F去世的王子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F就是科洛蒂亚公主的父亲。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#715F嗯，王太子夫妇因为\x01",
            "１５年前的海难事故而不幸身亡。\x02\x03",
            "倘若王子还活着的话，\x01",
            "现在这样的局面是不会发生的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#713F……对于已经发生的事情，\x01",
            "后悔是没有用处的。\x02\x03",
            "夜色已晚，这就准备出发吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 69050, 0, 75720, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "#710F茜亚，过来吧。\x02",
    )

    CloseMessageWindow()
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)

    def lambda_189B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_189B)

    def lambda_18A9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18A9)
    Sleep(300)

    def lambda_18BC():

        label("loc_18BC")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_18BC")

    QueueWorkItem2(0x9, 1, lambda_18BC)

    def lambda_18CD():
        OP_8E(0xFE, 0x10CCA, 0x0, 0x112B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18CD)

    def lambda_18E8():

        label("loc_18E8")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_18E8")

    QueueWorkItem2(0x8, 1, lambda_18E8)

    def lambda_18F9():

        label("loc_18F9")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_18F9")

    QueueWorkItem2(0x101, 1, lambda_18F9)

    def lambda_190A():

        label("loc_190A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_190A")

    QueueWorkItem2(0x102, 1, lambda_190A)
    OP_6D(70030, 0, 70300, 2000)

    ChrTalk(
        0x101,
        "#004F咦，你不是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您是茜亚小姐对吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P你、你们好……\x01",
            "艾丝蒂尔小姐，约修亚先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P事情我已经知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#711F#2P你们完全可以相信这个孩子。\x01",
            "　\x02\x03",
            "公主殿下在城里的时候，\x01",
            "就是由这位侍女陪伴在身的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F公主殿下……\x01",
            "就是科洛蒂亚公主吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F这样的话就没问题了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P谢、谢谢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P那么这就把准备好的制服\x01",
            "拿来试穿一下可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P总之小姐您应该会称心的。\x01",
            "丝带啊头饰啊那些细小的方面\x01",
            "我都已经准备完毕了。\x02",
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
        "#014F这么说……难道？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0x1)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "#711F#2P是啊，艾丝蒂尔如果\x01",
            "装扮成侍女的样子就可以进入女王宫了。\x01",
            "　\x02\x03",
            "再把头发的样式改变一下，\x01",
            "看守的那些人也就觉察不出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F原～来是这～样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F的确，制服可以很好地\x01",
            "将个人的特征隐藏起来。\x02\x03",
            "用来掩人耳目就再好不过了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊～侍女的服饰啊。\x02\x03",
            "之前看到过莉拉小姐的着装，\x01",
            "觉得那款式很不错呢。\x02\x03",
            "既飘逸而又很可爱，\x01",
            "行动起来也很方便的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P嘻嘻，如果行动不方便的话，\x01",
            "那扫除的时候就麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，真的是这样吗？\x02\x03",
            "#001F那就立刻穿上吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(
        0x102,
        (
            "#019F#2P很开心嘛……\x02\x03",
            "#010F蹦蹦跳跳的虽然是可以，\x01",
            "但不要在陛下面前失礼哦。\x02\x03",
            "这次我是不能和你一起去了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊，为什么呢？\x02\x03",
            "约修亚也换装不就行了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        "#014F#2P#5S……咦。\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#712F#2P艾丝蒂尔，你说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F约修亚你在学园祭的舞台剧里\x01",
            "扮演的公主不是很好看的嘛。\x02\x03",
            "礼服和侍女装不是差不多吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#2P这、这可不是在演戏。\x02\x03",
            "和女王陛下见面却身着女装，\x01",
            "这实在是有点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没关系，没关系。\x01",
            "一点都不难看！\x02\x03",
            "当时约修亚扮演的公主可是非常美丽哦！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#2P又、又来了……别开玩笑了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#012F希尔丹夫人你们也帮我说说情啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "#712F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#018F我、我说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#713F#2P原来如此……\x01",
            "好像的确没有什么问题。\x02\x03",
            "#710F茜亚，\x01",
            "为公主殿下准备的假发还在吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P是、是的……\x01",
            "一次都没有使用过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P如果是长长的黑发，\x01",
            "和约修亚先生会很配的哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F我、我说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F三比一，少数服从多数～\x01",
            "最终的结果已经揭晓⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P那就请到这边来。\x01",
            "您的服装已经准备好了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_234B():

        label("loc_234B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_234B")

    QueueWorkItem2(0x8, 1, lambda_234B)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x9, 0, 400)

    def lambda_2377():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2377)
    Sleep(300)
    OP_8E(0x101, 0x10FF4, 0x0, 0x10AEA, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        (
            "#012F请等一下！\x01",
            "我换衣服这件事怎么一句话就……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x10FEA, 0x0, 0x1090A, 0x7D0, 0x0)
    OP_8C(0x102, 180, 400)

    def lambda_240D():
        OP_6D(69970, 0, 72360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_240D)

    def lambda_2425():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2425)

    def lambda_2440():
        OP_8F(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2440)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_72(0x3, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_71(0x3, 0x800)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#4P我知道，我知道啦……\x01",
            "衣服什么的由我自己来脱……\x02\x03",
            "啊……茜亚小姐……\x01",
            "还要化妆的啊……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)

    ChrTalk(
        0x8,
        (
            "#716F呼……\x01",
            "现在的年轻人啊……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(69200, 0, 72370, 0)
    SetChrPos(0x8, 68890, 0, 69520, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)

    def lambda_25AC():

        label("loc_25AC")

        OP_8C(0xFE, 225, 0)
        OP_48()
        Jump("loc_25AC")

    QueueWorkItem2(0x101, 2, lambda_25AC)

    def lambda_25BD():
        OP_8E(0xFE, 0x11062, 0x0, 0x116F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25BD)
    Sleep(600)

    def lambda_25DD():
        OP_8E(0xFE, 0x10E00, 0x0, 0x11D78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25DD)
    WaitChrThread(0x9, 0x1)

    def lambda_25FD():
        OP_8E(0xFE, 0x1090A, 0x0, 0x11E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25FD)
    WaitChrThread(0x9, 0x1)

    def lambda_261D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_261D)

    ChrTalk(
        0x8,
        "#712F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#321F#5P#3S您～好。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 317, 400)
    OP_8C(0x101, 75, 400)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#328F#5P嗯，怎么样～呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘻嘻嘻……\x01",
            "非常合适呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#711F从乡村地方到城里不久、\x01",
            "活泼开朗的实习侍女……\x01",
            "这种解释十分有说服力啊。\x02\x03",
            "头发披下来之后，\x01",
            "就更不容易被别人察觉到了。\x02\x03",
            "不如就到我们这个\x01",
            "格兰赛尔城来工作如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#474F#5P游、游击士协会那边还有任务，\x01",
            "所以这个就不好意思了……\x02\x03",
            "#471F啊，对了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#321F喂喂，约修亚。\x01",
            "快点出来吧～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2860():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2860)

    def lambda_286E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_286E)
    OP_6D(69080, 0, 73680, 1000)
    SetChrPos(0x102, 69050, 0, 77130, 180)

    ChrTalk(
        0x102,
        (
            "#4P啊……\x02\x03",
            "不出来不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#326F不～行。\x02\x03",
            "再喋喋不休的话，\x01",
            "我就进去把你拖出来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4P我明白了……\x02\x03",
            "唉，没办法了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2944():

        label("loc_2944")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2944")

    QueueWorkItem2(0x9, 1, lambda_2944)

    def lambda_2955():

        label("loc_2955")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2955")

    QueueWorkItem2(0x8, 1, lambda_2955)

    def lambda_2966():

        label("loc_2966")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2966")

    QueueWorkItem2(0x101, 1, lambda_2966)

    def lambda_2977():
        OP_6C(5000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2977)

    def lambda_2987():
        OP_67(0, 6130, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2987)
    Sleep(1600)

    def lambda_29A4():
        OP_8E(0xFE, 0x10DBA, 0x0, 0x11DC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29A4)
    Sleep(3000)

    def lambda_29C4():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_29C4)

    def lambda_29D4():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29D4)
    OP_62(0x102, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(500)
    OP_22(0x89, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    OP_63(0x102)

    ChrTalk(
        0x102,
        "#333F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#712F这衣服和你竟然会……\x01",
            "相称到如此惊人的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#326F怎么样，我说过的吧！？\x02\x03",
            "#327F约修亚真是的……\x01",
            "竟然比身为少女的我还要漂亮，\x01",
            "这到底是怎～么回事嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘻嘻……\x01",
            "我还为他好好地化了妆的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#335F#5P好了……\x01",
            "请不要再说了……\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(68990, 0, 71660, 1000)

    def lambda_2B51():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B51)

    def lambda_2B5F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B5F)
    OP_8C(0x102, 180, 0)

    ChrTalk(
        0x8,
        (
            "#710F嗯……准备完毕了。\x01",
            "　\x02\x03",
            "那么，我现在就\x01",
            "带领你们两个去女王宫吧。\x02\x03",
            "彻底地把自己当成实习侍女，\x01",
            "这一点你们一定要记住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#471F啊，好的，明白了。\x02\x03",
            "#322F唔……\x01",
            "终于要见到女王了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#332F嗯……到了关键时刻了。\x02\x03",
            "集中精力，\x01",
            "无论如何也要进入女王宫。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#475F噗……你这身打扮配合\x01",
            "这样严肃的口气真是天衣无缝啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    ChrTalk(
        0x102,
        (
            "#337F太、太坏了！\x01",
            "什么天衣无缝！\x02\x03",
            "#333F我都打扮成这副模样了，\x01",
            "你还在取笑我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#321F对不起～对不起。\x01",
            "不要生气嘛～约修亚最听话的了。\x02\x03",
            "下次我请你吃冰淇淋～\x01",
            "总之你就消消气啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#332F哼，我又不是你，\x01",
            "用零食是不能收买我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#476F我、我什么时候\x01",
            "被零食什么的给收买过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嘻嘻……\x01",
            "真是一对好伙伴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#713F时间快来不及了……\x01",
            "立刻前往女王宫吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x80000000)
    OP_28(0x4A, 0x1, 0x20)
    OP_28(0x4A, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x9, 0x80)
    AddParty(0x37, 0xFF)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, 67460, 0, 69310, 180)
    SetChrPos(0x102, 67460, 0, 69310, 180)
    SetChrPos(0x138, 67460, 0, 69310, 180)
    OP_6D(67460, 0, 69310, 0)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x10)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_1387 end

    def Function_7_2F59(): pass

    label("Function_7_2F59")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(68370, 0, 69650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 68920, 0, 70070, 180)
    SetChrPos(0x9, 67750, 0, 70350, 180)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    RemoveParty(0x37, 0xFF)
    SetChrPos(0x101, 68360, 0, 68190, 0)
    SetChrPos(0x102, 67080, 0, 68350, 45)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#006F希尔丹夫人、茜亚小姐，\x01",
            "今天真是太感谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F帮了我们大忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#711F哪里，这是身为服侍女王陛下的我\x01",
            "理所当然要做的事情。\x02\x03",
            "陛下委托的任务就拜托你们了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我、我……\x01",
            "我也要拜托你们了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "请一定要帮我们……\x01",
            "把公主殿下救出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F啊……\x01",
            "茜亚小姐服侍过公主殿下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，服侍过……\x01",
            "虽然能够照顾她的机会并不多，\x01",
            "这是我非常遗憾的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但是她把我这种下人\x01",
            "当作朋友一样对待，\x01",
            "是一位平易近人而又温柔的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "当听说她被那些坏人捉去、\x01",
            "被囚禁在不知道什么地方的时候，\x01",
            "我每天都担心得睡不着觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F不用担心……\x01",
            "我们一定会把她救出来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    ClearMapFlags(0x80000000)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_7_2F59 end

    SaveToFile()

Try(main)
