from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2200.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60031",
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
        '基库',                                 # 9
        '黑衣男子',                             # 10
        '黑衣男子',                             # 11
        '弗科特老人',                           # 12
        '照相机',                               # 13
        '玛诺利亚间道方向',                     # 14
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
        Unknown_3A              = 84,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
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
        'ED6_DT07/CH02320 ._CH',             # 00
        'ED6_DT07/CH01330 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH00440 ._CH',             # 03
        'ED6_DT07/CH00441 ._CH',             # 04
        'ED6_DT06/CH20053 ._CH',             # 05
        'ED6_DT06/CH20085 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT07/CH01330P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH00440P._CP',             # 03
        'ED6_DT07/CH00441P._CP',             # 04
        'ED6_DT06/CH20053P._CP',             # 05
        'ED6_DT06/CH20085P._CP',             # 06
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
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
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
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
        X                   = 620,
        Z                   = 550,
        Y                   = -2470,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1330,
        Z                   = -430,
        Y                   = -46450,
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


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_287",          # 02, 2
        "Function_3_29D",          # 03, 3
        "Function_4_A2F",          # 04, 4
        "Function_5_A48",          # 05, 5
        "Function_6_1245",         # 06, 6
        "Function_7_1336",         # 07, 7
        "Function_8_1422",         # 08, 8
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FE")
    OP_72(0x2, 0x8)
    Jump("loc_1FE")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_20C")
    Event(0, 5)
    Jump("loc_214")

    label("loc_20C")

    ClearMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)

    label("loc_214")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_220"),
        (SWITCH_DEFAULT, "loc_236"),
    )


    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_233")
    OP_A2(0x438)
    Event(0, 3)

    label("loc_233")

    Jump("loc_236")

    label("loc_236")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_1E6 end

    def Function_1_248(): pass

    label("Function_1_248")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDDD20, 0x30050)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_273")
    OP_A3(0x3FA)
    Jump("loc_278")

    label("loc_273")

    OP_71(0xA, 0x4)

    label("loc_278")

    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x8)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_248 end

    def Function_2_287(): pass

    label("Function_2_287")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_287")

    label("loc_29C")

    Return()

    # Function_2_287 end

    def Function_3_29D(): pass

    label("Function_3_29D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(3700, 2600, -22200, 0)
    OP_6B(4000, 0)
    OP_6C(333000, 0)
    SetChrPos(0x8, 2780, 2600, -22200, 0)
    SetChrPos(0x101, 3920, -540, -27770, 0)
    SetChrPos(0x102, 2820, -530, -28580, 0)
    SetChrPos(0x105, 3690, -460, -29430, 0)
    SetChrPos(0x106, 4740, -440, -28690, 0)
    StopSound(0x7D00, 0x27100, 0x0)

    def lambda_32F():
        OP_6D(0, 8800, 6500, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_32F)

    def lambda_347():
        OP_6C(57000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_347)

    def lambda_357():
        OP_67(0, 11290, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_357)

    def lambda_36F():
        OP_6B(10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_36F)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x57E40, 0x1388)
    ClearChrFlags(0x8, 0x80)
    OP_8E(0x8, 0x253A, 0x2EE0, 0x1018, 0x36B0, 0x0)
    OP_43(0x8, 0x1, 0x0, 0x4)
    OP_97(0x8, 0x0, 0x1964, 0xFFF6D840, 0x36B0, 0x1)
    OP_44(0x8, 0xFF)
    Fade(1000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    SetChrFlags(0x8, 0x80)
    OP_6D(3940, -520, -28440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#002F那座建筑物是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F巴伦诺灯塔……\x01",
            "是卢安市辖下的设施。\x02\x03",
            "我记得这里只住着\x01",
            "一个看守灯塔的老头……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F但是，不会有错的。\x02\x03",
            "我想那些袭击老师的犯人\x01",
            "就在这座建筑物里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那就是说，\x01",
            "犯人很有可能占领了灯塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F看起来……\x01",
            "好像只有那一个入口。\x02\x03",
            "总之只能进去看看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F好……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x105, 400)

    ChrTalk(
        0x106,
        (
            "#052F#2P等一下。\x01",
            "小姑娘，难道你也……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F我想亲眼看看。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F#2P什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(
        0x105,
        (
            "#043F犯人到底是什么人，\x01",
            "为什么要对老师和孩子们下这种毒手……\x02\x03",
            "#043F所以……请让我也一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#055F#2P就、就算你这样说……\x02",
    )

    CloseMessageWindow()

    def lambda_7A3():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A3)

    def lambda_7B1():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F#1P啊～真是的。\x01",
            "别那么小气啦。\x02\x03",
            "#006F我们能找到犯人，\x01",
            "可全是科洛丝的功劳哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P她的身手我们可以担保。\x02\x03",
            "我想至少不用担心\x01",
            "她会成为我们的负担。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#048F艾丝蒂尔、约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F#2P嘁……随你们便吧。\x02\x03",
            "#057F但是你们要知道，\x01",
            "对方可是打倒了卡露娜的家伙。\x02\x03",
            "万事小心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(
        0x105,
        "#040F是，我一定会小心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#1P那就这么定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#3P嗯……\x01",
            "我们快进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3E, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_3_29D end

    def Function_4_A2F(): pass

    label("Function_4_A2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A47")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_4_A2F")

    label("loc_A47")

    Return()

    # Function_4_A2F end

    def Function_5_A48(): pass

    label("Function_5_A48")

    OP_72(0xA, 0x4)
    EventBegin(0x0)
    OP_6D(130, 21350, 6270, 0)
    OP_6C(270000, 0)
    OP_6B(3770, 0)
    OP_72(0x2, 0x8)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0x106, 5)
    SetChrPos(0x9, 5080, 25000, 6100, 0)
    SetChrPos(0xA, 5080, 25000, 6100, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x101, 5080, 25000, 6100, 0)
    SetChrPos(0x102, 5080, 25000, 6100, 0)
    SetChrPos(0x105, 5080, 25000, 6100, 0)
    SetChrPos(0x106, 5080, 25000, 6100, 0)
    OP_6F(0x1, 40)
    OP_70(0x1, 0x50)

    def lambda_B14():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B14)

    def lambda_B24():
        OP_6D(-2320, 25000, -1320, 6000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_B24)
    SetChrPos(0x9, 5080, 25000, 6100, 0)
    SetChrPos(0xA, 5080, 25000, 6100, 0)
    OP_43(0x9, 0x1, 0x0, 0x6)
    Sleep(1000)
    OP_43(0xA, 0x1, 0x0, 0x6)
    Sleep(2500)
    OP_43(0x106, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x101, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x6)
    Sleep(1750)
    OP_4A(0x106, 1)
    OP_51(0x106, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x106, 5)
    SetChrSubChip(0x106, 0)
    Sleep(50)
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(50)
    OP_44(0x105, 0xFF)
    OP_51(0x105, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Fade(1000)
    OP_6D(-240, 25000, -1010, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#014F逃跑用的钢索！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F还、还真是\x01",
            "准备得很周到啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F…………………………\x02\x03",
            "……混蛋秘书和那帮蠢货\x01",
            "就交给你们处理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 800)

    ChrTalk(
        0x106,
        (
            "#054F我要去追那些家伙！\x02\x03",
            "你们几个，把这次事件报告给嘉恩，\x01",
            "然后听他的指示吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 800)
    OP_4B(0x106, 1)

    ChrTalk(
        0x105,
        "#044F啊……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "『好吧，我也去！』\x01",              # 0
            "『真、真是乱来的家伙……』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E1F"),
        (1, "loc_EF7"),
        (SWITCH_DEFAULT, "loc_FCF"),
    )


    label("loc_E1F")


    ChrTalk(
        0x101,
        "#005F好吧，我也去！\x02",
    )

    CloseMessageWindow()

    def lambda_E42():
        OP_8E(0xFE, 0xFFFFF768, 0x61A8, 0xFFFFFBB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E42)
    Sleep(260)
    OP_44(0x101, 0xFF)
    SetChrSubChip(0x101, 6)

    ChrTalk(
        0x102,
        (
            "#012F等一下，艾丝蒂尔。\x01",
            "阿加特不是说了吗？\x02\x03",
            "#012F不能把市长秘书和\x01",
            "『渡鸦帮』的成员们丢下不管。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCF")

    label("loc_EF7")


    ChrTalk(
        0x101,
        (
            "#004F真、真是乱来的家伙……\x02\x03",
            "#004F约修亚，我们也要追吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不……\x01",
            "阿加特不是说了吗？\x02\x03",
            "#012F不能把市长秘书和\x01",
            "『渡鸦帮』的成员们丢下不管。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCF")

    label("loc_FCF")


    ChrTalk(
        0x105,
        (
            "#043F是啊……\x02\x03",
            "虽说是自作自受，\x01",
            "但是他腿上受了伤……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F这样啊……\x02\x03",
            "#007F虽然很不甘心，\x01",
            "不过也只能把追捕的任务交给阿加特了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_24(0x1C5, 0x5F)
    Sleep(200)
    OP_24(0x1C5, 0x5A)
    Sleep(200)
    OP_24(0x1C5, 0x55)
    Sleep(200)
    OP_24(0x1C5, 0x50)
    Sleep(200)
    OP_24(0x1C5, 0x4B)
    Sleep(200)
    OP_24(0x1C5, 0x46)
    Sleep(200)
    OP_24(0x1C5, 0x41)
    Sleep(200)
    OP_23(0x1C5)
    OP_0D()
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……就这样，艾丝蒂尔他们\x01",
            "成功取回了特蕾莎院长被抢走的捐款。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然后，他们把市长秘书和那些不良青年\x01",
            "关押在玛诺利亚的风车小屋里，\x01",
            "这时，天已经开始亮了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x40000000)
    OP_28(0x3E, 0x1, 0x80)
    OP_28(0x3E, 0x1, 0x100)
    Sleep(1000)
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(2500)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2300   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_A48 end

    def Function_6_1245(): pass

    label("Function_6_1245")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1C70, 0x61A8, 0x16B2, 0x1770, 0x0)
    OP_8E(0xFE, 0x1BC6, 0x61A8, 0x97E, 0x1770, 0x0)
    OP_8E(0xFE, 0xED8, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF894, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_96(0xFE, 0xFFFFF484, 0x6590, 0xFFFFF8E4, 0x3E8, 0x1770)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    OP_8F(0xFE, 0xFFFFF1E6, 0x61A8, 0xFFFFF7CC, 0xFA0, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5DC0, 0xFFFFF7CC, 0x1770, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x59D8, 0xFFFFF7CC, 0x1F40, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5208, 0xFFFFF7CC, 0x2710, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x1388, 0xFFFFF7CC, 0x32C8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_1245 end

    def Function_7_1336(): pass

    label("Function_7_1336")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1C70, 0x61A8, 0x16B2, 0x1770, 0x0)
    OP_8E(0xFE, 0x1BC6, 0x61A8, 0x97E, 0x1770, 0x0)
    OP_8E(0xFE, 0xED8, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF894, 0x61A8, 0xFFFFFBB4, 0x1770, 0x0)
    OP_96(0xFE, 0xFFFFF484, 0x6590, 0xFFFFF8E4, 0x3E8, 0x1770)
    OP_8C(0xFE, 45, 400)
    SetChrFlags(0xFE, 0x20)
    OP_8F(0xFE, 0xFFFFF1E6, 0x61A8, 0xFFFFF7CC, 0xFA0, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5DC0, 0xFFFFF7CC, 0x1770, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x59D8, 0xFFFFF7CC, 0x1F40, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x5208, 0xFFFFF7CC, 0x2710, 0x0)
    OP_8F(0xFE, 0xFFFFF1E6, 0x1388, 0xFFFFF7CC, 0x32C8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_1336 end

    def Function_8_1422(): pass

    label("Function_8_1422")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_8_1422 end

    SaveToFile()

Try(main)
