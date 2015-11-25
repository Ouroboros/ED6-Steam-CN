from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3300_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3300.x',
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
        "Function_3_14BC",         # 03, 3
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
    OP_6D(1160, 0, 48100, 0)
    OP_6B(2600, 0)
    SetChrPos(0x101, 1200, 0, 47440, 0)
    SetChrPos(0x102, -10, 0, 47200, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E")
    SetChrPos(0x107, 2240, 0, 46790, 0)

    label("loc_10E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D")
    SetChrPos(0x106, 940, 0, 45200, 0)

    label("loc_12D")

    OP_0D()
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88D")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)

    ChrTalk(
        0xFE,
        "……唔、唔～嗯……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)

    ChrTalk(
        0xFE,
        "唔、唔唔、唔唔唔～嗯……\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_63(0xFE)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(
        0xFE,
        (
            "#5S菲、菲！\x01",
            "原谅我吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0xFE,
        "啊…………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 270, 800)
    Sleep(200)
    OP_8C(0xFE, 91, 800)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "刚、刚才\x01",
            "我说了什么吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#509F#2P嗯、嗯，\x01",
            "突然地放声大叫。\x02\x03",
            "说什么『菲！原谅我吧！』。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xFE,
        "唔、哇，连名字都！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#2P嗯？菲……？\x02\x03",
            "好像在哪里听过这个名字……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#064F菲小姐……\x02\x03",
            "是地下工场那个菲小姐吗～？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是为我们准备好\x01",
            "汽油罐的那位工作人员吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F#2P啊，对啊。\x01",
            "是那位女工作员。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "咦？\x01",
            "你们认识菲吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(
        0x101,
        (
            "#000F#2P嗯，不久前，\x01",
            "我们在工作上受到了她的帮助。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        "#010F因为我们是游击士。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 225, 400)

    ChrTalk(
        0xFE,
        "游击士……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这、这可真是太好了，\x01",
            "太谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#2P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F有什么委托吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "虽然是私人问题……\x01",
            "但还是想委托你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#2P嗯～\x01",
            "能帮上忙的话我们当然乐意协助……\x02\x03",
            "#000F#2P……是什么样的委托呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔、唔唔……\x01",
            "我想请你们帮我带一封信给菲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "事实上，\x01",
            "我之前一直在和菲交往……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我对这方面并不在行，\x01",
            "所以她最后还是提出和我分手了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可、可是，我想和她重归于好。\x01",
            "所以就先给她写了一封信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们如果去蔡斯的话，\x01",
            "能不能帮我送一下这封信呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_88D")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "啊，是你们…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么样？\x01",
            "能帮我送信了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB")

    FadeToDark(300, 0, 70)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1209")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(
        0x101,
        (
            "#006F#2P嗯，没问题。\x02\x03",
            "…………约修亚，怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x02\x03",
            "如果不急的话\x01",
            "我们接受下来也无妨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C2")

    label("loc_9AF")


    ChrTalk(
        0x101,
        "#006F#2P嗯，没问题。\x02",
    )

    CloseMessageWindow()

    label("loc_9C2")


    ChrTalk(
        0xFE,
        (
            "太好了！\x01",
            "呀～谢谢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "我就把这个非常重要的东西交给你们了。\x02",
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
            "给菲的情书\x07\x00",
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
            "#006F#2P嗯，这封信就交给我们吧。\x02\x03",
            "#505F#2P可是……好像有些困难啊，\x01",
            "只靠写信能让她回心转意吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        "#064F咦？是～吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xFE,
        "果、果真如此吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，\x01",
            "你认为我们介入\x01",
            "别人的事情是礼貌的举止吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 225, 400)

    ChrTalk(
        0xFE,
        (
            "没、没关系，不用介意，\x01",
            "女性的意见是非常宝贵的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "…………那，怎么办？\x01",
            "只有一封信果然还是不够吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#2P是啊…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#508F#2P啊，对了，\x01",
            "再赠送点礼物如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "啊～礼物对吗，\x01",
            "糟了，我没有准备啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这可就麻烦了，\x01",
            "堡垒这里什么都买不到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2P的确是呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔～对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果可以的话，\x01",
            "拜托你们帮我准备可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P咦…………？\x02\x03",
            "让我们来准备礼物吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "在蔡斯买东西就很方便了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "准备好了之后，\x01",
            "再和这封信一起交给她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#506F#2P好、好吧，\x01",
            "我倒是没什么关系……\x02\x03",
            "#505F不过这么一来，\x01",
            "感觉责任重大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F……艾丝蒂尔，靠你了哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说菲她一般都是\x01",
            "穿着工作服积极地工作着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但她的性格和一般的女孩子差不多，\x01",
            "非常喜欢可爱的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F可爱的东西吗……？\x02\x03",
            "布娃娃……怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(
        0xFE,
        (
            "那、那个有点\x01",
            "太孩子气了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P好吧，\x01",
            "总之就是可爱的东西……对吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "我先把这些米拉作为预付款给你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许不太够，\x01",
            "但礼物的事就拜托你们了。\x02",
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
            "拿到了\x07\x04",
            "１０００\x07\x00",
            "米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    AddMira(1000)

    ChrTalk(
        0x101,
        (
            "#006F嗯，我知道了。\x02\x03",
            "那按照规矩，\x01",
            "确认委托的内容……\x02\x03",
            "在蔡斯城里买一样礼物……\x01",
            "　\x02\x03",
            "把它和信一起交给菲小姐，\x01",
            "对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，就是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x35E, 1)
    OP_28(0x31, 0x4, 0x2)
    OP_28(0x31, 0x4, 0x4)
    OP_28(0x31, 0x4, 0x8)
    OP_28(0x31, 0x1, 0x1)
    OP_28(0x31, 0x1, 0x2)
    OP_28(0x31, 0x1, 0x4)
    OP_28(0x31, 0x1, 0x8)
    OP_A2(0x8)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_14AE")

    label("loc_1209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EC")

    ChrTalk(
        0x101,
        (
            "#007F#2P对、对不起，\x01",
            "现在没有空……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "让您过于期待了。\x02\x03",
            "我们现在正有其他的任务，\x01",
            "要前往亚尔摩那边。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊、好、好吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请不用介意，\x01",
            "只是一点小事而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "实在是对不起，\x01",
            "占用了你们的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F#2P不不，我们才应该说对不起，\x01",
            "没能帮上你的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(800)
    OP_63(0xFE)

    ChrTalk(
        0xFE,
        (
            "…………我说的梦话，\x01",
            "你们大家一定要保密哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A8")

    label("loc_13EC")


    ChrTalk(
        0x101,
        (
            "#003F#2P对不起，\x01",
            "现在我们还有点事要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请不用介意，\x01",
            "只是一点小事而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实在是对不起，\x01",
            "占用了你们的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P拒绝了好几次，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A8")

    OP_28(0x31, 0x1, 0x8000)

    label("loc_14AE")

    OP_4B(0xFE, 255)
    OP_43(0xB, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_14BC(): pass

    label("Function_3_14BC")

    EventBegin(0x0)
    EventEnd(0x0)
    Return()

    # Function_3_14BC end

    SaveToFile()

Try(main)
