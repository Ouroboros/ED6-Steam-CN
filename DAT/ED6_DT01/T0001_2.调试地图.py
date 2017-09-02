from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_2 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_16B",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_35B",          # 03, 3
        "Function_4_45C",          # 04, 4
        "Function_5_549",          # 05, 5
        "Function_6_629",          # 06, 6
        "Function_7_74B",          # 07, 7
        "Function_8_82B",          # 08, 8
        "Function_9_90B",          # 09, 9
        "Function_10_AD6",         # 0A, 10
        "Function_11_BBA",         # 0B, 11
        "Function_12_C9A",         # 0C, 12
        "Function_13_D7A",         # 0D, 13
        "Function_14_E5A",         # 0E, 14
        "Function_15_F3A",         # 0F, 15
        "Function_16_101A",        # 10, 16
        "Function_17_10FA",        # 11, 17
        "Function_18_11DA",        # 12, 18
        "Function_19_12BE",        # 13, 19
        "Function_20_139E",        # 14, 20
        "Function_21_1554",        # 15, 21
        "Function_22_1634",        # 16, 22
        "Function_23_178B",        # 17, 23
        "Function_24_191A",        # 18, 24
        "Function_25_19FA",        # 19, 25
        "Function_26_1ADA",        # 1A, 26
        "Function_27_1BD1",        # 1B, 27
        "Function_28_1D0A",        # 1C, 28
        "Function_29_1DEA",        # 1D, 29
        "Function_30_1F25",        # 1E, 30
        "Function_31_2005",        # 1F, 31
        "Function_32_2176",        # 20, 32
        "Function_33_2256",        # 21, 33
        "Function_34_2336",        # 22, 34
        "Function_35_243B",        # 23, 35
        "Function_36_25F1",        # 24, 36
        "Function_37_26D1",        # 25, 37
        "Function_38_2825",        # 26, 38
        "Function_39_2996",        # 27, 39
        "Function_40_2A76",        # 28, 40
        "Function_41_2B56",        # 29, 41
        "Function_42_2C36",        # 2A, 42
        "Function_43_2D16",        # 2B, 43
        "Function_44_2DF6",        # 2C, 44
        "Function_45_2EF0",        # 2D, 45
        "Function_46_2FDB",        # 2E, 46
        "Function_47_30BB",        # 2F, 47
        "Function_48_3352",        # 30, 48
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    label("loc_BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B")

    Menu(
        1,
        10,
        100,
        1,
        (
            "洛连特\x01",        # 0
            "柏斯\x01",          # 1
            "卢安\x01",          # 2
            "蔡斯\x01",          # 3
            "格兰赛尔\x01",      # 4
            "其它\x01",          # 5
            "取消\x01",          # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_124"),
        (1, "loc_12B"),
        (2, "loc_132"),
        (3, "loc_139"),
        (4, "loc_140"),
        (5, "loc_147"),
        (SWITCH_DEFAULT, "loc_14E"),
    )


    label("loc_124")

    Call(2, 1)
    Jump("loc_158")

    label("loc_12B")

    Call(2, 9)
    Jump("loc_158")

    label("loc_132")

    Call(2, 20)
    Jump("loc_158")

    label("loc_139")

    Call(2, 27)
    Jump("loc_158")

    label("loc_140")

    Call(2, 35)
    Jump("loc_158")

    label("loc_147")

    Call(2, 46)
    Jump("loc_158")

    label("loc_14E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_158")

    Jump("loc_BE")

    label("loc_15B")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_16B(): pass

    label("Function_1_16B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "玛鲁加矿山\x01",              # 0
            "神秘森林\x01",                # 1
            "翡翠之塔\x01",                # 2
            "艾利兹街道\x01",              # 3
            "米尔西街道\x01",              # 4
            "玛鲁加山道\x01",              # 5
            "地下水路\x01",                # 6
            "帕赛尔农场（夜晚）\x01",      # 7
            "威尔特桥关所外部\x01",        # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_249"),
        (1, "loc_250"),
        (2, "loc_257"),
        (3, "loc_25E"),
        (4, "loc_265"),
        (5, "loc_26C"),
        (6, "loc_273"),
        (7, "loc_27A"),
        (8, "loc_28A"),
        (SWITCH_DEFAULT, "loc_29A"),
    )


    label("loc_249")

    Call(2, 2)
    Jump("loc_2A4")

    label("loc_250")

    Call(2, 3)
    Jump("loc_2A4")

    label("loc_257")

    Call(2, 4)
    Jump("loc_2A4")

    label("loc_25E")

    Call(2, 5)
    Jump("loc_2A4")

    label("loc_265")

    Call(2, 6)
    Jump("loc_2A4")

    label("loc_26C")

    Call(2, 7)
    Jump("loc_2A4")

    label("loc_273")

    Call(2, 8)
    Jump("loc_2A4")

    label("loc_27A")

    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A4")

    label("loc_28A")

    Battle(0x3ED, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A4")

    label("loc_29A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A4")

    Jump("Function_1_16B")

    label("loc_2A7")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_16B end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",      # 0
            "C0100_02\x01",      # 1
            "C0100_03\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_310"),
        (1, "loc_320"),
        (2, "loc_330"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_310")

    Battle(0x56, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_34A")

    label("loc_320")

    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_34A")

    label("loc_330")

    Battle(0x58, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_34A")

    label("loc_340")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34A")

    Jump("Function_2_2B5")

    label("loc_34D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_2B5 end

    def Function_3_35B(): pass

    label("Function_3_35B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44E")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",          # 0
            "C0100_02\x01",          # 1
            "C0100_03\x01",          # 2
            "C0100_20\x01",          # 3
            "C0100_11\x01",          # 4
            "BTL_EVENT001\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E1"),
        (1, "loc_3F1"),
        (2, "loc_401"),
        (3, "loc_411"),
        (4, "loc_421"),
        (5, "loc_431"),
        (SWITCH_DEFAULT, "loc_441"),
    )


    label("loc_3E1")

    Battle(0x3E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_44B")

    label("loc_3F1")

    Battle(0x3F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_44B")

    label("loc_401")

    Battle(0x40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_44B")

    label("loc_411")

    Battle(0x51, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_44B")

    label("loc_421")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_44B")

    label("loc_431")

    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_44B")

    label("loc_441")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44B")

    Jump("Function_3_35B")

    label("loc_44E")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_35B end

    def Function_4_45C(): pass

    label("Function_4_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53B")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0400_01\x01",          # 0
            "C0400_02\x01",          # 1
            "C0400_07\x01",          # 2
            "C0400_13\x01",          # 3
            "C0400_10\x01",          # 4
            "BTL_EVENT002\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DE"),
        (1, "loc_4EE"),
        (2, "loc_4FE"),
        (3, "loc_50E"),
        (4, "loc_51E"),
        (SWITCH_DEFAULT, "loc_52E"),
    )


    label("loc_4DE")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_538")

    label("loc_4EE")

    Battle(0x32, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_538")

    label("loc_4FE")

    Battle(0x37, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_538")

    label("loc_50E")

    Battle(0x3D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_538")

    label("loc_51E")

    Battle(0x3A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_538")

    label("loc_52E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_538")

    Jump("Function_4_45C")

    label("loc_53B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_45C end

    def Function_5_549(): pass

    label("Function_5_549")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61B")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0100_02\x01",      # 0
            "R0100_05\x01",      # 1
            "R0100_09\x01",      # 2
            "R0100_11\x01",      # 3
            "R0100_14\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5BE"),
        (1, "loc_5CE"),
        (2, "loc_5DE"),
        (3, "loc_5EE"),
        (4, "loc_5FE"),
        (SWITCH_DEFAULT, "loc_60E"),
    )


    label("loc_5BE")

    Battle(0x15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_618")

    label("loc_5CE")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_618")

    label("loc_5DE")

    Battle(0x1C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_618")

    label("loc_5EE")

    Battle(0x1E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_618")

    label("loc_5FE")

    Battle(0x21, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_618")

    label("loc_60E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_618")

    Jump("Function_5_549")

    label("loc_61B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_549 end

    def Function_6_629(): pass

    label("Function_6_629")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73D")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0200_02\x01",          # 0
            "R0200_06\x01",          # 1
            "R0200_09\x01",          # 2
            "R0200_11\x01",          # 3
            "R0200_17\x01",          # 4
            "BTL_QUEST003\x01",      # 5
            "BTL_QUEST004\x01",      # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C0"),
        (1, "loc_6D0"),
        (2, "loc_6E0"),
        (3, "loc_6F0"),
        (4, "loc_700"),
        (5, "loc_710"),
        (6, "loc_720"),
        (SWITCH_DEFAULT, "loc_730"),
    )


    label("loc_6C0")

    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_6D0")

    Battle(0x7E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_6E0")

    Battle(0x81, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_6F0")

    Battle(0x83, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_700")

    Battle(0x89, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_710")

    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_720")

    Battle(0x3EC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_73A")

    label("loc_730")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73A")

    Jump("Function_6_629")

    label("loc_73D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_629 end

    def Function_7_74B(): pass

    label("Function_7_74B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81D")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0300_02\x01",      # 0
            "R0300_06\x01",      # 1
            "R0300_09\x01",      # 2
            "R0300_12\x01",      # 3
            "R0300_17\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7C0"),
        (1, "loc_7D0"),
        (2, "loc_7E0"),
        (3, "loc_7F0"),
        (4, "loc_800"),
        (SWITCH_DEFAULT, "loc_810"),
    )


    label("loc_7C0")

    Battle(0x65, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_81A")

    label("loc_7D0")

    Battle(0x69, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_81A")

    label("loc_7E0")

    Battle(0x6C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_81A")

    label("loc_7F0")

    Battle(0x6F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_81A")

    label("loc_800")

    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_81A")

    label("loc_810")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81A")

    Jump("Function_7_74B")

    label("loc_81D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_74B end

    def Function_8_82B(): pass

    label("Function_8_82B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FD")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0500_01\x01",      # 0
            "C0500_02\x01",      # 1
            "C0500_03\x01",      # 2
            "C0500_04\x01",      # 3
            "C0500_07\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8A0"),
        (1, "loc_8B0"),
        (2, "loc_8C0"),
        (3, "loc_8D0"),
        (4, "loc_8E0"),
        (SWITCH_DEFAULT, "loc_8F0"),
    )


    label("loc_8A0")

    Battle(0x2A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8FA")

    label("loc_8B0")

    Battle(0x2B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8FA")

    label("loc_8C0")

    Battle(0x2C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8FA")

    label("loc_8D0")

    Battle(0x2D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8FA")

    label("loc_8E0")

    Battle(0x30, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8FA")

    label("loc_8F0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8FA")

    Jump("Function_8_82B")

    label("loc_8FD")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_82B end

    def Function_9_90B(): pass

    label("Function_9_90B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC8")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        60,
        1,
        (
            "琥珀之塔\x01",                        # 0
            "空贼要塞\x01",                        # 1
            "迷雾峡谷\x01",                        # 2
            "古罗尼山顶\x01",                      # 3
            "东柏斯街道\x01",                      # 4
            "西柏斯街道\x01",                      # 5
            "钢壁之路\x01",                        # 6
            "安塞尔新街\x01",                      # 7
            "拉文努山道\x01",                      # 8
            "拉文努废坑\x01",                      # 9
            "拉文努废坑中央广场（吉尔）\x01",      # 10
            "空贼要塞（多伦）\x01",                # 11
            "古罗尼关所外部（犬）\x01",            # 12
            "取消\x01",                            # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A45"),
        (1, "loc_A4C"),
        (2, "loc_A53"),
        (3, "loc_A5A"),
        (4, "loc_A61"),
        (5, "loc_A68"),
        (6, "loc_A6F"),
        (7, "loc_A76"),
        (8, "loc_A7D"),
        (9, "loc_A84"),
        (10, "loc_A8B"),
        (11, "loc_A9B"),
        (12, "loc_AAB"),
        (SWITCH_DEFAULT, "loc_ABB"),
    )


    label("loc_A45")

    Call(2, 10)
    Jump("loc_AC5")

    label("loc_A4C")

    Call(2, 11)
    Jump("loc_AC5")

    label("loc_A53")

    Call(2, 12)
    Jump("loc_AC5")

    label("loc_A5A")

    Call(2, 13)
    Jump("loc_AC5")

    label("loc_A61")

    Call(2, 14)
    Jump("loc_AC5")

    label("loc_A68")

    Call(2, 15)
    Jump("loc_AC5")

    label("loc_A6F")

    Call(2, 16)
    Jump("loc_AC5")

    label("loc_A76")

    Call(2, 17)
    Jump("loc_AC5")

    label("loc_A7D")

    Call(2, 18)
    Jump("loc_AC5")

    label("loc_A84")

    Call(2, 19)
    Jump("loc_AC5")

    label("loc_A8B")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AC5")

    label("loc_A9B")

    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AC5")

    label("loc_AAB")

    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_AC5")

    label("loc_ABB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC5")

    Jump("Function_9_90B")

    label("loc_AC8")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_90B end

    def Function_10_AD6(): pass

    label("Function_10_AD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1211_01\x01",          # 0
            "C1211_02\x01",          # 1
            "C1211_03\x01",          # 2
            "C1211_04\x01",          # 3
            "BTL_QUEST007\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B4F"),
        (1, "loc_B5F"),
        (2, "loc_B6F"),
        (3, "loc_B7F"),
        (4, "loc_B8F"),
        (SWITCH_DEFAULT, "loc_B9F"),
    )


    label("loc_B4F")

    Battle(0x8E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BA9")

    label("loc_B5F")

    Battle(0x8F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BA9")

    label("loc_B6F")

    Battle(0x90, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BA9")

    label("loc_B7F")

    Battle(0x91, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BA9")

    label("loc_B8F")

    Battle(0x3EF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BA9")

    label("loc_B9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BA9")

    Jump("Function_10_AD6")

    label("loc_BAC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_AD6 end

    def Function_11_BBA(): pass

    label("Function_11_BBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1300_01\x01",      # 0
            "C1300_02\x01",      # 1
            "C1300_03\x01",      # 2
            "C1300_04\x01",      # 3
            "C1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C2F"),
        (1, "loc_C3F"),
        (2, "loc_C4F"),
        (3, "loc_C5F"),
        (4, "loc_C6F"),
        (SWITCH_DEFAULT, "loc_C7F"),
    )


    label("loc_C2F")

    Battle(0xA1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C89")

    label("loc_C3F")

    Battle(0xA2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C89")

    label("loc_C4F")

    Battle(0xA3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C89")

    label("loc_C5F")

    Battle(0xA4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C89")

    label("loc_C6F")

    Battle(0xA5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C89")

    label("loc_C7F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C89")

    Jump("Function_11_BBA")

    label("loc_C8C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_BBA end

    def Function_12_C9A(): pass

    label("Function_12_C9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1400_01\x01",      # 0
            "C1400_02\x01",      # 1
            "C1400_03\x01",      # 2
            "C1400_04\x01",      # 3
            "C1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D0F"),
        (1, "loc_D1F"),
        (2, "loc_D2F"),
        (3, "loc_D3F"),
        (4, "loc_D4F"),
        (SWITCH_DEFAULT, "loc_D5F"),
    )


    label("loc_D0F")

    Battle(0xB5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D69")

    label("loc_D1F")

    Battle(0xB6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D69")

    label("loc_D2F")

    Battle(0xB7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D69")

    label("loc_D3F")

    Battle(0xB8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D69")

    label("loc_D4F")

    Battle(0xB9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D69")

    label("loc_D5F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D69")

    Jump("Function_12_C9A")

    label("loc_D6C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_C9A end

    def Function_13_D7A(): pass

    label("Function_13_D7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E4C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1500_01\x01",      # 0
            "C1500_02\x01",      # 1
            "C1500_03\x01",      # 2
            "C1500_04\x01",      # 3
            "C1500_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DEF"),
        (1, "loc_DFF"),
        (2, "loc_E0F"),
        (3, "loc_E1F"),
        (4, "loc_E2F"),
        (SWITCH_DEFAULT, "loc_E3F"),
    )


    label("loc_DEF")

    Battle(0xC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E49")

    label("loc_DFF")

    Battle(0xCA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E49")

    label("loc_E0F")

    Battle(0xCB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E49")

    label("loc_E1F")

    Battle(0xCC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E49")

    label("loc_E2F")

    Battle(0xCD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E49")

    label("loc_E3F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E49")

    Jump("Function_13_D7A")

    label("loc_E4C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_D7A end

    def Function_14_E5A(): pass

    label("Function_14_E5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1100_01\x01",      # 0
            "R1100_02\x01",      # 1
            "R1100_20\x01",      # 2
            "R1100_04\x01",      # 3
            "R1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ECF"),
        (1, "loc_EDF"),
        (2, "loc_EEF"),
        (3, "loc_EFF"),
        (4, "loc_F0F"),
        (SWITCH_DEFAULT, "loc_F1F"),
    )


    label("loc_ECF")

    Battle(0xDD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F29")

    label("loc_EDF")

    Battle(0xDE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F29")

    label("loc_EEF")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F29")

    label("loc_EFF")

    Battle(0xE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F29")

    label("loc_F0F")

    Battle(0xE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F29")

    label("loc_F1F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F29")

    Jump("Function_14_E5A")

    label("loc_F2C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_E5A end

    def Function_15_F3A(): pass

    label("Function_15_F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_100C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1200_01\x01",      # 0
            "R1200_02\x01",      # 1
            "R1200_03\x01",      # 2
            "R1200_04\x01",      # 3
            "R1200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FAF"),
        (1, "loc_FBF"),
        (2, "loc_FCF"),
        (3, "loc_FDF"),
        (4, "loc_FEF"),
        (SWITCH_DEFAULT, "loc_FFF"),
    )


    label("loc_FAF")

    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1009")

    label("loc_FBF")

    Battle(0xF2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1009")

    label("loc_FCF")

    Battle(0xF3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1009")

    label("loc_FDF")

    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1009")

    label("loc_FEF")

    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1009")

    label("loc_FFF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1009")

    Jump("Function_15_F3A")

    label("loc_100C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_F3A end

    def Function_16_101A(): pass

    label("Function_16_101A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10EC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1300_01\x01",      # 0
            "R1300_02\x01",      # 1
            "R1300_03\x01",      # 2
            "R1300_04\x01",      # 3
            "R1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_108F"),
        (1, "loc_109F"),
        (2, "loc_10AF"),
        (3, "loc_10BF"),
        (4, "loc_10CF"),
        (SWITCH_DEFAULT, "loc_10DF"),
    )


    label("loc_108F")

    Battle(0x105, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10E9")

    label("loc_109F")

    Battle(0x106, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10E9")

    label("loc_10AF")

    Battle(0x107, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10E9")

    label("loc_10BF")

    Battle(0x108, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10E9")

    label("loc_10CF")

    Battle(0x109, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10E9")

    label("loc_10DF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E9")

    Jump("Function_16_101A")

    label("loc_10EC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_101A end

    def Function_17_10FA(): pass

    label("Function_17_10FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11CC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1400_01\x01",      # 0
            "R1400_02\x01",      # 1
            "R1400_03\x01",      # 2
            "R1400_04\x01",      # 3
            "R1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_116F"),
        (1, "loc_117F"),
        (2, "loc_118F"),
        (3, "loc_119F"),
        (4, "loc_11AF"),
        (SWITCH_DEFAULT, "loc_11BF"),
    )


    label("loc_116F")

    Battle(0x119, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11C9")

    label("loc_117F")

    Battle(0x11A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11C9")

    label("loc_118F")

    Battle(0x11B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11C9")

    label("loc_119F")

    Battle(0x11C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11C9")

    label("loc_11AF")

    Battle(0x11D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11C9")

    label("loc_11BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11C9")

    Jump("Function_17_10FA")

    label("loc_11CC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_10FA end

    def Function_18_11DA(): pass

    label("Function_18_11DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B0")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1500_01\x01",          # 0
            "R1500_02\x01",          # 1
            "R1500_03\x01",          # 2
            "R1500_04\x01",          # 3
            "BTL_QUEST006\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1253"),
        (1, "loc_1263"),
        (2, "loc_1273"),
        (3, "loc_1283"),
        (4, "loc_1293"),
        (SWITCH_DEFAULT, "loc_12A3"),
    )


    label("loc_1253")

    Battle(0x12D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AD")

    label("loc_1263")

    Battle(0x12E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AD")

    label("loc_1273")

    Battle(0x12F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AD")

    label("loc_1283")

    Battle(0x130, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AD")

    label("loc_1293")

    Battle(0x3EE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AD")

    label("loc_12A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12AD")

    Jump("Function_18_11DA")

    label("loc_12B0")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_11DA end

    def Function_19_12BE(): pass

    label("Function_19_12BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1390")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1100_01\x01",      # 0
            "C1100_02\x01",      # 1
            "C1100_03\x01",      # 2
            "C1100_04\x01",      # 3
            "C1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1333"),
        (1, "loc_1343"),
        (2, "loc_1353"),
        (3, "loc_1363"),
        (4, "loc_1373"),
        (SWITCH_DEFAULT, "loc_1383"),
    )


    label("loc_1333")

    Battle(0x141, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_138D")

    label("loc_1343")

    Battle(0x142, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_138D")

    label("loc_1353")

    Battle(0x143, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_138D")

    label("loc_1363")

    Battle(0x144, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_138D")

    label("loc_1373")

    Battle(0x145, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_138D")

    label("loc_1383")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_138D")

    Jump("Function_19_12BE")

    label("loc_1390")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_12BE end

    def Function_20_139E(): pass

    label("Function_20_139E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1546")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        60,
        1,
        (
            "玛诺利亚间道\x01",                  # 0
            "梅威海道\x01",                      # 1
            "街景林道\x01",                      # 2
            "阿伊纳街道\x01",                    # 3
            "绀碧之塔\x01",                      # 4
            "卢安市长官邸内部（事件）\x01",      # 5
            "巴伦诺灯塔夜晚（事件）\x01",        # 6
            "卢安仓库内部（渡鸦帮）\x01",        # 7
            "旧校舍内部（事件）\x01",            # 8
            "巴伦诺灯塔白天（任务）\x01",        # 9
            "取消\x01",                          # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14CF"),
        (1, "loc_14D6"),
        (2, "loc_14DD"),
        (3, "loc_14E4"),
        (4, "loc_14EB"),
        (5, "loc_14F2"),
        (6, "loc_1502"),
        (7, "loc_1509"),
        (8, "loc_1519"),
        (9, "loc_1529"),
        (SWITCH_DEFAULT, "loc_1539"),
    )


    label("loc_14CF")

    Call(2, 21)
    Jump("loc_1543")

    label("loc_14D6")

    Call(2, 22)
    Jump("loc_1543")

    label("loc_14DD")

    Call(2, 23)
    Jump("loc_1543")

    label("loc_14E4")

    Call(2, 24)
    Jump("loc_1543")

    label("loc_14EB")

    Call(2, 25)
    Jump("loc_1543")

    label("loc_14F2")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1543")

    label("loc_1502")

    Call(2, 26)
    Jump("loc_1543")

    label("loc_1509")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1543")

    label("loc_1519")

    Battle(0x399, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1543")

    label("loc_1529")

    Battle(0x3F2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1543")

    label("loc_1539")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1543")

    Jump("Function_20_139E")

    label("loc_1546")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_139E end

    def Function_21_1554(): pass

    label("Function_21_1554")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1626")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2100_01\x01",      # 0
            "R2100_02\x01",      # 1
            "R2100_03\x01",      # 2
            "R2100_04\x01",      # 3
            "R2100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15C9"),
        (1, "loc_15D9"),
        (2, "loc_15E9"),
        (3, "loc_15F9"),
        (4, "loc_1609"),
        (SWITCH_DEFAULT, "loc_1619"),
    )


    label("loc_15C9")

    Battle(0x169, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1623")

    label("loc_15D9")

    Battle(0x16A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1623")

    label("loc_15E9")

    Battle(0x16B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1623")

    label("loc_15F9")

    Battle(0x16C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1623")

    label("loc_1609")

    Battle(0x16D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1623")

    label("loc_1619")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1623")

    Jump("Function_21_1554")

    label("loc_1626")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_1554 end

    def Function_22_1634(): pass

    label("Function_22_1634")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_177D")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2200_01主要\x01",            # 0
            "R2200_02\x01",                # 1
            "R2201_01沙滩\x01",            # 2
            "R2201_02\x01",                # 3
            "R2202_01主要(傍晚)\x01",      # 4
            "R2202_02\x01",                # 5
            "R2203_01沙滩(傍晚)\x01",      # 6
            "R2203_02\x01",                # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16F0"),
        (1, "loc_1700"),
        (2, "loc_1710"),
        (3, "loc_1720"),
        (4, "loc_1730"),
        (5, "loc_1740"),
        (6, "loc_1750"),
        (7, "loc_1760"),
        (SWITCH_DEFAULT, "loc_1770"),
    )


    label("loc_16F0")

    Battle(0x17D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1700")

    Battle(0x17E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1710")

    Battle(0x187, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1720")

    Battle(0x188, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1730")

    Battle(0x321, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1740")

    Battle(0x322, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1750")

    Battle(0x32B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1760")

    Battle(0x32C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_177A")

    label("loc_1770")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_177A")

    Jump("Function_22_1634")

    label("loc_177D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_1634 end

    def Function_23_178B(): pass

    label("Function_23_178B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_190C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2300_01\x01",            # 0
            "R2300_02\x01",            # 1
            "R2300_03\x01",            # 2
            "R2300_04\x01",            # 3
            "R2300_05\x01",            # 4
            "R2301_01(傍晚)\x01",      # 5
            "R2301_02(傍晚)\x01",      # 6
            "R2301_03(傍晚)\x01",      # 7
            "R2301_04(傍晚)\x01",      # 8
            "R2301_05(傍晚)\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_185F"),
        (1, "loc_186F"),
        (2, "loc_187F"),
        (3, "loc_188F"),
        (4, "loc_189F"),
        (5, "loc_18AF"),
        (6, "loc_18BF"),
        (7, "loc_18CF"),
        (8, "loc_18DF"),
        (9, "loc_18EF"),
        (SWITCH_DEFAULT, "loc_18FF"),
    )


    label("loc_185F")

    Battle(0x191, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_186F")

    Battle(0x192, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_187F")

    Battle(0x193, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_188F")

    Battle(0x194, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_189F")

    Battle(0x195, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_18AF")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_18BF")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_18CF")

    Battle(0x337, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_18DF")

    Battle(0x338, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_18EF")

    Battle(0x339, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1909")

    label("loc_18FF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1909")

    Jump("Function_23_178B")

    label("loc_190C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_178B end

    def Function_24_191A(): pass

    label("Function_24_191A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19EC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2400_01\x01",      # 0
            "R2400_02\x01",      # 1
            "R2400_03\x01",      # 2
            "R2400_04\x01",      # 3
            "R2400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_198F"),
        (1, "loc_199F"),
        (2, "loc_19AF"),
        (3, "loc_19BF"),
        (4, "loc_19CF"),
        (SWITCH_DEFAULT, "loc_19DF"),
    )


    label("loc_198F")

    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19E9")

    label("loc_199F")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19E9")

    label("loc_19AF")

    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19E9")

    label("loc_19BF")

    Battle(0x1A8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19E9")

    label("loc_19CF")

    Battle(0x1A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19E9")

    label("loc_19DF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19E9")

    Jump("Function_24_191A")

    label("loc_19EC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_191A end

    def Function_25_19FA(): pass

    label("Function_25_19FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ACC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C2111_01\x01",      # 0
            "C2111_02\x01",      # 1
            "C2111_03\x01",      # 2
            "C2111_04\x01",      # 3
            "C2111_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A6F"),
        (1, "loc_1A7F"),
        (2, "loc_1A8F"),
        (3, "loc_1A9F"),
        (4, "loc_1AAF"),
        (SWITCH_DEFAULT, "loc_1ABF"),
    )


    label("loc_1A6F")

    Battle(0x1B9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AC9")

    label("loc_1A7F")

    Battle(0x1BA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AC9")

    label("loc_1A8F")

    Battle(0x1BB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AC9")

    label("loc_1A9F")

    Battle(0x1BC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AC9")

    label("loc_1AAF")

    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1AC9")

    label("loc_1ABF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AC9")

    Jump("Function_25_19FA")

    label("loc_1ACC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_19FA end

    def Function_26_1ADA(): pass

    label("Function_26_1ADA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC3")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "BTL_EVENT011(迪恩)\x01",          # 0
            "BTL_EVENT012(雷斯)\x01",          # 1
            "BTL_EVENT013(洛克)\x01",          # 2
            "BTL_EVENT014(黑衣男子)\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B76"),
        (1, "loc_1B86"),
        (2, "loc_1B96"),
        (3, "loc_1BA6"),
        (SWITCH_DEFAULT, "loc_1BB6"),
    )


    label("loc_1B76")

    Battle(0x38F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BC0")

    label("loc_1B86")

    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BC0")

    label("loc_1B96")

    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BC0")

    label("loc_1BA6")

    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BC0")

    label("loc_1BB6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC0")

    Jump("Function_26_1ADA")

    label("loc_1BC3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_1ADA end

    def Function_27_1BD1(): pass

    label("Function_27_1BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "卡鲁迪亚隧道\x01",          # 0
            "卡鲁迪亚大钟乳洞\x01",      # 1
            "红莲之塔\x01",              # 2
            "托兰特平原道\x01",          # 3
            "利塔街道\x01",              # 4
            "佐达特军用道\x01",          # 5
            "雷斯顿水上要塞\x01",        # 6
            "红莲之塔（事件）\x01",      # 7
            "取消\x01",                  # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CAE"),
        (1, "loc_1CB5"),
        (2, "loc_1CBC"),
        (3, "loc_1CC3"),
        (4, "loc_1CCA"),
        (5, "loc_1CD1"),
        (6, "loc_1CD8"),
        (7, "loc_1CDF"),
        (SWITCH_DEFAULT, "loc_1CEF"),
    )


    label("loc_1CAE")

    Call(2, 28)
    Jump("loc_1CF9")

    label("loc_1CB5")

    Call(2, 29)
    Jump("loc_1CF9")

    label("loc_1CBC")

    Call(2, 30)
    Jump("loc_1CF9")

    label("loc_1CC3")

    Call(2, 31)
    Jump("loc_1CF9")

    label("loc_1CCA")

    Call(2, 32)
    Jump("loc_1CF9")

    label("loc_1CD1")

    Call(2, 33)
    Jump("loc_1CF9")

    label("loc_1CD8")

    Call(2, 34)
    Jump("loc_1CF9")

    label("loc_1CDF")

    Battle(0x3A0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CF9")

    label("loc_1CEF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF9")

    Jump("Function_27_1BD1")

    label("loc_1CFC")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_1BD1 end

    def Function_28_1D0A(): pass

    label("Function_28_1D0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DDC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3400_01\x01",      # 0
            "R3400_02\x01",      # 1
            "R3400_03\x01",      # 2
            "R3400_04\x01",      # 3
            "R3400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D7F"),
        (1, "loc_1D8F"),
        (2, "loc_1D9F"),
        (3, "loc_1DAF"),
        (4, "loc_1DBF"),
        (SWITCH_DEFAULT, "loc_1DCF"),
    )


    label("loc_1D7F")

    Battle(0x1CD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD9")

    label("loc_1D8F")

    Battle(0x1CE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD9")

    label("loc_1D9F")

    Battle(0x1CF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD9")

    label("loc_1DAF")

    Battle(0x1D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD9")

    label("loc_1DBF")

    Battle(0x1D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DD9")

    label("loc_1DCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DD9")

    Jump("Function_28_1D0A")

    label("loc_1DDC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_1D0A end

    def Function_29_1DEA(): pass

    label("Function_29_1DEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F17")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3300_01\x01",          # 0
            "C3300_02\x01",          # 1
            "C3300_03\x01",          # 2
            "C3300_04\x01",          # 3
            "C3300_05\x01",          # 4
            "C3300_06\x01",          # 5
            "C3300_07\x01",          # 6
            "BTL_EVENT020\x01",      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E8A"),
        (1, "loc_1E9A"),
        (2, "loc_1EAA"),
        (3, "loc_1EBA"),
        (4, "loc_1ECA"),
        (5, "loc_1EDA"),
        (6, "loc_1EEA"),
        (7, "loc_1EFA"),
        (SWITCH_DEFAULT, "loc_1F0A"),
    )


    label("loc_1E8A")

    Battle(0x1E1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1E9A")

    Battle(0x1E2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1EAA")

    Battle(0x1E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1EBA")

    Battle(0x1E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1ECA")

    Battle(0x1E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1EDA")

    Battle(0x1E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1EEA")

    Battle(0x1E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1EFA")

    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F14")

    label("loc_1F0A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F14")

    Jump("Function_29_1DEA")

    label("loc_1F17")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_1DEA end

    def Function_30_1F25(): pass

    label("Function_30_1F25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF7")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3511_01\x01",      # 0
            "C3511_02\x01",      # 1
            "C3511_03\x01",      # 2
            "C3511_04\x01",      # 3
            "C3511_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F9A"),
        (1, "loc_1FAA"),
        (2, "loc_1FBA"),
        (3, "loc_1FCA"),
        (4, "loc_1FDA"),
        (SWITCH_DEFAULT, "loc_1FEA"),
    )


    label("loc_1F9A")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FF4")

    label("loc_1FAA")

    Battle(0x1F6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FF4")

    label("loc_1FBA")

    Battle(0x1F7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FF4")

    label("loc_1FCA")

    Battle(0x1F8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FF4")

    label("loc_1FDA")

    Battle(0x1F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FF4")

    label("loc_1FEA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FF4")

    Jump("Function_30_1F25")

    label("loc_1FF7")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_1F25 end

    def Function_31_2005(): pass

    label("Function_31_2005")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2168")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3100_01\x01",      # 0
            "R3100_02\x01",      # 1
            "R3100_03\x01",      # 2
            "R3100_04\x01",      # 3
            "R3101_05\x01",      # 4
            "R3101_01\x01",      # 5
            "R3101_02\x01",      # 6
            "R3101_03\x01",      # 7
            "R3101_04\x01",      # 8
            "R3101_05\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20BB"),
        (1, "loc_20CB"),
        (2, "loc_20DB"),
        (3, "loc_20EB"),
        (4, "loc_20FB"),
        (5, "loc_210B"),
        (6, "loc_211B"),
        (7, "loc_212B"),
        (8, "loc_213B"),
        (9, "loc_214B"),
        (SWITCH_DEFAULT, "loc_215B"),
    )


    label("loc_20BB")

    Battle(0x209, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_20CB")

    Battle(0x20A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_20DB")

    Battle(0x20B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_20EB")

    Battle(0x20C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_20FB")

    Battle(0x20D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_210B")

    Battle(0x349, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_211B")

    Battle(0x34A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_212B")

    Battle(0x34B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_213B")

    Battle(0x34C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_214B")

    Battle(0x34D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2165")

    label("loc_215B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2165")

    Jump("Function_31_2005")

    label("loc_2168")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_2005 end

    def Function_32_2176(): pass

    label("Function_32_2176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2248")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3200_01\x01",      # 0
            "R3200_02\x01",      # 1
            "R3200_03\x01",      # 2
            "R3200_04\x01",      # 3
            "R3200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21EB"),
        (1, "loc_21FB"),
        (2, "loc_220B"),
        (3, "loc_221B"),
        (4, "loc_222B"),
        (SWITCH_DEFAULT, "loc_223B"),
    )


    label("loc_21EB")

    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2245")

    label("loc_21FB")

    Battle(0x21E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2245")

    label("loc_220B")

    Battle(0x21F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2245")

    label("loc_221B")

    Battle(0x220, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2245")

    label("loc_222B")

    Battle(0x221, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2245")

    label("loc_223B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2245")

    Jump("Function_32_2176")

    label("loc_2248")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_2176 end

    def Function_33_2256(): pass

    label("Function_33_2256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2328")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300_01\x01",      # 0
            "R3300_02\x01",      # 1
            "R3300_03\x01",      # 2
            "R3300_04\x01",      # 3
            "R3300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22CB"),
        (1, "loc_22DB"),
        (2, "loc_22EB"),
        (3, "loc_22FB"),
        (4, "loc_230B"),
        (SWITCH_DEFAULT, "loc_231B"),
    )


    label("loc_22CB")

    Battle(0x231, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2325")

    label("loc_22DB")

    Battle(0x232, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2325")

    label("loc_22EB")

    Battle(0x233, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2325")

    label("loc_22FB")

    Battle(0x234, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2325")

    label("loc_230B")

    Battle(0x235, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2325")

    label("loc_231B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2325")

    Jump("Function_33_2256")

    label("loc_2328")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_2256 end

    def Function_34_2336(): pass

    label("Function_34_2336")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242D")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3107_01\x01",              # 0
            "C3107_02\x01",              # 1
            "C3107_10\x01",              # 2
            "C3107_11\x01",              # 3
            "C3107_12\x01",              # 4
            "C3107_14特务兵Ｃ\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23C0"),
        (1, "loc_23D0"),
        (2, "loc_23E0"),
        (3, "loc_23F0"),
        (4, "loc_2400"),
        (5, "loc_2410"),
        (SWITCH_DEFAULT, "loc_2420"),
    )


    label("loc_23C0")

    Battle(0x245, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_242A")

    label("loc_23D0")

    Battle(0x246, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_242A")

    label("loc_23E0")

    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_242A")

    label("loc_23F0")

    Battle(0x24F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_242A")

    label("loc_2400")

    Battle(0x250, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_242A")

    label("loc_2410")

    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_242A")

    label("loc_2420")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_242A")

    Jump("Function_34_2336")

    label("loc_242D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_2336 end

    def Function_35_243B(): pass

    label("Function_35_243B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E3")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "艾尔贝周游道\x01",                                  # 0
            "地下水路\x01",                                      # 1
            "封印区域\x01",                                      # 2
            "庭园大道\x01",                                      # 3
            "艾尔贝离宫外部　中庭、回廊（夜晚）\x01",            # 4
            "艾尔贝离宫外部　内部（夜晚）\x01",                  # 5
            "格兰赛尔城内部、中庭、女王宫内\x01",                # 6
            "格兰赛尔城内部、空中庭园\x01",                      # 7
            "封印区域BOSS其它(凯诺娜、理查德、洛伦斯)\x01",      # 8
            "王都格兰赛尔外部（竞技场内部）\x01",                # 9
            "取消\x01",                                          # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2590"),
        (1, "loc_2597"),
        (2, "loc_259E"),
        (3, "loc_25A5"),
        (4, "loc_25AC"),
        (5, "loc_25B3"),
        (6, "loc_25BA"),
        (7, "loc_25C1"),
        (8, "loc_25C8"),
        (9, "loc_25CF"),
        (SWITCH_DEFAULT, "loc_25D6"),
    )


    label("loc_2590")

    Call(2, 36)
    Jump("loc_25E0")

    label("loc_2597")

    Call(2, 37)
    Jump("loc_25E0")

    label("loc_259E")

    Call(2, 38)
    Jump("loc_25E0")

    label("loc_25A5")

    Call(2, 39)
    Jump("loc_25E0")

    label("loc_25AC")

    Call(2, 40)
    Jump("loc_25E0")

    label("loc_25B3")

    Call(2, 41)
    Jump("loc_25E0")

    label("loc_25BA")

    Call(2, 42)
    Jump("loc_25E0")

    label("loc_25C1")

    Call(2, 43)
    Jump("loc_25E0")

    label("loc_25C8")

    Call(2, 44)
    Jump("loc_25E0")

    label("loc_25CF")

    Call(2, 45)
    Jump("loc_25E0")

    label("loc_25D6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25E0")

    Jump("Function_35_243B")

    label("loc_25E3")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_243B end

    def Function_36_25F1(): pass

    label("Function_36_25F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C3")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100_01\x01",      # 0
            "C4100_02\x01",      # 1
            "C4100_03\x01",      # 2
            "C4100_04\x01",      # 3
            "C4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2666"),
        (1, "loc_2676"),
        (2, "loc_2686"),
        (3, "loc_2696"),
        (4, "loc_26A6"),
        (SWITCH_DEFAULT, "loc_26B6"),
    )


    label("loc_2666")

    Battle(0x259, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26C0")

    label("loc_2676")

    Battle(0x25A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26C0")

    label("loc_2686")

    Battle(0x25B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26C0")

    label("loc_2696")

    Battle(0x25C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26C0")

    label("loc_26A6")

    Battle(0x25D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26C0")

    label("loc_26B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26C0")

    Jump("Function_36_25F1")

    label("loc_26C3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_25F1 end

    def Function_37_26D1(): pass

    label("Function_37_26D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2817")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4200_01\x01",      # 0
            "C4200_02\x01",      # 1
            "C4200_03\x01",      # 2
            "C4200_04\x01",      # 3
            "C4200_05\x01",      # 4
            "C4200_06\x01",      # 5
            "C4200_07\x01",      # 6
            "C4200_08\x01",      # 7
            "C4200_09\x01",      # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_277A"),
        (1, "loc_278A"),
        (2, "loc_279A"),
        (3, "loc_27AA"),
        (4, "loc_27BA"),
        (5, "loc_27CA"),
        (6, "loc_27DA"),
        (7, "loc_27EA"),
        (8, "loc_27FA"),
        (SWITCH_DEFAULT, "loc_280A"),
    )


    label("loc_277A")

    Battle(0x26D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_278A")

    Battle(0x26E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_279A")

    Battle(0x26F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_27AA")

    Battle(0x270, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_27BA")

    Battle(0x271, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_27CA")

    Battle(0x272, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_27DA")

    Battle(0x273, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_27EA")

    Battle(0x274, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_27FA")

    Battle(0x275, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2814")

    label("loc_280A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2814")

    Jump("Function_37_26D1")

    label("loc_2817")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_26D1 end

    def Function_38_2825(): pass

    label("Function_38_2825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2988")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4300_01\x01",      # 0
            "C4300_02\x01",      # 1
            "C4300_03\x01",      # 2
            "C4300_04\x01",      # 3
            "C4300_05\x01",      # 4
            "C4300_06\x01",      # 5
            "C4300_07\x01",      # 6
            "C4300_08\x01",      # 7
            "C4300_09\x01",      # 8
            "C4300_10\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28DB"),
        (1, "loc_28EB"),
        (2, "loc_28FB"),
        (3, "loc_290B"),
        (4, "loc_291B"),
        (5, "loc_292B"),
        (6, "loc_293B"),
        (7, "loc_294B"),
        (8, "loc_295B"),
        (9, "loc_296B"),
        (SWITCH_DEFAULT, "loc_297B"),
    )


    label("loc_28DB")

    Battle(0x281, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_28EB")

    Battle(0x282, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_28FB")

    Battle(0x283, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_290B")

    Battle(0x284, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_291B")

    Battle(0x285, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_292B")

    Battle(0x286, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_293B")

    Battle(0x287, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_294B")

    Battle(0x288, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_295B")

    Battle(0x289, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_296B")

    Battle(0x28A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2985")

    label("loc_297B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2985")

    Jump("Function_38_2825")

    label("loc_2988")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_2825 end

    def Function_39_2996(): pass

    label("Function_39_2996")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A68")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_01\x01",      # 0
            "R4100_02\x01",      # 1
            "R4100_03\x01",      # 2
            "R4100_04\x01",      # 3
            "R4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A0B"),
        (1, "loc_2A1B"),
        (2, "loc_2A2B"),
        (3, "loc_2A3B"),
        (4, "loc_2A4B"),
        (SWITCH_DEFAULT, "loc_2A5B"),
    )


    label("loc_2A0B")

    Battle(0x295, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A65")

    label("loc_2A1B")

    Battle(0x296, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A65")

    label("loc_2A2B")

    Battle(0x297, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A65")

    label("loc_2A3B")

    Battle(0x298, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A65")

    label("loc_2A4B")

    Battle(0x299, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A65")

    label("loc_2A5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A65")

    Jump("Function_39_2996")

    label("loc_2A68")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_2996 end

    def Function_40_2A76(): pass

    label("Function_40_2A76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B48")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4301_01\x01",      # 0
            "T4301_02\x01",      # 1
            "T4301_03\x01",      # 2
            "T4301_04\x01",      # 3
            "T4301_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AEB"),
        (1, "loc_2AFB"),
        (2, "loc_2B0B"),
        (3, "loc_2B1B"),
        (4, "loc_2B2B"),
        (SWITCH_DEFAULT, "loc_2B3B"),
    )


    label("loc_2AEB")

    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B45")

    label("loc_2AFB")

    Battle(0x2BE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B45")

    label("loc_2B0B")

    Battle(0x2BF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B45")

    label("loc_2B1B")

    Battle(0x2C0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B45")

    label("loc_2B2B")

    Battle(0x2C1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B45")

    label("loc_2B3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B45")

    Jump("Function_40_2A76")

    label("loc_2B48")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_2A76 end

    def Function_41_2B56(): pass

    label("Function_41_2B56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C28")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4310_01\x01",      # 0
            "T4310_02\x01",      # 1
            "T4310_03\x01",      # 2
            "T4310_04\x01",      # 3
            "T4310_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BCB"),
        (1, "loc_2BDB"),
        (2, "loc_2BEB"),
        (3, "loc_2BFB"),
        (4, "loc_2C0B"),
        (SWITCH_DEFAULT, "loc_2C1B"),
    )


    label("loc_2BCB")

    Battle(0x2D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BDB")

    Battle(0x2D2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BEB")

    Battle(0x2D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2BFB")

    Battle(0x2D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2C0B")

    Battle(0x2D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C25")

    label("loc_2C1B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C25")

    Jump("Function_41_2B56")

    label("loc_2C28")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_2B56 end

    def Function_42_2C36(): pass

    label("Function_42_2C36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D08")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4210_01\x01",      # 0
            "T4210_02\x01",      # 1
            "T4210_03\x01",      # 2
            "T4210_04\x01",      # 3
            "T4210_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CAB"),
        (1, "loc_2CBB"),
        (2, "loc_2CCB"),
        (3, "loc_2CDB"),
        (4, "loc_2CEB"),
        (SWITCH_DEFAULT, "loc_2CFB"),
    )


    label("loc_2CAB")

    Battle(0x2E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D05")

    label("loc_2CBB")

    Battle(0x2E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D05")

    label("loc_2CCB")

    Battle(0x2E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D05")

    label("loc_2CDB")

    Battle(0x2E8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D05")

    label("loc_2CEB")

    Battle(0x2E9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D05")

    label("loc_2CFB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D05")

    Jump("Function_42_2C36")

    label("loc_2D08")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_2C36 end

    def Function_43_2D16(): pass

    label("Function_43_2D16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DE8")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4201_01\x01",      # 0
            "T4201_02\x01",      # 1
            "T4201_03\x01",      # 2
            "T4201_04\x01",      # 3
            "T4201_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D8B"),
        (1, "loc_2D9B"),
        (2, "loc_2DAB"),
        (3, "loc_2DBB"),
        (4, "loc_2DCB"),
        (SWITCH_DEFAULT, "loc_2DDB"),
    )


    label("loc_2D8B")

    Battle(0x2F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DE5")

    label("loc_2D9B")

    Battle(0x2FA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DE5")

    label("loc_2DAB")

    Battle(0x2FB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DE5")

    label("loc_2DBB")

    Battle(0x2FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DE5")

    label("loc_2DCB")

    Battle(0x2FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DE5")

    label("loc_2DDB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DE5")

    Jump("Function_43_2D16")

    label("loc_2DE8")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_43_2D16 end

    def Function_44_2DF6(): pass

    label("Function_44_2DF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE2")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "洛伦斯\x01",                # 0
            "凯诺娜\x01",                # 1
            "理查德\x01",                # 2
            "最终BOSS第一形态\x01",      # 3
            "最终BOSS第二形态\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E7D"),
        (1, "loc_2E8D"),
        (2, "loc_2E9D"),
        (3, "loc_2EAD"),
        (4, "loc_2EC1"),
        (SWITCH_DEFAULT, "loc_2ED5"),
    )


    label("loc_2E7D")

    Battle(0x39A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EDF")

    label("loc_2E8D")

    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EDF")

    label("loc_2E9D")

    Battle(0x39C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EDF")

    label("loc_2EAD")

    Call(2, 48)
    Battle(0x3A1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EDF")

    label("loc_2EC1")

    Call(2, 48)
    Battle(0x3A2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2EDF")

    label("loc_2ED5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EDF")

    Jump("Function_44_2DF6")

    label("loc_2EE2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_2DF6 end

    def Function_45_2EF0(): pass

    label("Function_45_2EF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FCD")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "迪恩、雷斯、洛克、杂鱼\x01",                # 0
            "克鲁茨、库拉茨、卡露娜、亚妮拉丝\x01",      # 1
            "洛伦斯、特务兵、特务兵、特务兵\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F90"),
        (1, "loc_2FA0"),
        (2, "loc_2FB0"),
        (SWITCH_DEFAULT, "loc_2FC0"),
    )


    label("loc_2F90")

    Battle(0x39D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FCA")

    label("loc_2FA0")

    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FCA")

    label("loc_2FB0")

    Battle(0x39F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FCA")

    label("loc_2FC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FCA")

    Jump("Function_45_2EF0")

    label("loc_2FCD")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_45_2EF0 end

    def Function_46_2FDB(): pass

    label("Function_46_2FDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30AD")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_21\x01",      # 0
            "R4100_22\x01",      # 1
            "R4100_23\x01",      # 2
            "R4100_24\x01",      # 3
            "R4100_25\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3050"),
        (1, "loc_3060"),
        (2, "loc_3070"),
        (3, "loc_3080"),
        (4, "loc_3090"),
        (SWITCH_DEFAULT, "loc_30A0"),
    )


    label("loc_3050")

    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30AA")

    label("loc_3060")

    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30AA")

    label("loc_3070")

    Battle(0x2AB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30AA")

    label("loc_3080")

    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30AA")

    label("loc_3090")

    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30AA")

    label("loc_30A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30AA")

    Jump("Function_46_2FDB")

    label("loc_30AD")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_46_2FDB end

    def Function_47_30BB(): pass

    label("Function_47_30BB")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x0, 0x5, 0x0)
    OP_31(0x1, 0x5, 0x0)

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    label("loc_30E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3342")

    Menu(
        1,
        10,
        100,
        1,
        (
            "杂鱼中的杂鱼\x01",        # 0
            "爆种铃兰\x01",            # 1
            "事件战斗、田鼠\x01",      # 2
            "波波＋食人鲨\x01",        # 3
            "有NPC的战斗\x01",         # 4
            "空贼战\x01",              # 5
            "自动战斗１\x01",          # 6
            "竞技场①\x01",            # 7
            "竞技场②\x01",            # 8
            "竞技场③\x01",            # 9
            "竞技场④\x01",            # 10
            "竞技场⑤\x01",            # 11
            "竞技场⑥\x01",            # 12
            "取消\x01",                # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31E0"),
        (1, "loc_31F0"),
        (2, "loc_3200"),
        (3, "loc_3246"),
        (4, "loc_3256"),
        (5, "loc_326C"),
        (6, "loc_327C"),
        (7, "loc_3295"),
        (8, "loc_32AE"),
        (9, "loc_32C7"),
        (10, "loc_32E0"),
        (11, "loc_32F9"),
        (12, "loc_3312"),
        (SWITCH_DEFAULT, "loc_332B"),
    )


    label("loc_31E0")

    Battle(0x7A, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_3335")

    label("loc_31F0")

    Battle(0x18, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_3335")

    label("loc_3200")


    AnonymousTalk(
        "这是事件战斗，请打倒所有的敌人。\x02",
    )

    CloseMessageWindow()
    Battle(0x393, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_3335")

    label("loc_3246")

    Battle(0x38, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3335")

    label("loc_3256")

    AddParty(0xE, 0xFF)
    AddParty(0xF, 0xFF)
    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3335")

    label("loc_326C")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3335")

    label("loc_327C")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB8, 0x100001, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_3295")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB9, 0x100002, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_32AE")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBA, 0x100003, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_32C7")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBB, 0x100004, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_32E0")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBC, 0x100005, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_32F9")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBD, 0x100006, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_3312")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBE, 0x100007, 0x0, 0x200, 0xFF)
    Jump("loc_3335")

    label("loc_332B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3335")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30E3")

    label("loc_3342")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_30BB end

    def Function_48_3352(): pass

    label("Function_48_3352")

    OP_31(0x0, 0x0, 0x27)
    OP_31(0x1, 0x0, 0x27)
    OP_31(0x2, 0x0, 0x27)
    OP_31(0x3, 0x0, 0x27)
    OP_31(0x6, 0x0, 0x27)
    OP_31(0x4, 0x0, 0x27)
    OP_31(0x5, 0x0, 0x27)
    OP_31(0x7, 0x0, 0x27)
    OP_31(0x0, 0x5, 0x64)
    OP_31(0x1, 0x5, 0x64)
    OP_31(0x2, 0x5, 0x64)
    OP_31(0x3, 0x5, 0x64)
    OP_31(0x6, 0x5, 0x64)
    OP_31(0x4, 0x5, 0x64)
    OP_31(0x5, 0x5, 0x64)
    OP_31(0x7, 0x5, 0x64)
    OP_3E(0x1F5, 99)
    OP_3E(0x1F6, 99)
    OP_3E(0x1F7, 99)
    OP_3E(0x1FB, 99)
    OP_3E(0x1FC, 99)
    OP_3E(0x1FD, 10)
    OP_3E(0x1FF, 99)
    OP_3E(0x1FF, 99)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x41)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x5F)
    OP_34(0x1, 0x60)
    OP_34(0x1, 0x69)
    OP_34(0x1, 0x6A)
    OP_34(0x0, 0x1E)
    OP_34(0x0, 0x1F)
    OP_34(0x0, 0x20)
    OP_34(0x0, 0x23)
    OP_34(0x0, 0x25)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x70)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0x77)
    OP_34(0x0, 0x78)
    OP_34(0x2, 0x32)
    OP_34(0x2, 0x33)
    OP_34(0x2, 0x34)
    OP_34(0x2, 0x36)
    OP_34(0x2, 0x37)
    OP_34(0x3, 0x64)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x4B)
    OP_34(0x3, 0x4C)
    OP_34(0x4, 0x6E)
    OP_34(0x4, 0x6F)
    OP_34(0x4, 0x70)
    OP_34(0x4, 0x72)
    OP_34(0x4, 0x73)
    OP_34(0x4, 0x76)
    OP_34(0x4, 0x77)
    OP_34(0x4, 0x78)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0x1F)
    OP_34(0x5, 0x20)
    OP_34(0x6, 0x56)
    OP_34(0x6, 0x57)
    OP_34(0x6, 0x58)
    OP_34(0x6, 0x6E)
    OP_34(0x6, 0x6F)
    OP_34(0x6, 0x76)
    OP_34(0x7, 0xB)
    OP_34(0x7, 0xD)
    OP_34(0x7, 0x10)
    OP_34(0x7, 0x4B)
    OP_34(0x7, 0x4C)
    OP_41(0x0, 0xA)
    OP_41(0x0, 0xFE)
    OP_41(0x0, 0x119)
    OP_41(0x1, 0x29)
    OP_41(0x1, 0xFD)
    OP_41(0x1, 0x11A)
    OP_41(0x2, 0x41)
    OP_41(0x2, 0xFE)
    OP_41(0x2, 0x119)
    OP_41(0x3, 0x62)
    OP_41(0x3, 0xFD)
    OP_41(0x3, 0x11A)
    OP_41(0x4, 0x80)
    OP_41(0x4, 0xFE)
    OP_41(0x4, 0x119)
    OP_41(0x5, 0x9D)
    OP_41(0x5, 0xFD)
    OP_41(0x5, 0x11A)
    OP_41(0x6, 0xBB)
    OP_41(0x6, 0xFE)
    OP_41(0x6, 0x119)
    OP_41(0x7, 0xD9)
    OP_41(0x7, 0xFD)
    OP_41(0x7, 0x11A)
    Return()

    # Function_48_3352 end

    SaveToFile()

Try(main)
