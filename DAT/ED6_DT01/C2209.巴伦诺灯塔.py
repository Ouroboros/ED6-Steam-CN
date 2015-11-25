from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2209   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2209.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/C2209   ._SN',
            'ED6_DT01/C2209_1 ._SN',
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
        '弗科特老人',                           # 9
        '照相机',                               # 10
        '玛诺利亚间道方向',                     # 11
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
        Unknown_3A              = 84,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
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
        'ED6_DT07/CH01000 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
    )

    DeclNpc(
        X                   = 620,
        Z                   = 550,
        Y                   = -2470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1330,
        Z                   = -430,
        Y                   = -46450,
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


    DeclActor(
        TriggerX            = -960,
        TriggerZ            = 25000,
        TriggerY            = -770,
        TriggerRange        = 800,
        ActorX              = -960,
        ActorZ              = 26500,
        ActorY              = -770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_272",          # 02, 2
        "Function_3_288",          # 03, 3
        "Function_4_2B4",          # 04, 4
        "Function_5_2BB",          # 05, 5
        "Function_6_2D6",          # 06, 6
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_198")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    Jump("loc_1A2")

    label("loc_198")

    OP_1B(0x1, 0x0, 0x5)
    OP_1B(0x2, 0x0, 0x5)

    label("loc_1A2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_1AE"),
        (SWITCH_DEFAULT, "loc_227"),
    )


    label("loc_1AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 0)), scpexpr(EXPR_END)), "loc_213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 1)), scpexpr(EXPR_END)), "loc_213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_END)), "loc_213")
    OP_28(0x1C, 0x4, 0x10)
    SetMapFlags(0x400000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F")
    Event(1, 5)
    Jump("loc_213")

    label("loc_20F")

    Event(1, 7)

    label("loc_213")

    Jump("loc_224")

    label("loc_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_224")
    OP_A3(0x3FC)
    Event(1, 6)

    label("loc_224")

    Jump("loc_227")

    label("loc_227")

    Return()

    # Function_0_17A end

    def Function_1_228(): pass

    label("Function_1_228")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDDD20, 0x30050)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25A")
    OP_72(0x0, 0x10)

    label("loc_25A")

    OP_B0(0x0, 0x78)
    OP_B0(0x1, 0x78)
    OP_1C(0x0, 0x0, 0x3)
    OP_1C(0x1, 0x0, 0x4)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_228 end

    def Function_2_272(): pass

    label("Function_2_272")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_287")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_272")

    label("loc_287")

    Return()

    # Function_2_272 end

    def Function_3_288(): pass

    label("Function_3_288")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AD")
    OP_A2(0x2)
    Call(1, 1)
    Jump("loc_2B3")

    label("loc_2AD")

    TalkBegin(0xFF)
    TalkEnd(0xFF)

    label("loc_2B3")

    Return()

    # Function_3_288 end

    def Function_4_2B4(): pass

    label("Function_4_2B4")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_4_2B4 end

    def Function_5_2BB(): pass

    label("Function_5_2BB")

    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_21()
    OP_1B(0x1, 0x0, 0xFFFF)
    OP_1B(0x2, 0x0, 0xFFFF)
    Return()

    # Function_5_2BB end

    def Function_6_2D6(): pass

    label("Function_6_2D6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　危险！　　　\x01",
            "※工作人员以外禁止进入\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_2D6 end

    SaveToFile()

Try(main)
