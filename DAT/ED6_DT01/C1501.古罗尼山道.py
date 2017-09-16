from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'C1501   ._SN',
        MapName             = 'Bose',
        Location            = 'C1501.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/C1501   ._SN',
            'ED6_DT01/C1501_1 ._SN',
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
        '奥维德',                               # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '照相机',                               # 13
        '玛诺利亚海岸方向',                     # 14
        '古罗尼山道·关所方向',                 # 15
    )

    DeclEntryPoint(
        Unknown_00              = -110000,
        Unknown_04              = 6100,
        Unknown_08              = 108000,
        Unknown_0C              = 4,
        Unknown_0E              = 135,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 250,
        Unknown_32              = 228,
        Unknown_34              = 265,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 61,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01120 ._CH',             # 00
        'ED6_DT09/CH10200 ._CH',             # 01
        'ED6_DT09/CH10201 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00140 ._CH',             # 07
        'ED6_DT07/CH00141 ._CH',             # 08
        'ED6_DT09/CH10200 ._CH',             # 09
        'ED6_DT09/CH10201 ._CH',             # 0A
        'ED6_DT09/CH10880 ._CH',             # 0B
        'ED6_DT09/CH10881 ._CH',             # 0C
        'ED6_DT09/CH11160 ._CH',             # 0D
        'ED6_DT09/CH11161 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01120P._CP',             # 00
        'ED6_DT09/CH10200P._CP',             # 01
        'ED6_DT09/CH10201P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00140P._CP',             # 07
        'ED6_DT07/CH00141P._CP',             # 08
        'ED6_DT09/CH10200P._CP',             # 09
        'ED6_DT09/CH10201P._CP',             # 0A
        'ED6_DT09/CH10880P._CP',             # 0B
        'ED6_DT09/CH10881P._CP',             # 0C
        'ED6_DT09/CH11160P._CP',             # 0D
        'ED6_DT09/CH11161P._CP',             # 0E
    )

    DeclNpc(
        X                   = -98500,
        Z                   = 4000,
        Y                   = 70100,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -97500,
        Z                   = 4000,
        Y                   = 71500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -96700,
        Z                   = 4000,
        Y                   = 72300,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -95800,
        Z                   = 4000,
        Y                   = 73000,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -68830,
        Z                   = 70,
        Y                   = -31470,
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
        X                   = -114600,
        Z                   = 6050,
        Y                   = 118780,
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


    DeclMonster(
        X                   = -106080,
        Z                   = 6030,
        Y                   = 93200,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104200,
        Z                   = 1980,
        Y                   = 7590,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -109430,
        Z                   = 4040,
        Y                   = 46760,
        Unknown_0C          = 0,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121470,
        Z                   = 2040,
        Y                   = 22550,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -109700,
        Y                   = 6000,
        Z                   = 66600,
        Range               = 2000,
        Unknown_10          = 0x578,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 1,
    )


    DeclActor(
        TriggerX            = -106310,
        TriggerZ            = 1990,
        TriggerY            = 2710,
        TriggerRange        = 1000,
        ActorX              = -106430,
        ActorZ              = 1990,
        ActorY              = 2090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -112480,
        TriggerZ            = 2070,
        TriggerY            = 63130,
        TriggerRange        = 1000,
        ActorX              = -112990,
        ActorZ              = 2070,
        ActorY              = 63430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DA",          # 00, 0
        "Function_1_2DB",          # 01, 1
        "Function_2_320",          # 02, 2
        "Function_3_336",          # 03, 3
        "Function_4_473",          # 04, 4
    )


    def Function_0_2DA(): pass

    label("Function_0_2DA")

    Return()

    # Function_0_2DA end

    def Function_1_2DB(): pass

    label("Function_1_2DB")

    OP_16(0x2, 0xFA0, 0xFFFC8560, 0xFFFEA840, 0x3003F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF")
    OP_6F(0x0, 0)
    Jump("loc_306")

    label("loc_2FF")

    OP_6F(0x0, 60)

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318")
    OP_6F(0x1, 0)
    Jump("loc_31F")

    label("loc_318")

    OP_6F(0x1, 60)

    label("loc_31F")

    Return()

    # Function_1_2DB end

    def Function_2_320(): pass

    label("Function_2_320")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_335")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_320")

    label("loc_335")

    Return()

    # Function_2_320 end

    def Function_3_336(): pass

    label("Function_3_336")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_3AC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4C4)
    Jump("loc_422")

    label("loc_3AC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_422")

    Jump("loc_465")

    label("loc_425")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x19)

    label("loc_465")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_336 end

    def Function_4_473(): pass

    label("Function_4_473")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_562")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_4E9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4C5)
    Jump("loc_55F")

    label("loc_4E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_55F")

    Jump("loc_5AA")

    label("loc_562")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x1A)

    label("loc_5AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_473 end

    SaveToFile()

Try(main)
