from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择魔兽\x02",
        )
    )


    label("loc_C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试\x01",                      # 0
            "10000 嗜杀巨蟹\x01",            # 1
            "10260 红茶钳虫\x01",            # 2
            "10180 爆种铃兰\x01",            # 3
            "10010 巨型雪猿\x01",            # 4
            "10020 跳跳猫\x01",              # 5
            "10210 火爆麻雀\x01",            # 6
            "10190 岩溶捕猎手\x01",          # 7
            "11050 田鼠经理\x01",            # 8
            "10280 森林之雾\x01",            # 9
            "10230 菠萝怪\x01",              # 10
            "10240 多角铁牛\x01",            # 11
            "10050 剑齿吸血魔ＤＸ\x01",      # 12
            "取消\x01",                      # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22E"),
        (1, "loc_23E"),
        (2, "loc_24E"),
        (3, "loc_25E"),
        (4, "loc_26E"),
        (5, "loc_27E"),
        (6, "loc_28E"),
        (7, "loc_29E"),
        (8, "loc_2AE"),
        (9, "loc_2BE"),
        (10, "loc_2CE"),
        (11, "loc_2DE"),
        (12, "loc_2EE"),
        (SWITCH_DEFAULT, "loc_2FE"),
    )


    label("loc_22E")

    Battle(0x7D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_23E")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_24E")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_25E")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_26E")

    Battle(0x7DD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_27E")

    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_28E")

    Battle(0x6E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_29E")

    Battle(0x3C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_2AE")

    Battle(0x7DF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_2BE")

    Battle(0x42, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_2CE")

    Battle(0x45, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_2DE")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_2EE")

    Battle(0x7D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_308")

    label("loc_2FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_308")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8")

    label("loc_315")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
