from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AF",           # 01, 1
        "Function_2_1BF7",         # 02, 2
        "Function_3_282D",         # 03, 3
        "Function_4_2A85",         # 04, 4
        "Function_5_2B80",         # 05, 5
        "Function_6_4089",         # 06, 6
        "Function_7_57CF",         # 07, 7
        "Function_8_5D27",         # 08, 8
        "Function_9_62C0",         # 09, 9
        "Function_10_694A",        # 0A, 10
        "Function_11_6D57",        # 0B, 11
        "Function_12_70F2",        # 0C, 12
        "Function_13_7E5B",        # 0D, 13
        "Function_14_84AB",        # 0E, 14
        "Function_15_8E27",        # 0F, 15
        "Function_16_9129",        # 10, 16
        "Function_17_9326",        # 11, 17
        "Function_18_9E24",        # 12, 18
        "Function_19_A121",        # 13, 19
        "Function_20_A87B",        # 14, 20
        "Function_21_B030",        # 15, 21
        "Function_22_B4BE",        # 16, 22
        "Function_23_B731",        # 17, 23
        "Function_24_BA08",        # 18, 24
        "Function_25_BCCB",        # 19, 25
        "Function_26_BD7E",        # 1A, 26
        "Function_27_BE69",        # 1B, 27
        "Function_28_BFE1",        # 1C, 28
        "Function_29_C024",        # 1D, 29
        "Function_30_C083",        # 1E, 30
        "Function_31_C0C0",        # 1F, 31
        "Function_32_C105",        # 20, 32
        "Function_33_C179",        # 21, 33
        "Function_34_C1A5",        # 22, 34
        "Function_35_C1FB",        # 23, 35
        "Function_36_C225",        # 24, 36
        "Function_37_C25C",        # 25, 37
        "Function_38_C30D",        # 26, 38
        "Function_39_C381",        # 27, 39
        "Function_40_C3CF",        # 28, 40
        "Function_41_C43D",        # 29, 41
        "Function_42_C489",        # 2A, 42
        "Function_43_C4B3",        # 2B, 43
        "Function_44_C56D",        # 2C, 44
        "Function_45_C5FA",        # 2D, 45
        "Function_46_C6B5",        # 2E, 46
        "Function_47_C6F1",        # 2F, 47
        "Function_48_C742",        # 30, 48
        "Function_49_C796",        # 31, 49
        "Function_50_C7EA",        # 32, 50
        "Function_51_C852",        # 33, 51
        "Function_52_C930",        # 34, 52
        "Function_53_C959",        # 35, 53
        "Function_54_C9A0",        # 36, 54
        "Function_55_CA52",        # 37, 55
        "Function_56_CAD8",        # 38, 56
        "Function_57_CB28",        # 39, 57
        "Function_58_CB4F",        # 3A, 58
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Call(2, 1)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B17")
    OP_A2(0x61A)
    OP_28(0x47, 0x1, 0x4)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(108440, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x108, 107670, 1250, 24030, 135)
    SetChrPos(0x101, 107510, 1250, 23130, 90)
    SetChrPos(0x102, 107680, 1250, 22250, 45)
    SetChrPos(0x104, 106450, 1250, 22690, 90)
    TurnDirection(0xA, 0x108, 0)
    OP_0D()

    ChrTalk(
        0x108,
        "#070F哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊，是金选手。\x01",
            "早上好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天的比赛从中午才开始，\x01",
            "现在来有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F我已经找齐同伴了，\x01",
            "想来这里帮他们登记一下。\x02\x03",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊呀，真是恭喜了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "刚开始听到您一个人参赛的时候，\x01",
            "就觉得很不得了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        "啊，你们是昨天的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F嘿嘿，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这次我们是作为金先生的帮手，\x01",
            "来参加武术大会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么请你们在这张纸上\x01",
            "填写必要的事项。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔、约修亚和奥利维尔\x01",
            "在选手登记的单子上填写了必要事项。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "啊，这边的两位\x01",
            "原来是游击士协会的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么……\x01",
            "那一位的身份是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "『漂泊的诗人，\x01",
            "　身兼首屈一指的天才演奏家。』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "『身为爱与和平的使者，\x01",
            "　现在正热烈募集恋人中』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "哎呀，真是难为情啊。\x02\x03",
            "#030F怎么样？\x01",
            "比赛结束之后和我去喝一杯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F啊～～好了好了。\x01",
            "小姐你不要管这个白痴就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F登记的事情就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "好、好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "好了，\x01",
            "这样正式赛的选手登记就完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "小组成员以金选手为代表，\x01",
            "加上艾丝蒂尔选手、约修亚选手\x01",
            "和奥利维尔选手共计四名。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请注意，以后如果有人缺席，\x01",
            "就再也不能再换人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F哦哦，知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F逐渐有感觉了呢～\x02\x03",
            "对了，\x01",
            "今天比赛的对手已经确定了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对阵表已经确定了，\x01",
            "但为了防止赌博行为，\x01",
            "比赛之前是不会公布的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过，根据自己被安排到的休息室，\x01",
            "就可以把对手的范围缩小了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "也就是说，是和另一边的休息室里\x01",
            "其中一个小组进行对战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "嘻嘻，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么，各位参赛选手，\x01",
            "请把这个拿好。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x372, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "选手登记卡\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0xA,
        (
            "把这张卡片让那边的接待员看一下，\x01",
            "就可以进入场内了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "好了，\x01",
            "祝你们胜利。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1BF3")

    label("loc_B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 2)), scpexpr(EXPR_END)), "loc_C04")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 107600, 1250, 23440, 90)
    SetChrPos(0x102, 107500, 1250, 22630, 90)
    TurnDirection(0xA, 0x101, 0)
    OP_6C(90000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "欢迎来到王立竞技场。\x01",
            "是来买票的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "两个人的票合计是\x01",
            "１０００米拉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1030")

    label("loc_C04")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 107600, 1250, 23440, 90)
    SetChrPos(0x102, 107500, 1250, 22630, 90)
    TurnDirection(0xA, 0x101, 0)
    OP_6C(90000, 0)
    OP_0D()
    OP_A2(0x672)

    ChrTalk(
        0xA,
        (
            "欢迎来到王立竞技场。\x01",
            "是来买票的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(
        0x101,
        (
            "#006F啊，是的。\x01",
            "请给我们两张票。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFF")

    label("loc_CE3")


    ChrTalk(
        0x102,
        (
            "#010F是的。\x01",
            "请给我们两张票。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFF")


    ChrTalk(
        0xA,
        (
            "要看正式赛的话，\x01",
            "是从明天开始连续三天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "要买哪一天的票呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F正式赛……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F那个……\x01",
            "不是从明天开始的，\x01",
            "我们想看今天的预选赛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊，真是抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "比赛已经进行过一半了，\x01",
            "我以为不会有人再来买票……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "这样你们还要买吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊，没关系没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "两个人的票合计是\x01",
            "１０００米拉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哇，还真是贵呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F我听说诞辰庆典的武术大会\x01",
            "应该是有打折的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "真是抱歉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今年好像实行了\x01",
            "许多特殊的措施……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……\x01",
            "这样的话也没办法啦。\x02\x03",
            "嗯，１０００米拉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1030")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【付给１０００米拉】\x01",      # 0
            "【不付钱】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_109D"),
        (1, "loc_1209"),
        (SWITCH_DEFAULT, "loc_1242"),
    )


    label("loc_109D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B7")
    OP_22(0x14, 0x0, 0x64)
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0xA,
        "谢谢光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那么，\x01",
            "请拿好门票。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到两张\x07\x02",
            "观战门票\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x36B, 2)
    OP_A2(0x60C)
    OP_A2(0x60C)
    OP_28(0x45, 0x1, 0x800)

    ChrTalk(
        0xA,
        (
            "竞技场的入口\x01",
            "就在左边的正门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "把票让门口的工作人员看一下\x01",
            "就可以进去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1204")

    label("loc_11B7")


    ChrTalk(
        0x101,
        (
            "#004F（糟了……\x01",
            "　米拉好像不够了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（只好一会儿再来了。）\x02",
    )

    CloseMessageWindow()

    label("loc_1204")

    EventEnd(0x0)
    Jump("loc_1242")

    label("loc_1209")


    ChrTalk(
        0xA,
        (
            "我知道了。\x01",
            "期待你们再次光临。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1242")

    label("loc_1242")

    Jump("loc_1BF3")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_12C6")

    ChrTalk(
        0xA,
        (
            "街上的人们\x01",
            "个个脸上喜气洋洋的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "女王陛下的影响力果然很大啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1381")

    label("loc_12C6")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        (
            "诞辰庆典能顺利举行，\x01",
            "真的是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "街上的人们\x01",
            "个个脸上喜气洋洋的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "女王陛下的影响力果然很大啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1381")

    Jump("loc_1BF3")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1407")
    TurnDirection(0xA, 0x108, 400)

    ChrTalk(
        0xA,
        "哎呀，这不是优胜组的选手们吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "表情这么严肃，\x01",
            "是发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1491")

    ChrTalk(
        0xA,
        (
            "虽然武术大会平安地结束了，\x01",
            "可是诞辰庆典会怎么样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(
        0xA,
        "各位，恭喜你们获胜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天各位就请\x01",
            "请好好享受钓鱼的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160E")

    label("loc_152C")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        "各位，恭喜你们获胜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我虽然不能去看，\x01",
            "但应该是一场\x01",
            "很精彩的比赛吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天各位就请\x01",
            "好好享受王城的晚宴吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160E")

    Jump("loc_1BF3")

    label("loc_1611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_16A4")

    ChrTalk(
        0xA,
        "各位，总决赛就要开始了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "准备好了的话，\x01",
            "请告诉入口处的接待员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_16A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_179E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1707")

    ChrTalk(
        0xA,
        (
            "呵呵，\x01",
            "随着你们不断取胜，\x01",
            "你们的崇拜者也在不断增加呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "明天也要加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_179B")

    label("loc_1707")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        (
            "各位，\x01",
            "明天终于要迎来决赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "呵呵，\x01",
            "随着你们不断取胜，\x01",
            "你们的崇拜者也在不断增加呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "明天也要加油哦。\x02",
    )

    CloseMessageWindow()

    label("loc_179B")

    Jump("loc_1BF3")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_180E")
    TurnDirection(0xA, 0x108, 400)

    ChrTalk(
        0xA,
        "金先生，终于到第二回合比赛了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "准备好了的话，\x01",
            "请告诉入口处的接待员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(
        0xA,
        (
            "第一回合比赛胜利，\x01",
            "恭喜你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "明天的比赛\x01",
            "是从下午开始，\x01",
            "请在那之前来这里报到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(
        0xA,
        (
            "把选手登记卡\x01",
            "给那边入口的接待员看一下，\x01",
            "就可以进入场内了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "各位请这边走。\x01",
            "祝你们胜利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_192B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_19FB")

    ChrTalk(
        0xA,
        (
            "武术大会的正式赛\x01",
            "将于明日下午开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不用对号入座，\x01",
            "入场后请选择自己喜欢的座位。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_19FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(
        0xA,
        (
            "竞技场的入口\x01",
            "在正面的右手边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "把票让门口的工作人员看一下\x01",
            "就可以进去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_1ABE")

    ChrTalk(
        0xA,
        (
            "买过票之后\x01",
            "就可以直接从\x01",
            "正面的入口入场了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_1B4B")

    ChrTalk(
        0xA,
        (
            "离入场开始\x01",
            "还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请各位观众\x01",
            "耐心等待一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF3")

    label("loc_1B4B")

    OP_A2(0x18)

    ChrTalk(
        0xA,
        "欢迎来到王立竞技场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "离入场开始\x01",
            "还有一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "请各位观众\x01",
            "耐心等待一会儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF3")

    TalkEnd(0xA)
    Return()

    # Function_1_AF end

    def Function_2_1BF7(): pass

    label("Function_2_1BF7")

    TalkBegin(0xB)
    OP_8C(0xB, 270, 0)
    SetChrSubChip(0xB, 0)
    EventBegin(0x0)
    Fade(1500)

    def lambda_1C13():
        OP_6D(108230, 1250, 32820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C13)

    def lambda_1C2B():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C2B)
    SetChrPos(0x101, 107830, 1250, 33580, 90)
    SetChrPos(0x102, 107750, 1250, 32470, 90)
    OP_8C(0xB, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C7D")
    SetChrPos(0x108, 106450, 1250, 32450, 90)

    label("loc_1C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C9C")
    SetChrPos(0x104, 106450, 1250, 33600, 90)

    label("loc_1C9C")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3B")

    ChrTalk(
        0xB,
        (
            "各位，\x01",
            "欢迎来到王立竞技场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "一旦进去的话，\x01",
            "在比赛结束之前\x01",
            "就不能再出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "已经做好准备了吗？\x02",
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
            "【做好准备了】\x01",        # 0
            "【等一会儿再来】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E15"),
        (1, "loc_1EB1"),
        (SWITCH_DEFAULT, "loc_1F38"),
    )


    label("loc_1E15")

    OP_A2(0x631)
    OP_28(0x49, 0x1, 0x4)

    ChrTalk(
        0xB,
        "知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们的休息室是进入大厅之后，\x01",
            "在右边的『苍之组』休息室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那么祝你们胜利。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x3F5)
    NewScene("ED6_DT01/T4136   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_1F38")

    label("loc_1EB1")


    ChrTalk(
        0xB,
        "我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还有一些时间，\x01",
            "请准备好再来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F38")

    label("loc_1F38")

    Jump("loc_2827")

    label("loc_1F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D7")

    ChrTalk(
        0xB,
        (
            "这不是金大人吗。\x01",
            "欢迎您来到竞技场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "一旦进去的话，\x01",
            "在比赛结束之前\x01",
            "就不能再出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "已经做好准备了吗？\x02",
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
            "【做好准备了】\x01",        # 0
            "【等一会儿再来】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20B4"),
        (1, "loc_214D"),
        (SWITCH_DEFAULT, "loc_21D4"),
    )


    label("loc_20B4")

    OP_A2(0x623)
    OP_28(0x48, 0x1, 0x4)

    ChrTalk(
        0xB,
        "知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们的休息室是进入大厅之后，\x01",
            "在右边的『苍之组』休息室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "那么请加油。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21D4")

    label("loc_214D")


    ChrTalk(
        0xB,
        "我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还有一些时间，\x01",
            "请准备好再来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D4")

    label("loc_21D4")

    Jump("loc_2827")

    label("loc_21D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2482")

    ChrTalk(
        0xB,
        (
            "那张卡片……\x01",
            "你们是参加正式赛的选手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "有一点请各位注意。\x01",
            "就是只要进入竞技场，\x01",
            "比赛结束之前是不能再出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "已经做好准备了吗？\x02",
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
            "【做好准备了】\x01",        # 0
            "【等一会儿再来】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_235F"),
        (1, "loc_23F8"),
        (SWITCH_DEFAULT, "loc_247F"),
    )


    label("loc_235F")

    OP_A2(0x61B)
    OP_28(0x47, 0x1, 0x8)

    ChrTalk(
        0xB,
        "知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们的休息室是进入大厅之后，\x01",
            "在右边的『苍之组』休息室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "请加油。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_247F")

    label("loc_23F8")


    ChrTalk(
        0xB,
        "我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还有一些时间，\x01",
            "请准备好再来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_247F")

    Jump("loc_2827")

    label("loc_2482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2576")

    ChrTalk(
        0xB,
        (
            "现在，王立竞技场内\x01",
            "将要举行武术大会的正式赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "要作为参赛者出场的话，\x01",
            "先要进行选手登记。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "选手登记\x01",
            "请在右边的售票处进行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2827")

    label("loc_2576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2783")

    ChrTalk(
        0xB,
        (
            "现在，王立竞技场内\x01",
            "正在举行武术大会的预选赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "想要入场的话，\x01",
            "请先出示门票。\x02",
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
            "【交出门票】\x01",        # 0
            "【不交出门票】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_266F"),
        (1, "loc_2733"),
        (SWITCH_DEFAULT, "loc_2780"),
    )


    label("loc_266F")

    OP_A2(0x60D)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出两张\x07\x02",
            "观战门票\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x36B, 2)

    ChrTalk(
        0xB,
        (
            "好，可以了。\x01",
            "两位请进吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2780")

    label("loc_2733")


    ChrTalk(
        0xB,
        "可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "今天买的门票\x01",
            "只能在今天使用……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2780")

    label("loc_2780")

    Jump("loc_2827")

    label("loc_2783")


    ChrTalk(
        0xB,
        (
            "现在，王立竞技场内\x01",
            "正在举行武术大会的预选赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "想要入场的话，\x01",
            "请先出示门票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还没有买票的观众，\x01",
            "请到右手边的售票处购票。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2827")

    EventEnd(0x0)
    TalkEnd(0xB)
    Return()

    # Function_2_1BF7 end

    def Function_3_282D(): pass

    label("Function_3_282D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_283A")
    Jump("loc_2A81")

    label("loc_283A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2844")
    Jump("loc_2A81")

    label("loc_2844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_284E")
    Jump("loc_2A81")

    label("loc_284E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2858")
    Jump("loc_2A81")

    label("loc_2858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2862")
    Jump("loc_2A81")

    label("loc_2862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_286C")
    Jump("loc_2A81")

    label("loc_286C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2876")
    Jump("loc_2A81")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_295A")

    ChrTalk(
        0xFE,
        (
            "#819F今天早上工作的时候，\x01",
            "被军队纠缠了好一会儿。\x02\x03",
            "因为恐怖分子曾经\x01",
            "乔装过游击士的缘故，\x01",
            "不得不小心行事了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A63")

    label("loc_295A")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#810F今天早晨，\x01",
            "我到艾尔贝离宫附近执行任务。\x02\x03",
            "#819F军队那些人知道我是游击士后，\x01",
            "纠缠了我好一会儿呢。\x02\x03",
            "因为恐怖分子曾经\x01",
            "乔装过游击士的缘故，\x01",
            "不得不小心行事了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A63")

    Jump("loc_2A81")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2A70")
    Jump("loc_2A81")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2A7A")
    Jump("loc_2A81")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2A81")

    label("loc_2A81")

    TalkEnd(0xFE)
    Return()

    # Function_3_282D end

    def Function_4_2A85(): pass

    label("Function_4_2A85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2A92")
    Jump("loc_2B7C")

    label("loc_2A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A9C")
    Jump("loc_2B7C")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2AA6")
    Jump("loc_2B7C")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2AB0")
    Jump("loc_2B7C")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2ABA")
    Jump("loc_2B7C")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2B4D")

    ChrTalk(
        0xFE,
        (
            "为了给妻子\x01",
            "拿个观战的好位置，\x01",
            "我决定现在就排队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "这就是爱的代价吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2B57")
    Jump("loc_2B7C")

    label("loc_2B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B61")
    Jump("loc_2B7C")

    label("loc_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2B6B")
    Jump("loc_2B7C")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2B75")
    Jump("loc_2B7C")

    label("loc_2B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2B7C")

    label("loc_2B7C")

    TalkEnd(0xFE)
    Return()

    # Function_4_2A85 end

    def Function_5_2B80(): pass

    label("Function_5_2B80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2E64")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2C2D")

    ChrTalk(
        0xFE,
        "这里就是埃雷波尼亚帝国大使馆了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E61")

    label("loc_2C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D11")

    ChrTalk(
        0xFE,
        (
            "一到诞辰庆典，\x01",
            "人就多得不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "据说帝国的帝都就算平常\x01",
            "也比王都现在的人还要多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E61")

    label("loc_2D11")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "一到诞辰庆典，\x01",
            "人就多得不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "据说帝国的帝都就算平常\x01",
            "也比王都现在的人还要多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我简直无法想象。\x02",
    )

    CloseMessageWindow()

    label("loc_2E61")

    Jump("loc_4085")

    label("loc_2E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2FCE")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2F0B")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCB")

    label("loc_2F0B")


    ChrTalk(
        0xFE,
        (
            "其他的王国军士兵\x01",
            "好像都撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我因为还没有\x01",
            "接到新的命令，\x01",
            "所以继续在这里守卫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这是我的使命啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2FCB")

    Jump("loc_4085")

    label("loc_2FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3122")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3075")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311F")

    label("loc_3075")


    ChrTalk(
        0xFE,
        (
            "我负责不让奥利维尔先生\x01",
            "从大使馆逃出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以现在\x01",
            "也不能让你们进去见他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311F")

    Jump("loc_4085")

    label("loc_3122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3393")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_31C9")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3390")

    label("loc_31C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_327C")

    ChrTalk(
        0xFE,
        (
            "穆拉大人是最近\x01",
            "才到王都来的帝国驻外武官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然很年轻，但在帝国军中\x01",
            "好像是个很了不起的人物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3390")

    label("loc_327C")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "穆拉大人是最近\x01",
            "才到王都来的帝国驻外武官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然很年轻，但在帝国军中\x01",
            "好像是个很了不起的人物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个奥利维尔先生现在好像\x01",
            "也老老实实地呆在大使馆里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3390")

    Jump("loc_4085")

    label("loc_3393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3612")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_343A")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360F")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_350F")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生，\x01",
            "如果您又跑出去的话，\x01",
            "那个人也不会袖手旁观的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且他和我说过，\x01",
            "要是您太过放纵的话就要向他汇报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360F")

    label("loc_350F")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生，\x01",
            "您今天又要外出吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您又跑出去的话，\x01",
            "那个人也不会袖手旁观的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且他和我说过，\x01",
            "要是您太过放纵的话就要向他汇报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360F")

    Jump("loc_4085")

    label("loc_3612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3776")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_36B9")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3773")

    label("loc_36B9")


    ChrTalk(
        0xFE,
        (
            "帝国大使馆的人\x01",
            "如果能将奥利维尔先生\x01",
            "关在里面就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么还让他\x01",
            "每天都外出呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3773")

    Jump("loc_4085")

    label("loc_3776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_39C1")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_381D")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BE")

    label("loc_381D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38D8")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生，\x01",
            "请不要再做出让市民\x01",
            "怨声载道的行为了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其他的帝国人\x01",
            "都很讲究纪律和礼仪，\x01",
            "您也稍微向他们学习一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BE")

    label("loc_38D8")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生，\x01",
            "您今天又要外出吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请不要再做出让市民\x01",
            "怨声载道的行为了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其他的帝国人\x01",
            "都很讲究纪律和礼仪，\x01",
            "您也稍微向他们学习一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BE")

    Jump("loc_4085")

    label("loc_39C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3B04")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3A68")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B01")

    label("loc_3A68")


    ChrTalk(
        0xFE,
        (
            "能在武术大会出场是\x01",
            "王国军军人的至高荣誉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能够有机会的话，\x01",
            "我也好想参加武术大会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B01")

    Jump("loc_4085")

    label("loc_3B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3DD2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3BAB")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DCF")

    label("loc_3BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3C3B")
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生……\x01",
            "请您不要在街道上\x01",
            "过于放纵好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您陷入了什么\x01",
            "麻烦的事件中就不好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DCF")

    label("loc_3C3B")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生，\x01",
            "您现在要回大使馆吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵，你在开玩笑吧。\x02\x03",
            "美丽眩目的街道映入眼帘，\x01",
            "来来往往的人们兴味盎然，\x01",
            "以及无数味美绝伦的料理……\x02\x03",
            "#030F这充满美妙的王都正在呼唤着我，\x01",
            "如果我回去不就太失礼了吗。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……这样的话，\x01",
            "请您不要在街道上\x01",
            "过于放纵好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您陷入了什么\x01",
            "麻烦的事件中就不好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DCF")

    Jump("loc_4085")

    label("loc_3DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3FEA")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3E79")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE7")

    label("loc_3E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F05")

    ChrTalk(
        0xFE,
        (
            "帝国大使馆的人\x01",
            "个个都很率直，\x01",
            "而且朴实刚健。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，那个人就……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FE7")

    label("loc_3F05")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "帝国大使馆的人\x01",
            "个个都很率直，\x01",
            "而且朴实刚健。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，那个人就……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每次他在大街上引起骚乱，\x01",
            "市民们就都跑到我这里，\x01",
            "不停地抱怨……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE7")

    Jump("loc_4085")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4085")

    ChrTalk(
        0xFE,
        (
            "这里就是\x01",
            "埃雷波尼亚帝国大使馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有事的话，\x01",
            "是不允许进入的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4085")

    TalkEnd(0xFE)
    Return()

    # Function_5_2B80 end

    def Function_6_4089(): pass

    label("Function_6_4089")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4836")
    EventBegin(0x0)
    OP_69(0x23, 0x3E8)
    OP_A2(0x612)
    OP_28(0x46, 0x1, 0x8)
    OP_28(0x46, 0x1, 0x10)

    ChrTalk(
        0x23,
        (
            "你们好。\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F士兵大哥，你好。\x01",
            "我们有事来找住在这里的金先生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F能麻烦您帮忙通知一下吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "哎～\x01",
            "你们是来找金先生的啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "我第一次见到那个人的时候，\x01",
            "差点吓得尿裤子了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "当时就想着\x01",
            "『王都里面竟然有熊吗！？』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊哈哈，金先生体型太大了嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "不过和他谈过话之后，\x01",
            "发现他为人很和气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "换班之前肚子正饿的时候，\x01",
            "他还给我拿来了肉包子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嗯嗯。\x01",
            "就像很靠得住的大哥一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F咳咳……\x02\x03",
            "#010F那么，能帮我们通知金先生吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "啊，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "金先生刚才回来了，\x01",
            "不过立刻又出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "好像是为了备战武术大会的正式赛，\x01",
            "寻找可以修行的地方去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F修、修行的地方？\x01",
            "金先生还真是专业啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F他有没有提到具体会去什么地方呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "好像是去郊外的\x01",
            "『艾尔贝周游道』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "那里就像森林中的公园一样，\x01",
            "应该可以安静地修行吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F『艾尔贝周游道』啊……\x01",
            "明白了，那么我们也去看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F当然了！\x01",
            "要早点和他商量一下啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "啊，如果你们要去周游道的话，\x01",
            "有件事情请一定要注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "那附近有一处名为\x01",
            "『艾尔贝离宫』的王家宫殿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F啊，那个之前听说过呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F因为作为恐怖事件的搜查本部，\x01",
            "所以军队不让任何人进入对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "什么，已经知道了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "……在那里守备的家伙很麻烦，\x01",
            "请你们一定要注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "最好是不要靠近。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F呼～很麻烦的家伙们啊。\x02\x03",
            "#501F不想被他们看见，\x01",
            "还是尽量不要靠近那里对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F谢谢您的提醒。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_57CB")

    label("loc_4836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_498B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_48C5")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4988")

    label("loc_48C5")


    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "每年的这个日子都非常热闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游客这么多，\x01",
            "不知道其中有没有什么坏人，\x01",
            "得更严格地看守才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4988")

    Jump("loc_57CB")

    label("loc_498B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AEE")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A1A")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEB")

    label("loc_4A1A")


    ChrTalk(
        0xFE,
        (
            "王国军的同伴们都撤走了，\x01",
            "代之而来的是特务兵那群家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我因为还没有接到命令，\x01",
            "所以留在这里了，呵呵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEB")

    Jump("loc_57CB")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4C4D")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4B7D")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C4A")

    label("loc_4B7D")


    ChrTalk(
        0xFE,
        "女王的诞辰庆典该怎么办呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "共和国的大使还没能定下行程，\x01",
            "正为此事感到困扰呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C4A")

    Jump("loc_57CB")

    label("loc_4C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4EF4")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4CDC")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF1")

    label("loc_4CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D66")
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        "金先生，恭喜你们获胜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一直支持的\x01",
            "金先生获胜了，\x01",
            "让我也感到很骄傲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF1")

    label("loc_4D66")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        "金先生，恭喜你们获胜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一直支持的\x01",
            "金先生获胜了，\x01",
            "让我也感到很骄傲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大使馆的各位，\x01",
            "也非常开心呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，谢谢。\x01",
            "我本想回大使馆报告一声呢……\x02\x03",
            "不过今天我不能回大使馆了，\x01",
            "要住在王城里，\x01",
            "麻烦你帮我传达一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请您万事小心呀！\x02",
    )

    CloseMessageWindow()

    label("loc_4EF1")

    Jump("loc_57CB")

    label("loc_4EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4FE2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4F83")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FDF")

    label("loc_4F83")


    ChrTalk(
        0xFE,
        "今天是总决赛的日子哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "各位请努力迎战！\x01",
            "我相信你们一定能获胜的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FDF")

    Jump("loc_57CB")

    label("loc_4FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5103")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5071")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5100")

    label("loc_5071")


    ChrTalk(
        0xFE,
        (
            "我如果不用工作的话，\x01",
            "也想和金先生\x01",
            "一起去参加比赛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们一定要\x01",
            "连我这一份一起加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5100")

    Jump("loc_57CB")

    label("loc_5103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5223")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5192")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5220")

    label("loc_5192")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        (
            "金先生，\x01",
            "祝您在准决赛胜出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也在为您助威，\x01",
            "请一定要加油！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5220")

    Jump("loc_57CB")

    label("loc_5223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_537A")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_52B2")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5377")

    label("loc_52B2")


    ChrTalk(
        0xFE,
        (
            "金先生一向一视同仁地待人，\x01",
            "所以在大使馆里面也很受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果说他有什么缺点的话，\x01",
            "就是拿妙龄女子没办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5377")

    Jump("loc_57CB")

    label("loc_537A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_55C2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5409")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BF")

    label("loc_5409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_549D")
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        (
            "金先生，\x01",
            "今天正式赛就要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我虽然不能去看比赛，\x01",
            "但也要在这里支持你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BF")

    label("loc_549D")

    OP_A2(0x2)
    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(
        0xFE,
        (
            "金先生，\x01",
            "今天正式赛就要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我虽然不能去看比赛，\x01",
            "但也要在这里支持你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊啊，\x01",
            "现在有了这几位协助我的人，\x01",
            "目标就是冠军了。\x02\x03",
            "我不想让自己后悔，\x01",
            "所以会拼命努力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55BF")

    Jump("loc_57CB")

    label("loc_55C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5748")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5651")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5745")

    label("loc_5651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 1)), scpexpr(EXPR_END)), "loc_56C9")

    ChrTalk(
        0xFE,
        (
            "要找金先生的话，\x01",
            "他好像是去郊外的\x01",
            "『艾尔贝周游道』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们去的时候最好\x01",
            "不要靠近『艾尔贝离宫』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5745")

    label("loc_56C9")


    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5745")

    Jump("loc_57CB")

    label("loc_5748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_57CB")

    ChrTalk(
        0xFE,
        (
            "你们好，\x01",
            "这里是卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很抱歉，如果不是来办事的话，\x01",
            "这里是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CB")

    TalkEnd(0xFE)
    Return()

    # Function_6_4089 end

    def Function_7_57CF(): pass

    label("Function_7_57CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5828")

    ChrTalk(
        0xFE,
        (
            "科洛蒂娅公主\x01",
            "真是好漂亮啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "让人无比向往啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5895")

    ChrTalk(
        0xFE,
        (
            "大街上随处可见\x01",
            "那些黑衣的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是在训练吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5920")

    ChrTalk(
        0xFE,
        (
            "呀嗬～！\x01",
            "武术大会结束之后，\x01",
            "接下来就是诞辰庆典了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好～的，尽情地狂欢吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_59C9")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我已经拼尽全力加油了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会果然很棒，\x01",
            "明年我一定还来现场看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_59C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5A4D")

    ChrTalk(
        0xFE,
        (
            "呀嗬～！\x01",
            "总决赛终于开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "究竟哪个小组会获得冠军呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5AD8")

    ChrTalk(
        0xFE,
        (
            "哇～啊，\x01",
            "决赛的双方都是黑马呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "完全没有预料到。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5B5E")

    ChrTalk(
        0xFE,
        (
            "呵呵，今天的比赛\x01",
            "也是一场都不能错过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5BAE")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "不管哪场比赛都有精彩的看点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5C37")

    ChrTalk(
        0xFE,
        (
            "呀嗬～！\x01",
            "今天也要鼓足干劲支持他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5CAD")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "从预选赛的情况来看，\x01",
            "今年就支持游击士小组吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D23")

    label("loc_5CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5D23")

    ChrTalk(
        0xFE,
        (
            "呀嗬～！\x01",
            "今年支持谁好呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D23")

    TalkEnd(0xFE)
    Return()

    # Function_7_57CF end

    def Function_8_5D27(): pass

    label("Function_8_5D27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5D34")
    Jump("loc_62BC")

    label("loc_5D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5D3E")
    Jump("loc_62BC")

    label("loc_5D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5DC1")

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "昨天喝过头了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连是和谁喝的酒\x01",
            "都记不清了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～头疼得好厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_5DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5DCB")
    Jump("loc_62BC")

    label("loc_5DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5E9D")

    ChrTalk(
        0xFE,
        (
            "虽然今天来得比往常要早，\x01",
            "不过已经有这么多人了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不愧是总决赛啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_5E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F3E")

    ChrTalk(
        0xFE,
        (
            "支持空贼组的人\x01",
            "好像没有几个呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，我觉得他们\x01",
            "能在这次大会上堂堂正正地战斗，\x01",
            "非常了不起呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6080")

    label("loc_5F3E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "支持空贼组的人\x01",
            "好像没有几个呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们输的时候\x01",
            "大家还一同欢呼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，我觉得他们\x01",
            "能在这次大会上堂堂正正地战斗，\x01",
            "非常了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后希望他们也能\x01",
            "这样正大光明地生活啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6080")

    Jump("loc_62BC")

    label("loc_6083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_60CF")

    ChrTalk(
        0xFE,
        (
            "今天终于到了\x01",
            "准决赛的比赛日子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "究竟哪一组会\x01",
            "取得最终的胜利呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_60CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6168")

    ChrTalk(
        0xFE,
        (
            "空、空贼战胜了王国军，\x01",
            "总感觉不太妙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军的选手们\x01",
            "也要加把劲才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_6168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_61E7")

    ChrTalk(
        0xFE,
        "快点开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正式赛真是\x01",
            "让人异常激动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_61E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_625F")

    ChrTalk(
        0xFE,
        (
            "难道从今年开始\x01",
            "就变成团体战了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我对个人战的方式\x01",
            "更要感兴趣一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BC")

    label("loc_625F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_62BC")

    ChrTalk(
        0xFE,
        (
            "为何今年与往常不同呢，\x01",
            "对战的规则似乎改变了不少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BC")

    TalkEnd(0xFE)
    Return()

    # Function_8_5D27 end

    def Function_9_62C0(): pass

    label("Function_9_62C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_62CD")
    Jump("loc_6946")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_62D7")
    Jump("loc_6946")

    label("loc_62D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_62E1")
    Jump("loc_6946")

    label("loc_62E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_62EB")
    Jump("loc_6946")

    label("loc_62EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6420")

    ChrTalk(
        0xFE,
        "好，我决定了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就给共和国的\x01",
            "金选手加油吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不行不行，还是觉得\x01",
            "特务部队从名字上听起来更强……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……也就是说，\x01",
            "果然还是要反过来支持游击士小组了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_652D")

    label("loc_6420")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "那～么……\x01",
            "支持哪一组好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我之前支持的小组\x01",
            "在今年的比赛里都输掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……是不是还是不要支持\x01",
            "我希望胜利的小组会好一些呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总觉得很矛盾啊。\x02",
    )

    CloseMessageWindow()

    label("loc_652D")

    Jump("loc_6946")

    label("loc_6530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_659C")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我支持的小组又输了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我难道被什么\x01",
            "不祥之物附体了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6653")

    label("loc_659C")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我支持的小组又输了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我难道被什么\x01",
            "不祥之物附体了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……说起来，\x01",
            "街上的士兵一直在增加呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()

    label("loc_6653")

    Jump("loc_6946")

    label("loc_6656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_673F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_66A8")

    ChrTalk(
        0xFE,
        (
            "今天我要为游击士的\x01",
            "格兰赛尔支部小组加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673C")

    label("loc_66A8")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "今天我要为游击士的\x01",
            "格兰赛尔支部小组加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天还有前天，\x01",
            "我支持的小组都\x01",
            "悉数败下阵来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "希望他们今天能取得胜利。\x02",
    )

    CloseMessageWindow()

    label("loc_673C")

    Jump("loc_6946")

    label("loc_673F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_678A")

    ChrTalk(
        0xFE,
        (
            "呜～\x01",
            "渡鸦帮也输掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么我支持过的小组\x01",
            "都一一败下阵来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6946")

    label("loc_678A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6875")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_67EA")

    ChrTalk(
        0xFE,
        (
            "观战的时候\x01",
            "就是要先选好自己支持哪一方\x01",
            "才会更有意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6872")

    label("loc_67EA")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "这场比赛让我想起了\x01",
            "以前我也有一段叛逆的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为觉得很有亲切感，\x01",
            "所以我支持那个叫做『渡鸦帮』的小组。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6872")

    Jump("loc_6946")

    label("loc_6875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_68FB")

    ChrTalk(
        0xFE,
        (
            "我支持的\x01",
            "国境守备队输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到摩尔根将军\x01",
            "今年没有参加……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6946")

    label("loc_68FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6946")

    ChrTalk(
        0xFE,
        (
            "勿庸置疑，今年肯定也是\x01",
            "国境守备队取得优胜！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6946")

    TalkEnd(0xFE)
    Return()

    # Function_9_62C0 end

    def Function_10_694A(): pass

    label("Function_10_694A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_698D")

    ChrTalk(
        0xFE,
        "真的是王室御用的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_698D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6997")
    Jump("loc_6D53")

    label("loc_6997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_69A1")
    Jump("loc_6D53")

    label("loc_69A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_69AB")
    Jump("loc_6D53")

    label("loc_69AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6A64")

    ChrTalk(
        0xFE,
        (
            "考虑了很久\x01",
            "要支持哪一支队伍……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "最后我还是决定支持\x01",
            "约修亚君一个人！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6AFB")

    ChrTalk(
        0xFE,
        (
            "那个黑发男孩子很可爱，\x01",
            "而且感觉也很酷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好想紧紧地抱抱他啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B9D")

    label("loc_6AFB")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "那个黑发男孩子不错吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不仅很可爱，\x01",
            "而且感觉也很酷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好想紧紧地抱抱他啊～\x02",
    )

    CloseMessageWindow()

    label("loc_6B9D")

    Jump("loc_6D53")

    label("loc_6BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6BDD")

    ChrTalk(
        0xFE,
        (
            "唔～这就是那个\x01",
            "粗俗公爵的所作所为～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6C0C")

    ChrTalk(
        0xFE,
        "嗯嗯，说得对～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6C56")

    ChrTalk(
        0xFE,
        (
            "那些身着黑色铠甲的人\x01",
            "应该很强吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6CDC")

    ChrTalk(
        0xFE,
        (
            "那个叫做金的人，\x01",
            "对自己的实力好像很有信心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一个人去面对其他对手，\x01",
            "的确是个男子汉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D53")

    label("loc_6CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6D53")

    ChrTalk(
        0xFE,
        (
            "亲卫队居然不出场，\x01",
            "简直难以置信～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊～啊，我原本可是专门来看\x01",
            "尤莉亚中尉矫健身姿的呢～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D53")

    TalkEnd(0xFE)
    Return()

    # Function_10_694A end

    def Function_11_6D57(): pass

    label("Function_11_6D57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6DB1")

    ChrTalk(
        0xFE,
        "唔，不太清楚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然大家都说好吃，\x01",
            "不过味道不是也就一般吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6DBB")
    Jump("loc_70EE")

    label("loc_6DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6DC5")
    Jump("loc_70EE")

    label("loc_6DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6DCF")
    Jump("loc_70EE")

    label("loc_6DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6E15")

    ChrTalk(
        0xFE,
        (
            "什么？\x01",
            "只支持一个人？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6ED8")

    ChrTalk(
        0xFE,
        (
            "说起来啊，\x01",
            "我也是这么想的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "觉得我外表看上去\x01",
            "有散发出母性的本能吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6F1D")

    ChrTalk(
        0xFE,
        (
            "说实话～\x01",
            "那些空贼难道不危险吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6FB2")

    ChrTalk(
        0xFE,
        (
            "那个带红色面具的人，\x01",
            "虽然看不见他的脸，\x01",
            "但是不觉得他很酷吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "而且看起来也很强的样子。\x02",
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_6FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7038")

    ChrTalk(
        0xFE,
        (
            "哦～\x01",
            "你是说王国军的那个特别小组吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每个人都是同一种装束，\x01",
            "真是一点个性也没有啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_7038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_70B2")

    ChrTalk(
        0xFE,
        (
            "唉，虽说很强，\x01",
            "但只不过是个大叔啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在的格斗家果然\x01",
            "还是要偶像派的才好呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70EE")

    label("loc_70B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_70EE")

    ChrTalk(
        0xFE,
        (
            "啊～我到底是为了什么\x01",
            "才买了预售的门票啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70EE")

    TalkEnd(0xFE)
    Return()

    # Function_11_6D57 end

    def Function_12_70F2(): pass

    label("Function_12_70F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_715A")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典啊……\x01",
            "大家都很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_715A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_71BD")

    ChrTalk(
        0xFE,
        (
            "利库斯一直是\x01",
            "悠然自得的样子，\x01",
            "因为他没有想做的事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_71BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7241")

    ChrTalk(
        0xFE,
        (
            "像利库斯那样的\x01",
            "乐天派是不会\x01",
            "明白我的心情的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "谁来可怜可怜我啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_73F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_73BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7297")

    ChrTalk(
        0xFE,
        (
            "唉，这下又回到\x01",
            "毫无干劲的那个我了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73BC")

    label("loc_7297")


    ChrTalk(
        0xFE,
        (
            "……我向经常经过这里的\x01",
            "那个漂亮姑娘告白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你猜她说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『我讨厌你这种\x01",
            "　总用奇怪的眼神盯着别人看的人。』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来以为她就算拒绝，\x01",
            "也会用更温柔委婉的说法的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "这下子我的干劲全没了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BC")

    Jump("loc_73F5")

    label("loc_73BF")


    ChrTalk(
        0xFE,
        (
            "啊～啊，\x01",
            "今天又平平淡淡地度过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我的人生在何方呀……\x02",
    )

    CloseMessageWindow()

    label("loc_73F5")

    Jump("loc_7E57")

    label("loc_73F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_7946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_7443")

    ChrTalk(
        0xFE,
        (
            "好，就趁这个势头\x01",
            "试试向她告白吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_7443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_75B7")
    OP_A2(0x6EB)

    ChrTalk(
        0xFE,
        (
            "太好啦——！\x01",
            "她从这里经过三次了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在我真的想感谢\x01",
            "世界上的每一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢，谢谢！\x01",
            "我就在这里哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "谢谢你们！\x01",
            "把这个作为纪念吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x21C, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第11卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "好，就趁这个势头\x01",
            "试试向她告白吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_75B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_766E")

    ChrTalk(
        0xFE,
        "还有一次！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再看见她一次，\x01",
            "我就会干劲十足了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没错，她就是我的女神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_766E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7775")

    ChrTalk(
        0xFE,
        (
            "唔唔，\x01",
            "她快点从这里经过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还有两次……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再看见她两次，\x01",
            "我就能看到活下去的希望了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，万一她要是\x01",
            "不再从这里经过怎么办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经过……不经过……\x01",
            "经过……不经过……经过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7943")

    label("loc_7775")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "有个漂亮的姑娘\x01",
            "经常会经过这里哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近一天能见到她好几次，\x01",
            "真是幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果今天能\x01",
            "见到她经过这里三次的话，\x01",
            "我一定会充满干劲的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，在她来之前，\x01",
            "我就先装作一副读书的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7943")

    Jump("loc_7E57")

    label("loc_7946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7A05")

    ChrTalk(
        0xFE,
        (
            "现在街上到处都是节日的气氛，\x01",
            "没办法去找工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我到底什么时候\x01",
            "才能找到工作啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B06")

    label("loc_7A05")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "唉，好不容易我拿出干劲\x01",
            "开始去找工作了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在街上到处都是节日的气氛，\x01",
            "没办法去找工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我到底什么时候\x01",
            "才能找到工作啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B06")

    Jump("loc_7E57")

    label("loc_7B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7B57")

    ChrTalk(
        0xFE,
        (
            "利库斯为什么就能\x01",
            "那么悠闲自得地生活呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE7")

    label("loc_7B57")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "从昨天开始到今天，\x01",
            "我也渐渐地有些干劲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我打算这就去\x01",
            "找找适合我的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE7")

    Jump("loc_7E57")

    label("loc_7BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7C8B")

    ChrTalk(
        0xFE,
        (
            "今天又无所事事地\x01",
            "度过了一天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少还是得去找找工作吧，\x01",
            "要想办法改变现状才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_7D05")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "今天又是无所事事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去我就\x01",
            "只有毫无作为地\x01",
            "了却一生了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_7DB1")

    ChrTalk(
        0xFE,
        (
            "啊～啊，\x01",
            "今天又在无所事事中\x01",
            "度过了一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一点干劲都没有～\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E57")

    label("loc_7DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7E57")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "如果我有女朋友的话，\x01",
            "就可以一起去观看武术大会了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有个漂亮的姑娘\x01",
            "经常会经过这里，\x01",
            "她真的很不错呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E57")

    TalkEnd(0xFE)
    Return()

    # Function_12_70F2 end

    def Function_13_7E5B(): pass

    label("Function_13_7E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_7EE9")

    ChrTalk(
        0xFE,
        "呀，真热闹。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天看来是睡不成午觉了，\x01",
            "到处溜达溜达吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_7EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_7F65")

    ChrTalk(
        0xFE,
        "想做的事情吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算一次也好，\x01",
            "好想在格兰赛尔城的\x01",
            "空中庭园好好睡一觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_7F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_7FDD")

    ChrTalk(
        0xFE,
        (
            "唉，现在对安敦说什么，\x01",
            "恐怕他都听不进去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "谁都会有烦恼的时候啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_7FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_803D")

    ChrTalk(
        0xFE,
        (
            "……光看着安敦那家伙\x01",
            "是不能满足的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "接下来干点什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8074")

    label("loc_803D")


    ChrTalk(
        0xFE,
        (
            "……我今天又悠闲地度过了一天，\x01",
            "真是满足呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8074")

    Jump("loc_84A7")

    label("loc_8077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_81B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_80F6")

    ChrTalk(
        0xFE,
        (
            "从某种意义上来说，\x01",
            "安敦那家伙也挺幸福的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为什么非要让自己紧张起来呢？\x01",
            "我真是不能理解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B6")

    label("loc_80F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_813D")

    ChrTalk(
        0xFE,
        (
            "安敦那家伙\x01",
            "就光会想些莫名其妙的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B6")

    label("loc_813D")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "今天好像是武术大会的决赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我还是向平常一样\x01",
            "在这里悠闲度过今天吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81B6")

    Jump("loc_84A7")

    label("loc_81B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_824C")

    ChrTalk(
        0xFE,
        (
            "……安敦的坏习惯\x01",
            "又要开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他不是找不到工作，\x01",
            "而是找不到人生的目标。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_824C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_827F")

    ChrTalk(
        0xFE,
        "呼啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今天的天气也很好啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_827F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8307")

    ChrTalk(
        0xFE,
        (
            "我那朋友今天又是一幅\x01",
            "在为什么而烦恼的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果把找工作这个目标\x01",
            "作为人生的目标来看待，\x01",
            "那就太过局限了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_8307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_83B6")

    ChrTalk(
        0xFE,
        (
            "安敦他啊，\x01",
            "有什么好顾虑的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有了想法的话，\x01",
            "放手去做不就行了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_83B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8405")

    ChrTalk(
        0xFE,
        (
            "好吧，\x01",
            "在人多起来之前先去吃饭吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84A7")

    label("loc_8405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_84A7")

    ChrTalk(
        0xFE,
        "我对武术大会没什么兴趣。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，不管是什么样的活动，\x01",
            "我还是会和平常一样生活的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84A7")

    TalkEnd(0xFE)
    Return()

    # Function_13_7E5B end

    def Function_14_84AB(): pass

    label("Function_14_84AB")

    TalkBegin(0xFE)
    OP_A3(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_84BB")
    Jump("loc_8537")

    label("loc_84BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_84C8")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_84D5")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_84E2")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_84EF")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_84FC")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_84FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8506")
    Jump("loc_8537")

    label("loc_8506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8513")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_8513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8520")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_8520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_852D")
    OP_A2(0x19)
    Jump("loc_8537")

    label("loc_852D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8537")
    OP_A2(0x19)

    label("loc_8537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_85AC")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859B")
    OP_0D()
    OP_A9(0x74)
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_859B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85AC")
    TalkEnd(0xFE)
    Return()

    label("loc_85AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_85F3")

    ChrTalk(
        0xFE,
        (
            "今、今天的确要比\x01",
            "以往任何时候都要忙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8646")

    label("loc_85F3")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "请拿好，\x01",
            "这是薄荷巧克力品种的哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "谢谢惠顾！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_8646")

    Jump("loc_8E23")

    label("loc_8649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_86A9")

    ChrTalk(
        0xFE,
        (
            "士兵们好像\x01",
            "都很忙的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_86A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_870A")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "亲卫队的那些人怎么样了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你知道什么后续消息吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_870A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_88F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_87E9")

    ChrTalk(
        0xFE,
        (
            "本日特售的冰淇淋有\x01",
            "巧克力味、草莓味、\x01",
            "香草味、柠檬味这几种哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还有优胜组的金选手、\x01",
            "艾丝蒂尔选手、约修亚选手\x01",
            "和奥利维尔选手的形象哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88F3")

    label("loc_87E9")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "本日特售的冰淇淋\x01",
            "客人要来一份吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "巧克力味、草莓味、\x01",
            "香草味、柠檬味都有哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还有优胜组的金选手、\x01",
            "艾丝蒂尔选手、约修亚选手\x01",
            "和奥利维尔选手的形象哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88F3")

    Jump("loc_8E23")

    label("loc_88F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_898A")

    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店预定在今天武术大会结束后\x01",
            "推出一种限定数量的冰淇淋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要过来尝尝哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_898A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_89EF")

    ChrTalk(
        0xFE,
        "明天终于到决赛了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实际上我正在计划一种\x01",
            "仅限明天供应的冰淇淋。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_89EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8A87")

    ChrTalk(
        0xFE,
        (
            "从武术大会到诞辰庆典这段时间，\x01",
            "将用特别优惠的价格回报大家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请抓住机会哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B2E")

    label("loc_8A87")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从武术大会到诞辰庆典这段时间，\x01",
            "将用特别优惠的价格回报大家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请抓住机会哦！\x02",
    )

    CloseMessageWindow()

    label("loc_8B2E")

    Jump("loc_8E23")

    label("loc_8B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8BB3")

    ChrTalk(
        0xFE,
        (
            "本店的冰淇淋\x01",
            "虽然种类不多，\x01",
            "但每种都是经过精心制作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要品尝一下哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C40")

    label("loc_8BB3")

    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店的冰淇淋\x01",
            "虽然种类不多，\x01",
            "但每种都是经过精心制作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要品尝一下哦。\x02",
    )

    CloseMessageWindow()

    label("loc_8C40")

    Jump("loc_8E23")

    label("loc_8C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8D5D")

    ChrTalk(
        0xFE,
        (
            "大家都说我的店子\x01",
            "是王室御用的，\x01",
            "其实只是传言而已啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，科洛蒂娅公主\x01",
            "如果偷溜出城到街上来玩，\x01",
            "说不定真的会光临我这里一次呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_8D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8DCA")

    ChrTalk(
        0xFE,
        "在大会上助威呐喊辛苦了吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用凉爽的冰淇淋来\x01",
            "滋润一下干燥的喉咙怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E23")

    label("loc_8DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8E23")

    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "来点凉爽美味的\x01",
            "冰淇淋如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E23")

    TalkEnd(0xFE)
    Return()

    # Function_14_84AB end

    def Function_15_8E27(): pass

    label("Function_15_8E27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8EE2")

    ChrTalk(
        0xFE,
        (
            "我为了维持家庭生计\x01",
            "而忙于工作，\x01",
            "不能照顾好孩子们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管他们的前程会怎样，\x01",
            "关键还是在于自身的努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_8EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_8F8E")

    ChrTalk(
        0xFE,
        (
            "我们原本打算在诞辰庆典之前\x01",
            "一直呆在王都的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是最近定期船时常停运，\x01",
            "有些担心家里的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_8F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8FB9")

    ChrTalk(
        0xFE,
        (
            "男孩子就是要\x01",
            "充满阳光感才好哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_8FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9060")

    ChrTalk(
        0xFE,
        (
            "这位夫人是\x01",
            "定期船的空中乘务员哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为大家都是\x01",
            "有工作有儿女的人，\x01",
            "所以谈起话来会更加投缘。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_9060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_90EC")

    ChrTalk(
        0xFE,
        (
            "这个冰淇淋店的\x01",
            "冰淇淋真的非常好吃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说这个店子\x01",
            "在王都非常有名吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9125")

    label("loc_90EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_90F6")
    Jump("loc_9125")

    label("loc_90F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9100")
    Jump("loc_9125")

    label("loc_9100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_910A")
    Jump("loc_9125")

    label("loc_910A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9114")
    Jump("loc_9125")

    label("loc_9114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_911E")
    Jump("loc_9125")

    label("loc_911E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9125")

    label("loc_9125")

    TalkEnd(0xFE)
    Return()

    # Function_15_8E27 end

    def Function_16_9129(): pass

    label("Function_16_9129")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9190")

    ChrTalk(
        0xFE,
        (
            "妈妈去给我买冰淇淋了，\x01",
            "让我在这儿等着～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_9190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_91B6")

    ChrTalk(
        0xFE,
        (
            "卢希娅啊，\x01",
            "还想再吃一个冰淇淋呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_91B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_925B")

    ChrTalk(
        0xFE,
        (
            "卢希娅住的村子啊，\x01",
            "离海边很近很近哦～\x01",
            "还盛开着纯白色的花儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且，我还有波利他们\x01",
            "那样很多很多的朋友哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_925B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_92AD")

    ChrTalk(
        0xFE,
        (
            "卢希娅我好想\x01",
            "快点进王城看看啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但现在已经不能进去了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_92AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_92E9")

    ChrTalk(
        0xFE,
        (
            "冰淇淋～\x01",
            "真的很好吃哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是妈妈买给我的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9322")

    label("loc_92E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_92F3")
    Jump("loc_9322")

    label("loc_92F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_92FD")
    Jump("loc_9322")

    label("loc_92FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9307")
    Jump("loc_9322")

    label("loc_9307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9311")
    Jump("loc_9322")

    label("loc_9311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_931B")
    Jump("loc_9322")

    label("loc_931B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9322")

    label("loc_9322")

    TalkEnd(0xFE)
    Return()

    # Function_16_9129 end

    def Function_17_9326(): pass

    label("Function_17_9326")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_956A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_941F")

    ChrTalk(
        0xFE,
        (
            "托这次庆典的福，\x01",
            "和孩子一起好好的玩耍了一番，\x01",
            "也交到了很好的朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来就要开始繁忙的工作了，\x01",
            "不管怎么说，\x01",
            "也得更加努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9567")

    label("loc_941F")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "下次我要作为\x01",
            "『赛希莉亚号』的乘务员出航。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过托这次庆典的福，\x01",
            "和孩子一起好好的玩耍了一番，\x01",
            "也交到了很好的朋友。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来就要开始繁忙的工作了，\x01",
            "不管怎么说，\x01",
            "也得更加努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9567")

    Jump("loc_9E20")

    label("loc_956A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9633")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "今天开始本来可以去上班的，\x01",
            "但空港却又被封锁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说是为了逮捕\x01",
            "在逃中的恐怖分子，\x01",
            "但总觉得不太平啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_9633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_967E")

    ChrTalk(
        0xFE,
        (
            "见到卡拉的孩子，\x01",
            "就会觉得有个女儿也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_967E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_97CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9700")

    ChrTalk(
        0xFE,
        (
            "这位夫人\x01",
            "和她丈夫一起\x01",
            "经营一家旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听起来\x01",
            "就觉得很辛苦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97C9")

    label("loc_9700")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "我们儿女关系很好，\x01",
            "家长谈起话来\x01",
            "也会很投缘呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这位夫人\x01",
            "和她丈夫一起\x01",
            "经营一家旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听起来\x01",
            "就觉得很辛苦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97C9")

    Jump("loc_9E20")

    label("loc_97CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_98A6")

    ChrTalk(
        0xFE,
        (
            "这个冰淇淋店卖的\x01",
            "冰淇淋真的很不错哦，\x01",
            "在王都也受到一致的好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说科洛蒂娅公主\x01",
            "也微服来这里光顾过，\x01",
            "所以这里还被称为王室御用的店铺。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_98A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9939")

    ChrTalk(
        0xFE,
        (
            "回家之前在\x01",
            "这个公园里面\x01",
            "稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好久没带小孩一起出来玩了，\x01",
            "好累啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_9939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_99A4")

    ChrTalk(
        0xFE,
        (
            "我家孩子似乎\x01",
            "相当喜欢武术大会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "毕竟是男孩子啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_99A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9A75")

    ChrTalk(
        0xFE,
        (
            "在武术大会上，\x01",
            "绑架了我们的空贼竟然也出场了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为余兴节目，\x01",
            "他也许会觉得很有趣，\x01",
            "但对我们来说心情真是复杂啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B7A")

    label("loc_9A75")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "在武术大会上，\x01",
            "绑架了我们的空贼竟然也出场了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "杜南公爵\x01",
            "到底在想什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为余兴节目，\x01",
            "他也许会觉得很有趣，\x01",
            "但对我们来说心情真是复杂啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B7A")

    Jump("loc_9E20")

    label("loc_9B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9BFC")

    ChrTalk(
        0xFE,
        (
            "孩子总是催我，\x01",
            "所以今天打算带他去看武术大会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "这样下去会不会变得\x01",
            "过于溺爱孩子了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E20")

    label("loc_9BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_9D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9C8A")

    ChrTalk(
        0xFE,
        (
            "武术大会期间\x01",
            "从各地前来观战的人很多，\x01",
            "定期船也应该是非常拥挤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "公社那边真的没问题吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D64")

    label("loc_9C8A")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "武术大会期间\x01",
            "从各地前来观战的人很多，\x01",
            "定期船也应该是非常拥挤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种时期休假，\x01",
            "感觉有些过意不去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "公社那边真的没问题吗……\x02",
    )

    CloseMessageWindow()

    label("loc_9D64")

    Jump("loc_9E20")

    label("loc_9D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_9E20")

    ChrTalk(
        0xFE,
        (
            "因为我在柏斯的空贼事件里\x01",
            "一直被囚禁在空贼基地，\x01",
            "所以公司现在让我休假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样就能够长时间和孩子在一起了，\x01",
            "真是开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E20")

    TalkEnd(0xFE)
    Return()

    # Function_17_9326 end

    def Function_18_9E24(): pass

    label("Function_18_9E24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9E76")

    ChrTalk(
        0xFE,
        (
            "果然还是这里的\x01",
            "冰淇淋好吃呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我很喜欢吃薄荷巧克力味的～\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_9EA1")

    ChrTalk(
        0xFE,
        (
            "妈妈她们总是\x01",
            "在那里说个不停。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_9ECD")

    ChrTalk(
        0xFE,
        (
            "哎呀～我啊，\x01",
            "真是好想去\x01",
            "卢希娅的家里玩哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_9F1C")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "我也进过王城的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_9F66")

    ChrTalk(
        0xFE,
        "唔～冰淇淋真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家店的\x01",
            "冰淇淋非常好吃哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9FA6")

    ChrTalk(
        0xFE,
        "妈妈很快就累了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好没劲啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9FD4")

    ChrTalk(
        0xFE,
        "今天也想去看比赛呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_9FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A038")

    ChrTalk(
        0xFE,
        (
            "比武大会，\x01",
            "实在太有气魄了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我简直都激动得\x01",
            "要飞上天了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_A038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A07B")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "今天我要去看武术大会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们是不是很羡慕啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_A07B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A0DD")

    ChrTalk(
        0xFE,
        (
            "妈妈总是\x01",
            "可以乘坐飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等我长大了，\x01",
            "也想在飞艇上工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A11D")

    label("loc_A0DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A11D")

    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "今天能和妈妈一起玩呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A11D")

    TalkEnd(0xFE)
    Return()

    # Function_18_9E24 end

    def Function_19_A121(): pass

    label("Function_19_A121")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_A18E")

    ChrTalk(
        0xFE,
        (
            "我一直这样坚信\x01",
            "亲卫队是不会背叛陛下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A242")

    label("loc_A18E")

    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "我一直这样坚信\x01",
            "亲卫队是不会背叛陛下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "发动政变的居然是理查德上校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这也着实让人有些无法理解。\x02",
    )

    CloseMessageWindow()

    label("loc_A242")

    Jump("loc_A877")

    label("loc_A245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A2AD")

    ChrTalk(
        0xFE,
        (
            "王都守卫队\x01",
            "怎么都匆匆忙忙撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……有种不祥的预感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A35D")

    ChrTalk(
        0xFE,
        (
            "距离诞辰庆典只有几天了，\x01",
            "但是王城内却没有发布任何公告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大概都忙着搜捕\x01",
            "亲卫队去了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A41B")

    ChrTalk(
        0xFE,
        (
            "理查德上校和尤莉亚中尉\x01",
            "要是能携手合作，\x01",
            "我想利贝尔一定会国泰民安的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没想到却变成了这个样子……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A4D1")

    ChrTalk(
        0xFE,
        (
            "虽说那些特务部队的人\x01",
            "是理查德上校的部下，\x01",
            "不过却不招人喜欢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到王国军里\x01",
            "竟然会有这样的一个组织。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A565")

    ChrTalk(
        0xFE,
        (
            "说起来尤莉亚中尉\x01",
            "相当热衷于去教会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "做弥撒的时候\x01",
            "看见过她好多次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A60A")

    ChrTalk(
        0xFE,
        (
            "以前在这一带\x01",
            "常常可以看见\x01",
            "尤莉亚中尉巡查市区的身影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我腰疼的时候还得到她的照顾，\x01",
            "真是一个善良又体贴的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A69E")

    ChrTalk(
        0xFE,
        (
            "『埃尔赛尤号』在空港\x01",
            "被军队扣押住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此，\x01",
            "亲卫队还是在蔡斯出现了，\x01",
            "他们会来进攻王都吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A758")

    ChrTalk(
        0xFE,
        (
            "在市民心中，\x01",
            "亲卫队的人气是非常高的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且每年都会在武术大会中出场，\x01",
            "让诞辰庆典的气氛高涨起来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A82A")

    ChrTalk(
        0xFE,
        (
            "不管怎样，对于亲卫队\x01",
            "会来阻碍女王诞辰庆典的说法，\x01",
            "我还是不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算他们有反叛的意图，\x01",
            "也会堂堂正正地进行战斗，\x01",
            "而不是采用这种低劣的手段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A877")

    label("loc_A82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A877")

    ChrTalk(
        0xFE,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是去观看武术大会的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_A877")

    TalkEnd(0xFE)
    Return()

    # Function_19_A121 end

    def Function_20_A87B(): pass

    label("Function_20_A87B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A90F")

    ChrTalk(
        0xFE,
        (
            "竟然把女王陛下幽禁起来，\x01",
            "还把科洛蒂娅公主诱拐走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这些事实面前，\x01",
            "已经无法再称赞\x01",
            "理查德上校的功绩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_A90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A9B5")

    ChrTalk(
        0xFE,
        (
            "出来买东西的时候……\x01",
            "感觉街上的气氛和平时不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "警备的士兵们都换了，\x01",
            "而且虽然街上有人，但是感觉异常安静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_A9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_AA2C")

    ChrTalk(
        0xFE,
        (
            "现在似乎还是\x01",
            "不能进王城参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "远道而来的游客\x01",
            "想必感到很遗憾吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AA2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_AAED")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "你们不就是获得优胜的选手吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恭喜！\x01",
            "是场很棒的比赛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起特务部队，\x01",
            "你们取得优胜更好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AAED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_AE50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 3)), scpexpr(EXPR_END)), "loc_AB4E")

    ChrTalk(
        0xFE,
        (
            "那个人总用奇怪的眼神\x01",
            "盯着我看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我不知道他想干什么，\x01",
            "不过真是太没礼貌了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_AB4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_ABA8")

    ChrTalk(
        0xFE,
        (
            "那个人总用奇怪的眼神\x01",
            "盯着我看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我不知道他想干什么，\x01",
            "不过真是太没礼貌了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_ABA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_ACC5")
    OP_63(0x31)

    ChrTalk(
        0xFE,
        (
            "那边的那个人，\x01",
            "从刚才开始就一直在盯着我看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好可怕，不想从这里经过了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x31, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "啊，你们是游击士吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太好了，\x01",
            "有游击士在身边就感觉安全多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x15)
    OP_4B(0x31, 255)
    Jump("loc_AE4D")

    label("loc_ACC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AD53")

    ChrTalk(
        0xFE,
        (
            "刚才又不小心\x01",
            "看到了那个男人的目光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "感觉有点可怕……\x01",
            "我想还是不要从那边经过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_AD53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_ADE1")

    ChrTalk(
        0xFE,
        (
            "在百货店前有个男人\x01",
            "一直在盯着我看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "感觉有点恶心呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE4D")

    label("loc_ADE1")


    ChrTalk(
        0xFE,
        "从昨天开始就有士兵在大街上晃。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道他们已经\x01",
            "找到了亲卫队的人吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE4D")

    Jump("loc_B02C")

    label("loc_AE50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_AEE8")

    ChrTalk(
        0xFE,
        (
            "亲卫队竟然\x01",
            "被赶出王城了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是因为杜南公爵嫉妒亲卫队\x01",
            "而下达了这个命令吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AEE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AF40")

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "今天也是个清爽的早晨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "心情真是不错啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AF40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AF76")

    ChrTalk(
        0xFE,
        (
            "比赛的结果\x01",
            "怎么样了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AF76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_AF9A")

    ChrTalk(
        0xFE,
        "大会终于进入正式环节了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AF9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_AFD2")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "街上果然变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AFD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B02C")

    ChrTalk(
        0xFE,
        (
            "东街区这个冰淇淋店\x01",
            "卖的冰淇淋\x01",
            "简直太好吃了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B02C")

    TalkEnd(0xFE)
    Return()

    # Function_20_A87B end

    def Function_21_B030(): pass

    label("Function_21_B030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B078")

    ChrTalk(
        0xFE,
        (
            "能够看到女王陛下的尊容，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B0E1")

    ChrTalk(
        0xFE,
        (
            "平常的那些士兵们\x01",
            "都已经不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王城那里\x01",
            "发生什么事了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B0E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B182")

    ChrTalk(
        0xFE,
        (
            "女王陛下如果不能参加诞辰庆典，\x01",
            "就只能看见杜南公爵那家伙了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在庆典开始之前\x01",
            "病情一定要好转起来啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B1F7")

    ChrTalk(
        0xFE,
        (
            "决胜战好有魄力呀，\x01",
            "连我也很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "是时候回家做晚饭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B269")

    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "我在大圣堂见到一位\x01",
            "以前从没见过的修女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "她好像是新来的呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B2C2")

    ChrTalk(
        0xFE,
        (
            "对了，在艾德尔百货店\x01",
            "买了东西再回去吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B337")

    ChrTalk(
        0xFE,
        (
            "因为下午还有比赛，\x01",
            "就在这会儿把\x01",
            "事情全部办完吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B387")

    ChrTalk(
        0xFE,
        (
            "呼～武术大会的比赛我看了，\x01",
            "真精彩啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B3FA")

    ChrTalk(
        0xFE,
        "今天的比赛会怎么样呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快点开始吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B45C")

    ChrTalk(
        0xFE,
        (
            "呵呵，虽说是预选赛，\x01",
            "但值得一看的比赛也有不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BA")

    label("loc_B45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B4BA")

    ChrTalk(
        0xFE,
        (
            "这个武术大会啊，\x01",
            "是王都市民每年的\x01",
            "一项重要娱乐活动哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4BA")

    TalkEnd(0xFE)
    Return()

    # Function_21_B030 end

    def Function_22_B4BE(): pass

    label("Function_22_B4BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B540")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典开始后，\x01",
            "这附近就变得比较冷清了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "正因为如此，更要加强戒备才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B54A")
    Jump("loc_B72D")

    label("loc_B54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B58D")

    ChrTalk(
        0xFE,
        (
            "果然啊，大会结束了之后\x01",
            "这一带就变得有些冷清了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B642")

    ChrTalk(
        0xFE,
        "游击士小组获胜了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特务部队是最精锐的部队，\x01",
            "我还以为他们一定会赢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "结果还是被游击士打败了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B69C")

    ChrTalk(
        0xFE,
        "今天是总决赛啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须做好警备工作，\x01",
            "以防让任何事故发生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B6FE")

    ChrTalk(
        0xFE,
        (
            "来看武术大会的人\x01",
            "实在太多了，\x01",
            "执行警备工作也相当辛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B72D")

    label("loc_B6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B708")
    Jump("loc_B72D")

    label("loc_B708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B712")
    Jump("loc_B72D")

    label("loc_B712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B71C")
    Jump("loc_B72D")

    label("loc_B71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B726")
    Jump("loc_B72D")

    label("loc_B726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B72D")

    label("loc_B72D")

    TalkEnd(0xFE)
    Return()

    # Function_22_B4BE end

    def Function_23_B731(): pass

    label("Function_23_B731")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_B7C5")

    ChrTalk(
        0xFE,
        (
            "王国军整体\x01",
            "最近要进行重组。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是希望能够有一个\x01",
            "亲切的人作上司啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_B7CF")
    Jump("loc_BA04")

    label("loc_B7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_B86D")

    ChrTalk(
        0xFE,
        (
            "恐怖事件的犯人\x01",
            "好像还没有抓到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此，\x01",
            "还得继续保持这样的警戒状态……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们也觉得\x01",
            "多少有些累了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_B907")

    ChrTalk(
        0xFE,
        (
            "因为昨天的巡逻\x01",
            "导致睡眠不足，\x01",
            "今天要早点睡才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大会也顺利结束了，\x01",
            "好想放会儿假啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_B960")

    ChrTalk(
        0xFE,
        (
            "我昨天通宵\x01",
            "在王都里巡逻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "已经睡眠不足了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_B9D5")

    ChrTalk(
        0xFE,
        (
            "为了对付恐怖分子，\x01",
            "今天也要在街上巡逻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B9DF")
    Jump("loc_BA04")

    label("loc_B9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B9E9")
    Jump("loc_BA04")

    label("loc_B9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B9F3")
    Jump("loc_BA04")

    label("loc_B9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B9FD")
    Jump("loc_BA04")

    label("loc_B9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BA04")

    label("loc_BA04")

    TalkEnd(0xFE)
    Return()

    # Function_23_B731 end

    def Function_24_BA08(): pass

    label("Function_24_BA08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BAAA")

    ChrTalk(
        0xFE,
        (
            "王国军整体\x01",
            "最近要进行重组。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是希望能给\x01",
            "既诚实又有真本领的人当部下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BAAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BAB4")
    Jump("loc_BCC7")

    label("loc_BAB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BB3E")

    ChrTalk(
        0xFE,
        (
            "不仅街上在进行警戒，\x01",
            "关所似乎也暂时封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "抓到那些恐怖分子\x01",
            "也只是时间的问题吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BB3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BB9C")

    ChrTalk(
        0xFE,
        (
            "接下来就该到\x01",
            "百货店里巡逻了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BB9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BC07")

    ChrTalk(
        0xFE,
        (
            "如果发现了亲卫队\x01",
            "或者形迹可疑的人，\x01",
            "请务必马上告知我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BC07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BC98")

    ChrTalk(
        0xFE,
        (
            "竟然让空贼那群人\x01",
            "参加武术大会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "公爵到底在想些什么呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCC7")

    label("loc_BC98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BCA2")
    Jump("loc_BCC7")

    label("loc_BCA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BCAC")
    Jump("loc_BCC7")

    label("loc_BCAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BCB6")
    Jump("loc_BCC7")

    label("loc_BCB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BCC0")
    Jump("loc_BCC7")

    label("loc_BCC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BCC7")

    label("loc_BCC7")

    TalkEnd(0xFE)
    Return()

    # Function_24_BA08 end

    def Function_25_BCCB(): pass

    label("Function_25_BCCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BCD8")
    Jump("loc_BD7A")

    label("loc_BCD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BD23")

    ChrTalk(
        0xFE,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "喂，\x01",
            "不要在这里乱看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD7A")

    label("loc_BD23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BD2D")
    Jump("loc_BD7A")

    label("loc_BD2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BD37")
    Jump("loc_BD7A")

    label("loc_BD37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BD41")
    Jump("loc_BD7A")

    label("loc_BD41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BD4B")
    Jump("loc_BD7A")

    label("loc_BD4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BD55")
    Jump("loc_BD7A")

    label("loc_BD55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BD5F")
    Jump("loc_BD7A")

    label("loc_BD5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BD69")
    Jump("loc_BD7A")

    label("loc_BD69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BD73")
    Jump("loc_BD7A")

    label("loc_BD73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BD7A")

    label("loc_BD7A")

    TalkEnd(0xFE)
    Return()

    # Function_25_BCCB end

    def Function_26_BD7E(): pass

    label("Function_26_BD7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BD8B")
    Jump("loc_BE65")

    label("loc_BD8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BE0E")

    ChrTalk(
        0xFE,
        (
            "这几天在城里\x01",
            "都没有看见理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是不是外出\x01",
            "到什么地方去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE65")

    label("loc_BE0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BE18")
    Jump("loc_BE65")

    label("loc_BE18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BE22")
    Jump("loc_BE65")

    label("loc_BE22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BE2C")
    Jump("loc_BE65")

    label("loc_BE2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BE36")
    Jump("loc_BE65")

    label("loc_BE36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BE40")
    Jump("loc_BE65")

    label("loc_BE40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BE4A")
    Jump("loc_BE65")

    label("loc_BE4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BE54")
    Jump("loc_BE65")

    label("loc_BE54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BE5E")
    Jump("loc_BE65")

    label("loc_BE5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BE65")

    label("loc_BE65")

    TalkEnd(0xFE)
    Return()

    # Function_26_BD7E end

    def Function_27_BE69(): pass

    label("Function_27_BE69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BE76")
    Jump("loc_BFDD")

    label("loc_BE76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_BF86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_BEEC")

    ChrTalk(
        0xFE,
        (
            "哼，我不认为决赛时\x01",
            "洛伦斯队长使出了全力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长肯定是\x01",
            "手下留情了的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF83")

    label("loc_BEEC")

    OP_A2(0x17)

    ChrTalk(
        0xFE,
        (
            "你们好像是\x01",
            "武术大会取得优胜的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，我不认为决赛时\x01",
            "洛伦斯队长使出了全力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长肯定是\x01",
            "手下留情了的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF83")

    Jump("loc_BFDD")

    label("loc_BF86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_BF90")
    Jump("loc_BFDD")

    label("loc_BF90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_BF9A")
    Jump("loc_BFDD")

    label("loc_BF9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BFA4")
    Jump("loc_BFDD")

    label("loc_BFA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_BFAE")
    Jump("loc_BFDD")

    label("loc_BFAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BFB8")
    Jump("loc_BFDD")

    label("loc_BFB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BFC2")
    Jump("loc_BFDD")

    label("loc_BFC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_BFCC")
    Jump("loc_BFDD")

    label("loc_BFCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_BFD6")
    Jump("loc_BFDD")

    label("loc_BFD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_BFDD")

    label("loc_BFDD")

    TalkEnd(0xFE)
    Return()

    # Function_27_BE69 end

    def Function_28_BFE1(): pass

    label("Function_28_BFE1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "好～的，\x01",
            "接下来去百货店看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_BFE1 end

    def Function_29_C024(): pass

    label("Function_29_C024")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "怎么也要在王都\x01",
            "买到流行的衣服才回去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_C024 end

    def Function_30_C083(): pass

    label("Function_30_C083")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "为何会有那么多人\x01",
            "在那边排队呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "究竟是在排什么队呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_C083 end

    def Function_31_C0C0(): pass

    label("Function_31_C0C0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我、我已经不是小孩了，\x01",
            "怎么会想吃那种东西！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_C0C0 end

    def Function_32_C105(): pass

    label("Function_32_C105")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哈～哈～哈，是吗，\x01",
            "你已经不是小孩了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那老爸我要开始吃了哦～\x01",
            "哈～哈～哈～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_C105 end

    def Function_33_C179(): pass

    label("Function_33_C179")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "呀哈……\x01",
            "好热闹呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_C179 end

    def Function_34_C1A5(): pass

    label("Function_34_C1A5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "今天有一点热呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "想吃点凉爽的东西。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_C1A5 end

    def Function_35_C1FB(): pass

    label("Function_35_C1FB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能插队哦，\x01",
            "快到后面去排着吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_C1FB end

    def Function_36_C225(): pass

    label("Function_36_C225")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "等呀等呀等～……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_C225 end

    def Function_37_C25C(): pass

    label("Function_37_C25C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "当听说政变的时候我很担忧，\x01",
            "幸亏被亲卫队和游击士阻止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来我就开始\x01",
            "担心王国军是否还好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_C25C end

    def Function_38_C30D(): pass

    label("Function_38_C30D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "呵呵，历史资料馆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典结束之后，\x01",
            "一定要去看看。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_C30D end

    def Function_39_C381(): pass

    label("Function_39_C381")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "人啊，\x01",
            "要活到老，学到老。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_C381 end

    def Function_40_C3CF(): pass

    label("Function_40_C3CF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "痛痛痛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王都太大了，走的路过多，\x01",
            "结果脚都给磨破了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～啊，好惨……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_C3CF end

    def Function_41_C43D(): pass

    label("Function_41_C43D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "如果鞋子适脚的话，\x01",
            "走起来就会很舒服的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_C43D end

    def Function_42_C489(): pass

    label("Function_42_C489")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "爸～爸，你好～差劲。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_C489 end

    def Function_43_C4B3(): pass

    label("Function_43_C4B3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "噗噜噗噜噗噜…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果政变得逞的话，\x01",
            "那个杜南公爵\x01",
            "就会成为国王吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那样一来这个王国就完了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_C4B3 end

    def Function_44_C56D(): pass

    label("Function_44_C56D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "所谓恐怖事件不就是\x01",
            "情报部自导自演的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一直不认为亲卫队是坏人，\x01",
            "所以很放心哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_C56D end

    def Function_45_C5FA(): pass

    label("Function_45_C5FA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "百货店好像在搞\x01",
            "诞辰庆典纪念大酬宾哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "各种商品都\x01",
            "变得很便宜了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_C5FA end

    def Function_46_C6B5(): pass

    label("Function_46_C6B5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "呀啊～真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快快，现在立刻就去吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_C6B5 end

    def Function_47_C6F1(): pass

    label("Function_47_C6F1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哎呀，没想到在政变之后\x01",
            "还能有如此盛大的庆典。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_C6F1 end

    def Function_48_C742(): pass

    label("Function_48_C742")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哦，这里就是共和国大使馆啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好想进去看看，哪怕一次也好……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_48_C742 end

    def Function_49_C796(): pass

    label("Function_49_C796")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "我是第一次来王都呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太～棒了，好宽的大街啊～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_C796 end

    def Function_50_C7EA(): pass

    label("Function_50_C7EA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "喂～不要跑那么远～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我担心女儿\x01",
            "会不小心迷路。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_C7EA end

    def Function_51_C852(): pass

    label("Function_51_C852")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今年的航运杂乱无章，\x01",
            "害我没能欣赏到\x01",
            "武术大会的盛况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且竟然是理查德上校\x01",
            "发动的政变导致的这一切。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我可是上校的忠实支持者呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_51_C852 end

    def Function_52_C930(): pass

    label("Function_52_C930")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我想买一个\x01",
            "玩具飞艇～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_52_C930 end

    def Function_53_C959(): pass

    label("Function_53_C959")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "孙子一直缠着我，\x01",
            "就只好带他到百货店去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_53_C959 end

    def Function_54_C9A0(): pass

    label("Function_54_C9A0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "这种话只能在\x01",
            "一切都结束了才能说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "武术大会的优胜者\x01",
            "阻止了此次政变，\x01",
            "真是让人痛快之极啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市民的情绪这么高涨\x01",
            "也不是没有原因的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_54_C9A0 end

    def Function_55_CA52(): pass

    label("Function_55_CA52")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "从帝国大使馆门前走过时\x01",
            "不知为何就紧张起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "很可能是看到了那扇大门，\x01",
            "产生了压迫感。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_55_CA52 end

    def Function_56_CAD8(): pass

    label("Function_56_CAD8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "明明说好了你要自己走路的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……真是的，拿你没办法呀。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_56_CAD8 end

    def Function_57_CB28(): pass

    label("Function_57_CB28")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "姐姐，背我嘛！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_57_CB28 end

    def Function_58_CB4F(): pass

    label("Function_58_CB4F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "典礼已经结束了，\x01",
            "这下可以在市区内逛逛了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_58_CB4F end

    SaveToFile()

Try(main)
