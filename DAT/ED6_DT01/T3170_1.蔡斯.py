from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3170_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3170.x',
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
    OP_67(0, 5630, -10000, 1000)
    OP_4A(0x9, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E6")

    ChrTalk(
        0x9,
        "哦，什么事？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170")

    ChrTalk(
        0x102,
        (
            "#010F您正在工作啊，打扰了。\x02\x03",
            "我们看了公告板，\x01",
            "把您要的食材带来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8")

    label("loc_170")


    ChrTalk(
        0x101,
        (
            "#000F打扰一下可以吗？\x02\x03",
            "我们看了公告板，\x01",
            "把您要的食材带来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8")


    ChrTalk(
        0x101,
        (
            "#000F因为我们还有急事，\x01",
            "所以请快一点好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "哦，好的。\x01",
            "让我看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "唔唔哦哦…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x385)"), scpexpr(EXPR_END)), "loc_8F6")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        "…………………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦，\x01",
            "让我看看这个西红柿。\x02",
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
            "苦西红柿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x9,
        "我来尝尝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        "…………呸、呸呸！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "这、这是什么啊！？\x01",
            "简直苦得要命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F对吧？\x01",
            "这个西红柿很难吃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔唔～嗯，的确，\x01",
            "这个样子是没法吃的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但就凭这个强烈的味道和香味，\x01",
            "如果精心调配的话，\x01",
            "说不定可以弄出很有趣的料理来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F如、如果调配之后还是弄不出好味道，\x01",
            "应该就没有吃的必要了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不见得。\x01",
            "难吃的食材反而会\x01",
            "含有许多对人体很有益的成分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因此遵照传统，\x01",
            "蔡斯这里的料理\x01",
            "采用了各种各样刺激性的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F奇、奇怪的料理～\x02\x03",
            "总、总之这样\x01",
            "委托就算完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦，是啊。\x01",
            "你们等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "……嗯，和肉类搭配起来，\x01",
            "这个苦味也可能成为美味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "给，试验第１号作品。\x02",
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
            "得到了\x07\x02",
            "苦西红柿三明治\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#506F啊、啊哈哈……\x01",
            "多谢您的款待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "呵呵，别介意，尝尝吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么，我也要开工了。\x01",
            "今天谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，再见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_3F(0x385, 1)
    OP_3E(0x199, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找新奇食材】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    OP_A2(0xA)
    Jump("loc_9E3")

    label("loc_8F6")


    ChrTalk(
        0x9,
        "……唔～还不到位啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我需要更加有个性的、\x01",
            "更加有味道的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔～这样啊。\x02\x03",
            "#000F那我们再去找其它的来。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2B, 0x1, 0x1)
    OP_28(0x2B, 0x1, 0x2)

    label("loc_9E3")

    Jump("loc_1350")

    label("loc_9E6")


    ChrTalk(
        0x9,
        "哦，什么事？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A87")

    ChrTalk(
        0x102,
        (
            "#010F您正在工作啊，打扰了。\x02\x03",
            "我们看了公告板，\x01",
            "把您要的食材带来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B47")

    label("loc_A87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD8")

    ChrTalk(
        0x107,
        (
            "#060F你好，贝恩师傅。\x02\x03",
            "我们是来给您\x01",
            "送料理用的食材的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B47")

    label("loc_AD8")


    ChrTalk(
        0x101,
        (
            "#000F打扰一下可以吗？\x02\x03",
            "我们看了公告板，\x01",
            "把您要的食材带来了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    label("loc_B47")


    ChrTalk(
        0x9,
        "好，让我看看。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "唔唔哦哦…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x385)"), scpexpr(EXPR_END)), "loc_1263")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        "…………………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦，\x01",
            "让我看看这个西红柿。\x02",
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
            "苦西红柿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "看起来是个普通的西红柿，\x01",
            "但是香味要浓得多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "我来尝尝，哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        "…………呸、呸呸！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "这、这是什么啊！？\x01",
            "简直苦得要命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F对吧？\x01",
            "这个西红柿很难吃呢。\x02\x03",
            "应该是研究的副产品，\x01",
            "好像不能拿来吃的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "唔唔～嗯，的确，\x01",
            "这个样子是没法吃的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但就凭这个强烈的味道和香味，\x01",
            "如果精心调配的话，\x01",
            "说不定可以弄出很有趣的料理来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F如、如果调配之后还是弄不出好味道，\x01",
            "应该就没有吃的必要了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不见得。\x01",
            "难吃的食材反而会\x01",
            "含有许多对人体很有益的成分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因此遵照传统，\x01",
            "蔡斯这里的料理\x01",
            "采用了各种各样刺激性的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F奇、奇怪的料理～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCF")

    ChrTalk(
        0x107,
        "#067F哈，哈哈……………\x02",
    )

    CloseMessageWindow()

    label("loc_FCF")

    OP_62(0x9, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "……嗯，和肉类搭配起来，\x01",
            "这个苦味也可能成为美味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "看吧，\x01",
            "新料理之试验第１号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就作为你们\x01",
            "帮我寻找优秀食材的奖品吧。\x01",
            "不要顾虑，放心品尝吧。\x02",
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
            "得到了\x07\x02",
            "苦西红柿三明治\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#506F啊、啊哈哈……\x01",
            "多谢您的款待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，那好。\x01",
            "我也要开工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "谢了。\x01",
            "今天多亏你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，再见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x385, 1)
    OP_3E(0x199, 1)
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找新奇食材】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    OP_A2(0xA)
    Jump("loc_1350")

    label("loc_1263")


    ChrTalk(
        0x9,
        "……唔～还不到位啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我需要更加有个性的、\x01",
            "更加有味道的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔～这样啊。\x02\x03",
            "#000F那我们再去找其它的来。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2B, 0x1, 0x1)
    OP_28(0x2B, 0x1, 0x2)

    label("loc_1350")

    EventEnd(0x1)
    OP_4B(0x9, 255)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
