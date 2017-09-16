from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '希德少校',                             # 9
        '士兵的声音',                           # 10
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1100,
        Z                   = 0,
        Y                   = -3000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_11D",          # 01, 1
        "Function_2_12A",          # 02, 2
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_106"),
        (SWITCH_DEFAULT, "loc_11C"),
    )


    label("loc_106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119")
    OP_A2(0x570)
    Event(0, 2)

    label("loc_119")

    Jump("loc_11C")

    label("loc_11C")

    Return()

    # Function_0_FA end

    def Function_1_11D(): pass

    label("Function_1_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_129")
    OP_22(0xAC, 0x1, 0x3C)

    label("loc_129")

    Return()

    # Function_1_11D end

    def Function_2_12A(): pass

    label("Function_2_12A")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -820, 0, 4400, 180)
    SetChrPos(0x102, -1790, 0, -440, 0)
    SetChrPos(0x101, -1250, 0, 1250, 0)
    SetChrPos(0x106, -180, 0, 650, 0)
    SetChrPos(0x107, -170, 0, -450, 0)
    SetChrPos(0x10B, -2090, 0, 580, 0)
    OP_6D(-590, 0, 2080, 0)
    OP_67(0, 7290, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#701F真是千钧一发啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F果然……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#700F为了保险起见，快把门锁上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F知道了。\x02",
    )

    CloseMessageWindow()

    def lambda_266():

        label("loc_266")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_266")

    QueueWorkItem2(0x101, 1, lambda_266)

    def lambda_277():

        label("loc_277")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_277")

    QueueWorkItem2(0x106, 1, lambda_277)

    def lambda_288():

        label("loc_288")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_288")

    QueueWorkItem2(0x107, 1, lambda_288)

    def lambda_299():

        label("loc_299")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_299")

    QueueWorkItem2(0x10B, 1, lambda_299)
    OP_8E(0x102, 0xFFFFFBD2, 0x0, 0xFFFFF9B6, 0xBB8, 0x0)
    OP_8C(0x102, 180, 400)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x102, 0x8, 400)
    Sleep(100)

    def lambda_2E0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E0)

    def lambda_2EE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2EE)

    def lambda_2FC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2FC)

    def lambda_30A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_30A)

    def lambda_318():
        OP_6D(-740, 0, 3380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_318)

    def lambda_330():

        label("loc_330")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_330")

    QueueWorkItem2(0x101, 2, lambda_330)

    def lambda_341():
        OP_8E(0xFE, 0xFFFFFC22, 0x0, 0xADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_341)
    Sleep(200)

    def lambda_361():

        label("loc_361")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_361")

    QueueWorkItem2(0x106, 2, lambda_361)

    def lambda_372():
        OP_8E(0xFE, 0x1E0, 0x0, 0xD02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_372)
    Sleep(100)

    def lambda_392():

        label("loc_392")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_392")

    QueueWorkItem2(0x10B, 2, lambda_392)

    def lambda_3A3():
        OP_8E(0xFE, 0xFFFFF844, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3A3)
    Sleep(100)

    def lambda_3C3():

        label("loc_3C3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3C3")

    QueueWorkItem2(0x107, 2, lambda_3C3)

    def lambda_3D4():
        OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0x820, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3D4)
    Sleep(200)

    def lambda_3F4():
        OP_8E(0xFE, 0xFFFFF858, 0x0, 0x866, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F4)
    Sleep(2500)

    ChrTalk(
        0x10B,
        (
            "#102F哼，你打算怎么样？\x01",
            "雷斯顿要塞的守备队长。\x02\x03",
            "那个理查德上校\x01",
            "刚刚不是命令你要严密地监视我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F……那个时候真是失礼了。\x02\x03",
            "#700F现在王国军已经被\x01",
            "上校所管辖的情报部控制了。\x02\x03",
            "军中的主要将领不是被上校收服，\x01",
            "就是被剥夺了自由……\x02\x03",
            "摩尔根将军也被监禁在哈肯大门……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F咦咦咦！？\x01",
            "连那个顽固的老爷爷也……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F情况好像变得很糟糕啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#055F喂喂……\x01",
            "到底为什么会变成这样？\x02\x03",
            "王国军不是那么脆弱的组织吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F很遗憾……\x01",
            "和帝国的战争结束后，\x01",
            "王国军的军纪就渐渐散漫了。\x02\x03",
            "特别是将领级别之间，\x01",
            "互相攀比，争斗，受贿不断。\x02\x03",
            "理查德上校就是钻了这个空子。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F原来如此……\x01",
            "利用其特有的情报掌控能力，\x01",
            "然后逐一找到竞争对手的弱点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#700F就是这样。\x02\x03",
            "现在摩尔根将军被监禁着，\x01",
            "王国军实权已经落在了理查德上校手上。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F怎、怎么会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F艾莉茜雅女王怎么样了？\x02\x03",
            "王国军的指挥权\x01",
            "最终还是归属于女王的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F虽然不清楚情况……\x01",
            "但女王陛下一直保持着沉默。\x02\x03",
            "女王陛下直属的王室亲卫队\x01",
            "刚刚也以谋反的罪名被追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F谋、谋反！？\x02\x03",
            "尤莉亚中尉他们！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#702F他们将中央工房袭击事件\x01",
            "伪装成王室亲卫队的所为。\x02\x03",
            "竟然周全到连照片都准备了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F朵洛希的照片……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F这、这太过分了！\x02\x03",
            "#561F不仅把工房搞得乱七八糟，\x01",
            "而且还绑架了爷爷……\x02\x03",
            "连阿加特大哥哥也差点被他们……\x01",
            "　\x02\x03",
            "#062F之后居然还嫁祸于人！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F啊……我无可辩驳。\x02\x03",
            "虽说上级的命令不可不从……\x01",
            "但是，默许的我也有不可推卸的责任。\x02\x03",
            "#701F因此……\x01",
            "至少请让我在此向大家赎罪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F真是忠义两难全啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#104F嗯，既然这样，\x01",
            "以前的种种恩怨就付诸流水吧。\x02\x03",
            "先让我用扳手敲敲你这木鱼脑袋，\x01",
            "然后就饶了你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#702F不、不胜惶恐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F爷、爷爷真是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#100F开玩笑嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F事情我们明白了……\x01",
            "不过接下来你打算怎么办？\x02\x03",
            "让我们藏到风声过去吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#700F不，我还有个更安全的办法。\x01",
            "　\x02\x03",
            "我可以帮你们通过这个房间\x01",
            "安全地逃出雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F这个房间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此，\x01",
            "这里有逃脱的密道吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#701F呵呵，很敏锐啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)

    def lambda_F71():

        label("loc_F71")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F71")

    QueueWorkItem2(0x101, 1, lambda_F71)

    def lambda_F82():

        label("loc_F82")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F82")

    QueueWorkItem2(0x106, 1, lambda_F82)

    def lambda_F93():

        label("loc_F93")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F93")

    QueueWorkItem2(0x107, 1, lambda_F93)

    def lambda_FA4():

        label("loc_FA4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FA4")

    QueueWorkItem2(0x10B, 1, lambda_FA4)

    def lambda_FB5():
        OP_6D(3440, 0, 9720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FB5)

    def lambda_FCD():
        OP_8E(0xFE, 0xD02, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FCD)

    def lambda_FE8():

        label("loc_FE8")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_FE8")

    QueueWorkItem2(0x8, 1, lambda_FE8)
    Sleep(800)

    def lambda_FFE():

        label("loc_FFE")

        OP_8C(0xFE, 45, 0)
        OP_48()
        Jump("loc_FFE")

    QueueWorkItem2(0x106, 1, lambda_FFE)

    def lambda_100F():
        OP_8E(0xFE, 0x9D8, 0x0, 0x1DBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_100F)
    Sleep(50)

    def lambda_102F():

        label("loc_102F")

        OP_8C(0xFE, 45, 0)
        OP_48()
        Jump("loc_102F")

    QueueWorkItem2(0x107, 1, lambda_102F)

    def lambda_1040():
        OP_8E(0xFE, 0x794, 0x0, 0x1A86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1040)
    Sleep(100)

    def lambda_1060():

        label("loc_1060")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_1060")

    QueueWorkItem2(0x101, 1, lambda_1060)

    def lambda_1071():
        OP_8E(0xFE, 0x726, 0x0, 0x208A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1071)
    Sleep(350)

    def lambda_1091():

        label("loc_1091")

        OP_8C(0xFE, 45, 0)
        OP_48()
        Jump("loc_1091")

    QueueWorkItem2(0x10B, 1, lambda_1091)

    def lambda_10A2():
        OP_8E(0xFE, 0xAF0, 0x0, 0x1A86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_10A2)
    Sleep(50)

    def lambda_10C2():

        label("loc_10C2")

        OP_8C(0xFE, 90, 0)
        OP_48()
        Jump("loc_10C2")

    QueueWorkItem2(0x102, 1, lambda_10C2)

    def lambda_10D3():
        OP_8E(0xFE, 0x3E8, 0x0, 0x1B6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10D3)
    WaitChrThread(0x8, 0x2)
    Sleep(100)
    OP_70(0x0, 0xF0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#004F哇哇……\x02",
    )

    CloseMessageWindow()
    OP_73(0x0)
    OP_44(0x8, 0xFF)
    OP_8C(0x8, 0, 400)
    OP_8E(0x8, 0xA46, 0x0, 0x27EC, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x106,
        (
            "#051F不愧是要塞的司令室，\x01",
            "各方面都很有一套嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F使用这个紧急逃脱口，\x01",
            "就能通往要塞内部的水道。\x02\x03",
            "而且船已经准备好了，\x01",
            "这样你们就能完全逃离这里。\x02\x03",
            "#701F本来把这个秘密告诉外人\x01",
            "要被判处十年的监禁……\x02\x03",
            "哈哈……就算军规不能原谅，\x01",
            "我想女神也会原谅我吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12D4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D4)

    def lambda_12E2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12E2)

    def lambda_12F0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_12F0)

    def lambda_12FE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12FE)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0x107,
        "#063F少校先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F那我们就不客气了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)
    Sleep(400)

    ChrTalk(
        0x106,
        (
            "#050F#2P我最先下去，\x01",
            "接下来是老爷子和提妲。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(
        0x106,
        (
            "#054F#2P艾丝蒂尔、约修亚，\x01",
            "殿后就交给你们两个了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13D8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13D8)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        "#006F知道了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x10B, 0x4)
    SetChrFlags(0x107, 0x4)
    OP_8E(0x106, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x106, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)

    ChrTalk(
        0x10B,
        "#100F少校，再见了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10B, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x10B, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)

    ChrTalk(
        0x107,
        (
            "#560F嗯，那个……\x01",
            "真的非常感谢您呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x107, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x107, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)

    def lambda_14EE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14EE)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#006F好了……\x01",
            "只剩下我们两个了。\x02\x03",
            "少校，多谢你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xAA0, 0x0, 0x1DE2, 0xBB8, 0x0)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#010F承蒙您的关照了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F不，你们太客气了。\x02\x03",
            "其实……\x01",
            "当我最初遇到你们的时候，\x01",
            "我就预料到事情会变成这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F最初遇到的时候……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F在大门遇到的时候吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#701F啊啊……\x01",
            "听到你们俩名字的那时候。\x02\x03",
            "你们是卡西乌斯上校的孩子吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F卡西乌斯上校……\x02\x03",
            "#004F哎哎……\x01",
            "老爸有这么高的军衔吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#703F嗯，我和那个理查德上校\x01",
            "都曾经是他的直属部下。\x02\x03",
            "卡西乌斯上校是十年前\x01",
            "百日战役时击退帝国军的英雄啊……\x02\x03",
            "#701F我想他的孩子们\x01",
            "一定会为了追查真相，\x01",
            "前来要塞营救博士的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F是、是这样吗……\x02\x03",
            "不过……\x01",
            "老爸居然是击退帝国军的英雄……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x72, 0x0, 0x64)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_18FE():
        OP_6D(1910, 0, 8160, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18FE)

    def lambda_1916():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1916)

    def lambda_1924():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1924)
    TurnDirection(0x101, 0x9, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x9,
        "少校，可以进来吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "入侵者似乎来过地牢！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他们依然潜伏在司令部的可能性很高，\x01",
            "请问可以让我们进来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F不、不好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#704F#3S知道了！\x01",
            "你们先原地待命！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A40():
        OP_6D(3440, 0, 9720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A40)

    def lambda_1A58():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A58)

    def lambda_1A66():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A66)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        "#702F好了，你们快走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯、嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那么我们告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_1AD5():
        OP_8E(0xFE, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AD5)
    Sleep(600)

    def lambda_1AF5():

        label("loc_1AF5")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1AF5")

    QueueWorkItem2(0x8, 1, lambda_1AF5)
    OP_8E(0x102, 0xCEE, 0x0, 0x226A, 0x1388, 0x0)
    OP_8E(0x102, 0x1EA0, 0x0, 0x2328, 0x1388, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0x44, 0x1, 0x800)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3114   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_12A end

    SaveToFile()

Try(main)
