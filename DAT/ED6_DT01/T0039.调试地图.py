from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0039   ._SN',
        MapName             = 'map1',
        Location            = 'T0002.x',
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
        'CH01000村民老爷爷',                    # 9
        'CH01010村民老奶奶',                    # 10
        'CH01020村民中年男子',                  # 11
        'CH01030村民中年女子',                  # 12
        'CH01040村民青年男子',                  # 13
        'CH01050村民青年女子',                  # 14
        'CH01060村民男孩',                      # 15
        'CH01070村民女孩',                      # 16
        'CH01080男学生２',                      # 17
        'CH01090女学生２',                      # 18
        'CH01100城市老爷爷',                    # 19
        'CH01110城市老奶奶',                    # 20
        'CH01120城市中年男子',                  # 21
        'CH01130城市中年女子',                  # 22
        'CH01140城市青年男子',                  # 23
        'CH01150城市青年女子',                  # 24
        'CH01160城市男孩',                      # 25
        'CH01170城市女孩',                      # 26
        'CH01180贵族老奶奶',                    # 27
        'CH01190男性学者２',                    # 28
        'CH01200城市绅士１',                    # 29
        'CH01210城市淑女１',                    # 30
        'CH01220城市绅士２',                    # 31
        'CH01230城市淑女２',                    # 32
        'CH01240女游击士',                      # 33
        'CH01250工房工作人员',                  # 34
        'CH01260男游击士',                      # 35
        'CH01270酒保',                          # 36
        'CH01280大厨',                          # 37
        'CH01290前台',                          # 38
        'CH01300王国军士兵',                    # 39
        'CH01310王国军将校',                    # 40
        'CH01320亲卫队',                        # 41
        'CH01330特务兵',                        # 42
        'CH01340帝国军士兵',                    # 43
        'CH01350女佣',                          # 44
        'CH01360男学生',                        # 45
        'CH01370女学生',                        # 46
        'CH01380空贼团手下',                    # 47
        'CH01390市长手下',                      # 48
        'CH01400神父',                          # 49
        'CH01410修女',                          # 50
        'CH01420男性学者',                      # 51
        'CH01430女性学者',                      # 52
        'CH01440定期船长',                      # 53
        'CH01450维修员',                        # 54
        'CH01460乘务员（劳动者）',              # 55
        'CH01470贵族男孩',                      # 56
        'CH01480贵族女孩',                      # 57
        'CH01490贵族老爷爷',                    # 58
        'CH01500矿工',                          # 59
        'CH01510结社战斗兵',                    # 60
        'CH01520见习厨师',                      # 61
        'CH01530中年矿工',                      # 62
        'CH01540女性客房服务员',                # 63
        'CH01550女性维修员',                    # 64
        'CH01560管家',                          # 65
        'CH01570年轻管家',                      # 66
        'CH01580男学生３',                      # 67
        'CH01590女学生３',                      # 68
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = 2000,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT07/CH01003 ._CH',             # 00
        'ED6_DT07/CH01013 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH01033 ._CH',             # 03
        'ED6_DT07/CH01043 ._CH',             # 04
        'ED6_DT07/CH01053 ._CH',             # 05
        'ED6_DT07/CH01063 ._CH',             # 06
        'ED6_DT07/CH01073 ._CH',             # 07
        'ED6_DT07/CH01083 ._CH',             # 08
        'ED6_DT07/CH01093 ._CH',             # 09
        'ED6_DT07/CH01103 ._CH',             # 0A
        'ED6_DT07/CH01113 ._CH',             # 0B
        'ED6_DT07/CH01123 ._CH',             # 0C
        'ED6_DT07/CH01133 ._CH',             # 0D
        'ED6_DT07/CH01143 ._CH',             # 0E
        'ED6_DT07/CH01153 ._CH',             # 0F
        'ED6_DT07/CH01163 ._CH',             # 10
        'ED6_DT07/CH01173 ._CH',             # 11
        'ED6_DT07/CH01183 ._CH',             # 12
        'ED6_DT07/CH01193 ._CH',             # 13
        'ED6_DT07/CH01203 ._CH',             # 14
        'ED6_DT07/CH01213 ._CH',             # 15
        'ED6_DT07/CH01223 ._CH',             # 16
        'ED6_DT07/CH01233 ._CH',             # 17
        'ED6_DT07/CH01243 ._CH',             # 18
        'ED6_DT07/CH01253 ._CH',             # 19
        'ED6_DT07/CH01263 ._CH',             # 1A
        'ED6_DT07/CH01273 ._CH',             # 1B
        'ED6_DT07/CH01283 ._CH',             # 1C
        'ED6_DT07/CH01293 ._CH',             # 1D
        'ED6_DT07/CH01303 ._CH',             # 1E
        'ED6_DT07/CH01313 ._CH',             # 1F
        'ED6_DT07/CH01323 ._CH',             # 20
        'ED6_DT07/CH01333 ._CH',             # 21
        'ED6_DT07/CH01343 ._CH',             # 22
        'ED6_DT07/CH01353 ._CH',             # 23
        'ED6_DT07/CH01363 ._CH',             # 24
        'ED6_DT07/CH01373 ._CH',             # 25
        'ED6_DT07/CH01383 ._CH',             # 26
        'ED6_DT07/CH01393 ._CH',             # 27
        'ED6_DT07/CH01403 ._CH',             # 28
        'ED6_DT07/CH01413 ._CH',             # 29
        'ED6_DT07/CH01423 ._CH',             # 2A
        'ED6_DT07/CH01433 ._CH',             # 2B
        'ED6_DT07/CH01443 ._CH',             # 2C
        'ED6_DT07/CH01453 ._CH',             # 2D
        'ED6_DT07/CH01463 ._CH',             # 2E
        'ED6_DT07/CH01473 ._CH',             # 2F
        'ED6_DT07/CH01483 ._CH',             # 30
        'ED6_DT07/CH01493 ._CH',             # 31
        'ED6_DT07/CH01503 ._CH',             # 32
        'ED6_DT07/CH01513 ._CH',             # 33
        'ED6_DT07/CH01523 ._CH',             # 34
        'ED6_DT07/CH01533 ._CH',             # 35
        'ED6_DT07/CH01543 ._CH',             # 36
        'ED6_DT07/CH01553 ._CH',             # 37
        'ED6_DT07/CH01563 ._CH',             # 38
        'ED6_DT07/CH01573 ._CH',             # 39
        'ED6_DT07/CH01583 ._CH',             # 3A
        'ED6_DT07/CH01593 ._CH',             # 3B
    )

    AddCharChipPat(
        'ED6_DT07/CH01003P._CP',             # 00
        'ED6_DT07/CH01013P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH01033P._CP',             # 03
        'ED6_DT07/CH01043P._CP',             # 04
        'ED6_DT07/CH01053P._CP',             # 05
        'ED6_DT07/CH01063P._CP',             # 06
        'ED6_DT07/CH01073P._CP',             # 07
        'ED6_DT07/CH01083P._CP',             # 08
        'ED6_DT07/CH01093P._CP',             # 09
        'ED6_DT07/CH01103P._CP',             # 0A
        'ED6_DT07/CH01113P._CP',             # 0B
        'ED6_DT07/CH01123P._CP',             # 0C
        'ED6_DT07/CH01133P._CP',             # 0D
        'ED6_DT07/CH01143P._CP',             # 0E
        'ED6_DT07/CH01153P._CP',             # 0F
        'ED6_DT07/CH01163P._CP',             # 10
        'ED6_DT07/CH01173P._CP',             # 11
        'ED6_DT07/CH01183P._CP',             # 12
        'ED6_DT07/CH01193P._CP',             # 13
        'ED6_DT07/CH01203P._CP',             # 14
        'ED6_DT07/CH01213P._CP',             # 15
        'ED6_DT07/CH01223P._CP',             # 16
        'ED6_DT07/CH01233P._CP',             # 17
        'ED6_DT07/CH01243P._CP',             # 18
        'ED6_DT07/CH01253P._CP',             # 19
        'ED6_DT07/CH01263P._CP',             # 1A
        'ED6_DT07/CH01273P._CP',             # 1B
        'ED6_DT07/CH01283P._CP',             # 1C
        'ED6_DT07/CH01293P._CP',             # 1D
        'ED6_DT07/CH01303P._CP',             # 1E
        'ED6_DT07/CH01313P._CP',             # 1F
        'ED6_DT07/CH01323P._CP',             # 20
        'ED6_DT07/CH01333P._CP',             # 21
        'ED6_DT07/CH01343P._CP',             # 22
        'ED6_DT07/CH01353P._CP',             # 23
        'ED6_DT07/CH01363P._CP',             # 24
        'ED6_DT07/CH01373P._CP',             # 25
        'ED6_DT07/CH01383P._CP',             # 26
        'ED6_DT07/CH01393P._CP',             # 27
        'ED6_DT07/CH01403P._CP',             # 28
        'ED6_DT07/CH01413P._CP',             # 29
        'ED6_DT07/CH01423P._CP',             # 2A
        'ED6_DT07/CH01433P._CP',             # 2B
        'ED6_DT07/CH01443P._CP',             # 2C
        'ED6_DT07/CH01453P._CP',             # 2D
        'ED6_DT07/CH01463P._CP',             # 2E
        'ED6_DT07/CH01473P._CP',             # 2F
        'ED6_DT07/CH01483P._CP',             # 30
        'ED6_DT07/CH01493P._CP',             # 31
        'ED6_DT07/CH01503P._CP',             # 32
        'ED6_DT07/CH01513P._CP',             # 33
        'ED6_DT07/CH01523P._CP',             # 34
        'ED6_DT07/CH01533P._CP',             # 35
        'ED6_DT07/CH01543P._CP',             # 36
        'ED6_DT07/CH01553P._CP',             # 37
        'ED6_DT07/CH01563P._CP',             # 38
        'ED6_DT07/CH01573P._CP',             # 39
        'ED6_DT07/CH01583P._CP',             # 3A
        'ED6_DT07/CH01593P._CP',             # 3B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 53,
        ChipIndex           = 0x35,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 40000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 44000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 44000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 56,
        ChipIndex           = 0x38,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 44000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 57,
        ChipIndex           = 0x39,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 44000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 58,
        ChipIndex           = 0x3A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 44000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 59,
        ChipIndex           = 0x3B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_A0A",          # 00, 0
        "Function_1_A16",          # 01, 1
        "Function_2_A17",          # 02, 2
        "Function_3_A2D",          # 03, 3
    )


    def Function_0_A0A(): pass

    label("Function_0_A0A")

    OP_51(0xE, 0x31, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_A0A end

    def Function_1_A16(): pass

    label("Function_1_A16")

    Return()

    # Function_1_A16 end

    def Function_2_A17(): pass

    label("Function_2_A17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2C")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Jump("Function_2_A17")

    label("loc_A2C")

    Return()

    # Function_2_A17 end

    def Function_3_A2D(): pass

    label("Function_3_A2D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "你好。\x02",
    )

    CloseMessageWindow()
    OP_AE(0x5DC)
    TalkEnd(0xFE)
    Return()

    # Function_3_A2D end

    SaveToFile()

Try(main)
