from ED6ScenarioHelper import *

def main():
    # 梅威海道

    CreateScenaFile(
        FileName            = 'R2202   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2202.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R2202   ._SN',
            'ED6_DT01/R2202_1 ._SN',
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
        '扎古',                                 # 9
        '基库',                                 # 10
        '目标用摄像机',                         # 11
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
        Unknown_3A              = 101,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH02320 ._CH',             # 01
        'ED6_DT07/CH00045 ._CH',             # 02
        'ED6_DT09/CH10460 ._CH',             # 03
        'ED6_DT09/CH10461 ._CH',             # 04
        'ED6_DT09/CH10160 ._CH',             # 05
        'ED6_DT09/CH10161 ._CH',             # 06
        'ED6_DT09/CH10450 ._CH',             # 07
        'ED6_DT09/CH10451 ._CH',             # 08
        'ED6_DT09/CH10220 ._CH',             # 09
        'ED6_DT09/CH10221 ._CH',             # 0A
        'ED6_DT09/CH10480 ._CH',             # 0B
        'ED6_DT09/CH10481 ._CH',             # 0C
        'ED6_DT09/CH10470 ._CH',             # 0D
        'ED6_DT09/CH10471 ._CH',             # 0E
        'ED6_DT09/CH11060 ._CH',             # 0F
        'ED6_DT09/CH11061 ._CH',             # 10
        'ED6_DT09/CH11240 ._CH',             # 11
        'ED6_DT09/CH11241 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH02320P._CP',             # 01
        'ED6_DT07/CH00045P._CP',             # 02
        'ED6_DT09/CH10460P._CP',             # 03
        'ED6_DT09/CH10461P._CP',             # 04
        'ED6_DT09/CH10160P._CP',             # 05
        'ED6_DT09/CH10161P._CP',             # 06
        'ED6_DT09/CH10450P._CP',             # 07
        'ED6_DT09/CH10451P._CP',             # 08
        'ED6_DT09/CH10220P._CP',             # 09
        'ED6_DT09/CH10221P._CP',             # 0A
        'ED6_DT09/CH10480P._CP',             # 0B
        'ED6_DT09/CH10481P._CP',             # 0C
        'ED6_DT09/CH10470P._CP',             # 0D
        'ED6_DT09/CH10471P._CP',             # 0E
        'ED6_DT09/CH11060P._CP',             # 0F
        'ED6_DT09/CH11061P._CP',             # 10
        'ED6_DT09/CH11240P._CP',             # 11
        'ED6_DT09/CH11241P._CP',             # 12
    )

    DeclNpc(
        X                   = -7120,
        Z                   = 0,
        Y                   = 37380,
        Direction           = 315,
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
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x180,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 137430,
        Z                   = -2000,
        Y                   = -152480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 137430,
        Z                   = -2000,
        Y                   = -152480,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 146110,
        Z                   = -2000,
        Y                   = -272220,
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
        X                   = 195320,
        Z                   = -2000,
        Y                   = -200020,
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
        X                   = 117860,
        Z                   = -1990,
        Y                   = -86810,
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
        X                   = 108600,
        Z                   = -2090,
        Y                   = -127120,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x185,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 127020,
        Z                   = -2029,
        Y                   = -168530,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x186,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 131400,
        Z                   = -1930,
        Y                   = -226630,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x181,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 113340,
        Z                   = -6030,
        Y                   = -111320,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 118080,
        Z                   = -6670,
        Y                   = -145340,
        Unknown_0C          = 0,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x5DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 108600,
        Z                   = -2090,
        Y                   = -127120,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x329,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 127020,
        Z                   = -2029,
        Y                   = -168530,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 131400,
        Z                   = -1930,
        Y                   = -226630,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x325,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 113340,
        Z                   = -6030,
        Y                   = -111320,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x334,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 118080,
        Z                   = -6670,
        Y                   = -145340,
        Unknown_0C          = 0,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x5DF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 143910,
        Y                   = 1000,
        Z                   = -192310,
        Range               = 140270,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0xFFFCE4CE,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = 144550,
        Y                   = 1000,
        Z                   = -193950,
        Range               = 134900,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0xFFFD00EE,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 171570,
        Y                   = -3000,
        Z                   = -204390,
        Range               = 173310,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFD053A,
        Unknown_18          = 0x10000,
        Unknown_1C          = 1,
    )

    DeclEvent(
        X                   = 140060,
        Y                   = -4000,
        Z                   = -151030,
        Range               = 134200,
        Unknown_10          = 0x0,
        Unknown_14          = 0xFFFDA602,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 111300,
        TriggerZ            = -6040,
        TriggerY            = -229080,
        TriggerRange        = 1400,
        ActorX              = 111300,
        ActorZ              = -5040,
        ActorY              = -229080,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 145130,
        TriggerZ            = -2029,
        TriggerY            = -194770,
        TriggerRange        = 1500,
        ActorX              = 145130,
        ActorZ              = -500,
        ActorY              = -194770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 143160,
        TriggerZ            = -1960,
        TriggerY            = -203990,
        TriggerRange        = 1500,
        ActorX              = 143160,
        ActorZ              = -550,
        ActorY              = -203990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 123800,
        TriggerZ            = -6110,
        TriggerY            = -164160,
        TriggerRange        = 1000,
        ActorX              = 123890,
        ActorZ              = -6040,
        ActorY              = -164820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 110610,
        TriggerZ            = -2050,
        TriggerY            = -169010,
        TriggerRange        = 1000,
        ActorX              = 111270,
        ActorZ              = -1960,
        ActorY              = -169020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 114670,
        TriggerZ            = -6010,
        TriggerY            = -111030,
        TriggerRange        = 1000,
        ActorX              = 115310,
        ActorZ              = -5950,
        ActorY              = -111030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4D2",          # 00, 0
        "Function_1_4F0",          # 01, 1
        "Function_2_61D",          # 02, 2
        "Function_3_633",          # 03, 3
        "Function_4_F1C",          # 04, 4
        "Function_5_13B2",         # 05, 5
        "Function_6_140A",         # 06, 6
        "Function_7_146B",         # 07, 7
        "Function_8_16BF",         # 08, 8
        "Function_9_190E",         # 09, 9
        "Function_10_1A6C",        # 0A, 10
        "Function_11_1BA8",        # 0B, 11
    )


    def Function_0_4D2(): pass

    label("Function_0_4D2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_4D2 end

    def Function_1_4F0(): pass

    label("Function_1_4F0")

    OP_16(0x2, 0xFA0, 0x2710, 0xFFFB4128, 0x30028)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51A")
    OP_B1("R2202_y")
    Jump("loc_523")

    label("loc_51A")

    OP_B1("R2202_n")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54B")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_564")

    label("loc_54B")

    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B")
    OP_64(0x0, 0x1)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D")
    OP_6F(0x1, 0)
    Jump("loc_594")

    label("loc_58D")

    OP_6F(0x1, 60)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6")
    OP_6F(0x2, 0)
    Jump("loc_5AD")

    label("loc_5A6")

    OP_6F(0x2, 60)

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")
    OP_6F(0x3, 0)
    Jump("loc_5C6")

    label("loc_5BF")

    OP_6F(0x3, 60)

    label("loc_5C6")

    OP_B2(0x0, 0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    ClearChrFlags(0xC, 0x80)
    OP_B2(0x1, 0x3, 0x80)

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_5F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6")
    ClearChrFlags(0xD, 0x80)
    OP_B2(0x1, 0x3, 0x80)

    label("loc_5F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60D")
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_60D")

    OP_22(0x1C8, 0x1, 0x64)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_4F0 end

    def Function_2_61D(): pass

    label("Function_2_61D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_632")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_61D")

    label("loc_632")

    Return()

    # Function_2_61D end

    def Function_3_633(): pass

    label("Function_3_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1B")
    OP_A2(0x435)
    OP_28(0x3E, 0x4, 0x2)
    OP_28(0x3E, 0x4, 0x4)
    OP_28(0x3E, 0x1, 0x1)
    OP_28(0x1C, 0x4, 0x40)
    OP_28(0x20, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A")
    OP_28(0x21, 0x4, 0x40)

    label("loc_66A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A")
    OP_28(0x1E, 0x4, 0x40)

    label("loc_67A")

    OP_28(0x26, 0x4, 0x40)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(140150, -2000, -197420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 140170, -2000, -197360, 180)
    SetChrPos(0x101, 140900, -2000, -198500, 0)
    SetChrPos(0x102, 139540, -2000, -198900, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#010F好了，就在这里分手吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F嗯……\x02\x03",
            "#048F这几天承蒙你们的帮忙，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，别客气啦。\x01",
            "而且我们两个也玩得很开心。\x02\x03",
            "#006F那么……\x01",
            "替我们向特蕾莎院长他们问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F嗯，我一定会转告的。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 138530, -2000, -188460, 0)

    NpcTalk(
        0x8,
        "青年的声音",
        "#4P啊，是你们啊！\x02",
    )

    CloseMessageWindow()

    def lambda_83A():

        label("loc_83A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_83A")

    QueueWorkItem2(0x105, 1, lambda_83A)

    def lambda_84B():

        label("loc_84B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_84B")

    QueueWorkItem2(0x101, 1, lambda_84B)

    def lambda_85C():

        label("loc_85C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_85C")

    QueueWorkItem2(0x102, 1, lambda_85C)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x8, 0x21E9E, 0xFFFFF830, 0xFFFCFD10, 0x1388, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x101,
        "#004F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F您是……\x01",
            "玛诺利亚村的村民吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P真的是你们啊！\x01",
            "两位游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P大、大事不好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F大事不好……？\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(
        0x8,
        "#1P哈啊哈啊哈啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1P稍、稍等一会儿。\x01",
            "让、让我喘口气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P呼～呼～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P…………………呼……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_1D(0x56)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#1P……特蕾莎老师和孩子们，\x01",
            "在玛诺利亚附近被人袭击了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F什、什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F#1P………………啊………\x02",
    )

    OP_9E(0x105, 0x1E, 0x0, 0x190, 0x1388)
    CloseMessageWindow()

    def lambda_AB7():
        OP_94(0x1, 0x105, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AB7)
    WaitChrThread(0x105, 0x2)
    Fade(500)
    SetChrChipByIndex(0x105, 2)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 400)

    def lambda_B00():
        OP_92(0xFE, 0x105, 0x258, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B00)
    TurnDirection(0x102, 0x105, 400)
    TurnDirection(0x8, 0x105, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#004F你、你还好吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……振作点。\x01",
            "现在可不是倒下的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F#1P对、对不起……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x105, 65535)
    OP_0D()
    OP_94(0x1, 0x105, 0x0, 0x1F4, 0x3E8, 0x0)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x105,
        (
            "#043F#1P拜托了……\x01",
            "请告诉我们详细情形好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他们是在从王立学院回来的路上，\x01",
            "被一群奇怪的家伙袭击的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "孩子们都没受伤，\x01",
            "不过特蕾莎老师还有\x01",
            "护送的游击士大姐都晕过去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？卡露娜姐姐也！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F看来犯人很不简单……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F#1P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "本来想通知你们协会的，\x01",
            "但旅店的通信器似乎坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "情急之下，\x01",
            "我就只好急忙跑过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F是这样吗……\x01",
            "多谢您的紧急协助。\x02\x03",
            "#012F不过，如果可以的话，\x01",
            "可以麻烦您去一趟卢安吗？\x02\x03",
            "因为我们要马上赶去玛诺利亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(
        0x8,
        "#1P好，知道了！\x02",
    )

    CloseMessageWindow()

    def lambda_E69():

        label("loc_E69")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E69")

    QueueWorkItem2(0x105, 1, lambda_E69)

    def lambda_E7A():

        label("loc_E7A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E7A")

    QueueWorkItem2(0x101, 1, lambda_E7A)

    def lambda_E8B():

        label("loc_E8B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E8B")

    QueueWorkItem2(0x102, 1, lambda_E8B)
    OP_8E(0x8, 0x21688, 0xFFFFF830, 0xFFFCE528, 0x1388, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        "#012F好了，我们也快点吧！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F#1P……………好的！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_21()
    OP_1D(0x14)

    label("loc_F1B")

    Return()

    # Function_3_633 end

    def Function_4_F1C(): pass

    label("Function_4_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B1")
    OP_A2(0x43E)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(139070, -2000, -192040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 138410, -2009, -190790, 180)
    SetChrPos(0x102, 139470, -2029, -190120, 180)
    SetChrPos(0x105, 138400, -2009, -189000, 180)
    FadeToBright(500, 0)

    def lambda_FB7():
        OP_6D(139620, -2000, -195740, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FB7)

    def lambda_FCF():
        OP_8E(0xFE, 0x21FE8, 0xFFFFF830, 0xFFFCFF04, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCF)

    def lambda_FEA():
        OP_8E(0xFE, 0x22498, 0xFFFFF830, 0xFFFD0198, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FEA)

    def lambda_1005():
        OP_8E(0xFE, 0x22182, 0xFFFFF830, 0xFFFD06CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1005)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x105,
        "#043F……那个…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#004F科洛丝，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F那个……\x01",
            "艾丝蒂尔你们先去协会可以吗？\x02\x03",
            "我想起有件事要办，\x01",
            "所以想暂时离开一下。\x02\x03",
            "很快就会追上你们的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F我们倒没关系……\x01",
            "你是要先回学院吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F是、是的……\x02\x03",
            "我想先把事情\x01",
            "向校长也汇报一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这样啊……\x01",
            "嗯，我明白了。\x02\x03",
            "我们在协会等你！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    def lambda_11EC():
        OP_8E(0xFE, 0x2161A, 0xFFFFF830, 0xFFFCE190, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11EC)
    OP_8C(0x102, 180, 400)

    def lambda_120E():
        OP_8E(0xFE, 0x219BC, 0xFFFFF830, 0xFFFCE26C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_120E)
    WaitChrThread(0x102, 0x1)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
    OP_69(0x105, 0x3E8)

    ChrTalk(
        0x105,
        (
            "#049F#2P对不起……\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "科洛丝取出了身上的笔记本和笔，\x01",
            "写下了几行字。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x105,
        "#047F#2P嗯，这就行了。\x02",
    )

    CloseMessageWindow()

    def lambda_1305():
        OP_6D(135220, -2040, -194820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1305)
    OP_8C(0x105, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x105,
        "#042F#4P……基库！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 121590, 7000, -203340, 90)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0x9, 0x105, 0x1388, 0x2710, 0x0)
    OP_92(0x9, 0x105, 0xFA0, 0x1F40, 0x0)
    OP_92(0x9, 0x105, 0xBB8, 0x1770, 0x0)
    FadeToDark(1000, 0, -1)
    OP_92(0x9, 0x105, 0x7D0, 0xBB8, 0x0)
    OP_92(0x9, 0x105, 0x3E8, 0x5DC, 0x0)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2120   ._SN", 105, 0, 0)
    IdleLoop()

    label("loc_13B1")

    Return()

    # Function_4_F1C end

    def Function_5_13B2(): pass

    label("Function_5_13B2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　杰尼丝王立学院　２５２塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_13B2 end

    def Function_6_140A(): pass

    label("Function_6_140A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南　卢安市\x01",
            "北　玛诺利亚村　　　３１２塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_140A end

    def Function_7_146B(): pass

    label("Function_7_146B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1477")
    Call(0, 8)
    Return()

    label("loc_1477")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_156F"),
        (SWITCH_DEFAULT, "loc_158B"),
    )


    label("loc_156F")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_158B")

    Battle(0x3FB, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, 137350, -2000, -149140, 180)
    SetChrPos(0x1, 137350, -2000, -149140, 180)
    SetChrPos(0x2, 137350, -2000, -149140, 180)
    SetChrPos(0x3, 137350, -2000, -149140, 180)
    SetChrPos(0x4, 137350, -2000, -149140, 180)
    SetChrPos(0x5, 137350, -2000, -149140, 180)
    SetChrPos(0x6, 137350, -2000, -149140, 180)
    SetChrPos(0x7, 137350, -2000, -149140, 180)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1639"),
        (1, "loc_163C"),
        (SWITCH_DEFAULT, "loc_163F"),
    )


    label("loc_1639")

    EventEnd(0x0)
    Return()

    label("loc_163C")

    OP_B4(0x0)
    Return()

    label("loc_163F")

    EventBegin(0x1)
    SetChrFlags(0xC, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了梅威海道中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x4C6)
    OP_28(0x24, 0x4, 0x10)
    OP_28(0x24, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_146B end

    def Function_8_16BF(): pass

    label("Function_8_16BF")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_17B7"),
        (SWITCH_DEFAULT, "loc_17D3"),
    )


    label("loc_17B7")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_17D3")

    Battle(0x3FC, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, 137310, -2000, -155800, 0)
    SetChrPos(0x1, 137310, -2000, -155800, 0)
    SetChrPos(0x2, 137310, -2000, -155800, 0)
    SetChrPos(0x3, 137310, -2000, -155800, 0)
    SetChrPos(0x4, 137310, -2000, -155800, 0)
    SetChrPos(0x5, 137310, -2000, -155800, 0)
    SetChrPos(0x6, 137310, -2000, -155800, 0)
    SetChrPos(0x7, 137310, -2000, -155800, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1881"),
        (1, "loc_1884"),
        (SWITCH_DEFAULT, "loc_1887"),
    )


    label("loc_1881")

    EventEnd(0x0)
    Return()

    label("loc_1884")

    OP_B4(0x0)
    Return()

    label("loc_1887")

    EventBegin(0x1)
    SetChrFlags(0xD, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了梅威海道中被通缉的魔兽②！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x4C7)
    OP_28(0x25, 0x4, 0x10)
    OP_28(0x25, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_8_16BF end

    def Function_9_190E(): pass

    label("Function_9_190E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1984")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    FadeToBright(300, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4BF)
    Jump("loc_19FA")

    label("loc_1984")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_19FA")

    Jump("loc_1A5E")

    label("loc_19FD")

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
    OP_83(0xF, 0x88)

    label("loc_1A5E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_190E end

    def Function_10_1A6C(): pass

    label("Function_10_1A6C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1AE2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4C0)
    Jump("loc_1B58")

    label("loc_1AE2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1B58")

    Jump("loc_1B9A")

    label("loc_1B5B")

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
    OP_83(0xF, 0x89)

    label("loc_1B9A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1A6C end

    def Function_11_1BA8(): pass

    label("Function_11_1BA8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D79")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA6")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 115310, -3500, -111030, 320)
    TurnDirection(0xB, 0x0, 0)

    def lambda_1BF7():
        OP_8F(0xFE, 0x1C26E, 0xFFFFEC78, 0xFFFE4E4A, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1BF7)

    def lambda_1C12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1C12)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C5B")
    Battle(0x322, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C68")

    label("loc_1C5B")

    Battle(0x17E, 0x0, 0x0, 0x0, 0xFF)

    label("loc_1C68")

    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1C81"),
        (2, "loc_1C93"),
        (1, "loc_1CA3"),
        (SWITCH_DEFAULT, "loc_1CA6"),
    )


    label("loc_1C81")

    OP_A2(0x4C2)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_1CA6")

    label("loc_1C93")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1CA3")

    OP_B4(0x0)
    Return()

    label("loc_1CA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF9, 1)"), scpexpr(EXPR_END)), "loc_1CFE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "战斗服\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4C1)
    Jump("loc_1D76")

    label("loc_1CFE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "战斗服\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "战斗服\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1D76")

    Jump("loc_1DC0")

    label("loc_1D79")

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
    OP_83(0xF, 0x8A)

    label("loc_1DC0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1BA8 end

    SaveToFile()

Try(main)
