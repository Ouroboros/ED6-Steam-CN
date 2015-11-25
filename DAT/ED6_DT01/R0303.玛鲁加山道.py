from ED6ScenarioHelper import *

def main():
    # 玛鲁加山道

    CreateScenaFile(
        FileName            = 'R0303   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0303.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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
        '雪拉扎德',                             # 9
        '矿工兰古',                             # 10
        '见习矿工',                             # 11
        '玛鲁加山道方向',                       # 12
        '玛鲁加山道方向',                       # 13
        '目标用摄像机',                         # 14
    )

    DeclEntryPoint(
        Unknown_00              = -1500,
        Unknown_04              = 0,
        Unknown_08              = -28000,
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
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -1500,
        Unknown_04              = 0,
        Unknown_08              = -28000,
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
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 4000,
        Unknown_08              = -10000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -1500,
        Unknown_04              = 0,
        Unknown_08              = -28000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3200,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 21,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH01500 ._CH',             # 01
        'ED6_DT06/CH20063 ._CH',             # 02
        'ED6_DT06/CH20064 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH01500P._CP',             # 01
        'ED6_DT06/CH20063P._CP',             # 02
        'ED6_DT06/CH20064P._CP',             # 03
    )

    DeclNpc(
        X                   = 8600,
        Z                   = 4000,
        Y                   = -8230,
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
        X                   = -166100,
        Z                   = 100,
        Y                   = 127500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -167010,
        Z                   = -70,
        Y                   = 78790,
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

    DeclNpc(
        X                   = -2070,
        Z                   = -120,
        Y                   = -72730,
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
        X                   = -2500,
        Y                   = -1000,
        Z                   = -45000,
        Range               = 4000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF38C8,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -2000,
        Y                   = 4000,
        Z                   = -7442,
        Range               = 2000,
        Unknown_10          = 0x1770,
        Unknown_14          = 0xFFFFE4E4,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -168250,
        Y                   = -1000,
        Z                   = 128000,
        Range               = -164500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1EBCC,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -2472,
        Y                   = -1000,
        Z                   = -21384,
        Range               = 2537,
        Unknown_10          = 0x1770,
        Unknown_14          = 0xFFFFB32C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_33A",          # 01, 1
        "Function_2_387",          # 02, 2
        "Function_3_39D",          # 03, 3
        "Function_4_70B",          # 04, 4
        "Function_5_14BC",         # 05, 5
        "Function_6_14C6",         # 06, 6
        "Function_7_14D8",         # 07, 7
        "Function_8_14E2",         # 08, 8
        "Function_9_14FE",         # 09, 9
        "Function_10_151A",        # 0A, 10
        "Function_11_1536",        # 0B, 11
        "Function_12_1552",        # 0C, 12
        "Function_13_1667",        # 0D, 13
        "Function_14_1C2D",        # 0E, 14
        "Function_15_1C2E",        # 0F, 15
        "Function_16_1D76",        # 10, 16
        "Function_17_207B",        # 11, 17
        "Function_18_209B",        # 12, 18
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    ClearMapFlags(0x400000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_END)), "loc_2F3")
    SetChrPos(0x9, -167300, 0, 128100, 180)

    label("loc_2F3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (3, "loc_2FF"),
        (SWITCH_DEFAULT, "loc_339"),
    )


    label("loc_2FF")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    OP_6D(-166000, 0, 128270, 0)
    SetChrPos(0xA, -166200, 0, 131180, 0)
    Event(0, 15)
    Jump("loc_339")

    label("loc_339")

    Return()

    # Function_0_2D6 end

    def Function_1_33A(): pass

    label("Function_1_33A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_352"),
        (101, "loc_352"),
        (102, "loc_36C"),
        (103, "loc_36C"),
        (SWITCH_DEFAULT, "loc_386"),
    )


    label("loc_352")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD7790, 0x30011)
    ClearChrFlags(0xB, 0x4)
    Jump("loc_386")

    label("loc_36C")

    OP_16(0x2, 0xFA0, 0xFFFB8390, 0xFFFFBD98, 0x3006A)
    ClearChrFlags(0xC, 0x4)
    Jump("loc_386")

    label("loc_386")

    Return()

    # Function_1_33A end

    def Function_2_387(): pass

    label("Function_2_387")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_387")

    label("loc_39C")

    Return()

    # Function_2_387 end

    def Function_3_39D(): pass

    label("Function_3_39D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_454")

    ChrTalk(
        0x9,
        (
            "哟，这不是\x01",
            "游击士小姑娘小兄弟吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "坑道里面的魔兽\x01",
            "终于停止骚动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "老大他很长时间没回家了，\x01",
            "这次终于能回去好好休息一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4D9")

    ChrTalk(
        0x9,
        (
            "我一稍不留神，\x01",
            "提恩特那家伙\x01",
            "就趁机溜走出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那家伙肯定又去翘班了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(
        0x9,
        "哦，这不是游击士吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "有什么事吗？\x01",
            "里面很暗，请小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_61A")

    ChrTalk(
        0x9,
        (
            "哎呀哎呀，\x01",
            "事情变得一塌糊涂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，\x01",
            "多亏你们来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没你们的话，\x01",
            "事情可就糟啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_END)), "loc_697")

    ChrTalk(
        0x9,
        "里面很暗，请小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "找加通老大的话，\x01",
            "他应该在地下坑道里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_697")


    ChrTalk(
        0x9,
        (
            "喂，这里是玛鲁加矿山。\x01",
            "无关人员不能进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707")

    TalkEnd(0x9)
    Return()

    # Function_3_39D end

    def Function_4_70B(): pass

    label("Function_4_70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BB")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x254)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xD, 0x2, 0x0, 0x6)
    OP_43(0x0, 0x1, 0x0, 0x7)
    OP_6D(0, 5200, -6500, 3000)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x101, -845, 0, -22467, 0)
    SetChrPos(0x102, 471, 0, -22527, 0)
    SetChrPos(0x10F, -1170, 0, -24389, 0)
    SetChrPos(0x110, 72, 0, -24459, 0)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_0D()

    ChrTalk(
        0x110,
        (
            "#153F#4P哇……\x01",
            "好高的建筑物啊。\x02\x03",
            "#153F到底会有几层呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P这个嘛……\x01",
            "我们之前只到过第二层。\x02\x03",
            "#000F这么高的塔，\x01",
            "我想应该有五到六层左右吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P应该是五层，\x01",
            "家里的资料是这样记载的。\x02\x03",
            "#010F这里很久以前就有学者调查过，\x01",
            "只不过后来被放置不理罢了。\x02\x03",
            "#010F说起来，\x01",
            "王国其它地方好像也有类似的塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#140F#3P啊，没错。\x02\x03",
            "#140F柏斯、卢安和蔡斯\x01",
            "也建有同样建筑风格的塔。\x02\x03",
            "#140F而且，\x01",
            "好像是王国建国时期建造出来的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P啊～是吗。\x01",
            "这座塔似乎很有历史价值嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        "#141F#3P记录下这种价值就是我们来这的目的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x110, 400)
    TurnDirection(0x101, 0x110, 400)
    TurnDirection(0x102, 0x110, 400)

    ChrTalk(
        0x10F,
        (
            "#140F#3P朵洛希，\x01",
            "先从低角度拍几张。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x10F, 400)

    ChrTalk(
        0x110,
        "#151F#4P好～的！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x110, 2)
    OP_43(0x101, 0x1, 0x0, 0x8)
    OP_43(0x102, 0x1, 0x0, 0x9)
    OP_43(0x10F, 0x1, 0x0, 0xA)
    OP_43(0x110, 0x1, 0x0, 0xB)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0xBB8)
    SetChrChipByIndex(0x110, 3)

    ChrTalk(
        0x110,
        "#150F#4P好……我要拍了。\x02",
    )

    CloseMessageWindow()
    OP_6B(2800, 1000)

    ChrTalk(
        0x110,
        (
            "#150F#4P…………………………………………\x01",
            "…………………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F（好，好厉害的气势……\x01",
            "一拿起照相机，就像变了个人似的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（不愧是专业的……）\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x110,
        (
            "#4P……………………………\x02\x03",
            "#4P……………………\x02\x03",
            "#4P……………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x110, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x110,
        "#4P呼～……Ｚｚｚ……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_92(0x10F, 0x110, 0x7D0, 0xFA0, 0x0)
    OP_92(0x10F, 0x110, 0x3E8, 0x1388, 0x0)
    OP_92(0x10F, 0x110, 0x1F4, 0x1770, 0x0)
    SetChrChipByIndex(0x110, 2)
    OP_22(0x7D, 0x0, 0x64)
    OP_8F(0x110, 0x0, 0x0, 0xFFFF97B4, 0x1770, 0x0)
    OP_63(0x110)
    OP_62(0x110, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)
    Sleep(2000)
    OP_63(0x110)
    Sleep(600)
    TurnDirection(0x110, 0x10F, 400)

    ChrTalk(
        0x110,
        (
            "#152F#4P呜呜……\x02\x03",
            "#152F前辈，好疼啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#144F我都和你说过多少次了！\x02\x03",
            "#144F不要摆架势，\x01",
            "照平时的样子去拍就行了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10F, 0xFFFFF360, 0x0, 0xFFFFA091, 0xBB8, 0x0)
    TurnDirection(0x10F, 0x110, 400)

    ChrTalk(
        0x110,
        (
            "#151F#4P嘿嘿～\x01",
            "果然还不太习惯拍照的方式啊。\x02\x03",
            "#151F那么……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x110, 0xFFFFFE58, 0x0, 0xFFFF98E9, 0xBB8, 0x0)
    SetChrChipByIndex(0x110, 3)
    OP_8C(0x110, 0, 400)
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    ChrTalk(
        0x110,
        "#150F#4P哦哦，这个表情不错哦。\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0x2F6, 0x0, 0xFFFF99A3, 0xBB8, 0x0)

    ChrTalk(
        0x110,
        (
            "#150F#4P真是性感啊。\x01",
            "哇，太可爱了～！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0xFFFFFFC2, 0x0, 0xFFFF9BE7, 0xBB8, 0x0)

    ChrTalk(
        0x110,
        "#151F#4P要照了，来喊『茄～子』㈱\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_43(0x110, 0x1, 0x0, 0xC)
    OP_69(0x102, 0x3E8)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F怎、怎么回事？\x01",
            "又不是在拍人物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F不过却有种奇妙的融合感……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#145F这家伙能看到景色的『表情』。\x02\x03",
            "#145F她就是用这种白痴一样的做法，\x01",
            "拍出很多让人叹为观止的照片。\x02\x03",
            "#145F说起来，这也算是一种另类的天才吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼……\x01",
            "真是人不可貌相啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x110, 0xFF)
    Sleep(1000)
    SetChrChipByIndex(0x110, 65535)
    OP_92(0x110, 0x0, 0x640, 0xBB8, 0x0)
    TurnDirection(0x110, 0x10F, 400)
    TurnDirection(0x10F, 0x110, 400)

    ChrTalk(
        0x110,
        "#151F好了，让你们久等啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#141F好，我们进去吧。\x02\x03",
            "#141F目标是塔顶哦。\x01",
            "拜托了，两位游击士新人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哼哼，交给我们吧。\x02\x03",
            "#006F不管出现什么样的魔兽，\x01",
            "都不会让它碰你们一根手指的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F进塔之后请不要离开我们身后啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_14BB")

    Return()

    # Function_4_70B end

    def Function_5_14BC(): pass

    label("Function_5_14BC")

    OP_6C(0, 3000)
    Return()

    # Function_5_14BC end

    def Function_6_14C6(): pass

    label("Function_6_14C6")

    OP_67(0, 4500, -10000, 3000)
    Return()

    # Function_6_14C6 end

    def Function_7_14D8(): pass

    label("Function_7_14D8")

    OP_6B(6000, 3000)
    Return()

    # Function_7_14D8 end

    def Function_8_14E2(): pass

    label("Function_8_14E2")

    OP_8E(0x101, 0xFFFFF652, 0x0, 0xFFFFA67D, 0xBB8, 0x0)
    TurnDirection(0x101, 0x110, 400)
    Return()

    # Function_8_14E2 end

    def Function_9_14FE(): pass

    label("Function_9_14FE")

    OP_8E(0x102, 0xFFFFF5CE, 0x0, 0xFFFFA41E, 0xBB8, 0x0)
    TurnDirection(0x102, 0x110, 400)
    Return()

    # Function_9_14FE end

    def Function_10_151A(): pass

    label("Function_10_151A")

    OP_8E(0x10F, 0xFFFFF360, 0x0, 0xFFFFA091, 0xBB8, 0x0)
    TurnDirection(0x10F, 0x110, 400)
    Return()

    # Function_10_151A end

    def Function_11_1536(): pass

    label("Function_11_1536")

    OP_8E(0x110, 0xFFFFFE58, 0x0, 0xFFFF98E9, 0xBB8, 0x0)
    OP_8C(0x110, 0, 400)
    Return()

    # Function_11_1536 end

    def Function_12_1552(): pass

    label("Function_12_1552")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1666")
    OP_8F(0x110, 0xFFFFFE58, 0x0, 0xFFFF98E9, 0xBB8, 0x0)
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0x2F6, 0x0, 0xFFFF99A3, 0xBB8, 0x0)
    Sleep(1500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8F(0x110, 0xFFFFFFC2, 0x0, 0xFFFF9BE7, 0xBB8, 0x0)
    Sleep(3000)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("Function_12_1552")

    label("loc_1666")

    Return()

    # Function_12_1552 end

    def Function_13_1667(): pass

    label("Function_13_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1735")
    EventBegin(0x0)
    TurnDirection(0x9, 0x0, 400)
    OP_4A(0x9, 255)

    ChrTalk(
        0x9,
        "喂，这里是玛鲁加矿山。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "无关人员不能进去。\x02",
    )

    CloseMessageWindow()
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1E654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0x0, 0xD, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0x9, 180, 0)
    OP_4B(0x9, 255)
    Return()

    label("loc_1735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C2C")
    OP_4A(0x9, 255)
    EventBegin(0x0)
    OP_A2(0x23C)
    OP_28(0x3, 0x1, 0x8)
    Fade(1000)
    SetChrPos(0x101, -166670, 30, 125190, 0)
    SetChrPos(0x102, -165340, 40, 125200, 0)
    OP_6D(-167300, 0, 128070, 2000)
    TurnDirection(0x9, 0x101, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x9, 0xFFFD775E, 0x0, 0x1F040, 0x3E8, 0x0)
    OP_8C(0x9, 180, 400)

    ChrTalk(
        0x9,
        "#2P喂，这里是玛鲁加矿山。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P无关人员不能进去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F嘿嘿，我们是相关人员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们受洛连特的克劳斯市长委托，\x01",
            "来这里收取七耀石的结晶。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔出示市长的介绍信。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x9,
        (
            "#2P哦，原来如此。\x01",
            "这样就另当别论了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P不好意思，\x01",
            "你们直接进去找老大吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P我还要留在这里值班。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F等一下……老大……？\x02\x03",
            "你还听不懂吗？\x01",
            "我们是来找你们的矿长的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P嘿嘿，我当然知道。\x01",
            "矿长就是管我们这些矿工的加通老大嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2P七耀石矿脉就是他发现的。\x01",
            "比起一日三餐，他更喜欢整天挖洞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P今天他肯定也在地下矿坑里吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F明白了。\x01",
            "那我们就进去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFD727C, 0x0, 0x1F464, 0xBB8, 0x0)
    OP_8C(0x9, 180, 400)
    OP_4B(0x9, 255)
    EventEnd(0x0)

    label("loc_1C2C")

    Return()

    # Function_13_1667 end

    def Function_14_1C2D(): pass

    label("Function_14_1C2D")

    Return()

    # Function_14_1C2D end

    def Function_15_1C2E(): pass

    label("Function_15_1C2E")

    EventBegin(0x0)
    OP_6D(-166260, 20, 124370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_8E(0xA, 0xFFFD7646, 0xFFFFFFF6, 0x1DF9C, 0x1388, 0x0)
    OP_8C(0xA, 0, 400)

    ChrTalk(
        0xA,
        "真是失算啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "魔兽跑出来了，\x01",
            "连游击士也出动了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，没办法……\x01",
            "还是先回去如实报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    OP_8E(0xA, 0xFFFD756A, 0x14, 0x1B47C, 0x1770, 0x0)
    NewScene("ED6_DT01/C0100   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1C2E end

    def Function_16_1D76(): pass

    label("Function_16_1D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 6)), scpexpr(EXPR_END)), "loc_1E3A")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    TurnDirection(0x106, 0x108, 0)

    ChrTalk(
        0x108,
        (
            "#070F怎么了。\x01",
            "现在要回城去吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x106, 0)

    ChrTalk(
        0x106,
        "#050F不，还是算了……\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, 0, 0, -42800, 0)
    SetChrPos(0x1, 0, 0, -42800, 0)
    SetChrPos(0x2, 0, 0, -42800, 0)
    SetChrPos(0x3, 0, 0, -42800, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    label("loc_1E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E46")
    Return()

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_1E4E")
    Return()

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207A")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    StopSound(0x9470, 0x30D40, 0x0)

    def lambda_1E70():
        OP_6B(6000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1E70)

    def lambda_1E80():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1E80)

    def lambda_1E90():
        OP_67(0, 4000, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1E90)
    OP_6D(140, 5000, -10820, 6000)
    SetChrPos(0x101, 500, 100, -22600, 0)
    SetChrPos(0x102, -500, 100, -22600, 0)
    OP_43(0x102, 0x0, 0x0, 0x11)
    OP_A2(0x3)
    OP_8E(0x101, 0x1F4, 0xFA0, 0xFFFFD738, 0x1388, 0x0)
    OP_A5(0x3)
    WaitChrThread(0x0, 0x3)
    Fade(1000)
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6D(140, 4000, -10820, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F虽然来到翡翠之塔了……\x02\x03",
            "#002F可没在山路上遇到那两个孩子，\x01",
            "也就是说……他们已经进去这里面了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F看来可能性很高。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F我们进去吧。\x01",
            "……必须赶快才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#002F嗯……是啊！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_28(0x1, 0x1, 0x4)
    OP_A2(0x221)

    label("loc_207A")

    Return()

    # Function_16_1D76 end

    def Function_17_207B(): pass

    label("Function_17_207B")

    OP_A6(0x3)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFFE0C, 0xFA0, 0xFFFFD3D2, 0x1388, 0x0)
    OP_A3(0x3)
    Return()

    # Function_17_207B end

    def Function_18_209B(): pass

    label("Function_18_209B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 6)), scpexpr(EXPR_END)), "loc_20AD")
    EventBegin(0x0)
    NewScene("ED6_DT01/C2100   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_20AD")

    Return()

    # Function_18_209B end

    SaveToFile()

Try(main)
