import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉扎德'),
    TXT(0x02, '奥利维尔'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '金'),
    TXT(0x05, '尤莉亚上尉'),
    TXT(0x06, '摩尔根将军'),
    TXT(0x07, '操舵士勒克司'),
    TXT(0x08, '测量师艾柯'),
    TXT(0x09, '通信员利昂'),
    TXT(0x0A, '拉赛尔博士'),
    TXT(0x0B, '阿加特'),
    TXT(0x0C, '提妲'),
    TXT(0x0D, '凯文神父'),
    TXT(0x0E, '穆拉少校'),
    TXT(0x0F, '奈尔'),
    TXT(0x10, '朵洛希'),
    TXT(0x11, '亲卫队队员'),
    TXT(0x12, '亲卫队队员'),
    TXT(0x13, '亲卫队队员'),
    TXT(0x14, '空贼雷古'),
    TXT(0x15, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0310.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/E0310_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xDBA0
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT26/CH20362._CH', 'ED6_DT26/CH20362P._CP'),
        ('ED6_DT06/CH20113._CH', 'ED6_DT06/CH20113P._CP'),
        ('ED6_DT26/CH20367._CH', 'ED6_DT26/CH20367P._CP'),
        ('ED6_DT26/CH20368._CH', 'ED6_DT26/CH20368P._CP'),
        ('ED6_DT26/CH20369._CH', 'ED6_DT26/CH20369P._CP'),
        ('ED6_DT27/CH03840._CH', 'ED6_DT27/CH03840P._CP'),
        ('ED6_DT27/CH03850._CH', 'ED6_DT27/CH03850P._CP'),
        ('ED6_DT27/CH03860._CH', 'ED6_DT27/CH03860P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT26/CH20500._CH', 'ED6_DT26/CH20500P._CP'),
        ('ED6_DT27/CH03573._CH', 'ED6_DT27/CH03573P._CP'),
        ('ED6_DT27/CH03210._CH', 'ED6_DT27/CH03210P._CP'),
        ('ED6_DT26/CH20418._CH', 'ED6_DT26/CH20418P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT27/CH03001._CH', 'ED6_DT27/CH03001P._CP'),
        ('ED6_DT27/CH03011._CH', 'ED6_DT27/CH03011P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
    ]

# id: 0x10002 offset: 0x192
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -1040,
            z                   = 100,
            y                   = 99020,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            x                   = -3400,
            z                   = 100,
            y                   = 98950,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = 1300,
            z                   = 100,
            y                   = 98950,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1760,
            z                   = 300,
            y                   = 96770,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196626,
            chipIndex           = 18,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 3480,
            z                   = 0,
            y                   = -840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 3480,
            z                   = 0,
            y                   = -840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -2920,
            z                   = 2000,
            y                   = 49050,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 2670,
            z                   = 0,
            y                   = 100010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x412
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x412
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 3470,
            y           = -1000,
            z           = -840,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -2920,
            y           = 1000,
            z           = 49050,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -900,
            y           = -500,
            z           = 500,
            range       = -3110,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000898,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000002F,
        ),
    )

# id: 0x10005 offset: 0x472
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x472
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_6CE',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4A1',
    )

    SetChrChipByIndex(0x000A, 20)
    SetChrPos(0x000A, -910, 2000, 89640, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_55C',
    )

    SetChrPos(0x0016, 1860, 2000, 89340, 0)
    ClearChrFlags(0x0016, 0x0080)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)
    SetChrPos(0x0017, 2460, 2000, 88510, 0)
    ClearChrFlags(0x0017, 0x0080)
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, 3480, 0, -840, 270)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x001A, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_52A',
    )

    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrFlags(0x000C, 0x0004)
    ClearChrFlags(0x000C, 0x0080)
    SetChrChipByIndex(0x000C, 18)

    def _loc_52A(): pass

    label('loc_52A')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_559',
    )

    SetChrChipByIndex(0x0015, 24)
    SetChrPos(0x0015, 130, 2000, 91480, 0)
    ClearChrFlags(0x0015, 0x0080)
    CreateThread(0x0015, 0x00, 0x00, 0x0002)

    def _loc_559(): pass

    label('loc_559')

    Jump('loc_6CB')

    def _loc_55C(): pass

    label('loc_55C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_5E8',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrPos(0x000F, -2660, 0, 99090, 315)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 11)
    ClearChrFlags(0x000F, 0x0010)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    SetChrPos(0x000C, -840, 0, 97770, 45)
    SetChrSubChip(0x000C, 0)
    SetChrChipByIndex(0x000C, 4)
    ClearChrFlags(0x000C, 0x0010)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5E5',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 3280, 0, 260, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_5E5(): pass

    label('loc_5E5')

    Jump('loc_6CB')

    def _loc_5E8(): pass

    label('loc_5E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_63E',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_63B',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 3280, 0, 260, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_63B(): pass

    label('loc_63B')

    Jump('loc_6CB')

    def _loc_63E(): pass

    label('loc_63E')

    SetChrPos(0x000E, -920, 0, 97790, 0)
    ClearChrFlags(0x000E, 0x0010)
    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x000E, 13)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)
    SetChrPos(0x0010, 370, 0, 97940, 45)
    ClearChrFlags(0x0010, 0x0010)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x0010, 12)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    SetChrPos(0x000C, -1600, 2000, 91460, 90)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000C, 0x0080)
    SetChrChipByIndex(0x0015, 24)
    SetChrPos(0x0015, 130, 2000, 91480, 270)
    ClearChrFlags(0x0015, 0x0080)
    CreateThread(0x0015, 0x00, 0x00, 0x0002)
    def _loc_6CB(): pass

    label('loc_6CB')

    Jump('loc_92C')

    def _loc_6CE(): pass

    label('loc_6CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_733',
    )

    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_730',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_730(): pass

    label('loc_730')

    Jump('loc_92C')

    def _loc_733(): pass

    label('loc_733')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_79D',
    )

    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000C, 0x0010)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_79A',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_79A(): pass

    label('loc_79A')

    Jump('loc_92C')

    def _loc_79D(): pass

    label('loc_79D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_848',
    )

    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x000F, -1740, 0, 97950, 0)
    SetChrChipByIndex(0x000F, 11)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    SetChrPos(0x0010, 530, 0, 98030, 90)
    SetChrChipByIndex(0x0010, 12)
    ClearChrFlags(0x0010, 0x0010)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_845',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    def _loc_845(): pass

    label('loc_845')

    Jump('loc_92C')

    def _loc_848(): pass

    label('loc_848')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_8D6',
    )

    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x000F, -1740, 0, 97950, 0)
    SetChrChipByIndex(0x000F, 11)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8B8',
    )

    SetChrPos(0x0012, 770, 2000, 89910, 0)
    ClearChrFlags(0x0012, 0x0080)
    SetChrChipByIndex(0x0012, 28)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)

    def _loc_8B8(): pass

    label('loc_8B8')

    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    Jump('loc_92C')

    def _loc_8D6(): pass

    label('loc_8D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_8E5',
    )

    ClearChrFlags(0x0018, 0x0080)

    Jump('loc_92C')

    def _loc_8E5(): pass

    label('loc_8E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_92C',
    )

    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrFlags(0x000C, 0x0004)
    ClearChrFlags(0x000C, 0x0080)
    SetChrChipByIndex(0x000C, 18)
    SetChrPos(0x000A, -2290, 2000, 91270, 0)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0018, 0x0080)

    def _loc_92C(): pass

    label('loc_92C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_94D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FF)
    OP_A3(0x10F0)
    Event(0, 0x0029)

    Jump('loc_C0A')

    def _loc_94D(): pass

    label('loc_94D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_96E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FF)
    OP_A3(0x10F1)
    Event(1, 0x000C)

    Jump('loc_C0A')

    def _loc_96E(): pass

    label('loc_96E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_98F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x77),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FF)
    OP_A3(0x10F2)
    Event(1, 0x000D)

    Jump('loc_C0A')

    def _loc_98F(): pass

    label('loc_98F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9B0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FF)
    OP_A3(0x10F3)
    Event(1, 0x000E)

    Jump('loc_C0A')

    def _loc_9B0(): pass

    label('loc_9B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9D1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FF)
    OP_A3(0x10F4)
    Event(1, 0x0010)

    Jump('loc_C0A')

    def _loc_9D1(): pass

    label('loc_9D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9F2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x85),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FF)
    OP_A3(0x10F5)
    Event(1, 0x0011)

    Jump('loc_C0A')

    def _loc_9F2(): pass

    label('loc_9F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_A11',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    Jump('loc_C0A')

    def _loc_A11(): pass

    label('loc_A11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_A30',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x0010)

    Jump('loc_C0A')

    def _loc_A30(): pass

    label('loc_A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_A4F',
    )

    OP_A3(0x10F2)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0011)

    Jump('loc_C0A')

    def _loc_A4F(): pass

    label('loc_A4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_A6E',
    )

    OP_A3(0x10F3)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0012)

    Jump('loc_C0A')

    def _loc_A6E(): pass

    label('loc_A6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_A8D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 0x0013)

    Jump('loc_C0A')

    def _loc_A8D(): pass

    label('loc_A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_AAC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 0x0014)

    Jump('loc_C0A')

    def _loc_AAC(): pass

    label('loc_AAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_ACB',
    )

    OP_A3(0x10F6)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0017)

    Jump('loc_C0A')

    def _loc_ACB(): pass

    label('loc_ACB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Return,
        ),
        'loc_AEA',
    )

    OP_A3(0x10F7)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0018)

    Jump('loc_C0A')

    def _loc_AEA(): pass

    label('loc_AEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 0, 0x10F8)),
            Expr.Return,
        ),
        'loc_B09',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x23),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F8)
    SetMapFlags(0x10000000)
    Event(0, 0x0019)

    Jump('loc_C0A')

    def _loc_B09(): pass

    label('loc_B09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 1, 0x10F9)),
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 2, 0x10FA)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B2F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F9)
    OP_A3(0x10FA)
    SetMapFlags(0x10000000)
    Event(0, 0x0024)

    Jump('loc_C0A')

    def _loc_B2F(): pass

    label('loc_B2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 1, 0x10F9)),
            Expr.Return,
        ),
        'loc_B4E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F9)
    SetMapFlags(0x10000000)
    Event(0, 0x0022)

    Jump('loc_C0A')

    def _loc_B4E(): pass

    label('loc_B4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 2, 0x10FA)),
            Expr.Return,
        ),
        'loc_B6D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FA)
    SetMapFlags(0x10000000)
    Event(0, 0x0023)

    Jump('loc_C0A')

    def _loc_B6D(): pass

    label('loc_B6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 3, 0x10FB)),
            Expr.Return,
        ),
        'loc_B8C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FB)
    SetMapFlags(0x10000000)
    Event(0, 0x0025)

    Jump('loc_C0A')

    def _loc_B8C(): pass

    label('loc_B8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 4, 0x10FC)),
            Expr.Return,
        ),
        'loc_BAB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FC)
    SetMapFlags(0x10000000)
    Event(0, 0x0026)

    Jump('loc_C0A')

    def _loc_BAB(): pass

    label('loc_BAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 5, 0x10FD)),
            Expr.Return,
        ),
        'loc_BCA',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FD)
    SetMapFlags(0x10000000)
    Event(0, 0x0027)

    Jump('loc_C0A')

    def _loc_BCA(): pass

    label('loc_BCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 6, 0x10FE)),
            Expr.Return,
        ),
        'loc_BE9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10FE)
    SetMapFlags(0x10000000)
    Event(0, 0x0028)

    Jump('loc_C0A')

    def _loc_BE9(): pass

    label('loc_BE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 7, 0x1A1F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 0, 0x1A20)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 1, 0x1A21)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 2, 0x1A22)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C0A',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000A)

    def _loc_C0A(): pass

    label('loc_C0A')

    Return()

# id: 0x0001 offset: 0xC0B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C29',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C29(): pass

    label('loc_C29')

    Call(0, 0x0009)
    Call(0, 0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C4F',
    )

    OP_B2(0x00, 0x00, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)

    def _loc_C4F(): pass

    label('loc_C4F')

    Jump('loc_C63')

    def _loc_C52(): pass

    label('loc_C52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C63',
    )

    OP_B2(0x00, 0x00, 0x0080)

    def _loc_C63(): pass

    label('loc_C63')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C8C',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C99')

    def _loc_C8C(): pass

    label('loc_C8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C99',
    )

    OP_22(0x007A, 0x01, 0x46)

    def _loc_C99(): pass

    label('loc_C99')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 4, 0x1E24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CC4',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x007A, 0x01, 0x46)

    def _loc_CC4(): pass

    label('loc_CC4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CEA',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CEA(): pass

    label('loc_CEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_D08',
    )

    OP_D2(0x000600FE, 0x00060103, 0x1D)
    OP_D2(0x000600FC, 0x00060101, 0x1E)

    Jump('loc_D73')

    def _loc_D08(): pass

    label('loc_D08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_D12',
    )

    Jump('loc_D73')

    def _loc_D12(): pass

    label('loc_D12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_D30',
    )

    OP_D2(0x000600FE, 0x00060103, 0x1D)
    OP_D2(0x000600FC, 0x00060101, 0x1E)

    Jump('loc_D73')

    def _loc_D30(): pass

    label('loc_D30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_D53',
    )

    OP_D2(0x000600FE, 0x00060103, 0x1D)
    OP_D2(0x000600FC, 0x00060101, 0x1E)
    OP_1B(0x0A, 0x00, 0x002E)

    Jump('loc_D73')

    def _loc_D53(): pass

    label('loc_D53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D73',
    )

    OP_D2(0x000600FE, 0x00060103, 0x1D)
    OP_D2(0x000600FC, 0x00060101, 0x1E)

    def _loc_D73(): pass

    label('loc_D73')

    Return()

# id: 0x0002 offset: 0xD74
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D99',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_EDB')

    def _loc_D99(): pass

    label('loc_D99')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DB2',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_EDB')

    def _loc_DB2(): pass

    label('loc_DB2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DCB',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_EDB')

    def _loc_DCB(): pass

    label('loc_DCB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DE4',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_EDB')

    def _loc_DE4(): pass

    label('loc_DE4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DFD',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_EDB')

    def _loc_DFD(): pass

    label('loc_DFD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E16',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_EDB')

    def _loc_E16(): pass

    label('loc_E16')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E2F',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_EDB')

    def _loc_E2F(): pass

    label('loc_E2F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E48',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_EDB')

    def _loc_E48(): pass

    label('loc_E48')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E61',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_EDB')

    def _loc_E61(): pass

    label('loc_E61')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E7A',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_EDB')

    def _loc_E7A(): pass

    label('loc_E7A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E93',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_EDB')

    def _loc_E93(): pass

    label('loc_E93')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EAC',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_EDB')

    def _loc_EAC(): pass

    label('loc_EAC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EC5',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_EDB')

    def _loc_EC5(): pass

    label('loc_EC5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EDB',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_EDB(): pass

    label('loc_EDB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EF0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_EDB')

    def _loc_EF0(): pass

    label('loc_EF0')

    Return()

# id: 0x0003 offset: 0xEF1
@scena.Code('func_03_EF1')
def func_03_EF1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F91',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390319V#1164F<FIXME>……あ、皆さん。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390320V#1160F探索の方はどうですか？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390321V#1011Fうん、えっと……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0013)

    Return()

    def _loc_F91(): pass

    label('loc_F91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_23ED',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_FF6'),
        (0x00000001, 'loc_23AF'),
        (0x00000002, 'loc_23E7'),
        (-1, 'loc_23EA'),
    )

    def _loc_FF6(): pass

    label('loc_FF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 2, 0x2232)),
            Expr.Return,
        ),
        'loc_15F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0448, 1, 0x2241)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 5, 0x22A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1468',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390322V#1162F啊，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390323V中枢塔的情况\n',
            '怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x045B, 0, 0x22D8)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10E0',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390324V#175F<FIXME>……それが…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390325V#176F突然《怪盗紳士》と\n',
            '名乗る男に歓迎されまして。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x010F, 400)

    Jump('loc_114C')

    def _loc_10E0(): pass

    label('loc_10E0')

    ChrTalk(
        0x0101,
        (
            '#0010390326V#1003F嗯，一下子就受到了\n',
            '执行者的欢迎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390327V#1007F……那个『怪盗绅士』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    def _loc_114C(): pass

    label('loc_114C')

    ChrTalk(
        0x000A,
        (
            '#0060390328V#1163F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390329V#1040F不过他答应我们\n',
            '收手了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390330V所以科洛丝也可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '#0060390331V#1167F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390332V#1382F呼，感觉心里的\n',
            '一块石头落地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390333V#1016F哈哈，我能理解你的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390334V布卢布兰不知为什么，\n',
            '对科洛丝很执着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B1',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390335V#176F<FIXME>まったく……冗談ではない。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390336V#178F今度殿下の前に現れたら、\n',
            'この手で引っ捕らえてやるつもりだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390337V#1016F<FIXME>あ、あはははは……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390338V#1035F不过，接下来肯定还有\n',
            '其他执行者在等着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390339V#1042F提高警觉继续探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_141A')

    def _loc_13B1(): pass

    label('loc_13B1')

    ChrTalk(
        0x0102,
        (
            '#0020390340V#1035F不过，接下来肯定还有\n',
            '其他执行者在等着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390341V#1042F提高警觉继续探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_141A(): pass

    label('loc_141A')

    ChrTalk(
        0x000A,
        (
            '#0060390342V#1162F嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390343V#1006F嗯！　明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22A5)

    Jump('loc_14E5')

    def _loc_1468(): pass

    label('loc_1468')

    ChrTalk(
        0x000A,
        (
            '#0060390344V#1162F他能够收手\n',
            '真是个好消息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390345V不过还是不能\n',
            '掉以轻心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390346V请大家\n',
            '一定要小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_14E5(): pass

    label('loc_14E5')

    Jump('loc_15F4')

    def _loc_14E8(): pass

    label('loc_14E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1595',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390347V#1167F他能够收手，\n',
            '说实话，我真是松了口气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390348V#1162F不过，还是不能\n',
            '掉以轻心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390349V各位，接下来也请\n',
            '提高警觉继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_15F4')

    def _loc_1595(): pass

    label('loc_1595')

    ChrTalk(
        0x000A,
        (
            '#0060390350V#1162F接下来的战斗应该还是\n',
            '不能够掉以轻心的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390351V提起精神前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15F4(): pass

    label('loc_15F4')

    Jump('loc_23AC')

    def _loc_15F7(): pass

    label('loc_15F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1A32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 7, 0x22D7)),
            Expr.Ez,
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17A8',
    )

    ChrTurnDirection(0x000A, 0x010F, 400)

    ChrTalk(
        0x000A,
        (
            '#0060390352V#1160F<FIXME>あ、ユリアさん……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100390353V#178F<FIXME>申し訳ありません、殿下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390354Vこちらの指揮は\n',
            'しばらくお任せします。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390355V#1168F<FIXME>ふふ、大丈夫です。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390356Vクルーの皆さんのおかげで\n',
            '修復作業も順調ですし……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390357Vお祖母様に言って\n',
            'アルセイユを借り出したのは私です。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390358V#1160F私にも、これくらいのことは\n',
            'させてください。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22D7)

    Jump('loc_1A2F')

    def _loc_17A8(): pass

    label('loc_17A8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18BF',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390359V#1167F<FIXME>これから飛翔機関の\n',
            '負荷試験を行うところです。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390360Vこれに成功すれば\n',
            '何とか飛べる状態に\n',
            'なるそうですから……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390361V#1162Fみなさんも、どうか\n',
            '無事に戻ってきてください。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390362Vそして全員そろって\n',
            '地上に帰りましょう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A2F')

    def _loc_18BF(): pass

    label('loc_18BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19AD',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390363V#1167F接下来在舰桥\n',
            '好像要进行重要的测试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390364V看来修复工程也快要\n',
            '接近尾声了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390365V#1162F希望我们能完成使命，\n',
            '全体成员一起回到地面上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390366V各位……\n',
            '即使到最后一刻都请不要放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_1A2F')

    def _loc_19AD(): pass

    label('loc_19AD')

    ChrTalk(
        0x0105,
        (
            '#0060390367V#1160F希望我们能完成使命，\n',
            '全体成员一起回到地面上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390368V那么，诸位……\n',
            '即使到最后一刻都请不要放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A2F(): pass

    label('loc_1A2F')

    Jump('loc_23AC')

    def _loc_1A32(): pass

    label('loc_1A32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1B93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B26',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390369V#1160F空贼团的各位\n',
            '也能平安无事真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390370V他们好像来得\n',
            '比我们还要早。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390371V关于浮游都市\n',
            '他们或许会有什么\n',
            '有用的情报也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390372V有机会过去拜访一下\n',
            '他们的话可能也很有意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_1B90')

    def _loc_1B26(): pass

    label('loc_1B26')

    ChrTalk(
        0x000A,
        (
            '#0060390373V#1160F空贼团的各位好像\n',
            '比我们还要早。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390374V他们或许会有什么\n',
            '有用的情报也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B90(): pass

    label('loc_1B90')

    Jump('loc_23AC')

    def _loc_1B93(): pass

    label('loc_1B93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_2238',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 6, 0x22A6)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_201D',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000A,
        (
            '#0060390375V#1168F乔丝特小姐……\n',
            '欢迎来到埃尔赛尤号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390376V很不巧正值修复作业中，\n',
            '无法好好地招待您……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390377V请把这里当作自己的船，\n',
            '不要拘束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390378V#414F嗯、嗯……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390379V#415F嘿嘿，受到这样的欢迎，\n',
            '感觉身上都痒起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010390380V#1019F真、真不卫生……\n',
            '你几天没洗澡了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010B, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x010B, 0x0101, 400)

    ChrTalk(
        0x010B,
        (
            '#0090390381V#216F笨、笨蛋！\n',
            '我不是这个意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390382V#1016F对、对不起对不起。\n',
            '我知道的，只是顺口说出来而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390383V你想，一提到空贼\n',
            '总有种肮脏的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390384V#212F哼，清一色的男人才会这样吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390385V#210F我们打扫和洗衣服的工作都是\n',
            '我在做，堪称完美。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390386V说清楚一点，\n',
            '就是毫不逊色于这艘船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x010B, 400)

    ChrTalk(
        0x0102,
        (
            '#0020390387V#1040F的确……\n',
            '飞船内确实出人意料地整洁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390388V#211F嘿嘿，没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010390389V#1015F哦～原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390390V#1019F……等等，约修亚为什么\n',
            '要帮乔丝特说话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020390391V#1044F咦……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390392V我、我没有帮她说话啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390393V#1167F咳、咳………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390394V#1382F总、总之希望\n',
            '大家都能和睦相处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390395V在这种情况下，\n',
            '合作比什么都重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)
    OP_A2(0x22A6)

    Jump('loc_2235')

    def _loc_201D(): pass

    label('loc_201D')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_209E',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390396V#1382F总、总之希望\n',
            '大家珍惜船上的和谐氛围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390395V在这种情况下，\n',
            '合作比什么都重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2235')

    def _loc_209E(): pass

    label('loc_209E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2186',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390398V#1167F不管过去发生过什么，\n',
            '现在都处于同样的境遇下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390399V与空贼团的各位互相帮助，\n',
            '我想是理所当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390400V#1160F尤莉亚小姐那边\n',
            '我会去解释的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390401V各位请专注于\n',
            '都市的探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_2235')

    def _loc_2186(): pass

    label('loc_2186')

    ChrTalk(
        0x000A,
        (
            '#0060390398V#1167F不管过去发生过什么，\n',
            '现在都处于同样的境遇下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390403V#1160F与空贼团的各位互相帮助，\n',
            '我想是理所当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390401V各位请专注于\n',
            '都市的探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2235(): pass

    label('loc_2235')

    Jump('loc_23AC')

    def _loc_2238(): pass

    label('loc_2238')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_23AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2313',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390405V#1162F现在船员们正在\n',
            '确认受损的位置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390406V等到确认完成，就应该会\n',
            '展开修复工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390407V#1167F接下来不知道还会\n',
            '发生些什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390408V总之要尽快\n',
            '飞起来才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_23AC')

    def _loc_2313(): pass

    label('loc_2313')

    ChrTalk(
        0x000A,
        (
            '#0060390409V#1162F等确认完损伤情况，就应该会\n',
            '展开修复工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390410V接下来不知道还会\n',
            '发生些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390411V应该要尽快恢复\n',
            '飞行能力才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AC(): pass

    label('loc_23AC')

    Jump('loc_23EA')

    def _loc_23AF(): pass

    label('loc_23AF')

    ChrTalk(
        0x000A,
        (
            '#0060390412V#1160F明白了。\n',
            '要更换成员是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)

    Jump('loc_23EA')

    def _loc_23E7(): pass

    label('loc_23E7')

    Jump('loc_23EA')

    def _loc_23EA(): pass

    label('loc_23EA')

    Jump('loc_3230')

    def _loc_23ED(): pass

    label('loc_23ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_2D75',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2452'),
        (0x00000001, 'loc_2D38'),
        (0x00000002, 'loc_2D6F'),
        (-1, 'loc_2D72'),
    )

    def _loc_2452(): pass

    label('loc_2452')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_281B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 3, 0x1E4B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_279C',
    )

    ChrTalk(
        0x000A,
        (
            '#0060390413V#043F在最后之塔上等待我们的执行者……\n',
            '似乎是那个玲呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390414V就像艾丝蒂尔所说的，\n',
            '真希望她快点醒悟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390415V#1003F虽然不知道我们的话\n',
            '她能听进去多少……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390416V#1002F不过我们会尽力一试的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390417V#1035F是啊……\n',
            '只能尽力而为了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25E1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390418V#051F嗯，就这么做吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390419V要救那个女孩子，\n',
            '也没其他的办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272F')

    def _loc_25E1(): pass

    label('loc_25E1')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_265B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390420V#070F按照游击士的精神，\n',
            '就应该这么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390421V要救那个女孩子，\n',
            '也没其他的办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272F')

    def _loc_265B(): pass

    label('loc_265B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26C4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390422V#020F嗯，就这么做吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390423V要救那个女孩子，\n',
            '也没其他的办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272F')

    def _loc_26C4(): pass

    label('loc_26C4')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_272F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390424V#1067F本来就应该这么做呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390425V要救那个女孩子，\n',
            '也没其他的办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_272F(): pass

    label('loc_272F')

    ChrTalk(
        0x000A,
        (
            '#0060390426V#047F我们的声音一定\n',
            '可以传达到玲的心中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390427V#040F现在就相信那个女孩的心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E4B)

    Jump('loc_2818')

    def _loc_279C(): pass

    label('loc_279C')

    ChrTalk(
        0x000A,
        (
            '#0060390428V#047F我们的声音一定\n',
            '可以传达到玲的心中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390429V#040F现在就相信那个女孩的心，\n',
            '然后一切尽力而为吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2818(): pass

    label('loc_2818')

    Jump('loc_2D35')

    def _loc_281B(): pass

    label('loc_281B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_2B1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2ABB',
    )

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '#0060340395V#040F啊……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340396V刚才收到了玛诺利亚\n',
            '守备队的联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340397V特蕾莎老师和孩子们\n',
            '已经安全避难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340398V#1004F啊，真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060340399V#047F嗯，大家都很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340400V#1007F呼～太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340401V#1040F嗯……\n',
            '暂时可以安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340402V#1043F不过，塔还是那副样子……\n',
            '依然不能掉以轻心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030340403V#026F嗯，这时候高兴\n',
            '还为时过早。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340404V#022F现在就调整好心情\n',
            '向塔出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340405V#1002F嗯……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340406V那么我们先走了，科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060340407V#042F嗯，需要我的话\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340408V那么各位，\n',
            '一定要小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_2B1A')

    def _loc_2ABB(): pass

    label('loc_2ABB')

    ChrTalk(
        0x000A,
        (
            '#0060340409V#040F院长和孤儿院的孩子们\n',
            '似乎都顺利地避难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340410V暂时可以\n',
            '放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B1A(): pass

    label('loc_2B1A')

    Jump('loc_2D35')

    def _loc_2B1D(): pass

    label('loc_2B1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_2D35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CDC',
    )

    ChrTalk(
        0x000A,
        (
            '#0060340411V#040F蔡斯的守备队\n',
            '也正在努力呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340412V目前防卫线\n',
            '似乎还没被打破。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340413V#1011F是吗……\n',
            '也就是说可以暂时放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BFF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340414V#561F可是可是，我还是很担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BFF(): pass

    label('loc_2BFF')

    ChrTalk(
        0x0102,
        (
            '#0020340415V#1042F我们还是赶紧\n',
            '去调查塔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340416V对蔡斯的攻击\n',
            '应该是声东击西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080340417V#072F是啊。\n',
            '塔一定是要害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340418V现在应该优先\n',
            '考虑制服执行者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340419V#1002F嗯，我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_2D35')

    def _loc_2CDC(): pass

    label('loc_2CDC')

    ChrTalk(
        0x000A,
        (
            '#0060340420V#040F蔡斯的防卫线\n',
            '据说还没被打破。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340421V我们也赶紧\n',
            '去压制塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D35(): pass

    label('loc_2D35')

    Jump('loc_2D72')

    def _loc_2D38(): pass

    label('loc_2D38')

    ChrTalk(
        0x000A,
        (
            '#0060340422V#040F明白了。\n',
            '要更换成员是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)

    Jump('loc_2D72')

    def _loc_2D6F(): pass

    label('loc_2D6F')

    Jump('loc_2D72')

    def _loc_2D72(): pass

    label('loc_2D72')

    Jump('loc_3230')

    def _loc_2D75(): pass

    label('loc_2D75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_3230',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 1, 0x1A21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31B9',
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x000A,
        (
            '#0060310364V#040F哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310365V莫非你\n',
            '心情平静不下来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310366V#1000F嗯，有一点。\n',
            '总是无法静静地坐在座位上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310367V#045F对了，你在定期船上\n',
            '也一直会散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310368V#1008F啊哈哈……\n',
            '被你这么一说倒也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310369V举止得体地坐着\n',
            '总觉得绑手绑脚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310370V#048F呵呵……\n',
            '果然像是艾丝蒂尔会说的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310371V不过在『埃尔赛尤』上\n',
            '你不必担心这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310372V#1011F咦？怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310373V#047F虽然所属于王室，\n',
            '不过这艘船是巡洋舰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310374V和普通的飞行客船\n',
            '运动性能相差悬殊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310375V#040F用最大战速飞行的话\n',
            '要想站着都很困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310376V#1004F这、这么厉害啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310377V#048F呵呵，你一定会吓一跳的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310378V简直像遭遇暴风雨一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310379V#1004F是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310380V#1015F那么，现在一定是\n',
            '暴风雨前的寂静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310381V#047F嗯，你说得没错……\n',
            '有可能只是片刻的平静。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310382V#040F如果你要在舰内参观，\n',
            '就要趁现在哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310383V#1006F哦，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310384V那么我就去\n',
            '继续散步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310385V#040F嗯，那么回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A21)

    Jump('loc_3230')

    def _loc_31B9(): pass

    label('loc_31B9')

    ChrTalk(
        0x000A,
        (
            '#0060310386V#040F正如艾丝蒂尔所说，\n',
            '现在是暴风雨前的寂静。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310387V如果要在舰内参观的话，\n',
            '或许只能趁现在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3230(): pass

    label('loc_3230')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x3234
@scena.Code('func_04_3234')
def func_04_3234():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3295'),
        (0x00000001, 'loc_3677'),
        (0x00000002, 'loc_36A3'),
        (-1, 'loc_36A6'),
    )

    def _loc_3295(): pass

    label('loc_3295')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 5, 0x1E25)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3619',
    )

    ChrTalk(
        0x0012,
        (
            '#0050340423V#052F怎么了？你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340424V还在这种地方\n',
            '转来转去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340425V#1000F嗯，还想再整顿\n',
            '一下装备嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340426V倒是阿加特你，\n',
            '为什么会在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '#0050340427V#050F要支援你们的话，\n',
            '这里是最方便的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340428V在舰桥上可以完全\n',
            '掌握外界的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340429V#1028F哦～这些话听起来\n',
            '嘴上功夫倒是很厉害嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340430V#1040F拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050340431V#050F可别勉强啊。\n',
            '不管怎么说对手都不简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_348A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240159V#062F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_353B')

    def _loc_348A(): pass

    label('loc_348A')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34C6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340433V#022F嗯，有必要特别小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_353B')

    def _loc_34C6(): pass

    label('loc_34C6')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3502',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340434V#072F嗯，应该慎重地前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_353B')

    def _loc_3502(): pass

    label('loc_3502')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_353B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340435V#042F是……我们会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_353B(): pass

    label('loc_353B')

    ChrTalk(
        0x0101,
        (
            '#0010340436V#1002F阿加特也是……\n',
            '麻烦你做好准备哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340437V也不知道什么时候\n',
            '就需要借助你的力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050340438V#051F不用你说我也会这么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340439V好了，你们要努力一点，\n',
            '我会从这里好好地欣赏的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E25)

    Jump('loc_3674')

    def _loc_3619(): pass

    label('loc_3619')

    ChrTalk(
        0x0012,
        (
            '#0050340440V#050F我会从这里\n',
            '观察调查的情况的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340441V需要我的时候\n',
            '尽管开口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3674(): pass

    label('loc_3674')

    Jump('loc_36A6')

    def _loc_3677(): pass

    label('loc_3677')

    ChrTalk(
        0x0012,
        (
            '#0050340442V#050F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)

    Jump('loc_36A6')

    def _loc_36A3(): pass

    label('loc_36A3')

    Jump('loc_36A6')

    def _loc_36A6(): pass

    label('loc_36A6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x36AA
@scena.Code('func_05_36AA')
def func_05_36AA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_37B0',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000C)
    ClearChrFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3746',
    )

    Jump('loc_3788')

    def _loc_3746(): pass

    label('loc_3746')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3762',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3788')

    def _loc_3762(): pass

    label('loc_3762')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_377E',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3788')

    def _loc_377E(): pass

    label('loc_377E')

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3788(): pass

    label('loc_3788')

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000C, 0x0010)

    Jump('loc_37B3')

    def _loc_37B0(): pass

    label('loc_37B0')

    TalkBegin(0x00FE)
    def _loc_37B3(): pass

    label('loc_37B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_3A3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_384C',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390430V#170F<FIXME>……ああ、諸君。\n',
            '探索の方はどうだろうか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390321V#1011F<FIXME>うん、えっと……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0013)

    Return()

    def _loc_384C(): pass

    label('loc_384C')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_38AA'),
        (0x00000001, 'loc_39EA'),
        (0x00000002, 'loc_3A34'),
        (-1, 'loc_3A37'),
    )

    def _loc_38AA(): pass

    label('loc_38AA')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_394E',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390431V#178F接下来要进行\n',
            '飞翔引擎的驱动测试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390432V待殿下回来的时候，\n',
            '我们一定会让船恢复可飞行的状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390433V请您耐心期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39E7')

    def _loc_394E(): pass

    label('loc_394E')

    ChrTalk(
        0x000C,
        (
            '#0100390438V#178F接下来要进行\n',
            '飞翔引擎的驱动测试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390439V等各位回来的时候，\n',
            '我们一定会让船恢复可飞行的状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390440V你们就耐心期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39E7(): pass

    label('loc_39E7')

    Jump('loc_3A37')

    def _loc_39EA(): pass

    label('loc_39EA')

    ChrTalk(
        0x000C,
        (
            '#0100390435V#170F<FIXME>ああ……\n',
            '探索要員を入れ替えるのだな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)

    Jump('loc_3A37')

    def _loc_3A34(): pass

    label('loc_3A34')

    Jump('loc_3A37')

    def _loc_3A37(): pass

    label('loc_3A37')

    Jump('loc_584C')

    def _loc_3A3A(): pass

    label('loc_3A3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_3E18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 3, 0x22AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BF5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3ABB',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390436V#170F空贼团那帮家伙\n',
            '已经得救了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390437V刚才，从他们的飞艇上\n',
            '传来了通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B1A')

    def _loc_3ABB(): pass

    label('loc_3ABB')

    ChrTalk(
        0x000C,
        (
            '#0100390441V#170F空贼团那帮家伙\n',
            '已经得救了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390442V从他们的飞艇上\n',
            '刚传来了通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B1A(): pass

    label('loc_3B1A')

    ChrTalk(
        0x0101,
        (
            '#0010390443V#1011F啊，已经取得联络了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#0100390444V#170F嗯，他们也在\n',
            '忙着修船呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390445V#176F虽然和他们合作\n',
            '让人有点无法接受……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390446V不过在这种状况下也没办法。\n',
            '我也要遵从指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)
    OP_A2(0x22AB)

    Jump('loc_3E15')

    def _loc_3BF5(): pass

    label('loc_3BF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3D2A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C97',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390447V#170F空贼团的各位\n',
            '似乎也在忙着修船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390448V#176F想不到会在这种地方\n',
            '遭遇同样的困境……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390449V命运真是讽刺呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D27')

    def _loc_3C97(): pass

    label('loc_3C97')

    ChrTalk(
        0x000C,
        (
            '#0100390450V#170F空贼团的各位\n',
            '似乎也在忙着修船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390451V呼，想不到会在这种地方\n',
            '#176F遇上同样的困境……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390452V命运真是讽刺呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D27(): pass

    label('loc_3D27')

    Jump('loc_3E15')

    def _loc_3D2A(): pass

    label('loc_3D2A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DA6',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390453V#170F从空贼团的飞艇上\n',
            '传来了通讯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390454V目前应该先确认一下\n',
            '有没有物资不足的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E15')

    def _loc_3DA6(): pass

    label('loc_3DA6')

    ChrTalk(
        0x000C,
        (
            '#0100390455V#170F从空贼团的飞艇上\n',
            '刚传来了通讯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390456V目前应该先确认一下\n',
            '有没有物资不足的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E15(): pass

    label('loc_3E15')

    Jump('loc_584C')

    def _loc_3E18(): pass

    label('loc_3E18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_4163',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_400C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 2, 0x22AA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F60',
    )

    ChrTurnDirection(0x000C, 0x010B, 0)

    ChrTalk(
        0x000C,
        (
            '#0100390457V#178F哟，你就是乔丝特啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390458V本来我是不愿意和\n',
            '罪犯一起合作的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390459V不过在这种状况下也没办法。\n',
            '我就特别准许你登舰吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390460V不过你也要认真\n',
            '帮大家一起工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390461V和其他船员一起\n',
            '帮忙作业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390462V#212F嗯、嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22AA)

    Jump('loc_4009')

    def _loc_3F60(): pass

    label('loc_3F60')

    ChrTurnDirection(0x000C, 0x010B, 0)

    ChrTalk(
        0x000C,
        (
            '#0100390463V#178F因为现在是这样的状况。\n',
            '就特别准许你登舰吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390464V不过你也要认真\n',
            '帮大家一起工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390465V有空闲的话就去帮忙\n',
            '船员们的作业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4009(): pass

    label('loc_4009')

    Jump('loc_4160')

    def _loc_400C(): pass

    label('loc_400C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40F1',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390466V#178F哟，各位。\n',
            '你们救了空贼小姑娘吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390467V#176F和罪犯一起合作\n',
            '罪犯一起合作的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390459V不过在这种状况下也没办法。\n',
            '我就特别准许你登舰吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390469V#178F毕竟也不能把她\n',
            '丢在野外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_4160')

    def _loc_40F1(): pass

    label('loc_40F1')

    ChrTalk(
        0x000C,
        (
            '#0100390470V#170F对空贼小姑娘，\n',
            '我就特别准许你登舰吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390471V不过，当然也会为此\n',
            '要求她好好地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4160(): pass

    label('loc_4160')

    Jump('loc_584C')

    def _loc_4163(): pass

    label('loc_4163')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_4426',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4245',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390472V#170F现在最大的问题\n',
            '就是修复要用到的材料……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390473V总之准备先把船体的碎片\n',
            '再加工后使用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390474V虽然说这毕竟只是应急措施，\n',
            '不过应该能充分具备\n',
            '可以承受飞行的强度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_42B0')

    def _loc_4245(): pass

    label('loc_4245')

    ChrTalk(
        0x000C,
        (
            '#0100390475V#170F修复工作所用的材料\n',
            '准备使用船体的碎片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390476V回收部队已经在船外\n',
            '展开活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42B0(): pass

    label('loc_42B0')

    Jump('loc_4423')

    def _loc_42B3(): pass

    label('loc_42B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43A9',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390477V#178F修复工作所用的材料\n',
            '准备使用船体的碎片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390478V当前，队员们\n',
            '正在进行回收工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390479V用人力来回收\n',
            '或许相当地辛苦，\n',
            '不过现在也没有其他的办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390480V抱歉，如果你们哪位有空的话\n',
            '请过去帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_4423')

    def _loc_43A9(): pass

    label('loc_43A9')

    ChrTalk(
        0x000C,
        (
            '#0100390481V#178F为了进行修复工作，\n',
            '队员们\n',
            '正在回收船体的碎片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390482V抱歉，如果你们哪位有空的话\n',
            '请过去帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4423(): pass

    label('loc_4423')

    Jump('loc_584C')

    def _loc_4426(): pass

    label('loc_4426')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_490A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4734',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 0, 0x1E48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_461F',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390483V#178F在下一座塔上等待的\n',
            '是手持巨大镰刀的少女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390484V她一定就是那个在背后\n',
            '指挥凯诺娜事件的人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390485V#176F本来应该由我亲自前去\n',
            '对其进行制裁的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390486V现在这个责任就\n',
            '落到殿下的肩上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390487V#178F为了女王陛下，\n',
            '请一并替在下完成使命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060390488V#040F虽然我不认为自己\n',
            '能替代尤莉亚小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390489V不过我会和大家携手\n',
            '一同努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x000C, 29)
    SetChrSubChip(0x000C, 0)
    OP_99(0x000C, 0x00, 0x01, 0x000005DC)

    ChrTalk(
        0x000C,
        (
            '#0100390490V#172F是！　祝您旗开得胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000C, 0x01, 0x00, 0x000005DC)
    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)
    OP_A2(0x1E48)

    Jump('loc_4731')

    def _loc_461F(): pass

    label('loc_461F')

    ChrTalk(
        0x000C,
        (
            '#0100390491V#178F在下一座塔上等待的\n',
            '是手持巨大镰刀的少女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390485V#176F本来应该由我亲自前去\n',
            '对其进行制裁的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390493V现在这个责任就\n',
            '落到殿下的肩上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x000C, 29)
    SetChrSubChip(0x000C, 0)
    OP_99(0x000C, 0x00, 0x01, 0x000005DC)

    ChrTalk(
        0x000C,
        (
            '#0100390494V#172F为了女王陛下，\n',
            '请一并替在下完成使命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000C, 0x01, 0x00, 0x000005DC)
    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)
    OP_A2(0x0008)

    def _loc_4731(): pass

    label('loc_4731')

    Jump('loc_4907')

    def _loc_4734(): pass

    label('loc_4734')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_486B',
    )

    ChrTalk(
        0x000C,
        (
            '#0100390495V#178F下一个执行者是手持巨大镰刀的少女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390496V她一定就是那个在背后\n',
            '指挥凯诺娜事件的人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390497V#176F本来应该是\n',
            '由我来制裁她的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390498V现在就把这个任务交给\n',
            '接受了陛下命令的各位吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390499V#178F我尤莉亚的心愿就托付给各位了。\n',
            '……请各位尽量放手去做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_4907')

    def _loc_486B(): pass

    label('loc_486B')

    ChrTalk(
        0x000C,
        (
            '#0100390500V#178F既然是扰乱过王都秩序的对手，\n',
            '本该由我亲自来制裁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390501V现在就把这个任务交给\n',
            '接受了陛下命令的各位吧。\n',
            '请各位尽量放手去做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4907(): pass

    label('loc_4907')

    Jump('loc_584C')

    def _loc_490A(): pass

    label('loc_490A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_4B5D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49D1',
    )

    ChrTalk(
        0x000C,
        (
            '#0100340362V#170F卢安近郊的守备队\n',
            '顺利抵达了玛诺利亚村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340363V他们报告说街道附近的居民\n',
            '也已经完成避难了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340364V似乎总算是度过了\n',
            '危急的状况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_4A3C')

    def _loc_49D1(): pass

    label('loc_49D1')

    ChrTalk(
        0x000C,
        (
            '#0100340362V#170F卢安近郊的守备队\n',
            '顺利抵达了玛诺利亚村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340364V似乎总算是度过了\n',
            '危急的状况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A3C(): pass

    label('loc_4A3C')

    Jump('loc_4B5A')

    def _loc_4A3F(): pass

    label('loc_4A3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AEF',
    )

    ChrTalk(
        0x000C,
        (
            '#0100340367V#170F卢安近郊的守备队\n',
            '顺利抵达了玛诺利亚村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340368V他们报告说街道附近的居民\n',
            '也已经完成避难了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340369V总算是度过了\n',
            '危急的状况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_4B5A')

    def _loc_4AEF(): pass

    label('loc_4AEF')

    ChrTalk(
        0x000C,
        (
            '#0100340367V#170F卢安近郊的守备队\n',
            '顺利抵达了玛诺利亚村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340371V似乎总算是度过了\n',
            '危急的状况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B5A(): pass

    label('loc_4B5A')

    Jump('loc_584C')

    def _loc_4B5D(): pass

    label('loc_4B5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_4DDA',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C24',
    )

    ChrTalk(
        0x000C,
        (
            '#0100340372V#178F在蔡斯近郊\n',
            '守备队正在奋战中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340373V我们赌上王国军人的名誉，\n',
            '一定会保障城镇的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340374V请不必担心──\n',
            '殿下请专注于塔的调查上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_4C9F')

    def _loc_4C24(): pass

    label('loc_4C24')

    ChrTalk(
        0x000C,
        (
            '#0100340375V#178F我们赌上王国军人的名誉，\n',
            '一定会保障城镇的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340376V请不必担心──\n',
            '现在请专注于塔的调查上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C9F(): pass

    label('loc_4C9F')

    Jump('loc_4DD7')

    def _loc_4CA2(): pass

    label('loc_4CA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D5E',
    )

    ChrTalk(
        0x000C,
        (
            '#0100340377V#178F在蔡斯近郊\n',
            '王国军的守备队正在奋战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340378V我们赌上王国军人的名誉，\n',
            '一定会保障蔡斯市区的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340379V请不必担心。\n',
            '各位请专注于塔的调查上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_4DD7')

    def _loc_4D5E(): pass

    label('loc_4D5E')

    ChrTalk(
        0x000C,
        (
            '#0100340380V#178F我们赌上王国军人的名誉，\n',
            '一定会保障蔡斯的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340379V请不必担心。\n',
            '各位请专注于塔的调查上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DD7(): pass

    label('loc_4DD7')

    Jump('loc_584C')

    def _loc_4DDA(): pass

    label('loc_4DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_50FF',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FCD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 7, 0x1E47)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F61',
    )

    ChrTalk(
        0x000C,
        (
            '#0100340382V#170F殿下您可能已经知道了，\n',
            '下降到地面的时候请使用\n',
            '货舱的货物升降机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340383V人员的配置已经完成，\n',
            '应该随时都能使用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340384V敌人的实力也相当强──\n',
            '请一定要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060340385V#040F谢谢你，尤莉亚小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340386V我不在时埃尔赛尤号就\n',
            '拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x000C, 29)
    SetChrSubChip(0x000C, 0)
    OP_99(0x000C, 0x00, 0x01, 0x000005DC)

    ChrTalk(
        0x000C,
        (
            '#0100340387V#172F是！　请交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000C, 0x01, 0x00, 0x000005DC)
    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)
    OP_A2(0x1E47)

    Jump('loc_4FCA')

    def _loc_4F61(): pass

    label('loc_4F61')

    ChrTalk(
        0x000C,
        (
            '#0100340388V#170F下降到地面的时候请使用\n',
            '货舱的货物升降机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340389V那么，殿下──\n',
            '请保重贵体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FCA(): pass

    label('loc_4FCA')

    Jump('loc_50FC')

    def _loc_4FCD(): pass

    label('loc_4FCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5087',
    )

    ChrTalk(
        0x000C,
        (
            '#0100340390V#170F下降到地面的时候请使用\n',
            '货舱的货物升降机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340391V人员的配置已经完成，\n',
            '应该随时都能使用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340392V我期待着各位的奋斗。\n',
            '──愿女神保佑各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_50FC')

    def _loc_5087(): pass

    label('loc_5087')

    ChrTalk(
        0x000C,
        (
            '#0100340390V#170F下降到地面的时候请使用\n',
            '货舱的货物升降机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340394V人员的配置已经完成，\n',
            '应该随时都能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50FC(): pass

    label('loc_50FC')

    Jump('loc_584C')

    def _loc_50FF(): pass

    label('loc_50FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_584C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 5, 0x1A6D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53E0',
    )

    ChrTalk(
        0x000C,
        (
            '#0100310388V#170F这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310389V『埃尔赛尤』\n',
            '还让你满意吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310390V#1001F嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310391V女王陛下的船\n',
            '果然就是不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310392V#171F承蒙夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310393V新型引擎总算是赶上了，\n',
            '我们也才刚放下心来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310394V#176F本来没想到过会有\n',
            '这么大规模的作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310395V#1007F的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310396V谁也想象不到\n',
            '龙竟然会出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310397V#178F嗯，对我们来说\n',
            '是个完全未知的对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310398V虽说有万全的计划，\n',
            '不过也绝不能掉以轻心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310399V考虑到万一的情况，\n',
            '应该做好最坏的打算才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310400V#1015F我们就是为了以防万一\n',
            '才被叫来的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310401V#175F嗯，我们想尽可能地\n',
            '不借助各位的力量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310402V现在只有女神知道\n',
            '结果会是怎样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A6D)

    Jump('loc_584C')

    def _loc_53E0(): pass

    label('loc_53E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 0, 0x1A70)),
            Expr.Return,
        ),
        'loc_57B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 6, 0x1A6E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5738',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310403V#1011F啊，对了，尤莉亚小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310404V奈尔那家伙说想要\n',
            '采访尤莉亚小姐哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310405V#173F采访……？　找我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310406V#1006F嗯，他说想让市民们了解\n',
            '亲卫队的真实一面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310407V那家伙对工作很正经，\n',
            '我觉得这个理由也挺可信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310408V#176F关于他的报导方式，\n',
            '我也早就有所了解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310409V不然我也不会允许\n',
            '他随行采访了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310410V#1015F嗯，就事论事的话，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310411V#175F我也完全赞同\n',
            '他所选择的题材……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310412V可是，这次\n',
            '我得谢绝他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310413V#1004F咦……？　你不是赞成吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310414V#176F迄今为止，我对其他通讯社\n',
            '的采访请求都是婉言谢绝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310415V所以不能只对他的\n',
            '通讯社开放特例。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310416V#1007F嗯、嗯……也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310417V#170F抱歉，\n',
            '请这么转达他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310418V对于报道本身，\n',
            '我是很期待的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310419V#1015F哦，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)
    OP_A2(0x1A6E)

    Jump('loc_57B3')

    def _loc_5738(): pass

    label('loc_5738')

    ChrTalk(
        0x000C,
        (
            '#0100310420V#176F很遗憾，我不能接受利贝尔\n',
            '通讯社的提议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310421V虽然我赞同他的题材，\n',
            '不过毕竟以前从未有过先例。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_57B3(): pass

    label('loc_57B3')

    Jump('loc_584C')

    def _loc_57B6(): pass

    label('loc_57B6')

    ChrTalk(
        0x000C,
        (
            '#0100310422V#170F一旦发现古代龙，\n',
            '作战就随之展开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310423V我们也会竭尽全力，\n',
            '但是结果不得而知。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310424V艾丝蒂尔也请\n',
            '做好万全的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_584C(): pass

    label('loc_584C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5863',
    )

    SetChrSubChip(0x000C, 0)
    TalkEnd(0x000C)

    Jump('loc_5866')

    def _loc_5863(): pass

    label('loc_5863')

    TalkEnd(0x00FE)

    def _loc_5866(): pass

    label('loc_5866')

    Return()

# id: 0x0006 offset: 0x5867
@scena.Code('func_06_5867')
def func_06_5867():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#030F◆无台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x5887
@scena.Code('func_07_5887')
def func_07_5887():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_58FE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Return,
        ),
        'loc_58B9',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    Jump('loc_58FB')

    def _loc_58B9(): pass

    label('loc_58B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_58E0',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0xFFFF,
        ),
    )

    Jump('loc_58FB')

    def _loc_58E0(): pass

    label('loc_58E0')

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    def _loc_58FB(): pass

    label('loc_58FB')

    Jump('loc_597C')

    def _loc_58FE(): pass

    label('loc_58FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_5921',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    Jump('loc_597C')

    def _loc_5921(): pass

    label('loc_5921')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_5942',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_597C')

    def _loc_5942(): pass

    label('loc_5942')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_5963',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x0007,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0008,
            0xFFFF,
        ),
    )

    Jump('loc_597C')

    def _loc_5963(): pass

    label('loc_5963')

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    def _loc_597C(): pass

    label('loc_597C')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_59B3',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0015, 0x0080)

    def _loc_59B3(): pass

    label('loc_59B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_5AC6',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_59E2',
    )

    SetChrChipByIndex(0x000A, 20)
    SetChrPos(0x000A, -910, 2000, 89640, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_59E2(): pass

    label('loc_59E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_5A54',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Return,
        ),
        'loc_5A51',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5A22',
    )

    SetChrChipByIndex(0x000C, 18)
    SetChrSubChip(0x000C, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrFlags(0x000C, 0x0004)
    ClearChrFlags(0x000C, 0x0080)

    def _loc_5A22(): pass

    label('loc_5A22')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5A51',
    )

    SetChrChipByIndex(0x0015, 24)
    SetChrPos(0x0015, 130, 2000, 91480, 0)
    ClearChrFlags(0x0015, 0x0080)
    CreateThread(0x0015, 0x00, 0x00, 0x0002)

    def _loc_5A51(): pass

    label('loc_5A51')

    Jump('loc_5AC3')

    def _loc_5A54(): pass

    label('loc_5A54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_5A8F',
    )

    OP_8C(0x000A, 45, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5A8C',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 3280, 0, 260, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_5A8C(): pass

    label('loc_5A8C')

    Jump('loc_5AC3')

    def _loc_5A8F(): pass

    label('loc_5A8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_5AC3',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5AC0',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 3280, 0, 260, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_5AC0(): pass

    label('loc_5AC0')

    Jump('loc_5AC3')

    def _loc_5AC3(): pass

    label('loc_5AC3')

    Jump('loc_5B83')

    def _loc_5AC6(): pass

    label('loc_5AC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_5AF3',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5AF0',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_5AF0(): pass

    label('loc_5AF0')

    Jump('loc_5B83')

    def _loc_5AF3(): pass

    label('loc_5AF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_5B20',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B1D',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_5B1D(): pass

    label('loc_5B1D')

    Jump('loc_5B83')

    def _loc_5B20(): pass

    label('loc_5B20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_5B4D',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B4A',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_5B4A(): pass

    label('loc_5B4A')

    Jump('loc_5B83')

    def _loc_5B4D(): pass

    label('loc_5B4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_5B83',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B83',
    )

    SetChrPos(0x0012, 770, 2000, 89910, 0)
    ClearChrFlags(0x0012, 0x0080)
    SetChrChipByIndex(0x0012, 28)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)

    def _loc_5B83(): pass

    label('loc_5B83')

    OP_0D()

    Return()

# id: 0x0008 offset: 0x5B85
@scena.Code('func_08_5B85')
def func_08_5B85():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BA9',
    )

    OP_10(0x00, 0x00)
    OP_10(0x09, 0x00)
    OP_10(0x07, 0x01)
    OP_10(0x0B, 0x00)
    OP_10(0x0A, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x08, 0x01)

    Jump('loc_5C01')

    def _loc_5BA9(): pass

    label('loc_5BA9')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BCD',
    )

    OP_10(0x09, 0x00)
    OP_10(0x07, 0x00)
    OP_10(0x00, 0x01)
    OP_10(0x0B, 0x00)
    OP_10(0x0A, 0x00)
    OP_10(0x08, 0x00)
    OP_10(0x01, 0x01)

    Jump('loc_5C01')

    def _loc_5BCD(): pass

    label('loc_5BCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_5BEC',
    )

    OP_10(0x00, 0x00)
    OP_10(0x07, 0x00)
    OP_10(0x09, 0x00)
    OP_10(0x0B, 0x01)
    OP_10(0x0A, 0x01)
    OP_10(0x08, 0x00)
    OP_10(0x01, 0x00)

    Jump('loc_5C01')

    def _loc_5BEC(): pass

    label('loc_5BEC')

    OP_10(0x00, 0x00)
    OP_10(0x07, 0x00)
    OP_10(0x09, 0x01)
    OP_10(0x0B, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x08, 0x00)
    OP_10(0x0A, 0x01)

    def _loc_5C01(): pass

    label('loc_5C01')

    Return()

# id: 0x0009 offset: 0x5C02
@scena.Code('func_09_5C02')
def func_09_5C02():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CB2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_5C44',
    )

    OP_B1('E0310_1')
    OP_71(0x0003, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)

    Jump('loc_5CAF')

    def _loc_5C44(): pass

    label('loc_5C44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_5C75',
    )

    OP_B1('E0310_1')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_72(0x000F, 0x0004)

    Jump('loc_5CAF')

    def _loc_5C75(): pass

    label('loc_5C75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 7, 0x22AF)),
            Expr.Return,
        ),
        'loc_5C8D',
    )

    OP_B1('E0310_2')
    OP_71(0x0019, 0x0004)

    Jump('loc_5CAF')

    def _loc_5C8D(): pass

    label('loc_5C8D')

    OP_B1('E0310_1')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)

    def _loc_5CAF(): pass

    label('loc_5CAF')

    Jump('loc_5E5B')

    def _loc_5CB2(): pass

    label('loc_5CB2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 4, 0x1E24)),
            Expr.Return,
        ),
        'loc_5CEF',
    )

    OP_B1('E0310_1')
    OP_71(0x0003, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_72(0x000E, 0x0004)

    Jump('loc_5DC5')

    def _loc_5CEF(): pass

    label('loc_5CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_5D16',
    )

    OP_B1('E0310_4')
    OP_71(0x000D, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0014, 0x0004)

    Jump('loc_5DC5')

    def _loc_5D16(): pass

    label('loc_5D16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_5D3D',
    )

    OP_B1('E0310_4')
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)

    Jump('loc_5DC5')

    def _loc_5D3D(): pass

    label('loc_5D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 7, 0x1E2F)),
            Expr.Return,
        ),
        'loc_5D6E',
    )

    OP_B1('E0310_1')
    OP_71(0x0003, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)

    Jump('loc_5DC5')

    def _loc_5D6E(): pass

    label('loc_5D6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_5D95',
    )

    OP_B1('E0310_4')
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0014, 0x0004)

    Jump('loc_5DC5')

    def _loc_5D95(): pass

    label('loc_5D95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 0, 0x1E00)),
            Expr.Return,
        ),
        'loc_5DBC',
    )

    OP_B1('E0310_4')
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0014, 0x0004)

    Jump('loc_5DC5')

    def _loc_5DBC(): pass

    label('loc_5DBC')

    OP_B1('E0310_3')

    def _loc_5DC5(): pass

    label('loc_5DC5')

    Jump('loc_5E5B')

    def _loc_5DC8(): pass

    label('loc_5DC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_5DF4',
    )

    OP_B1('E0310_1')
    OP_71(0x0003, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)

    Jump('loc_5E5B')

    def _loc_5DF4(): pass

    label('loc_5DF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 7, 0x1A1F)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 0, 0x1A20)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 1, 0x1A21)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 2, 0x1A22)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5E34',
    )

    OP_B1('E0310_1')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)

    Jump('loc_5E5B')

    def _loc_5E34(): pass

    label('loc_5E34')

    OP_B1('E0310_1')
    OP_71(0x0003, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)

    def _loc_5E5B(): pass

    label('loc_5E5B')

    Return()

# id: 0x000A offset: 0x5E5C
@scena.Code('func_0A_5E5C')
def func_0A_5E5C():
    EventBegin(0x00)
    OP_22(0x00AB, 0x01, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('尤莉亚上尉')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0100310483V巡逻艇『梅尔杰号』传来联络！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310484V在玛鲁加矿山上空\n',
            '发现了飞行中的龙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310485V全体船员立刻前往工作岗位！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310486V协会有关人员\n',
            '请迅速前来舰桥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010310487V#1005F──来了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x5F92
@scena.Code('func_0B_5F92')
def func_0B_5F92():
    EventBegin(0x00)
    OP_6D(-470, 2000, 93430, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x007A, 0x01, 0x46)
    SetChrFlags(0x0101, 0x0080)
    SetChrPos(0x000A, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_72(0x0003, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x006D, 0x00, 0x64)
    Sleep(300)

    CreateThread(0x0101, 0x00, 0x00, 0x000C)
    Sleep(500)

    CreateThread(0x0008, 0x00, 0x00, 0x000D)
    Sleep(500)

    CreateThread(0x0009, 0x00, 0x00, 0x000F)
    Sleep(500)

    CreateThread(0x000B, 0x00, 0x00, 0x000E)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010310488V#1005F#6P现在怎么样了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 225, 400)
    OP_8C(0x000A, 180, 400)

    ChrTalk(
        0x000D,
        (
            '#0600310489V#160F#5P你们也听到了，\n',
            '龙出现在了玛鲁加矿山上空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310490V请看显示器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6118')
    def lambda_6118():
        OP_6D(720, 2000, 95220, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6118)

    @scena.Lambda('lambda_6130')
    def lambda_6130():
        OP_67(0, 5150, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6130)

    OP_8C(0x000D, 45, 400)

    @scena.Lambda('lambda_614F')
    def lambda_614F():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_614F)

    Sleep(50)

    @scena.Lambda('lambda_6162')
    def lambda_6162():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6162)

    Sleep(50)

    @scena.Lambda('lambda_6175')
    def lambda_6175():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6175)

    Sleep(50)

    @scena.Lambda('lambda_6188')
    def lambda_6188():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6188)

    Sleep(50)

    @scena.Lambda('lambda_619B')
    def lambda_619B():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_619B)

    WaitForThreadExit(0x0101, 0x0002)
    OP_6F(0x000C, 1)
    OP_70(0x000C, 0x0000003C)
    Sleep(150)

    OP_22(0x0127, 0x00, 0x64)
    OP_73(0x000C)
    OP_22(0x009D, 0x00, 0x64)
    OP_22(0x009D, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    OP_74(0x000C, 0x00000006, 0x0001)
    OP_74(0x000C, 0x00000008, 0x0001)
    OP_74(0x000C, 0x0000000A, 0x0001)
    OP_0D()
    Sleep(500)

    FadeOut(500, 0, -1)
    OP_AD(0x0024010E, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010310491V#1002F玛鲁加矿山……\n',
            '出现在洛连特了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030310492V#022F终于发现了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x00, 0x03, 16777215, 500, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(100)

    SetChrSubChip(0x000C, 2)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310493V#178F#5P迎击地点\n',
            '设定在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 0, 400)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#0600310494V#163F#2P让我看看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310495V虽说要诱导到湖上，\n',
            '不过不能让它接近王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310496V#160F──迎击地点\n',
            '就定在雷那特川河口附近！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310497V巡逻艇沿着河岸诱导龙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310498V攻击艇立刻出发！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310499V#170F#5P是，长官。！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 0)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310500V#176F#6P──这里是『埃尔赛尤』。\n',
            '通告作战行动中的全舰艇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310501V#178F迎击地点\n',
            '就设定在雷那特川河口附近！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310502V全巡逻艇以B队形沿着河岸\n',
            '将龙诱导到迎击地点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310503V全攻击艇立刻出发，\n',
            '迅速赶往迎击地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C3108._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x6536
@scena.Code('func_0C_6536')
def func_0C_6536():
    SetChrPos(0x00FE, -1040, 2000, 83000, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_655D')
    def lambda_655D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_655D)

    OP_8E(0x00FE, -1170, 2000, 91550, 5000, 0x00)

    Return()

# id: 0x000D offset: 0x657E
@scena.Code('func_0D_657E')
def func_0D_657E():
    SetChrPos(0x00FE, -1040, 2000, 83000, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_65A5')
    def lambda_65A5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_65A5)

    OP_8E(0x00FE, -2390, 2000, 91050, 5000, 0x00)

    Return()

# id: 0x000E offset: 0x65C6
@scena.Code('func_0E_65C6')
def func_0E_65C6():
    SetChrPos(0x00FE, -1040, 2000, 83000, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_65ED')
    def lambda_65ED():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_65ED)

    OP_8E(0x00FE, -1610, 2000, 89800, 5000, 0x00)

    Return()

# id: 0x000F offset: 0x660E
@scena.Code('func_0F_660E')
def func_0F_660E():
    SetChrPos(0x00FE, -1040, 2000, 83000, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6635')
    def lambda_6635():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6635)

    OP_8E(0x00FE, -180, 2000, 90890, 5000, 0x00)

    Return()

# id: 0x0010 offset: 0x6656
@scena.Code('func_10_6656')
def func_10_6656():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x007A, 0x01, 0x46)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0008, -2390, 2000, 91050, 0)
    SetChrPos(0x000B, -1610, 2000, 89800, 0)
    SetChrPos(0x0009, -180, 2000, 90890, 0)
    SetChrPos(0x000A, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_72(0x0003, 0x0004)
    FadeOut(0, 0, -1)
    OP_AD(0x0024010F, 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 500, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    Sleep(100)

    SetChrSubChip(0x000C, 2)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310511V#178F#5P全攻击艇出发完毕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310512V部署完成的预定时间是\n',
            '１２:２０。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310513V#163F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310514V#160F『埃尔赛尤』出发。\n',
            '迅速赶往迎击地点的西南方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310515V#170F#5P是，长官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 0)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310516V#178F#6P恢复对各部位的导力传达。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310517V『埃尔赛尤』出发。\n',
            '火速赶往雷那特川河口西南方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS219._CH')
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS230._CH')
    OP_C5(0x02, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS231._CH')
    OP_C5(0x03, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS232._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1000)

    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x03, -1, 500, 0)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 1000, 0)
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x6AD9
@scena.Code('func_11_6AD9')
def func_11_6AD9():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x007A, 0x01, 0x46)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0008, -2390, 2000, 91050, 0)
    SetChrPos(0x000B, -1610, 2000, 89800, 0)
    SetChrPos(0x0009, -180, 2000, 90890, 0)
    SetChrPos(0x000A, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_72(0x0003, 0x0004)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0100310518V#170F#5P全体攻击艇\n',
            '都已到达部属位置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310519V麻醉弹的装填也已完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310520V#163F#2P好，接下来\n',
            '就等龙出现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310521V#160F全体攻击艇做好射击准备。\n',
            '随命令一同开始攻击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310522V#178F#5P是，长官！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310523V#1002F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310524V#042F#6P终于要开始了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS233._CH')
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS234._CH')
    OP_C5(0x02, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS235._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1000)

    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 1000, 0)
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x6E77
@scena.Code('func_12_6E77')
def func_12_6E77():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x007A, 0x01, 0x46)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0008, -2390, 2000, 91050, 0)
    SetChrPos(0x000B, -1610, 2000, 89800, 0)
    SetChrPos(0x0009, -180, 2000, 90890, 0)
    SetChrPos(0x000A, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_72(0x0003, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    Fade(500)

    @scena.Lambda('lambda_6F85')
    def lambda_6F85():
        OP_6B(3300, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F85)

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0600310525V#162F#2P#5S射击！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x6FE1
@scena.Code('func_13_6FE1')
def func_13_6FE1():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x007A, 0x01, 0x46)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0008, -2390, 2000, 91050, 0)
    SetChrPos(0x000B, -1610, 2000, 89800, 0)
    SetChrPos(0x0009, -180, 2000, 90890, 0)
    SetChrPos(0x000A, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_72(0x0003, 0x0004)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0600310526V#164F#2P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310527V#1018F#6P成、成功了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030310528V#020F#6P……太漂亮了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080310529V#071F#4P嗯，就算是\n',
            '巨龙也无从抵抗啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310530V#031F哎呀……\n',
            '真是华丽的场面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 2)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310531V#170F#5P──确认龙已坠入\n',
            '瓦雷利亚湖！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310532V要按照预定计划，\n',
            '用绳索捕捉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310513V#163F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310534V#160F在确认安全的情况下，\n',
            '『埃尔赛尤』也一起降落。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310535V降在湖面上后进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310536V#171F#5P是，长官！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    OP_23(0x007A)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0900._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x72F9
@scena.Code('func_14_72F9')
def func_14_72F9():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_23(0x007A)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0008, -2390, 2000, 91050, 0)
    SetChrPos(0x000B, -1610, 2000, 89800, 0)
    SetChrPos(0x0009, -180, 2000, 90890, 0)
    SetChrPos(0x000A, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_71(0x0003, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100310537V#176F#5P『埃尔赛尤』降落完毕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310538V#178F龙还没有任何反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310539V#163F#2P好……\n',
            '我们去亲眼看一下吧',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310540V#160F上尉，你也跟来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000C, 2)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310541V#172F#5P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(250)
    ClearChrFlags(0x000C, 0x0004)
    SetChrPos(0x000C, -1050, 2000, 94150, 0)
    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)
    OP_0D()
    Sleep(200)

    @scena.Lambda('lambda_7514')
    def lambda_7514():
        OP_6D(-340, 2000, 90490, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7514)

    @scena.Lambda('lambda_752C')
    def lambda_752C():
        OP_6C(36000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_752C)

    @scena.Lambda('lambda_753C')
    def lambda_753C():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_753C)

    Sleep(70)

    @scena.Lambda('lambda_754F')
    def lambda_754F():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_754F)

    Sleep(70)

    @scena.Lambda('lambda_7562')
    def lambda_7562():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_7562')

    DispatchAsync2(0x0101, 0x0002, lambda_7562)

    @scena.Lambda('lambda_7573')
    def lambda_7573():
        OP_8C(0x00FE, 270, 400)
        Yield()

        Jump('lambda_7573')

    DispatchAsync2(0x0009, 0x0002, lambda_7573)

    Sleep(70)

    @scena.Lambda('lambda_7589')
    def lambda_7589():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_7589')

    DispatchAsync2(0x0008, 0x0002, lambda_7589)

    Sleep(80)

    @scena.Lambda('lambda_759F')
    def lambda_759F():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_759F')

    DispatchAsync2(0x000B, 0x0002, lambda_759F)

    Sleep(70)

    @scena.Lambda('lambda_75B5')
    def lambda_75B5():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_75B5')

    DispatchAsync2(0x000A, 0x0002, lambda_75B5)

    @scena.Lambda('lambda_75C6')
    def lambda_75C6():
        OP_8F(0x00FE, 660, 2000, 90090, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_75C6)

    CreateThread(0x000D, 0x00, 0x00, 0x0016)
    CreateThread(0x000C, 0x00, 0x00, 0x0015)
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_75F9')
    def lambda_75F9():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_75F9')

    DispatchAsync2(0x0009, 0x0002, lambda_75F9)

    Sleep(2300)

    ChrTalk(
        0x0101,
        (
            '#0010310542V#1004F#5P啊，等一等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000C, 0x0000)
    ChrTurnDirection(0x000C, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100310543V#171F呵呵，你们也一起来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310544V这是传说中的古代龙。\n',
            '平常很难得有机会见可以到吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310545V#1008F#5P嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)
    OP_6D(-890, 2000, 88540, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -890, 2000, 88540, 180)
    SetChrPos(0x0105, -890, 2000, 88540, 180)
    SetChrPos(0x0103, -890, 2000, 88540, 180)
    SetChrPos(0x0104, -890, 2000, 88540, 180)
    SetChrPos(0x0108, -890, 2000, 88540, 180)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x1A23)
    OP_28(0x0095, 0x01, 0x0020)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0015 offset: 0x77BE
@scena.Code('func_15_77BE')
def func_15_77BE():
    Sleep(800)

    OP_8E(0x00FE, -230, 2000, 93700, 2000, 0x00)
    OP_8E(0x00FE, -420, 2000, 89390, 2000, 0x00)
    OP_8F(0x00FE, -750, 2000, 87630, 2000, 0x00)

    Return()

# id: 0x0016 offset: 0x7800
@scena.Code('func_16_7800')
def func_16_7800():
    OP_8E(0x00FE, -420, 2000, 89390, 2000, 0x00)
    OP_8F(0x00FE, -1100, 2000, 83980, 2000, 0x00)
    OP_8F(0x00FE, -970, 2000, 83230, 2000, 0x00)

    @scena.Lambda('lambda_7842')
    def lambda_7842():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_7842)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0017 offset: 0x7859
@scena.Code('func_17_7859')
def func_17_7859():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_D2(0x00270009, 0x0027000D, 0x1D)
    OP_D2(0x00070025, 0x0007002D, 0x1E)
    OP_D2(0x00070035, 0x0007003D, 0x1F)
    OP_D2(0x00070045, 0x0007004D, 0x20)
    OP_D2(0x00070075, 0x0007007D, 0x21)
    OP_22(0x007A, 0x01, 0x50)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0103, -2390, 2000, 91050, 0)
    SetChrPos(0x0108, -1610, 2000, 89800, 0)
    SetChrPos(0x0104, -180, 2000, 90890, 0)
    SetChrPos(0x0105, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_71(0x0003, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_76(0x0007, 0x00000002, 0x0001, 0xFFFFFFFC, 0xFFFFFFFF, 0x00000000, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    SetChrName('操舵士勒克司')

    ChrTalk(
        0x000E,
        (
            '#3530310616V#5P不行！\n',
            '诱导弹无法锁定目标！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3530310617V#5P明明已经探测到热源了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310618V#176F#2P也就是说有\n',
            '某种干扰波吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310619V#177F那就切换到主炮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrName('测量师艾柯')

    ChrTalk(
        0x000F,
        (
            '#3540310620V#2P龙的速度持续上升中……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540310621V#2P时速２３００塞尔矩──\n',
            '２４００、２５００、２６００……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310622V#162F#2P可恶，这是什么怪物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310623V竟能轻松超越\n',
            '警备艇的最高速度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 2)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0100310624V#172F#5P不过，用搭载了新型引擎的\n',
            '『埃尔赛尤』就有可能进行追击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 0)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0100310625V#176F#2P──通告全体船员！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310626V#177F接下来『埃尔赛尤』将加速至\n',
            '最大战速３２００塞尔矩！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310627V全体进行抗重力准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310628V#1020F咦咦？这是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0105, 180, 600)

    ChrTalk(
        0x0105,
        (
            '#0060310629V#046F#5P会有紧急加速的重力袭来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310630V请蹲下\n',
            '将姿势摆低！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310631V#1002F！　明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0105, 0, 600)
    Fade(500)
    SetChrChipByIndex(0x0105, 32)
    SetChrSubChip(0x0105, 0)
    SetChrChipByIndex(0x0101, 29)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0103, 30)
    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0104, 31)
    SetChrSubChip(0x0104, 0)
    SetChrChipByIndex(0x0108, 33)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x000D, 6)
    SetChrSubChip(0x000D, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100310632V#177F#2P──开始加速！\n',
            '绝对不能让龙逃跑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3530310633V#5P是，长官！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0129, 0x01, 0x46)
    Sleep(200)

    OP_24(0x0129, 0x50)
    Sleep(200)

    OP_24(0x0129, 0x5A)
    Sleep(200)

    OP_24(0x0129, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_7DDF')
    def lambda_7DDF():
        OP_7C(0x00000032, 0x00000032, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_7DDF')

    DispatchAsync2(0x0101, 0x0003, lambda_7DDF)

    Fade(500)
    OP_71(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310634V#1021F哇哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    @scena.Lambda('lambda_7E43')
    def lambda_7E43():
        OP_6D(-2040, 2000, 69140, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7E43)

    @scena.Lambda('lambda_7E5B')
    def lambda_7E5B():
        OP_67(0, 7960, -10000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7E5B)

    Sleep(1000)

    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x7E8F
@scena.Code('func_18_7E8F')
def func_18_7E8F():
    EventBegin(0x00)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1170, 2000, 91550, 0)
    SetChrPos(0x0103, -2390, 2000, 91050, 0)
    SetChrPos(0x0108, -1610, 2000, 89800, 0)
    SetChrPos(0x0104, -180, 2000, 90890, 0)
    SetChrPos(0x0105, -2160, 2020, 92450, 0)
    SetChrPos(0x000C, -1090, 2200, 93560, 0)
    SetChrPos(0x000D, -210, 2000, 92630, 0)
    SetChrFlags(0x000C, 0x0004)
    SetChrChipByIndex(0x000C, 18)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_D2(0x00270009, 0x0027000D, 0x1D)
    OP_D2(0x00070025, 0x0007002D, 0x1E)
    OP_D2(0x00070035, 0x0007003D, 0x1F)
    OP_D2(0x00070045, 0x0007004D, 0x20)
    OP_D2(0x00070075, 0x0007007D, 0x21)
    SetChrChipByIndex(0x0101, 29)
    SetChrChipByIndex(0x0103, 30)
    SetChrChipByIndex(0x0104, 31)
    SetChrChipByIndex(0x0108, 33)
    SetChrChipByIndex(0x000D, 6)
    SetChrChipByIndex(0x0105, 32)
    SetChrSubChip(0x0105, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x0104, 0)
    SetChrSubChip(0x0108, 0)
    SetChrSubChip(0x000D, 0)
    OP_22(0x007A, 0x01, 0x50)
    OP_22(0x0129, 0x01, 0x64)

    @scena.Lambda('lambda_7FDF')
    def lambda_7FDF():
        OP_7C(0x00000032, 0x00000032, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_7FDF')

    DispatchAsync2(0x0101, 0x0003, lambda_7FDF)

    OP_71(0x0003, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_72(0x000D, 0x0004)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#3540310635V#2P……龙的高度下降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540310636V#2P再这样下去将会跟丢目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310637V#177F#2P要紧跟到最后一刻！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310638V#175F……可恶。\n',
            '云层还没冲破吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030310639V#024F#6P等等！\n',
            '这是什么地区！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 1)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310640V#173F#2P！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_AD(0x00240120, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(160, 220, -1, -1)
    SetChrName('尤莉亚上尉')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0100310641V#172F是迷雾峡谷吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010310642V#1020F莫非我们\n',
            '已经进入了雾中！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310643V#162F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x00, 0x03, 16777215, 500, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#3540310644V#2P龙的高度下降至１２００亚矩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540310645V#2P１１００、１０００、９００……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540310646V#2P……………………\n',
            '……目标丢失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(100)

    SetChrSubChip(0x000C, 0)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100310647V#175F#5P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060310648V#043F#6P尤莉亚上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310649V#1015F跟、跟丢了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310650V#176F#5P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310651V#175F在迷雾峡谷的西北部……\n',
            '被它逃到雾气浓密的险处去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310652V#160F#2P……埃尔赛尤号要停到\n',
            '那个空贼巢穴去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000C, 2)

    ChrTalk(
        0x000C,
        (
            '#0100310653V#175F#5P不……按照埃尔赛尤号的\n',
            '大小是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310654V#163F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310655V#160F──作战结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310656V让后续的巡逻艇\n',
            '监视峡谷周围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310657V#163F让『埃尔赛尤』\n',
            '暂时返回柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_23(0x007A)
    OP_23(0x0129)
    Sleep(1000)

    OP_A2(0x1A24)
    ClearMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x852E
@scena.Code('func_19_852E')
def func_19_852E():
    EventBegin(0x00)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['约修亚'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['提妲'], 0xFE, 0)
    SetChrStatus(ChrTable['凯文神父'], 0xFE, 0)
    SetChrStatus(ChrTable['金'], 0xFE, 0)
    OP_6D(490, 2000, 88600, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(287, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrPos(0x000C, -250, 2000, 92100, 270)
    SetChrPos(0x0011, -1630, 2000, 92100, 90)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000C, 0x0004)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_85F2')
    def lambda_85F2():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_85F2')

    DispatchAsync2(0x000C, 0x0001, lambda_85F2)

    Sleep(100)

    @scena.Lambda('lambda_8608')
    def lambda_8608():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_8608)

    Sleep(400)

    @scena.Lambda('lambda_861B')
    def lambda_861B():
        OP_6D(190, 2000, 92150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_861B)

    CreateThread(0x0101, 0x01, 0x00, 0x001A)
    Sleep(300)

    CreateThread(0x0102, 0x01, 0x00, 0x001B)
    Sleep(300)

    CreateThread(0x0013, 0x01, 0x00, 0x001C)
    Sleep(300)

    CreateThread(0x000A, 0x01, 0x00, 0x001D)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, 0x001E)
    Sleep(300)

    CreateThread(0x0012, 0x01, 0x00, 0x001F)
    Sleep(300)

    CreateThread(0x0014, 0x01, 0x00, 0x0020)
    Sleep(300)

    CreateThread(0x000B, 0x01, 0x00, 0x0021)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x000C, 0x01)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260612V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070340257V#064F爷、爷爷！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340258V#101F#5P好久不见了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340259V#100F提妲。\n',
            '你还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070340260V#067F嘿嘿……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050340261V#051F喂喂，老爷子。\n',
            '你怎么在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340262V#104F#5P说来话长，几天前\n',
            '我就乘上埃尔赛尤号了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340263V#100F话说回来……\n',
            '艾丝蒂尔、约修亚，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340264V你们都能平安\n',
            '返回真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340265V#1016F哈哈……嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340266V#1035F……很抱歉，\n',
            '让您担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340267V#101F#5P哪里，只要能回来\n',
            '就万事大吉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340268V#102F不过想不到『四轮之塔』\n',
            '居然发生了异变呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340269V现在我也得集中精神\n',
            '进行调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340270V#1006F嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340271V#1015F不过……\n',
            '应该先去哪座塔好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340272V#1043F是啊……\n',
            '如果考虑距离的话\n',
            '还是『琥珀』和『红莲』比较近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100340273V#176F不过以『埃尔赛尤』的速度，\n',
            '去哪座塔都差不多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340274V#178F或许应该先去已经掌握了\n',
            '敌人情报的地方会比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340275V#1004F敌人的情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100340276V#178F刚才前往『翡翠之塔』的\n',
            '侦察部队传来了后续报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340277V据说是出现了一个\n',
            '戴着面具、身穿白衣的可疑男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010340278V#1005F是那个怪盗男！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060340279V#043F虽说只是侦察部队，\n',
            '不过竟能以一己之力击破……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C10',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇第１章选择了阿加特】\n'),
            TXT(0x01, '【◇第１章选择了雪拉扎德】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8C04'),
        (0x00000001, 'loc_8C0A'),
        (-1, 'loc_8C10'),
    )

    def _loc_8C04(): pass

    label('loc_8C04')

    OP_A2(0x1201)

    Jump('loc_8C10')

    def _loc_8C0A(): pass

    label('loc_8C0A')

    OP_A3(0x1200)

    Jump('loc_8C10')

    def _loc_8C10(): pass

    label('loc_8C10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8C50',
    )

    ChrTalk(
        0x0012,
        (
            '#0050340280V#057F嘿，看来不只是个\n',
            '古怪的家伙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C85')

    def _loc_8C50(): pass

    label('loc_8C50')

    ChrTalk(
        0x0008,
        (
            '#0030340281V#022F看来他的实力在我们的想象之上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C85(): pass

    label('loc_8C85')

    ChrTalk(
        0x0102,
        (
            '#0020340282V#1035F『怪盗绅士』布卢布兰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340283V#1042F以分身和影缝为主要攻击手段，\n',
            '使用各种魔术般技巧的执行者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340284V一般的战法在他面前大概行不通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251390V#1007F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340286V#1015F不过，至少了解了敌人的真身，\n',
            '总比去其他的塔更有把握……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340287V#1006F嗯！\n',
            '先去『翡翠之塔』吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100340288V#170F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8DEB')
    def lambda_8DEB():
        OP_6D(310, 2000, 95070, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8DEB)

    @scena.Lambda('lambda_8E03')
    def lambda_8E03():
        OP_67(0, 4710, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8E03)

    @scena.Lambda('lambda_8E1B')
    def lambda_8E1B():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_8E1B)

    Sleep(800)

    OP_8C(0x0011, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0100340289V#172F#2P准备出发！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340290V本舰现在前往\n',
            '洛连特地区的『翡翠之塔』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E00)
    OP_BB(0x01, 0x00, 0x00200033)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T4106._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x8EAF
@scena.Code('func_1A_8EAF')
def func_1A_8EAF():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_8ED6')
    def lambda_8ED6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8ED6)

    OP_8F(0x00FE, -400, 2020, 90600, 3000, 0x00)

    Return()

# id: 0x001B offset: 0x8EF7
@scena.Code('func_1B_8EF7')
def func_1B_8EF7():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_8F1E')
    def lambda_8F1E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8F1E)

    OP_8F(0x00FE, -1420, 2020, 90600, 3000, 0x00)

    Return()

# id: 0x001C offset: 0x8F3F
@scena.Code('func_1C_8F3F')
def func_1C_8F3F():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_8F66')
    def lambda_8F66():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8F66)

    OP_8F(0x00FE, -2650, 2000, 89700, 3000, 0x00)

    Return()

# id: 0x001D offset: 0x8F87
@scena.Code('func_1D_8F87')
def func_1D_8F87():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_8FAE')
    def lambda_8FAE():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8FAE)

    OP_8F(0x00FE, 100, 2000, 89800, 3000, 0x00)

    Return()

# id: 0x001E offset: 0x8FCF
@scena.Code('func_1E_8FCF')
def func_1E_8FCF():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_8FF6')
    def lambda_8FF6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8FF6)

    OP_8F(0x00FE, -1600, 2000, 89200, 3000, 0x00)

    Return()

# id: 0x001F offset: 0x9017
@scena.Code('func_1F_9017')
def func_1F_9017():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_903E')
    def lambda_903E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_903E)

    OP_8F(0x00FE, -2480, 2000, 88000, 3000, 0x00)

    Return()

# id: 0x0020 offset: 0x905F
@scena.Code('func_20_905F')
def func_20_905F():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_9086')
    def lambda_9086():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_9086)

    OP_8F(0x00FE, -1120, 2000, 88300, 3000, 0x00)

    Return()

# id: 0x0021 offset: 0x90A7
@scena.Code('func_21_90A7')
def func_21_90A7():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -1170, 2000, 83500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_90CE')
    def lambda_90CE():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_90CE)

    OP_8F(0x00FE, -590, 2000, 87700, 3000, 0x00)

    Return()

# id: 0x0022 offset: 0x90EF
@scena.Code('func_22_90EF')
def func_22_90EF():
    EventBegin(0x00)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -310, 2000, 91660, 0)
    SetChrPos(0x0102, -1460, 2000, 91520, 0)
    SetChrPos(0x0013, -2630, 2000, 90470, 0)
    SetChrPos(0x000A, 220, 2020, 90650, 0)
    SetChrPos(0x0012, -2550, 2000, 89380, 0)
    SetChrPos(0x0008, -1000, 2020, 90140, 0)
    SetChrPos(0x000B, -80, 2000, 89260, 0)
    SetChrPos(0x0014, -1380, 2000, 88780, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -2400, 2000, 91710, 0)
    OP_4A(0x000A, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x000C, 18)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x000F, 8)
    SetChrChipByIndex(0x0010, 9)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0010)
    SetChrPos(0x000C, -920, 2100, 93680, 0)
    SetChrPos(0x000E, -1040, 100, 99020, 0)
    SetChrPos(0x000F, -3400, 100, 98950, 315)
    SetChrPos(0x0010, 1300, 100, 98950, 45)
    OP_22(0x007A, 0x01, 0x46)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100340316V#176F#2P已到达『翡翠之塔』上空。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340317V#1004F啊～真的好快呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340318V不到30分钟\n',
            '就抵达了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070340319V#061F#6P嘿嘿，差不多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340320V#560F应该用了定期船\n',
            '将近三倍的速度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340321V#1006F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340322V#1042F#6P『翡翠之塔』的塔顶\n',
            '情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100340323V#178F#2P马上会显示在屏幕上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x009D, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_9416')
    def lambda_9416():
        OP_67(0, 5150, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9416)

    OP_72(0x0013, 0x0004)
    OP_6F(0x0013, 0)
    OP_70(0x0013, 0x0000003C)
    SetChrSubChip(0x000C, 2)
    Sleep(100)

    @scena.Lambda('lambda_944B')
    def lambda_944B():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_944B)

    @scena.Lambda('lambda_9459')
    def lambda_9459():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9459)

    Sleep(50)

    OP_22(0x0127, 0x00, 0x64)

    @scena.Lambda('lambda_9471')
    def lambda_9471():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9471)

    @scena.Lambda('lambda_947F')
    def lambda_947F():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_947F)

    Sleep(50)

    @scena.Lambda('lambda_9492')
    def lambda_9492():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_9492)

    OP_73(0x0013)
    WaitForThreadExit(0x0101, 0x0000)
    OP_22(0x009D, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    OP_74(0x0013, 0x00000006, 0x0002)
    OP_74(0x0013, 0x00000008, 0x0002)
    OP_74(0x0013, 0x0000000A, 0x0002)
    OP_0D()
    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C0706._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0023 offset: 0x94EA
@scena.Code('func_23_94EA')
def func_23_94EA():
    EventBegin(0x00)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x0013, 0x0004)
    OP_6F(0x0013, 60)
    OP_74(0x0013, 0x00000006, 0x0002)
    OP_74(0x0013, 0x00000008, 0x0002)
    OP_74(0x0013, 0x0000000A, 0x0002)
    SetChrPos(0x0101, -310, 2000, 91660, 0)
    SetChrPos(0x0102, -1460, 2000, 91520, 0)
    SetChrPos(0x0013, -2630, 2000, 90470, 0)
    SetChrPos(0x000A, 220, 2020, 90650, 0)
    SetChrPos(0x0012, -2550, 2000, 89380, 0)
    SetChrPos(0x0008, -1000, 2020, 90140, 0)
    SetChrPos(0x000B, -80, 2000, 89260, 0)
    SetChrPos(0x0014, -1380, 2000, 88780, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -2400, 2000, 91710, 0)
    OP_4A(0x000A, 255)

    @scena.Lambda('lambda_961B')
    def lambda_961B():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_961B)

    @scena.Lambda('lambda_9629')
    def lambda_9629():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9629)

    @scena.Lambda('lambda_9637')
    def lambda_9637():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9637)

    @scena.Lambda('lambda_9645')
    def lambda_9645():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_9645)

    @scena.Lambda('lambda_9653')
    def lambda_9653():
        OP_8C(0x00FE, 45, 0)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_9653)

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrSubChip(0x000C, 2)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x000C, 18)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x000F, 8)
    SetChrChipByIndex(0x0010, 9)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0010)
    SetChrPos(0x000C, -920, 2100, 93680, 0)
    SetChrPos(0x000E, -1040, 100, 99020, 0)
    SetChrPos(0x000F, -3400, 100, 98950, 315)
    SetChrPos(0x0010, 1300, 100, 98950, 45)
    OP_22(0x007A, 0x01, 0x46)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x0102, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340328V#1042F#6P尤莉亚小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340329V我们应该怎样\n',
            '下降到地面呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100340330V#176F#5P很不巧，没有能让\n',
            '『埃尔赛尤』着陆的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340331V#178F我们会在滞空状态放下升降机，\n',
            '请你们乘上去下降到地面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340332V#1004F升降机？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060340333V#040F#4P就是投放榴弹炮时\n',
            '使用的货用升降机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340334V被设置在货舱里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, -180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340335V#1006F#5P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340336V#1040F#6P那么，请选择调查塔\n',
            '内部的成员人选吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_71(0x0013, 0x0004)
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_994A',
    )

    Call(0, 0x002C)

    def _loc_994A(): pass

    label('loc_994A')

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(200)

    Sleep(1000)

    OP_A2(0x10F9)
    OP_A2(0x10FA)
    NewScene('ED6_DT21/E0310._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0024 offset: 0x99EE
@scena.Code('func_24_99EE')
def func_24_99EE():
    EventBegin(0x00)
    OP_6D(-740, 2000, 46900, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0101, -430, 2000, 47400, 180)
    SetChrPos(0x0102, -1430, 2000, 47400, 180)
    SetChrPos(0x00F8, -1430, 2000, 48400, 180)
    SetChrPos(0x00F9, -430, 2000, 48400, 180)
    SetChrPos(0x0011, -920, 2000, 45630, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0540340337V#100F我会暂时待在\n',
            '下面的工房里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340338V在调查塔时，如果需要整备导力器\n',
            '或合成回路的话就来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340339V#1006F#5P嗯，我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9CE4',
    )

    ChrTalk(
        0x0011,
        (
            '#0540340340V#102F提妲……\n',
            '你一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340341V#560F#5P嗯……不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340342V#061F我也\n',
            '和姐姐他们一起\n',
            '旅行过很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340343V#100F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340344V#1006F#5P博士，请别担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050340345V#051F#5P没事，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340346V#104F嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340347V#102F……敌人的目的\n',
            '尚不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340348V你们小心上路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EB2')

    def _loc_9CE4(): pass

    label('loc_9CE4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E64',
    )

    ChrTalk(
        0x0011,
        (
            '#0540340340V#102F提妲……\n',
            '你一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340341V#560F#5P嗯……不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340342V#061F我也\n',
            '和姐姐他们一起\n',
            '旅行过很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340343V#100F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340344V#1006F#5P博士，请别担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340354V#1040F#5P请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540340346V#104F嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340347V#102F……敌人的目的\n',
            '尚不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340348V你们小心上路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EB2')

    def _loc_9E64(): pass

    label('loc_9E64')

    ChrTalk(
        0x0011,
        (
            '#0540340347V#102F……敌人的目的\n',
            '尚不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340348V你们小心上路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EB2(): pass

    label('loc_9EB2')

    OP_8C(0x0011, 90, 400)

    @scena.Lambda('lambda_9EBF')
    def lambda_9EBF():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9EBF')

    DispatchAsync2(0x0101, 0x0001, lambda_9EBF)

    @scena.Lambda('lambda_9ED0')
    def lambda_9ED0():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9ED0')

    DispatchAsync2(0x0102, 0x0001, lambda_9ED0)

    @scena.Lambda('lambda_9EE1')
    def lambda_9EE1():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9EE1')

    DispatchAsync2(0x00F8, 0x0001, lambda_9EE1)

    @scena.Lambda('lambda_9EF2')
    def lambda_9EF2():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9EF2')

    DispatchAsync2(0x00F9, 0x0001, lambda_9EF2)

    SetChrFlags(0x0011, 0x0004)
    OP_8E(0x0011, 1670, 2050, 45650, 2000, 0x00)
    ClearChrFlags(0x0011, 0x0004)
    OP_8E(0x0011, 2080, 0, 49520, 2000, 0x00)
    SetChrFlags(0x0011, 0x0080)
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_9F4F')
    def lambda_9F4F():
        OP_6D(-710, 2000, 47510, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9F4F)

    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_9F6E')
    def lambda_9F6E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9F6E)

    @scena.Lambda('lambda_9F7C')
    def lambda_9F7C():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9F7C)

    Sleep(50)

    @scena.Lambda('lambda_9F8F')
    def lambda_9F8F():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_9F8F)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010340360V#1006F#2P那么，准备完成之后\n',
            '就必须马上下降到地面才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340361V#1040F#6P嗯。\n',
            '是货舱的升降机吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-1210, 2000, 46360, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1210, 2000, 46360, 180)
    SetChrPos(0x0102, -1210, 2000, 46360, 180)
    SetChrPos(0x00F8, -1210, 2000, 46360, 180)
    SetChrPos(0x00F9, -1210, 2000, 46360, 180)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    OP_D2(0x000600FE, 0x00060103, 0x1D)
    OP_D2(0x000600FC, 0x00060101, 0x1E)
    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x000F, -1740, 0, 97950, 0)
    SetChrChipByIndex(0x000F, 11)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A135',
    )

    SetChrPos(0x0012, 770, 2000, 89910, 0)
    ClearChrFlags(0x0012, 0x0080)
    SetChrChipByIndex(0x0012, 28)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)

    def _loc_A135(): pass

    label('loc_A135')

    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    OP_A2(0x1E01)
    OP_28(0x0099, 0x01, 0x0800)
    OP_28(0x009A, 0x04, 0x02)
    OP_28(0x009A, 0x04, 0x08)
    OP_28(0x009A, 0x01, 0x0001)
    OP_28(0x009A, 0x01, 0x0002)
    OP_28(0x009A, 0x01, 0x0004)
    OP_28(0x009A, 0x01, 0x0008)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0025 offset: 0xA191
@scena.Code('func_25_A191')
def func_25_A191():
    EventBegin(0x00)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -310, 2000, 91660, 0)
    SetChrPos(0x0102, -1460, 2000, 91520, 0)
    SetChrPos(0x0013, -2630, 2000, 90470, 0)
    SetChrPos(0x000A, 220, 2020, 90650, 0)
    SetChrPos(0x0012, -2550, 2000, 89380, 0)
    SetChrPos(0x0008, -1000, 2020, 90140, 0)
    SetChrPos(0x0014, -1380, 2000, 88780, 0)
    SetChrPos(0x000E, -1040, 200, 99240, 0)
    SetChrPos(0x000F, -3530, 200, 99080, 315)
    SetChrPos(0x0010, 1380, 200, 99090, 45)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    TerminateThread(0x0012, 0xFF)
    SetChrSubChip(0x0012, 0)
    SetChrChipByIndex(0x0012, 15)
    OP_4A(0x000A, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrSubChip(0x000C, 2)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x000C, 18)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x000F, 8)
    SetChrChipByIndex(0x0010, 9)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0010)
    SetChrPos(0x000C, -920, 2100, 93680, 0)
    SetChrPos(0x000E, -1040, 100, 99020, 0)
    SetChrPos(0x000F, -3400, 100, 98950, 315)
    SetChrPos(0x0010, 1300, 100, 98950, 45)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100340972V#178F#5P已到达『红莲之塔』上空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340973V塔顶部分果然\n',
            '被漆黑的结界所覆盖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340974V#1002F#4P那么\n',
            '就像『翡翠之塔』一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340975V#1035F#6P内部很有可能已经\n',
            '变成另一个空间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_A449')
    def lambda_A449():
        OP_6D(-130, 2000, 90500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A449)

    @scena.Lambda('lambda_A461')
    def lambda_A461():
        OP_67(0, 5000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A461)

    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x000B, -1040, 2000, 83000, 0)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_A49A')
    def lambda_A49A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_A49A)

    @scena.Lambda('lambda_A4AC')
    def lambda_A4AC():
        OP_8E(0x00FE, -1040, 2000, 86000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_A4AC)

    @scena.Lambda('lambda_A4C7')
    def lambda_A4C7():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A4C7')

    DispatchAsync2(0x0101, 0x0001, lambda_A4C7)

    Sleep(50)

    @scena.Lambda('lambda_A4DD')
    def lambda_A4DD():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A4DD')

    DispatchAsync2(0x0102, 0x0001, lambda_A4DD)

    Sleep(50)

    @scena.Lambda('lambda_A4F3')
    def lambda_A4F3():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A4F3')

    DispatchAsync2(0x0013, 0x0001, lambda_A4F3)

    Sleep(50)

    @scena.Lambda('lambda_A509')
    def lambda_A509():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A509')

    DispatchAsync2(0x000A, 0x0001, lambda_A509)

    Sleep(50)

    @scena.Lambda('lambda_A51F')
    def lambda_A51F():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A51F')

    DispatchAsync2(0x0012, 0x0001, lambda_A51F)

    Sleep(50)

    @scena.Lambda('lambda_A535')
    def lambda_A535():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A535')

    DispatchAsync2(0x0008, 0x0001, lambda_A535)

    Sleep(100)

    @scena.Lambda('lambda_A54B')
    def lambda_A54B():
        OP_8C(0x00FE, 180, 400)
        Yield()

        Jump('lambda_A54B')

    DispatchAsync2(0x0014, 0x0001, lambda_A54B)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000B,
        (
            '#0080340976V#070F#4P哟，让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340977V#1004F#5P啊，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340978V#1015F和雾香小姐的联络中\n',
            '都说了什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080340979V#074F#4P嗯，她是在询问\n',
            '我们这边的情况如何了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340980V#070F我把在『翡翠之塔』发生的事\n',
            '大致跟她说了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340981V#1006F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340982V#1040F#5P辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080340983V#070F#4P好，那我们赶快\n',
            '进入『塔』里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A73F',
    )

    Call(0, 0x002C)

    def _loc_A73F(): pass

    label('loc_A73F')

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择固定队员外的一名同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0007,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0008,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(200)

    OP_6D(-1320, 2000, 87840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0000, -1320, 2000, 87840, 180)
    SetChrPos(0x0001, -1320, 2000, 87840, 180)
    SetChrPos(0x0002, -1320, 2000, 87840, 180)
    SetChrPos(0x0003, -1320, 2000, 87840, 180)
    OP_69(0x0000, 0x00000000)
    SetChrSubChip(0x000C, 0)
    SetChrChipByIndex(0x000C, 4)
    SetChrPos(0x000C, -1090, 2000, 94920, 0)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x000F, -1740, 0, 97950, 0)
    SetChrChipByIndex(0x000F, 11)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    SetChrPos(0x0010, 1330, 0, 98300, 225)
    SetChrChipByIndex(0x0010, 12)
    ClearChrFlags(0x0010, 0x0010)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    OP_D2(0x000600FE, 0x00060103, 0x1D)
    OP_D2(0x000600FC, 0x00060101, 0x1E)
    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000C, 0x0010)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x000F, -1740, 0, 97950, 0)
    SetChrChipByIndex(0x000F, 11)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    SetChrPos(0x0010, 530, 0, 98030, 90)
    SetChrChipByIndex(0x0010, 12)
    ClearChrFlags(0x0010, 0x0010)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A9B1',
    )

    TerminateThread(0x000A, 0xFF)
    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    OP_8C(0x000A, 0, 0)

    def _loc_A9B1(): pass

    label('loc_A9B1')

    Sleep(500)

    OP_A2(0x1E0A)
    OP_28(0x009A, 0x01, 0x0010)
    OP_28(0x009A, 0x01, 0x0020)
    OP_28(0x009A, 0x01, 0x0040)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0026 offset: 0xA9E1
@scena.Code('func_26_A9E1')
def func_26_A9E1():
    EventBegin(0x00)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    OP_76(0x0007, 0x00000002, 0x0001, 0xFFFFFFFC, 0xFFFFFFFF, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_AA0F')
    def lambda_AA0F():
        OP_7C(0x00000001, 0x00000001, 0x000007D0, 0x00000064)
        Yield()

        Jump('lambda_AA0F')

    DispatchAsync2(0x0101, 0x0003, lambda_AA0F)

    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -310, 2000, 91660, 0)
    SetChrPos(0x0102, -1460, 2000, 91520, 0)
    SetChrPos(0x0013, -2630, 2000, 90470, 0)
    SetChrPos(0x000A, 220, 2020, 90650, 0)
    SetChrPos(0x0012, -2550, 2000, 89380, 0)
    SetChrPos(0x0008, -1000, 2020, 90140, 0)
    SetChrPos(0x000B, -80, 2000, 89260, 0)
    SetChrPos(0x0014, -1380, 2000, 88780, 0)
    SetChrPos(0x000E, -1040, 200, 99240, 0)
    SetChrPos(0x000F, -3530, 200, 99080, 315)
    SetChrPos(0x0010, 1380, 200, 99090, 45)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    TerminateThread(0x0012, 0xFF)
    SetChrSubChip(0x0012, 0)
    SetChrChipByIndex(0x0012, 15)
    OP_4A(0x000A, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x000C, 18)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x000F, 8)
    SetChrChipByIndex(0x0010, 9)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0010)
    SetChrPos(0x000C, -920, 2100, 93680, 0)
    SetChrPos(0x000E, -1040, 100, 99020, 0)
    SetChrPos(0x000F, -3400, 100, 98950, 315)
    SetChrPos(0x0010, 1300, 100, 98950, 45)
    OP_71(0x0014, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341272V#1025F#5P卢安地区吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341273V特蕾莎院长和那些孩子们\n',
            '现在不知道怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060341274V#043F#4P我想应该已经在军队的\n',
            '保护下去避难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341275V#049F希望她们能平安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341276V#1040F#5P没事的，别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341277V在父亲的命令下，军队和\n',
            '协会正在进行联合镇压。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060341278V#542F#4P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341279V#1006F#5P的确，老爸\n',
            '是不会在此事上有任何疏忽的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050341280V#051F#6P嗯……那是自然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 2)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0100341281V#178F#5P──各位游击士，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341282V还有5分钟\n',
            '就将到达『绀碧之塔』上空。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_AEF8')
    def lambda_AEF8():
        OP_6D(370, 2000, 93430, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_AEF8)

    @scena.Lambda('lambda_AF10')
    def lambda_AF10():
        OP_67(0, 4500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_AF10)

    @scena.Lambda('lambda_AF28')
    def lambda_AF28():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_AF28)

    Sleep(50)

    @scena.Lambda('lambda_AF3B')
    def lambda_AF3B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_AF3B)

    @scena.Lambda('lambda_AF49')
    def lambda_AF49():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_AF49)

    Sleep(50)

    @scena.Lambda('lambda_AF5C')
    def lambda_AF5C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AF5C)

    @scena.Lambda('lambda_AF6A')
    def lambda_AF6A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_AF6A)

    Sleep(50)

    @scena.Lambda('lambda_AF7D')
    def lambda_AF7D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_AF7D)

    @scena.Lambda('lambda_AF8B')
    def lambda_AF8B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_AF8B)

    Sleep(400)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010200288V#1026F#5P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030341284V#026F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341285V#020F到达后就要出发了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B062',
    )

    Call(0, 0x002C)

    def _loc_B062(): pass

    label('loc_B062')

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择固定队员外的一名同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(500)

    OP_A2(0x1E11)
    SetMapFlags(0x02000000)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0027 offset: 0xB105
@scena.Code('func_27_B105')
def func_27_B105():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B11C',
    )

    Call(0, 0x002C)
    Call(0, 0x002D)

    def _loc_B11C(): pass

    label('loc_B11C')

    OP_6D(-1320, 2000, 87840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -1320, 2000, 87840, 180)
    SetChrPos(0x0001, -1320, 2000, 87840, 180)
    SetChrPos(0x0002, -1320, 2000, 87840, 180)
    SetChrPos(0x0003, -1320, 2000, 87840, 180)
    SetChrPos(0x000C, -1900, 2000, 93320, 0)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -2920, 2000, 49050, 180)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B1F8',
    )

    SetChrPos(0x000A, 80, 2000, 91070, 0)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_B1F8(): pass

    label('loc_B1F8')

    OP_28(0x009A, 0x01, 0x0080)
    OP_28(0x009A, 0x01, 0x0100)
    OP_28(0x009A, 0x01, 0x0200)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0028 offset: 0xB220
@scena.Code('func_28_B220')
def func_28_B220():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    OP_6D(460, 2000, 94360, 0)
    OP_67(0, 4750, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -310, 2000, 91660, 0)
    SetChrPos(0x0102, -1460, 2000, 91520, 0)
    SetChrPos(0x0013, -2630, 2000, 90470, 0)
    SetChrPos(0x000A, 220, 2020, 90650, 0)
    SetChrPos(0x0012, -2550, 2000, 89380, 0)
    SetChrPos(0x0008, -1000, 2020, 90140, 0)
    SetChrPos(0x000B, -80, 2000, 89260, 0)
    SetChrPos(0x0014, -1380, 2000, 88780, 0)
    SetChrPos(0x000E, -1040, 200, 99240, 0)
    SetChrPos(0x000F, -3530, 200, 99080, 315)
    SetChrPos(0x0010, 1380, 200, 99090, 45)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    TerminateThread(0x0012, 0xFF)
    SetChrSubChip(0x0012, 0)
    SetChrChipByIndex(0x0012, 15)
    OP_4A(0x000A, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrSubChip(0x000C, 2)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x000C, 18)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x000F, 8)
    SetChrChipByIndex(0x0010, 9)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0010)
    SetChrPos(0x000C, -920, 2100, 93680, 0)
    SetChrPos(0x000E, -1040, 100, 99020, 0)
    SetChrPos(0x000F, -3400, 100, 98950, 315)
    SetChrPos(0x0010, 1300, 100, 98950, 45)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100341430V#178F#5P已到达『琥珀之塔』上空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341431V来自侦察部队的后续报告也\n',
            '终于传过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341432V#176F……从塔中现身的袭击者\n',
            '是一名手持巨大镰刀的少女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341433V#1003F#4P是吗……\n',
            '我也已经猜到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070341434V#063F#6P……小玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341435V#1035F#6P『歼灭天使』玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341436V当初我在结社的时候，\n',
            '她还是候补『执行者』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341437V#1043F想不到她竟已能操纵\n',
            '那架『帕蒂尔·玛蒂尔』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010341438V#1004F#2P约修亚……\n',
            '你知道那架巨大机器人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020341439V#1042F#6P那是结社的实验室开发的\n',
            '战略级巨大人形兵器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341440V因为操控困难，所以开发计划\n',
            '应该已被冻结了才对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180341441V#1063F#4P那个女孩子\n',
            '可以轻松地操控吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180341442V#1068F真是个可怕的小家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070341443V#561F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0013, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010341444V#1006F#5P没事的，提妲。\n',
            '别摆出这样的表情嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341445V我一定会让那孩子\n',
            '醒过来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0070341446V#560F#6P姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341447V#1043F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010341448V#1015F#2P那个……\n',
            '我是不是有点太乐观了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341449V#1035F#6P……不。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341450V#1040F说不定你……\n',
            '真的能进入那孩子的心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341451V让我们一起呼唤她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341452V#1016F#2P……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B945',
    )

    Call(0, 0x002C)

    def _loc_B945(): pass

    label('loc_B945')

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    OP_6D(-1160, 2000, 46570, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -1160, 2000, 46570, 180)
    SetChrPos(0x0001, -1160, 2000, 46570, 180)
    SetChrPos(0x0002, -1160, 2000, 46570, 180)
    SetChrPos(0x0003, -1160, 2000, 46570, 180)
    OP_28(0x009A, 0x01, 0x0400)
    OP_28(0x009A, 0x01, 0x0800)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x02)
    SetMapFlags(0x00000001)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0029 offset: 0xBA77
@scena.Code('func_29_BA77')
def func_29_BA77():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    SetChrPos(0x0101, -290, 2000, 90360, 0)
    SetChrPos(0x0102, -1500, 2000, 90260, 0)
    SetChrPos(0x0013, -1660, 2000, 88720, 0)
    SetChrPos(0x0014, 500, 2000, 89150, 0)
    SetChrPos(0x0012, -1880, 2000, 87500, 0)
    SetChrPos(0x0008, -2540, 2000, 88900, 0)
    SetChrPos(0x000B, -140, 2000, 87500, 0)
    SetChrPos(0x000A, -490, 2000, 88880, 0)
    ChrTurnDirection(0x0101, 0x000C, 0)
    ChrTurnDirection(0x0102, 0x000C, 0)
    ChrTurnDirection(0x0013, 0x000C, 0)
    ChrTurnDirection(0x000A, 0x000C, 0)
    ChrTurnDirection(0x0012, 0x000C, 0)
    ChrTurnDirection(0x0008, 0x000C, 0)
    ChrTurnDirection(0x000B, 0x000C, 0)
    ChrTurnDirection(0x0014, 0x000C, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    TerminateThread(0x0012, 0xFF)
    SetChrSubChip(0x0012, 0)
    SetChrChipByIndex(0x0012, 15)
    OP_4A(0x000A, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x000F, 8)
    SetChrChipByIndex(0x0010, 9)
    SetChrChipByIndex(0x000C, 4)
    SetChrPos(0x000C, -1130, 2000, 92290, 180)
    SetChrPos(0x000E, -1040, 100, 99020, 0)
    SetChrPos(0x000F, -3400, 100, 98950, 315)
    SetChrPos(0x0010, 1300, 100, 98950, 45)
    OP_6D(-10, 2000, 92570, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x007A, 0x01, 0x46)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100341734V#176F#5P出现在各地的机器人和\n',
            '装甲兽已经基本上被消灭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341735V#171F警戒体制虽然还在持续，\n',
            '不过应该也快要解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060341736V#542F#4P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050341737V#051F#6P虽然还有诸多不明之处，\n',
            '不过『塔』的异变也已得到平息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341738V感觉可以松口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030341739V#524F#6P说得也是……\n',
            '如果是这样就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080341740V#074F#4P可是……\n',
            '怎么也看不出敌人的意图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341741V#1003F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180341742V#1063F#4P艾丝蒂尔，\n',
            '你好像很没精神呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180341743V是因为那小家伙的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341744V#1007F#6P……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BEAF')
    def lambda_BEAF():
        OP_6D(-10, 2000, 91570, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BEAF)

    OP_8C(0x0101, 180, 400)

    @scena.Lambda('lambda_BECE')
    def lambda_BECE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BECE)

    @scena.Lambda('lambda_BEDC')
    def lambda_BEDC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_BEDC)

    Sleep(50)

    @scena.Lambda('lambda_BEEF')
    def lambda_BEEF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_BEEF)

    @scena.Lambda('lambda_BEFD')
    def lambda_BEFD():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_BEFD)

    Sleep(50)

    @scena.Lambda('lambda_BF10')
    def lambda_BF10():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_BF10)

    @scena.Lambda('lambda_BF1E')
    def lambda_BF1E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_BF1E)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010341745V#1025F#5P我明明不知道她受过的苦，\n',
            '还自以为是地对她大加指责，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341746V会不会已经伤害到她了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070280780V#063F#6P姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060210934V#043F#4P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341749V#1003F#5P像我这种人，既没有人生阅历，\n',
            '又总是被大家保护着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341750V怎么可能有资格去\n',
            '拯救那孩子呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341751V#1007F我真是太异想天开了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341752V#1040F#6P……你说得不对哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341753V#1004F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020341754V#1035F#6P玲她……\n',
            '其实是个真正的天才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341755V瞬间吸收所有信息\n',
            '并将其转换为自己的力量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341756V迅速适应任何环境，\n',
            '并逐渐控制自己和周遭环境……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341757V#1042F她似乎天生\n',
            '就具备了这种才能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341758V#1026F#2P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341759V#1043F#6P在被『结社』收留之前，\n',
            '那孩子所处的环境\n',
            '非常残酷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341760V但是，和我不同，\n',
            '那孩子的心并没有坏掉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341761V#1035F因为她可以承受任何逆境，\n',
            '并强迫自己去接受、适应......',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341762V所以才能够在这样的遭遇下保持自我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341763V#1020F#2P不、不过这样的话……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341764V#1043F#6P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341765V无论再怎么控制感情，\n',
            '我想心也不可能不会痛的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341766V#1026F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341767V#1035F#6P在我的印象中，\n',
            '从来没有见过玲\n',
            '像这次这样激动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341768V我想大概是你的话\n',
            '触碰到了连玲自己\n',
            '也没有察觉的真实情感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341769V#1040F……这是只有你才能做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341770V#1025F#2P约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341771V#1007F……既然这样的话，\n',
            '我也不能一直垂头丧气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341772V#1022F#6P你看着吧～玲！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341773V#1005F下次见面，我一定要\n',
            '彻底面对真实的你！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070341774V#067F#6P姐、姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030341775V#027F#6P呵呵，真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180341776V#1061F#4P哈哈。\n',
            '这才是艾丝蒂尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 225, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010341777V#1016F#5P嗯，先不说这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341778V#1015F总之，我们接下来该怎么办？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341779V既然不明白『结社』的意图，\n',
            '回王都也不太合适……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100341780V#170F#5P这样的话，今天\n',
            '先去一下雷斯顿要塞怎样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341781V这样一来也可以和\n',
            '卡西乌斯准将讨论今后的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C6FB')
    def lambda_C6FB():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C6FB)

    @scena.Lambda('lambda_C709')
    def lambda_C709():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C709)

    Sleep(50)

    @scena.Lambda('lambda_C71C')
    def lambda_C71C():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_C71C)

    @scena.Lambda('lambda_C72A')
    def lambda_C72A():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_C72A)

    Sleep(50)

    @scena.Lambda('lambda_C73D')
    def lambda_C73D():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_C73D)

    @scena.Lambda('lambda_C74B')
    def lambda_C74B():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_C74B)

    Sleep(50)

    @scena.Lambda('lambda_C75E')
    def lambda_C75E():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_C75E)

    @scena.Lambda('lambda_C76C')
    def lambda_C76C():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_C76C)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010341782V#1004F#4P啊，也对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341783V#1040F#6P这样的确比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060341784V#040F#4P那么，尤莉亚小姐，\n',
            '请带我们前往雷斯顿要塞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100341785V#171F#5P明白──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -1040, 2000, 83000, 0)

    NpcTalk(
        0x0011,
        '老人的声音',
        (
            '#0540341786V#1P不、不好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0013, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_C976')
    def lambda_C976():
        OP_6D(-130, 2000, 90500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C976)

    @scena.Lambda('lambda_C98E')
    def lambda_C98E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_C98E)

    @scena.Lambda('lambda_C9A0')
    def lambda_C9A0():
        OP_8E(0x00FE, -1200, 2000, 86000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_C9A0)

    @scena.Lambda('lambda_C9BB')
    def lambda_C9BB():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C9BB)

    @scena.Lambda('lambda_C9C9')
    def lambda_C9C9():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C9C9)

    Sleep(50)

    @scena.Lambda('lambda_C9DC')
    def lambda_C9DC():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_C9DC)

    @scena.Lambda('lambda_C9EA')
    def lambda_C9EA():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_C9EA)

    Sleep(50)

    @scena.Lambda('lambda_C9FD')
    def lambda_C9FD():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_C9FD)

    @scena.Lambda('lambda_CA0B')
    def lambda_CA0B():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_CA0B)

    Sleep(50)

    @scena.Lambda('lambda_CA1E')
    def lambda_CA1E():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_CA1E)

    @scena.Lambda('lambda_CA2C')
    def lambda_CA2C():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_CA2C)

    Sleep(50)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0011, 0x0003)

    ChrTalk(
        0x0013,
        (
            '#0070341787V#064F#5P爷、爷爷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341788V#1015F#5P怎、怎么了？\n',
            '这么惊慌的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540341789V#105F#4P这是你们在塔上找到的\n',
            '数据水晶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341790V刚才『卡佩尔』\n',
            '分析了其中的一个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341791V#1004F#5P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341792V#1042F#5P上面记载着什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540341793V#105F#4P『设备塔』的功能！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341794V四座塔是为了将『辉之环』\n',
            '维系于异次元\n',
            '而建造出来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341795V#1020F#5P异、异次元……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341796V#1044F#5P『辉之环』在那种地方！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180341797V#1064F#5P等、等一等！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180341798V那么莫非\n',
            '那些『里塔』的空间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540341799V#104F#4P嗯，应该也是\n',
            '属于异次元的空间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341800V#102F而『福音』的真面目是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName('男人的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150341801V──没错。\n',
            '是『辉之环』的『终端』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_1D(0x5A)
    Sleep(500)

    @scena.Lambda('lambda_CE3F')
    def lambda_CE3F():
        OP_6D(1970, 2000, 92640, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_CE3F)

    @scena.Lambda('lambda_CE57')
    def lambda_CE57():
        OP_67(0, 5150, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_CE57)

    @scena.Lambda('lambda_CE6F')
    def lambda_CE6F():
        OP_8C(0x00FE, 45, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_CE6F)

    @scena.Lambda('lambda_CE7D')
    def lambda_CE7D():
        OP_8C(0x00FE, 45, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_CE7D)

    Sleep(50)

    @scena.Lambda('lambda_CE90')
    def lambda_CE90():
        OP_8C(0x00FE, 45, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_CE90)

    @scena.Lambda('lambda_CE9E')
    def lambda_CE9E():
        OP_8C(0x00FE, 45, 500)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_CE9E)

    Sleep(50)

    @scena.Lambda('lambda_CEB1')
    def lambda_CEB1():
        OP_8C(0x00FE, 45, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_CEB1)

    @scena.Lambda('lambda_CEBF')
    def lambda_CEBF():
        OP_8C(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_CEBF)

    Sleep(50)

    @scena.Lambda('lambda_CED2')
    def lambda_CED2():
        OP_8C(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_CED2)

    @scena.Lambda('lambda_CEE0')
    def lambda_CEE0():
        OP_8C(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_CEE0)

    Sleep(50)

    @scena.Lambda('lambda_CEF3')
    def lambda_CEF3():
        OP_8C(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_CEF3)

    OP_72(0x000C, 0x0004)
    OP_6F(0x000C, 0)
    OP_70(0x000C, 0x0000003C)
    Sleep(150)

    OP_22(0x0127, 0x00, 0x64)
    OP_73(0x000C)
    WaitForThreadExit(0x0101, 0x0002)
    OP_22(0x009D, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    OP_74(0x000C, 0x00000006, 0x0003)
    OP_74(0x000C, 0x00000008, 0x0003)
    OP_74(0x000C, 0x0000000A, 0x0003)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0102,
        (
            '#0020341802V#1042F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341803V#1020F#6P教、教授！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050341804V#052F#6P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060341805V#044F#4P这、这个人就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180341806V#1063F#4P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100341807V#173F#6P为、为什么他能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341808V#177F利昂！\n',
            '到底是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3850341809V#6P我、我不知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3850341810V#6P刚才收到了一个通讯，\n',
            '控制权就突然被夺走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540341811V#104F#2P这就是所谓的系统入侵吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341812V#102F高精度的智能信息处理系统\n',
            '似乎反倒是成了麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName('怀斯曼教授')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150341813V哼哼……\n',
            '初次见面，拉赛尔博士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341814V这么了不起的系统\n',
            '竟然能凭一己之力完成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341815V不愧是爱普斯泰恩博士的\n',
            '入室弟子之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0011,
        (
            '#0540341816V#102F#2P哼，这算是挖苦吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341817V#104F我告诉你，航行控制\n',
            '是独立于系统的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341818V就算你想操控也是白费心机！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName('怀斯曼教授')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150341819V哪里哪里，\n',
            '我当然不会这么做了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341820V只是不想让诸位\n',
            '错过难得的决定性瞬间，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341821V所以才特意前来通知的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0011,
        (
            '#0540341822V#102F#2P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341823V#1046F#6P决定性瞬间……难道是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName('怀斯曼教授')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150341824V呵呵，你们就到\n',
            '前方甲板上去欣赏吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150341825V那么诸位，祝晚上愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_22(0x009D, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    OP_74(0x000C, 0x00000006, 0x0000)
    OP_74(0x000C, 0x00000008, 0x0000)
    OP_74(0x000C, 0x0000000A, 0x0000)
    OP_0D()
    Sleep(200)

    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0101, 0x0102, 600)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010341826V#1005F#2P约修亚……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 600)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020341827V#1042F#6P嗯……去甲板上看看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(ItemTable['数据水晶４'], 1)
    RemoveItem(ItemTable['数据水晶５'], 1)
    RemoveItem(ItemTable['数据水晶６'], 1)
    RemoveItem(ItemTable['数据水晶７'], 1)
    RemoveItem(ItemTable['数据水晶８'], 1)
    RemoveItem(ItemTable['数据水晶９'], 1)
    RemoveItem(ItemTable['数据水晶１０'], 1)
    RemoveItem(ItemTable['数据水晶１１'], 1)
    RemoveItem(ItemTable['数据水晶１２'], 1)
    RemoveItem(ItemTable['数据水晶１３'], 1)
    RemoveItem(ItemTable['数据水晶１４'], 1)
    RemoveItem(ItemTable['数据水晶１５'], 1)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F9)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002A offset: 0xD4E8
@scena.Code('func_2A_D4E8')
def func_2A_D4E8():
    SetChrFlags(0x00FE, 0x1000)
    SetChrChipByIndex(0x0101, 25)
    OP_8E(0x00FE, -3460, 2000, 89980, 6000, 0x00)
    OP_8E(0x00FE, -3640, 2000, 86920, 6000, 0x00)
    OP_8E(0x00FE, -820, 2000, 85600, 6000, 0x00)

    @scena.Lambda('lambda_D534')
    def lambda_D534():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_D534)

    OP_8E(0x00FE, -1140, 2000, 83660, 6000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002B offset: 0xD55A
@scena.Code('func_2B_D55A')
def func_2B_D55A():
    SetChrFlags(0x00FE, 0x1000)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -3460, 2000, 89980, 6000, 0x00)
    OP_8E(0x00FE, -3640, 2000, 86920, 6000, 0x00)
    OP_8E(0x00FE, -820, 2000, 85600, 6000, 0x00)

    @scena.Lambda('lambda_D5A6')
    def lambda_D5A6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_D5A6)

    OP_8E(0x00FE, -1140, 2000, 83660, 6000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x002C offset: 0xD5CC
@scena.Code('func_2C_D5CC')
def func_2C_D5CC():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D646'),
        (0x00000001, 'loc_D64C'),
        (-1, 'loc_D652'),
    )

    def _loc_D646(): pass

    label('loc_D646')

    OP_A2(0x1200)

    Jump('loc_D652')

    def _loc_D64C(): pass

    label('loc_D64C')

    OP_A2(0x1201)

    Jump('loc_D652')

    def _loc_D652(): pass

    label('loc_D652')

    Return()

# id: 0x002D offset: 0xD653
@scena.Code('func_2D_D653')
def func_2D_D653():
    FadeOut(0, 0, -1)
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x002E offset: 0xD6E0
@scena.Code('func_2E_D6E0')
def func_2E_D6E0():
    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_D6FE'),
        (0x00000002, 'loc_D768'),
        (0x00000004, 'loc_D7DC'),
        (0x00000003, 'loc_D846'),
        (0x00000007, 'loc_D8B7'),
        (-1, 'loc_D925'),
    )

    def _loc_D6FE(): pass

    label('loc_D6FE')

    ChrTalk(
        0x0101,
        (
            '#0010310546V#1016F啊，这里是船的后侧呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310547V#1008F传说中的龙啊……\n',
            '心里真是七上八下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D925')

    def _loc_D768(): pass

    label('loc_D768')

    ChrTalk(
        0x0103,
        (
            '#0030310548V#025F……这里是后甲板呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310549V#020F传说中究竟是什么样子，\n',
            '真想赶快近距离好好确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D925')

    def _loc_D7DC(): pass

    label('loc_D7DC')

    ChrTalk(
        0x0105,
        (
            '#0060310550V#047F这里是船尾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310551V#042F……从古代活到现在的龙。\n',
            '必须好好看个清楚才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D925')

    def _loc_D846(): pass

    label('loc_D846')

    ChrTalk(
        0x0104,
        (
            '#0040310552V#033F哎呀，这是船尾吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310553V#035F……呵呵，连我在\n',
            '传说中的龙面前\n',
            '似乎也略感紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D925')

    def _loc_D8B7(): pass

    label('loc_D8B7')

    ChrTalk(
        0x0108,
        (
            '#0080310554V#073F哟，这边是船尾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310555V#070F……对方可是传说中的角色。\n',
            '一定要亲眼看个仔细。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D925')

    def _loc_D925(): pass

    label('loc_D925')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002F offset: 0xD941
@scena.Code('func_2F_D941')
def func_2F_D941():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DB3F',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_D96B'),
        (0x00000002, 'loc_D9C6'),
        (0x00000004, 'loc_DA1B'),
        (0x00000003, 'loc_DA74'),
        (0x00000007, 'loc_DACB'),
        (-1, 'loc_DB24'),
    )

    def _loc_D96B(): pass

    label('loc_D96B')

    ChrTalk(
        0x0101,
        (
            '#0010310556V#1007F下去也没意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310557V#1000F……现在赶紧去龙所在的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB24')

    def _loc_D9C6(): pass

    label('loc_D9C6')

    ChrTalk(
        0x0103,
        (
            '#0030310558V#026F下去也没意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310559V#020F……赶紧去龙所在的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB24')

    def _loc_DA1B(): pass

    label('loc_DA1B')

    ChrTalk(
        0x0105,
        (
            '#0060310560V#047F下去也没意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310561V#042F……现在赶紧去龙所在的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB24')

    def _loc_DA74(): pass

    label('loc_DA74')

    ChrTalk(
        0x0104,
        (
            '#0040310562V#030F……传说中的角色近在眼前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310563V#035F没必要绕道了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB24')

    def _loc_DACB(): pass

    label('loc_DACB')

    ChrTalk(
        0x0108,
        (
            '#0080310564V#074F下去也没意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310565V#070F……现在赶紧去龙所在的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB24')

    def _loc_DB24(): pass

    label('loc_DB24')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_DB3F(): pass

    label('loc_DB3F')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
