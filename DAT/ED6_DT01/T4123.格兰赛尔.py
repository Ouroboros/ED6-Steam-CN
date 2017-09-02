from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4123   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4123.x',
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
        '亚妮拉丝',                             # 9
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
        'ED6_DT07/CH01630 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01630P._CP',             # 00
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_F5",           # 01, 1
        "Function_2_F6",           # 02, 2
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10500, 0, 5390, 90)

    label("loc_F4")

    Return()

    # Function_0_D2 end

    def Function_1_F5(): pass

    label("Function_1_F5")

    Return()

    # Function_1_F5 end

    def Function_2_F6(): pass

    label("Function_2_F6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 9240, 0, 5790, 90)
    SetChrPos(0x102, 9180, 0, 4760, 90)
    SetChrPos(0x108, 8280, 0, 5410, 90)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64C)
    OP_6D(9900, 0, 5380, 1000)

    ChrTalk(
        0x8,
        (
            "啊呀，\x01",
            "这不是两位新人和金大哥吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这么快就从城里回来啦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，虽然是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F亚妮拉丝前辈。\x01",
            "占用你一点时间好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "什么事，什么事？\x01",
            "有什么好玩儿的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯。\x02\x03",
            "好玩儿倒是不至于，\x01",
            "但是会下人一跳的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "咦……\x01",
            "好像不太好玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在这儿站着不好说话，\x01",
            "我们到外面的休息处去如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_353")

    TalkEnd(0x8)
    Return()

    # Function_2_F6 end

    SaveToFile()

Try(main)
