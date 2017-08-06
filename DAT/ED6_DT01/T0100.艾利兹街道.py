from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100   ._SN',
        MapName             = 'rolent',
        Location            = 'T0100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0100   ._SN',
            'ED6_DT01/T0100_1 ._SN',
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
        '爱娜',                                 # 9
        '鲁克',                                 # 10
        '帕特',                                 # 11
        '克露莎',                               # 12
        '胡里奥',                               # 13
        '艾娅莉',                               # 14
        '阿鲁姆',                               # 15
        '艾娅莉',                               # 16
        '阿鲁姆',                               # 17
        '尤妮',                                 # 18
        '卡雷尔',                               # 19
        '拉德米拉',                             # 20
        '伊娜',                                 # 21
        '安莉尔',                               # 22
        '安莉尔',                               # 23
        '亚鲁瓦教授',                           # 24
        '奈尔',                                 # 25
        '朵洛希',                               # 26
        '雪拉扎德',                             # 27
        '目标用摄像机',                         # 28
        '鸽子',                                 # 29
        '鸽子',                                 # 30
        '鸽子',                                 # 31
        '鸽子',                                 # 32
        '鸽子',                                 # 33
        '洛连特市长官邸',                       # 34
        '洛连特飞艇坪',                         # 35
        '艾利兹街道方向',                       # 36
        '米尔西街道方向',                       # 37
        '玛鲁加山道方向',                       # 38
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 49000,
        Unknown_04              = 0,
        Unknown_08              = 41000,
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
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH02560 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01170 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH01690 ._CH',             # 09
        'ED6_DT07/CH02050 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT07/CH02070 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01700 ._CH',             # 0E
        'ED6_DT07/CH01700 ._CH',             # 0F
        'ED6_DT07/CH00020 ._CH',             # 10
        'ED6_DT07/CH01153 ._CH',             # 11
        'ED6_DT07/CH01143 ._CH',             # 12
        'ED6_DT07/CH01030 ._CH',             # 13
        'ED6_DT07/CH01033 ._CH',             # 14
        'ED6_DT07/CH01730 ._CH',             # 15
        'ED6_DT07/CH01731 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH02560P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01170P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH01690P._CP',             # 09
        'ED6_DT07/CH02050P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT07/CH02070P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01700P._CP',             # 0E
        'ED6_DT07/CH01700P._CP',             # 0F
        'ED6_DT07/CH00020P._CP',             # 10
        'ED6_DT07/CH01153P._CP',             # 11
        'ED6_DT07/CH01143P._CP',             # 12
        'ED6_DT07/CH01030P._CP',             # 13
        'ED6_DT07/CH01033P._CP',             # 14
        'ED6_DT07/CH01730P._CP',             # 15
        'ED6_DT07/CH01731P._CP',             # 16
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 49900,
        Z                   = 0,
        Y                   = 72100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 46900,
        Z                   = 0,
        Y                   = 74100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 30422,
        Z                   = 0,
        Y                   = 40087,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 51829,
        Z                   = 0,
        Y                   = 35208,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 29979,
        Z                   = 0,
        Y                   = 17921,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 31832,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 36305,
        Z                   = 100,
        Y                   = 46015,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 39160,
        Z                   = 80,
        Y                   = 47020,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x12,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 72160,
        Z                   = 0,
        Y                   = 18851,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 62400,
        Z                   = 250,
        Y                   = 22000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 33500,
        Z                   = 0,
        Y                   = 45800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 39420,
        Z                   = 250,
        Y                   = 51560,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x115,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 38700,
        Z                   = 0,
        Y                   = 50720,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
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
        X                   = 49150,
        Z                   = 0,
        Y                   = 95090,
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
        X                   = 48960,
        Z                   = 0,
        Y                   = 1120,
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
        X                   = 5400,
        Z                   = 0,
        Y                   = 39830,
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
        X                   = 28060,
        Z                   = 0,
        Y                   = 80870,
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


    DeclEvent(
        X                   = 44000,
        Y                   = 0,
        Z                   = 12250,
        Range               = 54000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x2710,
        Unknown_18          = 0x0,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 18000,
        Y                   = 0,
        Z                   = 44000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x9088,
        Unknown_18          = 0x0,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = 25000,
        Y                   = 0,
        Z                   = 72000,
        Range               = 31000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x11364,
        Unknown_18          = 0x0,
        Unknown_1C          = 64,
    )

    DeclEvent(
        X                   = 55000,
        Y                   = -1000,
        Z                   = 57200,
        Range               = 61500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xDB88,
        Unknown_18          = 0x10000,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 42000,
        Y                   = -1000,
        Z                   = 34400,
        Range               = 54000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x8278,
        Unknown_18          = 0x10000,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 60900,
        Y                   = -1000,
        Z                   = 35800,
        Range               = 61900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xAFC8,
        Unknown_18          = 0x10000,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 61850,
        Y                   = -1000,
        Z                   = 30150,
        Range               = 66550,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7DC8,
        Unknown_18          = 0x10000,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 78,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 79,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 80,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 82,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 83,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 84,
    )


    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 45300,
        TriggerRange        = 1700,
        ActorX              = 55000,
        ActorZ              = 2500,
        ActorY              = 45300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45000,
        TriggerZ            = 0,
        TriggerY            = 25400,
        TriggerRange        = 500,
        ActorX              = 45000,
        ActorZ              = 0,
        ActorY              = 25400,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 76980,
        TriggerZ            = 0,
        TriggerY            = 19020,
        TriggerRange        = 800,
        ActorX              = 76980,
        ActorZ              = 0,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44710,
        TriggerZ            = 0,
        TriggerY            = 70740,
        TriggerRange        = 1500,
        ActorX              = 44710,
        ActorZ              = 1800,
        ActorY              = 70740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 75,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45280,
        TriggerZ            = 0,
        TriggerY            = 71310,
        TriggerRange        = 1500,
        ActorX              = 45280,
        ActorZ              = 1800,
        ActorY              = 71310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 76,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_85E",          # 00, 0
        "Function_1_D0B",          # 01, 1
        "Function_2_E60",          # 02, 2
        "Function_3_FDD",          # 03, 3
        "Function_4_1116",         # 04, 4
        "Function_5_124F",         # 05, 5
        "Function_6_1273",         # 06, 6
        "Function_7_12F1",         # 07, 7
        "Function_8_1335",         # 08, 8
        "Function_9_1380",         # 09, 9
        "Function_10_13B0",        # 0A, 10
        "Function_11_15B3",        # 0B, 11
        "Function_12_16AB",        # 0C, 12
        "Function_13_1D47",        # 0D, 13
        "Function_14_205B",        # 0E, 14
        "Function_15_3813",        # 0F, 15
        "Function_16_3DB7",        # 10, 16
        "Function_17_3F91",        # 11, 17
        "Function_18_41BF",        # 12, 18
        "Function_19_4424",        # 13, 19
        "Function_20_47F3",        # 14, 20
        "Function_21_4D98",        # 15, 21
        "Function_22_5300",        # 16, 22
        "Function_23_530F",        # 17, 23
        "Function_24_531E",        # 18, 24
        "Function_25_532D",        # 19, 25
        "Function_26_5357",        # 1A, 26
        "Function_27_5703",        # 1B, 27
        "Function_28_60C2",        # 1C, 28
        "Function_29_678A",        # 1D, 29
        "Function_30_67AB",        # 1E, 30
        "Function_31_67D5",        # 1F, 31
        "Function_32_67DF",        # 20, 32
        "Function_33_67E9",        # 21, 33
        "Function_34_6A4B",        # 22, 34
        "Function_35_6A6B",        # 23, 35
        "Function_36_6A8B",        # 24, 36
        "Function_37_6A92",        # 25, 37
        "Function_38_7288",        # 26, 38
        "Function_39_72EA",        # 27, 39
        "Function_40_733A",        # 28, 40
        "Function_41_7422",        # 29, 41
        "Function_42_74D8",        # 2A, 42
        "Function_43_74F0",        # 2B, 43
        "Function_44_7584",        # 2C, 44
        "Function_45_7BAA",        # 2D, 45
        "Function_46_7BE9",        # 2E, 46
        "Function_47_7C28",        # 2F, 47
        "Function_48_7C75",        # 30, 48
        "Function_49_7C7C",        # 31, 49
        "Function_50_7D1D",        # 32, 50
        "Function_51_7DC9",        # 33, 51
        "Function_52_7E69",        # 34, 52
        "Function_53_7EF5",        # 35, 53
        "Function_54_7FA1",        # 36, 54
        "Function_55_814D",        # 37, 55
        "Function_56_81E9",        # 38, 56
        "Function_57_8489",        # 39, 57
        "Function_58_856C",        # 3A, 58
        "Function_59_8651",        # 3B, 59
        "Function_60_8745",        # 3C, 60
        "Function_61_8815",        # 3D, 61
        "Function_62_88A1",        # 3E, 62
        "Function_63_894D",        # 3F, 63
        "Function_64_8AF5",        # 40, 64
        "Function_65_8B7A",        # 41, 65
        "Function_66_8D80",        # 42, 66
        "Function_67_8E50",        # 43, 67
        "Function_68_8F35",        # 44, 68
        "Function_69_9028",        # 45, 69
        "Function_70_90AD",        # 46, 70
        "Function_71_9259",        # 47, 71
        "Function_72_95A7",        # 48, 72
        "Function_73_9C7C",        # 49, 73
        "Function_74_9C98",        # 4A, 74
        "Function_75_9CE6",        # 4B, 75
        "Function_76_9D2F",        # 4C, 76
        "Function_77_9D72",        # 4D, 77
        "Function_78_9D76",        # 4E, 78
        "Function_79_9D7A",        # 4F, 79
        "Function_80_9D7E",        # 50, 80
        "Function_81_9D82",        # 51, 81
        "Function_82_9D86",        # 52, 82
        "Function_83_9D8A",        # 53, 83
        "Function_84_9D8E",        # 54, 84
        "Function_85_9D92",        # 55, 85
        "Function_86_9D96",        # 56, 86
        "Function_87_9D9A",        # 57, 87
        "Function_88_9D9E",        # 58, 88
        "Function_89_9DA2",        # 59, 89
    )


    def Function_0_85E(): pass

    label("Function_0_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_886")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_8DA")

    label("loc_886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8AE")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    Jump("loc_8DA")

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8DA")
    SetChrPos(0xD, 32000, 0, 21020, 0)
    SetChrPos(0xE, 31990, 0, 22540, 180)
    Jump("loc_8DA")

    label("loc_8DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x9, 48900, 0, 48800, 0)
    Jump("loc_A64")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_93F")
    SetChrPos(0x9, 68600, 0, 42100, 0)
    SetChrPos(0xA, 66000, 0, 40200, 225)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_93F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_975")
    SetChrPos(0x9, 48900, 0, 48800, 0)
    SetChrPos(0xA, 34900, 0, 38200, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_9AB")
    SetChrPos(0x9, 70160, 0, 16850, 0)
    SetChrPos(0xA, 72160, 0, 18850, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    Jump("loc_A64")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_9E8")
    SetChrPos(0x9, 70160, 0, 16850, 90)
    SetChrPos(0xA, 71160, 0, 17850, 225)
    SetChrPos(0x11, 72160, 0, 18850, 0)
    Jump("loc_A64")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0x11, 45200, 0, 42700, 0)
    SetChrPos(0x9, 46900, 0, 74100, 0)
    OP_43(0x9, 0x0, 0x0, 0x4)
    SetChrPos(0xA, 49900, 0, 72100, 0)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_A64")

    label("loc_A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_END)), "loc_A64")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    OP_44(0x11, 0xFF)

    label("loc_A64")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F")

    label("loc_A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A95")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Jump("loc_B09")

    label("loc_A95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AB8")
    SetChrPos(0x12, 62400, 250, 22000, 270)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_B09")

    label("loc_AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_ADD")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32150, 0, 28000, 45)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_B09")

    label("loc_ADD")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 45660, 0, 19400, 270)
    SetChrPos(0x12, 62400, 250, 22000, 270)

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1A")
    Jump("loc_B70")

    label("loc_B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B51")
    SetChrPos(0x14, 36320, 0, 57180, 135)
    ClearChrFlags(0x14, 0x40)
    SetChrChipByIndex(0x14, 19)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_B70")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B70")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_B70")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_B7E")
    OP_A3(0x3FA)
    Event(0, 71)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_B95")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 72)

    label("loc_B95")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BB1"),
        (119, "loc_BE9"),
        (110, "loc_C58"),
        (122, "loc_CC7"),
        (2, "loc_CDD"),
        (SWITCH_DEFAULT, "loc_D0A"),
    )


    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD8")
    OP_28(0x9, 0x4, 0x10)
    Event(1, 35)
    Jump("loc_BE6")

    label("loc_BD8")

    ClearMapFlags(0x1)
    SetMapFlags(0x80)
    Event(1, 9)

    label("loc_BE6")

    Jump("loc_D0A")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF4")
    Jump("loc_D0A")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C55")
    EventBegin(0x0)
    SetMapFlags(0x400000)
    SetChrPos(0x101, 48300, 0, 7432, 0)
    SetChrPos(0x102, 49500, 0, 6573, 0)
    OP_6D(49336, 0, 72554, 0)
    OP_6C(36000, 0)
    OP_6B(5000, 0)
    FadeToBright(500, 0)
    Event(0, 33)

    label("loc_C55")

    Jump("loc_D0A")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC4")
    ClearMapFlags(0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrPos(0x9, 57890, 0, 14350, 0)
    SetChrPos(0xA, 57890, 0, 14350, 0)
    OP_6D(49800, 0, 18520, 0)
    OP_6C(33000, 0)
    FadeToBright(500, 0)
    Event(0, 37)

    label("loc_CC4")

    Jump("loc_D0A")

    label("loc_CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDA")
    OP_A2(0x264)
    Event(0, 21)

    label("loc_CDA")

    Jump("loc_D0A")

    label("loc_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_CEB")
    Event(0, 28)
    Jump("loc_D07")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_CFE")
    SetChrFlags(0x11, 0x80)
    Event(0, 26)
    Jump("loc_D07")

    label("loc_CFE")

    SetChrFlags(0x11, 0x80)
    Event(0, 27)

    label("loc_D07")

    Jump("loc_D0A")

    label("loc_D0A")

    Return()

    # Function_0_85E end

    def Function_1_D0B(): pass

    label("Function_1_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D23")
    OP_B1("t0100_y")
    Jump("loc_D2C")

    label("loc_D23")

    OP_B1("t0100_n")

    label("loc_D2C")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEA840, 0x30001)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D57")
    OP_64(0x1, 0x1)
    Jump("loc_D69")

    label("loc_D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D69")
    OP_64(0x1, 0x1)
    Jump("loc_D69")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D75")
    OP_64(0x2, 0x1)

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_D9B")
    OP_6F(0x25, 90)
    OP_6F(0x27, 90)
    OP_6F(0x29, 90)
    OP_6F(0x2B, 90)
    Jump("loc_E5F")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC6")
    OP_6F(0x25, 100)
    OP_6F(0x27, 100)
    OP_6F(0x29, 100)
    OP_6F(0x2B, 100)
    Jump("loc_E5F")

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF1")
    OP_6F(0x25, 50)
    OP_6F(0x27, 50)
    OP_6F(0x29, 50)
    OP_6F(0x2B, 50)
    Jump("loc_E5F")

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1C")
    OP_6F(0x25, 30)
    OP_6F(0x27, 30)
    OP_6F(0x29, 30)
    OP_6F(0x2B, 30)
    Jump("loc_E5F")

    label("loc_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E43")
    OP_6F(0x25, 90)
    OP_6F(0x27, 90)
    OP_6F(0x29, 90)
    OP_6F(0x2B, 90)
    Jump("loc_E5F")

    label("loc_E43")

    OP_6F(0x25, 30)
    OP_6F(0x27, 30)
    OP_6F(0x29, 30)
    OP_6F(0x2B, 30)

    label("loc_E5F")

    Return()

    # Function_1_D0B end

    def Function_2_E60(): pass

    label("Function_2_E60")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E85")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_FC7")

    label("loc_E85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_FC7")

    label("loc_E9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_FC7")

    label("loc_EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_FC7")

    label("loc_ED0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_FC7")

    label("loc_EE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F02")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_FC7")

    label("loc_F02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_FC7")

    label("loc_F1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F34")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_FC7")

    label("loc_F34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_FC7")

    label("loc_F4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F66")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_FC7")

    label("loc_F66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_FC7")

    label("loc_F7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F98")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_FC7")

    label("loc_F98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_FC7")

    label("loc_FB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_FC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_FC7")

    label("loc_FDC")

    Return()

    # Function_2_E60 end

    def Function_3_FDD(): pass

    label("Function_3_FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_100A")

    label("loc_FE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1007")
    OP_8D(0xFE, 47400, 52400, 50900, 47700, 3000)
    Jump("loc_FE4")

    label("loc_1007")

    Jump("loc_1115")

    label("loc_100A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1037")

    label("loc_1011")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1034")
    OP_8D(0xFE, 64500, 43600, 73600, 38500, 3000)
    Jump("loc_1011")

    label("loc_1034")

    Jump("loc_1115")

    label("loc_1037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1064")

    label("loc_103E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1061")
    OP_8D(0xFE, 47400, 52400, 50900, 47700, 3000)
    Jump("loc_103E")

    label("loc_1061")

    Jump("loc_1115")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1091")

    label("loc_106B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_108E")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_106B")

    label("loc_108E")

    Jump("loc_1115")

    label("loc_1091")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1115")
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_1091")

    label("loc_1115")

    Return()

    # Function_3_FDD end

    def Function_4_1116(): pass

    label("Function_4_1116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1143")

    label("loc_111D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1140")
    OP_8D(0xFE, 64500, 43600, 73600, 38500, 3000)
    Jump("loc_111D")

    label("loc_1140")

    Jump("loc_124E")

    label("loc_1143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1170")

    label("loc_114A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_116D")
    OP_8D(0xFE, 31500, 36600, 36600, 40300, 3000)
    Jump("loc_114A")

    label("loc_116D")

    Jump("loc_124E")

    label("loc_1170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_119D")

    label("loc_1177")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_119A")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 3000)
    Jump("loc_1177")

    label("loc_119A")

    Jump("loc_124E")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_11CA")

    label("loc_11A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11C7")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 3000)
    Jump("loc_11A4")

    label("loc_11C7")

    Jump("loc_124E")

    label("loc_11CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_124E")
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_11CA")

    label("loc_124E")

    Return()

    # Function_4_1116 end

    def Function_5_124F(): pass

    label("Function_5_124F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1272")
    OP_8D(0xFE, 25948, 43568, 37838, 41060, 3000)
    Jump("Function_5_124F")

    label("loc_1272")

    Return()

    # Function_5_124F end

    def Function_6_1273(): pass

    label("Function_6_1273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_12A0")

    label("loc_127A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_129D")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_127A")

    label("loc_129D")

    Jump("loc_12F0")

    label("loc_12A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_12CD")

    label("loc_12A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12CA")
    OP_8D(0xFE, 43800, 43900, 47136, 39800, 4000)
    Jump("loc_12A7")

    label("loc_12CA")

    Jump("loc_12F0")

    label("loc_12CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F0")
    OP_8D(0xFE, 74178, 21340, 67183, 16526, 4000)
    Jump("loc_12CD")

    label("loc_12F0")

    Return()

    # Function_6_1273 end

    def Function_7_12F1(): pass

    label("Function_7_12F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131F")

    label("loc_12F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_131C")
    OP_8D(0xFE, 31735, 16555, 28343, 23211, 2000)
    Jump("loc_12F9")

    label("loc_131C")

    Jump("loc_1334")

    label("loc_131F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1334")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_131F")

    label("loc_1334")

    Return()

    # Function_7_12F1 end

    def Function_8_1335(): pass

    label("Function_8_1335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135C")

    label("loc_1344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1359")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1344")

    label("loc_1359")

    Jump("loc_137F")

    label("loc_135C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_137F")
    OP_8D(0xFE, 63200, 17400, 61600, 22900, 2000)
    Jump("loc_135C")

    label("loc_137F")

    Return()

    # Function_8_1335 end

    def Function_9_1380(): pass

    label("Function_9_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AF")

    label("loc_139A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13AF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_139A")

    label("loc_13AF")

    Return()

    # Function_9_1380 end

    def Function_10_13B0(): pass

    label("Function_10_13B0")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15B2")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157B")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_146B")

    def lambda_144F():

        label("loc_144F")

        OP_97(0xFE, 0xD6D8, 0xB824, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_144F")

    QueueWorkItem2(0xFE, 1, lambda_144F)
    Jump("loc_148A")

    label("loc_146B")


    def lambda_1471():

        label("loc_1471")

        OP_97(0xFE, 0xD6D8, 0xB824, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1471")

    QueueWorkItem2(0xFE, 1, lambda_1471)

    label("loc_148A")

    SetChrChipByIndex(0xFE, 21)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_1499")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14D1")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14C9")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_14D1")

    label("loc_14C9")

    Sleep(15)
    Jump("loc_1499")

    label("loc_14D1")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 55000, 0, 47140, 74)

    label("loc_14F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1578")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1570")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 22)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    Jump("loc_1578")

    label("loc_1570")

    Sleep(500)
    Jump("loc_14F0")

    label("loc_1578")

    Jump("loc_15AF")

    label("loc_157B")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AF")

    def lambda_1597():
        OP_8D(0xFE, 51380, 38050, 58760, 43900, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1597)

    label("loc_15AF")

    Jump("loc_13E4")

    label("loc_15B2")

    Return()

    # Function_10_13B0 end

    def Function_11_15B3(): pass

    label("Function_11_15B3")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１０７５年\x01",
            "　由利贝尔王家、七耀教会\x01",
            "　以及洛连特市共同建造。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１９２年\x01",
            "　百日战役中，被围攻洛连特的\x01",
            "　埃雷波尼亚帝国军队炮击而倒塌。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１９７年\x01",
            "　在市民的协力下得以重建。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_11_15B3 end

    def Function_12_16AB(): pass

    label("Function_12_16AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C6")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "怎么了，艾丝蒂尔。\x01",
            "你要出去旅行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F就算是吧。\x02\x03",
            "我要暂时离开\x01",
            "洛连特一段时间。\x02\x03",
            "我不在的时候，\x01",
            "你不要感到寂寞哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "傻、傻瓜啊你。\x01",
            "谁会感到寂寞啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……对了，你什么时候回来啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F唔……其实我也不清楚呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是这样吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_182E")

    label("loc_17C6")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……你要早点回来哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F呵呵，你刚才说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什、什么都没说。\x02",
    )

    CloseMessageWindow()

    label("loc_182E")

    Jump("loc_1D43")

    label("loc_1831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1866")

    ChrTalk(
        0xFE,
        (
            "克劳斯爷爷家里\x01",
            "是不是发生什么事了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D43")

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1900")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "记者好像是来采访\x01",
            "卡西乌斯叔叔的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我老爸虽然是\x01",
            "王国军的士兵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是和游击士比起来，\x01",
            "就显得缺乏人情味又不引人注目了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1932")

    label("loc_1900")


    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "和士兵相比，\x01",
            "果然还是游击士比较帅啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1932")

    Jump("loc_1D43")

    label("loc_1935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_19B6")

    ChrTalk(
        0xFE,
        "啊～啊，好想快点变成大人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好想做个游击士，\x01",
            "然后大展拳脚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "居然被那个\x01",
            "艾丝蒂尔抢先了，\x01",
            "真是不甘心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D43")

    label("loc_19B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAA")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我上次看到\x01",
            "克劳斯爷爷在钟楼周围\x01",
            "专心致志地拔草呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市长连这种事\x01",
            "都要亲力亲为的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那是兴趣吧，\x01",
            "都说他喜欢园艺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F所以他才会被叫作\x01",
            "『克劳斯爷爷』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F呵呵，\x01",
            "和蔼可亲的称呼也挺好的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B07")

    label("loc_1AAA")


    ChrTalk(
        0xFE,
        (
            "我上次看到\x01",
            "克劳斯爷爷在钟楼周围\x01",
            "专心致志地拔草呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市长连这种事\x01",
            "都要亲力亲为的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B07")

    Jump("loc_1D43")

    label("loc_1B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1B65")
    OP_A2(0x6)
    OP_4A(0x9, 0)

    ChrTalk(
        0x9,
        "我就是卡西乌斯·布莱特！\x05\x02",
    )

    OP_4B(0x9, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "别跑，混帐魔兽，\x01",
            "受死吧！\x05\x02",
        )
    )

    OP_4B(0x9, 0)
    Jump("loc_1D43")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2F")
    OP_A2(0x6)

    ChrTalk(
        0x9,
        (
            "哼……\x01",
            "还是要谢谢\x01",
            "你们救了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "而且……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然不服气，\x01",
            "但艾丝蒂尔你真的很厉害哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然还远远比不上\x01",
            "卡西乌斯叔叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "决定了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我将来一定要\x01",
            "成为一名游击士！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8A")

    label("loc_1C2F")


    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "卡西乌斯叔叔\x01",
            "真是太酷了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要当男子汉就是应该\x01",
            "以卡西乌斯叔叔作为目标啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8A")

    Jump("loc_1D43")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1CC5")

    ChrTalk(
        0x9,
        (
            "本应在翡翠之塔。\x01",
            "看到我就说明发生了BUG。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D43")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1A")
    OP_A2(0x6)
    OP_4A(0x9, 0)

    ChrTalk(
        0x9,
        "嘿嘿，来追我呀，追我呀～～\x05\x02",
    )

    OP_4B(0x9, 0)
    Sleep(800)

    ChrTalk(
        0x9,
        "你追不到我的啦～\x05\x02",
    )

    OP_4B(0x9, 0)
    Jump("loc_1D43")

    label("loc_1D1A")

    OP_4A(0x9, 0)

    ChrTalk(
        0x9,
        (
            "但是～\x01",
            "那可是我先发现的哦～\x05\x02",
        )
    )

    OP_4B(0x9, 0)

    label("loc_1D43")

    TalkEnd(0x9)
    Return()

    # Function_12_16AB end

    def Function_13_1D47(): pass

    label("Function_13_1D47")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1D93")

    ChrTalk(
        0xFE,
        (
            "刚才克劳斯爷爷\x01",
            "急匆匆地跑了过去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2057")

    label("loc_1D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1DF7")

    ChrTalk(
        0xFE,
        (
            "我老爸也一直在读\x01",
            "《利贝尔通讯》这本杂志呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "封面上会刊登\x01",
            "眼下风云人物的照片哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2057")

    label("loc_1DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1E55")

    ChrTalk(
        0xFE,
        (
            "最近在主日学校学了\x01",
            "关于游击士协会的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士果然是\x01",
            "让人神往的职业啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2057")

    label("loc_1E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1EA7")

    ChrTalk(
        0xFE,
        (
            "市长家里的庭院\x01",
            "真的很漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "克劳斯爷爷说\x01",
            "那是他自己打理的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2057")

    label("loc_1EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1EE2")
    OP_4A(0xA, 0)

    ChrTalk(
        0xA,
        (
            "鲁克一点情面都不讲，\x01",
            "我只好逃跑了。\x05\x02",
        )
    )

    OP_4B(0xA, 0)
    Jump("loc_2057")

    label("loc_1EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA5")
    OP_A2(0x7)

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔姐姐，\x01",
            "今天真是谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果姐姐你们\x01",
            "没有来救我们的话，\x01",
            "我们不知道会变成什么样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我想鲁克也会非常\x01",
            "感谢姐姐你们的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "姐姐就别再生他的气了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FEC")

    label("loc_1FA5")


    ChrTalk(
        0xA,
        (
            "我想鲁克也会非常\x01",
            "感谢姐姐你们的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "姐姐就别再生他的气了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1FEC")

    Jump("loc_2057")

    label("loc_1FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_202A")

    ChrTalk(
        0xA,
        (
            "应该在翡翠之塔的。\x01",
            "如果看到了就请联系近藤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2057")

    label("loc_202A")

    OP_4A(0xA, 0)

    ChrTalk(
        0xA,
        (
            "带我去嘛～！\x01",
            "可是我提醒你的哦～\x05\x02",
        )
    )

    OP_4B(0xA, 0)

    label("loc_2057")

    TalkEnd(0xA)
    Return()

    # Function_13_1D47 end

    def Function_14_205B(): pass

    label("Function_14_205B")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2209")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚。\x01",
            "你们真的要去柏斯吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈……\x01",
            "不愧是小克露莎啊。\x02\x03",
            "消息总是那么灵通。\x02\x03",
            "我们要调查一些事情，\x01",
            "所以呢，要去柏斯那里才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不单是卡西乌斯叔叔，\x01",
            "就连你们两人也不在了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔……人家也要一起去，\x01",
            "帮你们做采访。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        "约修亚，把我也带上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F啊……这、这不好办哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我果然还是\x01",
            "放不下这里发生的新闻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人烦恼啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_227D")

    label("loc_2209")


    ChrTalk(
        0xFE,
        (
            "人家会乖乖地在这里等着，\x01",
            "直到你们归来。\x01",
            "所以你们要早点回来哦。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都不在的话，\x01",
            "新闻的材料就少了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227D")

    Jump("loc_380F")

    label("loc_2280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_23B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2361")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "啊，是艾丝蒂尔和约修亚！\x01",
            "还有……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "呀，雪拉姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F你好啊，小克露莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "街上居然同时聚集了\x01",
            "三位鼎鼎大名的游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "哈，难道是有什么事件吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_23AE")

    label("loc_2361")


    ChrTalk(
        0xB,
        (
            "街上居然同时聚集了\x01",
            "三位鼎鼎大名的游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "难道是有什么事件吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_23AE")

    Jump("loc_380F")

    label("loc_23B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_255E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2511")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "艾丝蒂尔、约修亚㈱\x01",
            "听说你们两人很活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "唔，\x01",
            "在帕赛尔农场驱逐魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "在矿山救助矿工……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这次又要负责护送\x01",
            "记者叔叔们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F知、知道得还真清楚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "嗯，还好啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "要是记者叔叔他们\x01",
            "肯聘用人家就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "人家绝对\x01",
            "是做记者的好料哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F（嗯，\x01",
            "　想来也的确挺适合的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（哈哈……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_255B")

    label("loc_2511")


    ChrTalk(
        0xB,
        (
            "要是记者叔叔他们\x01",
            "肯聘用人家就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "人家绝对\x01",
            "是做记者的好料哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255B")

    Jump("loc_380F")

    label("loc_255E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_263A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2618")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "上次我看见市长爷爷\x01",
            "从游击士协会出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "还有，最近经常在街上看见\x01",
            "里农叔叔家的老婆婆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "不寻常呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但是，到底要追哪一条线索呢，\x01",
            "真是让人烦恼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2637")

    label("loc_2618")


    ChrTalk(
        0xB,
        (
            "啊啊，\x01",
            "新闻在呼唤人家呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2637")

    Jump("loc_380F")

    label("loc_263A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_26A7")

    ChrTalk(
        0xB,
        (
            "根据我的情报，\x01",
            "帕赛尔农场那边\x01",
            "好像有什么事要发生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "要不要写份突击报道\x01",
            "给爱娜姐姐呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_380F")

    label("loc_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_28A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2873")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "对了， \x01",
            "卡西乌斯叔叔上哪儿去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，因为工作的关系，\x01",
            "他恐怕短期内不会回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "唔，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "卡西乌斯叔叔\x01",
            "也是人家很关注的人呢。\x01",
            "有点可惜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F小克露莎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我觉得卡西乌斯叔叔\x01",
            "是个经得起考验的\x01",
            "成熟男人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "他所表现出来的那种强大、\x01",
            "不灭、独特的华丽，\x01",
            "实在是让人无法抗拒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "他一定是很有影响力的游击士。\x01",
            "嗯，卡西乌斯叔叔不错～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F……喂，\x01",
            "小克露莎你几岁了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，好早熟呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28A4")

    label("loc_2873")


    ChrTalk(
        0xFE,
        (
            "啊～啊，卡西乌斯叔叔不在，\x01",
            "少了很多谈资呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A4")

    Jump("loc_380F")

    label("loc_28A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2982")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2948")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "艾丝蒂尔和约修亚\x01",
            "这么快就有表现了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真不愧是人家\x01",
            "关注的游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "继续好好加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "人家是你们\x01",
            "忠实的崇拜者哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_297F")

    label("loc_2948")


    ChrTalk(
        0xB,
        "继续好好加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "人家是你们\x01",
            "忠实的崇拜者哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_297F")

    Jump("loc_2F1A")

    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_2B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B06")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "喂喂，\x01",
            "艾丝蒂尔、约修亚。\x01",
            "你们真的已经成为了游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你的消息总是那么灵通啊～\x01",
            "小克露莎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真不愧是克露莎\x01",
            "看重的一对呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这下你们就可以大展拳脚了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "其实克露莎也\x01",
            "喜欢有大人魅力的\x01",
            "雪拉扎德姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但是忍不住会偏袒\x01",
            "艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506F好、好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F多谢你了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B40")

    label("loc_2B06")


    ChrTalk(
        0xB,
        "一场划时代的大戏剧终于要开演了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "人家好期待哦★\x02",
    )

    CloseMessageWindow()

    label("loc_2B40")

    Jump("loc_2F1A")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E75")
    OP_A2(0x8)

    ChrTalk(
        0xB,
        (
            "啊……\x01",
            "艾丝蒂尔、约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对了对了，\x01",
            "你们两个成为游击士了，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，\x01",
            "为什么你会知道呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为因为，\x01",
            "人家将来想成为一名记者嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "将来我会成为利贝尔通讯的女记者，\x01",
            "发挥自己的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "可不要小看人家\x01",
            "收集情报的能力哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506F是、是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "凭人家的直觉， \x01",
            "你们两人肯定会成为风云人物的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F呵、呵呵，\x01",
            "谢谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为爱而结合的你们，\x01",
            "一定会成为坚守正义的游击士，\x01",
            "这多美妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "感觉就像\x01",
            "浪漫的舞台剧一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……啊？\x02\x03",
            "我和约修亚不是恋人，\x01",
            "我们是家人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵～\x01",
            "艾丝蒂尔这你就不懂啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "约修亚是你们家的养子嘛，\x01",
            "以后什么身份还说不定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而且这样的故事\x01",
            "读者也会很喜欢的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019F读、读者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔……\x01",
            "真是超乎我的想象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总之，\x01",
            "我很期待你们的未来哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1A")

    label("loc_2E75")


    ChrTalk(
        0xB,
        (
            "相互信任守护着彼此，\x01",
            "并尝试脱离险境的\x01",
            "一对游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "啊，此时爱的种子\x01",
            "就在他们的心中生根发芽。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "多美妙啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2F1A")

    Jump("loc_380F")

    label("loc_2F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_343A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_30B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3078")
    OP_A2(0x8)
    OP_A2(0x215)

    ChrTalk(
        0xB,
        (
            "喂喂，\x01",
            "艾丝蒂尔、约修亚。\x01",
            "你们真的已经成为了游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你的消息总是那么灵通啊～\x01",
            "小克露莎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "真不愧是克露莎\x01",
            "看重的一对呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这下你们就可以大展拳脚了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "其实克露莎\x01",
            "也喜欢有大人魅力的\x01",
            "雪拉扎德姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "但是忍不住会偏袒\x01",
            "艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F好、好的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F多谢你了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30B2")

    label("loc_3078")


    ChrTalk(
        0xB,
        "好戏终于要开演了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "好期待哦★\x02",
    )

    CloseMessageWindow()

    label("loc_30B2")

    Jump("loc_3437")

    label("loc_30B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C5")
    OP_A2(0x8)
    OP_A2(0x215)

    ChrTalk(
        0xB,
        (
            "啊……\x01",
            "艾丝蒂尔、约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对了对了，\x01",
            "你们两个成为游击士了，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊，\x01",
            "为什么你会知道呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为我的目标\x01",
            "是当记者嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我将来会加入利贝尔通讯社，\x01",
            "当一名出色的女记者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "可不要小看我\x01",
            "收集情报的能力哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506F是、是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "凭我的直觉， \x01",
            "你们两人肯定会成为风云人物的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F呵、呵呵，\x01",
            "谢谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为，彼此深爱的两位游击士\x01",
            "共同坚守正义，\x01",
            "这是多么美妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "感觉就像\x01",
            "一场浪漫的爱情剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……啊？\x02\x03",
            "#000F我和约修亚不是恋人，\x01",
            "是家人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵～\x01",
            "艾丝蒂尔这你就不懂啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "约修亚只是你们家的养子嘛，\x01",
            "以后什么身份还说不定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而且这样的故事\x01",
            "读者也会很喜欢的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019F读、读者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总之，\x01",
            "我很期待你们的未来哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3437")

    label("loc_33C5")


    ChrTalk(
        0xB,
        (
            "相互信任守护着彼此，\x01",
            "并尝试脱离险境的\x01",
            "一对游击士……\x02",

        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "多美妙啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3437")

    Jump("loc_380F")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376A")
    OP_A2(0x8)
    OP_A2(0x214)

    ChrTalk(
        0x101,
        "#001F早上好呀，小克露莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "早上好。\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对了对了，\x01",
            "你们两个成为游击士了，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F是啊，\x01",
            "为什么你会知道呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为，我的目标\x01",
            "是当记者嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我将来会加入利贝尔通讯社，\x01",
            "当一名出色的女记者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "可不要小看我\x01",
            "收集情报的能力哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#506F是、是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "凭我的直觉， \x01",
            "你们两人肯定会成为风云人物的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F呵、呵呵，\x01",
            "谢谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "因为爱而结合的你们，\x01",
            "一定会成为坚守正义的游击士，\x01",
            "这多美妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "感觉就像\x01",
            "浪漫的舞台剧一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F……啊？\x02\x03",
            "我和约修亚不是恋人，\x01",
            "我们是家人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "呵～\x01",
            "艾丝蒂尔这你就不懂啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "约修亚只是你们家的养子嘛，\x01",
            "以后什么身份还说不定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "而且这样的故事\x01",
            "读者也会很喜欢的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#019F读、读者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总之，\x01",
            "我很期待你们的未来哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_380F")

    label("loc_376A")


    ChrTalk(
        0xB,
        (
            "相互信任守护着彼此，\x01",
            "并尝试脱离险境的\x01",
            "一对游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "啊，此时爱的种子\x01",
            "就在他们的心中生根发芽。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "多美妙啊……\x02",
    )

    CloseMessageWindow()

    label("loc_380F")

    TalkEnd(0xB)
    Return()

    # Function_14_205B end

    def Function_15_3813(): pass

    label("Function_15_3813")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_391D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DB")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "最近，我的岳父\x01",
            "在工作上给了我不少的建议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说我在林业\x01",
            "这行业里做了很久，\x01",
            "不过要学习的东西还有很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我以前的确是\x01",
            "有点自高自大……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在我觉得有些羞愧呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_391A")

    label("loc_38DB")


    ChrTalk(
        0xFE,
        (
            "我以前的确是\x01",
            "有点自高自大……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在我觉得有些羞愧呢。\x02",
    )

    CloseMessageWindow()

    label("loc_391A")

    Jump("loc_3DB3")

    label("loc_391D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_39EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3996")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "虽说工作挺顺利的，\x01",
            "木材的销量也不断增加……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么说呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是没有得到\x01",
            "岳父的认同。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E8")

    label("loc_3996")


    ChrTalk(
        0xFE,
        (
            "虽说工作挺顺利的，\x01",
            "木材的销量也不断增加……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是没有得到\x01",
            "岳父的认同。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E8")

    Jump("loc_3DB3")

    label("loc_39EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3A6F")

    ChrTalk(
        0xFE,
        (
            "木材卖出去越多，\x01",
            "我养家的自信和动力也\x01",
            "源源不断地涌上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "事业上顺心顺境，\x01",
            "我觉得自己的能力\x01",
            "一点都不比岳父差。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DB3")

    label("loc_3A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3ACF")

    ChrTalk(
        0xFE,
        (
            "刚收到柏斯商人\x01",
            "追加的木材订单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要继续加油，\x01",
            "向其他地方推销自己的木材！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DB3")

    label("loc_3ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3BD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6F")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "我是为了\x01",
            "能和妻子在一起， \x01",
            "才承继了岳父的林业工作的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近好不容易\x01",
            "才习惯了这份工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且感觉干劲和效率\x01",
            "也提高了很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD3")

    label("loc_3B6F")


    ChrTalk(
        0xFE,
        (
            "我是为了\x01",
            "能和妻子在一起， \x01",
            "才承继了岳父的林业工作的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近好不容易\x01",
            "才习惯了这份工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD3")

    Jump("loc_3DB3")

    label("loc_3BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3BFC")

    ChrTalk(
        0xC,
        (
            "见到这个的你。\x01",
            "是Bug。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DB3")

    label("loc_3BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C83")
    OP_A2(0x9)

    ChrTalk(
        0xC,
        (
            "虽然接受了商人的订货，\x01",
            "不过木材好像还有些不够啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "为了我的妻子，为了得到岳父的承认，\x01",
            "我一定要努力加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3C83")


    ChrTalk(
        0xC,
        (
            "为了我的妻子，为了得到岳父的承认，\x01",
            "我一定要努力加油。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBE")

    Jump("loc_3DB3")

    label("loc_3CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5B")
    OP_A2(0x9)

    ChrTalk(
        0xC,
        (
            "呼，\x01",
            "今后的工作就得到\x01",
            "南面的神秘森林去开展了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不久之后就会有\x01",
            "柏斯的木材采购商来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "需要准备足够的木材\x01",
            "供他们采购才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DB3")

    label("loc_3D5B")


    ChrTalk(
        0xC,
        (
            "不久之后就会有\x01",
            "柏斯的木材采购商来这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "需要准备足够的木材\x01",
            "供他们采购才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB3")

    TalkEnd(0xC)
    Return()

    # Function_15_3813 end

    def Function_16_3DB7(): pass

    label("Function_16_3DB7")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3E08")

    ChrTalk(
        0x11,
        (
            "刚才克劳斯爷爷\x01",
            "从这里走过哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "还好大声地和我\x01",
            "打了招呼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F8D")

    label("loc_3E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3E55")

    ChrTalk(
        0x11,
        (
            "鲁克真是的，\x01",
            "从早上开始就一直那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "男孩子还真是单纯啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F8D")

    label("loc_3E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3E8A")

    ChrTalk(
        0x11,
        (
            "鲁克和帕特他们\x01",
            "究竟跑到哪里去了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F8D")

    label("loc_3E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F62")
    OP_A2(0xA)

    ChrTalk(
        0x11,
        (
            "呀，\x01",
            "是艾丝蒂尔姐姐和约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好啊，小尤妮。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F今天怎么没有和\x01",
            "鲁克、帕特在一起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "直到刚才\x01",
            "还和他们在一起的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过一眨眼的功夫他们两个\x01",
            "就不知道跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F8D")

    label("loc_3F62")


    ChrTalk(
        0x11,
        (
            "鲁克和帕特他们\x01",
            "究竟跑到哪里去了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8D")

    TalkEnd(0x11)
    Return()

    # Function_16_3DB7 end

    def Function_17_3F91(): pass

    label("Function_17_3F91")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_40A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406C")
    OP_A2(0xD)

    ChrTalk(
        0xE,
        "成功啦～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "听我说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "她终于答应\x01",
            "和我交往了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "啊啊，女神大人……\x01",
            "一整天所做的努力终于没有白费啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F（一、一整天？\x01",
            "　唔……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（真是坚持不懈换来的胜利呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_40A5")

    label("loc_406C")


    ChrTalk(
        0xE,
        (
            "啊啊，女神大人……\x01",
            "一整天所做的努力终于没有白费啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A5")

    Jump("loc_41BB")

    label("loc_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_417D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_413A")
    OP_A2(0xD)

    ChrTalk(
        0xE,
        (
            "唉～从早晨开始，\x01",
            "我就告白好多次了，\x01",
            "可她好像都不愿意接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "看起来她应该\x01",
            "并不讨厌我呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "我究竟应该怎么办啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_417A")

    label("loc_413A")


    ChrTalk(
        0xE,
        (
            "唉～从早晨开始，\x01",
            "我就告白好多次了，\x01",
            "可她好像都不愿意接受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417A")

    Jump("loc_41BB")

    label("loc_417D")


    ChrTalk(
        0xE,
        (
            "啊……\x01",
            "那个姑娘真可爱呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "鼓足勇气\x01",
            "去和她打招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41BB")

    TalkEnd(0xE)
    Return()

    # Function_17_3F91 end

    def Function_18_41BF(): pass

    label("Function_18_41BF")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4238")
    OP_A2(0xD)

    ChrTalk(
        0xFE,
        "成功啦～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我约她一起去看女王的诞辰庆典，\x01",
            "她真的答应了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我要努力打工赚钱才行！\x02",
    )

    CloseMessageWindow()
    Jump("loc_425F")

    label("loc_4238")


    ChrTalk(
        0xFE,
        (
            "从现在起我要\x01",
            "努力打工赚钱才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425F")

    Jump("loc_4420")

    label("loc_4262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F9")
    OP_A2(0xD)

    ChrTalk(
        0x10,
        (
            "听说王都将举行\x01",
            "女王的诞辰庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "而且还会举办每年一度的武术大会，\x01",
            "这还真是非常热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "我约了她一起去看诞辰庆典。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4346")

    label("loc_42F9")


    ChrTalk(
        0x10,
        "我约了她到王都看女王的诞辰庆典。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "呵呵呵，\x01",
            "其实我想在那里向她表白。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4346")

    Jump("loc_4420")

    label("loc_4349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_43A5")

    ChrTalk(
        0x10,
        (
            "每天和她见面的时候，\x01",
            "不是聊天就是喝茶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "洛连特的约会场所\x01",
            "实在是有限啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4420")

    label("loc_43A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_43F0")

    ChrTalk(
        0x10,
        "啊啊，真是幸福呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "每天都可以\x01",
            "和自己喜欢的人一起度过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4420")

    label("loc_43F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_4420")

    ChrTalk(
        0x10,
        (
            "嗯呼呼呼，\x01",
            "今天是我第一次的约会哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4420")

    TalkEnd(0x10)
    Return()

    # Function_18_41BF end

    def Function_19_4424(): pass

    label("Function_19_4424")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_4575")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_454E")
    OP_A2(0xB)

    ChrTalk(
        0xD,
        (
            "星星开始闪烁的时候，\x01",
            "他在塔上对我这么说——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "可以和我交往吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "嗯呵呵★\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这就是\x01",
            "我梦寐以求的场景啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F（唔，\x01",
            "　的确是一个相当不错的地方……）\x02\x03",
            "#000F（不过为了听这句话\x01",
            "　两个人特意跑上这里来？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（呵呵……\x01",
            "　这要看当事人是怎么想的了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4572")

    label("loc_454E")


    ChrTalk(
        0xD,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "好·幸·福·呢★\x02",
    )

    CloseMessageWindow()

    label("loc_4572")

    Jump("loc_47EF")

    label("loc_4575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4716")
    OP_A2(0xB)

    ChrTalk(
        0xD,
        "哎～我该怎么办呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "那个人，他好像喜欢我。\x01",
            "我虽然很乐意接受他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "不过这样的场景，\x01",
            "跟我理想中的告白场景不太一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔……\x01",
            "场景什么的真的那么重要吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "当然啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "这有可能成为我\x01",
            "一生难忘的回忆啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "当我变成老太婆的时候，\x01",
            "临死前脑海里浮现的不也应该是\x01",
            "现在这个最美妙的场景吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我不能在这个胡同里面\x01",
            "接受表白啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵……\x01",
            "这个就是当事人的想法问题了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4796")

    label("loc_4716")


    ChrTalk(
        0xD,
        (
            "他，无论怎样热心地向我告白……\x01",
            "我还是觉得跟我理想中的\x01",
            "告白场景不太一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "要是他能在\x01",
            "一个好点的场景\x01",
            "说那番话就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4796")

    Jump("loc_47EF")

    label("loc_4799")


    ChrTalk(
        0xD,
        (
            "今天这么好的天气，\x01",
            "真是让人神清气爽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我感觉今天似乎\x01",
            "有什么好事要发生呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EF")

    TalkEnd(0xD)
    Return()

    # Function_19_4424 end

    def Function_20_47F3(): pass

    label("Function_20_47F3")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B1")
    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "虽然有些犹豫，不过我还是决定\x01",
            "和他一起去观看女王的诞辰庆典。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而我还是对妈妈说\x01",
            "自己是和普通朋友一起去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是对不起，妈妈……\x01",
            "不过我还是想和他一起去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A17")

    label("loc_48B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FD")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "王都这个地方，\x01",
            "听说是个很繁华的大都会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "被传颂成为灯火辉煌的\x01",
            "传统与美丽相融合的不夜城……\x01",
            "伫立在湖畔的典雅的格兰赛尔城……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "络绎不绝往来穿梭的人群……\x01",
            "各式各样的街市商店……\x01",
            "还有诞辰庆典的盛装游行和烟花表演……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光是想想就已经很期待了。\x01",
            "真是让人向往的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "而且还可以和他……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A17")

    label("loc_49FD")


    ChrTalk(
        0xFE,
        "啊啊，我太激动了……\x02",
    )

    CloseMessageWindow()

    label("loc_4A17")

    Jump("loc_4D94")

    label("loc_4A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4B26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABE")
    OP_A2(0xC)

    ChrTalk(
        0xF,
        (
            "他主动约我一起\x01",
            "到王都观看女王的诞辰庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "哎呀，有点犹豫呢。\x01",
            "怎么和妈妈说才好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "要是到了王都之后\x01",
            "他向我求婚的话那就太棒了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B23")

    label("loc_4ABE")

    OP_A2(0xC)

    ChrTalk(
        0xF,
        (
            "他主动约我一起\x01",
            "到王都观看女王的诞辰庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "要是到了王都之后\x01",
            "他向我求婚的话那就太棒了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B23")

    Jump("loc_4D94")

    label("loc_4B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_4C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF2")
    OP_A2(0xB)

    ChrTalk(
        0xF,
        (
            "我觉得每天和他见面\x01",
            "是一件开心的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "不过最近的约会地点\x01",
            "已经有些千篇一律了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嗯，现在才是\x01",
            "考验男朋友真正价值的时候呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（艾丝蒂尔，说的挺直接嘛……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C48")

    label("loc_4BF2")


    ChrTalk(
        0xF,
        (
            "我觉得每天和他见面\x01",
            "是一件开心的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "最近的约会地点\x01",
            "已经有些千篇一律了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C48")

    Jump("loc_4D94")

    label("loc_4C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_4C86")

    ChrTalk(
        0xF,
        (
            "他这个人其实挺好的呢。\x01",
            "希望他能永远疼爱我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D94")

    label("loc_4C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_4D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D2A")
    OP_A2(0xB)

    ChrTalk(
        0xF,
        (
            "呵呵，\x01",
            "我们才刚刚开始交往呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "刚才看到什么东西闪了一闪呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "啊啊，\x01",
            "这世界其实是如此的美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（唔，二人世界呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D94")

    label("loc_4D2A")


    ChrTalk(
        0xF,
        (
            "呵呵，现在觉得什么都是新鲜美好的。\x01",
            "刚才看到什么东西闪了一闪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "啊啊，\x01",
            "这世界其实是如此的美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D94")

    TalkEnd(0xF)
    Return()

    # Function_20_47F3 end

    def Function_21_4D98(): pass

    label("Function_21_4D98")

    EventBegin(0x0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrPos(0x0, 49730, 0, 79070, 180)
    SetChrPos(0x1, 50770, 0, 79870, 180)
    SetChrPos(0x2, 49620, 0, 80520, 180)
    SetChrPos(0x19, 50932, 0, 42709, 270)
    SetChrPos(0x18, 64013, 0, 42894, 270)
    OP_6C(45000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x19,
        "女孩的声音",
        (
            "前辈，太危险了啦！\x01",
            "跑得那么快的话……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "男人的声音",
        (
            "因、因为……\x01",
            "不跑快点就赶不上啦！\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    TurnDirection(0x19, 0x18, 0)
    OP_6D(51350, 0, 43040, 3000)

    def lambda_4EA6():

        label("loc_4EA6")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_4EA6")

    QueueWorkItem2(0x19, 1, lambda_4EA6)
    OP_8E(0x18, 0xE25B, 0x0, 0xA926, 0x1388, 0x0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x18, 0xDC36, 0x0, 0xA85E, 0xBB8, 0x0)
    OP_8F(0x18, 0xD89B, 0x0, 0xA98A, 0xBB8, 0x0)
    OP_8F(0x18, 0xD398, 0x0, 0xA7FA, 0xBB8, 0x0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x18, 0xCE24, 0x0, 0xA926, 0xBB8, 0x0)
    OP_8F(0x18, 0xC7B3, 0x0, 0xAAA0, 0x7D0, 0x0)
    OP_44(0x19, 0xFF)

    ChrTalk(
        0x18,
        (
            "#145F#4P哈啊……呼呼……\x02\x03",
            "#145F可、可恶……\x01",
            "难道香烟也要少抽了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F你们两位，在干什么啊？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrPos(0x101, 50434, 0, 54609, 270)
    SetChrPos(0x102, 48721, 0, 55602, 270)
    SetChrPos(0x103, 51196, 0, 55910, 270)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0x102, 0x1, 0x0, 0x17)
    OP_43(0x103, 0x1, 0x0, 0x18)
    OP_6D(51050, 0, 45160, 1000)
    TurnDirection(0x18, 0x101, 400)
    TurnDirection(0x19, 0x101, 400)
    Sleep(2000)

    ChrTalk(
        0x18,
        (
            "#140F#4P哦哦，是你们啊。\x02\x03",
            "#140F其实啊， \x01",
            "我们现在正赶去柏斯啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F可是，\x01",
            "定期船好像还没有来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#141F#4P啊，我知道。\x01",
            "所以才打算从大道走过去啊。\x02\x03",
            "#141F虽然要花不少时间，\x01",
            "不过也不至于远到不能走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F那真是辛苦你们了。\x01",
            "难道发现了独家新闻吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#147F#4P没错，是非常棒的题材。\x02\x03",
            "#144F不能再磨蹭了！\x01",
            "今天之内必须要赶到柏斯！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x18, 0x1, 0x0, 0x19)
    TurnDirection(0x19, 0x18, 0)
    OP_62(0x18, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x18, 0x998B, 0x0, 0x9FC4, 0x1770, 0x0)
    OP_44(0x18, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)

    ChrTalk(
        0x19,
        "#154F#4P前辈，真的不要紧吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 400)
    TurnDirection(0x101, 0x19, 400)
    TurnDirection(0x102, 0x19, 400)
    TurnDirection(0x103, 0x19, 400)

    ChrTalk(
        0x19,
        (
            "#151F啊，那么再见了～！\x01",
            "小艾，小约。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x19, 0x1, 0x0, 0x19)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x19, 0x998B, 0x0, 0x9FC4, 0x1770, 0x0)
    OP_44(0x19, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8)

    ChrTalk(
        0x103,
        (
            "#020F真是活泼的组合呢。\x01",
            "你们认识那两个人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F就是那两个杂志的记者啊。\x01",
            "之前我们还带他们去塔那边取材。\x02\x03",
            "#000F是不是发生了什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_21_4D98 end

    def Function_22_5300(): pass

    label("Function_22_5300")

    OP_92(0x101, 0x19, 0x7D0, 0xBB8, 0x0)
    Return()

    # Function_22_5300 end

    def Function_23_530F(): pass

    label("Function_23_530F")

    OP_92(0x102, 0x19, 0xBB8, 0xBB8, 0x0)
    Return()

    # Function_23_530F end

    def Function_24_531E(): pass

    label("Function_24_531E")

    OP_92(0x103, 0x19, 0xDAC, 0xBB8, 0x0)
    Return()

    # Function_24_531E end

    def Function_25_532D(): pass

    label("Function_25_532D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5356")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x2, 0xFE, 0)
    TurnDirection(0x19, 0xFE, 0)
    OP_48()
    Jump("Function_25_532D")

    label("loc_5356")

    Return()

    # Function_25_532D end

    def Function_26_5357(): pass

    label("Function_26_5357")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 72905, 0, 18979, 90)
    SetChrPos(0x102, 74801, 0, 19516, 225)
    SetChrPos(0x101, 74801, 0, 18064, 315)
    OP_6F(0x2C, 30)
    OP_6D(74132, 0, 18793, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_28(0xA, 0x4, 0x10)
    OP_28(0xA, 0x1, 0x4)

    ChrTalk(
        0x1A,
        (
            "#020F两人都辛苦了。\x02\x03",
            "#020F那么按照规矩，\x01",
            "我还是要确认一下搜索对象。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了２个\x07\x02",
            "小箱子\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x373, 2)

    ChrTalk(
        0x1A,
        (
            "#020F……嗯，是真品。\x02\x03",
            "而且也没有打开过的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（好、好险呢～～）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F（果然……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#021F恭喜你们两人，\x01",
            "实地研修考试合格了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F哼哼，这种考试太轻松了。\x02\x03",
            "#000F……对了，雪拉姐。\x01",
            "那小箱子里面放的是什么啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020F这个暂时保密。\x01",
            "等一下回到协会你们就知道了。\x02\x03",
            "#020F好了，\x01",
            "闲话就到此为止。\x02\x03",
            "#020F其实考试通过\x01",
            "并不代表研修就这样结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦，什么？\x02\x03",
            "#004F可是我们的考试不是都合格了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020F最后一样要做的\x01",
            "就是关于你们的研修报告。\x02\x03",
            "#020F我知道你们已经很累了，\x01",
            "不过现在要先回协会才行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F呼，还要继续啊……\x02\x03",
            "#505F不过也没办法。\x01",
            "才刚刚踏上游击士之路，不努力不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "已经到这步了，再忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_26_5357 end

    def Function_27_5703(): pass

    label("Function_27_5703")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, 72905, 0, 18979, 90)
    SetChrPos(0x102, 74801, 0, 19516, 225)
    SetChrPos(0x101, 74801, 0, 18064, 315)
    OP_6F(0x2C, 30)
    OP_6D(74132, 0, 18793, 0)
    OP_0D()
    OP_28(0xA, 0x4, 0x4)
    OP_28(0xA, 0x4, 0x8)
    OP_28(0xA, 0x1, 0x1)

    ChrTalk(
        0x1A,
        (
            "#020F终于到了研修最后也是最重要的一关了。\x01",
            "　\x02\x03",
            "#020F现在就要开始进行你们两人的认定考试。\x01",
            "　\x02\x03",
            "#020F希望你们能把\x01",
            "到目前为止学到的知识都发挥出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 315, 400)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F……我说雪拉姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#020F什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F……难道，\x01",
            "你说的考试不是笔试吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#023F哈啊？\x02\x03",
            "艾丝蒂尔，\x01",
            "你刚才不是看了公告板吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯，看是看了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020F你还在手册上做了记录，\x01",
            "难道又不记得了？\x02\x03",
            "#020F公告板上不是写着搜索地下水路吗。\x01",
            "那就是研修的最终考试哦。\x01",
            "  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F………………………\x02\x03",
            "#007F哈啊～太好了～～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x101, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F啊啊，空之女神大人……\x02\x03",
            "衷心感谢您为我们\x01",
            "创造了地下水路这种东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F难道……\x01",
            "你一直以为那是笔试吗？\x02\x03",
            "所以刚才在工房一直闹着不肯走……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#502F呼，真怀念……现在想起来，\x01",
            "研修还真是一段美好的回忆呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F唉。\x01",
            "我们真的能够毕业吗……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#509F什么嘛～这样说算什么意思啊？\x02",
    )

    CloseMessageWindow()

    def lambda_5B39():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5B39)

    def lambda_5B47():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5B47)

    ChrTalk(
        0x1A,
        (
            "#022F好了好了，\x01",
            "两人的闲聊到此为止。\x02\x03",
            "#022F都已经快考试了，\x01",
            "至少也应该有点紧张感吧。\x02\x03",
            "#022F如果考试不合格，\x01",
            "可就要接受严酷的补习哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，没问题啦㈱\x02\x03",
            "#001F好了，赶快开始考试吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#026F嗯，这么有自信的话，\x01",
            "就用结果来证明给我看吧。\x02\x03",
            "#020F……回到正题。正如公告板写的那样，\x01",
            "考试的题目是搜索地下水路。\x02\x03",
            "#020F搜索对象是位于某处的宝箱，\x01",
            "搜索目的是把藏在宝箱内的东西回收。\x02\x03",
            "#020F地下水路的构造很简单，\x01",
            "所以你们不用担心会迷路……\x02\x03",
            "#020F但是里面到处都有真正的魔兽，\x01",
            "大意的话可会吃苦头的哦。\x02\x03",
            "#020F要是遭遇到危险的话，就用这个吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了３个\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了 \x07\x02",
            "魔兽手册\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x1F5, 3)
    OP_3E(0x20F, 1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x101,
        "#505F嗯？这本手册是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#020F这是魔兽手册，用来记录战斗过的\x01",
            "对手的情报。\x02\x03",
            "#020一旦掌握了敌人的特点，就要马上\x01",
            "记录到这本手册中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x02\x03",
            "知己知彼，才能百战百胜。\x01",
            "就是这个意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#021F呵呵，正是。\x01",
            "你懂得很多嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嘿，看来是件好东西啊。\x02\x03",
            "#001F谢啦，雪拉姐！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会充分利用的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F好～的！ \x01",
            "约修亚，一鼓作气向前冲吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x02\x03",
            "#010F就把这当作实战，\x01",
            "小心谨慎地行动吧。\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_27_5703 end

    def Function_28_60C2(): pass

    label("Function_28_60C2")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x17, 0xFF)
    SetChrPos(0x102, 29410, 0, 68310, 0)
    SetChrPos(0x101, 30510, 0, 69400, 0)
    SetChrPos(0x19, 31602, 0, 67448, 0)
    SetChrPos(0x18, 32375, 0, 68461, 0)
    SetChrPos(0x17, 33719, 0, 67665, 0)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_6D(31270, 0, 68330, 0)
    OP_6B(3000, 0)
    OP_6C(270000, 0)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x17, 0x40)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x102, 0x17, 0)
    TurnDirection(0x19, 0x17, 0)
    TurnDirection(0x18, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_A2(0x259)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x1, 0x100)
    OP_28(0x19, 0x1, 0x200)
    OP_28(0x5, 0x4, 0x40)
    OP_28(0x9, 0x4, 0x40)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x17), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_61B1")

    label("loc_61B1")

    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        (
            "#130F——呀，回到城镇真是太好了。\x02\x03",
            "#130F我还是第一次这么平安地从遗迹回来啊。\x01",
            "　\x02\x03",
            "#130F艾丝蒂尔、约修亚。\x01",
            "该怎么感谢你们好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F哪里，这是我们游击士应尽的义务。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F所以我就说嘛，\x01",
            "下次调查的时候就请个游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#130F哈哈，我要和钱包商量一下再说。\x02\x03",
            "#130F那么各位，我先告辞了……\x01",
            "说不定以后还会有机会再见哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x17, 0x1, 0x0, 0x1E)
    OP_8C(0x17, 90, 400)
    OP_8E(0x17, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    OP_44(0x17, 0xFF)
    TurnDirection(0x101, 0x19, 400)
    TurnDirection(0x102, 0x18, 400)
    TurnDirection(0x19, 0x101, 400)
    TurnDirection(0x18, 0x101, 400)

    ChrTalk(
        0x18,
        (
            "#141F那么……\x01",
            "我们也就此告辞了。\x02\x03",
            "#141F一开始还不太放心，\x01",
            "不过你们确实干得很不错啊。\x02\x03",
            "#147F总之谢谢你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F哼哼，这就是实力哦☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#142F丫头，不要搞错了。\x02\x03",
            "#142F和我认识的游击士比起来，\x01",
            "你们还是乳臭未干的小鬼呢。\x02\x03",
            "#142F还需要不断努力才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F唔……我会铭记在心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，\x01",
            "你们两位这就打算回杂志社去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#141F不，\x01",
            "我想今天先呆在洛连特休息一下。\x02\x03",
            "#141F因为还得起稿写新闻嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#151F而我就要去工房那儿\x01",
            "把今天的照片冲洗出来～\x02\x03",
            "#151F那么，再见哦～！\x01",
            "小艾，小约。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x19, 0x1, 0x0, 0x1D)
    OP_43(0x18, 0x1, 0x0, 0x1E)
    OP_8C(0x18, 90, 400)
    OP_8E(0x18, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    OP_44(0x18, 0xFF)
    OP_51(0x1B, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x1B, 0x3E8)
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000F这下代替老爸去做的工作都完成了……\x01",
            "　\x02\x03",
            "#000F嘿嘿～\x01",
            "比想象中还要顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，对啊。\x02\x03",
            "#010F而且，\x01",
            "原来游击士的本职不只局限于战斗，\x01",
            "现在我总算明白这道理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F你又在装酷了～\x02\x03",
            "#006F不过呢，嗯……\x01",
            "我好像也有点明白了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F前面还有很长的路要走啊……\x02\x03",
            "#019F总之，先回协会报告吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，好的。\x02\x03",
            "#004F啊，你现在感觉怎么样？\x01",
            "还会感到不舒服吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F啊，嗯……\x02\x03",
            "好像已经完全好了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8)
    Return()

    # Function_28_60C2 end

    def Function_29_678A(): pass

    label("Function_29_678A")

    Sleep(500)
    OP_8C(0x19, 90, 400)
    OP_8E(0x19, 0xAA94, 0x0, 0x104A4, 0xBB8, 0x0)
    Return()

    # Function_29_678A end

    def Function_30_67AB(): pass

    label("Function_30_67AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67D4")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x19, 0xFE, 0)
    TurnDirection(0x18, 0xFE, 0)
    OP_48()
    Jump("Function_30_67AB")

    label("loc_67D4")

    Return()

    # Function_30_67AB end

    def Function_31_67D5(): pass

    label("Function_31_67D5")

    OP_6B(2800, 1300)
    Return()

    # Function_31_67D5 end

    def Function_32_67DF(): pass

    label("Function_32_67DF")

    OP_6C(270000, 1300)
    Return()

    # Function_32_67DF end

    def Function_33_67E9(): pass

    label("Function_33_67E9")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x22)
    OP_43(0x102, 0x0, 0x0, 0x23)
    OP_43(0x0, 0x1, 0x0, 0x24)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x2)
    StopSound(0x9470, 0x30D40, 0x0)
    OP_6D(50063, 0, 24460, 8000)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x2)
    Fade(1000)
    OP_6D(48500, 0, 16400, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F时间刚刚好呢。\x02\x03",
            "既不是太早，又没有迟到。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F呜～\x01",
            "明明刚从教会的主日学校毕业……\x02\x03",
            "为了当游击士，\x01",
            "又要这么辛苦地学习，\x01",
            "真是连做梦也没想到呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F今天不是到最后了嘛。\x02\x03",
            "为了自己憧憬的理想，\x01",
            "付出这点辛苦也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F这样说也对。\x02\x03",
            "#006F………好吧！\x02\x03",
            "既然到了最后关头，\x01",
            "就鼓起干劲接受雪拉姐严格的训练吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F好像已经干劲十足了。\x02\x03",
            "那我们赶快到那边的游击士协会去吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_A2(0x203)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_33_67E9 end

    def Function_34_6A4B(): pass

    label("Function_34_6A4B")

    OP_A6(0x0)
    Sleep(5000)
    OP_8E(0xFE, 0xBCAC, 0x0, 0x3C28, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_34_6A4B end

    def Function_35_6A6B(): pass

    label("Function_35_6A6B")

    OP_A6(0x1)
    Sleep(5000)
    OP_8E(0xFE, 0xC15C, 0x0, 0x3B60, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_35_6A6B end

    def Function_36_6A8B(): pass

    label("Function_36_6A8B")

    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_36_6A8B end

    def Function_37_6A92(): pass

    label("Function_37_6A92")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x26)
    OP_43(0x102, 0x0, 0x0, 0x27)
    OP_43(0x9, 0x0, 0x0, 0x28)
    OP_43(0xA, 0x0, 0x0, 0x29)
    OP_43(0x0, 0x1, 0x0, 0x2A)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    OP_A2(0x3)
    OP_A5(0x3)

    ChrTalk(
        0x9,
        "喂～快点过来啦～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Sleep(1500)

    ChrTalk(
        0xA,
        "等、等一下嘛～！\x02",
    )

    CloseMessageWindow()
    OP_A5(0x4)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x4)
    OP_6D(49690, 0, 23330, 2500)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x4)

    ChrTalk(
        0x101,
        "#501F啊，是你们……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_A5(0x3)
    SetChrName("鲁克")

    ChrTalk(
        0x9,
        "哎哎，艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()
    SetChrName("帕特")

    ChrTalk(
        0xA,
        "啊，约修亚哥哥。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    ChrTalk(
        0x101,
        (
            "#007F真没礼貌～\x01",
            "那个『哎哎』是什么意思啊？\x02\x03",
            "#006F看你们急急忙忙的样子，\x01",
            "要去哪里玩啊？\x02\x03",
            "#006F小孩子不要随处乱跑呢～\x01",
            "外面的街道有很多魔兽在游荡哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哼，真啰嗦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "男人要干大事，\x01",
            "女人管那么多干嘛啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "又不是游击士，拽什么呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啧啧啧……\x01",
            "太嫩了！　嫩得不得了呢，鲁克！\x02\x03",
            "#006F你简直比帕赛尔农场的蔬菜还要鲜嫩！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "难、难道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿，就在刚才，\x01",
            "我已经得到游击士的资格啦。\x02\x03",
            "#502F现在的我可是如假包换的正牌游·击·士哦☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F现在还不过是见习阶段，\x01",
            "用不着在小孩子面前摆架子吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#509F喂，别给我泼冷水嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哇，太羡慕了！\x01",
            "姐姐，你们真的好了不起哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#001F呵呵，帕特真是个懂事的好孩子～\x02\x03",
            "和你那个又狂妄又任性的\x01",
            "臭小子哥哥完全不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "什、什么呀……\x01",
            "本来应该是我先当上游击士才对的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "约修亚哥哥倒也罢了，\x01",
            "居然被艾丝蒂尔之类的抢先一步……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#005F什么呀！\x01",
            "那个『之类的』是什么意思！？\x02\x03",
            "#005F首先，\x01",
            "没到１６岁是不能成为游击士的！\x02\x03",
            "#005F还在教会的主日学校学习的小孩就更不行了！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F又这么孩子气了。\x01",
            "怎么老是和小孩子认真计较……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "可恶～你给我记着！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在秘密基地进行特训之后，\x01",
            "很快我也能成为游击士的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0x9,
        "帕特，我们走！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        "啊～嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x1, 0)

    ChrTalk(
        0xA,
        "哥哥姐姐，再见了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_7075():
        OP_6D(49470, 0, 24950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7075)

    def lambda_708D():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_708D)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x3)
    OP_A2(0x4)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x3)
    OP_A5(0x4)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)

    ChrTalk(
        0x101,
        (
            "#007F真是的，鲁克那小子……\x01",
            "总是劈头就顶撞我。\x02\x03",
            "#007F会不会是因为讨厌我啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#011F不，我觉得恰恰相反。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#004F恰恰相反？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F呵呵，因为是男孩子嘛。\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#013F话说回来，\x01",
            "鲁克说的那个秘密基地……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，\x01",
            "是不是引起了共鸣呢？\x02\x03",
            "#001F约修亚小时候的纯真心灵被触动了吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#018F什么呀。\x01",
            "我想说的不是这个……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x206)
    EventEnd(0x0)
    Return()

    # Function_37_6A92 end

    def Function_38_7288(): pass

    label("Function_38_7288")

    OP_A6(0x0)
    OP_8E(0xFE, 0xC896, 0x0, 0x6BEE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC1F2, 0x0, 0x5FDC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_A3(0x0)
    OP_A6(0x0)

    label("loc_72D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_72E9")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_72D7")

    label("loc_72E9")

    Return()

    # Function_38_7288 end

    def Function_39_72EA(): pass

    label("Function_39_72EA")

    OP_A6(0x1)
    Sleep(1000)
    OP_8E(0xFE, 0xC896, 0x0, 0x6BEE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xC710, 0x0, 0x623E, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_7327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7339")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_7327")

    label("loc_7339")

    Return()

    # Function_39_72EA end

    def Function_40_733A(): pass

    label("Function_40_733A")

    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xCBE8, 0x0, 0x37A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xC3B4, 0x0, 0x3D5E, 0x1388, 0x0)
    OP_8E(0xFE, 0xBF2C, 0x0, 0x57A8, 0x1388, 0x0)
    OP_8C(0xFE, 160, 400)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x1F40)
    OP_8C(0xFE, 0, 800)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_8E(0xFE, 0xBD74, 0x0, 0x6090, 0x1B58, 0x0)
    OP_8E(0xFE, 0xBD74, 0x0, 0x9358, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x3)
    Return()

    # Function_40_733A end

    def Function_41_7422(): pass

    label("Function_41_7422")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xCBE8, 0x0, 0x37A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xC3B4, 0x0, 0x3D5E, 0x1388, 0x0)
    OP_8E(0xFE, 0xC2EC, 0x0, 0x4826, 0x1388, 0x0)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6C(12000, 2500)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_8E(0xFE, 0xC288, 0x0, 0x5410, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_A3(0x4)
    OP_A6(0x4)
    Sleep(500)
    OP_8E(0xFE, 0xBD74, 0x0, 0x6090, 0x1B58, 0x0)
    OP_8E(0xFE, 0xBD74, 0x0, 0x9358, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x4)
    Return()

    # Function_41_7422 end

    def Function_42_74D8(): pass

    label("Function_42_74D8")

    OP_A6(0x2)
    OP_6D(49800, 0, 19520, 3000)
    OP_A3(0x2)
    Return()

    # Function_42_74D8 end

    def Function_43_74F0(): pass

    label("Function_43_74F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7503")
    Call(0, 54)
    Jump("loc_7583")

    label("loc_7503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_750D")
    Jump("loc_7583")

    label("loc_750D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7520")
    Call(0, 53)
    Jump("loc_7583")

    label("loc_7520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7533")
    Call(0, 52)
    Jump("loc_7583")

    label("loc_7533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7541")
    Jump("loc_7583")

    label("loc_7541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_754F")
    Call(0, 51)
    Jump("loc_7583")

    label("loc_754F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_7559")
    Jump("loc_7583")

    label("loc_7559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_7567")
    Call(0, 50)
    Jump("loc_7583")

    label("loc_7567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_7575")
    Call(0, 44)
    Jump("loc_7583")

    label("loc_7575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_7583")
    Call(0, 49)
    Jump("loc_7583")

    label("loc_7583")

    Return()

    # Function_43_74F0 end

    def Function_44_7584(): pass

    label("Function_44_7584")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 51370, 0, 29175, 180)
    OP_43(0x101, 0x0, 0x0, 0x2D)
    OP_43(0x102, 0x0, 0x0, 0x2E)
    OP_43(0x8, 0x0, 0x0, 0x2F)
    OP_43(0x0, 0x1, 0x0, 0x30)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚！\x01",
            "还好找到你们了！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 49700, 0, 15020, 315)
    SetChrPos(0x102, 48380, 0, 15120, 0)
    SetChrPos(0x8, 49950, 0, 25270, 180)
    OP_6B(3000, 0)
    OP_6D(50250, 0, 16110, 0)
    OP_6C(156000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_0D()
    OP_8E(0x8, 0xC030, 0x0, 0x4C22, 0x1388, 0x0)

    ChrTalk(
        0x101,
        "#004F哎呀，爱娜姐姐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F发生什么事了？\x01",
            "这么着急的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F事情有点麻烦。\x02\x03",
            "我想问你们，\x01",
            "今天卡西乌斯先生在家吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，在啊。\x01",
            "他说要在家整理书本的。\x02\x03",
            "#002F嗯……发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#742F鲁克和帕特，你们认识吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F当然了。\x01",
            "刚才还见到他们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F他们怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F其实……\x01",
            "是尤妮告诉我的。\x02\x03",
            "那两个孩子\x01",
            "往北面郊外的『翡翠之塔』去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F『翡翠之塔』！？\x02\x03",
            "#004F我记得那里好像已经变成魔兽的栖息地了呀！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F嗯，很有可能。\x02\x03",
            "雪拉扎德还没回来，\x01",
            "所以现在只能拜托卡西乌斯先生去保护他们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你在说什么呀，爱娜姐姐！\x02\x03",
            "#005F如果现在不赶快去追就麻烦啦！\x01",
            "让我们去把他们带回来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#745F可是你们才刚刚成为游击士……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F爱娜小姐，\x01",
            "我觉得这次艾丝蒂尔说得对。\x02\x03",
            "#012F现在赶去的话，\x01",
            "说不定在他们到达塔之前就能追上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#744F……………………\x02\x03",
            "#742F好吧，有什么责任由我来承担。\x02\x03",
            "这是游击士协会的紧急委托。\x01",
            "一定要尽快确保孩子们的安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#742F翡翠之塔就在通往玛鲁加山道途中\x01",
            "往西拐的那个方向。\x02\x03",
            "玛鲁加山道从城镇的北边出去就是了。\x02\x03",
            "我在协会待命，\x01",
            "如果有什么问题务必与我联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_8E(0x8, 0xC31E, 0x0, 0x62B6, 0x1388, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        "#002F这么快就接到第一份任务了……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        "#005F约修亚，我们快走！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        "#012F好！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 48920, 0, 15320, 0)
    SetChrPos(0x102, 48920, 0, 15320, 0)
    OP_6C(0, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x20C)
    OP_28(0x1, 0x1, 0x1)
    OP_28(0x1, 0x1, 0x2)
    OP_28(0x1, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_44_7584 end

    def Function_45_7BAA(): pass

    label("Function_45_7BAA")

    OP_A6(0x0)

    label("loc_7BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7BBF")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_7BAD")

    label("loc_7BBF")

    OP_A6(0x0)

    label("loc_7BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7BD4")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_7BC2")

    label("loc_7BD4")

    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_45_7BAA end

    def Function_46_7BE9(): pass

    label("Function_46_7BE9")

    OP_A6(0x1)

    label("loc_7BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7BFE")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_7BEC")

    label("loc_7BFE")

    OP_A6(0x1)

    label("loc_7C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7C13")
    TurnDirection(0xFE, 0x8, 0)
    OP_48()
    Jump("loc_7C01")

    label("loc_7C13")

    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_46_7BE9 end

    def Function_47_7C28(): pass

    label("Function_47_7C28")

    OP_A6(0x5)
    OP_8E(0xFE, 0xC2F6, 0x0, 0x4902, 0x1388, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x5)
    OP_A6(0x5)
    OP_8E(0xFE, 0xC8AA, 0x0, 0x71F7, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x5)
    Return()

    # Function_47_7C28 end

    def Function_48_7C75(): pass

    label("Function_48_7C75")

    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_48_7C75 end

    def Function_49_7C7C(): pass

    label("Function_49_7C7C")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，好像忘了一件事哦。\x02\x03",
            "今天早上老爸不是吩咐过\x01",
            "我们到杂货铺买杂志的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#008F啊，差点给忘了……\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_49_7C7C end

    def Function_50_7D1D(): pass

    label("Function_50_7D1D")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#012F玛鲁加山道在城镇北面出口的方向。\x02\x03",
            "#012F顺带说说，北面出口就是\x01",
            "飞艇坪隔壁那个不起眼的小出口。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#002F我、我知道啊。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_50_7D1D end

    def Function_51_7DC9(): pass

    label("Function_51_7DC9")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，我们先到协会那里吧。\x02\x03",
            "#010F先向爱娜小姐打听一下\x01",
            "我们可以做些什么工作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000F嗯，说得对呢。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_51_7DC9 end

    def Function_52_7E69(): pass

    label("Function_52_7E69")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F可以不去工房吗？\x02\x03",
            "我们不是要去接杂志社的摄影师吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000F啊，对啊。\x01",
            "说得没错。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_52_7E69 end

    def Function_53_7EF5(): pass

    label("Function_53_7EF5")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#015F要去『翡翠之塔』的话，\x01",
            "要从城镇的北面出口走才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000F啊，没错呢。\x02\x03",
            "从飞艇坪旁边那个\x01",
            "很小的出口出城就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_7EF5 end

    def Function_54_7FA1(): pass

    label("Function_54_7FA1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_806D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_801D")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022F哎呀，我说你们想去哪儿？\x02\x03",
            "还是快点去飞艇坪那里吧。\x01",
            "说不定现在还来得及呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_806A")

    label("loc_801D")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F现在不是出城的时候，\x02\x03",
            "总之我们还是先到飞艇坪那里看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_806A")

    Jump("loc_8131")

    label("loc_806D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80DA")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022F我说你们究竟想去哪啊？\x02\x03",
            "总之我们还是先去旅馆那里确认一下情况吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_80DA")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F现在不是出城的时候，\x02\x03",
            "总之我们还是先去旅馆那里确认一下情况再说吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8131")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_7FA1 end

    def Function_55_814D(): pass

    label("Function_55_814D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8160")
    Call(0, 63)
    Jump("loc_81E8")

    label("loc_8160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_816A")
    Jump("loc_81E8")

    label("loc_816A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_817D")
    Call(0, 62)
    Jump("loc_81E8")

    label("loc_817D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8190")
    Call(0, 61)
    Jump("loc_81E8")

    label("loc_8190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_819E")
    Jump("loc_81E8")

    label("loc_819E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_81AC")
    Call(0, 56)
    Jump("loc_81E8")

    label("loc_81AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_81BA")
    Call(0, 56)
    Jump("loc_81E8")

    label("loc_81BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_81C8")
    Call(0, 56)
    Jump("loc_81E8")

    label("loc_81C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_81D6")
    Call(0, 56)
    Jump("loc_81E8")

    label("loc_81D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_81E4")
    Call(0, 56)
    Jump("loc_81E8")

    label("loc_81E4")

    Call(0, 56)

    label("loc_81E8")

    Return()

    # Function_55_814D end

    def Function_56_81E9(): pass

    label("Function_56_81E9")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_8277")

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，我们先到协会那里吧。\x02\x03",
            "#010F先向爱娜小姐打听一下\x01",
            "我们可以做些什么工作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000F嗯，说得对呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_846D")

    label("loc_8277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_82E4")

    ChrTalk(
        0x102,
        (
            "#010F已经傍晚了啊。\x02\x03",
            "#010F父亲还在等我们呢，\x01",
            "我们还是早点回家吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_846D")

    label("loc_82E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_8375")

    ChrTalk(
        0x102,
        (
            "#012F玛鲁加山道在城镇北面出口的方向。\x02\x03",
            "#012F顺带说说，北面出口就是\x01",
            "飞艇坪隔壁那个不起眼的小出口。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F我、我知道啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_846D")

    label("loc_8375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_83F7")

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "总之我们还是先回家吧。\x02\x03",
            "#010F我们要把成为游击士的事告诉父亲呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，那倒也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_846D")

    label("loc_83F7")


    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "很快就要开始研修了。\x02\x03",
            "#010F我们还是先到\x01",
            "南面的游击士协会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#007F哎～没办法啦。\x02",
    )

    CloseMessageWindow()

    label("loc_846D")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_81E9 end

    def Function_57_8489(): pass

    label("Function_57_8489")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "很快就要开始研修了。\x02\x03",
            "#010F我们还是先到\x01",
            "南面的游击士协会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#007F哎～没办法啦。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_57_8489 end

    def Function_58_856C(): pass

    label("Function_58_856C")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "总之我们还是先回家吧。\x02\x03",
            "#010F我们要把成为游击士的事告诉父亲呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，那倒也是。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_58_856C end

    def Function_59_8651(): pass

    label("Function_59_8651")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F玛鲁加山道在城镇北面出口的方向。\x02\x03",
            "#012F顺带说说，北面出口就是\x01",
            "飞艇坪隔壁那个不起眼的小出口。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F我、我知道啊。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_59_8651 end

    def Function_60_8745(): pass

    label("Function_60_8745")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经傍晚了啊。\x02\x03",
            "#010F父亲还在等我们呢，\x01",
            "我们还是早点回家吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0, 22000, 0, 40000, 0)
    SetChrPos(0x1, 22000, 0, 40000, 0)
    SetChrPos(0x2, 22000, 0, 40000, 0)
    SetChrPos(0x3, 22000, 0, 40000, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_60_8745 end

    def Function_61_8815(): pass

    label("Function_61_8815")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F可以不去工房吗？\x02\x03",
            "我们不是要去接杂志社的摄影师吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000F啊，对啊。\x01",
            "说得没错。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_61_8815 end

    def Function_62_88A1(): pass

    label("Function_62_88A1")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#015F要去『翡翠之塔』的话，\x01",
            "要从城镇的北面出口走才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000F啊，没错呢。\x02\x03",
            "从飞艇坪旁边那个\x01",
            "很小的出口出城就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_62_88A1 end

    def Function_63_894D(): pass

    label("Function_63_894D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_8A19")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89C9")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022F哎呀，我说你们想去哪儿？\x02\x03",
            "还是快点去飞艇坪那里吧。\x01",
            "说不定现在还来得及呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A16")

    label("loc_89C9")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F现在不是出城的时候，\x02\x03",
            "总之我们还是先到飞艇坪那里看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A16")

    Jump("loc_8AD9")

    label("loc_8A19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A86")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022F我说你们究竟想去哪啊？\x02\x03",
            "总之我们还是先去旅馆那里确认一下情况吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AD9")

    label("loc_8A86")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F现在不是出城的时候，\x02\x03",
            "总之我们还是先去旅馆那里确认一下情况吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AD9")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_63_894D end

    def Function_64_8AF5(): pass

    label("Function_64_8AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B08")
    Call(0, 70)
    Jump("loc_8B79")

    label("loc_8B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_8B12")
    Jump("loc_8B79")

    label("loc_8B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B25")
    Call(0, 69)
    Jump("loc_8B79")

    label("loc_8B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B33")
    Jump("loc_8B79")

    label("loc_8B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_8B41")
    Call(0, 65)
    Jump("loc_8B79")

    label("loc_8B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8B4F")
    Call(0, 65)
    Jump("loc_8B79")

    label("loc_8B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_8B59")
    Jump("loc_8B79")

    label("loc_8B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_8B67")
    Call(0, 65)
    Jump("loc_8B79")

    label("loc_8B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8B75")
    Call(0, 65)
    Jump("loc_8B79")

    label("loc_8B75")

    Call(0, 65)

    label("loc_8B79")

    Return()

    # Function_64_8AF5 end

    def Function_65_8B7A(): pass

    label("Function_65_8B7A")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_8C08")

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，我们先到协会那里吧。\x02\x03",
            "#010F先向爱娜小姐打听一下\x01",
            "我们可以做些什么工作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000F嗯，说得对呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D64")

    label("loc_8C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8C75")

    ChrTalk(
        0x102,
        (
            "#010F已经傍晚了啊。\x02\x03",
            "#010F父亲还在等我们呢，\x01",
            "我们还是早点回家吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D64")

    label("loc_8C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_8C7F")
    Jump("loc_8D64")

    label("loc_8C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8D01")

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "总之我们还是先回家吧。\x02\x03",
            "#010F我们要把成为游击士的事告诉父亲呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，那倒也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D64")

    label("loc_8D01")


    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "很快就要开始研修了。\x02\x03",
            "#010F我们快点去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#007F哎～没办法啦。\x02",
    )

    CloseMessageWindow()

    label("loc_8D64")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_65_8B7A end

    def Function_66_8D80(): pass

    label("Function_66_8D80")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "很快就要开始研修了。\x02\x03",
            "#010F我们快点去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#007F哎～没办法啦。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_66_8D80 end

    def Function_67_8E50(): pass

    label("Function_67_8E50")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔。\x01",
            "总之我们还是先回家吧。\x02\x03",
            "#010F我们要把成为游击士的事告诉父亲呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#000F嗯，那倒也是。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_67_8E50 end

    def Function_68_8F35(): pass

    label("Function_68_8F35")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，等一下。\x02\x03",
            "#010F我们还没到里农先生那里\x01",
            "买《利贝尔通讯》呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#000F啊，忘了忘了。\x01",
            "那我们快点去杂货铺吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0, 32000, 0, 67800, 90)
    SetChrPos(0x1, 32000, 0, 67800, 90)
    SetChrPos(0x2, 32000, 0, 67800, 90)
    SetChrPos(0x3, 32000, 0, 67800, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    EventEnd(0x0)
    Return()

    # Function_68_8F35 end

    def Function_69_9028(): pass

    label("Function_69_9028")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#010F可以不去工房吗？\x02\x03",
            "我们不是要去接杂志社的摄影师吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，对啊。\x01",
            "说得没错。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_69_9028 end

    def Function_70_90AD(): pass

    label("Function_70_90AD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_9179")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9129")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022F哎呀，我说你们想去哪儿？\x02\x03",
            "还是快点去飞艇坪那里吧。\x01",
            "说不定现在还来得及呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9176")

    label("loc_9129")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F现在不是出城的时候，\x02\x03",
            "总之我们还是先到飞艇坪那里看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9176")

    Jump("loc_923D")

    label("loc_9179")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91E6")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(
        0x103,
        (
            "#022F我说你们究竟想去哪啊？\x02\x03",
            "总之我们还是先去旅馆那里确认一下情况吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_923D")

    label("loc_91E6")

    TurnDirection(0x103, 0x1, 400)

    ChrTalk(
        0x103,
        (
            "#022F现在不是出城的时候，\x02\x03",
            "总之我们还是先去旅馆那里确认一下情况再说吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_923D")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_70_90AD end

    def Function_71_9259(): pass

    label("Function_71_9259")

    EventBegin(0x0)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrPos(0x102, 54640, 0, 43670, 0)
    SetChrPos(0x101, 55690, 0, 43940, 0)
    OP_6D(55160, 1000, 47020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(314000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_92E2():
        OP_6D(55160, 9000, 47020, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92E2)
    OP_6C(44000, 7000)
    Fade(1000)
    OP_6D(55310, 0, 45740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１０７５年\x01",
            "　由利贝尔王家、七耀教会\x01",
            "　以及洛连特市共同建造。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１９２年\x01",
            "　百日战役中，被围攻洛连特的\x01",
            "　埃雷波尼亚帝国军队炮击而倒塌。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１９７年\x01",
            "　在市民的协力下得以重建。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#010F#3P每次看到这座钟楼，\x01",
            "我都会这样想……\x02\x03",
            "在战争中被破坏之后，\x01",
            "还能修复到如此程度。\x02\x03",
            "洛连特市民的气概真是令人赞叹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#500F#2P…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F#3P艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#2P……我说，约修亚。\x02\x03",
            "在雪拉姐来之前，\x01",
            "我们上去看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#3P到钟楼上面？\x01",
            "我倒是没什么意见……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#2P那我们就上去吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_71_9259 end

    def Function_72_95A7(): pass

    label("Function_72_95A7")

    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    AddParty(0x2, 0xFF)
    OP_A2(0x301)
    EventBegin(0x0)
    SetMapFlags(0x1)
    SetChrPos(0x102, 51920, 0, 49090, 180)
    SetChrPos(0x101, 53010, 0, 50110, 270)
    SetChrPos(0x103, 56060, 0, 43300, 270)
    OP_6C(45000, 0)
    OP_6A(0x102)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x0, 0x0, 0x4A)
    OP_8E(0x102, 0xCA12, 0x0, 0xAC9E, 0xBB8, 0x0)
    ClearMapFlags(0x1)
    OP_43(0x102, 0x0, 0x0, 0x49)
    OP_6D(55290, 0, 43570, 1500)
    OP_6A(0x0)
    ClearMapFlags(0x1)

    ChrTalk(
        0x103,
        (
            "#021F嘿嘿，你们两个。\x01",
            "刚才的气氛真不错嘛。\x02\x03",
            "姐姐我啊～\x01",
            "都觉得不好意思了呢㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F#4P哎……\x02\x03",
            "#014F难、难道刚才在偷看……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F什么呀，说得这么难听。\x02\x03",
            "只不过是仰头看时间的时候\x01",
            "不小心瞥见了而已。\x02\x03",
            "#021F啊～要是身上带有\x01",
            "导力照相机的话那就更完美了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F#4P呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F真是的～在说什么呀。\x01",
            "不过是单纯的肢体接触而已嘛。\x02\x03",
            "和被喝醉了的雪拉姐抱着\x01",
            "是一样的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(
        0x102,
        "#017F#4P………呼……………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#501F嗯？怎么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F唉，你这孩子啊，\x01",
            "真是一点也不好玩。\x02\x03",
            "#020F算了。\x01",
            "你已经和莱娜小姐打了招呼吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#000F……嗯。\x01",
            "我向她许了愿呢。\x02\x03",
            "祈愿她守护着老爸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F那么，这样就一定没问题的。\x02\x03",
            "莱娜小姐的保佑\x01",
            "可以和空之女神相媲美呢。\x02\x03",
            "卡西乌斯老师\x01",
            "一定会平安无事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊哈哈，\x01",
            "我觉得这样说好像有点太夸张了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4P那样说的话，\x01",
            "雪拉姐姐曾经见过\x01",
            "艾丝蒂尔的母亲是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是的……\x01",
            "我小时候还受过她很多照顾呢。\x02\x03",
            "那是我还在剧团里的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#4P剧团？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是巡回马戏团的剧团哦。\x01",
            "雪拉姐是舞者呢。\x02\x03",
            "很久以前来洛连特\x01",
            "巡回演出的时候和我们认识的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F准确地说是１２年前。\x01",
            "那时我１１岁，艾丝蒂尔４岁。\x02\x03",
            "可能是缘分吧，后来我成为游击士的时候，\x01",
            "就被卡西乌斯老师收做徒弟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4P原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F好了，\x01",
            "这些闲话等到以后再慢慢聊吧……\x02\x03",
            "咱们也该起程去柏斯了。\x02\x03",
            "因为定期船停航，\x01",
            "要去柏斯就不得不走陆路。\x02\x03",
            "首先，我们先去\x01",
            "通往柏斯地区的边界关所威尔特桥吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4P是西边的米尔西街道的终点对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F那么，我们出发吧～！\x02",
    )

    CloseMessageWindow()
    OP_28(0x52, 0x4, 0x2)
    OP_28(0x52, 0x4, 0x4)
    OP_28(0x52, 0x1, 0x1)
    OP_3F(0x32A, 1)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x400000)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0xA)
    Return()

    # Function_72_95A7 end

    def Function_73_9C7C(): pass

    label("Function_73_9C7C")

    OP_8E(0x102, 0xD50C, 0x0, 0xA690, 0xBB8, 0x0)
    OP_8C(0x102, 45, 400)
    Return()

    # Function_73_9C7C end

    def Function_74_9C98(): pass

    label("Function_74_9C98")

    SetChrFlags(0x101, 0x4)
    OP_8E(0x101, 0xC9B8, 0x0, 0xC468, 0xBB8, 0x0)
    OP_8E(0x101, 0xCAF8, 0x0, 0xAC94, 0xBB8, 0x0)
    OP_8E(0x101, 0xD41C, 0x0, 0xAB86, 0xBB8, 0x0)
    ClearChrFlags(0x101, 0x4)
    TurnDirection(0x101, 0x103, 400)
    Return()

    # Function_74_9C98 end

    def Function_75_9CE6(): pass

    label("Function_75_9CE6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　玛鲁加山道一侧出口\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_75_9CE6 end

    def Function_76_9D2F(): pass

    label("Function_76_9D2F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　洛连特飞艇坪\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_76_9D2F end

    def Function_77_9D72(): pass

    label("Function_77_9D72")

    SetPlaceName(0x4)
    Return()

    # Function_77_9D72 end

    def Function_78_9D76(): pass

    label("Function_78_9D76")

    SetPlaceName(0x2)
    Return()

    # Function_78_9D76 end

    def Function_79_9D7A(): pass

    label("Function_79_9D7A")

    SetPlaceName(0x6)
    Return()

    # Function_79_9D7A end

    def Function_80_9D7E(): pass

    label("Function_80_9D7E")

    SetPlaceName(0x5)
    Return()

    # Function_80_9D7E end

    def Function_81_9D82(): pass

    label("Function_81_9D82")

    SetPlaceName(0x7)
    Return()

    # Function_81_9D82 end

    def Function_82_9D86(): pass

    label("Function_82_9D86")

    SetPlaceName(0x8)
    Return()

    # Function_82_9D86 end

    def Function_83_9D8A(): pass

    label("Function_83_9D8A")

    SetPlaceName(0x3)
    Return()

    # Function_83_9D8A end

    def Function_84_9D8E(): pass

    label("Function_84_9D8E")

    SetPlaceName(0xA)
    Return()

    # Function_84_9D8E end

    def Function_85_9D92(): pass

    label("Function_85_9D92")

    SetPlaceName(0xC)
    Return()

    # Function_85_9D92 end

    def Function_86_9D96(): pass

    label("Function_86_9D96")

    SetPlaceName(0x9)
    Return()

    # Function_86_9D96 end

    def Function_87_9D9A(): pass

    label("Function_87_9D9A")

    SetPlaceName(0x15)
    Return()

    # Function_87_9D9A end

    def Function_88_9D9E(): pass

    label("Function_88_9D9E")

    SetPlaceName(0x16)
    Return()

    # Function_88_9D9E end

    def Function_89_9DA2(): pass

    label("Function_89_9DA2")

    SetPlaceName(0x17)
    Return()

    # Function_89_9DA2 end

    SaveToFile()

Try(main)
