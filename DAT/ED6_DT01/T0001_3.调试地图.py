from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_3 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0001   ._SN',
            'ED6_DT01/T0001_1 ._SN',
            'ED6_DT01/T0001_2 ._SN',
            'ED6_DT01/T0001_3 ._SN',
            'ED6_DT01/T0001_4 ._SN',
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
        "Function_1_2A1",          # 01, 1
        "Function_2_70D",          # 02, 2
        "Function_3_7F7",          # 03, 3
        "Function_4_B8E",          # 04, 4
        "Function_5_FAA",          # 05, 5
        "Function_6_151E",         # 06, 6
        "Function_7_19CE",         # 07, 7
        "Function_8_1E22",         # 08, 8
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪个？\x02",
        )
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_291")

    Menu(
        1,
        10,
        100,
        1,
        (
            "30泛用ＮＰＬ\x01",                                                 # 0
            "31我方队员和专用ＮＰＬ\x01",                                       # 1
            "32泛用ＮＰＬ和专用ＮＰＬ２＿ＡＰＬ\x01",                           # 2
            "33PT战斗艾丝蒂尔、约修亚、金、阿加特、奥利维尔\x01",               # 3
            "34PT战斗约修亚、雪拉、提妲、科洛丝\x01",                           # 4
            "35NPC战斗男女游击士、流氓、空贼\x01",                              # 5
            "36NPC战斗流氓、男女游击士２\x01",                                  # 6
            "37NPC战斗王国士兵、军官、特务兵、洛伦斯、理查德、凯诺娜\x01",      # 7
            "39坐着的角色\x01",                                                 # 8
            "取消\x01",                                                         # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_233"),
        (1, "loc_23C"),
        (2, "loc_245"),
        (3, "loc_24E"),
        (4, "loc_257"),
        (5, "loc_260"),
        (6, "loc_269"),
        (7, "loc_272"),
        (8, "loc_27B"),
        (SWITCH_DEFAULT, "loc_284"),
    )


    label("loc_233")

    NewScene("ED6_DT01/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_23C")

    NewScene("ED6_DT01/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_245")

    NewScene("ED6_DT01/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24E")

    NewScene("ED6_DT01/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_257")

    NewScene("ED6_DT01/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_260")

    NewScene("ED6_DT01/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_269")

    NewScene("ED6_DT01/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_272")

    NewScene("ED6_DT01/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_27B")

    NewScene("ED6_DT01/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_284")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4")

    label("loc_291")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_2A1(): pass

    label("Function_1_2A1")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪个？\x02",
        )
    )


    label("loc_2AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FD")

    Menu(
        1,
        10,
        32,
        1,
        (
            "40魔兽列表(10000-10290)\x01",      # 0
            "41魔兽列表(10300-10590)\x01",      # 1
            "42魔兽列表(10600-10890)\x01",      # 2
            "57魔兽列表(10900-11040)\x01",      # 3
            "60魔兽列表(11050-11190)\x01",      # 4
            "43魔兽动作(10000-10050)\x01",      # 5
            "44魔兽动作(10060-10140)\x01",      # 6
            "45魔兽动作(10150-10210)\x01",      # 7
            "46魔兽动作(10220-10290)\x01",      # 8
            "47魔兽动作(10300-10380)\x01",      # 9
            "48魔兽动作(10390-10450)\x01",      # 10
            "49魔兽动作(10460-10530)\x01",      # 11
            "50魔兽动作(10540-10610)\x01",      # 12
            "51魔兽动作(10620-10690)\x01",      # 13
            "52魔兽动作(10700-10770)\x01",      # 14
            "53魔兽动作(10780-10850)\x01",      # 15
            "54魔兽动作(10860-10900)\x01",      # 16
            "55魔兽动作(10910-10940)\x01",      # 17
            "56魔兽动作(10950-10990)\x01",      # 18
            "58魔兽动作(11000-11060)\x01",      # 19
            "59魔兽动作(11070-11110)\x01",      # 20
            "61魔兽动作(11120-11150)\x01",      # 21
            "62魔兽动作(11160-11190)\x01",      # 22
            "取消\x01",                         # 23
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_62A"),
        (1, "loc_633"),
        (2, "loc_63C"),
        (3, "loc_645"),
        (4, "loc_64E"),
        (5, "loc_657"),
        (6, "loc_660"),
        (7, "loc_669"),
        (8, "loc_672"),
        (9, "loc_67B"),
        (10, "loc_684"),
        (11, "loc_68D"),
        (12, "loc_696"),
        (13, "loc_69F"),
        (14, "loc_6A8"),
        (15, "loc_6B1"),
        (16, "loc_6BA"),
        (17, "loc_6C3"),
        (18, "loc_6CC"),
        (19, "loc_6D5"),
        (20, "loc_6DE"),
        (21, "loc_6E7"),
        (SWITCH_DEFAULT, "loc_6F0"),
    )


    label("loc_62A")

    NewScene("ED6_DT01/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_633")

    NewScene("ED6_DT01/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_63C")

    NewScene("ED6_DT01/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_645")

    NewScene("ED6_DT01/T0057   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_64E")

    NewScene("ED6_DT01/T0060   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_657")

    NewScene("ED6_DT01/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_660")

    NewScene("ED6_DT01/T0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_669")

    NewScene("ED6_DT01/T0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_672")

    NewScene("ED6_DT01/T0046   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_67B")

    NewScene("ED6_DT01/T0047   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_684")

    NewScene("ED6_DT01/T0048   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_68D")

    NewScene("ED6_DT01/T0049   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_696")

    NewScene("ED6_DT01/T0050   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_69F")

    NewScene("ED6_DT01/T0051   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6A8")

    NewScene("ED6_DT01/T0052   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6B1")

    NewScene("ED6_DT01/T0053   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6BA")

    NewScene("ED6_DT01/T0054   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6C3")

    NewScene("ED6_DT01/T0055   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6CC")

    NewScene("ED6_DT01/T0056   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6D5")

    NewScene("ED6_DT01/T0058   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6DE")

    NewScene("ED6_DT01/T0059   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6E7")

    NewScene("ED6_DT01/T0061   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6F0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AB")

    label("loc_6FD")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2A1 end

    def Function_2_70D(): pass

    label("Function_2_70D")


    AnonymousTalk(
        (
            scpstr(0x6),
            "这些是地图。选一个吧。\x02",
        )
    )


    label("loc_723")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E7")

    Menu(
        1,
        10,
        100,
        1,
        (
            "洛连特地区\x01",        # 0
            "柏斯地区\x01",          # 1
            "卢安地区\x01",          # 2
            "蔡斯地区\x01",          # 3
            "格兰赛尔地区\x01",      # 4
            "其它\x01",              # 5
            "取消\x01",              # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7B0"),
        (1, "loc_7B7"),
        (2, "loc_7BE"),
        (3, "loc_7C5"),
        (4, "loc_7CC"),
        (5, "loc_7D3"),
        (SWITCH_DEFAULT, "loc_7DA"),
    )


    label("loc_7B0")

    Call(3, 3)
    Jump("loc_7E4")

    label("loc_7B7")

    Call(3, 4)
    Jump("loc_7E4")

    label("loc_7BE")

    Call(3, 5)
    Jump("loc_7E4")

    label("loc_7C5")

    Call(3, 6)
    Jump("loc_7E4")

    label("loc_7CC")

    Call(3, 7)
    Jump("loc_7E4")

    label("loc_7D3")

    Call(3, 8)
    Jump("loc_7E4")

    label("loc_7DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E4")

    Jump("loc_723")

    label("loc_7E7")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_70D end

    def Function_3_7F7(): pass

    label("Function_3_7F7")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7E")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_854"),
        (1, "loc_963"),
        (2, "loc_AA2"),
        (3, "loc_B28"),
        (SWITCH_DEFAULT, "loc_B71"),
    )


    label("loc_854")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "洛连特\x01",                  # 0
            "市长官邸\x01",                # 1
            "布莱特家\x01",                # 2
            "帕赛尔农场\x01",              # 3
            "帕赛尔农场（夜晚）\x01",      # 4
            "威尔特关所\x01",              # 5
            "飞行场\x01",                  # 6
            "布莱特家\x01",                # 7
            "格鲁纳门\x01",                # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_909"),
        (1, "loc_912"),
        (2, "loc_91B"),
        (3, "loc_924"),
        (4, "loc_92D"),
        (5, "loc_936"),
        (6, "loc_93F"),
        (7, "loc_948"),
        (8, "loc_951"),
        (SWITCH_DEFAULT, "loc_95A"),
    )


    label("loc_909")

    NewScene("ED6_DT01/T0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_912")

    NewScene("ED6_DT01/T0200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_91B")

    NewScene("ED6_DT01/T0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_924")

    NewScene("ED6_DT01/T0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_92D")

    NewScene("ED6_DT01/T0401   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_936")

    NewScene("ED6_DT01/T0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_93F")

    NewScene("ED6_DT01/T0700   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_948")

    NewScene("ED6_DT01/T0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_951")

    NewScene("ED6_DT01/T0600   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_95A")

    OP_5F(0x3)
    Jump("loc_960")

    label("loc_960")

    Jump("loc_B7B")

    label("loc_963")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "玛鲁加矿山\x01",              # 0
            "神秘森林\x01",                # 1
            "翡翠之塔（后半）\x01",        # 2
            "地下水路\x01",                # 3
            "翡翠之塔1F（前半）\x01",      # 4
            "翡翠之塔2F（前半）\x01",      # 5
            "翡翠之塔3F（前半）\x01",      # 6
            "翡翠之塔4F（前半）\x01",      # 7
            "翡翠之塔5F（前半）\x01",      # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A48"),
        (1, "loc_A51"),
        (2, "loc_A5A"),
        (3, "loc_A63"),
        (4, "loc_A6C"),
        (5, "loc_A75"),
        (6, "loc_A7E"),
        (7, "loc_A87"),
        (8, "loc_A90"),
        (SWITCH_DEFAULT, "loc_A99"),
    )


    label("loc_A48")

    NewScene("ED6_DT01/C0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A51")

    NewScene("ED6_DT01/C0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A5A")

    NewScene("ED6_DT01/C0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A63")

    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A6C")

    NewScene("ED6_DT01/C0411   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A75")

    NewScene("ED6_DT01/C0412   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A7E")

    NewScene("ED6_DT01/C0413   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A87")

    NewScene("ED6_DT01/C0414   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A90")

    NewScene("ED6_DT01/C0415   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A99")

    OP_5F(0x3)
    Jump("loc_A9F")

    label("loc_A9F")

    Jump("loc_B7B")

    label("loc_AA2")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "艾利兹街道\x01",      # 0
            "米尔西街道\x01",      # 1
            "玛鲁加山道\x01",      # 2
            "取消\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AFB"),
        (1, "loc_B07"),
        (2, "loc_B13"),
        (SWITCH_DEFAULT, "loc_B1F"),
    )


    label("loc_AFB")

    NewScene("ED6_DT01/R0100   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_B25")

    label("loc_B07")

    NewScene("ED6_DT01/R0200   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_B25")

    label("loc_B13")

    NewScene("ED6_DT01/R0300   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_B25")

    label("loc_B1F")

    OP_5F(0x3)
    Jump("loc_B25")

    label("loc_B25")

    Jump("loc_B7B")

    label("loc_B28")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        "布莱特家·外观\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B5C"),
        (SWITCH_DEFAULT, "loc_B68"),
    )


    label("loc_B5C")

    NewScene("ED6_DT01/T0311   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_B6E")

    label("loc_B68")

    OP_5F(0x3)
    Jump("loc_B6E")

    label("loc_B6E")

    Jump("loc_B7B")

    label("loc_B71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7B")

    Jump("loc_801")

    label("loc_B7E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_7F7 end

    def Function_4_B8E(): pass

    label("Function_4_B8E")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9A")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BEB"),
        (1, "loc_CFC"),
        (2, "loc_E37"),
        (3, "loc_F28"),
        (SWITCH_DEFAULT, "loc_F8A"),
    )


    label("loc_BEB")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "柏斯市南口\x01",              # 0
            "柏斯市民家\x01",              # 1
            "古罗尼关所\x01",              # 2
            "古罗尼关所（夜晚）\x01",      # 3
            "柏斯国际空港\x01",            # 4
            "拉文努村\x01",                # 5
            "哈肯要塞\x01",                # 6
            "湖畔的旅店\x01",              # 7
            "取消\x01",                    # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CAB"),
        (1, "loc_CB4"),
        (2, "loc_CBD"),
        (3, "loc_CC6"),
        (4, "loc_CCF"),
        (5, "loc_CD8"),
        (6, "loc_CE1"),
        (7, "loc_CEA"),
        (SWITCH_DEFAULT, "loc_CF3"),
    )


    label("loc_CAB")

    NewScene("ED6_DT01/T1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CB4")

    NewScene("ED6_DT01/T1110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CBD")

    NewScene("ED6_DT01/T1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CC6")

    NewScene("ED6_DT01/T1301   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CCF")

    NewScene("ED6_DT01/T1102   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CD8")

    NewScene("ED6_DT01/T1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CE1")

    NewScene("ED6_DT01/T1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CEA")

    NewScene("ED6_DT01/T1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CF3")

    OP_5F(0x3)
    Jump("loc_CF9")

    label("loc_CF9")

    Jump("loc_F97")

    label("loc_CFC")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "琥珀之塔（后半）\x01",        # 0
            "迷雾峡谷\x01",                # 1
            "拉文努废坑\x01",              # 2
            "空贼要塞\x01",                # 3
            "琥珀之塔1F（前半）\x01",      # 4
            "琥珀之塔2F（前半）\x01",      # 5
            "琥珀之塔3F（前半）\x01",      # 6
            "琥珀之塔4F（前半）\x01",      # 7
            "琥珀之塔5F（前半）\x01",      # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DDD"),
        (1, "loc_DE6"),
        (2, "loc_DEF"),
        (3, "loc_DF8"),
        (4, "loc_E01"),
        (5, "loc_E0A"),
        (6, "loc_E13"),
        (7, "loc_E1C"),
        (8, "loc_E25"),
        (SWITCH_DEFAULT, "loc_E2E"),
    )


    label("loc_DDD")

    NewScene("ED6_DT01/C1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DE6")

    NewScene("ED6_DT01/C1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DEF")

    NewScene("ED6_DT01/C1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DF8")

    NewScene("ED6_DT01/C1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E01")

    NewScene("ED6_DT01/C1211   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E0A")

    NewScene("ED6_DT01/C1212   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E13")

    NewScene("ED6_DT01/C1213   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E1C")

    NewScene("ED6_DT01/C1214   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E25")

    NewScene("ED6_DT01/C1215   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E2E")

    OP_5F(0x3)
    Jump("loc_E34")

    label("loc_E34")

    Jump("loc_F97")

    label("loc_E37")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "古罗尼山道\x01",            # 0
            "钢壁之路\x01",              # 1
            "东柏斯街道\x01",            # 2
            "西柏斯街道\x01",            # 3
            "安塞尔新街\x01",            # 4
            "安塞尔新街(夜晚)\x01",      # 5
            "拉文努山道\x01",            # 6
            "取消\x01",                  # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE0"),
        (1, "loc_EE9"),
        (2, "loc_EF2"),
        (3, "loc_EFB"),
        (4, "loc_F04"),
        (5, "loc_F0D"),
        (6, "loc_F16"),
        (SWITCH_DEFAULT, "loc_F1F"),
    )


    label("loc_EE0")

    NewScene("ED6_DT01/C1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_EE9")

    NewScene("ED6_DT01/R1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_EF2")

    NewScene("ED6_DT01/R1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_EFB")

    NewScene("ED6_DT01/R1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F04")

    NewScene("ED6_DT01/R1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F0D")

    NewScene("ED6_DT01/R1403   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F16")

    NewScene("ED6_DT01/R1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F1F")

    OP_5F(0x3)
    Jump("loc_F25")

    label("loc_F25")

    Jump("loc_F97")

    label("loc_F28")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "哈肯大门\x01",        # 0
            "古罗尼关所\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F69"),
        (1, "loc_F75"),
        (SWITCH_DEFAULT, "loc_F81"),
    )


    label("loc_F69")

    NewScene("ED6_DT01/T1401   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_F87")

    label("loc_F75")

    NewScene("ED6_DT01/T1311   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_F87")

    label("loc_F81")

    OP_5F(0x3)
    Jump("loc_F87")

    label("loc_F87")

    Jump("loc_F97")

    label("loc_F8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F97")

    label("loc_F97")

    Jump("loc_B98")

    label("loc_F9A")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_B8E end

    def Function_5_FAA(): pass

    label("Function_5_FAA")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150E")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "其它\x01",      # 4
            "取消\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1012"),
        (1, "loc_121A"),
        (2, "loc_1363"),
        (3, "loc_1416"),
        (4, "loc_14A6"),
        (SWITCH_DEFAULT, "loc_14FE"),
    )


    label("loc_1012")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "卢安市\x01",                         # 0
            "飞行场\x01",                         # 1
            "市长官邸\x01",                       # 2
            "王立学院 旧校舍\x01",                # 3
            "王立学院 主楼\x01",                  # 4
            "王立学院 主楼 学园祭\x01",           # 5
            "王立学院 主楼 学园祭准备\x01",       # 6
            "玛西亚孤儿院\x01",                   # 7
            "玛西亚孤儿院（火灾后）\x01",         # 8
            "玛西亚孤儿院（再建后）\x01",         # 9
            "民家\x01",                           # 10
            "店\x01",                             # 11
            "教会\x01",                           # 12
            "酒馆、赌场\x01",                     # 13
            "艾尔·雷登关所\x01",                 # 14
            "玛诺利亚村\x01",                     # 15
            "玛西亚孤儿院内部（火灾中)\x01",      # 16
            "取消\x01",                           # 17
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1178"),
        (1, "loc_1181"),
        (2, "loc_118A"),
        (3, "loc_1193"),
        (4, "loc_119C"),
        (5, "loc_11A5"),
        (6, "loc_11AE"),
        (7, "loc_11B7"),
        (8, "loc_11C0"),
        (9, "loc_11C9"),
        (10, "loc_11D2"),
        (11, "loc_11DB"),
        (12, "loc_11E4"),
        (13, "loc_11ED"),
        (14, "loc_11F6"),
        (15, "loc_11FF"),
        (16, "loc_1208"),
        (SWITCH_DEFAULT, "loc_1211"),
    )


    label("loc_1178")

    NewScene("ED6_DT01/T2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1181")

    NewScene("ED6_DT01/T2102   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_118A")

    NewScene("ED6_DT01/T2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1193")

    NewScene("ED6_DT01/T2600   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_119C")

    NewScene("ED6_DT01/T2510   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11A5")

    NewScene("ED6_DT01/T2520   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11AE")

    NewScene("ED6_DT01/T2530   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11B7")

    NewScene("ED6_DT01/T2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11C0")

    NewScene("ED6_DT01/T2401   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11C9")

    NewScene("ED6_DT01/T2402   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11D2")

    NewScene("ED6_DT01/T2110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11DB")

    NewScene("ED6_DT01/T2120   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11E4")

    NewScene("ED6_DT01/T2130   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11ED")

    NewScene("ED6_DT01/T2131   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11F6")

    NewScene("ED6_DT01/T2700   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11FF")

    NewScene("ED6_DT01/T2300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1208")

    NewScene("ED6_DT01/T2411   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1211")

    OP_5F(0x3)
    Jump("loc_1217")

    label("loc_1217")

    Jump("loc_150B")

    label("loc_121A")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "绀碧之塔（后半）\x01",        # 0
            "巴伦诺灯塔\x01",              # 1
            "巴伦诺灯塔（夜晚）\x01",      # 2
            "旧校舍地下遗迹\x01",          # 3
            "绀碧之塔1F（前半）\x01",      # 4
            "绀碧之塔2F（前半）\x01",      # 5
            "绀碧之塔3F（前半）\x01",      # 6
            "绀碧之塔4F（前半）\x01",      # 7
            "绀碧之塔5F（前半）\x01",      # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1309"),
        (1, "loc_1312"),
        (2, "loc_131B"),
        (3, "loc_1324"),
        (4, "loc_132D"),
        (5, "loc_1336"),
        (6, "loc_133F"),
        (7, "loc_1348"),
        (8, "loc_1351"),
        (SWITCH_DEFAULT, "loc_135A"),
    )


    label("loc_1309")

    NewScene("ED6_DT01/C2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1312")

    NewScene("ED6_DT01/C2209   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_131B")

    NewScene("ED6_DT01/C2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1324")

    NewScene("ED6_DT01/C2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_132D")

    NewScene("ED6_DT01/C2111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1336")

    NewScene("ED6_DT01/C2112   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_133F")

    NewScene("ED6_DT01/C2113   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1348")

    NewScene("ED6_DT01/C2114   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1351")

    NewScene("ED6_DT01/C2115   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_135A")

    OP_5F(0x3)
    Jump("loc_1360")

    label("loc_1360")

    Jump("loc_150B")

    label("loc_1363")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "古罗尼山道\x01",        # 0
            "玛诺利亚间道\x01",      # 1
            "阿伊纳街道\x01",        # 2
            "梅威海道\x01",          # 3
            "街景林道\x01",          # 4
            "取消\x01",              # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13E0"),
        (1, "loc_13E9"),
        (2, "loc_13F2"),
        (3, "loc_13FB"),
        (4, "loc_1404"),
        (SWITCH_DEFAULT, "loc_140D"),
    )


    label("loc_13E0")

    NewScene("ED6_DT01/C1501   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_13E9")

    NewScene("ED6_DT01/R2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_13F2")

    NewScene("ED6_DT01/R2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_13FB")

    NewScene("ED6_DT01/R2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1404")

    NewScene("ED6_DT01/R2300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_140D")

    OP_5F(0x3)
    Jump("loc_1413")

    label("loc_1413")

    Jump("loc_150B")

    label("loc_1416")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "玛诺利亚\x01",          # 0
            "玛诺利亚海岸\x01",      # 1
            "孤儿院\x01",            # 2
            "阿伊纳街道\x01",        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_146D"),
        (1, "loc_1479"),
        (2, "loc_1485"),
        (3, "loc_1491"),
        (SWITCH_DEFAULT, "loc_149D"),
    )


    label("loc_146D")

    NewScene("ED6_DT01/T2301   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A3")

    label("loc_1479")

    NewScene("ED6_DT01/R2111   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A3")

    label("loc_1485")

    NewScene("ED6_DT01/T2403   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A3")

    label("loc_1491")

    NewScene("ED6_DT01/R2412   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A3")

    label("loc_149D")

    OP_5F(0x3)
    Jump("loc_14A3")

    label("loc_14A3")

    Jump("loc_150B")

    label("loc_14A6")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "海卷轴\x01",      # 0
            "海\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14DD"),
        (1, "loc_14E9"),
        (SWITCH_DEFAULT, "loc_14F5"),
    )


    label("loc_14DD")

    NewScene("ED6_DT01/T2103   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FB")

    label("loc_14E9")

    NewScene("ED6_DT01/T2104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FB")

    label("loc_14F5")

    OP_5F(0x3)
    Jump("loc_14FB")

    label("loc_14FB")

    Jump("loc_150B")

    label("loc_14FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_150B")

    label("loc_150B")

    Jump("loc_FB4")

    label("loc_150E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_FAA end

    def Function_6_151E(): pass

    label("Function_6_151E")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_1528")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BE")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_157B"),
        (1, "loc_1706"),
        (2, "loc_18A8"),
        (3, "loc_1954"),
        (SWITCH_DEFAULT, "loc_19AE"),
    )


    label("loc_157B")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "蔡斯市\x01",                    # 0
            "蔡斯市民家１～３室内\x01",      # 1
            "中央工房　室内\x01",            # 2
            "沃尔费堡垒\x01",                # 3
            "蔡斯教会\x01",                  # 4
            "武器店\x01",                    # 5
            "拉赛尔工房\x01",                # 6
            "亚尔摩村外部\x01",              # 7
            "亚尔摩村外部（夜晚）\x01",      # 8
            "圣海姆门\x01",                  # 9
            "蔡斯市(夜晚)\x01",              # 10
            "蔡斯市（停电）\x01",            # 11
            "取消\x01",                      # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1691"),
        (1, "loc_169A"),
        (2, "loc_16A3"),
        (3, "loc_16AC"),
        (4, "loc_16B5"),
        (5, "loc_16BE"),
        (6, "loc_16C7"),
        (7, "loc_16D0"),
        (8, "loc_16D9"),
        (9, "loc_16E2"),
        (10, "loc_16EB"),
        (11, "loc_16F4"),
        (SWITCH_DEFAULT, "loc_16FD"),
    )


    label("loc_1691")

    NewScene("ED6_DT01/T3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_169A")

    NewScene("ED6_DT01/T3110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16A3")

    NewScene("ED6_DT01/T3111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16AC")

    NewScene("ED6_DT01/T3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16B5")

    NewScene("ED6_DT01/T3130   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16BE")

    NewScene("ED6_DT01/T3120   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16C7")

    NewScene("ED6_DT01/T3133   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16D0")

    NewScene("ED6_DT01/T3200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16D9")

    NewScene("ED6_DT01/T3201   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16E2")

    NewScene("ED6_DT01/T3400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16EB")

    NewScene("ED6_DT01/T3103   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16F4")

    NewScene("ED6_DT01/T3106   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16FD")

    OP_5F(0x3)
    Jump("loc_1703")

    label("loc_1703")

    Jump("loc_19BB")

    label("loc_1706")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "红莲之塔（后半）\x01",                # 0
            "雷斯顿水上要塞外\x01",                # 1
            "雷斯顿水上要塞中\x01",                # 2
            "雷斯顿水上要塞外（夜晚)\x01",         # 3
            "卡鲁迪亚大钟乳洞\x01",                # 4
            "卡鲁迪亚大钟乳洞　BOSS房间\x01",      # 5
            "红莲之塔1F（前半）\x01",              # 6
            "红莲之塔2F（前半）\x01",              # 7
            "红莲之塔3F（前半）\x01",              # 8
            "红莲之塔4F（前半）\x01",              # 9
            "红莲之塔5F（前半）\x01",              # 10
            "取消\x01",                            # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_183C"),
        (1, "loc_1845"),
        (2, "loc_184E"),
        (3, "loc_1857"),
        (4, "loc_1860"),
        (5, "loc_1869"),
        (6, "loc_1872"),
        (7, "loc_187B"),
        (8, "loc_1884"),
        (9, "loc_188D"),
        (10, "loc_1896"),
        (SWITCH_DEFAULT, "loc_189F"),
    )


    label("loc_183C")

    NewScene("ED6_DT01/C3500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1845")

    NewScene("ED6_DT01/C3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_184E")

    NewScene("ED6_DT01/C3110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1857")

    NewScene("ED6_DT01/C3104   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1860")

    NewScene("ED6_DT01/C3300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1869")

    NewScene("ED6_DT01/C3303   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1872")

    NewScene("ED6_DT01/C3511   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_187B")

    NewScene("ED6_DT01/C3512   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1884")

    NewScene("ED6_DT01/C3513   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_188D")

    NewScene("ED6_DT01/C3514   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1896")

    NewScene("ED6_DT01/C3515   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_189F")

    OP_5F(0x3)
    Jump("loc_18A5")

    label("loc_18A5")

    Jump("loc_19BB")

    label("loc_18A8")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "佐达特军用道\x01",             # 0
            "卡鲁迪亚隧道（隧道)\x01",      # 1
            "托兰特平原道\x01",             # 2
            "利塔街道\x01",                 # 3
            "取消\x01",                     # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1927"),
        (1, "loc_1930"),
        (2, "loc_1939"),
        (3, "loc_1942"),
        (SWITCH_DEFAULT, "loc_194B"),
    )


    label("loc_1927")

    NewScene("ED6_DT01/R3300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1930")

    NewScene("ED6_DT01/R3400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1939")

    NewScene("ED6_DT01/R3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1942")

    NewScene("ED6_DT01/R3200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_194B")

    OP_5F(0x3)
    Jump("loc_1951")

    label("loc_1951")

    Jump("loc_19BB")

    label("loc_1954")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "蔡斯\x01",          # 0
            "中央工房\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_198D"),
        (1, "loc_1999"),
        (SWITCH_DEFAULT, "loc_19A5"),
    )


    label("loc_198D")

    NewScene("ED6_DT01/T3103   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_19AB")

    label("loc_1999")

    NewScene("ED6_DT01/T3104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_19AB")

    label("loc_19A5")

    OP_5F(0x3)
    Jump("loc_19AB")

    label("loc_19AB")

    Jump("loc_19BB")

    label("loc_19AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19BB")

    label("loc_19BB")

    Jump("loc_1528")

    label("loc_19BE")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_151E end

    def Function_7_19CE(): pass

    label("Function_7_19CE")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_19D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E12")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A2B"),
        (1, "loc_1B08"),
        (2, "loc_1BD5"),
        (3, "loc_1C3C"),
        (SWITCH_DEFAULT, "loc_1E02"),
    )


    label("loc_1A2B")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "格兰赛尔\x01",            # 0
            "格兰赛尔城\x01",          # 1
            "艾尔贝离宫\x01",          # 2
            "旅馆（夜晚）\x01",        # 3
            "大圣堂（夜晚）\x01",      # 4
            "历史资料馆\x01",          # 5
            "竞技场\x01",              # 6
            "取消\x01",                # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AC0"),
        (1, "loc_1AC9"),
        (2, "loc_1AD2"),
        (3, "loc_1ADB"),
        (4, "loc_1AE4"),
        (5, "loc_1AED"),
        (6, "loc_1AF6"),
        (SWITCH_DEFAULT, "loc_1AFF"),
    )


    label("loc_1AC0")

    NewScene("ED6_DT01/T4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AC9")

    NewScene("ED6_DT01/T4200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AD2")

    NewScene("ED6_DT01/T4300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1ADB")

    NewScene("ED6_DT01/T4133   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AE4")

    NewScene("ED6_DT01/T4134   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AED")

    NewScene("ED6_DT01/T4135   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AF6")

    NewScene("ED6_DT01/T4136   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AFF")

    OP_5F(0x3)
    Jump("loc_1B05")

    label("loc_1B05")

    Jump("loc_1E0F")

    label("loc_1B08")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "地下水路Ａ\x01",          # 0
            "地下水路Ｂ\x01",          # 1
            "地下水路Ｃ\x01",          # 2
            "封印区域最上层\x01",      # 3
            "封印区域中层\x01",        # 4
            "封印区域最下层\x01",      # 5
            "取消\x01",                # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B96"),
        (1, "loc_1B9F"),
        (2, "loc_1BA8"),
        (3, "loc_1BB1"),
        (4, "loc_1BBA"),
        (5, "loc_1BC3"),
        (SWITCH_DEFAULT, "loc_1BCC"),
    )


    label("loc_1B96")

    NewScene("ED6_DT01/C4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B9F")

    NewScene("ED6_DT01/C4202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1BA8")

    NewScene("ED6_DT01/C4204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1BB1")

    NewScene("ED6_DT01/C4300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1BBA")

    NewScene("ED6_DT01/C4301   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1BC3")

    NewScene("ED6_DT01/C4302   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1BCC")

    OP_5F(0x3)
    Jump("loc_1BD2")

    label("loc_1BD2")

    Jump("loc_1E0F")

    label("loc_1BD5")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "艾尔贝周游道\x01",      # 0
            "庭园大道\x01",          # 1
            "取消\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C21"),
        (1, "loc_1C2A"),
        (SWITCH_DEFAULT, "loc_1C33"),
    )


    label("loc_1C21")

    NewScene("ED6_DT01/C4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C2A")

    NewScene("ED6_DT01/R4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C33")

    OP_5F(0x3)
    Jump("loc_1C39")

    label("loc_1C39")

    Jump("loc_1E0F")

    label("loc_1C3C")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "艾尔贝周游道 C4111\x01",         # 0
            "艾尔贝周游道 C4113\x01",         # 1
            "艾尔贝离宫 入口庭园\x01",        # 2
            "艾尔贝离宫 中庭、回廊\x01",      # 3
            "艾尔贝离宫 大厅～\x01",          # 4
            "艾尔贝离宫 客室～\x01",          # 5
            "格兰赛尔 南街区\x01",            # 6
            "格兰赛尔 东街区\x01",            # 7
            "格兰赛尔 西街区\x01",            # 8
            "格兰赛尔 北街区\x01",            # 9
            "格兰赛尔城\x01",                 # 10
            "格兰赛尔城 室内\x01",            # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D69"),
        (1, "loc_1D75"),
        (2, "loc_1D81"),
        (3, "loc_1D8D"),
        (4, "loc_1D99"),
        (5, "loc_1DA5"),
        (6, "loc_1DB1"),
        (7, "loc_1DBD"),
        (8, "loc_1DC9"),
        (9, "loc_1DD5"),
        (10, "loc_1DE1"),
        (11, "loc_1DED"),
        (SWITCH_DEFAULT, "loc_1DF9"),
    )


    label("loc_1D69")

    NewScene("ED6_DT01/C4111   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1D75")

    NewScene("ED6_DT01/C4113   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1D81")

    NewScene("ED6_DT01/T4302   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1D8D")

    NewScene("ED6_DT01/T4303   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1D99")

    NewScene("ED6_DT01/T4312   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DA5")

    NewScene("ED6_DT01/T4313   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DB1")

    NewScene("ED6_DT01/T4150   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DBD")

    NewScene("ED6_DT01/T4151   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DC9")

    NewScene("ED6_DT01/T4152   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DD5")

    NewScene("ED6_DT01/T4153   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DE1")

    NewScene("ED6_DT01/T4203   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DED")

    NewScene("ED6_DT01/T4250   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DFF")

    label("loc_1DF9")

    OP_5F(0x3)
    Jump("loc_1DFF")

    label("loc_1DFF")

    Jump("loc_1E0F")

    label("loc_1E02")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E0F")

    label("loc_1E0F")

    Jump("loc_19D8")

    label("loc_1E12")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_19CE end

    def Function_8_1E22(): pass

    label("Function_8_1E22")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_1E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FBC")

    Menu(
        2,
        10,
        100,
        1,
        (
            "船\x01",        # 0
            "天空\x01",      # 1
            "取消\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E73"),
        (1, "loc_1F5D"),
        (SWITCH_DEFAULT, "loc_1FAC"),
    )


    label("loc_1E73")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "定期船\x01",          # 0
            "定期船绿色\x01",      # 1
            "工房船\x01",          # 2
            "空贼艇\x01",          # 3
            "军用两栖舰\x01",      # 4
            "埃尔赛尤外\x01",      # 5
            "特务艇\x01",          # 6
            "空内装置\x01",        # 7
            "取消\x01",            # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F0C"),
        (1, "loc_1F15"),
        (2, "loc_1F1E"),
        (3, "loc_1F27"),
        (4, "loc_1F30"),
        (5, "loc_1F39"),
        (6, "loc_1F42"),
        (7, "loc_1F4B"),
        (SWITCH_DEFAULT, "loc_1F54"),
    )


    label("loc_1F0C")

    NewScene("ED6_DT01/E0000   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F15")

    NewScene("ED6_DT01/E0001   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F1E")

    NewScene("ED6_DT01/E0002   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F27")

    NewScene("ED6_DT01/E0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F30")

    NewScene("ED6_DT01/E0200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F39")

    NewScene("ED6_DT01/E0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F42")

    NewScene("ED6_DT01/E0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F4B")

    NewScene("ED6_DT01/E0111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F54")

    OP_5F(0x3)
    Jump("loc_1F5A")

    label("loc_1F5A")

    Jump("loc_1FB9")

    label("loc_1F5D")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "天空\x01",      # 0
            "取消\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F9A"),
        (SWITCH_DEFAULT, "loc_1FA3"),
    )


    label("loc_1F9A")

    NewScene("ED6_DT01/E0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1FA3")

    OP_5F(0x3)
    Jump("loc_1FA9")

    label("loc_1FA9")

    Jump("loc_1FB9")

    label("loc_1FAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB9")

    label("loc_1FB9")

    Jump("loc_1E2C")

    label("loc_1FBC")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_1E22 end

    SaveToFile()

Try(main)
