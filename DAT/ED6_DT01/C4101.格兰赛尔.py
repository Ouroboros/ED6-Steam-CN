from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4101.x',
        MapIndex            = 1,
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
        '修女艾伦',                             # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '魔兽',                                 # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
        '卡露娜',                               # 20
        '亚妮拉丝',                             # 21
        '库拉茨',                               # 22
        '克鲁茨',                               # 23
        '尤莉亚中尉',                           # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '亲卫队员',                             # 28
        '亲卫队员',                             # 29
        '亲卫队员',                             # 30
        '亲卫队员',                             # 31
        '亲卫队员',                             # 32
        '庭园大道方向',                         # 33
        '艾尔贝离宫方向',                       # 34
        '庭园大道方向',                         # 35
        '凶暴巨鳄3',                            # 36
        '沼泽剑齿吸血魔2',                      # 37
        '贪婪鳄鱼4',                            # 38
        '地狱火爆麻雀3',                        # 39
        '迅猛小鹫3',                            # 40
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT09/CH10780 ._CH',             # 01
        'ED6_DT09/CH10781 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
        'ED6_DT07/CH00171 ._CH',             # 08
        'ED6_DT07/CH01610 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT07/CH00112 ._CH',             # 0B
        'ED6_DT07/CH01240 ._CH',             # 0C
        'ED6_DT07/CH01630 ._CH',             # 0D
        'ED6_DT07/CH01260 ._CH',             # 0E
        'ED6_DT07/CH01620 ._CH',             # 0F
        'ED6_DT07/CH02090 ._CH',             # 10
        'ED6_DT07/CH01320 ._CH',             # 11
        'ED6_DT07/CH00172 ._CH',             # 12
        'ED6_DT09/CH10780 ._CH',             # 13
        'ED6_DT09/CH10781 ._CH',             # 14
        'ED6_DT09/CH10790 ._CH',             # 15
        'ED6_DT09/CH10791 ._CH',             # 16
        'ED6_DT09/CH10050 ._CH',             # 17
        'ED6_DT09/CH10051 ._CH',             # 18
        'ED6_DT09/CH10800 ._CH',             # 19
        'ED6_DT09/CH10801 ._CH',             # 1A
        'ED6_DT09/CH10810 ._CH',             # 1B
        'ED6_DT09/CH10811 ._CH',             # 1C
        'ED6_DT09/CH10820 ._CH',             # 1D
        'ED6_DT09/CH10821 ._CH',             # 1E
        'ED6_DT09/CH11220 ._CH',             # 1F
        'ED6_DT09/CH11221 ._CH',             # 20
        'ED6_DT09/CH11230 ._CH',             # 21
        'ED6_DT09/CH11231 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT09/CH10780P._CP',             # 01
        'ED6_DT09/CH10781P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
        'ED6_DT07/CH00171P._CP',             # 08
        'ED6_DT07/CH01610P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT07/CH00112P._CP',             # 0B
        'ED6_DT07/CH01240P._CP',             # 0C
        'ED6_DT07/CH01630P._CP',             # 0D
        'ED6_DT07/CH01260P._CP',             # 0E
        'ED6_DT07/CH01620P._CP',             # 0F
        'ED6_DT07/CH02090P._CP',             # 10
        'ED6_DT07/CH01320P._CP',             # 11
        'ED6_DT07/CH00172P._CP',             # 12
        'ED6_DT09/CH10780P._CP',             # 13
        'ED6_DT09/CH10781P._CP',             # 14
        'ED6_DT09/CH10790P._CP',             # 15
        'ED6_DT09/CH10791P._CP',             # 16
        'ED6_DT09/CH10050P._CP',             # 17
        'ED6_DT09/CH10051P._CP',             # 18
        'ED6_DT09/CH10800P._CP',             # 19
        'ED6_DT09/CH10801P._CP',             # 1A
        'ED6_DT09/CH10810P._CP',             # 1B
        'ED6_DT09/CH10811P._CP',             # 1C
        'ED6_DT09/CH10820P._CP',             # 1D
        'ED6_DT09/CH10821P._CP',             # 1E
        'ED6_DT09/CH11220P._CP',             # 1F
        'ED6_DT09/CH11221P._CP',             # 20
        'ED6_DT09/CH11230P._CP',             # 21
        'ED6_DT09/CH11231P._CP',             # 22
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62880,
        Z                   = 0,
        Y                   = 55500,
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
        X                   = -25910,
        Z                   = 0,
        Y                   = 25290,
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
        X                   = -107380,
        Z                   = 0,
        Y                   = -10960,
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
        X                   = 54960,
        Z                   = 20,
        Y                   = 1810,
        Unknown_0C          = 0,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x264,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39700,
        Z                   = 70,
        Y                   = -19490,
        Unknown_0C          = 0,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x263,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18160,
        Z                   = 10,
        Y                   = -7650,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x265,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32450,
        Z                   = 20,
        Y                   = -19130,
        Unknown_0C          = 0,
        Unknown_0E          = 31,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x267,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30720,
        Z                   = -20,
        Y                   = -16340,
        Unknown_0C          = 0,
        Unknown_0E          = 33,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x268,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 32110,
        Y                   = -1000,
        Z                   = -45500,
        Range               = 35850,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF84AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -88800,
        Y                   = -1000,
        Z                   = -3040,
        Range               = -85900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFB7EE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 70260,
        Y                   = -1000,
        Z                   = 32570,
        Range               = 56300,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7602,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -18470,
        TriggerZ            = 0,
        TriggerY            = -5070,
        TriggerRange        = 1500,
        ActorX              = -18470,
        ActorZ              = 1700,
        ActorY              = -5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9670,
        TriggerZ            = 500,
        TriggerY            = -54320,
        TriggerRange        = 1500,
        ActorX              = 9670,
        ActorZ              = 4000,
        ActorY              = -54320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_656",          # 00, 0
        "Function_1_673",          # 01, 1
        "Function_2_686",          # 02, 2
        "Function_3_2D1D",         # 03, 3
        "Function_4_3626",         # 04, 4
        "Function_5_38B6",         # 05, 5
        "Function_6_3A31",         # 06, 6
        "Function_7_3BAD",         # 07, 7
        "Function_8_3C4F",         # 08, 8
    )


    def Function_0_656(): pass

    label("Function_0_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_664")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_672")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_672")

    Return()

    # Function_0_656 end

    def Function_1_673(): pass

    label("Function_1_673")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFDDD20, 0x30064)
    Return()

    # Function_1_673 end

    def Function_2_686(): pass

    label("Function_2_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1C")
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14740, 0, -49400, 225)
    SetChrPos(0x9, 12040, 0, -49370, 90)
    SetChrPos(0xA, 12070, 0, -51990, 45)
    SetChrPos(0xB, 14800, 0, -52250, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_6F2():

        label("loc_6F2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6F2")

    QueueWorkItem2(0x9, 1, lambda_6F2)

    def lambda_705():

        label("loc_705")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_705")

    QueueWorkItem2(0xA, 1, lambda_705)

    def lambda_718():

        label("loc_718")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_718")

    QueueWorkItem2(0xB, 1, lambda_718)
    OP_A2(0x616)
    OP_28(0x46, 0x1, 0x20)
    OP_28(0x46, 0x1, 0x40)
    OP_20(0x5DC)

    NpcTalk(
        0x8,
        "女性的声音",
        "……呀啊啊～～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13F, 0)
    TurnDirection(0x102, 0x13F, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)

    ChrTalk(
        0x101,
        "#005F是女人的惨叫！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F在这里面，赶快！\x02",
    )

    CloseMessageWindow()

    def lambda_7EB():
        OP_6D(13190, 0, -50600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EB)

    def lambda_803():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_803)

    def lambda_813():
        OP_6C(241000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_813)
    WaitChrThread(0x101, 0x2)
    AddParty(0x3E, 0xFF)
    ClearChrFlags(0x13F, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x13F, 14740, 0, -49400, 225)
    SetChrPos(0x101, 20850, 0, -44670, 0)
    SetChrPos(0x102, 19400, 0, -43210, 0)
    OP_62(0x13F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(
        0x13F,
        "修女",
        "呀啊啊啊啊啊啊！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13F,
        "修女",
        (
            "救命啊！\x01",
            "谁来救救我啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 2)

    def lambda_8C4():
        OP_92(0xFE, 0x13F, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8C4)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_8E3():
        OP_92(0xFE, 0x13F, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8E3)
    Sleep(100)
    SetChrChipByIndex(0xB, 2)

    def lambda_902():
        OP_92(0xFE, 0x13F, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_902)
    Sleep(500)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)

    def lambda_926():
        OP_8E(0xFE, 0x457E, 0x0, 0xFFFF458E, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_926)
    Sleep(300)

    def lambda_946():
        OP_8E(0xFE, 0x35DE, 0x0, 0xFFFF414C, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_946)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_96B():
        OP_96(0xFE, 0x3B7E, 0x0, 0xFFFF3B8E, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96B)
    Sleep(200)
    OP_44(0x102, 0xFF)
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_9A1():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_9B6():
        OP_96(0xFE, 0x35DE, 0x0, 0xFFFF414C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B6)
    Sleep(200)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 10)

    def lambda_9E3():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E3)
    Sleep(150)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0xB, 1)

    def lambda_A02():

        label("loc_A02")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A02")

    QueueWorkItem2(0xB, 2, lambda_A02)

    def lambda_A15():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A15)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_A3D():
        OP_95(0xFE, 0xFFFFF830, 0x0, 0x0, 0x9C4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A3D)

    def lambda_A5B():

        label("loc_A5B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A5B")

    QueueWorkItem2(0x9, 2, lambda_A5B)
    TurnDirection(0x101, 0xB, 0)
    Sleep(150)
    SetChrChipByIndex(0xA, 1)

    def lambda_A7F():
        OP_95(0xFE, 0xFFFFFD44, 0x0, 0xFFFFFD44, 0x6A4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A7F)

    def lambda_A9D():

        label("loc_A9D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A9D")

    QueueWorkItem2(0xA, 2, lambda_A9D)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x101, 3)

    def lambda_ABA():
        OP_8F(0xFE, 0x38AE, 0x0, 0xFFFF3B16, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABA)
    WaitChrThread(0x102, 0x2)
    SetChrChipByIndex(0x102, 5)

    def lambda_ADF():
        OP_8F(0xFE, 0x35D4, 0x0, 0xFFFF3DF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADF)
    Sleep(150)
    TurnDirection(0x102, 0x9, 0)
    WaitChrThread(0x101, 0x1)

    NpcTalk(
        0x13F,
        "修女",
        "哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F修女小姐，已经没事了！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F很危险！\x01",
            "请快点退到后面去！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0x9, 1)

    def lambda_B79():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B79)
    Sleep(50)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0xA, 1)

    def lambda_B9D():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B9D)
    Sleep(50)
    OP_44(0xB, 0xFF)
    SetChrChipByIndex(0xB, 1)

    def lambda_BC1():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BC1)
    WaitChrThread(0x9, 0x1)

    def lambda_BDC():
        OP_96(0xFE, 0x3994, 0x0, 0xFFFF3F08, 0x7D0, 0xA28)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BDC)
    Sleep(50)

    def lambda_BFF():
        OP_96(0xFE, 0x3994, 0x0, 0xFFFF3F08, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BFF)
    Sleep(50)

    def lambda_C22():
        OP_96(0xFE, 0x3994, 0x0, 0xFFFF3F08, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C22)
    Sleep(500)
    Battle(0x3A3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C58"),
        (SWITCH_DEFAULT, "loc_C5B"),
    )


    label("loc_C58")

    OP_B4(0x0)
    Return()

    label("loc_C5B")

    OP_31(0x7, 0x0, 0x21)
    OP_B5(0x7, 0x0)
    OP_B5(0x7, 0x1)
    OP_B5(0x7, 0x2)
    OP_B5(0x7, 0x3)
    OP_B5(0x7, 0x4)
    OP_B5(0x7, 0x5)
    OP_41(0x7, 0xD4)
    OP_41(0x7, 0xF5)
    OP_41(0x7, 0x113)
    OP_41(0x7, 0x262, 0x0)
    OP_41(0x7, 0x259, 0x1)
    OP_41(0x7, 0x25F, 0x2)
    OP_41(0x7, 0x274, 0x3)
    OP_35(0x7, 0xDC)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDF)
    OP_36(0x7, 0x109)
    OP_36(0x7, 0x10A)
    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 22520, 0, -37100, 0)
    SetChrFlags(0x108, 0x80)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 14390, 0, -50980, 225)
    SetChrPos(0x102, 12920, 0, -49800, 225)
    SetChrPos(0x13F, 14740, 0, -49400, 225)
    OP_6D(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(241000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F呼……\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x13F, 400)

    ChrTalk(
        0x101,
        "#006F修女小姐，你没事吧？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)

    def lambda_DCA():
        TurnDirection(0xFE, 0x13F, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCA)

    NpcTalk(
        0x13F,
        "修女",
        "啊，没事……多亏了你们。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13F,
        "修女",
        "嗯……你们到底是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是游击士协会的人。\x02\x03",
            "在找人的途中听到了你的呼叫声，\x01",
            "所以……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13F,
        "修女",
        "是……这样啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13F,
        "修女",
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F怎、怎么了？\x01",
            "看起来好像很没精神的样子……\x02\x03",
            "难道受伤了？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13F,
        "修女",
        (
            "没有……\x01",
            "多亏了你们，我才平安无事呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13F,
        "修女",
        (
            "我是王都大圣堂的修女，\x01",
            "名叫艾伦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13F,
        "真是太感谢你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，不用谢啦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不过，作为圣职者的女性，\x01",
            "孤身一人来这种地方似乎有点……\x01",
            "　\x02\x03",
            "您没有和其他人一起来吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13F,
        "是的，只有我一个人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13F,
        (
            "其实是因为大圣堂里调药用的\x01",
            "草药没有了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13F,
        (
            "商店里也卖完了，\x01",
            "所以我才来这里采集的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F这也太危险了，\x01",
            "明明到处都是魔兽啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13F,
        (
            "不是的……\x01",
            "以前这里没有这么多魔兽的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13F,
        (
            "好像是从最近\x01",
            "才突然开始增多的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x5DC)
    OP_8C(0x13F, 45, 600)

    ChrTalk(
        0x13F,
        "啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_1D(0x56)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    Sleep(500)

    def lambda_120A():
        OP_8E(0xFE, 0x3CD2, 0x0, 0xFFFF3EB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_120A)
    Sleep(100)

    def lambda_122A():
        OP_8E(0xFE, 0x37C8, 0x0, 0xFFFF4282, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_122A)

    def lambda_1245():
        OP_8F(0xFE, 0x3782, 0x0, 0xFFFF3C24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13F, 3, lambda_1245)
    SetChrPos(0x9, 19840, 0, -40400, 0)
    SetChrPos(0xA, 21100, 0, -41220, 0)
    SetChrPos(0xB, 21440, 0, -39410, 0)
    SetChrPos(0xC, 21420, 0, -38390, 0)
    SetChrPos(0xD, 23130, 0, -39910, 0)
    SetChrPos(0xE, 21460, 0, -36780, 0)
    SetChrPos(0xF, 23510, 0, -37150, 0)
    SetChrPos(0x10, 24560, 0, -39000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    def lambda_1310():
        OP_8E(0xFE, 0x3BB0, 0x0, 0xFFFF4E44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1310)

    def lambda_132B():
        OP_8E(0xFE, 0x43DA, 0x0, 0xFFFF4BA6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_132B)

    def lambda_1346():
        OP_8E(0xFE, 0x40E2, 0x0, 0xFFFF5060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1346)

    def lambda_1361():
        OP_8E(0xFE, 0x3FAC, 0x0, 0xFFFF56B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1361)

    def lambda_137C():
        OP_8E(0xFE, 0x4A1A, 0x0, 0xFFFF5132, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_137C)

    def lambda_1397():
        OP_8E(0xFE, 0x433A, 0x0, 0xFFFF5A74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1397)

    def lambda_13B2():
        OP_8E(0xFE, 0x4AF6, 0x0, 0xFFFF5ACE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13B2)

    def lambda_13CD():
        OP_8E(0xFE, 0x4A74, 0x0, 0xFFFF55F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13CD)

    def lambda_13E8():

        label("loc_13E8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13E8")

    QueueWorkItem2(0x9, 2, lambda_13E8)

    def lambda_13FB():

        label("loc_13FB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13FB")

    QueueWorkItem2(0xA, 2, lambda_13FB)
    Sleep(100)

    def lambda_1413():

        label("loc_1413")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1413")

    QueueWorkItem2(0xB, 2, lambda_1413)

    def lambda_1426():

        label("loc_1426")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1426")

    QueueWorkItem2(0xC, 2, lambda_1426)
    Sleep(100)

    def lambda_143E():

        label("loc_143E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_143E")

    QueueWorkItem2(0xD, 2, lambda_143E)

    def lambda_1451():

        label("loc_1451")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1451")

    QueueWorkItem2(0xE, 2, lambda_1451)
    Sleep(100)

    def lambda_1469():

        label("loc_1469")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1469")

    QueueWorkItem2(0xF, 2, lambda_1469)

    def lambda_147C():

        label("loc_147C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_147C")

    QueueWorkItem2(0x10, 2, lambda_147C)

    def lambda_148F():
        OP_6D(19250, 0, -43570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_148F)

    def lambda_14A7():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A7)
    Sleep(1500)

    def lambda_14BC():
        OP_6D(17110, 0, -45970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BC)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#005F怎么回事啊，这些家伙们……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F好像是因为听到骚动而聚集过来了……\x01",
            "　\x02\x03",
            "有这么多，还真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，以防万一，\x01",
            "至少先让修女小姐逃出去……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x108,
        "男性的声音",
        "#3P哦，看起来你们遇到麻烦了？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)
    SetChrPos(0x108, 23450, 0, -37300, 225)

    def lambda_15E7():
        OP_6D(17970, 0, -45090, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15E7)
    SetChrChipByIndex(0x108, 8)
    SetChrFlags(0x108, 0x1000)

    def lambda_1609():
        OP_8E(0xFE, 0x528A, 0x0, 0xFFFF61B8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1609)
    WaitChrThread(0x108, 0x1)
    Sleep(60)
    SetChrFlags(0x108, 0x20)
    SetChrChipByIndex(0x108, 18)
    SetChrFlags(0x108, 0x20)
    SetChrFlags(0x108, 0x1000)

    def lambda_1642():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1642)
    OP_8E(0x108, 0x4CD6, 0x0, 0xFFFF5C36, 0x2134, 0x0)
    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 19660, 1000, -41900, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_16A5():
        OP_8F(0xFE, 0x43DA, 0x0, 0xFFFF542A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_16A5)

    def lambda_16C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_16C0)
    Sleep(500)
    OP_96(0x108, 0x4F9C, 0x0, 0xFFFF5EDE, 0x1F4, 0x1388)

    def lambda_16EE():
        OP_99(0xFE, 0x4, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_16EE)

    def lambda_16FE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_16FE)

    def lambda_170C():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_170C)

    def lambda_171A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_171A)

    def lambda_1728():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1728)

    def lambda_1736():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1736)
    WaitChrThread(0x108, 0x2)

    ChrTalk(
        0x101,
        "#501F#5P啊，金先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5P太好了……\x01",
            "终于找到您了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，我还以为是谁，\x01",
            "原来是你们两个啊。\x02\x03",
            "总之，有话一会儿再说，\x01",
            "赶快把这些家伙收拾掉吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#5P明白！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)
    SetChrChipByIndex(0x108, 7)

    def lambda_185F():
        OP_8E(0xFE, 0x416E, 0x0, 0xFFFF4868, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_185F)

    def lambda_187A():
        OP_92(0xFE, 0xB, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_187A)

    def lambda_188F():
        OP_8E(0xFE, 0x492A, 0x0, 0xFFFF5952, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 3, lambda_188F)
    Sleep(400)
    Battle(0x3A4, 0x0, 0x0, 0x0, 0xFF)
    RemoveParty(0x3E, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_18C5"),
        (SWITCH_DEFAULT, "loc_18C8"),
    )


    label("loc_18C5")

    OP_B4(0x0)
    Return()

    label("loc_18C8")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 16770, 0, -47500, 45)
    SetChrPos(0x102, 15050, 0, -45990, 45)
    SetChrPos(0x108, 17690, 0, -44440, 225)
    SetChrPos(0x8, 14650, 0, -48360, 45)
    OP_6D(15920, 0, -45970, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x108, 0x1000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x108,
        (
            "#074F哎呀哎呀……\x01",
            "多亏了这些家伙，让我好好地出了一次汗。\x02\x03",
            "#070F不过话说回来，\x01",
            "真没想到能在这里见到你们啊。\x02\x03",
            "你们不是在蔡斯地区工作吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊哈哈～～\x01",
            "确实从那时候起就一直没有像这样见面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P其实我们已经从蔡斯支部\x01",
            "转属到王都格兰赛尔支部来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，是这样啊。\x02\x03",
            "也就是说，\x01",
            "那个绑架事件已经解决了吗。\x02\x03",
            "#071F那个中毒的红发小哥现在还好吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，已经没事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……请问…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F哦，真是失礼了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x108,
        "#072F…………啊……………\x02",
    )

    CloseMessageWindow()

    def lambda_1C0C():

        label("loc_1C0C")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1C0C")

    QueueWorkItem2(0x101, 1, lambda_1C0C)

    def lambda_1C1D():

        label("loc_1C1D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1C1D")

    QueueWorkItem2(0x108, 1, lambda_1C1D)
    OP_8F(0x108, 0x3D72, 0x0, 0xFFFF4DAE, 0xBB8, 0x0)
    OP_44(0x101, 0x1)

    ChrTalk(
        0x108,
        (
            "#070F（喂喂……\x01",
            "　真是个美人啊。）\x02\x03",
            "（是你们的同伴吗？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#014F（不是，\x01",
            "　我们也是刚认识的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#007F真是的，这么色迷迷的，\x01",
            "也不知道什么叫害羞……\x02\x03",
            "#507F小心我去告诉雾香姐哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#073F哎呀……\x01",
            "我只是陈述客观的事实罢了……\x02\x03",
            "#072F喂，我说艾丝蒂尔，\x01",
            "为什么要提到那女人的名字啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3AE8, 0x0, 0xFFFF455C, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "那个……把我从危险的地方救出来，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们都是我的救命恩人。\x02",
    )

    CloseMessageWindow()

    def lambda_1E43():

        label("loc_1E43")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1E43")

    QueueWorkItem2(0x108, 1, lambda_1E43)

    def lambda_1E54():

        label("loc_1E54")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1E54")

    QueueWorkItem2(0x102, 1, lambda_1E54)
    OP_8F(0x108, 0x3DC2, 0x0, 0xFFFF491C, 0xBB8, 0x0)

    ChrTalk(
        0x108,
        (
            "#071F#2P没什么没什么，请别放在心上！\x02\x03",
            "作为男人，就应该贯彻武侠之道嘛！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哎呀……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 600)
    OP_8E(0x101, 0x4182, 0x0, 0xFFFF4B88, 0xFA0, 0x0)
    OP_8E(0x101, 0x3C8C, 0x0, 0xFFFF4ED0, 0xFA0, 0x0)
    TurnDirection(0x101, 0x108, 600)

    ChrTalk(
        0x101,
        (
            "#506F（嘿嘿，好像在装帅呢。）\x02\x03",
            "（金先生其实对女性是没有办法的。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F（哈哈……说得没错。）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 27890, 0, -33290, 0)
    SetChrPos(0x12, 26890, 0, -32290, 0)

    NpcTalk(
        0x11,
        "男人的声音",
        "#3P你们在干什么！？\x02",
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_2002():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2002)

    def lambda_2010():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2010)

    def lambda_201E():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_201E)

    def lambda_202C():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_202C)

    def lambda_203A():
        OP_8E(0xFE, 0x4434, 0x0, 0xFFFF55EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_203A)
    Sleep(200)

    def lambda_205A():
        OP_8E(0xFE, 0x48DA, 0x0, 0xFFFF540C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_205A)
    OP_6D(17010, 0, -44670, 3000)

    def lambda_2086():

        label("loc_2086")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2086")

    QueueWorkItem2(0x108, 2, lambda_2086)

    def lambda_2097():

        label("loc_2097")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2097")

    QueueWorkItem2(0x101, 2, lambda_2097)

    def lambda_20A8():

        label("loc_20A8")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_20A8")

    QueueWorkItem2(0x102, 2, lambda_20A8)

    def lambda_20B9():

        label("loc_20B9")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_20B9")

    QueueWorkItem2(0x8, 2, lambda_20B9)

    ChrTalk(
        0x101,
        "#580F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F……………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(
        0x11,
        (
            "在这种没人的地方密谈，\x01",
            "真是可疑的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P难道……\x01",
            "你们是恐怖分子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x4182, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    ChrTalk(
        0x101,
        (
            "#005F谁、谁是恐怖分子啊！？\x01",
            "我们是——\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x3F2A, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    def lambda_221B():
        OP_8E(0xFE, 0x42FE, 0x0, 0xFFFF49D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_221B)
    OP_8F(0x102, 0x4182, 0x0, 0xFFFF4BF6, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        (
            "#019F……我们是游击士协会\x01",
            "格兰赛尔支部所属的成员。\x02\x03",
            "就在刚才，\x01",
            "我们保护了这位修女免遭魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5P你们是游击士！？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3A84, 0x0, 0xFFFF4B60, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "那个……\x01",
            "他们说的都是真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我来这里采摘草药，\x01",
            "结果被魔兽袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F顺便一说，我也是游击士。\x02\x03",
            "我记得和你们的同僚\x01",
            "在预选赛中曾经碰过面对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "卡尔瓦德的武术家……\x01",
            "那个一个人参赛的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P哼……\x01",
            "身份好像可以确定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "这次就放过你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过，这里离艾尔贝离宫很近。\x01",
            "没事不要在这边乱转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5P还有，修女小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P如果可以的话，\x01",
            "我们把你送回王都去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P有我们在就行了，\x01",
            "不要借助什么游击士的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哎，但、但是我……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#005F可恶，等一下，你们！\x02\x03",
            "真是的……\x01",
            "从刚才就一直在说些过分的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#013F艾丝蒂尔……算了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x11, 400)

    ChrTalk(
        0x102,
        (
            "#010F以后我们一定会注意的。\x01",
            "这次真感谢你们能如此宽大地处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哼，算了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "你们到底只不过是普通市民。\x01",
            "弄清楚自己的本分就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5P那么，修女小姐，我们走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "好、好的……\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0x4042, 0x0, 0xFFFF525E, 0xBB8, 0x0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "那个，各位……\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 51, 400)

    def lambda_27F0():
        OP_6C(20000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27F0)

    def lambda_2800():
        OP_6D(18100, 0, -44370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2800)

    def lambda_2818():
        OP_8F(0xFE, 0x6CF2, 0x0, 0xFFFF7DF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2818)
    OP_8C(0x12, 51, 400)

    def lambda_283A():
        OP_8F(0xFE, 0x6CF2, 0x0, 0xFFFF7DF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_283A)
    Sleep(200)

    def lambda_285A():
        OP_8E(0xFE, 0x6CF2, 0x0, 0xFFFF7DF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_285A)
    Sleep(4000)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(16870, 0, -45560, 1000)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#582F#2P什、什、什……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#2P什么呀！那些家伙！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F他们是王国军情报部所属的\x01",
            "『特务部队』的人吧。\x02\x03",
            "虽然很厉害，\x01",
            "不过都是些很阴险的家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29CA():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29CA)
    Sleep(200)

    def lambda_29DD():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29DD)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F#2P与其说阴险，\x01",
            "倒不如说是品行恶劣呢！\x02\x03",
            "#505F哎……\x02\x03",
            "为什么金先生会知道他们的事情呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，武术大会的预选赛，\x01",
            "他们的队伍也出场了。\x02\x03",
            "那时就是这样介绍的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#580F#2P（那些家伙也有出场……！？）\x02\x03",
            "（平时进行地下活动那些家伙\x01",
            "　这样堂堂正正地被人看到……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#5P（大概是已经没有\x01",
            "　再隐藏自己存在的必要了吧……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F总之，在被他们再次发现之前，\x01",
            "我们还是赶快回城里去吧。\x02\x03",
            "#073F……对了，\x01",
            "你们为什么会在这里的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#2P啊……都忘了重要的事情呢。\x02\x03",
            "#006F其实，我们是来找金先生你的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#073F嗯？找我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#5P其实有件事情想拜托金先生。\x01",
            "　\x02\x03",
            "是有关武术大会的事情……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2D1C")

    Return()

    # Function_2_686 end

    def Function_3_2D1D(): pass

    label("Function_3_2D1D")

    EventBegin(0x0)
    SetChrPos(0x101, 11690, 0, -52560, 225)
    SetChrPos(0x102, 11000, 0, -51680, 225)
    SetChrPos(0x108, 10930, 0, -50240, 196)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x13, 14410, 0, -53900, 257)
    SetChrPos(0x14, 14820, 0, -52280, 244)
    SetChrPos(0x15, 13050, 0, -51640, 207)
    SetChrPos(0x16, 13090, 0, -50260, 213)
    OP_6D(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeToBright(3000, 0)

    def lambda_2DF6():
        OP_6C(249000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DF6)
    OP_6E(309, 5000)

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "这里就是集合点吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在琥耀石的石碑旁的休息场所，\x01",
            "和这里完全符合。\x02\x03",
            "问题是，尤莉亚中尉\x01",
            "他们还没来啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x17, 17080, 0, -45130, 225)
    SetChrPos(0x18, 17100, 0, -43830, 225)
    SetChrPos(0x19, 18380, 0, -45010, 225)
    SetChrPos(0x1A, 17740, 0, -42700, 225)
    SetChrPos(0x1B, 18600, 0, -43670, 225)
    SetChrPos(0x1C, 19480, 0, -44620, 225)
    SetChrPos(0x1D, 18580, 0, -41840, 225)
    SetChrPos(0x1E, 19520, 0, -42690, 225)
    SetChrPos(0x1F, 20400, 0, -43690, 225)

    ChrTalk(
        0x17,
        "……请不用担心。\x02",
    )

    CloseMessageWindow()

    def lambda_2FDB():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FDB)

    def lambda_2FE9():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FE9)

    def lambda_2FF7():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2FF7)

    def lambda_3005():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3005)

    def lambda_3013():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3013)

    def lambda_3021():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3021)

    def lambda_302F():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_302F)

    def lambda_303D():
        OP_6C(335000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_303D)

    def lambda_304D():
        OP_6D(14730, 0, -48030, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_304D)

    def lambda_3065():
        OP_6E(332, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3065)
    Sleep(2000)

    def lambda_307A():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_307A)
    Sleep(100)

    def lambda_309A():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_309A)

    def lambda_30B5():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_30B5)
    Sleep(100)

    def lambda_30D5():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_30D5)

    def lambda_30F0():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_30F0)

    def lambda_310B():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_310B)
    Sleep(100)

    def lambda_312B():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_312B)

    def lambda_3146():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3146)

    def lambda_3161():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3161)
    OP_6D(13880, 0, -49890, 4000)

    ChrTalk(
        0x101,
        "#000F哇，什么时候……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，有这么多人\x01",
            "都能够潜伏在王都啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#170F在支持我们人当中，\x01",
            "市民也是占大多数的。\x02\x03",
            "我们这边已经准备好了，\x01",
            "随时可以开始作战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "好……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 400)

    ChrTalk(
        0x16,
        (
            "艾丝蒂尔，\x01",
            "请发号施令。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_32B5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32B5)

    def lambda_32C3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_32C3)

    def lambda_32D1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_32D1)

    def lambda_32DF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32DF)

    def lambda_32ED():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_32ED)

    def lambda_32FB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_32FB)

    ChrTalk(
        0x101,
        (
            "#000F咦……？\x02\x03",
            "我、我来！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "因为是由你们\x01",
            "接受女王委托的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "啊，由你来发号施令\x01",
            "是理所当然的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F可、可是……\x01",
            "我还只是个新人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "哈哈，没关系。\x01",
            "由你来我们没有异议的哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "只是注意要\x01",
            "大声一点，好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#170F我们是来帮忙的，\x01",
            "绝对不会有半点异议呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，要有自信。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不用再细想了。\x02\x03",
            "这可是老规矩了，老规矩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x02\x03",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_352E():

        label("loc_352E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_352E")

    QueueWorkItem2(0x102, 1, lambda_352E)

    def lambda_353F():

        label("loc_353F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_353F")

    QueueWorkItem2(0x108, 1, lambda_353F)

    def lambda_3550():

        label("loc_3550")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3550")

    QueueWorkItem2(0x13, 1, lambda_3550)

    def lambda_3561():

        label("loc_3561")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3561")

    QueueWorkItem2(0x14, 1, lambda_3561)

    def lambda_3572():

        label("loc_3572")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3572")

    QueueWorkItem2(0x15, 1, lambda_3572)

    def lambda_3583():

        label("loc_3583")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3583")

    QueueWorkItem2(0x16, 1, lambda_3583)

    def lambda_3594():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3594)
    OP_8E(0x101, 0x2972, 0x1E0, 0xFFFF2F40, 0x258, 0x0)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#000F我向全体作战成员宣布……\x02\x03",
            "艾尔贝离宫攻略战，\x01",
            "暨人质解救作战现在开始！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2D1D end

    def Function_4_3626(): pass

    label("Function_4_3626")

    EventBegin(0x0)
    OP_6D(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x18, -25890, 0, -4510, 180)
    SetChrPos(0x19, -27370, 0, -4510, 180)
    SetChrPos(0x1A, -27240, 0, -2700, 180)
    SetChrPos(0x1B, -25950, 0, -2920, 180)
    SetChrPos(0x101, -26570, 0, -6220, 0)
    SetChrPos(0x102, -28030, 0, -6250, 45)
    SetChrPos(0x108, -25360, 0, -6190, 313)

    ChrTalk(
        0x108,
        "#070F好，伏击组开始行动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "我们先行一步，\x01",
            "去引开前庭的残存兵力！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "趁此机会，请你们\x01",
            "突入离宫内部！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，知道了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F愿女神保佑你们！\x02",
    )

    CloseMessageWindow()

    def lambda_37E3():

        label("loc_37E3")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_37E3")

    QueueWorkItem2(0x101, 1, lambda_37E3)

    def lambda_37F4():

        label("loc_37F4")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_37F4")

    QueueWorkItem2(0x102, 1, lambda_37F4)

    def lambda_3805():

        label("loc_3805")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_3805")

    QueueWorkItem2(0x108, 1, lambda_3805)

    def lambda_3816():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3816)
    Sleep(100)

    def lambda_3836():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3836)
    Sleep(200)

    def lambda_3856():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3856)
    Sleep(100)

    def lambda_3876():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3876)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_A2(0x651)
    EventEnd(0x0)
    Return()

    # Function_4_3626 end

    def Function_5_38B6(): pass

    label("Function_5_38B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A30")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392E")

    ChrTalk(
        0x101,
        (
            "#002F……在突击的时刻是不能退缩的。\x01",
            " \x02\x03",
            "立刻赶去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A15")

    label("loc_392E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A0")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F要突击也只有趁现在了……\x02\x03",
            "赶快去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A15")

    label("loc_39A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A15")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(
        0x108,
        (
            "#072F如果现在不行动的话，\x01",
            "就没有突入离宫的机会了。\x02\x03",
            "……赶快去艾尔贝离宫吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A15")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3A30")

    Return()

    # Function_5_38B6 end

    def Function_6_3A31(): pass

    label("Function_6_3A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BAC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA9")

    ChrTalk(
        0x101,
        (
            "#002F……在突击的时刻是不能退缩的。\x01",
            "　\x02\x03",
            "立刻赶去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B91")

    label("loc_3AA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1C")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F要突击也只有趁现在了……\x02\x03",
            "赶快去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B91")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B91")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(
        0x108,
        (
            "#072F如果现在不行动的话，\x01",
            "就没有突入离宫的机会了。\x02\x03",
            "……赶快去艾尔贝离宫吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B91")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3BAC")

    Return()

    # Function_6_3A31 end

    def Function_7_3BAD(): pass

    label("Function_7_3BAD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　艾尔贝离宫\x01",
            "西　圣海姆门　　２２４塞尔矩\x01",
            "东　格鲁纳门　　２５６塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_3BAD end

    def Function_8_3C4F(): pass

    label("Function_8_3C4F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "竖立着古老的琥耀石石碑。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_3C4F end

    SaveToFile()

Try(main)
