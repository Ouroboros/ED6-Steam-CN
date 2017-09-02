from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        '科洛丝',                               # 9
        '基库',                                 # 10
        '理查德上校',                           # 11
        '洛伦斯少尉',                           # 12
        '卡露娜',                               # 13
        '亚妮拉丝',                             # 14
        '库拉茨',                               # 15
        '克鲁茨',                               # 16
        '尤莉亚中尉',                           # 17
        '亲卫队员',                             # 18
        '亲卫队员',                             # 19
        '亲卫队员',                             # 20
        '亲卫队员',                             # 21
        '亲卫队员',                             # 22
        '亲卫队员',                             # 23
        '亲卫队员',                             # 24
        '亲卫队员',                             # 25
        '特务艇影子',                           # 26
        '特务艇',                               # 27
        '特务兵',                               # 28
        '特务兵',                               # 29
        '特务兵',                               # 30
        '特务兵',                               # 31
        '圣海姆门方向',                         # 32
        '王都格兰赛尔方向',                     # 33
        '格鲁纳门方向',                         # 34
        '沼泽剑齿吸血魔',                       # 35
        '丘陵毒蜂',                             # 36
        '迅猛小鹫',                             # 37
        '迅猛小鹫',                             # 38
        '沼泽剑齿吸血魔',                       # 39
        '剑齿吸血魔',                           # 40
        '丘陵毒蜂',                             # 41
        '迅猛小鹫',                             # 42
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
        'ED6_DT07/CH00040 ._CH',             # 00
        'ED6_DT07/CH02320 ._CH',             # 01
        'ED6_DT07/CH02030 ._CH',             # 02
        'ED6_DT07/CH02200 ._CH',             # 03
        'ED6_DT07/CH01240 ._CH',             # 04
        'ED6_DT07/CH01630 ._CH',             # 05
        'ED6_DT07/CH01260 ._CH',             # 06
        'ED6_DT07/CH01620 ._CH',             # 07
        'ED6_DT07/CH02090 ._CH',             # 08
        'ED6_DT07/CH01320 ._CH',             # 09
        'ED6_DT07/CH01610 ._CH',             # 0A
        'ED6_DT06/CH20051 ._CH',             # 0B
        'ED6_DT07/CH00041 ._CH',             # 0C
        'ED6_DT09/CH10780 ._CH',             # 0D
        'ED6_DT09/CH10781 ._CH',             # 0E
        'ED6_DT09/CH10790 ._CH',             # 0F
        'ED6_DT09/CH10791 ._CH',             # 10
        'ED6_DT09/CH10050 ._CH',             # 11
        'ED6_DT09/CH10051 ._CH',             # 12
        'ED6_DT09/CH10800 ._CH',             # 13
        'ED6_DT09/CH10801 ._CH',             # 14
        'ED6_DT09/CH10810 ._CH',             # 15
        'ED6_DT09/CH10811 ._CH',             # 16
        'ED6_DT09/CH10820 ._CH',             # 17
        'ED6_DT09/CH10821 ._CH',             # 18
        'ED6_DT09/CH11220 ._CH',             # 19
        'ED6_DT09/CH11221 ._CH',             # 1A
        'ED6_DT09/CH11230 ._CH',             # 1B
        'ED6_DT09/CH11231 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH00040P._CP',             # 00
        'ED6_DT07/CH02320P._CP',             # 01
        'ED6_DT07/CH02030P._CP',             # 02
        'ED6_DT07/CH02200P._CP',             # 03
        'ED6_DT07/CH01240P._CP',             # 04
        'ED6_DT07/CH01630P._CP',             # 05
        'ED6_DT07/CH01260P._CP',             # 06
        'ED6_DT07/CH01620P._CP',             # 07
        'ED6_DT07/CH02090P._CP',             # 08
        'ED6_DT07/CH01320P._CP',             # 09
        'ED6_DT07/CH01610P._CP',             # 0A
        'ED6_DT06/CH20051P._CP',             # 0B
        'ED6_DT07/CH00041P._CP',             # 0C
        'ED6_DT09/CH10780P._CP',             # 0D
        'ED6_DT09/CH10781P._CP',             # 0E
        'ED6_DT09/CH10790P._CP',             # 0F
        'ED6_DT09/CH10791P._CP',             # 10
        'ED6_DT09/CH10050P._CP',             # 11
        'ED6_DT09/CH10051P._CP',             # 12
        'ED6_DT09/CH10800P._CP',             # 13
        'ED6_DT09/CH10801P._CP',             # 14
        'ED6_DT09/CH10810P._CP',             # 15
        'ED6_DT09/CH10811P._CP',             # 16
        'ED6_DT09/CH10820P._CP',             # 17
        'ED6_DT09/CH10821P._CP',             # 18
        'ED6_DT09/CH11220P._CP',             # 19
        'ED6_DT09/CH11221P._CP',             # 1A
        'ED6_DT09/CH11230P._CP',             # 1B
        'ED6_DT09/CH11231P._CP',             # 1C
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5160,
        Z                   = -50,
        Y                   = -7520,
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
        X                   = -39160,
        Z                   = 0,
        Y                   = 152720,
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
        X                   = 61180,
        Z                   = 0,
        Y                   = 83020,
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
        X                   = -6830,
        Z                   = 90,
        Y                   = 29510,
        Unknown_0C          = 0,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16290,
        Z                   = 70,
        Y                   = 76970,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31220,
        Z                   = 40,
        Y                   = 83060,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33000,
        Z                   = 20,
        Y                   = 72240,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17830,
        Z                   = 10,
        Y                   = 103860,
        Unknown_0C          = 0,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -58070,
        Z                   = 30,
        Y                   = 101390,
        Unknown_0C          = 0,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -59820,
        Z                   = 0,
        Y                   = 105790,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61630,
        Z                   = 70,
        Y                   = 108700,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -13540,
        TriggerZ            = 0,
        TriggerY            = 63650,
        TriggerRange        = 1500,
        ActorX              = -13540,
        ActorZ              = 1700,
        ActorY              = 63650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 130,
        TriggerZ            = 0,
        TriggerY            = 56450,
        TriggerRange        = 1500,
        ActorX              = 130,
        ActorZ              = 1700,
        ActorY              = 56450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1460,
        TriggerZ            = 0,
        TriggerY            = 53030,
        TriggerRange        = 1500,
        ActorX              = -1460,
        ActorZ              = 1700,
        ActorY              = 53030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_61E",          # 00, 0
        "Function_1_666",          # 01, 1
        "Function_2_679",          # 02, 2
        "Function_3_ED6",          # 03, 3
        "Function_4_1202",         # 04, 4
        "Function_5_1266",         # 05, 5
        "Function_6_12CA",         # 06, 6
        "Function_7_132E",         # 07, 7
        "Function_8_1392",         # 08, 8
        "Function_9_13E4",         # 09, 9
        "Function_10_144D",        # 0A, 10
        "Function_11_14A8",        # 0B, 11
        "Function_12_17A0",        # 0C, 12
        "Function_13_17E8",        # 0D, 13
        "Function_14_1818",        # 0E, 14
        "Function_15_1848",        # 0F, 15
        "Function_16_1878",        # 10, 16
        "Function_17_18A8",        # 11, 17
        "Function_18_18D8",        # 12, 18
        "Function_19_1908",        # 13, 19
        "Function_20_1938",        # 14, 20
        "Function_21_1968",        # 15, 21
        "Function_22_1998",        # 16, 22
        "Function_23_19C8",        # 17, 23
        "Function_24_19F8",        # 18, 24
        "Function_25_1A28",        # 19, 25
        "Function_26_1A68",        # 1A, 26
        "Function_27_1AB8",        # 1B, 27
    )


    def Function_0_61E(): pass

    label("Function_0_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_63D")
    SoundLoad(121)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_654")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 11)

    label("loc_654")

    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_61E end

    def Function_1_666(): pass

    label("Function_1_666")

    OP_16(0x2, 0xFA0, 0xFFFDF0A8, 0xFFFF15A0, 0x3003C)
    Return()

    # Function_1_666 end

    def Function_2_679(): pass

    label("Function_2_679")

    OP_B6(0x0)
    ClearMapFlags(0x2000000)
    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_77(0xC8, 0xC8, 0xC8, 0x0, 0x0)
    OP_6D(-38280, 0, 81580, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    OP_11(0x0, 0x0, 0x0, 0x9470, 0x1FBD0, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -38320, 0, 69680, 270)
    SetChrPos(0x9, -39300, 6000, 86750, 270)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrChipByIndex(0x8, 12)

    def lambda_72A():
        OP_8E(0xFE, 0xFFFF644C, 0x0, 0x19866, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72A)
    Sleep(1000)

    def lambda_74A():
        OP_6D(-38720, 0, 104400, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_74A)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0)

    ChrTalk(
        0x8,
        "#049F#5P呼呼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "#043F#5P……基库，过来！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    OP_92(0x9, 0x8, 0x2710, 0x2328, 0x0)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0x9, 0x8, 0x1388, 0x1F40, 0x0)
    OP_92(0x9, 0x8, 0xFA0, 0x1770, 0x0)
    OP_92(0x9, 0x8, 0xBB8, 0xFA0, 0x0)
    OP_92(0x9, 0x8, 0x7D0, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF6154, 0x3E8, 0x19820, 0x5DC, 0x0)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 2)

    def lambda_81E():
        OP_8C(0xFE, 135, 200)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_81E)
    OP_8F(0x9, 0xFFFF62A8, 0xC8, 0x19852, 0x3E8, 0x0)
    WaitChrThread(0x9, 0x3)
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Fade(250)
    SetChrFlags(0x9, 0x80)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#310F啾？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#043F#5P我已经没事了，\x01",
            "你去尤莉亚那里吧。\x02\x03",
            "这样下去尤莉亚会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#311F啾～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#048F#5P谢谢，拜托了！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x8, 2)
    OP_0D()
    OP_22(0x8C, 0x0, 0x64)

    def lambda_91D():
        OP_8E(0xFE, 0xFFFF6EB0, 0x2710, 0x10C66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_91D)
    Sleep(400)

    def lambda_93D():
        OP_8E(0xFE, 0xFFFF6EB0, 0x2710, 0x10C66, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_93D)
    Sleep(400)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0)

    def lambda_96C():
        OP_8E(0xFE, 0xFFFF6EB0, 0x2710, 0x10C66, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_96C)

    def lambda_987():

        label("loc_987")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_987")

    QueueWorkItem2(0x8, 1, lambda_987)
    Sleep(1800)
    OP_44(0x8, 0xFF)
    OP_8C(0x8, 90, 400)

    def lambda_9A8():
        OP_6D(-39530, 0, 108060, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9A8)
    OP_8E(0x8, 0xFFFF6596, 0x0, 0x1A61C, 0x7D0, 0x0)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#042F尤莉亚说得没错，\x01",
            "这里的警戒果然比较薄弱……\x02\x03",
            "不赶快去游击士协会的话……\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -39360, 0, 108740, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x105, 0x3, 0x0, 0x9)
    Sleep(1500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#043F下雨了……\x02\x03",
            "#047F……………………………\x02\x03",
            "#049F对了……\x01",
            "艾丝蒂尔他们也应该快来到王都了……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x79, 0x1, 0x50)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x19, 800)

    def lambda_B57():

        label("loc_B57")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_B57")

    QueueWorkItem2(0x8, 1, lambda_B57)

    ChrTalk(
        0x8,
        "#044F……难道！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    StopSound(0xC350, 0x30D40, 0x0)
    Fade(1000)
    OP_6C(134000, 0)
    OP_6D(-28620, 12200, 104390, 0)
    OP_6B(4810, 0)
    OP_67(0, 8730, -10000, 0)
    OP_24(0x79, 0x64)
    OP_43(0x19, 0x1, 0x0, 0x3)
    Sleep(4000)

    def lambda_BDD():
        OP_6B(6420, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BDD)

    def lambda_BED():
        OP_6D(-38470, 6000, 118990, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BED)

    def lambda_C05():
        OP_6C(24000, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C05)
    Sleep(8000)

    def lambda_C1A():
        OP_6D(-38470, 0, 118990, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C1A)

    def lambda_C32():
        OP_67(0, 5740, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C32)
    Sleep(3000)
    OP_8F(0x8, 0xFFFF6550, 0x0, 0x19F32, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#046F情报部的特务飞艇……！\x02\x03",
            "怎么会……\x01",
            "竟然在光天化日之下出现在王都前面……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -38770, 0, 98180, 0)

    def lambda_CEC():
        OP_8E(0xFE, 0xFFFF6604, 0x0, 0x193F2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CEC)
    Sleep(300)

    def lambda_D0C():
        OP_6B(5300, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D0C)
    OP_6D(-39190, 0, 105060, 1000)

    ChrTalk(
        0x8,
        "#043F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#280F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_D4E():
        OP_6D(-39940, 2250, 109870, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D4E)

    def lambda_D66():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D66)

    def lambda_D76():
        OP_6D(-39940, 2250, 109870, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D76)
    WaitChrThread(0x19, 0x1)
    OP_73(0x0)

    def lambda_D96():
        OP_6D(-39410, 0, 106900, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D96)
    WaitChrThread(0x1E, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x40)
    SetChrBattleFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x80)
    OP_89(0xA, -38890, 3450, 120920, 180)
    WaitChrThread(0x0, 0x3)

    NpcTalk(
        0xA,
        "男性的声音",
        "#4P啊，在这种地方相遇真是难得啊。\x02",
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0x8)
    Sleep(300)
    TurnDirection(0x8, 0xA, 400)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#115F杰尼丝王立学院社会系的\x01",
            "科洛丝·琳希小姐……\x02\x03",
            "#111F能和您稍微谈一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x105, 0x3, 0x0, 0xA)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x3FA)
    WaitChrThread(0x105, 0x3)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_679 end

    def Function_3_ED6(): pass

    label("Function_3_ED6")

    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x40)
    OP_A1(0x19, 0x0)
    OP_A1(0x1A, 0x1)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 700)
    OP_70(0x0, 0x30C)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    SetChrPos(0x19, -13930, 20000, 76820, 324)
    SetChrPos(0x1A, -13930, 0, 76820, 324)

    def lambda_F4D():
        OP_8F(0xFE, 0xFFFF685C, 0x1388, 0x1D8A8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_F4D)

    def lambda_F68():
        OP_8F(0xFE, 0xFFFF685C, 0x64, 0x1D8A8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_F68)
    Sleep(3000)

    def lambda_F88():
        OP_8F(0xFE, 0xFFFF685C, 0x1388, 0x1D8A8, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_F88)

    def lambda_FA3():
        OP_8F(0xFE, 0xFFFF685C, 0x64, 0x1D8A8, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_FA3)

    def lambda_FBE():
        OP_8C(0x19, 0, 5)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_FBE)

    def lambda_FCC():
        OP_8C(0x1A, 0, 5)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_FCC)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1014():
        OP_8F(0xFE, 0xFFFF685C, 0x1388, 0x1D8A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1014)

    def lambda_102F():
        OP_8F(0xFE, 0xFFFF685C, 0x64, 0x1D8A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_102F)
    Sleep(1000)

    def lambda_104F():
        OP_8F(0xFE, 0xFFFF685C, 0x1388, 0x1D8A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_104F)

    def lambda_106A():
        OP_8F(0xFE, 0xFFFF685C, 0x64, 0x1D8A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_106A)
    Sleep(1000)

    def lambda_108A():
        OP_8F(0xFE, 0xFFFF685C, 0x1388, 0x1D8A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_108A)

    def lambda_10A5():
        OP_8F(0xFE, 0xFFFF685C, 0x64, 0x1D8A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_10A5)
    Sleep(1000)
    WaitChrThread(0x19, 0x2)
    OP_72(0x0, 0x20)
    PlayEffect(0x1, 0x2, 0x1A, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_6F(0x0, 1021)
    OP_70(0x0, 0x41A)
    OP_73(0x0)
    OP_6F(0x0, 1051)
    OP_70(0x0, 0x456)
    OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xBB8, 0x0)
    OP_91(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x9C4, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_91(0xFE, 0x0, 0xFFFFF704, 0x0, 0x7D0, 0x0)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_6F(0x0, 61)
    OP_70(0x0, 0xE6)
    OP_73(0x0)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 231)
    OP_70(0x0, 0x168)
    OP_73(0x0)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    OP_73(0x0)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    OP_43(0x1B, 0x1, 0x0, 0x4)
    Sleep(300)
    OP_43(0x1C, 0x1, 0x0, 0x5)
    Sleep(300)
    OP_43(0x1D, 0x1, 0x0, 0x6)
    Sleep(300)
    OP_43(0x1E, 0x1, 0x0, 0x7)
    Return()

    # Function_3_ED6 end

    def Function_4_1202(): pass

    label("Function_4_1202")

    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, -38890, 3450, 120920, 180)
    OP_8E(0xFE, 0xFFFF6834, 0xD7A, 0x1CA34, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF683E, 0x0, 0x1B418, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF5790, 0x0, 0x19DE8, 0x1388, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_4_1202 end

    def Function_5_1266(): pass

    label("Function_5_1266")

    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, -38890, 3450, 120920, 180)
    OP_8E(0xFE, 0xFFFF6834, 0xD7A, 0x1CA34, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF683E, 0x0, 0x1B418, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF7518, 0x0, 0x19DE8, 0x1388, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_5_1266 end

    def Function_6_12CA(): pass

    label("Function_6_12CA")

    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, -38890, 3450, 120920, 180)
    OP_8E(0xFE, 0xFFFF6834, 0xD7A, 0x1CA34, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF683E, 0x0, 0x1B418, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF5D80, 0x0, 0x1A720, 0x1388, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_6_12CA end

    def Function_7_132E(): pass

    label("Function_7_132E")

    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_89(0xFE, -38890, 3450, 120920, 180)
    OP_8E(0xFE, 0xFFFF6834, 0xD7A, 0x1CA34, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF683E, 0x0, 0x1B418, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF6DF2, 0x0, 0x1A720, 0x1388, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_7_132E end

    def Function_8_1392(): pass

    label("Function_8_1392")

    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFF6834, 0xD7A, 0x1CA34, 0xBB8, 0x0)

    def lambda_13B1():
        OP_6B(4270, 2500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13B1)
    OP_8E(0xFE, 0xFFFF683E, 0x0, 0x1B418, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF65B4, 0x0, 0x1A3EC, 0xBB8, 0x0)
    Return()

    # Function_8_1392 end

    def Function_9_13E4(): pass

    label("Function_9_13E4")

    OP_22(0x1C9, 0x1, 0xA)
    Sleep(700)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x41)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x4B)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x55)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    Sleep(300)
    OP_24(0x1C9, 0x5F)
    Sleep(300)
    OP_24(0x1C9, 0x64)
    Return()

    # Function_9_13E4 end

    def Function_10_144D(): pass

    label("Function_10_144D")

    Sleep(100)
    OP_24(0x1C9, 0x5F)
    Sleep(100)
    OP_24(0x1C9, 0x5A)
    Sleep(100)
    OP_24(0x1C9, 0x55)
    Sleep(100)
    OP_24(0x1C9, 0x50)
    Sleep(100)
    OP_24(0x1C9, 0x4B)
    Sleep(100)
    OP_24(0x1C9, 0x46)
    Sleep(100)
    OP_24(0x1C9, 0x3C)
    Sleep(100)
    OP_24(0x1C9, 0x32)
    Sleep(100)
    OP_24(0x1C9, 0x28)
    Sleep(100)
    OP_24(0x1C9, 0x1)
    Return()

    # Function_10_144D end

    def Function_11_14A8(): pass

    label("Function_11_14A8")

    OP_B6(0x0)
    EventBegin(0x0)
    OP_6D(-38800, 0, 97110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrPos(0x10, -38880, 0, 82480, 0)
    SetChrPos(0xD, -38350, 0, 81550, 0)
    SetChrPos(0x11, -38350, 0, 80450, 0)
    SetChrPos(0x12, -38350, 0, 79350, 0)
    SetChrPos(0x13, -38350, 0, 78250, 0)
    SetChrPos(0x14, -38350, 0, 77150, 0)
    SetChrPos(0xE, -38350, 0, 76050, 0)
    SetChrPos(0xC, -39570, 0, 81550, 0)
    SetChrPos(0x15, -39570, 0, 80450, 0)
    SetChrPos(0x16, -39570, 0, 79350, 0)
    SetChrPos(0x17, -39570, 0, 78250, 0)
    SetChrPos(0x18, -39570, 0, 77150, 0)
    SetChrPos(0xF, -39570, 0, 76050, 0)
    FadeToBright(2000, 0)
    OP_43(0x10, 0x1, 0x0, 0xC)
    OP_43(0xC, 0x1, 0x0, 0x12)
    OP_43(0xD, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x11, 0x1, 0x0, 0x14)
    OP_43(0x15, 0x1, 0x0, 0xE)
    Sleep(100)
    OP_43(0x12, 0x1, 0x0, 0x16)
    OP_43(0x16, 0x1, 0x0, 0x10)
    Sleep(100)
    OP_43(0x13, 0x1, 0x0, 0x15)
    OP_43(0x17, 0x1, 0x0, 0xF)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x17)
    OP_43(0x18, 0x1, 0x0, 0x11)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x13)
    OP_43(0xF, 0x1, 0x0, 0xD)

    def lambda_1694():
        OP_6D(-38550, 0, 106960, 6500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1694)

    def lambda_16AC():
        OP_6E(405, 6500)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_16AC)
    Sleep(2500)

    def lambda_16C1():
        OP_67(0, 6530, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_16C1)

    def lambda_16D9():
        OP_6C(314000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_16D9)
    Sleep(5100)

    def lambda_16EE():
        OP_6D(-36100, 0, 109830, 4000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_16EE)

    def lambda_1706():
        OP_67(0, 4320, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1706)
    Sleep(4000)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x10,
        (
            "#178F#5P好……\x01",
            "各位，在此等候时机的到来。\x02\x03",
            "正午钟响的同时就冲进去。\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_14A8 end

    def Function_12_17A0(): pass

    label("Function_12_17A0")

    OP_8E(0xFE, 0xFFFF676C, 0x0, 0x184B6, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF8062, 0x0, 0x197BC, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_17A0 end

    def Function_13_17E8(): pass

    label("Function_13_17E8")

    OP_8E(0xFE, 0xFFFF64EC, 0x0, 0x17F16, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF4F34, 0x0, 0x1A25C, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_17E8 end

    def Function_14_1818(): pass

    label("Function_14_1818")

    OP_8E(0xFE, 0xFFFF64EC, 0x0, 0x17F16, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF4B88, 0x0, 0x19DDE, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_1818 end

    def Function_15_1848(): pass

    label("Function_15_1848")

    OP_8E(0xFE, 0xFFFF64EC, 0x0, 0x17F16, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF476E, 0x0, 0x19A3C, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_1848 end

    def Function_16_1878(): pass

    label("Function_16_1878")

    OP_8E(0xFE, 0xFFFF64EC, 0x0, 0x17F16, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF4278, 0x0, 0x198CA, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_1878 end

    def Function_17_18A8(): pass

    label("Function_17_18A8")

    OP_8E(0xFE, 0xFFFF64EC, 0x0, 0x17F16, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF3DAA, 0x0, 0x19866, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_18A8 end

    def Function_18_18D8(): pass

    label("Function_18_18D8")

    OP_8E(0xFE, 0xFFFF64EC, 0x0, 0x17F16, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF3954, 0x0, 0x19802, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_18D8 end

    def Function_19_1908(): pass

    label("Function_19_1908")

    OP_8E(0xFE, 0xFFFF6974, 0x0, 0x17EE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF7E64, 0x0, 0x1A342, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_1908 end

    def Function_20_1938(): pass

    label("Function_20_1938")

    OP_8E(0xFE, 0xFFFF6974, 0x0, 0x17EE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF82D8, 0x0, 0x19F78, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_1938 end

    def Function_21_1968(): pass

    label("Function_21_1968")

    OP_8E(0xFE, 0xFFFF6974, 0x0, 0x17EE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF8814, 0x0, 0x19A96, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_21_1968 end

    def Function_22_1998(): pass

    label("Function_22_1998")

    OP_8E(0xFE, 0xFFFF6974, 0x0, 0x17EE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF8D28, 0x0, 0x19776, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_1998 end

    def Function_23_19C8(): pass

    label("Function_23_19C8")

    OP_8E(0xFE, 0xFFFF6974, 0x0, 0x17EE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF92AA, 0x0, 0x19712, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_19C8 end

    def Function_24_19F8(): pass

    label("Function_24_19F8")

    OP_8E(0xFE, 0xFFFF6974, 0x0, 0x17EE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF975A, 0x0, 0x19776, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_24_19F8 end

    def Function_25_1A28(): pass

    label("Function_25_1A28")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　王都格兰赛尔\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_1A28 end

    def Function_26_1A68(): pass

    label("Function_26_1A68")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　格鲁纳门　　　１６５塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_1A68 end

    def Function_27_1AB8(): pass

    label("Function_27_1AB8")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南　圣海姆门　　　２２８塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_1AB8 end

    SaveToFile()

Try(main)
