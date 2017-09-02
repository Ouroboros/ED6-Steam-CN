from ED6ScenarioHelper import *

def main():
    CreateScenaFile(
        FileName            = 'E0012_1 ._SN',
        MapName             = 'event',
        Location            = 'E0012.x',
        MapIndex            = 1,
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 29200, 0, -7430, 270)
    SetChrPos(0x102, 30010, 0, -8090, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4")
    SetChrPos(0x107, 29960, 0, -6410, 225)

    label("loc_F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113")
    SetChrPos(0x106, 31010, 0, -7540, 270)

    label("loc_113")

    OP_6D(28990, 0, -7070, 2000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F菲小姐，\x01",
            "打扰一下好吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x10)
    TalkBegin(0xA)
    OP_4A(0xA, 255)
    ClearChrFlags(0xA, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "嗯？什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F在你正忙的时候来打扰真是抱歉。\x02\x03",
            "#000F这是某人托我们带给您的东西。\x01",
            "　\x02\x03",
            "这个，请您收下。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "给菲的情书\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_3F(0x35E, 1)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "这封信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…………难道说，\x01",
            "是沃尔费堡垒的布拉姆写的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，是的。\x02\x03",
            "#002F（好！\x01",
            "　这就把礼物拿给她。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A0")
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#008F（……哎呀，虽然心里一直惦记着，\x01",
            "　最后还是忘记买礼物了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_7E0")

    label("loc_3A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42B")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41C"),
        (1, "loc_422"),
        (SWITCH_DEFAULT, "loc_428"),
    )


    label("loc_41C")

    OP_A2(0x6)
    Jump("loc_428")

    label("loc_422")

    OP_A2(0x9)
    Jump("loc_428")

    label("loc_428")

    Jump("loc_7E0")

    label("loc_42B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【果馅饼】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4A9"),
        (1, "loc_4AF"),
        (SWITCH_DEFAULT, "loc_4B5"),
    )


    label("loc_4A9")

    OP_A2(0x7)
    Jump("loc_4B5")

    label("loc_4AF")

    OP_A2(0x9)
    Jump("loc_4B5")

    label("loc_4B5")

    Jump("loc_7E0")

    label("loc_4B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【绒毛编织帽】\x01",      # 0
            "【放弃】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_538"),
        (1, "loc_53E"),
        (SWITCH_DEFAULT, "loc_544"),
    )


    label("loc_538")

    OP_A2(0x8)
    Jump("loc_544")

    label("loc_53E")

    OP_A2(0x9)
    Jump("loc_544")

    label("loc_544")

    Jump("loc_7E0")

    label("loc_547")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EB")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",      # 0
            "【果馅饼】\x01",        # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5D6"),
        (1, "loc_5DC"),
        (2, "loc_5E2"),
        (SWITCH_DEFAULT, "loc_5E8"),
    )


    label("loc_5D6")

    OP_A2(0x6)
    Jump("loc_5E8")

    label("loc_5DC")

    OP_A2(0x7)
    Jump("loc_5E8")

    label("loc_5E2")

    OP_A2(0x9)
    Jump("loc_5E8")

    label("loc_5E8")

    Jump("loc_7E0")

    label("loc_5EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_691")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",        # 0
            "【绒毛编织帽】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_67C"),
        (1, "loc_682"),
        (2, "loc_688"),
        (SWITCH_DEFAULT, "loc_68E"),
    )


    label("loc_67C")

    OP_A2(0x6)
    Jump("loc_68E")

    label("loc_682")

    OP_A2(0x8)
    Jump("loc_68E")

    label("loc_688")

    OP_A2(0x9)
    Jump("loc_68E")

    label("loc_68E")

    Jump("loc_7E0")

    label("loc_691")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_739")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【果馅饼】\x01",          # 0
            "【绒毛编织帽】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_724"),
        (1, "loc_72A"),
        (2, "loc_730"),
        (SWITCH_DEFAULT, "loc_736"),
    )


    label("loc_724")

    OP_A2(0x7)
    Jump("loc_736")

    label("loc_72A")

    OP_A2(0x8)
    Jump("loc_736")

    label("loc_730")

    OP_A2(0x9)
    Jump("loc_736")

    label("loc_736")

    Jump("loc_7E0")

    label("loc_739")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【工作手套】\x01",        # 0
            "【果馅饼】\x01",          # 1
            "【绒毛编织帽】\x01",      # 2
            "【放弃】\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7CB"),
        (1, "loc_7CE"),
        (2, "loc_7D4"),
        (3, "loc_7DA"),
        (SWITCH_DEFAULT, "loc_7E0"),
    )


    label("loc_7CB")

    OP_A2(0x6)

    label("loc_7CE")

    OP_A2(0x7)
    Jump("loc_7E0")

    label("loc_7D4")

    OP_A2(0x8)
    Jump("loc_7E0")

    label("loc_7DA")

    OP_A2(0x9)
    Jump("loc_7E0")

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_AAB")

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "这是他送你的礼物。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "工作手套\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "……礼物？\x01",
            "工作手套？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好、好吧，\x01",
            "我收下了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(
        0xFE,
        (
            "哼，真是的，\x01",
            "那个家伙到底在想什么，\x01",
            "我一点都不明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F（唔…………………）\x02\x03",
            "（这、这个礼物\x01",
            "　好像失败了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在不是\x01",
            "说这种话的时候。\x02",
        )
    )

    CloseMessageWindow()

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
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、嗯，再见。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x14D, 1)
    OP_28(0x31, 0x1, 0x40)
    OP_2B(0x31, 0x2)
    Jump("loc_123F")

    label("loc_AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D8D")

    ChrTalk(
        0x101,
        (
            "#000F对了，\x01",
            "这是他送你的礼物。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "果馅饼\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        (
            "谢、谢谢了。\x01",
            "我很高兴…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我最近要\x01",
            "控制甜食的数量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管这样，\x01",
            "却送这样的礼物给我……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(
        0xFE,
        (
            "哼！他不懂得体贴别人这点\x01",
            "看来还是完全没变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F（唔…………………）\x02\x03",
            "（这、这个礼物\x01",
            "　好像失败了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在不是\x01",
            "说这种话的时候。\x02",
        )
    )

    CloseMessageWindow()

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
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x1B2, 1)
    OP_28(0x31, 0x1, 0x80)
    OP_2B(0x31, 0x2)
    Jump("loc_123F")

    label("loc_D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_FD3")

    ChrTalk(
        0x101,
        (
            "#506F啊、嗯，再见。\x01",
            "这是他送你的礼物。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "绒毛编织帽\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0xFE,
        "哇，好可爱呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "他总算是稍微……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……开始为我着想了呢。\x01",
            "呵呵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过既然知道该这样，\x01",
            "为什么不早点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在不是\x01",
            "说这种话的时候。\x02",
        )
    )

    CloseMessageWindow()

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
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，再见了。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x14A, 1)
    OP_28(0x31, 0x1, 0x20)
    OP_2B(0x31, 0x4)
    Jump("loc_123F")

    label("loc_FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1015")

    ChrTalk(
        0x101,
        (
            "#505F（……唔～\x01",
            "　没有看到合适的礼物。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1015")

    Sleep(400)

    ChrTalk(
        0xFE,
        "呼～这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙啊，\x01",
            "肯定是已经反省过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "就算他现在想到要写封信给我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F（唔…………………）\x02\x03",
            "（果然还是应该送点礼物才行……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0xFE,
        "……哎呀，对、对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在不是\x01",
            "说这种话的时候。\x02",
        )
    )

    CloseMessageWindow()

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
            "那…………\x01",
            "我要继续工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F啊、嗯，再见。\x02",
    )

    CloseMessageWindow()
    OP_28(0x31, 0x1, 0x100)

    label("loc_123F")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【爱之使者】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x35E, 1)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x1, 0x10)
    OP_A2(0x5)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xA, 255)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
