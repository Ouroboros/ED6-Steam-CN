from ED6ScenarioHelper import *

def main():
    # 街景林道

    CreateScenaFile(
        FileName            = 'R2301   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2301.x',
        MapIndex            = 102,
        MapDefaultBGM       = "ed60021",
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
        '梅威海道方向',                         # 9
        '杰尼丝王立学院方向',                   # 10
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
        Unknown_3A              = 102,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT09/CH10340 ._CH',             # 02
        'ED6_DT09/CH10341 ._CH',             # 03
        'ED6_DT09/CH11040 ._CH',             # 04
        'ED6_DT09/CH11041 ._CH',             # 05
        'ED6_DT09/CH11070 ._CH',             # 06
        'ED6_DT09/CH11071 ._CH',             # 07
        'ED6_DT09/CH11080 ._CH',             # 08
        'ED6_DT09/CH11081 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT09/CH10340P._CP',             # 02
        'ED6_DT09/CH10341P._CP',             # 03
        'ED6_DT09/CH11040P._CP',             # 04
        'ED6_DT09/CH11041P._CP',             # 05
        'ED6_DT09/CH11070P._CP',             # 06
        'ED6_DT09/CH11071P._CP',             # 07
        'ED6_DT09/CH11080P._CP',             # 08
        'ED6_DT09/CH11081P._CP',             # 09
    )

    DeclNpc(
        X                   = 128320,
        Z                   = 20,
        Y                   = -8070,
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
        X                   = 288640,
        Z                   = 10,
        Y                   = -9980,
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
        X                   = 164610,
        Z                   = 540,
        Y                   = -8970,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 161500,
        Z                   = -30,
        Y                   = -7250,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 193850,
        Z                   = 320,
        Y                   = -43450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 218740,
        Z                   = 0,
        Y                   = -37100,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x194,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 235120,
        Z                   = -10,
        Y                   = -3610,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x193,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 230490,
        Z                   = 130,
        Y                   = -5740,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x195,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 210450,
        Z                   = 10,
        Y                   = -27270,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 164610,
        Z                   = 540,
        Y                   = -8970,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x33A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 161500,
        Z                   = -30,
        Y                   = -7250,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x33A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 193850,
        Z                   = 320,
        Y                   = -43450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x336,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 218740,
        Z                   = 0,
        Y                   = -37100,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x338,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 235120,
        Z                   = -10,
        Y                   = -3610,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x337,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 230490,
        Z                   = 130,
        Y                   = -5740,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x339,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 210450,
        Z                   = 10,
        Y                   = -27270,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x336,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_2C2",          # 00, 0
        "Function_1_2E6",          # 01, 1
        "Function_2_36F",          # 02, 2
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2E5")
    OP_B1("R2301_y")
    OP_A2(0x434)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_2E5")

    Return()

    # Function_0_2C2 end

    def Function_1_2E6(): pass

    label("Function_1_2E6")

    OP_16(0x2, 0xFA0, 0x14C08, 0xFFFDA670, 0x3002A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310")
    OP_B1("R2301_y")
    Jump("loc_319")

    label("loc_310")

    OP_B1("R2301_n")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34B")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_36E")

    label("loc_34B")

    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_36E")

    Return()

    # Function_1_2E6 end

    def Function_2_36F(): pass

    label("Function_2_36F")

    OP_A2(0x434)
    EventBegin(0x0)
    OP_6D(275050, 0, -9400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 287750, 10, -9520, 90)
    SetChrPos(0x102, 287750, 10, -10870, 90)
    SetChrPos(0x105, 287750, 20, -10050, 90)
    FadeToBright(1000, 0)

    def lambda_3F3():
        OP_8E(0xFE, 0x4225C, 0x32, 0xFFFFDAD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F3)
    Sleep(500)

    def lambda_413():
        OP_8E(0xFE, 0x422AC, 0xFFFFFFF6, 0xFFFFD58A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_413)
    Sleep(500)

    def lambda_433():
        OP_8E(0xFE, 0x42798, 0xFFFFFFEC, 0xFFFFD8BE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_433)

    def lambda_44E():
        OP_6D(272170, 0, -9340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44E)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#001F#1P嗯……\x02\x03",
            "虽然只有几天，\x01",
            "但真的很开心呢～！\x02\x03",
            "#008F当然呢，上课这个除外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#4P你这是什么\x01",
            "本末倒置的话啊……\x02\x03",
            "#018F本来上课才是主业，\x01",
            "学园祭只是特别活动嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F#1P那也是啊～\x02\x03",
            "唉，原来不管在哪里\x01",
            "做学生都是那么辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F#2P呵呵……\x02\x03",
            "#044F……咦……？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)
    Sleep(200)
    OP_8C(0x105, 0, 400)
    Sleep(200)
    OP_8C(0x105, 90, 400)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_67E():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67E)
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        "#014F#4P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2P没什么……\x02\x03",
            "我觉得基库\x01",
            "好像不在这附近……\x02\x03",
            "到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#3P嘿嘿，\x01",
            "可能是去找吃的了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#045F#2P是啊……\x01",
            "那也可能是。\x02\x03",
            "对不起。\x01",
            "突然说了些奇怪的话……\x02\x03",
            "#040F那么，在出海道之前，\x01",
            "就让我们一起上路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#3P嗯⊙\x01",
            "慢慢走吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    ClearMapFlags(0x2000000)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_21()
    OP_1D(0x15)
    Return()

    # Function_2_36F end

    SaveToFile()

Try(main)
