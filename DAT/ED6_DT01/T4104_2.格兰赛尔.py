from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104_2 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_90",           # 01, 1
        "Function_2_B8",           # 02, 2
        "Function_3_D9",           # 03, 3
        "Function_4_13F",          # 04, 4
        "Function_5_16D",          # 05, 5
        "Function_6_19A",          # 06, 6
        "Function_7_1C6",          # 07, 7
        "Function_8_220",          # 08, 8
        "Function_9_26D",          # 09, 9
        "Function_10_2BD",         # 0A, 10
        "Function_11_2FB",         # 0B, 11
        "Function_12_345",         # 0C, 12
        "Function_13_3AC",         # 0D, 13
        "Function_14_3D9",         # 0E, 14
        "Function_15_40A",         # 0F, 15
        "Function_16_433",         # 10, 16
        "Function_17_475",         # 11, 17
        "Function_18_4E4",         # 12, 18
        "Function_19_54A",         # 13, 19
        "Function_20_5C5",         # 14, 20
        "Function_21_631",         # 15, 21
        "Function_22_67A",         # 16, 22
        "Function_23_6AF",         # 17, 23
        "Function_24_6F2",         # 18, 24
        "Function_25_73E",         # 19, 25
        "Function_26_7D5",         # 1A, 26
        "Function_27_800",         # 1B, 27
        "Function_28_869",         # 1C, 28
        "Function_29_8ED",         # 1D, 29
        "Function_30_950",         # 1E, 30
        "Function_31_9BE",         # 1F, 31
        "Function_32_A2C",         # 20, 32
        "Function_33_A82",         # 21, 33
        "Function_34_B11",         # 22, 34
        "Function_35_B35",         # 23, 35
        "Function_36_BBB",         # 24, 36
        "Function_37_D2F",         # 25, 37
        "Function_38_DFB",         # 26, 38
        "Function_39_E25",         # 27, 39
        "Function_40_EB8",         # 28, 40
        "Function_41_EDE",         # 29, 41
        "Function_42_1038",        # 2A, 42
        "Function_43_1212",        # 2B, 43
        "Function_44_1301",        # 2C, 44
        "Function_45_15EB",        # 2D, 45
        "Function_46_19AC",        # 2E, 46
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "比赛快点开始吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_0_66 end

    def Function_1_90(): pass

    label("Function_1_90")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "不管是谁取得优胜都很好啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_1_90 end

    def Function_2_B8(): pass

    label("Function_2_B8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "我现在已经开始兴奋了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_B8 end

    def Function_3_D9(): pass

    label("Function_3_D9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哈～哈，因为兴奋过度，\x01",
            "来得太早了些。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_D9 end

    def Function_4_13F(): pass

    label("Function_4_13F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "今年为谁加油好呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_13F end

    def Function_5_16D(): pass

    label("Function_5_16D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "准决赛要开始了呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_16D end

    def Function_6_19A(): pass

    label("Function_6_19A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "完了，\x01",
            "导力相机忘带了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_19A end

    def Function_7_1C6(): pass

    label("Function_7_1C6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "可惜了！\x01",
            "今年亲卫队没有出战呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1C6 end

    def Function_8_220(): pass

    label("Function_8_220")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "团体赛比想象的要有趣呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_220 end

    def Function_9_26D(): pass

    label("Function_9_26D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我想还是国境警卫队\x01",
            "会取得优胜吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_26D end

    def Function_10_2BD(): pass

    label("Function_10_2BD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今天的对阵\x01",
            "会是怎么样的呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_2BD end

    def Function_11_2FB(): pass

    label("Function_11_2FB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "游击士的两个小组\x01",
            "都还没有出局。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "两组都要加油啊～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_2FB end

    def Function_12_345(): pass

    label("Function_12_345")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "特务部队虽然让人觉得有些害怕，\x01",
            "但实力相当强啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_345 end

    def Function_13_3AC(): pass

    label("Function_13_3AC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "比赛怎么还不开始啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3AC end

    def Function_14_3D9(): pass

    label("Function_14_3D9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "每年的比赛\x01",
            "我都很期待呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_3D9 end

    def Function_15_40A(): pass

    label("Function_15_40A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "今天是总决赛的日子啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_40A end

    def Function_16_433(): pass

    label("Function_16_433")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哪支小组会取胜呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我心里扑通扑通地响呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_433 end

    def Function_17_475(): pass

    label("Function_17_475")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我喜欢游击士组里面\x01",
            "那个金色头发的小哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "外表英俊潇洒，\x01",
            "而且射击方面也无懈可击。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_475 end

    def Function_18_4E4(): pass

    label("Function_18_4E4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我想看那个戴着红色面具的哥哥\x01",
            "和那个像熊一样的叔叔\x01",
            "打架的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4E4 end

    def Function_19_54A(): pass

    label("Function_19_54A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "真不愧是总决赛的日子，\x01",
            "一大早就已经有很多人来了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_54A end

    def Function_20_5C5(): pass

    label("Function_20_5C5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "双方都是今年\x01",
            "第一次参加比赛，\x01",
            "哪一边会取胜的确是决赛的看点啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_5C5 end

    def Function_21_631(): pass

    label("Function_21_631")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "游击士小组里面\x01",
            "好像有个女孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这可真了不起啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_631 end

    def Function_22_67A(): pass

    label("Function_22_67A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "比赛还没有开始吗。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_67A end

    def Function_23_6AF(): pass

    label("Function_23_6AF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "每年只有我和老头子\x01",
            "两个人来看比赛，\x01",
            "感到无聊也没有办法啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_6AF end

    def Function_24_6F2(): pass

    label("Function_24_6F2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "因为太期待今天的比赛了，\x01",
            "我昨天一夜都睡不着觉呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_6F2 end

    def Function_25_73E(): pass

    label("Function_25_73E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我还是觉得\x01",
            "特务部队会取胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一看名字就知道来头不小嘛。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_73E end

    def Function_26_7D5(): pass

    label("Function_26_7D5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "就算口干舌燥\x01",
            "我也要全力为比赛呐喊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_7D5 end

    def Function_27_800(): pass

    label("Function_27_800")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "我支持游击士组哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前我也曾受到\x01",
            "游击士的很多关照啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_800 end

    def Function_28_869(): pass

    label("Function_28_869")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "要是把便当\x01",
            "也带来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一大早就过来排队，\x01",
            "肚子都饿了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_869 end

    def Function_29_8ED(): pass

    label("Function_29_8ED")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "武术大会果然很有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "光是看就已经爽呆了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_8ED end

    def Function_30_950(): pass

    label("Function_30_950")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "游击士组里的那个男孩子\x01",
            "和我儿子的年纪差不多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论如何\x01",
            "我也要支持游击士组。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_950 end

    def Function_31_9BE(): pass

    label("Function_31_9BE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "如果从综合实力来看的话，\x01",
            "不用说也知道\x01",
            "那个特务部队是最强的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_9BE end

    def Function_32_A2C(): pass

    label("Function_32_A2C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "没有想到决赛对阵\x01",
            "会是这样的呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_A2C end

    def Function_33_A82(): pass

    label("Function_33_A82")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "王国军和游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得无论哪一方，\x01",
            "都是保卫我们市民的、\x01",
            "值得大家信赖的好战士。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_A82 end

    def Function_34_B11(): pass

    label("Function_34_B11")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "比赛快要开始了……\x01",
            "我会全力为大家呐喊助威的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_B11 end

    def Function_35_B35(): pass

    label("Function_35_B35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_BB7")

    ChrTalk(
        0x2F,
        (
            "#600F我从年轻的时候就喜欢\x01",
            "观看每年一度的武术大会。\x02\x03",
            "加油啊。\x01",
            "艾丝蒂尔、约修亚，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB7")

    TalkEnd(0xFE)
    Return()

    # Function_35_B35 end

    def Function_36_BBB(): pass

    label("Function_36_BBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C72")

    ChrTalk(
        0xFE,
        (
            "虽说那些对手\x01",
            "的确不容易对付，\x01",
            "不过我坚信你们一定能够取胜的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我会给你们加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D2B")

    label("loc_C72")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "哟，两位新人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们决赛的对手相当强劲，\x01",
            "不过肯定会有胜算的。\x01",
            "我坚信你们一定能够取胜的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我会给你们加油哦。\x02",
    )

    CloseMessageWindow()

    label("loc_D2B")

    TalkEnd(0xFE)
    Return()

    # Function_36_BBB end

    def Function_37_D2F(): pass

    label("Function_37_D2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D8E")

    ChrTalk(
        0xFE,
        (
            "听好，一定要放松，\x01",
            "像往常那样出战就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就连在气势上也要战胜对手。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF7")

    label("loc_D8E")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听好，一定要放松，\x01",
            "像往常那样出战就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就连在气势上也要战胜对手。\x02",
    )

    CloseMessageWindow()

    label("loc_DF7")

    TalkEnd(0xFE)
    Return()

    # Function_37_D2F end

    def Function_38_DFB(): pass

    label("Function_38_DFB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "快点开始吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_DFB end

    def Function_39_E25(): pass

    label("Function_39_E25")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今天我一大早\x01",
            "就去叫了那两个人，\x01",
            "然后来竞技场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为绝对不能错过总决赛啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_E25 end

    def Function_40_EB8(): pass

    label("Function_40_EB8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哪个小组会取胜呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_EB8 end

    def Function_41_EDE(): pass

    label("Function_41_EDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_EEB")
    Jump("loc_1034")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_EF5")
    Jump("loc_1034")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_EFF")
    Jump("loc_1034")

    label("loc_EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_F09")
    Jump("loc_1034")

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_FFB")

    ChrTalk(
        0xFE,
        (
            "想拿个观战的好位置，\x01",
            "所以我在门外彻夜排队，\x01",
            "不料被那些巡逻的士兵赶回了家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之后，我偷偷地从家里溜出来，\x01",
            "躲在大街上的草丛里等那些士兵撤走，\x01",
            "然后才来排队的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1034")

    label("loc_FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1005")
    Jump("loc_1034")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_100F")
    Jump("loc_1034")

    label("loc_100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1019")
    Jump("loc_1034")

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1023")
    Jump("loc_1034")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_102D")
    Jump("loc_1034")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1034")

    label("loc_1034")

    TalkEnd(0xFE)
    Return()

    # Function_41_EDE end

    def Function_42_1038(): pass

    label("Function_42_1038")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1045")
    Jump("loc_120E")

    label("loc_1045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_104F")
    Jump("loc_120E")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1059")
    Jump("loc_120E")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1063")
    Jump("loc_120E")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_10F3")

    ChrTalk(
        0xFE,
        (
            "昨天真是辛苦我丈夫了，\x01",
            "帮我拿到这么一个好座位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说我的要求很任性，\x01",
            "不过没想到他能为我做到这种地步……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_10FD")
    Jump("loc_120E")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "明明和昨天同时来的，\x01",
            "好的座位却都被占了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来明天的决赛\x01",
            "我必须来早一点才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11D0")
    Jump("loc_120E")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_11FD")

    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "今年又到了这个时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120E")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1207")
    Jump("loc_120E")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_120E")

    label("loc_120E")

    TalkEnd(0xFE)
    Return()

    # Function_42_1038 end

    def Function_43_1212(): pass

    label("Function_43_1212")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_121F")
    Jump("loc_12FD")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1229")
    Jump("loc_12FD")

    label("loc_1229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1233")
    Jump("loc_12FD")

    label("loc_1233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_123D")
    Jump("loc_12FD")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_12C4")

    ChrTalk(
        0xFE,
        (
            "今天大家都来到竞技场\x01",
            "为你们呐喊助威。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为游击士协会的代表，\x01",
            "你们一定要为荣誉而战哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FD")

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_12CE")
    Jump("loc_12FD")

    label("loc_12CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_12D8")
    Jump("loc_12FD")

    label("loc_12D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_12E2")
    Jump("loc_12FD")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_12EC")
    Jump("loc_12FD")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_12F6")
    Jump("loc_12FD")

    label("loc_12F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_12FD")

    label("loc_12FD")

    TalkEnd(0xFE)
    Return()

    # Function_43_1212 end

    def Function_44_1301(): pass

    label("Function_44_1301")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1506")
    OP_A2(0x633)

    ChrTalk(
        0x23,
        (
            "#151F啊，是小艾你们啊！\x02\x03",
            "真厉害～！\x01",
            "你们打进决赛了～！\x02\x03",
            "我真是兴奋得都要跳起来了～！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F哈哈，别这么激动嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果不静下心来集中精神的话，\x01",
            "说不定会错过很多精彩的画面哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#150F哎嘿，不用担心啦。\x02\x03",
            "因为我只有在静不下心的时候\x01",
            "才能拍下一些好的照片呢～\x02\x03",
            "这样才有自然感哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不愧是朵洛希……\x01",
            "完全是个另类的天才。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_1506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(
        0x110,
        (
            "#151F小艾你们的精彩表现，\x01",
            "我一定会好好拍下来的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_15E7")

    ChrTalk(
        0x110,
        (
            "#150F嘿嘿，\x01",
            "因为我是负责报道的记者，\x01",
            "所以拿到了特等席位哦。\x02\x03",
            "好了，要赶快准备好照相机了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E7")

    TalkEnd(0x23)
    Return()

    # Function_44_1301 end

    def Function_45_15EB(): pass

    label("Function_45_15EB")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1939")
    OP_A2(0x632)

    ChrTalk(
        0x22,
        (
            "#130F你们好啊。\x01",
            "艾丝蒂尔、约修亚，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎，是亚鲁瓦教授！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F您也来观看比赛吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#130F哈哈，\x01",
            "因为受了你们好多的照顾嘛。\x02\x03",
            "今天是恩人出战决赛的日子，\x01",
            "我想无论如何也要来看一看的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，谢谢啦。\x02\x03",
            "#006F不过，买决赛的门票\x01",
            "肯定花了不少米拉吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#130F哈哈，那也不是。\x02\x03",
            "资料馆的馆长突然有急事，\x01",
            "不能前来观看比赛了。\x02\x03",
            "所以就把这张票免费转让给了我。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F什～么啊，果然还是没付钱嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#130F哈哈……真是不好意思。\x02\x03",
            "不过，我支持你们的信念\x01",
            "是绝对不会输给其他人的。\x02\x03",
            "请你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，包在我们身上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们必定全力出战。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19A8")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(
        0x22,
        (
            "#130F我支持你们的信念\x01",
            "是绝对不会输给其他人的。\x02\x03",
            "请你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A8")

    TalkEnd(0x22)
    Return()

    # Function_45_15EB end

    def Function_46_19AC(): pass

    label("Function_46_19AC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202D")
    OP_A2(0x634)
    OP_8C(0xC, 90, 0)

    ChrTalk(
        0xC,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "克鲁茨前辈，你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xC, 0xF, 0x0, 0x12C, 0xFA0)
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(
        0xC,
        "哎……啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "终于到了决赛呢。\x01",
            "我很期待你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，看我的吧！\x02\x03",
            "#505F……不过，克鲁茨前辈，\x01",
            "你的脸色好像有点不对劲啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊。\x01",
            "脸色铁青铁青呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "没什么……\x01",
            "只是从刚才开始就觉得有点头晕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不过奇怪的是……\x01",
            "我的身体没有什么事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "……难道是那个时候留下的后遗症……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F后、后遗症……\x01",
            "难道是说昨天的比赛吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哈哈，不是不是。\x01",
            "是三个月之前的一次事故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "那时候我好像执行任务失败了，\x01",
            "还弄得自己伤痕累累。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F好像执行任务失败了……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好像是很模糊的说法啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "啊啊，不好意思。\x01",
            "因为那次事故的记忆确实很模糊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "连那是件什么样的工作\x01",
            "也完全记不起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "虽然医生说，\x01",
            "这是因事故所受的刺激……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F是这样啊……\x02\x03",
            "#002F不过，以这样的状态来参加比赛，\x01",
            "不会有事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我刚才已经说了，\x01",
            "其实这不是身体上的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "嗯，跟你们说了一会儿话，\x01",
            "我感觉比刚才舒服多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "已经没事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看起来脸色确实好些了呢。\x01",
            "　\x02\x03",
            "不过……\x01",
            "请不要勉强硬撑着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你们今天一定要\x01",
            "全力出战获取冠军哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    Jump("loc_2072")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2072")

    ChrTalk(
        0xFE,
        (
            "要连我们的份也一起加油，\x01",
            "全力出战获取冠军哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2072")

    TalkEnd(0xC)
    Return()

    # Function_46_19AC end

    SaveToFile()

Try(main)
