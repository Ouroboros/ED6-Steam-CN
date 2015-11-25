from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3114_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3114.x',
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C6")
    Return()

    label("loc_C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29B")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-107170, 0, -700, 0)
    SetChrPos(0x101, -107070, 0, -2860, 2)
    SetChrPos(0x102, -108010, 0, -2670, 359)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136")
    SetChrPos(0x107, -105720, 0, -2270, 332)

    label("loc_136")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155")
    SetChrPos(0x106, -109230, 0, -1920, 56)

    label("loc_155")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_174")
    SetChrPos(0x13C, -106920, 0, -560, 21)

    label("loc_174")

    OP_0D()
    Sleep(400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵呀～～呵。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F咦…………！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x101, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵呀～～呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……对这道门有反应吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F这、这个房间是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F不管怎样，\x01",
            "先进去调查再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，说得对。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x100)
    OP_B2(0x0, 0x3, 0x80)
    EventEnd(0x0)

    label("loc_29B")

    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
