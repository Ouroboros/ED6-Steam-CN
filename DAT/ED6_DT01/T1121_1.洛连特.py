from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_95")
    OP_2A(0xE, 0x10, 0x11, 0x12, 0x13, 0x15, 0x16, 0x17, 0x18, 0xFFFF)
    Jump("loc_A8")

    label("loc_95")

    OP_2A(0xE, 0x10, 0x12, 0x13, 0x15, 0x16, 0x17, 0x18, 0xFFFF)

    label("loc_A8")

    Jump("loc_1C6")

    label("loc_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_D5")
    OP_2A(0xE, 0x10, 0x11, 0x12, 0x13, 0x15, 0x16, 0x17, 0x18, 0xFFFF)
    Jump("loc_E8")

    label("loc_D5")

    OP_2A(0xE, 0x10, 0x12, 0x13, 0x15, 0x16, 0x17, 0x18, 0xFFFF)

    label("loc_E8")

    Jump("loc_1C6")

    label("loc_EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_127")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_113")
    OP_2A(0xE, 0x10, 0x11, 0x12, 0x15, 0x16, 0x17, 0x18, 0xFFFF)
    Jump("loc_124")

    label("loc_113")

    OP_2A(0xE, 0x10, 0x12, 0x15, 0x16, 0x17, 0x18, 0xFFFF)

    label("loc_124")

    Jump("loc_1C6")

    label("loc_127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_15B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_14B")
    OP_2A(0xE, 0x11, 0x12, 0x15, 0x16, 0x17, 0xFFFF)
    Jump("loc_158")

    label("loc_14B")

    OP_2A(0xE, 0x12, 0x15, 0x16, 0x17, 0xFFFF)

    label("loc_158")

    Jump("loc_1C6")

    label("loc_15B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 5)), scpexpr(EXPR_END)), "loc_170")
    OP_2A(0xE, 0x12, 0x15, 0x16, 0xFFFF)
    Jump("loc_1C6")

    label("loc_170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_183")
    OP_2A(0xE, 0x12, 0x15, 0xFFFF)
    Jump("loc_1C6")

    label("loc_183")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有什么特别的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1C6")

    TalkEnd(0xFF)
    Sleep(400)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
