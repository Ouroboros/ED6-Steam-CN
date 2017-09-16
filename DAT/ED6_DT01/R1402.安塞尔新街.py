from ED6ScenarioHelper import *

def main():
    # 安塞尔新街

    CreateScenaFile(
        FileName            = 'R1402   ._SN',
        MapName             = 'Bose',
        Location            = 'R1402.x',
        MapIndex            = 58,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R1402   ._SN',
            'ED6_DT01/R1402_1 ._SN',
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
        '亚鲁瓦教授',                           # 9
        '亚鲁瓦教授',                           # 10
        '安塞尔新街方向',                       # 11
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
        Unknown_3A              = 58,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02050 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02050P._CP',             # 00
    )

    DeclNpc(
        X                   = -77000,
        Z                   = 2000,
        Y                   = 0,
        Direction           = 135,
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
        X                   = -77000,
        Z                   = 2000,
        Y                   = 0,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1CD,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1070,
        Z                   = -600,
        Y                   = -32720,
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


    ScpFunction(
        "Function_0_112",          # 00, 0
        "Function_1_14C",          # 01, 1
    )


    def Function_0_112(): pass

    label("Function_0_112")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_11E"),
        (SWITCH_DEFAULT, "loc_14B"),
    )


    label("loc_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148")
    OP_28(0xF, 0x1, 0x10)
    Event(1, 0)

    label("loc_148")

    Jump("loc_14B")

    label("loc_14B")

    Return()

    # Function_0_112 end

    def Function_1_14C(): pass

    label("Function_1_14C")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x3001E)
    Return()

    # Function_1_14C end

    SaveToFile()

Try(main)
