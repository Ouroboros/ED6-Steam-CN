from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0100.x',
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_142B",         # 01, 1
        "Function_2_1FB0",         # 02, 2
        "Function_3_287C",         # 03, 3
        "Function_4_3B2A",         # 04, 4
        "Function_5_4261",         # 05, 5
        "Function_6_4286",         # 06, 6
        "Function_7_429F",         # 07, 7
        "Function_8_42B8",         # 08, 8
        "Function_9_4319",         # 09, 9
        "Function_10_4363",        # 0A, 10
        "Function_11_467A",        # 0B, 11
        "Function_12_4914",        # 0C, 12
        "Function_13_493C",        # 0D, 13
        "Function_14_4946",        # 0E, 14
        "Function_15_496B",        # 0F, 15
        "Function_16_4997",        # 10, 16
        "Function_17_49C3",        # 11, 17
        "Function_18_49DF",        # 12, 18
        "Function_19_49FB",        # 13, 19
        "Function_20_4C46",        # 14, 20
        "Function_21_4C58",        # 15, 21
        "Function_22_4CA4",        # 16, 22
        "Function_23_4CC9",        # 17, 23
        "Function_24_4CF5",        # 18, 24
        "Function_25_4D21",        # 19, 25
        "Function_26_4F88",        # 1A, 26
        "Function_27_4F9A",        # 1B, 27
        "Function_28_4FE6",        # 1C, 28
        "Function_29_501D",        # 1D, 29
        "Function_30_5036",        # 1E, 30
        "Function_31_5045",        # 1F, 31
        "Function_32_52E9",        # 20, 32
        "Function_33_52FB",        # 21, 33
        "Function_34_5326",        # 22, 34
        "Function_35_5348",        # 23, 35
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22A")
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "之前真是多谢了。\x01",
            "真的是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里明明是空港城市，\x01",
            "还能坚持卖这些小玩意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我嘛，觉得这样正好哦。\x01",
            "老妈也真是反应迟钝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_224")

    label("loc_17C")


    ChrTalk(
        0xFE,
        (
            "这里明明是空港城市，\x01",
            "还能坚持卖这些小玩意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我嘛，觉得这样正好哦。\x01",
            "老妈也真是反应迟钝。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224")

    TalkEnd(0x12)
    Jump("loc_142A")

    label("loc_22A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x325)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1F")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 31400, 0, 29390, 120)
    SetChrPos(0x102, 30330, 0, 28560, 120)
    OP_4A(0x12, 255)
    OP_6D(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x12,
        "啊…………！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……那块石头。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F难道……\x02\x03",
            "这就是你刚才在找的石头？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "结晶回路的碎片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x12,
        (
            "啊，就是它没错。\x01",
            "我美丽的石头……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)

    ChrTalk(
        0x12,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x12)

    ChrTalk(
        0x12,
        (
            "……怎么回事，\x01",
            "怎么弄得这么脏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F喂喂，\x01",
            "发牢骚也要在表示过谢意之后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "啊，知道啦。\x01",
            "你们是游击士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我可是向游击士协会\x01",
            "付过酬金的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这下我总该有\x01",
            "发牢骚的权利了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F问题的关键根本不在这～里！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，冷静点，\x01",
            "对方只是个孩子而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#009F哼，知道啦。\x02",
    )

    CloseMessageWindow()

    def lambda_54C():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54C)
    Sleep(200)
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(
        0x102,
        (
            "#010F你在找的就是\x01",
            "这块结晶回路的碎片吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "……这块石头，\x01",
            "是结晶回路？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "装在导力器里面的\x01",
            "那种结晶回路？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F嗯，\x01",
            "这的确就是用耀晶片制成的结晶回路。\x02\x03",
            "因为已经碎了，\x01",
            "所以也没什么能量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)

    ChrTalk(
        0x12,
        (
            "这块石头，\x01",
            "果然是结晶回路啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F？？？\x02\x03",
            "怎么回事呢？\x01",
            "干嘛站在那里发呆？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(
        0x12,
        "……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，没什么，没事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不管怎样，\x01",
            "谢谢你们帮我找东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "那就这样吧。\x02",
    )

    CloseMessageWindow()

    def lambda_7C6():

        label("loc_7C6")

        TurnDirection(0x101, 0x12, 400)
        OP_48()
        Jump("loc_7C6")

    QueueWorkItem2(0x101, 1, lambda_7C6)

    def lambda_7D7():

        label("loc_7D7")

        TurnDirection(0x102, 0x12, 400)
        OP_48()
        Jump("loc_7D7")

    QueueWorkItem2(0x102, 1, lambda_7D7)
    OP_8E(0xFE, 0x7D5A, 0x0, 0x5E1A, 0x1388, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x12,
        "啊，对了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x7A12, 0x0, 0x7080, 0x1388, 0x0)

    ChrTalk(
        0x12,
        (
            "……差点忘了，\x01",
            "这东西就给你吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了５个\x07\x02",
            "肉馅丸子\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x1A5, 5)

    ChrTalk(
        0x12,
        (
            "这些肉丸子对身体很有好处，\x01",
            "是老妈刚才给我的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不过味道有些苦，\x01",
            "我不喜欢吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总之，今天还真是谢谢你们啦。\x02",
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0x7D8C, 0x0, 0x46AA, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#007F呼～～\x01",
            "真是个傲慢的小孩啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F一定是因为正值年少气盛吧。\x02\x03",
            "#010F可是，那个孩子……\x02\x03",
            "为什么要寻找\x01",
            "结晶回路这样的东西呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F…………嗯？\x02\x03",
            "这么说来，\x01",
            "的确有点不可思议……\x02\x03",
            "#001F哎呀，管他呢。\x01",
            "每个人喜欢的东西都不一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，说得也是。\x02\x03",
            "说不定那个孩子\x01",
            "对结晶回路非常有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "真不知道那种复杂的机械有什么好。\x02\x03",
            "真是个让我无法理解的世界啊～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，从现在开始\x01",
            "你也要主动去了解才行啊。\x02\x03",
            "如果不能把结晶回路运用自如，\x01",
            "是不能胜任游击士这个工作的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#007F好～啦，我加把劲就是了。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, 62400, 250, 22000, 270)
    OP_3F(0x325, 1)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x1, 0x40)
    OP_44(0x12, 0xFF)
    OP_43(0x12, 0x0, 0x0, 0x8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找发光的石头】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    Jump("loc_142A")

    label("loc_D1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_DDA")
    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "如果你们找到发光石头的话，\x01",
            "赶快来告诉我。应该就在这附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "杂货店这边也找过了，\x01",
            "……接下来该找哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Jump("loc_142A")

    label("loc_DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_12E1")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 31400, 0, 29390, 120)
    SetChrPos(0x102, 30690, 0, 29150, 133)
    OP_4A(0x12, 255)
    OP_6D(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x12,
        "真是奇怪啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……到底掉到哪儿去了呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x12,
        "啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "……喂喂，\x01",
            "我有点事想问你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "在这附近看到过\x01",
            "一块漂亮的石头吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    ChrTalk(
        0x101,
        (
            "#004F啊？\x02\x03",
            "漂亮的石头？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "对呀，漂亮的石头，\x01",
            "闪闪发光的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "那样的石头\x01",
            "会掉到哪儿去呢？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是弄丢的东西吗？\x02\x03",
            "#505F嗯～\x01",
            "我们好像也没看到。\x02\x03",
            "大概掉在什么位置呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "刚才老妈叫我，\x01",
            "我就到杂货铺去了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "一开始石头还在手里的，\x01",
            "回头的时候就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F杂货铺是里农老板开的那间吧。\x01",
            "　\x02\x03",
            "你在杂货铺的门口仔细找过了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "还用你说！\x01",
            "不要把我当成小孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎呀，好傲慢的小子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "还好已经委托游击士了，\x01",
            "相信很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果你们找到发光石头的话，\x01",
            "一定要赶快来告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "我想应该就在这附近。\x02",
    )

    CloseMessageWindow()
    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x1, 0x2)
    OP_65(0x1, 0x1)
    OP_4B(0x12, 255)
    OP_8C(0x12, 45, 0)
    EventEnd(0x0)
    Jump("loc_142A")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_13BD")
    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")

    ChrTalk(
        0xFE,
        (
            "可恶，\x01",
            "到哪里去了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有可能的地方\x01",
            "已经全找过了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B5")

    label("loc_135C")


    ChrTalk(
        0xFE,
        (
            "真是奇怪啊……\x01",
            "为什么会找不到呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，到底掉到哪儿去了。\x02",
    )

    CloseMessageWindow()

    label("loc_13B5")

    ClearChrFlags(0x12, 0x10)
    Jump("loc_1427")

    label("loc_13BD")

    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "这附近有各种各样的破烂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说都是些有趣的东西，\x01",
            "不过通通都不值钱。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)

    label("loc_1427")

    TalkEnd(0x12)

    label("loc_142A")

    Return()

    # Function_0_66 end

    def Function_1_142B(): pass

    label("Function_1_142B")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C0")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "这里明明是空港城市，\x01",
            "还能坚持卖这些小玩意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈反应这么迟钝，真是可叹啊。\x01",
            "哎呀，我说真的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_14C0")


    ChrTalk(
        0xFE,
        (
            "老妈反应这么迟钝，真是可叹啊。\x01",
            "哎呀，我说真的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F7")

    Jump("loc_1FAC")

    label("loc_14FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x325)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1590")
    TurnDirection(0xFE, 0x101, 0)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        "啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……喂，那个。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        (
            "#000F是这个吗？\x01",
            "你要找的齿轮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D2")

    label("loc_1590")


    ChrTalk(
        0xFE,
        "喂喂，我有点事想问你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "在这附近看到过一个齿轮吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        "#000F啊？齿轮？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "对啊。\x01",
            "闪着金属光泽的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "会掉到哪儿去呢？ \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还好已经委托游击士了，\x01",
            "相信很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，说起来。\x02\x03",
            "#000F难道是这个？\x01",
            "你要找的齿轮。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D2")

    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x1, 0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "齿轮\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x325, 1)

    ChrTalk(
        0xFE,
        "啊，就是它没错。我的齿轮……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……怎么回事，怎么弄得这么脏啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F喂喂，\x01",
            "发牢骚也要在表示过谢意之后吧。\x02\x03",
            "#000F这可是我们特地从\x01",
            "排水沟里帮你捞上来的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可是向游击士协会\x01",
            "付过酬金的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这下我总该有发牢骚的权利了吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#002F#5S问题的关键根本不在这～里！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不管怎样，\x01",
            "谢谢你们帮我找东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那就这样吧。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x40)
    OP_43(0x101, 0x0, 0x1, 0x6)
    OP_43(0x102, 0x0, 0x1, 0x7)
    OP_43(0x12, 0x0, 0x1, 0x5)
    OP_A2(0x11)
    OP_A2(0xE)
    OP_A2(0xF)
    OP_A5(0x11)
    OP_A5(0xE)
    OP_A5(0xF)
    SetChrPos(0x12, 62400, 250, 22000, 270)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_85(0x12)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F呼～～真是个傲慢的小孩啊～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，冷静一点。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        "#000F我、我知道啦。\x02",
    )

    CloseMessageWindow()
    OP_8B(0x102, 0x10ACC, 0x9858, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#010F可是，那个孩子……\x02\x03",
            "#010F为什么要找齿轮这样的东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……啊？\x02\x03",
            "#000F嗯，\x01",
            "听你这么一说，的确有点不可思议……\x02\x03",
            "#000F哎呀，管他呢。\x01",
            "每个人喜欢的东西都不一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F哈哈，说得也是。\x02\x03",
            "#010F……那，\x01",
            "那么我们也走吧。\x02\x03",
            "#010F还得回协会\x01",
            "报告一下情况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_30(0x0)
    EventEnd(0x0)
    Jump("loc_1FAC")

    label("loc_1B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1E97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1BE1")

    ChrTalk(
        0xFE,
        (
            "如果你们找到齿轮的话，\x01",
            "赶快来告诉我。应该就在这附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……杂货店这边也找过了，\x01",
            "接下来该找哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E94")

    label("loc_1BE1")

    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x4, 0x2)

    ChrTalk(
        0xFE,
        (
            "喂喂，我有点事想问你们。\x01",
            "在这附近看到过一个齿轮吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        "#000F啊？齿轮？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "对啊。\x01",
            "闪着金属光泽的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "会掉到哪儿去呢？ \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F弄丢了？\x01",
            "嗯～我们好像也没看到。\x02\x03",
            "#000F大概掉在什么位置呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才老妈叫我，\x01",
            "我就到杂货铺去了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一开始石头还在手里的，\x01",
            "回头的时候就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那应该就很可能掉在店前面了。\x01",
            "你已经找过了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还用你说！\x01",
            "不要把我当成小孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F哎呀，好傲慢的小子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还好已经委托游击士了，\x01",
            "相信很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是找到了，赶快来告诉我。\x01",
            "我想应该就在这附近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E94")

    Jump("loc_1FAC")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F49")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "……飞艇这东西真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我来的时候也坐过，\x01",
            "又大又舒服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的经验告诉我，\x01",
            "这东西肯定是由导力器驱动的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAC")

    label("loc_1F49")


    ChrTalk(
        0xFE,
        "不错嘛，飞艇这玩意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的经验告诉我，\x01",
            "这东西肯定是由导力器驱动的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAC")

    TalkEnd(0x12)
    Return()

    # Function_1_142B end

    def Function_2_1FB0(): pass

    label("Function_2_1FB0")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_END)), "loc_2084")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "没办法，再在这里呆一阵\x01",
            "就上格兰赛尔去试试吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家那傻小子\x01",
            "真是一点用都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "才刚帮了一会儿忙\x01",
            "又不知道跑到哪儿去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)
    Jump("loc_266D")

    label("loc_2084")

    OP_A2(0x280)

    ChrTalk(
        0xFE,
        "哈啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特地大老远跑来这里，\x01",
            "真是白折腾一场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又没有顾客，\x01",
            "商店也比想象中的破旧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "乡下果然\x01",
            "就是乡下啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x101,
        "#009F（哼。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "……嗯？\x01",
            "你们是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，不管是谁，\x01",
            "我给你们打折，随便买点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这个木雕小工艺品怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么精细的工艺，\x01",
            "只有在卡尔瓦德才买得到哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F卡尔瓦德，嗯～\x01",
            "是我们的邻国吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F卡尔瓦德共和国是\x01",
            "利贝尔王国东面的国家哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#008F这、这我当然知道啦。\x02",
    )

    CloseMessageWindow()

    def lambda_23E7():
        TurnDirection(0x102, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23E7)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(
        0x102,
        (
            "#010F但是，卡尔瓦德的民间工艺品吗……\x02\x03",
            "我想要是在王都摆卖的话，\x01",
            "一定会更受欢迎的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哈啊……\x01",
            "果然是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来以为稍微乡下点的地方会更好卖，\x01",
            "但这里也实在有点乡下过头了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x101,
        "#009F（哼哼。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "没办法，再在这里呆一阵\x01",
            "就上格兰赛尔去试试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……话说回来，\x01",
            "我家的卡雷尔在做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "才刚帮了一会儿忙\x01",
            "又在到处乱转了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)

    label("loc_266D")

    Jump("loc_2878")

    label("loc_2670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A9")
    OP_A2(0x19)

    ChrTalk(
        0xFE,
        (
            "这里虽然是个小的城镇，\x01",
            "不过商店里东西的品种还是不少哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "托导力器的福， \x01",
            "利贝尔王国和以前大不相同了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，明天要更加努力才行，\x01",
            "销售额可不能降低呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2878")

    label("loc_27A9")


    ChrTalk(
        0xFE,
        (
            "这里虽然是个小的城镇，\x01",
            "不过商店里东西的品种还是不少哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，明天要更加努力才行，\x01",
            "销售额可不能降低呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2878")

    TalkEnd(0x13)
    Return()

    # Function_2_1FB0 end

    def Function_3_287C(): pass

    label("Function_3_287C")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2906")

    ChrTalk(
        0xFE,
        (
            "唔～～啊，\x01",
            "今天天气依旧很暖和啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "睡个午觉\x01",
            "一定很舒服呢～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B21")

    label("loc_2906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_2A17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2960")
    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_2A14")

    label("loc_2960")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29CF")
    OP_28(0x9, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#004F（啊……！）\x02\x03",
            "（小猫回来了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_2A14")

    label("loc_29CF")

    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)

    label("loc_2A14")

    Jump("loc_3B21")

    label("loc_2A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2D2C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B00")
    OP_A2(0x12)
    ClearChrFlags(0x14, 0x10)

    ChrTalk(
        0xFE,
        (
            "哎呀～～\x01",
            "这不是尤基士君吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦呵呵～㈱\x01",
            "要不要和阿姨一起来午睡呢～～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        "#018F……还是免了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_2B00")

    ClearChrFlags(0x14, 0x10)

    ChrTalk(
        0xFE,
        (
            "哎呀～～\x01",
            "这不是尤基士君吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦呵呵～㈱\x01",
            "要不要和阿姨一起来午睡呢～～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")

    Jump("loc_2D29")

    label("loc_2B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2BF8")

    ChrTalk(
        0xFE,
        (
            "尤基士君～\x01",
            "不好意思呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小安莉尔\x01",
            "自己回我这里来了哦～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D29")

    label("loc_2BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CD6")
    OP_28(0x9, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#004F啊……！\x02\x03",
            "猫也会自己回家？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎哟哟～～\x01",
            "这不是尤基士君吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小安莉尔\x01",
            "自己回我这里来了哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～～啊，\x01",
            "多么可爱伶俐的小乖乖啊～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D29")

    label("loc_2CD6")


    ChrTalk(
        0xFE,
        (
            "真是的～～\x01",
            "那个小安莉尔\x01",
            "到底去了哪儿呢～～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真的是好担心呢～～\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～呼。\x02",
    )

    CloseMessageWindow()

    label("loc_2D29")

    Jump("loc_3B21")

    label("loc_2D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2DA7")

    ChrTalk(
        0xFE,
        (
            "已经中午了， \x01",
            "我要好好地睡上顿午觉～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "喂～～小安莉尔～～㈱\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B21")

    label("loc_2DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB5")
    OP_A2(0x12)
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(
        0xFE,
        "找到小安莉尔了吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯！找到了。\x02\x03",
            "#007F……但是又被它给跑掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，怎么会这样呢～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奇怪了啊～\x01",
            "它本来不是很怕陌生人的啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿姨会一直在这里等着的，\x01",
            "拜托了啊，尤基士君。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F55")

    label("loc_2EB5")

    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "真是奇怪啊，怎么会逃跑呢～？\x01",
            "它本来不是很怕陌生人的啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿姨会一直在这里等着的，\x01",
            "拜托了啊，尤基士君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F55")

    Jump("loc_3B21")

    label("loc_2F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_39F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3991")
    OP_28(0x9, 0x4, 0x4)
    OP_28(0x9, 0x4, 0x8)
    OP_28(0x9, 0x4, 0x2)
    OP_28(0x9, 0x1, 0x1)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(36950, 0, 57050, 0)
    OP_6C(0, 0)
    SetChrPos(0x101, 38560, 0, 57230, 270)
    SetChrPos(0x102, 37800, 0, 58080, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF5")
    SetChrPos(0x2, 39290, 0, 58080, 211)
    SetChrPos(0x3, 40280, 0, 58050, 212)
    Jump("loc_3014")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3014")
    SetChrPos(0x2, 39290, 0, 58080, 211)

    label("loc_3014")

    OP_0D()
    Sleep(100)

    ChrTalk(
        0xFE,
        (
            "真是的～\x01",
            "究竟跑到哪儿去了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～～\x01",
            "不知道尤基士看到委托了没有～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F阿姨，您在等游击士吗？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(
        0xFE,
        "嗯，是啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～～？\x01",
            "难道你就是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯⊙我就是游击士。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 0)

    ChrTalk(
        0xFE,
        "难道～那边那位也是～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x14, 0)

    ChrTalk(
        0x102,
        "#010F嗯，我也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀呀，阿姨真的很高兴啊～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近叫做尤基士的人\x01",
            "好像很多呢～～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#501F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，你们好像是姐弟嘛～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对呀，对呀～～\x01",
            "有相同的名字的一般就是一家人的嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x01",
            "可以说是姐弟没错啦……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#014F（……艾丝蒂尔，\x01",
            "　这位阿姨好像不知道什么是游击士啊。）\x02\x03",
            "#014F（她好像把游击士这个词的读音\x01",
            "　当作人的名字了啊。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F（…………不、不会吧～）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～～你们两个\x01",
            "在唧唧喳喳的说些什么呢～～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（有些麻烦啊，只有顺着她的话说了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F（……知道～了。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x14, 400)
    Sleep(200)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(
        0x102,
        (
            "#010F是这样，\x01",
            "您有什么困难吗……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "哎呀～这孩子看上去这么可爱，\x01",
            "没想到洞察力这么敏锐呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "男孩子果然就是用心啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……阿姨，您到底有没有困难？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "啊，对了对了。\x01",
            "说实话啊～\x01",
            "我真的好苦恼的哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的小安莉尔\x01",
            "到现在还没有回来啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我只不过在茶座小睡了一觉，\x01",
            "就那么一不留神，它就不见了～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F小安莉尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是小猫呀～\x01",
            "好可爱的小猫呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且不仅是外表可爱，\x01",
            "内心也好温顺的哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是什么颜色的小猫呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯～让我想想啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像在秋天的夕阳中\x01",
            "那种小麦田的颜色哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……小麦色，对吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它可能正在外面到处乱跑呢，\x01",
            "拜托你们帮我把它捉回来好吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我明白了，\x01",
            "首先从茶座周围开始找吧。\x02\x03",
            "#010F一旦找到了，\x01",
            "我们就会回来告诉您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿姨就在这里\x01",
            "等着你们哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托了啊，尤基士君。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_39F4")

    label("loc_3991")

    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "阿姨就在这里\x01",
            "等着你们哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小安莉尔就拜托你们去找了啊，\x01",
            "尤基士君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F4")

    Jump("loc_3B21")

    label("loc_39F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3A56")

    ChrTalk(
        0xFE,
        "哎～～真是不省心的孩子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是不是在哪儿睡觉呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B21")

    label("loc_3A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3AA1")
    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_3B21")

    label("loc_3AA1")


    ChrTalk(
        0xFE,
        (
            "嗯呼呼呼，\x01",
            "今天天气很暖和哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "可以睡上美美的一觉了～～\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵喵喵～～～咪咪。\x02",
    )

    CloseMessageWindow()

    label("loc_3B21")

    TalkEnd(0x14)
    SetChrFlags(0x14, 0x10)
    Return()

    # Function_3_287C end

    def Function_4_3B2A(): pass

    label("Function_4_3B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3B39")
    Return()

    label("loc_3B39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3CC1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BFF")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F如果想要弄清是什么掉下去的话，\x01",
            "就去地下水路调查一下吧？\x02\x03",
            "地下水路的入口在教堂的后面。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBB")

    label("loc_3BFF")


    ChrTalk(
        0x101,
        (
            "#505F唔……\x01",
            "什么东西掉下去了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F如果想要弄清楚的话，\x01",
            "我们就去下面调查一下吧？\x02\x03",
            "地下水路的入口在教堂的后面。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBB")

    TalkEnd(0xFF)
    Jump("loc_4260")

    label("loc_3CC1")

    OP_28(0x4, 0x1, 0x4)
    OP_28(0x4, 0x1, 0x8)
    OP_28(0x4, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x0, 46120, 0, 26090, 225)
    SetChrPos(0x1, 45540, 0, 27200, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D1D")
    OP_6C(350000, 0)
    Jump("loc_3D3E")

    label("loc_3D1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3E")
    OP_6C(350000, 0)
    Jump("loc_3D3E")

    label("loc_3D3E")

    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB1")
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F……哎？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F那是什么……\x01",
            "排水沟里面好像有东西在发光。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xB176, 0x0, 0x67AC, 0x7D0, 0x0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F………果然。\x02\x03",
            "好像有东西落到排水沟的沟底了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4085")

    label("loc_3EB1")

    Sleep(400)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x102,
        "#014F……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 0)

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F那是什么……\x01",
            "排水沟里面好像有东西在发光。\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xB176, 0x67AC, 0x190)

    ChrTalk(
        0x101,
        "#000F哪里哪里？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xB176, 0x0, 0x67AC, 0x7D0, 0x0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#004F啊，是真的。\x01",
            "还在闪闪发光呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像有东西落到排水沟的沟底了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4085")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F排水沟的沟底？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F你忘记了城里的地下有什么了吗？\x01",
            "　\x02\x03",
            "不久之前我们才去过的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F啊，对呀！是地下水路。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在实地研修时下去过的。\x02\x03",
            "地下水路的入口在教堂的后面。\x01",
            "　\x02\x03",
            "如果想要弄清楚的话，\x01",
            "我们就去下面调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    EventEnd(0x0)

    label("loc_4260")

    Return()

    # Function_4_3B2A end

    def Function_5_4261(): pass

    label("Function_5_4261")

    SetChrFlags(0x12, 0x40)
    OP_A6(0x11)
    OP_8E(0xFE, 0x10ACC, 0x0, 0x9858, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x11)
    Return()

    # Function_5_4261 end

    def Function_6_4286(): pass

    label("Function_6_4286")

    OP_A6(0xE)

    label("loc_4289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_429B")
    TurnDirection(0xFE, 0x12, 0)
    OP_48()
    Jump("loc_4289")

    label("loc_429B")

    OP_A3(0xE)
    Return()

    # Function_6_4286 end

    def Function_7_429F(): pass

    label("Function_7_429F")

    OP_A6(0xF)

    label("loc_42A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_42B4")
    TurnDirection(0xFE, 0x12, 0)
    OP_48()
    Jump("loc_42A2")

    label("loc_42B4")

    OP_A3(0xF)
    Return()

    # Function_7_429F end

    def Function_8_42B8(): pass

    label("Function_8_42B8")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "进入地下水路\x01",      # 0
            "离开\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4301"),
        (1, "loc_430D"),
        (SWITCH_DEFAULT, "loc_4313"),
    )


    label("loc_4301")

    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_4313")

    label("loc_430D")

    TalkEnd(0xFF)
    Jump("loc_4313")

    label("loc_4313")

    Sleep(30)
    Return()

    # Function_8_42B8 end

    def Function_9_4319(): pass

    label("Function_9_4319")

    FadeToBright(500, 0)
    OP_6D(76970, 0, 20370, 0)
    SetChrPos(0x101, 76970, 0, 20370, 180)
    SetChrPos(0x102, 76970, 0, 20370, 0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    Return()

    # Function_9_4319 end

    def Function_10_4363(): pass

    label("Function_10_4363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4370")
    Jump("loc_4679")

    label("loc_4370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4679")
    OP_28(0x9, 0x1, 0x2)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x16, 58830, 0, 40470, 165)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    OP_6D(59150, 0, 42330, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 59390, 0, 55350, 176)
    SetChrPos(0x102, 57010, 0, 55120, 164)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_441A")
    SetChrPos(0x2, 59390, 0, 57350, 176)
    SetChrPos(0x3, 57010, 0, 57120, 164)
    Jump("loc_4439")

    label("loc_441A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4439")
    SetChrPos(0x2, 59390, 0, 57350, 176)

    label("loc_4439")

    OP_0D()

    def lambda_4440():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4440)

    def lambda_4450():
        OP_6D(58950, 0, 46580, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4450)
    OP_8E(0x16, 0xE63C, 0x0, 0xB63A, 0x7D0, 0x0)
    OP_8E(0x101, 0xE61E, 0x0, 0xCC6A, 0x1770, 0x0)

    ChrTalk(
        0x101,
        "#004F啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    def lambda_44D6():
        OP_8E(0x101, 0xE95C, 0x0, 0xAB18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44D6)

    def lambda_44F1():
        OP_8E(0x102, 0xE48E, 0x0, 0xB450, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44F1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454D")

    def lambda_451A():
        OP_8E(0x2, 0xE75E, 0x0, 0xBF5E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_451A)

    def lambda_4535():
        OP_8E(0x3, 0xE394, 0x0, 0xBD56, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4535)
    Jump("loc_4576")

    label("loc_454D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4576")

    def lambda_4561():
        OP_8E(0x2, 0xE75E, 0x0, 0xBF5E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4561)

    label("loc_4576")

    OP_8E(0x16, 0xE6C8, 0x0, 0xAD16, 0x1770, 0x0)

    def lambda_4590():
        OP_6D(59770, 0, 44910, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4590)
    OP_8E(0x16, 0xF082, 0x0, 0x95BA, 0x1770, 0x0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x40)
    WaitChrThread(0x0, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F约修亚，刚才那只小猫……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F似乎就是那位阿姨要找的小猫呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F绝对错不了啦，\x01",
            "快追上它！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4679")

    label("loc_4679")

    Return()

    # Function_10_4363 end

    def Function_11_467A(): pass

    label("Function_11_467A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4687")
    Jump("loc_4913")

    label("loc_4687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4913")
    OP_28(0x9, 0x1, 0x2)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x16, 48900, 0, 84200, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    OP_43(0x16, 0x0, 0x1, 0xC)
    OP_43(0x16, 0x1, 0x1, 0xD)
    Fade(1000)
    SetChrPos(0x2, 47800, 0, 50200, 0)
    SetChrPos(0x3, 46800, 0, 50200, 0)
    Sleep(2000)
    SetChrPos(0x0, 48800, 0, 50200, 0)
    SetChrPos(0x1, 48800, 0, 50200, 0)
    OP_62(0x16, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_8E(0x16, 0xBFCC, 0x0, 0x116E8, 0xBB8, 0x0)
    OP_63(0x16)
    Sleep(500)
    SetChrPos(0x0, 48800, 0, 59200, 0)
    SetChrPos(0x1, 48800, 0, 59200, 0)

    ChrTalk(
        0x101,
        "#004F啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)
    OP_43(0x101, 0x0, 0x1, 0xF)
    OP_43(0x102, 0x0, 0x1, 0x10)
    OP_43(0x16, 0x0, 0x1, 0xE)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A2(0x14)
    OP_A5(0x15)
    OP_A5(0x13)
    OP_A5(0x14)
    SetChrPos(0x16, 5488, 0, 16806, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8)

    ChrTalk(
        0x101,
        "#002F约修亚，刚才那只小猫……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好像是刚才说的那只小猫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F绝对错不了啦，\x01",
            "快追上它！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x2, 48800, 0, 62200, 0)
    SetChrPos(0x3, 48800, 0, 61200, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48CF")
    OP_43(0x10F, 0x0, 0x1, 0x11)
    OP_43(0x110, 0x0, 0x1, 0x12)
    OP_A2(0x17)
    OP_A2(0x16)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_A5(0x16)
    OP_A5(0x17)
    Jump("loc_4902")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_48F4")
    OP_43(0x10F, 0x0, 0x1, 0x11)
    OP_A2(0x16)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_A5(0x16)
    Jump("loc_4902")

    label("loc_48F4")

    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)

    label("loc_4902")

    OP_30(0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x1)
    Jump("loc_4913")

    label("loc_4913")

    Return()

    # Function_11_467A end

    def Function_12_4914(): pass

    label("Function_12_4914")

    OP_6D(49100, 0, 76400, 3000)
    Sleep(500)
    OP_6D(49100, 0, 70400, 2500)
    Return()

    # Function_12_4914 end

    def Function_13_493C(): pass

    label("Function_13_493C")

    OP_6C(0, 3000)
    Return()

    # Function_13_493C end

    def Function_14_4946(): pass

    label("Function_14_4946")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_8E(0x16, 0xE420, 0x0, 0x11170, 0x1B58, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_A3(0x15)
    Return()

    # Function_14_4946 end

    def Function_15_496B(): pass

    label("Function_15_496B")

    OP_A6(0x13)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xC094, 0x0, 0x10108, 0x1B58, 0x0)
    OP_8C(0x101, 45, 0)
    ClearChrFlags(0x101, 0x40)
    OP_A3(0x13)
    Return()

    # Function_15_496B end

    def Function_16_4997(): pass

    label("Function_16_4997")

    OP_A6(0x14)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0xBBE4, 0x0, 0xFE4B, 0xBB8, 0x0)
    OP_8C(0x102, 45, 0)
    ClearChrFlags(0x102, 0x40)
    OP_A3(0x14)
    Return()

    # Function_16_4997 end

    def Function_17_49C3(): pass

    label("Function_17_49C3")

    SetChrFlags(0x10F, 0x40)
    OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
    ClearChrFlags(0x10F, 0x40)
    OP_A3(0x16)
    Return()

    # Function_17_49C3 end

    def Function_18_49DF(): pass

    label("Function_18_49DF")

    SetChrFlags(0x110, 0x40)
    OP_92(0x110, 0x0, 0x0, 0xBB8, 0x0)
    ClearChrFlags(0x110, 0x40)
    OP_A3(0x17)
    Return()

    # Function_18_49DF end

    def Function_19_49FB(): pass

    label("Function_19_49FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4A08")
    Jump("loc_4C45")

    label("loc_4A08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C45")
    OP_28(0x9, 0x1, 0x4)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x16, 60700, 0, 14400, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    Fade(1000)
    OP_43(0x16, 0x0, 0x1, 0x14)
    OP_43(0x16, 0x1, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A8F")
    SetChrPos(0x2, 47400, 0, 50200, 0)
    SetChrPos(0x3, 46400, 0, 50200, 0)
    Jump("loc_4AAE")

    label("loc_4A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAE")
    SetChrPos(0x2, 47400, 0, 50200, 0)

    label("loc_4AAE")

    OP_8E(0x16, 0xC5A8, 0x0, 0x3840, 0xBB8, 0x0)
    OP_8E(0x16, 0xBDD8, 0x0, 0x3DB8, 0xBB8, 0x0)
    SetChrPos(0x0, 48800, 0, 29600, 0)
    SetChrPos(0x1, 48800, 0, 29600, 0)

    ChrTalk(
        0x101,
        "#004F呀！是那只小猫！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8E(0x16, 0xBDD8, 0x0, 0x3E80, 0xBB8, 0x0)
    Sleep(500)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    ChrTalk(
        0x101,
        "#005F你给我站住～～！\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x17)
    OP_43(0x102, 0x0, 0x1, 0x18)
    OP_43(0x16, 0x0, 0x1, 0x16)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A2(0x14)
    OP_A5(0x15)
    OP_A5(0x13)
    OP_A5(0x14)
    SetChrPos(0x16, 5488, 0, 16806, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8)

    ChrTalk(
        0x102,
        (
            "#017F呼～\x01",
            "怎么感觉和帕赛尔农场的情形差不多……\x02\x03",
            "#017F为什么最近总是在追过来赶过去的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x1)
    Jump("loc_4C45")

    label("loc_4C45")

    Return()

    # Function_19_49FB end

    def Function_20_4C46(): pass

    label("Function_20_4C46")

    OP_6D(48800, 0, 16800, 3000)
    Return()

    # Function_20_4C46 end

    def Function_21_4C58(): pass

    label("Function_21_4C58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C79")
    OP_6C(0, 3000)
    Jump("loc_4CA3")

    label("loc_4C79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9A")
    OP_6C(0, 3000)
    Jump("loc_4CA3")

    label("loc_4C9A")

    OP_6C(180000, 3000)

    label("loc_4CA3")

    Return()

    # Function_21_4C58 end

    def Function_22_4CA4(): pass

    label("Function_22_4CA4")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_8E(0x16, 0xD994, 0x0, 0x3840, 0x1B58, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_A3(0x15)
    Return()

    # Function_22_4CA4 end

    def Function_23_4CC9(): pass

    label("Function_23_4CC9")

    OP_A6(0x13)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xBC48, 0x0, 0x4E84, 0x1B58, 0x0)
    OP_8C(0x101, 135, 0)
    ClearChrFlags(0x101, 0x40)
    OP_A3(0x13)
    Return()

    # Function_23_4CC9 end

    def Function_24_4CF5(): pass

    label("Function_24_4CF5")

    OP_A6(0x14)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0xC0F8, 0x0, 0x558C, 0xBB8, 0x0)
    OP_8C(0x102, 135, 0)
    ClearChrFlags(0x102, 0x40)
    OP_A3(0x14)
    Return()

    # Function_24_4CF5 end

    def Function_25_4D21(): pass

    label("Function_25_4D21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4D2E")
    Jump("loc_4F87")

    label("loc_4D2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F87")
    OP_28(0x9, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(180000, 0)
    OP_6D(64629, 0, 38310, 0)
    SetChrPos(0x16, 75500, 0, 40200, 270)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    OP_0D()
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0xFD84, 0x0, 0x9DD0, 0xBB8, 0x0)
    TurnDirection(0x101, 0x16, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F啊，在那里！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFBF4, 0x0, 0x8BD8, 0x1770, 0x0)
    TurnDirection(0x101, 0x16, 0)
    TurnDirection(0x16, 0x101, 0)

    def lambda_4E2C():
        OP_92(0x102, 0x101, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E2C)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x16, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F等一下，艾丝蒂尔，听我说。\x02\x03",
            "#014F那只小猫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，它要跑了！\x02",
    )

    CloseMessageWindow()
    OP_90(0x101, 0x0, 0x0, 0x3E8, 0x1B58, 0x0)
    OP_43(0x101, 0x0, 0x1, 0x1D)
    OP_43(0x16, 0x0, 0x1, 0x1C)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A5(0x15)
    OP_A5(0x13)

    ChrTalk(
        0x101,
        (
            "#005F它朝教会那里跑去了，\x01",
            "这回可一定要把它给捉住！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F唉……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4F87")

    label("loc_4F87")

    Return()

    # Function_25_4D21 end

    def Function_26_4F88(): pass

    label("Function_26_4F88")

    OP_6D(64300, 0, 38200, 3000)
    Return()

    # Function_26_4F88 end

    def Function_27_4F9A(): pass

    label("Function_27_4F9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FBB")
    OP_6C(0, 3000)
    Jump("loc_4FE5")

    label("loc_4FBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FDC")
    OP_6C(0, 3000)
    Jump("loc_4FE5")

    label("loc_4FDC")

    OP_6C(180000, 3000)

    label("loc_4FE5")

    Return()

    # Function_27_4F9A end

    def Function_28_4FE6(): pass

    label("Function_28_4FE6")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0x11BFC, 0x1F4, 0x87F0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x15)
    Return()

    # Function_28_4FE6 end

    def Function_29_501D(): pass

    label("Function_29_501D")

    OP_A6(0x13)

    label("loc_5020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_5032")
    TurnDirection(0x101, 0x16, 0)
    OP_48()
    Jump("loc_5020")

    label("loc_5032")

    OP_A3(0x13)
    Return()

    # Function_29_501D end

    def Function_30_5036(): pass

    label("Function_30_5036")

    OP_92(0x102, 0x101, 0x5DC, 0xBB8, 0x0)
    Return()

    # Function_30_5036 end

    def Function_31_5045(): pass

    label("Function_31_5045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_5052")
    Jump("loc_52E8")

    label("loc_5052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E8")
    OP_28(0x9, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(90000, 0)
    OP_6D(64500, 0, 40400, 0)
    SetChrPos(0x16, 75500, 0, 40200, 270)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x101, 61000, 0, 40300, 90)
    SetChrPos(0x102, 60000, 0, 42300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5111")
    SetChrPos(0x2, 59000, 0, 41300, 90)
    SetChrPos(0x3, 59000, 0, 42800, 90)
    Jump("loc_5130")

    label("loc_5111")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5130")
    SetChrPos(0x2, 59000, 0, 41300, 90)

    label("loc_5130")

    OP_0D()
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0x1016C, 0x0, 0x9DD0, 0xBB8, 0x0)
    TurnDirection(0x101, 0x16, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F啊，在那里！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 0)
    TurnDirection(0x16, 0x101, 0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x16, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F等一下，艾丝蒂尔，听我说。\x02\x03",
            "#014F那只小猫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，它要跑了！\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x22)
    OP_43(0x16, 0x0, 0x1, 0x1C)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A5(0x15)
    OP_A5(0x13)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#005F它朝教会那里跑去了，\x01",
            "这回可一定要把它给捉住！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F唉……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_52E8")

    label("loc_52E8")

    Return()

    # Function_31_5045 end

    def Function_32_52E9(): pass

    label("Function_32_52E9")

    OP_6D(64300, 0, 40200, 3000)
    Return()

    # Function_32_52E9 end

    def Function_33_52FB(): pass

    label("Function_33_52FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_531C")
    OP_6C(90000, 3000)
    Jump("loc_5325")

    label("loc_531C")

    OP_6C(270000, 3000)

    label("loc_5325")

    Return()

    # Function_33_52FB end

    def Function_34_5326(): pass

    label("Function_34_5326")

    OP_A6(0x13)
    OP_90(0x101, 0xBB8, 0x0, 0x0, 0x1B58, 0x0)
    OP_8C(0x101, 135, 400)
    OP_A3(0x13)
    Return()

    # Function_34_5326 end

    def Function_35_5348(): pass

    label("Function_35_5348")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_6C(45000, 0)
    OP_6D(36470, 0, 58400, 0)
    OP_67(0, 11530, -10000, 0)
    OP_6B(2150, 0)
    SetChrPos(0x101, 38560, 0, 57230, 270)
    SetChrPos(0x102, 37800, 0, 58080, 225)
    TurnDirection(0x14, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53E3")
    SetChrPos(0x2, 39290, 0, 58080, 211)
    SetChrPos(0x3, 40280, 0, 58050, 212)
    Jump("loc_5402")

    label("loc_53E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5402")
    SetChrPos(0x2, 39290, 0, 58080, 211)

    label("loc_5402")

    SetChrPos(0x15, 36010, 0, 56150, 36)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x15, 0x40)
    TurnDirection(0x14, 0x102, 0)

    def lambda_542F():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_542F)
    OP_0D()
    Sleep(3000)

    ChrTalk(
        0x102,
        "#010F……事情的经过就是这样的。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F我想刚才安莉尔\x01",
            "可能正要回阿姨您这里来的……\x02\x03",
            "#010F它每次都是朝着茶座这边跑来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "确实，经你这么一说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F或许是我们把它吓跑到其他地方去了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 400)

    ChrTalk(
        0x14,
        (
            "没有～\x01",
            "没关系的啦～～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 0)

    ChrTalk(
        0x14,
        (
            "能够平安无事把它送回我这里来～\x01",
            "我已经很感激了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "特别是这位帅气的尤基士君，\x01",
            "阿姨感动得都要哭了啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵喵～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F您、您实在太客气了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        "#507F（嘿嘿，他害羞啦、他害羞啦。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "呜呜～\x01",
            "阿姨是认真的啊～～㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#511F对、对不起，\x01",
            "我们必须要回协会报告情况了……\x02\x03",
            "告、告辞了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 0)

    ChrTalk(
        0x101,
        "#508F阿姨再见～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "哦呵呵～㈱\x01",
            "再见了～～～～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5821():

        label("loc_5821")

        TurnDirection(0x0, 0x14, 0)
        OP_48()
        Jump("loc_5821")

    QueueWorkItem2(0x0, 1, lambda_5821)

    def lambda_5832():

        label("loc_5832")

        TurnDirection(0x1, 0x14, 0)
        OP_48()
        Jump("loc_5832")

    QueueWorkItem2(0x1, 1, lambda_5832)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5870")

    def lambda_5851():

        label("loc_5851")

        TurnDirection(0x2, 0x14, 0)
        OP_48()
        Jump("loc_5851")

    QueueWorkItem2(0x2, 1, lambda_5851)

    def lambda_5862():

        label("loc_5862")

        TurnDirection(0x3, 0x14, 0)
        OP_48()
        Jump("loc_5862")

    QueueWorkItem2(0x3, 1, lambda_5862)
    Jump("loc_588F")

    label("loc_5870")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_588F")

    def lambda_5884():

        label("loc_5884")

        TurnDirection(0x2, 0x14, 0)
        OP_48()
        Jump("loc_5884")

    QueueWorkItem2(0x2, 1, lambda_5884)

    label("loc_588F")

    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x14, 0x40)

    def lambda_589F():
        OP_8E(0x15, 0x8AB6, 0x0, 0xC7EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_589F)

    def lambda_58BA():
        OP_8E(0x14, 0x8ACA, 0x0, 0xC918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_58BA)
    Sleep(400)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58FF")
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jump("loc_5911")

    label("loc_58FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5911")
    OP_44(0x2, 0x1)

    label("loc_5911")

    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x14, 0x40)
    SetChrPos(0x14, 39420, 250, 51560, 315)
    SetChrPos(0x15, 38700, 0, 50720, 315)
    SetChrChipByIndex(0x14, 20)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找小猫】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_35_5348 end

    SaveToFile()

Try(main)
