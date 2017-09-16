from ED6ScenarioHelper import *

def main():
    # 洛连特市 民居

    CreateScenaFile(
        FileName            = 'T0111   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0111.x',
        MapIndex            = 11,
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
        '菲特',                                 # 9
        '尤妮',                                 # 10
        '拉欧老人',                             # 11
        '亚尔丽',                               # 12
        '芙莉莎',                               # 13
        '阿妮娅',                               # 14
        '胡里奥',                               # 15
        '加通老大',                             # 16
    )

    DeclEntryPoint(
        Unknown_00              = -76000,
        Unknown_04              = 0,
        Unknown_08              = 32000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -76000,
        Unknown_04              = 0,
        Unknown_08              = 30000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -77000,
        Unknown_04              = 0,
        Unknown_08              = -2000,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 3000,
        Unknown_04              = 0,
        Unknown_08              = 30000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 37000,
        Unknown_04              = 0,
        Unknown_08              = 30000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 11,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01170 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01070 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01170P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01070P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
    )

    DeclNpc(
        X                   = 37069,
        Z                   = 0,
        Y                   = 33566,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 38800,
        Z                   = 0,
        Y                   = 30060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -35400,
        Z                   = 0,
        Y                   = 36030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -39940,
        Z                   = 0,
        Y                   = 33130,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4547,
        Z                   = 0,
        Y                   = 37480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3137,
        Z                   = 0,
        Y                   = 32103,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -35634,
        Z                   = 0,
        Y                   = 31939,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4600,
        Z                   = 0,
        Y                   = 31530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    ScpFunction(
        "Function_0_2FA",          # 00, 0
        "Function_1_3A1",          # 01, 1
        "Function_2_3C3",          # 02, 2
        "Function_3_3D9",          # 03, 3
        "Function_4_3FD",          # 04, 4
        "Function_5_181A",         # 05, 5
        "Function_6_1A90",         # 06, 6
        "Function_7_251B",         # 07, 7
        "Function_8_2D09",         # 08, 8
        "Function_9_2E76",         # 09, 9
        "Function_10_3833",        # 0A, 10
        "Function_11_3C71",        # 0B, 11
    )


    def Function_0_2FA(): pass

    label("Function_0_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_309")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_322")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_322")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_32E")
    ClearChrFlags(0xF, 0x80)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_3A0")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_34C")
    Jump("loc_3A0")

    label("loc_34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_360")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_3A0")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_38C")
    SetChrPos(0xA, -35860, 0, 32500, 172)
    SetChrPos(0xE, -35860, 0, 31320, 357)
    Jump("loc_3A0")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3A0")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_3A0")

    label("loc_3A0")

    Return()

    # Function_0_2FA end

    def Function_1_3A1(): pass

    label("Function_1_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B9")
    OP_B1("t0111_y")
    Jump("loc_3C2")

    label("loc_3B9")

    OP_B1("t0111_n")

    label("loc_3C2")

    Return()

    # Function_1_3A1 end

    def Function_2_3C3(): pass

    label("Function_2_3C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3C3")

    label("loc_3D8")

    Return()

    # Function_2_3C3 end

    def Function_3_3D9(): pass

    label("Function_3_3D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FC")
    OP_8D(0xFE, -447, 33095, 4354, 30386, 4000)
    Jump("Function_3_3D9")

    label("loc_3FC")

    Return()

    # Function_3_3D9 end

    def Function_4_3FD(): pass

    label("Function_4_3FD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "要尤妮一直跟着我生活\x01",
            "的确也不太好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是不是也该像里农的老妈那样\x01",
            "从现在就开始物色女婿呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不，可是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_53E")

    label("loc_4F2")


    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "要尤妮一直跟着我生活\x01",
            "的确也不太好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E")

    Jump("loc_1816")

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_91A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B2")
    OP_A2(0x2A6)

    ChrTalk(
        0xFE,
        (
            "里农的妈妈\x01",
            "到这里找媳妇来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "我家的尤妮还太小了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "而且……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尤妮的夫婿一定要是\x01",
            "能超越我的男人！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F（菲特先生这么热血，\x01",
            "　真少见呀……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，只要是父亲\x01",
            "　应该都会热血沸腾的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "约修亚， \x01",
            "我其实很欣赏你，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你不合格。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为，\x01",
            "谁叫你长得太帅了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且你总是不经意\x01",
            "卷入一些涉及女性的问题上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，我也有同感。\x02\x03",
            "#007F约修亚对这方面的话题\x01",
            "总是唯恐避之不及。\x02\x03",
            "这也是个问题啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（……唯恐避之不及的是你吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_917")

    label("loc_8B2")


    ChrTalk(
        0xFE,
        (
            "嗯，约修亚的话，\x01",
            "年龄相差有些悬殊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是不合格……\x02",
    )

    CloseMessageWindow()

    label("loc_917")

    Jump("loc_1816")

    label("loc_91A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0E")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "你们好，艾丝蒂尔、约修亚。\x01",
            "听说你们最近很活跃啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "镇上人都说你们是\x01",
            "备受期待的年轻一辈游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真不愧是卡西乌斯的孩子啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3E")

    label("loc_A0E")


    ChrTalk(
        0xFE,
        (
            "我也支持你们，\x01",
            "要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3E")

    Jump("loc_1816")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C05")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "十年前，突破边境线\x01",
            "大举入侵而来的帝国军\x01",
            "肆意践踏了整个利贝尔王国……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，通过一次\x01",
            "奇迹般的闪电作战，\x01",
            "我们终于击退了帝国军。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果没有那次作战 \x01",
            "现在这里已经是帝国的领土了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也随洛连特的\x01",
            "部队一起参加了战斗，\x01",
            "但被打伤了腿，变成了现在这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5E")

    label("loc_C05")


    ChrTalk(
        0xFE,
        (
            "如果没有那次作战，\x01",
            "现在这里已经是帝国的领土了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5E")

    Jump("loc_1816")

    label("loc_C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9D")
    OP_A2(0x2A5)

    ChrTalk(
        0xFE,
        (
            "你们俩听你们父亲谈起过\x01",
            "他在军队时的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F没……\x01",
            "他不怎么提起\x01",
            "成为游击士前的事。\x02\x03",
            "#000F不过，\x01",
            "倒是经常提起妈妈的事……\x02\x03",
            "约修亚听说过吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……不，没有呢。\x02\x03",
            "就算问他， \x01",
            "他也总是支吾着岔开话题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F就是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "利贝尔终于恢复和平了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但愿尤妮……\x01",
            "但愿女儿能一直\x01",
            "生活在和平的时代。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E9D")


    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "利贝尔终于恢复和平了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但愿尤妮……\x01",
            "但愿女儿能一直\x01",
            "生活在和平的时代。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F13")

    Jump("loc_1816")

    label("loc_F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_11A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1128")
    OP_A2(0x2A4)

    ChrTalk(
        0x8,
        (
            "为何帕特和鲁克\x01",
            "要跑到北边的塔里面去呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在被魔兽袭击的时候\x01",
            "多亏你们救了他们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "干得不错啊。\x01",
            "不愧是卡西乌斯的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F嗯，唉～不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F实际上最后我们\x01",
            "也陷入了危险之中，\x01",
            "多亏父亲及时赶到帮了我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈，你们俩还年轻嘛，\x01",
            "以后还有很大的潜力可以发掘的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "尤妮也回家了，\x01",
            "没有什么比大家平安无事更好的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A6")

    label("loc_1128")


    ChrTalk(
        0x8,
        (
            "你们两个都还很年轻，\x01",
            "以后还有很大的潜力可以发掘的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没有什么比大家平安无事更好的了。\x02",
    )

    CloseMessageWindow()

    label("loc_11A6")

    Jump("loc_1816")

    label("loc_11A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1424")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CD")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我家的尤妮\x01",
            "也是时候该回来了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "唔，奇怪了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚。\x01",
            "你们如果看见了我家的尤妮\x01",
            "就叫她早些回家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在虽然离晚上\x01",
            "关门的时间还很早……\x01",
            "不过女孩子是要多担心一些才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C0")
    OP_A2(0x1)

    ChrTalk(
        0x8,
        (
            "对了，\x01",
            "尤妮经常和帕特、\x01",
            "鲁克在一起玩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "为什么总是那么喜欢\x01",
            "和男孩子一起玩呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，没、没什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_13C0")


    ChrTalk(
        0x8,
        (
            "现在虽然离晚上\x01",
            "关门的时间还很早……\x01",
            "不过女孩子是要多担心一些才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1421")

    Jump("loc_1816")

    label("loc_1424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179F")
    OP_A2(0x2A3)

    ChrTalk(
        0x8,
        (
            "噢，这不是\x01",
            "艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F早上好啊，\x01",
            "菲特叔叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "卡西乌斯他可还好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，还好，\x01",
            "就是有些忙。\x02\x03",
            "#000F疾病和伤痛\x01",
            "一般都不会找他的麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "呵呵，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我家女儿说\x01",
            "在街上偶尔能看到他，\x01",
            "不过我已经好长时间没见他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果你们不介意的话，\x01",
            "帮我捎个口信给你们父亲好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就说菲特偶尔\x01",
            "想找老朋友叙叙旧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，我会转达的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（……对了，约修亚。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000F（菲特叔叔\x01",
            "　和老爸是什么关系呢？）\x02\x03",
            "#000F（我只知道\x01",
            "　他们是朋友。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F（我听说他们是\x01",
            "　王国军时代的战友。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（啊，是这样的啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_179F")


    ChrTalk(
        0x8,
        (
            "你们回去告诉他，\x01",
            "让他平时有空的时候\x01",
            "也来我家坐坐喝喝茶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "老朋友偶尔叙叙旧\x01",
            "也很不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1816")

    TalkEnd(0x8)
    Return()

    # Function_4_3FD end

    def Function_5_181A(): pass

    label("Function_5_181A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_184F")

    ChrTalk(
        0xFE,
        "爸爸真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我才刚７岁啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_18B1")

    ChrTalk(
        0xFE,
        (
            "爸爸问了我\x01",
            "一件奇怪的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他问我鲁克\x01",
            "和帕特当中选哪个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1941")

    ChrTalk(
        0x9,
        (
            "今天呢，\x01",
            "我一直留在爸爸身边孝顺他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "只要我呆在爸爸身边，\x01",
            "爸爸也就会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_1941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0F")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "艾丝蒂尔姐姐，\x01",
            "约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "谢谢你们救了\x01",
            "帕特和鲁克啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "爱娜姐姐对你们的表现\x01",
            "评价很高呢，\x01",
            "艾丝蒂尔姐姐你们好厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呵呵……\x01",
            "谢谢你的支持，小尤妮……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_1A0F")


    ChrTalk(
        0x9,
        (
            "谢谢你们救了\x01",
            "帕特和鲁克啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "爱娜姐姐对你们的\x01",
            "表现评价很高呢，\x01",
            "艾丝蒂尔姐姐你们好厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8C")

    TalkEnd(0x9)
    Return()

    # Function_5_181A end

    def Function_6_1A90(): pass

    label("Function_6_1A90")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1C50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAD")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "最近的年轻人\x01",
            "就只关注眼前的利益。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我年轻时\x01",
            "也有一段时间瞻前不顾后地\x01",
            "一心只想要得到别人认同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女儿说得没错，\x01",
            "或许他也需要更多的支持和帮助。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4D")

    label("loc_1BAD")


    ChrTalk(
        0xFE,
        (
            "我年轻的时候\x01",
            "也有一段时间瞻前不顾后地\x01",
            "一心只想要得到别人认同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女儿说得没错，\x01",
            "或许他也需要更多的支持和帮助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4D")

    Jump("loc_2517")

    label("loc_1C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAA")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "所谓林业，\x01",
            "并不只是为了利用树木\x01",
            "而栽培树木。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "同时也要守护森林，\x01",
            "与森林相互依存并感谢其恩赐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有领会了这一点，\x01",
            "才能算一个合格的林业工人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "女婿还远远不够格呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1DAA")


    ChrTalk(
        0xFE,
        (
            "要守护森林，\x01",
            "与森林相互依存并感谢其恩赐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有领会了这一点，\x01",
            "才能算一个合格的林业工人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E67")

    Jump("loc_2517")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F97")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "要不是这腰不中用，\x01",
            "我也还能在森林里干干活儿啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "身体这儿疼那儿疼的真叫人懊丧，\x01",
            "我还想再接着工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只靠女婿一个的话总是不放心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2043")

    label("loc_1F97")


    ChrTalk(
        0xFE,
        (
            "要不是这腰不中用，\x01",
            "我也还能在森林里干干活儿啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只靠女婿一个的话总是不放心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2043")

    Jump("loc_2517")

    label("loc_2046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_220A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2168")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "哼，工作就算\x01",
            "进行得顺利了一点，\x01",
            "也不能有骄傲的情绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你作为我女婿想接我的班\x01",
            "还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "必须靠洛连特的林业发展\x01",
            "自己的脚跟才会站稳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2207")

    label("loc_2168")


    ChrTalk(
        0xA,
        (
            "你作为我女婿想接我的班\x01",
            "还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "必须靠洛连特的林业发展\x01",
            "自己的脚跟才会站稳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2207")

    Jump("loc_2517")

    label("loc_220A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CC")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        "哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "太嫩了，\x01",
            "那家伙也不过是个半吊子而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想在两三年内\x01",
            "在林业上做出好成绩来，\x01",
            "这种想法也太天真了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2323")

    label("loc_22CC")


    ChrTalk(
        0xA,
        "哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "太嫩了，\x01",
            "那家伙也不过是个半吊子而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2323")

    Jump("loc_2517")

    label("loc_2326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245F")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "农业、矿业以及林业\x01",
            "是洛连特的三大产业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "说它们是\x01",
            "洛连特的经济支柱\x01",
            "也毫不为过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "其中植树造林，\x01",
            "循环地利用树木作为资源的林业，\x01",
            "是由艾莉茜雅女王的提案发展而来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_245F")


    ChrTalk(
        0xA,
        (
            "无论洛连特的森林资源有多么丰富，\x01",
            "也不是取之不尽的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "女王陛下的想法真是妙啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2517")

    TalkEnd(0xA)
    Return()

    # Function_6_1A90 end

    def Function_7_251B(): pass

    label("Function_7_251B")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D0")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "最近丈夫和父亲\x01",
            "好像少了很多隔阂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太好了啊……\x01",
            "和睦温馨的家庭比什么都要好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2636")

    label("loc_25D0")


    ChrTalk(
        0xFE,
        (
            "我对父亲苦苦的劝说\x01",
            "果然得到了效果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2636")

    Jump("loc_2D05")

    label("loc_2639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_27A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271B")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "父亲不再对丈夫的工作\x01",
            "抱怨不停了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "看他好像有什么话想说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干吗不痛痛快快\x01",
            "说清楚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A6")

    label("loc_271B")


    ChrTalk(
        0xFE,
        (
            "父亲不再对丈夫的工作\x01",
            "抱怨不停了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "看他好像有什么话想说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A6")

    Jump("loc_2D05")

    label("loc_27A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2814")

    ChrTalk(
        0xFE,
        (
            "最近，父亲成天念念叨叨地\x01",
            "在盘算着什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底在想什么呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_28A5")

    ChrTalk(
        0xFE,
        (
            "最近丈夫的工作\x01",
            "好像很顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "父亲也该接受他为继承人了，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_28A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2981")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "刚才买东西时\x01",
            "我就注意到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "新鲜蔬菜\x01",
            "似乎比平时少了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是心理作用吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A19")

    label("loc_2981")


    ChrTalk(
        0xFE,
        (
            "刚才买东西时\x01",
            "我就注意到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "新鲜蔬菜\x01",
            "似乎比平时少了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A19")

    Jump("loc_2D05")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEF")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        "又开始了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我父亲对我丈夫\x01",
            "也太过严厉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "丈夫已经在拼命努力了，\x01",
            "父亲应该把目光放长远一点才好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B94")

    label("loc_2AEF")


    ChrTalk(
        0xB,
        (
            "我父亲对我丈夫\x01",
            "也太过严厉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "丈夫已经在拼命努力了，\x01",
            "父亲应该把目光放长远一点才好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B94")

    Jump("loc_2D05")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2C0F")

    ChrTalk(
        0xB,
        (
            "很快就到\x01",
            "丈夫回来的时间了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "得赶快把晚饭准备好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB1")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "好了～\x01",
            "我丈夫已经工作去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我要快点把\x01",
            "早上的家务弄完，\x01",
            "然后到街上去买菜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2CB1")


    ChrTalk(
        0xB,
        (
            "我要快点把\x01",
            "早上的家务弄完，\x01",
            "然后到街上去买菜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D05")

    TalkEnd(0xB)
    Return()

    # Function_7_251B end

    def Function_8_2D09(): pass

    label("Function_8_2D09")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEE")
    OP_A2(0x7)

    ChrTalk(
        0xE,
        "唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不管怎样，\x01",
            "我接手的那份工作一定要完成才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过想要得到岳父的认可\x01",
            "可是很不容易的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "我要努力加油啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2DEE")


    ChrTalk(
        0xE,
        (
            "不管怎样，\x01",
            "我接手的那份工作一定要完成才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "不过想要得到岳父的认可\x01",
            "可是很不容易的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E72")

    TalkEnd(0xE)
    Return()

    # Function_8_2D09 end

    def Function_9_2E76(): pass

    label("Function_9_2E76")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_3010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F8B")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "老公他终于\x01",
            "从矿山回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "已经好几天没见他了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女儿看到她爸回来肯定会很高兴的，\x01",
            "今天我也要做一顿美餐。\x01",
            "毕竟一家人好久都没一起吃饭了，呵呵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_300D")

    label("loc_2F8B")


    ChrTalk(
        0xFE,
        (
            "今天一家人要吃团圆饭呢。\x01",
            "要早点做好晚饭才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300D")

    Jump("loc_382F")

    label("loc_3010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_31BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3118")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "老公终于有消息了，\x01",
            "说是矿山的工作\x01",
            "就要告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，得准备一顿大餐才行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因为有离别\x01",
            "才更体会得到彼此的牵绊啊，\x01",
            "这样也不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B9")

    label("loc_3118")


    ChrTalk(
        0xFE,
        (
            "老公终于有消息了，\x01",
            "说是矿山的工作\x01",
            "就要告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，得准备一顿大餐才行啊。\x02",
    )

    CloseMessageWindow()

    label("loc_31B9")

    Jump("loc_382F")

    label("loc_31BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_322E")

    ChrTalk(
        0xFE,
        (
            "我听说矿山里\x01",
            "有魔兽出没……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "老公他没事吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_322E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F7")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "刚才老公工作的矿山\x01",
            "发了联络过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说好像是新矿脉中\x01",
            "发现了非同小可的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说是『非同小可』，\x01",
            "到底是什么样的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_32F7")


    ChrTalk(
        0xFE,
        (
            "老公工作的矿山\x01",
            "发现了非同小可的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说是『非同小可』，\x01",
            "到底是什么样的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337F")

    Jump("loc_382F")

    label("loc_3382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_34EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3497")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "老公在矿山\x01",
            "努力地工作，\x01",
            "我也一定要加油呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要这么一想，\x01",
            "和老公的分别\x01",
            "也意外地并不那么难耐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵呵，这也是\x01",
            "爱的其中一种形式吧㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E8")

    label("loc_3497")


    ChrTalk(
        0xFE,
        (
            "老公在矿山\x01",
            "努力地工作，\x01",
            "我也一定要加油呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E8")

    Jump("loc_382F")

    label("loc_34EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_359C")

    ChrTalk(
        0xC,
        (
            "刚才老公联络我说\x01",
            "矿山又发现了\x01",
            "什么新的矿脉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "唉……今天的晚饭\x01",
            "又只有我和女儿两人吃了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_359C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_371E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3687")
    OP_A2(0x6)

    ChrTalk(
        0xC,
        (
            "虽说已经到了\x01",
            "可以开始准备晚餐的时候了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不过不知道老公\x01",
            "今天会不会回来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在矿山里面\x01",
            "通宵的工作\x01",
            "是常有的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371B")

    label("loc_3687")


    ChrTalk(
        0xC,
        (
            "不知道老公\x01",
            "今天会不会回来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在矿山里面\x01",
            "通宵的工作\x01",
            "是常有的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371B")

    Jump("loc_382F")

    label("loc_371E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CC")
    OP_A2(0x6)

    ChrTalk(
        0xC,
        (
            "我的老公\x01",
            "在北面的玛鲁加矿山工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "今天也是\x01",
            "一大早就去上班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "而且经常一连几天\x01",
            "都不能回一次家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_37CC")


    ChrTalk(
        0xC,
        (
            "他这样会因为\x01",
            "劳累过度而病倒的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我真的好担心他啊。\x02",
    )

    CloseMessageWindow()

    label("loc_382F")

    TalkEnd(0xC)
    Return()

    # Function_9_2E76 end

    def Function_10_3833(): pass

    label("Function_10_3833")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_38E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AF")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "爸爸回来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才回来的哦。\x01",
            "他说等一下要和我玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "太好了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E2")

    label("loc_38AF")


    ChrTalk(
        0xFE,
        "我好想早点和爸爸玩呢！\x02",
    )

    CloseMessageWindow()

    label("loc_38E2")

    Jump("loc_3C6D")

    label("loc_38E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_39C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397C")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "嗨！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "听我说听我说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爸爸他、\x01",
            "爸爸他要回家了哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但愿快点到家。\x01",
            "阿妮娅要好好和他一起玩！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BF")

    label("loc_397C")


    ChrTalk(
        0xFE,
        (
            "但愿爸爸快点到家。\x01",
            "阿妮娅要好好和他一起玩！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BF")

    Jump("loc_3C6D")

    label("loc_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3A07")

    ChrTalk(
        0xFE,
        "哎，妈妈没什么精神呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3AB6")

    ChrTalk(
        0xFE,
        (
            "爸爸不在的时候\x01",
            "我就努力给妈妈帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "帮着打扫、\x01",
            "洗衣服、做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很了不起吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3B12")

    ChrTalk(
        0xFE,
        (
            "阿妮娅也马上\x01",
            "要去主日学校上学了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不知道学校好不好玩呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3B60")

    ChrTalk(
        0xD,
        (
            "爸爸今天因为工作\x01",
            "不能回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "唉……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3BB8")

    ChrTalk(
        0xD,
        (
            "阿妮娅\x01",
            "好崇拜爸爸哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "又有力气，\x01",
            "对阿妮娅又温柔～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C41")
    OP_A2(0x5)

    ChrTalk(
        0xD,
        (
            "我爸爸啊，\x01",
            "是在矿场工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "他发现了一个\x01",
            "好漂亮好漂亮的石头哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "他还说\x01",
            "要送给我做礼物哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3C41")


    ChrTalk(
        0xD,
        (
            "我爸爸啊，\x01",
            "是在矿场工作的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6D")

    TalkEnd(0xD)
    Return()

    # Function_10_3833 end

    def Function_11_3C71(): pass

    label("Function_11_3C71")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC3")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "哟，这不是\x01",
            "游击士小姑娘和小兄弟吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，你是玛鲁加矿山的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前给你们添麻烦了，\x01",
            "好在大家最后都平安无事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "矿山的魔兽骚动\x01",
            "终于也告一段落了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也好久\x01",
            "没有回家休息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E00")

    label("loc_3DC3")


    ChrTalk(
        0xFE,
        (
            "果然还是\x01",
            "呆在家里最舒服啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E00")

    TalkEnd(0xF)
    Return()

    # Function_11_3C71 end

    SaveToFile()

Try(main)
