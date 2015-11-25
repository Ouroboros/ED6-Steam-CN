from ED6ScenarioHelper import *

def main():
    # 封印区域

    CreateScenaFile(
        FileName            = 'C4304   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4304.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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


    AddCharChip(
        'ED6_DT09/CH11090 ._CH',             # 00
        'ED6_DT09/CH11091 ._CH',             # 01
        'ED6_DT09/CH11000 ._CH',             # 02
        'ED6_DT09/CH11001 ._CH',             # 03
        'ED6_DT09/CH10930 ._CH',             # 04
        'ED6_DT09/CH10931 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT09/CH11090P._CP',             # 00
        'ED6_DT09/CH11091P._CP',             # 01
        'ED6_DT09/CH11000P._CP',             # 02
        'ED6_DT09/CH11001P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -3060,
        Z                   = 0,
        Y                   = 75060,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13240,
        Z                   = 0,
        Y                   = 150640,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 135180,
        Z                   = 0,
        Y                   = 146710,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 64840,
        Z                   = 0,
        Y                   = 273920,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23360,
        Z                   = 0,
        Y                   = 233960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -159380,
        Z                   = 0,
        Y                   = 159140,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -303150,
        TriggerZ            = 0,
        TriggerY            = 178540,
        TriggerRange        = 1000,
        ActorX              = -302930,
        ActorZ              = 0,
        ActorY              = 179190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 64950,
        TriggerZ            = 0,
        TriggerY            = 274130,
        TriggerRange        = 1000,
        ActorX              = 64980,
        ActorZ              = 0,
        ActorY              = 274850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 130900,
        TriggerZ            = 0,
        TriggerY            = 152640,
        TriggerRange        = 1000,
        ActorX              = 130930,
        ActorZ              = 0,
        ActorY              = 153290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -154890,
        TriggerZ            = 0,
        TriggerY            = 158890,
        TriggerRange        = 1000,
        ActorX              = -154240,
        ActorZ              = 0,
        ActorY              = 158990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -177340,
        TriggerZ            = 0,
        TriggerY            = 241160,
        TriggerRange        = 1000,
        ActorX              = -178080,
        ActorZ              = 0,
        ActorY              = 241020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_24F",          # 01, 1
        "Function_2_2CD",          # 02, 2
        "Function_3_2E3",          # 03, 3
        "Function_4_506",          # 04, 4
        "Function_5_722",          # 05, 5
        "Function_6_886",          # 06, 6
        "Function_7_9D5",          # 07, 7
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Return()

    # Function_0_24E end

    def Function_1_24F(): pass

    label("Function_1_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261")
    OP_6F(0x0, 0)
    Jump("loc_268")

    label("loc_261")

    OP_6F(0x0, 60)

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A")
    OP_6F(0x2, 0)
    Jump("loc_281")

    label("loc_27A")

    OP_6F(0x2, 60)

    label("loc_281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293")
    OP_6F(0x1, 0)
    Jump("loc_29A")

    label("loc_293")

    OP_6F(0x1, 60)

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC")
    OP_6F(0x3, 0)
    Jump("loc_2B3")

    label("loc_2AC")

    OP_6F(0x3, 60)

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5")
    OP_6F(0x4, 0)
    Jump("loc_2CC")

    label("loc_2C5")

    OP_6F(0x4, 60)

    label("loc_2CC")

    Return()

    # Function_1_24F end

    def Function_2_2CD(): pass

    label("Function_2_2CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CD")

    label("loc_2E2")

    Return()

    # Function_2_2CD end

    def Function_3_2E3(): pass

    label("Function_3_2E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -302930, 1500, 179190, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_332():
        OP_8F(0xFE, 0xFFFB60AE, 0x3E8, 0x2BBF6, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_332)

    def lambda_34D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_34D)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x30F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (2, "loc_3BE"),
        (1, "loc_3CE"),
        (SWITCH_DEFAULT, "loc_3D1"),
    )


    label("loc_3AC")

    OP_A2(0x6C9)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_3D1")

    label("loc_3BE")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3CE")

    OP_B4(0x0)
    Return()

    label("loc_3D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xD9, 1)"), scpexpr(EXPR_END)), "loc_42A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "代达罗斯护腕\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6C8)
    Jump("loc_4A4")

    label("loc_42A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "代达罗斯护腕\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "代达罗斯护腕\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4A4")

    Jump("loc_4F8")

    label("loc_4A7")

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
    OP_83(0xF, 0x4E)

    label("loc_4F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2E3 end

    def Function_4_506(): pass

    label("Function_4_506")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 64980, 1500, 274850, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_555():
        OP_8F(0xFE, 0xFDD4, 0x3E8, 0x431A2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_555)

    def lambda_570():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_570)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x30F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5CF"),
        (2, "loc_5E1"),
        (1, "loc_5F1"),
        (SWITCH_DEFAULT, "loc_5F4"),
    )


    label("loc_5CF")

    OP_A2(0x6CB)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_5F4")

    label("loc_5E1")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5F1")

    OP_B4(0x0)
    Return()

    label("loc_5F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x62, 1)"), scpexpr(EXPR_END)), "loc_648")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "王权之光\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6CA)
    Jump("loc_6B8")

    label("loc_648")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "王权之光\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "王权之光\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6B8")

    Jump("loc_714")

    label("loc_6BB")

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
    OP_83(0xF, 0x4F)

    label("loc_714")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_506 end

    def Function_5_722(): pass

    label("Function_5_722")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_820")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_79D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6CC)
    Jump("loc_81D")

    label("loc_79D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "圣灵药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "圣灵药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_81D")

    Jump("loc_878")

    label("loc_820")

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
    OP_83(0xF, 0x50)

    label("loc_878")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_722 end

    def Function_6_886(): pass

    label("Function_6_886")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_984")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_901")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6CD)
    Jump("loc_981")

    label("loc_901")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "圣灵药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "圣灵药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_981")

    Jump("loc_9C7")

    label("loc_984")

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
    OP_83(0xF, 0x51)

    label("loc_9C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_886 end

    def Function_7_9D5(): pass

    label("Function_7_9D5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_A4C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6CE)
    Jump("loc_AC4")

    label("loc_A4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_AC4")

    Jump("loc_AF9")

    label("loc_AC7")

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
    OP_83(0xF, 0x52)

    label("loc_AF9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9D5 end

    SaveToFile()

Try(main)
