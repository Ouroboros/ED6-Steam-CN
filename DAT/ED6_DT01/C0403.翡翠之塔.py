from ED6ScenarioHelper import *

def main():
    # 翡翠之塔

    CreateScenaFile(
        FileName            = 'C0403   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 16,
        MapDefaultBGM       = "ed60033",
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
        '阿加特',                               # 9
        '金',                                   # 10
        '幽灵骸骨鱼',                           # 11
        '亚鲁瓦教授',                           # 12
        '约修亚',                               # 13
        '奈尔',                                 # 14
        '朵洛希',                               # 15
        '目标用摄像机',                         # 16
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 16,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = -3000,
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 16,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00390 ._CH',             # 00
        'ED6_DT07/CH00391 ._CH',             # 01
        'ED6_DT07/CH00170 ._CH',             # 02
        'ED6_DT07/CH00171 ._CH',             # 03
        'ED6_DT09/CH10090 ._CH',             # 04
        'ED6_DT09/CH10091 ._CH',             # 05
        'ED6_DT07/CH02050 ._CH',             # 06
        'ED6_DT07/CH00010 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT06/CH20063 ._CH',             # 09
        'ED6_DT06/CH20064 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00390P._CP',             # 00
        'ED6_DT07/CH00391P._CP',             # 01
        'ED6_DT07/CH00170P._CP',             # 02
        'ED6_DT07/CH00171P._CP',             # 03
        'ED6_DT09/CH10090P._CP',             # 04
        'ED6_DT09/CH10091P._CP',             # 05
        'ED6_DT07/CH02050P._CP',             # 06
        'ED6_DT07/CH00010P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT06/CH20063P._CP',             # 09
        'ED6_DT06/CH20064P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4830,
        Z                   = 250,
        Y                   = 7810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 1600,
        Y                   = 1000,
        Z                   = -2680,
        Range               = -1600,
        Unknown_10          = 0xFFFFF830,
        Unknown_14          = 0xFFFFE82C,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_309",          # 01, 1
        "Function_2_324",          # 02, 2
        "Function_3_4A1",          # 03, 3
        "Function_4_10AD",         # 04, 4
        "Function_5_156C",         # 05, 5
        "Function_6_157B",         # 06, 6
        "Function_7_1FAE",         # 07, 7
        "Function_8_26C7",         # 08, 8
        "Function_9_48FB",         # 09, 9
        "Function_10_4915",        # 0A, 10
        "Function_11_493B",        # 0B, 11
        "Function_12_4955",        # 0C, 12
        "Function_13_496F",        # 0D, 13
        "Function_14_49AA",        # 0E, 14
        "Function_15_4AE4",        # 0F, 15
        "Function_16_4B80",        # 10, 16
        "Function_17_4BDE",        # 11, 17
        "Function_18_4EEE",        # 12, 18
        "Function_19_4F4E",        # 13, 19
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27E")
    EventBegin(0x0)
    OP_28(0x19, 0x1, 0x80)
    Event(0, 8)

    label("loc_27E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_28A"),
        (SWITCH_DEFAULT, "loc_308"),
    )


    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 6)), scpexpr(EXPR_END)), "loc_305")
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x108, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -1000, 0, -1600, 0)
    SetChrPos(0x9, 500, 0, -2620, 0)
    SetChrChipByIndex(0x8, 1)
    SetChrChipByIndex(0x9, 3)
    OP_6D(0, 0, -10700, 0)
    OP_6C(45000, 0)
    Event(0, 17)

    label("loc_305")

    Jump("loc_308")

    label("loc_308")

    Return()

    # Function_0_266 end

    def Function_1_309(): pass

    label("Function_1_309")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_323")

    Return()

    # Function_1_309 end

    def Function_2_324(): pass

    label("Function_2_324")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_48B")

    label("loc_349")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_48B")

    label("loc_362")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_48B")

    label("loc_37B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_394")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_48B")

    label("loc_394")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_48B")

    label("loc_3AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_48B")

    label("loc_3C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_48B")

    label("loc_3DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_48B")

    label("loc_3F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_48B")

    label("loc_411")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_48B")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_48B")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_48B")

    label("loc_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_48B")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_48B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_48B")

    label("loc_4A0")

    Return()

    # Function_2_324 end

    def Function_3_4A1(): pass

    label("Function_3_4A1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE5")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)
    OP_A2(0x258)

    ChrTalk(
        0xB,
        (
            "#130F哎呀……\x01",
            "你是叫艾丝蒂尔吧。\x02\x03",
            "#130F你的同伴怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "他想稍微吹一会儿风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F这样啊。\x01",
            "这里的风吹起来也挺舒服的。\x02\x03",
            "#130F说起来，你们俩这么年轻就当上游击士，\x01",
            "的确是让人佩服不已啊。\x02\x03",
            "#130F我记得要取得游击士资格，\x01",
            "至少要１６岁的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿～知道得很清楚嘛。\x02\x03",
            "#001F嗯。\x01",
            "我们正好１６岁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F年轻真是好啊。\x01",
            "只要年轻就有无限的可能性。\x02\x03",
            "#130F如果我也能年轻个１０岁，\x01",
            "就能亲自去解开沉眠于\x01",
            "整个大陆上的古代遗迹之谜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F整个大陆很广阔吧。\x02\x03",
            "#000F这么说，\x01",
            "教授不是利贝尔人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F嗯，我是北方人。\x02\x03",
            "#130F啊……\x01",
            "不过不是埃雷波尼亚出身哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，不用担心啦。\x02\x03",
            "#003F我虽然十分讨厌战争……\x01",
            "不过这并不代表我痛恨帝国的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#130F……难道你重要的人被……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#500F……………………………\x02\x03",
            "#000F嗯……我的母亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#131F实在抱歉……\x01",
            "问了些不该问的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x01",
            "这已经是十年前的事了。\x02\x03",
            "#000F在那之后我和老爸也有了新的家人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F原来如此。\x01",
            "就是那个和你在一起的同伴吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，就像弟弟一样呢。\x02\x03",
            "#001F不过对约修亚来说，\x01",
            "他一直都是当自己是哥哥呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#132F呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哎呀，\x01",
            "我都说了些什么啊……\x02\x03",
            "#008F这些话怎么好意思对别人说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F这有什么关系。\x01",
            "你们能这么亲密不是很好吗。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_10A9")

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1006")
    OP_A2(0x3)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(
        0x101,
        (
            "#000F对了教授……\x01",
            "关于这座塔，你又弄清了些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F不，现在还完全摸不着头脑。\x02\x03",
            "#130F看起来有必要和\x01",
            "其它的塔做一下对比调查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F其它的塔……\x01",
            "是指洛连特以外的三座塔吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F嗯，正是。\x02\x03",
            "#130F柏斯地区的『琥珀之塔』……\x02\x03",
            "#130F卢安地区的『绀碧之塔』……\x02\x03",
            "#130F蔡斯地区的『红莲之塔』……\x02\x03",
            "#130F每座塔都是和这座『翡翠之塔』\x01",
            "同一时代建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F果然了解得很清楚啊。\x02\x03",
            "#006F不过，调查虽然很有趣……\x01",
            "可不要做太危险的事情哦。\x02\x03",
            "虽然要花点钱，\x01",
            "不过还是请个游击士做护卫比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#130F哈哈，我可是个贫穷学者……\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_10A9")

    label("loc_1006")


    ChrTalk(
        0xB,
        (
            "#130F看起来这个装置的机能\x01",
            "已经完全停止了。\x02\x03",
            "#130F如果找到什么线索，\x01",
            "也许可以再次启动这个装置。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A9")

    TalkEnd(0xB)
    Return()

    # Function_3_4A1 end

    def Function_4_10AD(): pass

    label("Function_4_10AD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AA")
    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xB, 0xFF)
    Fade(1000)
    OP_6D(-12280, 250, 14520, 0)
    SetChrPos(0xD, -9000, 0, 4732, 0)
    SetChrPos(0xE, -6000, 0, 8006, 0)
    SetChrPos(0xB, -2610, 0, 10050, 0)
    SetChrPos(0x101, -13260, 250, 12860, 0)
    SetChrPos(0xC, -12660, 250, 14050, 180)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(
        0x101,
        "#002F约修亚，还是不舒服吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#010F#1P不，已经好多了。\x02\x03",
            "#010F应该可以正常走动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F太好了……\x01",
            "到底是什么原因呢？\x02\x03",
            "#000F如果是因为缺氧的话，\x01",
            "为什么我们又没有事……\x02\x03",
            "#001F一定是突发性的恐高症吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#019F#1P我、我想不是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#151F小艾，小约！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    TurnDirection(0xC, 0xE, 400)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xB, 0xFF)
    OP_43(0xE, 0x1, 0x0, 0x5)
    Sleep(800)
    OP_43(0xD, 0x1, 0x0, 0x5)
    Sleep(1300)
    OP_43(0xB, 0x1, 0x0, 0x5)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F啊，拍摄已经结束了吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#151F#1P当然啦！\x01",
            "还拍了好多张呢⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F#3P这样取材工作就结束了，\x01",
            "我们回城里去吧。\x02\x03",
            "#141F两位新人，回去的时候也拜托了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#130F#1P请多关照了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    AddParty(0x1, 0xFF)
    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Jump("loc_1568")

    label("loc_14AA")


    ChrTalk(
        0x101,
        "#000F约修亚，好点了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#010F嗯，好了一点点吧。\x02\x03",
            "#010F已经休息了一阵子，\x01",
            "#010F艾丝蒂尔你还是继续参观吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_1568")

    TalkEnd(0xC)
    Return()

    # Function_4_10AD end

    def Function_5_156C(): pass

    label("Function_5_156C")

    OP_92(0xFE, 0xF, 0xBB8, 0xBB8, 0x0)
    Return()

    # Function_5_156C end

    def Function_6_157B(): pass

    label("Function_6_157B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C97")
    EventBegin(0x0)
    OP_A2(0x256)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(
        0xD,
        (
            "#145F哈～香烟的味道真好啊。\x02\x03",
            "#141F来到洛连特这种乡下地方取材，\x01",
            "刚开始真是一点干劲都没有……\x02\x03",
            "#141F不过看样子，偶尔来一次也不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哼，真是没礼貌。\x01",
            "不想来的话就不要来嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#142F这可是总编的命令啊。\x01",
            "而且还得带一下那个脱线的丫头。\x02\x03",
            "#142F若不是这样，\x01",
            "我现在应该正为了寻找独家新闻，\x01",
            "而在王国全境到处奔走的旅途中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哼，说是独家新闻，\x01",
            "其实就是点小道消息吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F我倒不讨厌小道消息，\x01",
            "不过绝大部分还是正规报道啦。\x02\x03",
            "#141F……所以说，\x01",
            "现在我最感兴趣的地方就是柏斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F柏斯地区？\x01",
            "难道发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#140F接连发生了大规模的盗窃案件呢。\x02\x03",
            "#140F犯人的真实身份还没有弄清，\x01",
            "不过似乎是有专用交通工具的人干的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F交通工具……是指飞艇吧。\x02\x03",
            "#002F难道说，是空贼？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#140F这种可能性很高。\x02\x03",
            "#140F不过，也有可能是\x01",
            "埃雷波尼亚帝国策划的伪装活动。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F啊……怎么会！\x02\x03",
            "#004F明明已经签订了和平条约了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#140F的确，在十年前的战争中\x01",
            "帝国也受到了重创。\x02\x03",
            "#140F目前在大陆诸国的监视下，\x01",
            "他们应该不敢轻举妄动。\x02\x03",
            "#140F但暗地里捣乱的可能性还是有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F现在真相还隐藏在黑暗中啊。\x02\x03",
            "#141F所以说，弄清楚事实真相也是\x01",
            "我们这些笔杆子的工作啦。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1FAA")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC3")
    OP_A2(0x4)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(
        0xD,
        (
            "#145F此外，\x01",
            "王国军方面也有很多新动向。\x02\x03",
            "#145F真是的，\x01",
            "有几个分身都不够用啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F新动向？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#140F新人军官中出现了个特别能干的人。\x02\x03",
            "#140F听说给缺乏人才而又老化的\x01",
            "王国军带来了新鲜血液。\x02\x03",
            "#140F真想采访一下啊……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1FAA")

    label("loc_1EC3")


    ChrTalk(
        0xD,
        (
            "#141F哈哈，即使是工作再忙碌，\x01",
            "也得偷空抽一两口美味香烟啊。\x02\x03",
            "#141F最近王都的禁烟活动搞得很厉害，\x01",
            "我都不敢在杂志社里面抽烟了。\x02\x03",
            "#147F烟这种东西，果然还是戒不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAA")

    TalkEnd(0xD)
    Return()

    # Function_6_157B end

    def Function_7_1FAE(): pass

    label("Function_7_1FAE")

    TalkBegin(0xE)
    SetChrChipByIndex(0xE, 9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_241F")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)
    OP_A2(0x257)

    ChrTalk(
        0xE,
        (
            "#151F啊，小艾。\x01",
            "这儿真是棒得不得了啊～\x02\x03",
            "#151F我还担心感光结晶回路\x01",
            "够不够用呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这儿的确实风景很好呢。\x02\x03",
            "#000F对了，感光结晶回路是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#150F是用七耀石加工出来的\x01",
            "一种非常薄的结晶回路。\x02\x03",
            "#150F是一种受到光的照射之后，\x01",
            "就可以拍出照片来的装置呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F不愧是专业摄影师，\x01",
            "对自己的谋生工具很精通啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#151F嘿嘿㈱\x02\x03",
            "#153F对了对了……\x01",
            "小约他怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "他想自己吹一会儿风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#150F哦～\x01",
            "伫立在风中的黑发少年……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#151F哇，应该可以拍出很好的照片呢㈱\x02\x03",
            "#151F要不要也给他拍上一张呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊～\x01",
            "约修亚好像不太喜欢这个……\x02\x03",
            "#008F我想他大概会拒绝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#154F唔，有点可惜呢。\x02\x03",
            "#151F这样说来，\x01",
            "小约还真的有点腼腆呢。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_26C3")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267C")
    OP_A2(0x5)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(
        0xE,
        (
            "#151F对了，小约不肯的话，\x01",
            "小艾你来怎么样？\x02\x03",
            "#151F让姐姐拍一张行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F我、我吗？\x02\x03",
            "#004F为什么要拍我呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#151F你很可爱嘛，\x01",
            "而且还有一股闪闪生辉的灵气呢～\x02\x03",
            "#151F说不定还能当封面模特哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F还、还是算了吧！\x01",
            "怎么想也不合我的形象啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#154F唉，又被拒绝了吗。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_26C3")

    label("loc_267C")


    ChrTalk(
        0xE,
        "#151F唔～要拍什么好呢。\x02",
    )

    CloseMessageWindow()

    label("loc_26C3")

    TalkEnd(0xE)
    Return()

    # Function_7_1FAE end

    def Function_8_26C7(): pass

    label("Function_8_26C7")

    EventBegin(0x0)
    OP_A2(0x255)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x101, 90, 0, -4010, 0)
    SetChrPos(0xC, 90, 0, -4010, 0)
    SetChrPos(0xD, 90, 0, -4010, 0)
    SetChrPos(0xE, 90, 0, -4010, 0)
    RemoveParty(0xF, 0xFF)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0xE, 0xFF)
    OP_6D(-2600, 0, 20370, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5300, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_2794():
        OP_6D(-60, 0, 2490, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2794)

    def lambda_27AC():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x11C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_27AC)
    Sleep(500)

    def lambda_27CC():
        OP_8E(0xFE, 0x3FC, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27CC)
    Sleep(500)

    def lambda_27EC():
        OP_8E(0xFE, 0xFFFFFAF6, 0x0, 0xC94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_27EC)
    Sleep(500)

    def lambda_280C():
        OP_8E(0xFE, 0xFFFFFFEC, 0x0, 0x9BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_280C)
    Sleep(3500)
    Fade(1000)
    OP_6D(90, 0, 3680, 0)
    OP_6B(3700, 0)
    OP_8C(0x101, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_8C(0xD, 315, 0)
    OP_8C(0xE, 270, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F好耀眼啊……\x02\x03",
            "#000F终于到达塔顶了～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#151F哇～好美丽的景色哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#147F呵呵，果然十分壮观。\x01",
            "这样可以拍到比预想还好的照片了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(300)

    ChrTalk(
        0xD,
        "#141F还有，那个就是我们要找的……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0xC, 0, 400)
    OP_8C(0xE, 0, 400)

    def lambda_29F3():
        OP_6D(430, 950, 12060, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29F3)

    def lambda_2A0B():
        OP_67(0, 5170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2A0B)

    def lambda_2A23():
        OP_6B(4840, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2A23)
    Sleep(3000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F#1P那个？是什么东西啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#151F#1P看起来像一个超级大锅，\x01",
            "应该是导力器之类的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F#1P根据资料记载，\x01",
            "好像是古代的装置。\x02\x03",
            "#141F目前还不清楚它的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#1P哦……\x02",
    )

    CloseMessageWindow()

    def lambda_2B76():
        OP_6D(90, 0, 3680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B76)

    def lambda_2B8E():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2B8E)

    def lambda_2BA6():
        OP_6B(3700, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2BA6)
    Sleep(1500)
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        (
            "#501F喂，约修亚。\x01",
            "你知道这东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#015F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0xD, 0xC, 400)
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(
        0x101,
        "#002F约修亚？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 45, 400)
    OP_6D(2710, 250, 5470, 1000)

    ChrTalk(
        0xC,
        (
            "#510F……藏起来也没用的。\x02\x03",
            "#510F为了安全着想还是现身比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "男性的声音",
        "啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "男性的声音",
        (
            "我、我出来！\x01",
            "现在立刻就出来！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_43(0xB, 0x1, 0x0, 0xD)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0xDA2, 0xFA, 0x2058, 0xBB8, 0x0)
    OP_8C(0xB, 225, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F这、这个人是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#143F怎么回事，有人捷足先登吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#153F呜哇，吓了一跳～\x01",
            "小约，你的感觉真敏锐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#014F#4P……你是…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "戴眼镜的男性",
        (
            "#131F抱歉、对不起！\x02\x03",
            "#131F我把身上的钱全都给你们，\x01",
            "请饶我一命吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F等等，大叔……\x01",
            "你怎么能把我们当成强盗啊！\x02\x03",
            "看见这个纹章就应该知道了吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔展示了游击士协会的纹章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    NpcTalk(
        0xB,
        "戴眼镜的男性",
        (
            "#130F哦哦，那个是游击士协会的……\x02\x03",
            "#130F难道……\x01",
            "你们是游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿，说对了。\x02\x03",
            "#006F我叫艾丝蒂尔，\x01",
            "这个男孩叫约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F而我们是《利贝尔通讯》的记者。\x02\x03",
            "#141F为了来这座塔取材，\x01",
            "委托这两个游击士当护卫。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3135():
        OP_6D(380, 0, 5840, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3135)
    OP_8E(0xB, 0x1E, 0x0, 0x1B58, 0xBB8, 0x0)
    OP_8C(0xB, 180, 400)

    NpcTalk(
        0xB,
        "戴眼镜的男性",
        (
            "#131F唉～～\x01",
            "真是的，不要吓我嘛……\x02\x03",
            "#131F竟然来这种地方，\x01",
            "不会让人觉得很可疑吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#018F这么说的话，\x01",
            "你不也很可疑吗……\x02\x03",
            "#018F你到底是什么人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F抱歉，还没做自我介绍。\x01",
            "我叫亚鲁瓦，是一个考古学家。\x02\x03",
            "#130F为了研究古代文明\x01",
            "而到这座塔做一些考古调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#153F只有一个人？\x01",
            "能平安无事到这儿还真不简单呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F哪里，哈哈哈。\x01",
            "因为调查遗迹习惯了嘛。\x02\x03",
            "#130F对于从魔兽身边逃走的脚力，\x01",
            "我还是很有自信的。\x02\x03",
            "#130F……不过话说回来，\x01",
            "这次还真是险些丧命呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F真、真是一个蛮干的学者啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#140F不过，你既然是考古学者，\x01",
            "应该对这座塔的由来很清楚吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F嗯，比起一般人应该……\x02\x03",
            "#130F不过刚开始调查不久，\x01",
            "不清楚的地方也还不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F这样也可以啦。\x01",
            "有没有什么有趣的资料？\x02\x03",
            "#141F拿来给我当报道的题材也好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#130F嗯，这样吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#130F不知道各位听说过\x01",
            "『七至宝』这个词吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F听起来，\x01",
            "教区长好像告诉过我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#012F是指女神授予古代人的、\x01",
            "蕴藏巨大力量的『七至宝』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F嗯，就是那个！\x02\x03",
            "#130F传说他们凭借这些至宝的力量，\x01",
            "支配了海洋、大地和天空。\x02\x03",
            "#130F甚至还传说他们连\x01",
            "生命和时间的秘密也解开了……\x02\x03",
            "#130F大概在１２００年前，\x01",
            "一场神秘的灾难毁灭了古代文明，\x01",
            "『七至宝』也因此失传了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#140F这是在七耀教会的圣典里\x01",
            "也有记载的传说啊。\x02\x03",
            "#140F那么，和这座塔有什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F传说七至宝其中之一，\x01",
            "就在这利贝尔的某处沉眠着。\x02\x03",
            "#132F——它的名字是『辉之环』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F『辉之环』……\x01",
            "听起来很不可思议的词语啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F如果这个传说是真的，\x01",
            "我猜想作为利贝尔最古老遗迹的这座塔，\x01",
            "一定留有什么线索才对。\x02\x03",
            "#130F所以我才会来这里调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#151F哈～真是梦幻般的故事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F呵呵……对吧！？\x01",
            "是不是有种古代传承的感觉呢。\x02\x03",
            "#130F呀～！有人能理解我的研究，\x01",
            "真令人感到欣慰啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#012F那样的话……\x01",
            "找到什么线索了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#131F现、现在还没……\x02\x03",
            "#131F如果能解开那边的装置之谜的话，\x01",
            "应该可以知道些什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#145F虽然听起来很有趣，\x01",
            "不过也只是推测的程度而已啊。\x02\x03",
            "#145F抱歉，你告诉我的这些资料\x01",
            "作为报道还是有些欠缺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#131F是吗……那太可惜了。\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0xFF)
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿～真意外。\x01",
            "你写报道出乎意料地认真啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xD,
        (
            "#141F#5P把来源不实的消息\x01",
            "写成报道是绝对不行的。\x02\x03",
            "#141F宁可登载小道消息也不登载无稽之谈，\x01",
            "这就是《利贝尔通讯》的原则。\x02\x03",
            "#141F算了，按照预定计划行事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    TurnDirection(0xD, 0xE, 400)
    TurnDirection(0x101, 0xE, 400)
    OP_21()
    OP_1D(0x1)

    ChrTalk(
        0xD,
        (
            "#140F#5P朵洛希。\x01",
            "拍几张洛连特全景的照片。\x02\x03",
            "#140F其余的就随你喜欢来拍吧。\x02\x03",
            "#140F到处都转一遍，\x01",
            "尽情地多拍些好照片。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)
    OP_62(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#151F知道了！\x02\x03",
            "#151F不肖弟子朵洛希·海娅特，\x01",
            "一定会尽力拍出最好的照片！\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    OP_43(0xE, 0x1, 0x0, 0xD)
    OP_8C(0xE, 270, 400)
    OP_8E(0xE, 0xFFFFF0E2, 0xFA, 0xD5C, 0x1388, 0x0)
    OP_8E(0xE, 0xFFFFDD14, 0xFA, 0x12C, 0x1388, 0x0)
    OP_44(0xE, 0xFF)
    Sleep(1000)
    TurnDirection(0xD, 0xB, 400)
    TurnDirection(0xC, 0xB, 400)
    TurnDirection(0x101, 0xB, 400)
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(
        0xD,
        (
            "#141F学者先生，难得这么巧，\x01",
            "不如就和我们一起回城吧？\x02\x03",
            "#141F这两个家伙，虽然看起来只是小鬼，\x01",
            "不过护卫本领还是很不赖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F真是话中有话呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#130F哈哈，如果能一起回去的话，\x01",
            "我可求之不得啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#141F那就这么决定了。\x02\x03",
            "#141F好了，在摄影结束之前，\x01",
            "我们就稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xB, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_69(0xF, 0x320)
    SetChrPos(0x101, -13260, 250, 12860, 270)
    SetChrPos(0xC, -12660, 250, 14050, 270)
    SetChrPos(0xD, 15093, 250, 5901, 90)
    SetChrPos(0xE, -12962, 0, 3438, 270)
    SetChrPos(0xB, -370, 950, 12896, 0)
    OP_43(0xB, 0x0, 0x0, 0xF)
    OP_43(0xD, 0x0, 0x0, 0x2)
    FadeToBright(1000, 0)
    OP_69(0xD, 0x0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_69(0xB, 0x0)
    Sleep(1000)
    OP_43(0xE, 0x0, 0x0, 0xE)
    Sleep(2900)
    Fade(1000)
    OP_6D(-9350, 250, 760, 0)
    Sleep(2800)
    OP_8C(0xE, 225, 400)
    Sleep(500)
    OP_44(0xE, 0xFF)
    OP_62(0xE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    Sleep(1000)
    Fade(1000)
    OP_6D(-18140, 250, 14540, 0)
    Sleep(1000)
    SetChrPos(0xE, -12962, 0, 3438, 270)
    OP_43(0xE, 0x0, 0x0, 0xE)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F#3P哇～真的好壮观啊！\x02\x03",
            "#001F站得这么高，\x01",
            "可以看到整个洛连特地区呢。\x02\x03",
            "#000F这么好的景色，\x01",
            "说不定可以成为观光胜地哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#013F#3P嗯……也许吧。\x02",
    )

    CloseMessageWindow()
    OP_6D(-15070, 250, 13930, 1000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#002F#3P………………………\x02\x03",
            "#002F怎么了？\x01",
            "好像没什么精神啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 225, 400)

    ChrTalk(
        0xC,
        (
            "#019F#1P哈哈，真瞒不过你。\x02\x03",
            "#019F来到塔顶之后……\x01",
            "就一直感到有点不舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3P没、没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#010F#1P嗯，稍微吹吹风，\x01",
            "应该很快就会好起来的……\x02\x03",
            "#010F反正机会难得，\x01",
            "你就好好参观一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#3P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#011F#1P借这样的机会扩展一下见识，\x01",
            "也是作为游击士必要的工作态度啊。\x02\x03",
            "#011F如果看到什么有趣的事情，\x01",
            "等一下也要告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#3P真是的，说不过你……\x02\x03",
            "#000F我知道了，就稍微转转吧。\x02\x03",
            "#000F不过……\x01",
            "如果觉得难受的话，要赶快叫我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#019F#1P知道了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    OP_8C(0xC, 270, 400)
    OP_43(0xC, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_8_26C7 end

    def Function_9_48FB(): pass

    label("Function_9_48FB")

    Sleep(1300)
    OP_8E(0x101, 0xFFFFFF00, 0x3B6, 0x32F0, 0xBB8, 0x0)
    Return()

    # Function_9_48FB end

    def Function_10_4915(): pass

    label("Function_10_4915")

    Sleep(2000)
    OP_8E(0xC, 0x4C2, 0x0, 0x2726, 0xBB8, 0x0)
    Sleep(1000)
    OP_8C(0xC, 45, 400)
    Return()

    # Function_10_4915 end

    def Function_11_493B(): pass

    label("Function_11_493B")

    Sleep(1500)
    OP_8E(0xD, 0xFFFFFBC4, 0x3B6, 0x2F52, 0xBB8, 0x0)
    Return()

    # Function_11_493B end

    def Function_12_4955(): pass

    label("Function_12_4955")

    Sleep(1500)
    OP_8E(0xE, 0xE1, 0x3B6, 0x2EBE, 0xBB8, 0x0)
    Return()

    # Function_12_4955 end

    def Function_13_496F(): pass

    label("Function_13_496F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49A9")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0xC, 0xFE, 0)
    TurnDirection(0xD, 0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_499E")
    TurnDirection(0xE, 0xFE, 0)
    Jump("loc_49A5")

    label("loc_499E")

    TurnDirection(0xB, 0xFE, 0)

    label("loc_49A5")

    OP_48()
    Jump("Function_13_496F")

    label("loc_49A9")

    Return()

    # Function_13_496F end

    def Function_14_49AA(): pass

    label("Function_14_49AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AE3")
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFCD5E, 0x0, 0xD6E, 0x7D0, 0x0)
    OP_8C(0xE, 270, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(2000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFD04E, 0x0, 0xFFFFF27C, 0x7D0, 0x0)
    OP_8C(0xE, 225, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(1500)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0x33, 0x0, 0xFFFFFE09, 0x7D0, 0x0)
    OP_8C(0xE, 0, 400)
    OP_8C(0xE, 180, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(2000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0x1B82, 0x0, 0x18EE, 0x7D0, 0x0)
    OP_8C(0xE, 90, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(1000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0x330E, 0x0, 0x3543, 0x7D0, 0x0)
    OP_8C(0xE, 45, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(3000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFFFE9, 0x0, 0x22F4, 0x7D0, 0x0)
    OP_8C(0xE, 0, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(1000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFE978, 0x0, 0x2D03, 0x7D0, 0x0)
    OP_8C(0xE, 45, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(2000)
    Jump("Function_14_49AA")

    label("loc_4AE3")

    Return()

    # Function_14_49AA end

    def Function_15_4AE4(): pass

    label("Function_15_4AE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B7F")
    OP_97(0xB, 0x8E, 0x3E1C, 0x7530, 0x3E8, 0x1)
    OP_8B(0xB, 0x8E, 0x3E1C, 0x190)
    Sleep(1000)
    OP_97(0xB, 0x8E, 0x3E1C, 0xFFFFD8F0, 0x1F4, 0x2)
    OP_8B(0xB, 0x8E, 0x3E1C, 0x190)
    Sleep(1000)
    OP_97(0xB, 0x8E, 0x3E1C, 0x1388, 0x2BC, 0x2)
    Sleep(1000)
    OP_97(0xB, 0x8E, 0x3E1C, 0xC350, 0x3E8, 0x1)
    OP_8B(0xB, 0x8E, 0x3E1C, 0x190)
    Sleep(1000)
    Jump("Function_15_4AE4")

    label("loc_4B7F")

    Return()

    # Function_15_4AE4 end

    def Function_16_4B80(): pass

    label("Function_16_4B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BDD")
    EventBegin(0x1)
    ClearMapFlags(0x1)

    ChrTalk(
        0x101,
        "#000F（……不能自己单独行动。）\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4BDD")

    Return()

    # Function_16_4B80 end

    def Function_17_4BDE(): pass

    label("Function_17_4BDE")

    OP_43(0x8, 0x0, 0x0, 0x12)
    OP_43(0x9, 0x0, 0x0, 0x13)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_6D(0, 1000, 12000, 4000)
    OP_A5(0x1)
    OP_A5(0x0)
    OP_20(0x5DC)
    Sleep(1000)
    OP_21()

    ChrTalk(
        0x8,
        "#050F………………真奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#050F虽然感觉得到魔兽的气息，\x01",
            "但是却看不见……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#070F#4S在上面，小心！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#050F什么！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x28)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 0, 10000, 16000, 0)

    ChrTalk(
        0xA,
        "#4S嘎呀呀呀呀呀啊啊啊！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    SetChrChipByIndex(0xA, 5)
    OP_8E(0xA, 0x0, 0x3E8, 0x2DE1, 0x1770, 0x0)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xA, 4)
    OP_A5(0x1)
    OP_A5(0x0)
    Sleep(1000)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x108, 0x8)
    Battle(0x5E, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_20(0x0)
    OP_21()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "辛苦了。\x01",
            "战斗用体验版到此为止。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "这一次是为了测试战斗的感觉、\x01",
            "手感而制作的版本，\x01",
            "没有加入的要素还有很多。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "今后会根据测试员\x01",
            "提交的意见和感想\x01",
            "制作更高完成度的体验版。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "──现在返回主菜单。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    NewScene("ED6_DT01/T0001   ._SN", 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    Return()

    # Function_17_4BDE end

    def Function_18_4EEE(): pass

    label("Function_18_4EEE")

    OP_A6(0x0)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFFF9C, 0x3E8, 0x3019, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x0)
    OP_A6(0x0)
    Sleep(500)
    OP_44(0xFE, 0x3)
    TurnDirection(0xFE, 0xA, 0)
    OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x1B58)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x0)
    Return()

    # Function_18_4EEE end

    def Function_19_4F4E(): pass

    label("Function_19_4F4E")

    OP_A6(0x1)
    Sleep(500)
    OP_8E(0xFE, 0x3A2, 0x0, 0x28DD, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x1)
    OP_A6(0x1)
    Sleep(500)
    OP_44(0xFE, 0x3)
    TurnDirection(0xFE, 0xA, 0)
    OP_95(0xFE, 0x3E8, 0x0, 0xFFFFF448, 0x7D0, 0x1B58)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x1)
    Return()

    # Function_19_4F4E end

    SaveToFile()

Try(main)
