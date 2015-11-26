from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2210_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        "Function_1_1838",         # 01, 1
        "Function_2_1874",         # 02, 2
        "Function_3_18B5",         # 03, 3
        "Function_4_18FB",         # 04, 4
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x10, 255)
    SetChrPos(0x101, 500, 0, 200, 0)
    SetChrPos(0x102, -500, 0, 200, 0)
    SetChrPos(0x105, 300, 0, -1300, 0)
    OP_6D(200, 0, 300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_235")
    Sleep(400)
    OP_8C(0x10, 180, 400)

    ChrTalk(
        0x10,
        (
            "#670F呀，是你们啊。\x02\x03",
            "如何，\x01",
            "现在可以去寻找了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232")
    OP_0D()

    ChrTalk(
        0x101,
        "#003F对不起，还是不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F这样啊……\x01",
            "虽然很遗憾，不过没有办法啊。\x02\x03",
            "如果你们有空了，\x01",
            "请尽快到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x20, 0x1, 0x2000)
    EventEnd(0x0)
    OP_4B(0x10, 255)
    OP_8C(0x10, 0, 0)
    Return()

    label("loc_232")

    Jump("loc_775")

    label("loc_235")


    ChrTalk(
        0x10,
        (
            "#673F唔，不见了。\x02\x03",
            "『苍耀之灯火』\x01",
            "居然被盗走了……\x02\x03",
            "#671F而且偏偏还是在这种时候……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x10, 180, 400)
    Sleep(800)

    ChrTalk(
        0x10,
        (
            "#670F呀，是你们啊。\x02\x03",
            "我一直在等你们来呢。\x02\x03",
            "#672F哦？怎么回事，\x01",
            "竟然连科洛丝也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x10, 400)

    ChrTalk(
        0x105,
        "#040F嗯，是我请他们带着我一起来的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_43C")
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#010F我们已经看过公告板了。\x01",
            "　\x02\x03",
            "这次是什么样的情况呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        "#671F请看这边。\x02",
    )

    CloseMessageWindow()

    def lambda_3EB():
        OP_8C(0x102, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EB)
    OP_8C(0x10, 0, 400)

    ChrTalk(
        0x10,
        (
            "#671F这个台座上本来\x01",
            "放有一支作为装饰的烛台。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_510")

    label("loc_43C")

    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#501F等一下……\x02\x03",
            "……有什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        "#671F请看这边。\x02",
    )

    CloseMessageWindow()

    def lambda_49F():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49F)
    OP_8C(0x10, 0, 400)

    ChrTalk(
        0x10,
        (
            "#671F这个台座上本来放着装饰用的烛台，\x01",
            "不知道被谁偷走了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F啊…………\x02",
    )

    CloseMessageWindow()

    label("loc_510")

    OP_28(0x20, 0x4, 0x2)

    ChrTalk(
        0x101,
        (
            "#004F哎呀…………\x02\x03",
            "果然已经无影无踪了啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(
        0x10,
        (
            "#671F正是因为如此，\x01",
            "我希望你们能够尽快找回来……\x02\x03",
            "怎么样，你们有时间吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_775")
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#003F对不起啊，\x01",
            "现在我们还有点事要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F十分抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F没事，没关系的。\x01",
            "你们还有其他的事情要办嘛。\x02\x03",
            "如果待会儿有空了，\x01",
            "就请来帮帮我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，我们就先行告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#670F嗯，待会儿就拜托你们了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x20, 0x1, 0x2000)
    EventEnd(0x0)
    OP_4B(0x10, 255)
    OP_8C(0x10, 0, 0)
    Return()

    label("loc_775")

    OP_28(0x20, 0x4, 0x8)
    OP_28(0x20, 0x4, 0x4)
    OP_28(0x20, 0x1, 0x1)
    OP_28(0x20, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#006F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#670F彼此彼此。\x02\x03",
            "那么我就立刻\x01",
            "说明事情的状况…………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 400)

    ChrTalk(
        0x10,
        (
            "#671F被盗走的是\x01",
            "名为『苍耀之灯火』的烛台。\x02\x03",
            "是在导力革命之后不久\x01",
            "所制造出的导力艺术珍品。\x02\x03",
            "也是这个戴尔蒙家族的传家之宝。\x02\x03",
            "#673F由于这是极为贵重的物品，\x01",
            "一旦被卖出去，\x01",
            "至少可以换来数百万米拉的金钱。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x10, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F数、数百万米拉…………！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#013F…………原来如此。\x02\x03",
            "不过这一点好像并不是\x01",
            "犯人的动机所在。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F嗯？为什么呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F如此高价的物品要想安全地脱手，\x01",
            "必须要经过特殊的渠道才行。\x01",
            "　\x02\x03",
            "然而我认为这次的这个犯人，\x01",
            "不像是有那样的门路。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这样啊………………\x02\x03",
            "虽然偷走了，\x01",
            "但却不能像一般的东西那样换成钱啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        (
            "#672F是呀，总觉得有些奇怪……\x02\x03",
            "这次的偷盗事件，\x01",
            "犯人的动机似乎并不在于金钱啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B22():
        TurnDirection(0x101, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B22)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x101,
        "#004F…………啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F究竟是怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#671F请看看这张卡片。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "『方才蚕食巢穴的乃是比野兽更狂野的兽中之兽。\x01",
            "　\x01",
            "　苍之光将黑暗中迷失的灵魂赞颂并传承。\x01",
            "　让残存之耀得以救赎，而我即为解放者。\x01",
            "　\x01",
            "　啊，探寻者们。\x01",
            "　如女神一般直视真实，抛弃虚伪吧。\x01",
            "　\x01",
            "　前往耸立于此村落中的\x01",
            "　三眼巨人所在之处吧。\x01",
            "　如是，探寻者们，\x01",
            "　汝等将至苍之光所在。\x01",
            "　　　　　　　　　　　　　　　　　　　　怪盗Ｂ』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x102,
        "#012F…………这是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F空空如也的台座上留下的东西。\x01",
            "　\x02\x03",
            "这上面所写的内容\x01",
            "肯定是犯人留下的字句。\x01",
            "我想这点应该是毫无疑问的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#002F也就是说…………\x01",
            "这是犯罪声明之类的东西？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#671F我想大概就是这样，\x01",
            "要不然也不会写成这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F原来是这样，如果是以钱为目的，\x01",
            "就不会费心去弄这样的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E6F():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E6F)
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#042F这篇文章到底是什么意思呢？\x01",
            "　\x02\x03",
            "再细细地品味一下，\x01",
            "有些诗样的感觉呢…………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#013F『苍之光将黑暗中……』是吗。\x02\x03",
            "所谓的『苍之光』\x01",
            "应该就是被盗的烛台吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#671F是的，应该就是如此。\x02",
    )

    CloseMessageWindow()

    def lambda_F81():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F81)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x10,
        (
            "#671F那个烛台，是市民们赠送给\x01",
            "为城市的繁荣发展鞠躬尽瘁的\x01",
            "戴尔蒙家前代的主人的。\x02\x03",
            "#670F如果这么考虑，\x01",
            "『将灵魂赞颂并传承』这一句就讲得通了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#501F哎～原来是这样啊。\x02\x03",
            "那么最后的部分是什么意思呢？\x01",
            "　\x02\x03",
            "为什么感觉上是\x01",
            "为了指引我们才这么写的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F就是这句『前往耸立于此村落中的\x01",
            "　三眼巨人所在之处吧。』\x02\x03",
            "的确是这样……\x01",
            "要去哪里寻找，\x01",
            "已经给了我们提示了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F……意思就是说，\x01",
            "已经提示出了所在地吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#042F『此村落』\x01",
            "应该就是指卢安吧……\x02\x03",
            "在这个城市里的某个地方\x01",
            "有一个所谓的『三眼巨人』…………\x01",
            "我想应该是这个意思吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#505F嗯，\x01",
            "不过为什么要说什么巨人……\x02\x03",
            "不过这个肯定是线索没错啦。\x01",
            "赶快把它仔细地记录下来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#673F唔，\x01",
            "看起来已经没有我再解释的必要了。\x02\x03",
            "#670F那么我先就此失陪了。\x01",
            "我还有一些事情要去处理。\x01",
            "  \x02\x03",
            "接下来就由你们去搜寻了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_132A():
        TurnDirection(0x101, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_132A)

    def lambda_1338():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1338)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，我知道了。\x02\x03",
            "那就首先对屋子\x01",
            "里面进行彻底的搜查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#672F啊，没有这个必要吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F为什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F屋子里面我已经\x01",
            "叫佣人找了个底朝天了。\x02\x03",
            "因此你们只需要\x01",
            "在城里进行搜寻就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F不过…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F犯人留下的卡片\x01",
            "上面留下了很明显的提示。\x02\x03",
            "希望你们能够赶快展开调查。\x01",
            "　\x02\x03",
            "以取回烛台为最首要的目的。\x01",
            "其他的事情你们不需多管。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#015F…………这样啊。\x02\x03",
            "#010F那我们会听取您的建议，\x01",
            "以卡片的提示为根据行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F好吧，既然委托人这样说，\x01",
            "那我们就这样做啦……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        (
            "#673F由专业人士来处理，\x01",
            "就不用我来操心或干预了。\x01",
            "我的工作也非常的繁忙。\x02\x03",
            "希望你们能够理解。\x02\x03",
            "#670F那么…………\x01",
            "接下来就拜托你们了。\x02\x03",
            "我会一直呆在二楼，\x01",
            "如果有什么发现就请随时来找我。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_164A():

        label("loc_164A")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_164A")

    QueueWorkItem2(0x101, 1, lambda_164A)

    def lambda_165B():

        label("loc_165B")

        TurnDirection(0x102, 0x10, 0)
        OP_48()
        Jump("loc_165B")

    QueueWorkItem2(0x102, 1, lambda_165B)

    def lambda_166C():

        label("loc_166C")

        TurnDirection(0x105, 0x10, 0)
        OP_48()
        Jump("loc_166C")

    QueueWorkItem2(0x105, 1, lambda_166C)
    OP_8E(0x10, 0x2134, 0x0, 0x4B0, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    SetChrPos(0x10, 4530, 0, 36330, 90)
    Sleep(1000)

    def lambda_16B3():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16B3)

    def lambda_16C1():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16C1)

    def lambda_16CF():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16CF)
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x11, 0x320)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#003F唉，\x01",
            "为什么会有这么奇怪的事件呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们唯有先根据\x01",
            "卡片上所写的去调查了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#040F在卢安的某个地方\x01",
            "应该会有线索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F与其在这里发呆，\x01",
            "倒不如赶快开始调查。\x02\x03",
            "我们这就行动吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    OP_8C(0x10, 0, 0)
    OP_4B(0x10, 255)
    Return()

    # Function_0_66 end

    def Function_1_1838(): pass

    label("Function_1_1838")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_1853():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1853)
    OP_8E(0xFE, 0x1F4, 0xFFFFFE0C, 0xC8, 0x7D0, 0x0)
    Return()

    # Function_1_1838 end

    def Function_2_1874(): pass

    label("Function_2_1874")

    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_1894():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1894)
    OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFE0C, 0xFFFFFED4, 0x7D0, 0x0)
    Return()

    # Function_2_1874 end

    def Function_3_18B5(): pass

    label("Function_3_18B5")

    Sleep(400)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_18DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18DA)
    OP_8E(0xFE, 0x12C, 0xFFFFFE0C, 0xFFFFFAEC, 0x7D0, 0x0)
    Return()

    # Function_3_18B5 end

    def Function_4_18FB(): pass

    label("Function_4_18FB")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrPos(0x101, 500, 0, 200, 0)
    SetChrPos(0x102, -500, 0, 200, 0)
    SetChrPos(0x105, 300, 0, -1300, 0)
    SetChrPos(0x8, 0, 0, 1800, 180)
    SetChrPos(0x10, 1000, 0, 2000, 180)
    OP_44(0x10, 0xFF)
    OP_44(0x8, 0xFF)
    OP_6D(200, 0, 300, 2000)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F…………事情的经过就是这样。\x02\x03",
            "我们将烛台完好无损地取了回来……\x01",
            "　\x02\x03",
            "#015F不过遗憾的是，\x01",
            "有关犯人的线索\x01",
            "我们至今毫无头绪。\x02\x03",
            "除了知道他自称为『怪盗Ｂ』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，\x01",
            "如果能早点注意到那个是假冒的就好了。\x02\x03",
            "我匆匆忙忙追过去的时候，\x01",
            "他已经逃得无影无踪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661F呵呵，\x01",
            "其实你们已经做得很好了。\x02\x03",
            "能够顺利地取回『苍耀之灯火』，\x01",
            "对我们来说就已经足够了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#678F市长说的极是。\x02\x03",
            "你们已经做得十分出色了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F您的话让我们深感欣慰……\x02\x03",
            "#013F不过，我们让犯人逃跑了，\x01",
            "这是不争的事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，这点是不能让人信服的。\x02\x03",
            "让那个喜欢愚弄人的家伙逍遥法外了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F如果可以的话，\x01",
            "能否让我们再做进一步的搜查？\x02\x03",
            "挨家挨户的搜索，\x01",
            "一定会找到线索的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#662F不用了，没有那个必要。\x02\x03",
            "而且，我的委托里面\x01",
            "并没有说一定要抓到犯人吧。\x02\x03",
            "能够取回烛台就已经足够了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F不过…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#662F约修亚…………\x02\x03",
            "为了正义而奋斗，\x01",
            "你的热情是难能可贵的。\x02\x03",
            "说到底…… \x01",
            "这次的事件最多也只能算是\x01",
            "针对我个人的犯罪。\x02\x03",
            "那些琐碎的细节是其次的，\x01",
            "你们就不用再为这件事而费心了。\x01",
            "　\x02\x03",
            "#664F此时此刻，\x01",
            "我想一定还有其他有需要的人\x01",
            "在等待着你们游击士的帮助。\x02\x03",
            "在我看来，\x01",
            "帮助有困难的人才应该是\x01",
            "你们最优先去做的事情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x8, 400)

    ChrTalk(
        0x10,
        "#672F市长…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F……………………\x02\x03",
            "……我明白了。\x02\x03",
            "#010F那么，\x01",
            "搜查就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#505F唔…………\x01",
            "算了，这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#661F嗯，辛苦你们了，\x01",
            "报酬会通过协会全额支付给你们的。\x02\x03",
            "#660F那么……\x01",
            "我就先失陪了，\x01",
            "还有一大堆的工作在等待我去处理呢。\x02\x03",
            "希望以后\x01",
            "能够看到你们更加杰出的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "我们也就此告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2200   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_4_18FB end

    SaveToFile()

Try(main)
