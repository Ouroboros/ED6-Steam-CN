import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5900_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5900   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉扎德'),
    TXT(0x02, '奥利维尔'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '阿加特'),
    TXT(0x05, '提妲'),
    TXT(0x06, '金'),
    TXT(0x07, '凯文神父'),
    TXT(0x08, '拉赛尔博士'),
    TXT(0x09, '奈尔'),
    TXT(0x0A, '朵洛希'),
    TXT(0x0B, '穆拉少校'),
    TXT(0x0C, '尤莉亚上尉'),
    TXT(0x0D, '基库'),
    TXT(0x0E, '操舵士勒克司'),
    TXT(0x0F, '菲'),
    TXT(0x10, '乔丝特'),
    TXT(0x11, '亲卫队队员'),
    TXT(0x12, '亲卫队队员'),
    TXT(0x13, '亲卫队队员'),
    TXT(0x14, '亲卫队队员'),
    TXT(0x15, '库莱泽'),
    TXT(0x16, '公园区域『卡尔玛丽』２'),
    TXT(0x17, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5900.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6BF6
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
        ('ED6_DT27/CH03210._CH', 'ED6_DT27/CH03210P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT27/CH03860._CH', 'ED6_DT27/CH03860P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
        ('ED6_DT27/CH04107._CH', 'ED6_DT27/CH04107P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10002 offset: 0x152
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
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
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13600,
            z                   = 0,
            y                   = 37280,
            direction           = 236,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -21910,
            z                   = 3500,
            y                   = 23300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -20140,
            z                   = 3500,
            y                   = 22380,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 2830,
            z                   = 0,
            y                   = 28680,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -24350,
            z                   = 0,
            y                   = 18840,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -21600,
            z                   = 0,
            y                   = 15040,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -24920,
            z                   = 0,
            y                   = 16710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -13210,
            z                   = -3390,
            y                   = 27060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -10,
            z                   = 0,
            y                   = -43810,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
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
            x           = -16900,
            y           = -3300,
            z           = 24600,
            range       = -15900,
            dword_10    = 0xFFFFFAEC,
            dword_14    = 0x000067E8,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = -24500,
            y           = 3200,
            z           = 26800,
            range       = -23500,
            dword_10    = 0x00001450,
            dword_14    = 0x00007080,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = -2800,
            y           = 0,
            z           = -34600,
            range       = 2700,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFF7CC0,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001E,
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
        'loc_7C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_532',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -38250, 4500, 28710, 180)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -45190, 5000, 33140, 45)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4E9',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -17120, 3500, 23510, 135)

    def _loc_4E9(): pass

    label('loc_4E9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_50C',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -20610, 0, 16960, 315)

    def _loc_50C(): pass

    label('loc_50C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_52F',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -23120, 0, 16149, 0)

    def _loc_52F(): pass

    label('loc_52F')

    Jump('loc_7C0')

    def _loc_532(): pass

    label('loc_532')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_670',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -43870, 5000, 31520, 225)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -39890, 4500, 33700, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 2, 0x229A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_573',
    )

    SetChrFlags(0x0011, 0x0010)

    def _loc_573(): pass

    label('loc_573')

    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, -18420, 3500, 22380, 227)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrPos(0x0019, 1440, -4000, 23570, 45)
    ClearChrFlags(0x001A, 0x0080)
    SetChrPos(0x001A, 33290, -4000, 16740, 225)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001C, -11560, 0, 34340, 262)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 4340, -4000, 19880, 315)
    CreateThread(0x0012, 0x00, 0x06, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_615',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 4310, -4000, 22130, 315)

    def _loc_615(): pass

    label('loc_615')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_627',
    )

    ClearChrFlags(0x0017, 0x0080)

    def _loc_627(): pass

    label('loc_627')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_64A',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 5070, -3880, 23930, 270)

    def _loc_64A(): pass

    label('loc_64A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_66D',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 11730, -4000, 18510, 90)

    def _loc_66D(): pass

    label('loc_66D')

    Jump('loc_7C0')

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_736',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -18600, 3500, 25160, 35)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 10, -4000, 24410, 90)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 14280, 0, 25700, 135)
    CreateThread(0x0012, 0x00, 0x06, 0x0002)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001C, -16370, 3500, 27040, 170)
    ClearChrFlags(0x001B, 0x0080)
    SetChrPos(0x001B, 14760, -4000, 19280, 225)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_710',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 34850, -4000, 16079, 225)

    def _loc_710(): pass

    label('loc_710')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_733',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 11730, -4000, 18510, 90)

    def _loc_733(): pass

    label('loc_733')

    Jump('loc_7C0')

    def _loc_736(): pass

    label('loc_736')

    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001C, -22940, 0, 39040, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_792',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_792',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -18510, 3500, 22430, 180)
    CreateThread(0x0008, 0x00, 0x06, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 1, 0x22A1)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_792',
    )

    SetChrFlags(0x0008, 0x0010)

    def _loc_792(): pass

    label('loc_792')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7C0',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7C0',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -43550, 5000, 31240, 225)

    def _loc_7C0(): pass

    label('loc_7C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_7D3',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0013)

    def _loc_7D3(): pass

    label('loc_7D3')

    Return()

# id: 0x0001 offset: 0x7D4
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFE3EC8, 0x00230079)

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x01C3, 0x01, 0x50)
    OP_22(0x01C7, 0x01, 0x64)

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_837',
    )

    OP_71(0x0004, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_72(0x0012, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)

    Jump('loc_873')

    def _loc_837(): pass

    label('loc_837')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_855',
    )

    OP_71(0x0004, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_72(0x0012, 0x0004)

    Jump('loc_873')

    def _loc_855(): pass

    label('loc_855')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_86E',
    )

    OP_71(0x0004, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_71(0x0012, 0x0004)

    Jump('loc_873')

    def _loc_86E(): pass

    label('loc_86E')

    OP_71(0x0012, 0x0004)

    def _loc_873(): pass

    label('loc_873')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_8C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88F',
    )

    OP_D2(0x000600FC, 0x00060101, 0x15)

    Jump('loc_8C3')

    def _loc_88F(): pass

    label('loc_88F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8A4',
    )

    OP_D2(0x000600FC, 0x00060101, 0x15)

    Jump('loc_8C3')

    def _loc_8A4(): pass

    label('loc_8A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8B9',
    )

    OP_D2(0x000600FC, 0x00060101, 0x15)

    Jump('loc_8C3')

    def _loc_8B9(): pass

    label('loc_8B9')

    OP_D2(0x000600FC, 0x00060101, 0x15)

    def _loc_8C3(): pass

    label('loc_8C3')

    Return()

# id: 0x0002 offset: 0x8C4
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_CE0',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B9D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 1, 0x2299)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ACC',
    )

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x010B, 0)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0270400753V#143F哦，莫非你是\n',
            '空贼团的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400754V#210F呵呵，是啊。\n',
            '我是卡普亚一家的乔丝特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270400755V#141F哦，果然没错啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400756V下次有时间的话，\n',
            '把你们的故事说给我听听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400757V#212F不好意思，如果是利贝尔通讯\n',
            '的采访的话我拒绝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400758V写了那么多别人的坏话，\n',
            '居然还好意思说这些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270400759V#147F这、这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400760V你也希望有一个\n',
            '澄清的机会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400761V#214F不───要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x2299)

    Jump('loc_B9A')

    def _loc_ACC(): pass

    label('loc_ACC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B36',
    )

    ChrTurnDirection(0x0010, 0x010B, 0)

    ChrTalk(
        0x0010,
        (
            '#0270400762V#147F拜托你\n',
            '别拒绝我的采访。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400763V这、这次我不会\n',
            '把你们写坏的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B9A')

    def _loc_B36(): pass

    label('loc_B36')

    ChrTurnDirection(0x0010, 0x010B, 0)

    ChrTalk(
        0x0010,
        (
            '#0270400764V#147F拜托，请你别\n',
            '拒绝我的采访。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400763V这、这次我不会\n',
            '把你们写坏的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B9A(): pass

    label('loc_B9A')

    Jump('loc_CDD')

    def _loc_B9D(): pass

    label('loc_B9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C74',
    )

    ChrTalk(
        0x0010,
        (
            '#0270400766V#140F想不到卡普亚一家\n',
            '居然会来到这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400767V有机会的话真想\n',
            '拍张空贼艇的照片呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400768V不过毕竟还是没办法\n',
            '在这种地方乱晃。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400769V好吧，先老老实实地\n',
            '等待机会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_CDD')

    def _loc_C74(): pass

    label('loc_C74')

    ChrTalk(
        0x0010,
        (
            '#0270400770V#142F想不到卡普亚一家\n',
            '居然会来到这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400771V真是有够命大的。\n',
            '简直就像杂草一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CDD(): pass

    label('loc_CDD')

    Jump('loc_E25')

    def _loc_CE0(): pass

    label('loc_CE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_E25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DBA',
    )

    ChrTalk(
        0x0010,
        (
            '#0270400772V#143F重新看了一下才发现，\n',
            '这还真是个不得了的东西呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400773V虽然有点晚，不过还是让我\n',
            '想起了『七至宝』的传说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400774V#145F女神授予的宝物……吗？\n',
            '看来不只是传说而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_E25')

    def _loc_DBA(): pass

    label('loc_DBA')

    ChrTalk(
        0x0010,
        (
            '#0270400775V#145F抱歉，让我一个人\n',
            '静一静吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270400776V多年积累的常识突然崩溃，\n',
            '我的脑子里有点乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E25(): pass

    label('loc_E25')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0xE29
@scena.Code('func_03_E29')
def func_03_E29():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_14AC',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_139D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 2, 0x229A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12D7',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(-38760, 4500, 32630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -37750, 4500, 32580, 298)
    SetChrPos(0x0102, -39650, 4500, 31210, 360)
    SetChrPos(0x010B, -38490, 4500, 31610, 317)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EE1',
    )

    SetChrPos(0x00F9, -37690, 4500, 30730, 307)

    Jump('loc_EF2')

    def _loc_EE1(): pass

    label('loc_EE1')

    SetChrPos(0x00F8, -37690, 4500, 30730, 307)

    def _loc_EF2(): pass

    label('loc_EF2')

    OP_0D()
    ClearChrFlags(0x0011, 0x0010)
    ChrTurnDirection(0x0011, 0x010B, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0280400777V#151F哇，好可爱的护目镜！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400778V请问－－，不好意思，\n',
            '能不能请您摆个ＰＯＳＥ？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F82')
    def lambda_0F82():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F82)

    @scena.Lambda('lambda_0F90')
    def lambda_0F90():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F90)

    ChrTalk(
        0x010B,
        (
            '#0090400779V#213F啊！？ＰＯＳＥ？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0011, 14)

    ChrTalk(
        0x0011,
        (
            '#0280400780V#153F快点，不然我就要\n',
            '拍了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400781V#216F那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x010B, 15)
    OP_0D()

    ChrTalk(
        0x010B,
        (
            '#0090400782V#214F……这、这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0280400783V#151F嗯嗯，很好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(
        0x0011,
        (
            '#0280400784V#151F再来一张～\n',
            '这次要更可爱点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400785V#413F那、那么就这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x010B, 16)
    OP_0D()

    ChrTalk(
        0x0011,
        (
            '#0280400786V#151F哇，很棒的感觉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Fade(500)
    SetChrChipByIndex(0x0011, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0280400787V#151F好～拍摄完毕～\n',
            '谢谢您的配合～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0011, 0, 400)
    Fade(400)
    SetChrChipByIndex(0x010B, 65535)
    OP_0D()
    OP_6D(-38090, 4500, 31080, 1000)

    ChrTalk(
        0x010B,
        (
            '#0090400788V#213F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400789V#215F……咦？刚才那是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400790V#1040F就像是在打个招呼之类的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400791V#1016F不、不过变得\n',
            '比以前更变本加厉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    SetMapFlags(0x02000000)
    OP_A2(0x0005)
    OP_A2(0x229A)

    Jump('loc_139A')

    def _loc_12D7(): pass

    label('loc_12D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1333',
    )

    ChrTalk(
        0x0011,
        (
            '#0280400792V#150F嘿嘿，也因此\n',
            '拍到了很好的照片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400793V谢谢您的配合～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139A')

    def _loc_1333(): pass

    label('loc_1333')

    ChrTalk(
        0x0011,
        (
            '#0280400794V#151F从这里看的话，\n',
            '天空显得特别接近哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400795V呼～感觉整个人\n',
            '要被吸进去似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_139A(): pass

    label('loc_139A')

    Jump('loc_14A9')

    def _loc_139D(): pass

    label('loc_139D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1442',
    )

    ChrTalk(
        0x0011,
        (
            '#0280400794V#151F从这里看的话，\n',
            '天空显得特别接近哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400795V呼～感觉整个人\n',
            '要被吸进去似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400798V#1019F……别掉下去啊，朵洛希。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_14A9')

    def _loc_1442(): pass

    label('loc_1442')

    ChrTalk(
        0x0011,
        (
            '#0280400794V#151F从这里看的话，\n',
            '天空显得特别接近哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400795V呼～感觉整个人\n',
            '要被吸进去似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A9(): pass

    label('loc_14A9')

    Jump('loc_15E5')

    def _loc_14AC(): pass

    label('loc_14AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_15E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_157C',
    )

    ChrTalk(
        0x0011,
        (
            '#0280400801V#151F哇，好棒的景色！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400802V空气清新又宜人，\n',
            '真想住在这里呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400803V#154F啊，不过没工房的话\n',
            '就买不到感光结晶回路了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400804V嗯～这个就\n',
            '有点伤脑筋了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_15E5')

    def _loc_157C(): pass

    label('loc_157C')

    ChrTalk(
        0x0011,
        (
            '#0280400805V#150F这里景色好棒，\n',
            '真想住在这里试试～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280400806V要不要干脆把整个\n',
            '编辑部都搬过来呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E5(): pass

    label('loc_15E5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x15E9
@scena.Code('func_04_15E9')
def func_04_15E9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_15F6',
    )

    Jump('loc_1A37')

    def _loc_15F6(): pass

    label('loc_15F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_17EA',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1693',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在调整飞翔引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是很困难的作业，\n',
            '不过这也是最后的难题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '距离修复完成只差一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16ED')

    def _loc_1693(): pass

    label('loc_1693')

    ChrTalk(
        0x00FE,
        (
            '飞翔引擎的调整\n',
            '是最后的难关了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要这方面顺利的话，\n',
            '距离修复完成只差一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16ED(): pass

    label('loc_16ED')

    Jump('loc_17E7')

    def _loc_16F0(): pass

    label('loc_16F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1785',
    )

    ChrTalk(
        0x00FE,
        (
            '现在我正在调整\n',
            '飞翔引擎的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为飞船是一种借由推力平衡的\n',
            '偏向来改变方向的交通工具……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '引擎的调整就\n',
            '相当于舵的调整。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_17E7')

    def _loc_1785(): pass

    label('loc_1785')

    ChrTalk(
        0x00FE,
        (
            '因为飞船是一种借由推力平衡的\n',
            '偏向来改变方向的交通工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '引擎的调整\n',
            '有着非常重要的意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E7(): pass

    label('loc_17E7')

    Jump('loc_1A37')

    def _loc_17EA(): pass

    label('loc_17EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_1A30',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 0, 0x22D0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18ED',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x00FE,
        (
            '哦，我还在想怎么会有\n',
            '陌生的面孔出现呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来如此，你是\n',
            '那个空贼团的女孩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，还真没想到\n',
            '会和你们合作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，虽然感觉很复杂，\n',
            '不过这段时间还是要拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在真是忙得\n',
            '不可开交啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001E)
    OP_A2(0x22D0)

    Jump('loc_1A2D')

    def _loc_18ED(): pass

    label('loc_18ED')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 6, 0x1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_196E',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x00FE,
        (
            '虽然和你们合作\n',
            '感觉很复杂……',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '不过这段时间还是要拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在真是忙得\n',
            '不可开交啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A2D')

    def _loc_196E(): pass

    label('loc_196E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19D1',
    )

    ChrTalk(
        0x00FE,
        (
            '修复左舷脱落的支架\n',
            '是最庞大的工程呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须借助大家的\n',
            '智慧一起来想办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A2D')

    def _loc_19D1(): pass

    label('loc_19D1')

    ChrTalk(
        0x00FE,
        (
            '修复左舷脱落的支架\n',
            '是个巨大的工程哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此，必须借助大家的\n',
            '智慧一起来想办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A2D(): pass

    label('loc_1A2D')

    Jump('loc_1A37')

    def _loc_1A30(): pass

    label('loc_1A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_1A37',
    )

    def _loc_1A37(): pass

    label('loc_1A37')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1A3B
@scena.Code('func_05_1A3B')
def func_05_1A3B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_2016',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 3, 0x229B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C77',
    )

    ChrTurnDirection(0x0016, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，又碰到你们了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ACE',
    )

    ChrTalk(
        0x0101,
        (
            '#1004F啊，菲小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F您留在船上吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF4')

    def _loc_1ACE(): pass

    label('loc_1ACE')

    ChrTalk(
        0x0101,
        (
            '#1004F啊，菲小姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你留在船上？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF4(): pass

    label('loc_1AF4')

    ChrTalk(
        0x00FE,
        (
            '嗯，我想既然博士留下来了，\n',
            '那么我也跟着留下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和整备人员们商量后，\n',
            '我就决定一起留下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在看起来，\n',
            '这个决定似乎是正确的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F不只正确，是明智的决定哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为现在必须要\n',
            '修理『埃尔赛尤』嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F太好了。\n',
            '专业人员是相当宝贵的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，谢谢你们欢迎我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不辜负你们的期望，\n',
            '我会竭尽所能地努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯！　拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)
    OP_A2(0x229B)

    Jump('loc_2016')

    def _loc_1C77(): pass

    label('loc_1C77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1CCF',
    )

    ChrTalk(
        0x00FE,
        (
            '看来留在飞船上\n',
            '似乎是正确的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就让我这机械专家\n',
            '竭尽所能地努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2016')

    def _loc_1CCF(): pass

    label('loc_1CCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1DDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D80',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，还能使用的碎片\n',
            '差不多都回收完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '舷梯的设置也完成了，\n',
            '我差不多也要回飞船上\n',
            '去帮忙修理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们应该是在忙着进行\n',
            '零部件的加工与调整吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_1DD8')

    def _loc_1D80(): pass

    label('loc_1D80')

    ChrTalk(
        0x00FE,
        (
            '碎片的回收和舷梯的设置\n',
            '总算告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我差不多也要回飞船上\n',
            '去帮忙修理了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD8(): pass

    label('loc_1DD8')

    Jump('loc_2016')

    def _loc_1DDB(): pass

    label('loc_1DDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_1F97',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E89',
    )

    ChrTalk(
        0x00FE,
        (
            '这个新来的女孩……\n',
            '干得相当不错哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工具使用起来很熟练，\n',
            '也具备相当的整备知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们还真是在关键时刻\n',
            '带来了个好女孩过来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_1ED8')

    def _loc_1E89(): pass

    label('loc_1E89')

    ChrTalk(
        0x00FE,
        (
            '这个新来的女孩干得不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们还真是在关键时刻\n',
            '带了个有用的人回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ED8(): pass

    label('loc_1ED8')

    Jump('loc_1F94')

    def _loc_1EDB(): pass

    label('loc_1EDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F60',
    )

    ChrTalk(
        0x00FE,
        (
            '就如你们所看到的，\n',
            '舷梯已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来预定要\n',
            '放在必要的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，还要架设一座\n',
            '在往下走的时候使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_1F94')

    def _loc_1F60(): pass

    label('loc_1F60')

    ChrTalk(
        0x00FE,
        (
            '舷梯已经完成了。\n',
            '接下来预定要\n',
            '放在必要的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F94(): pass

    label('loc_1F94')

    Jump('loc_2016')

    def _loc_1F97(): pass

    label('loc_1F97')

    ChrTalk(
        0x00FE,
        (
            '收拾好下面的碎片之后，\n',
            '预计要在这里架一座桥哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样出入甲板\n',
            '就方便得多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们出去探索的时候\n',
            '也会比较便利吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2016(): pass

    label('loc_2016')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x201A
@scena.Code('func_06_201A')
def func_06_201A():
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
        (0x00000000, 'loc_207B'),
        (0x00000001, 'loc_2562'),
        (0x00000002, 'loc_2569'),
        (-1, 'loc_256C'),
    )

    def _loc_207B(): pass

    label('loc_207B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 4, 0x22D4)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 1, 0x2221)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 5, 0x22D5)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_20FE',
    )

    ChrTalk(
        0x0017,
        (
            '#0090400807V#214F你、你们在闲晃些什么啊！\n',
            '赶快去结社那帮家伙的飞船啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400808V哥哥他们\n',
            '肯定在那里的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255F')

    def _loc_20FE(): pass

    label('loc_20FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 0, 0x2220)),
            Expr.Return,
        ),
        'loc_22A0',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x0017,
        (
            '#0090400809V#210F啊，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400810V#213F……怎么了？\n',
            '你好像想说什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400811V#1042F嗯，我是来报告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0090400812V#213F……报告？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400813V#1015F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了在工业区域发现了『古罗力亚斯』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0017,
        (
            '#0090400814V#214F真、真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400815V马、马上带我过去！\n',
            '哥哥他们应该在那里才对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22D5)

    Jump('loc_255F')

    def _loc_22A0(): pass

    label('loc_22A0')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 7, 0x22C7)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24C1',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x0017,
        (
            '#0090400816V#415F啊，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400817V#1040F已经开始帮忙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0090400818V#210F嗯、嗯，当然啰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400819V我一开始就说过\n',
            '会帮忙的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400820V我在『山猫号』上\n',
            '也经常修东修西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400821V我会证明自己比某人\n',
            '要有用得多的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400822V#1019F（气、气人……\n',
            '最令人懊恼的是完全无法反驳。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400823V#1049F谢谢你，实在帮了我们的大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400824V如果发现了吉尔他们的话，\n',
            '我们会马上来通知你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0090400825V#210F嗯，拜托了你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400826V那么，约修亚也\n',
            '要当心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22C7)

    Jump('loc_255F')

    def _loc_24C1(): pass

    label('loc_24C1')

    ChrTalk(
        0x0017,
        (
            '#0090400827V#210F在找到哥哥他们之前，\n',
            '我会一起帮忙修理的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400820V我在『山猫号』上\n',
            '也经常修东修西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400829V我会证明自己比某人\n',
            '要有用得多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_255F(): pass

    label('loc_255F')

    Jump('loc_256C')

    def _loc_2562(): pass

    label('loc_2562')

    Call(0, 0x0012)

    Jump('loc_256C')

    def _loc_2569(): pass

    label('loc_2569')

    Jump('loc_256C')

    def _loc_256C(): pass

    label('loc_256C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x2570
@scena.Code('func_07_2570')
def func_07_2570():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Neq,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 5, 0x229D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_25D1',
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

    def _loc_25D1(): pass

    label('loc_25D1')

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_25E6'),
        (0x00000001, 'loc_2BE8'),
        (0x00000002, 'loc_2C2D'),
        (-1, 'loc_2C30'),
    )

    def _loc_25E6(): pass

    label('loc_25E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_2A75',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 5, 0x229D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_285B',
    )

    ChrTurnDirection(0x0009, 0x010B, 0)

    ChrTalk(
        0x0009,
        (
            '#0040400830V#035F呼，自从上次王都的\n',
            '武术大会以来就没见过你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400831V而且今天是第一次\n',
            '和你面对面交谈吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400832V#210F嗯，我也\n',
            '还记得你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400833V因为就某方面来说，\n',
            '你不像是个帝国人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040400834V#033F哟，真残酷啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400835V#031F我在也用我的方式\n',
            '爱着我的祖国哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400836V#215F要是你有那份心的话，\n',
            '为什么不赶快回到国内工作？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400837V在王国到处闲晃，\n',
            '不像是帝国男儿的作风吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040400838V#035F呵呵，不必担心。\n',
            '我迟早会回去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400839V#030F好了，先不管这些……\n',
            '以后请多多关照啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400840V我们都是用枪的，\n',
            '一起努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)
    OP_A2(0x229D)

    Jump('loc_2A72')

    def _loc_285B(): pass

    label('loc_285B')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28DE',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x0009,
        (
            '#0040400841V#030F好了，不管怎么说，\n',
            '以后请多多关照啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400840V我们都是用枪的，\n',
            '一起努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A72')

    def _loc_28DE(): pass

    label('loc_28DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29FE',
    )

    ChrTalk(
        0x0009,
        (
            '#0040400843V#035F接下来好像要大家\n',
            '一起合力搬运巨大碎片呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400844V不知道为什么，\n',
            '连我也被拉来当苦力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400845V#037F……是、是不是该找我\n',
            '一起去探索了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400846V如果需要的话，\n',
            '跟我打声招呼就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400847V#034F……应该说，拜托你们\n',
            '把我带离这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_2A72')

    def _loc_29FE(): pass

    label('loc_29FE')

    ChrTalk(
        0x0009,
        (
            '#0040400848V#037F如果需要我的话，\n',
            '随时可以过来找我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400847V#034F……应该说，拜托你们\n',
            '把我带离这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A72(): pass

    label('loc_2A72')

    Jump('loc_2BE5')

    def _loc_2A75(): pass

    label('loc_2A75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_2BE5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B68',
    )

    ChrTalk(
        0x0009,
        (
            '#0040400850V#034F舰体的碎片还\n',
            '散落得真远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400851V要靠人力回收的话，\n',
            '可是个浩大工程哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400852V#035F当然，我身为演奏家，\n',
            '也会发挥我的所长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400853V呵呵，让我用美丽的音符\n',
            '来激励流汗劳动的诸位吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_2BE5')

    def _loc_2B68(): pass

    label('loc_2B68')

    ChrTalk(
        0x0009,
        (
            '#0040400854V#035F在大家流汗的时候，\n',
            '就让我用歌声来支持大家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400855V因此，体力劳动的事情\n',
            '交给穆拉来做就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BE5(): pass

    label('loc_2BE5')

    Jump('loc_2C30')

    def _loc_2BE8(): pass

    label('loc_2BE8')

    ChrTalk(
        0x0009,
        (
            '#0040310432V#035F呵呵，看来你们需要\n',
            '我这个天才的力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_2C30')

    def _loc_2C2D(): pass

    label('loc_2C2D')

    Jump('loc_2C30')

    def _loc_2C30(): pass

    label('loc_2C30')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x2C34
@scena.Code('func_08_2C34')
def func_08_2C34():
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
        (0x00000000, 'loc_2C95'),
        (0x00000001, 'loc_3583'),
        (0x00000002, 'loc_35B7'),
        (-1, 'loc_35BA'),
    )

    def _loc_2C95(): pass

    label('loc_2C95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            Expr.Return,
        ),
        'loc_3184',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 1, 0x22A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3110',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400857V#1011F咦，雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030400858V#020F呵呵，我就知道\n',
            '你们差不多该回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400859V#1044F莫非……\n',
            '你在等我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0030400860V#026F只是一种预感而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400861V你们……\n',
            '和姐姐她战斗过了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400862V#1043F嗯，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400863V#1035F不过，最后\n',
            '她还是走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400864V#1003F她说她和雪拉姐的\n',
            '缘分还没有断……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400865V以后还有机会相见，\n',
            '然后就消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030400866V#522F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400867V果然不会\n',
            '那么简单就落幕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400868V#1026F雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0030400869V#524F呵呵，不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400870V如姐姐所说，\n',
            '应该还会再相见的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400871V总之，现在我就先相信这一点，\n',
            '然后把这件事情放在心底。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400872V……对我们来说，接下来\n',
            '还有更加重要的事要完成吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FCA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400873V#035F呵呵，雪拉说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307F')

    def _loc_2FCA(): pass

    label('loc_2FCA')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3008',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400874V#051F嗯，雪拉扎德说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307F')

    def _loc_3008(): pass

    label('loc_3008')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3040',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400875V#070F嗯，你说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307F')

    def _loc_3040(): pass

    label('loc_3040')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_307F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400876V#1060F是啊……\n',
            '大姐你说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_307F(): pass

    label('loc_307F')

    ChrTalk(
        0x0101,
        (
            '#0010400877V#1002F嗯……\n',
            '现在必须前进才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030400878V#020F如果需要我帮忙\n',
            '就过来说，不用客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400879V那么，你们小心点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22A1)

    Jump('loc_3181')

    def _loc_3110(): pass

    label('loc_3110')

    ChrTalk(
        0x0008,
        (
            '#0030400880V#020F我会把露茜奥拉姐姐的事\n',
            '放在心底的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400881V不管怎么说，现在\n',
            '我们必须做好该做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3181(): pass

    label('loc_3181')

    Jump('loc_3580')

    def _loc_3184(): pass

    label('loc_3184')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Return,
        ),
        'loc_3580',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 1, 0x22A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34FF',
    )

    ChrTalk(
        0x0008,
        (
            '#0030400882V#522F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3203',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400883V#033F雪拉……你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    Jump('loc_32BC')

    def _loc_3203(): pass

    label('loc_3203')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3246',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400884V#052F雪拉扎德……你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    Jump('loc_32BC')

    def _loc_3246(): pass

    label('loc_3246')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3289',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400885V#072F雪拉扎德……你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    Jump('loc_32BC')

    def _loc_3289(): pass

    label('loc_3289')

    ChrTalk(
        0x0102,
        (
            '#0020400886V#1044F雪拉姐……你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    def _loc_32BC(): pass

    label('loc_32BC')

    ChrTalk(
        0x0008,
        (
            '#0030400887V#524F嗯……我只是\n',
            '在想一些事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400888V没事的……\n',
            '我已经整理好心情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_335C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400889V#033F那就好……\n',
            '不过也别太勉强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_345B')

    def _loc_335C(): pass

    label('loc_335C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_339F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400890V#552F那就好……\n',
            '不过也别太勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_345B')

    def _loc_339F(): pass

    label('loc_339F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33E0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400891V#072F是吗……\n',
            '不过也别太勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_345B')

    def _loc_33E0(): pass

    label('loc_33E0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3424',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400892V#1063F那就好……\n',
            '不过可别太勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_345B')

    def _loc_3424(): pass

    label('loc_3424')

    ChrTalk(
        0x0102,
        (
            '#0020400893V#1043F那就好……\n',
            '不过请别太勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_345B(): pass

    label('loc_345B')

    ChrTalk(
        0x0008,
        (
            '#0030400894V#025F是是，我知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400895V唉，为什么男人只有在\n',
            '这时候才会表现出温柔来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400896V我倒是希望你们平时\n',
            '能够更多多怜恤女人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0010)
    OP_A2(0x22A1)

    Jump('loc_3580')

    def _loc_34FF(): pass

    label('loc_34FF')

    ChrTalk(
        0x0008,
        (
            '#0030400897V#020F我已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400898V心情也整理好了，\n',
            '随时可以去探索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400899V那么，需要我的时候\n',
            '就来叫我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3580(): pass

    label('loc_3580')

    Jump('loc_35BA')

    def _loc_3583(): pass

    label('loc_3583')

    ChrTalk(
        0x0008,
        (
            '#0030340489V#020F哎呀，要更换成员了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_35BA')

    def _loc_35B7(): pass

    label('loc_35B7')

    Jump('loc_35BA')

    def _loc_35BA(): pass

    label('loc_35BA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x35BE
@scena.Code('func_09_35BE')
def func_09_35BE():
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
        (0x00000000, 'loc_361F'),
        (0x00000001, 'loc_4230'),
        (0x00000002, 'loc_425C'),
        (-1, 'loc_425F'),
    )

    def _loc_361F(): pass

    label('loc_361F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3C5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            Expr.Return,
        ),
        'loc_3ABC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 0, 0x22A8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A06',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400901V#1011F啊，金先生……\n',
            '你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0080400902V#070F哦，是艾丝蒂尔啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400903V……你好像有什么话要说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400904V#1002F嗯……\n',
            '其实是瓦鲁特的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080400905V#074F……他还是出现了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400906V#070F不过，你们能够\n',
            '安然地回来就代表……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400907V#1040F是的，好不容易才击退了他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400908V#1015F嗯，虽然很危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400909V总之，看来这次他是\n',
            '退出战局了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080400910V#074F原来如此，他走了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400911V把和我之间的对决\n',
            '留到下次了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400912V#1043F嗯，瓦鲁特他自己\n',
            '也是这么说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400913V看来是\n',
            '暂时停战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080400914V#074F嗯，应该是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400915V虽然心情上有点遗憾……\n',
            '不过这或许也是件好事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400916V#572F和瓦鲁特的因缘\n',
            '是我自己应该解决的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400917V把你们也卷进来的话\n',
            '是缺乏道义的行为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400918V#1026F金先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080400919V#070F总之，现在我们应该为\n',
            '能够突破他的防守而高兴吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400920V我们确实面对着\n',
            '应该完成的使命前进了一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AB6')

    def _loc_3A06(): pass

    label('loc_3A06')

    ChrTalk(
        0x000D,
        (
            '#0080400921V#070F虽然决战被留到了将来，\n',
            '不过现在这样说不定也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400922V和瓦鲁特的因缘\n',
            '是我自己应该解决的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400917V把你们也卷进来的话\n',
            '是缺乏道义的行为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AB6(): pass

    label('loc_3AB6')

    OP_A2(0x22A8)

    Jump('loc_3C5A')

    def _loc_3ABC(): pass

    label('loc_3ABC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Return,
        ),
        'loc_3C5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BCD',
    )

    ChrTalk(
        0x000D,
        (
            '#0080400924V#074F瓦鲁特曾是位\n',
            '天资远胜于我的拳术师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400925V可是，却被背负『泰斗』\n',
            '之名的我轻易击败……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400926V#072F看来重要的不是力量的强与弱，\n',
            '而是为了什么去使用的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400927V身为一个为武而生的人，\n',
            '我也必须重新审视自己才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    Jump('loc_3C5A')

    def _loc_3BCD(): pass

    label('loc_3BCD')

    ChrTalk(
        0x000D,
        (
            '#0080400928V#074F看来重要的不是力量的强与弱，\n',
            '而是为了什么去使用的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400929V身为一个为武而生的人，\n',
            '我也必须重新审视自己才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C5A(): pass

    label('loc_3C5A')

    Jump('loc_422D')

    def _loc_3C5D(): pass

    label('loc_3C5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_3DE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D41',
    )

    ChrTalk(
        0x000D,
        (
            '#0080400930V#070F嗯，看来碎片的\n',
            '回收也快完成了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400931V收拾完这个，剩下的\n',
            '就交给亲卫队吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400932V毕竟都市的探索\n',
            '也渐入佳境了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400933V接下来应该是将力量放在\n',
            '身为游击士的本分上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    Jump('loc_3DE1')

    def _loc_3D41(): pass

    label('loc_3D41')

    ChrTalk(
        0x000D,
        (
            '#0080400934V#070F收拾完这个，剩下的\n',
            '就交给亲卫队吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400935V毕竟都市的探索\n',
            '也渐入佳境了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400933V接下来应该是将力量放在\n',
            '身为游击士的本分上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DE1(): pass

    label('loc_3DE1')

    Jump('loc_422D')

    def _loc_3DE4(): pass

    label('loc_3DE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_40F4',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 7, 0x22A7)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F35',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '#0080400937V#073F哦，你……\n',
            '应该是乔丝特吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400938V#210F嗯，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080400939V#071F哈哈，想不到\n',
            '会在这种地方再见到你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400940V#070F不过情况既然变成这样，\n',
            '我们就是站在同一船上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400941V在这段时间里，\n',
            '就让我们互相协助吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400942V#210F嗯，我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0017)
    OP_A2(0x22A7)

    Jump('loc_40F1')

    def _loc_3F35(): pass

    label('loc_3F35')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FC4',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '#0080400943V#070F话说回来，真没想到\n',
            '我们会在这种地方再见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400944V真是的，空之女神\n',
            '还真喜欢恶作剧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40F1')

    def _loc_3FC4(): pass

    label('loc_3FC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_407E',
    )

    ChrTalk(
        0x000D,
        (
            '#0080400945V#070F为了方便往来艇尾，\n',
            '这里听说也要修一条通道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400946V嗯，的确有通道的话，\n',
            '施工也会变得比较容易。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400947V好，提起精神，\n',
            '开始着手进行作业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    Jump('loc_40F1')

    def _loc_407E(): pass

    label('loc_407E')

    ChrTalk(
        0x000D,
        (
            '#0080400945V#070F为了方便往来艇尾，\n',
            '这里听说也要修一条通道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400947V好，提起精神，\n',
            '开始着手进行作业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40F1(): pass

    label('loc_40F1')

    Jump('loc_422D')

    def _loc_40F4(): pass

    label('loc_40F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_422D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41C6',
    )

    ChrTalk(
        0x000D,
        (
            '#0080400950V#070F听说要从这里\n',
            '架一座桥到甲板……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400951V所以在此之前必须先把\n',
            '这块碎片搬走才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400952V你们几个\n',
            '有空也来帮个忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400953V再怎么说\n',
            '我一个人也搞不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    Jump('loc_422D')

    def _loc_41C6(): pass

    label('loc_41C6')

    ChrTalk(
        0x000D,
        (
            '#0080400954V#070F听说要先搬走碎片，\n',
            '然后在这里架一座桥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400955V你们几个\n',
            '有空也来帮个忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_422D(): pass

    label('loc_422D')

    Jump('loc_425F')

    def _loc_4230(): pass

    label('loc_4230')

    ChrTalk(
        0x000D,
        (
            '#0080340548V#070F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_425F')

    def _loc_425C(): pass

    label('loc_425C')

    Jump('loc_425F')

    def _loc_425F(): pass

    label('loc_425F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x4263
@scena.Code('func_0A_4263')
def func_0A_4263():
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
        (0x00000000, 'loc_42C4'),
        (0x00000001, 'loc_4870'),
        (0x00000002, 'loc_489C'),
        (-1, 'loc_489F'),
    )

    def _loc_42C4(): pass

    label('loc_42C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_43E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_437E',
    )

    ChrTalk(
        0x000B,
        (
            '#0050400986V#050F碎片的回收进行得很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400987V接下来只要解决了那个大零件，\n',
            '基本的工作就完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400988V好，重新提起精神，\n',
            '开始着手进行作业吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    Jump('loc_43E6')

    def _loc_437E(): pass

    label('loc_437E')

    ChrTalk(
        0x000B,
        (
            '#0050400986V#050F碎片的回收进行得很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400990V只要解决了那个大零件，\n',
            '基本的工作就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43E6(): pass

    label('loc_43E6')

    Jump('loc_486D')

    def _loc_43E9(): pass

    label('loc_43E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_4642',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 1, 0x22A9)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_449C',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000B,
        (
            '#0050400991V#051F哦，这么快要我帮忙探索了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400992V设想得挺周到的嘛。\n',
            '那就一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400993V#210F嘿嘿，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0019)
    OP_A2(0x22A9)

    Jump('loc_463F')

    def _loc_449C(): pass

    label('loc_449C')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4514',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000B,
        (
            '#0050400994V#051F这么快要我帮忙探索，\n',
            '设想得挺周到的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400995V那就一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_463F')

    def _loc_4514(): pass

    label('loc_4514')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45D0',
    )

    ChrTalk(
        0x000B,
        (
            '#0050400996V#552F这个机翼倒是还好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400997V不过横躺在上面的零件，\n',
            '用普通的办法无法回收啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400998V#053F虽然似乎是重要的部分，\n',
            '不过还是跟老爷子商量看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    Jump('loc_463F')

    def _loc_45D0(): pass

    label('loc_45D0')

    ChrTalk(
        0x000B,
        (
            '#0050400999V#053F横躺在上面的零件，\n',
            '用普通的办法无法回收呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401000V待会儿去和\n',
            '老爷子商量看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_463F(): pass

    label('loc_463F')

    Jump('loc_486D')

    def _loc_4642(): pass

    label('loc_4642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_486D',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_479A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4745',
    )

    ChrTalk(
        0x000B,
        (
            '#0050401001V#552F真是的……\n',
            '大得离谱的碎片啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401002V竟然叫我们搬这个东西，\n',
            '胡乱使唤人也要有个限度啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401003V#053F不过，在这种时候\n',
            '发牢骚也没有意义……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401004V先把在甲板上偷懒的\n',
            '那个家伙抓来好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    Jump('loc_4797')

    def _loc_4745(): pass

    label('loc_4745')

    ChrTalk(
        0x000B,
        (
            '#0050401005V#552F算了，现在\n',
            '发牢骚也没用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401006V只有提起精神做事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4797(): pass

    label('loc_4797')

    Jump('loc_486D')

    def _loc_479A(): pass

    label('loc_479A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_481B',
    )

    ChrTalk(
        0x000B,
        (
            '#0050401001V#552F真是的……\n',
            '大得离谱的碎片啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401008V竟然叫我们搬这个东西，\n',
            '胡乱使唤人也要有个限度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    Jump('loc_486D')

    def _loc_481B(): pass

    label('loc_481B')

    ChrTalk(
        0x000B,
        (
            '#0050401009V#053F算了，现在\n',
            '发牢骚也没用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401006V只有提起精神做事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_486D(): pass

    label('loc_486D')

    Jump('loc_489F')

    def _loc_4870(): pass

    label('loc_4870')

    ChrTalk(
        0x000B,
        (
            '#0050340442V#050F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_489F')

    def _loc_489C(): pass

    label('loc_489C')

    Jump('loc_489F')

    def _loc_489F(): pass

    label('loc_489F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x48A3
@scena.Code('func_0B_48A3')
def func_0B_48A3():
    TalkBegin(0x00FE)

    Return()

# id: 0x000C offset: 0x48A7
@scena.Code('func_0C_48A7')
def func_0C_48A7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_49FA',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4905',
    )

    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目前正在准备\n',
            '进行下一项工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Jump('loc_49F7')

    def _loc_4905(): pass

    label('loc_4905')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49A8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，在游击士的协助下，\n',
            '回收碎片总算还是顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀～不过话说回来，\n',
            '男游击士的力量真惊人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和我们这些卖弄力气的\n',
            '士兵感觉有着天壤之别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    Jump('loc_49F7')

    def _loc_49A8(): pass

    label('loc_49A8')

    ChrTalk(
        0x00FE,
        (
            '男游击士的力量真惊人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和我们这些卖弄力气的\n',
            '士兵感觉有着天壤之别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49F7(): pass

    label('loc_49F7')

    Jump('loc_4BA7')

    def _loc_49FA(): pass

    label('loc_49FA')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B03',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A96',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，殿下……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '这、这点程度的碎片，\n',
            '完全没有任何的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们很快就会清理掉的，\n',
            '请您放心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)
    OP_A2(0x0011)

    Jump('loc_4B00')

    def _loc_4A96(): pass

    label('loc_4A96')

    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '赌上王国军亲卫队的名誉，\n',
            '我们会迅速清理掉碎片的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请殿下安心地\n',
            '前往探索吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    def _loc_4B00(): pass

    label('loc_4B00')

    Jump('loc_4BA7')

    def _loc_4B03(): pass

    label('loc_4B03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B5D',
    )

    ChrTalk(
        0x00FE,
        (
            '这、这个\n',
            '要用人力搬走吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '觉、觉得很难的人，\n',
            '大概只有我一个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    Jump('loc_4BA7')

    def _loc_4B5D(): pass

    label('loc_4B5D')

    ChrTalk(
        0x00FE,
        (
            '我、我们现在要\n',
            '把这个搬走吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我好像已经\n',
            '有点头晕目眩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BA7(): pass

    label('loc_4BA7')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x4BAB
@scena.Code('func_0D_4BAB')
def func_0D_4BAB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C42',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '我们正在工程师的指导下\n',
            '设置通道当中！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请再稍微等一些时间\n',
            '就能完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)
    OP_A2(0x0010)

    Jump('loc_4CA6')

    def _loc_4C42(): pass

    label('loc_4C42')

    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '我们正在工程师的指导下\n',
            '设置通道当中！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请再稍微等一些时间\n',
            '就能完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    def _loc_4CA6(): pass

    label('loc_4CA6')

    Jump('loc_4D65')

    def _loc_4CA9(): pass

    label('loc_4CA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D0D',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～接下来好像\n',
            '就要在这里建造通道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '清理完碎片之后\n',
            '得去叫菲小姐过来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    Jump('loc_4D65')

    def _loc_4D0D(): pass

    label('loc_4D0D')

    ChrTalk(
        0x00FE,
        (
            '有菲小姐在这里\n',
            '真是再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从焊接到导力引擎的调整，\n',
            '她实在是无所不能啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D65(): pass

    label('loc_4D65')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x4D69
@scena.Code('func_0E_4D69')
def func_0E_4D69():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_4EB9',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DCB',
    )

    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '视察辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '修复工作很顺利！\n',
            '请不用担心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Jump('loc_4EB6')

    def _loc_4DCB(): pass

    label('loc_4DCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E58',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～就算是这样的碎片，\n',
            '要一个人搬运也是绝对办不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再怎么说，\n',
            '这都是金属块啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，再去拜托\n',
            '游击士来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    Jump('loc_4EB6')

    def _loc_4E58(): pass

    label('loc_4E58')

    ChrTalk(
        0x00FE,
        (
            '就算是这样的碎片，\n',
            '要一个人搬运也是绝对办不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，再去拜托\n',
            '游击士来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EB6(): pass

    label('loc_4EB6')

    Jump('loc_4FA0')

    def _loc_4EB9(): pass

    label('loc_4EB9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F25',
    )

    SetChrChipByIndex(0x00FE, 21)
    SetChrSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '这样的碎片\n',
            '根本就不算什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '马上就会清理掉的，\n',
            '请不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)
    SetChrChipByIndex(0x00FE, 19)
    SetChrSubChip(0x00FE, 0)

    Jump('loc_4FA0')

    def _loc_4F25(): pass

    label('loc_4F25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F7B',
    )

    ChrTalk(
        0x00FE,
        (
            '接、接下来要\n',
            '搬动这块碎片吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤、尤莉亚上尉也\n',
            '真会乱来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    Jump('loc_4FA0')

    def _loc_4F7B(): pass

    label('loc_4F7B')

    ChrTalk(
        0x00FE,
        (
            '接、接下来要\n',
            '搬动这块碎片吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FA0(): pass

    label('loc_4FA0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x4FA4
@scena.Code('func_0F_4FA4')
def func_0F_4FA4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_5043',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FFF',
    )

    ChrTalk(
        0x00FE,
        (
            '支架的回收\n',
            '看来要放到最后了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果赶得上\n',
            '修复就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5040')

    def _loc_4FFF(): pass

    label('loc_4FFF')

    ChrTalk(
        0x00FE,
        (
            '支架的回收\n',
            '看来要放到最后了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果赶得上修复就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5040(): pass

    label('loc_5040')

    Jump('loc_516B')

    def _loc_5043(): pass

    label('loc_5043')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5115',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50C9',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，公主殿下……\n',
            '您要出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '您回来的时候，\n',
            '这里应该已经造好一座桥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之请您期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0014)

    Jump('loc_5112')

    def _loc_50C9(): pass

    label('loc_50C9')

    ChrTalk(
        0x00FE,
        (
            '殿下您回来的时候，\n',
            '这里应该已经造好一座桥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之请您期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5112(): pass

    label('loc_5112')

    Jump('loc_516B')

    def _loc_5115(): pass

    label('loc_5115')

    ChrTalk(
        0x00FE,
        (
            '唔唔～……\n',
            '近看的话还真是巨大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不拿出相当的气势的话，\n',
            '看来是动不了它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_516B(): pass

    label('loc_516B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x516F
@scena.Code('func_10_516F')
def func_10_516F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_517C',
    )

    Jump('loc_5865')

    def _loc_517C(): pass

    label('loc_517C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_52CF',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5230',
    )

    ChrTalk(
        0x0012,
        (
            '#0110400957V#270F大到这种程度的话，\n',
            '光靠人力是动不了的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400958V可是，辅助飞翔引擎\n',
            '只有单翼是靠不住的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400959V必须想出一个\n',
            '回收的办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52CC')

    def _loc_5230(): pass

    label('loc_5230')

    ChrTalk(
        0x0012,
        (
            '#0110400960V#270F大到这种程度的话，\n',
            '光靠人力是动不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400958V可是，辅助飞翔引擎\n',
            '只有单翼是靠不住的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400962V必须想出一个\n',
            '回收的办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52CC(): pass

    label('loc_52CC')

    Jump('loc_5865')

    def _loc_52CF(): pass

    label('loc_52CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_585E',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 4, 0x22AC)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5492',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x0012,
        (
            '#0110400963V#270F嗯……\n',
            '你就是空贼团的小丫头吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400964V#212F你、你真没礼貌。\n',
            '什么小丫头啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0110400965V#270F把小丫头叫做小丫头，\n',
            '完全没有什么不妥的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400966V我先声明……\n',
            '为了你好，你可别太得意忘形。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400967V你能够待在这里，\n',
            '是因为现在是非常时期。\n',
            '你可要谨记在心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400968V#214F我、我当然知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0110400969V#272F那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400970V你就尽量努力地干活吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001C)
    OP_A2(0x22AC)

    Jump('loc_585B')

    def _loc_5492(): pass

    label('loc_5492')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 4, 0x1C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5521',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x0012,
        (
            '#0110400971V#270F你就尽量努力地干活吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400967V你能够待在这里，\n',
            '是因为现在是非常时期。\n',
            '你可要谨记在心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_585B')

    def _loc_5521(): pass

    label('loc_5521')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5615',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 5, 0x1D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_55B2',
    )

    ChrTalk(
        0x0012,
        (
            '#0110400973V#270F奥利维尔说的话，\n',
            '你们当作没听到就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400974V现在正是让他了解到\n',
            '劳动的价值的绝佳机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001D)

    Jump('loc_5612')

    def _loc_55B2(): pass

    label('loc_55B2')

    ChrTalk(
        0x0012,
        (
            '#0110400975V#270F那家伙说的话，\n',
            '你们当作没听到就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400976V别在意，尽管去探索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5612(): pass

    label('loc_5612')

    Jump('loc_585B')

    def _loc_5615(): pass

    label('loc_5615')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57CD',
    )

    ChrTurnDirection(0x00FE, 0x0104, 0)

    ChrTalk(
        0x0012,
        (
            '#0110400977V#276F接下来就要开始\n',
            '回收碎片了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400978V#270F这里如果没你这家伙的话\n',
            '会让人无比遗憾的，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040400979V#035F呵呵，体力劳动虽然也不错，\n',
            '但不巧的是我正好有重要的使命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400980V下次有机会再让我\n',
            '学习劳动的珍贵吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0110400981V#274F一旦知道和自己没关系\n',
            '就耍起嘴皮子来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400982V艾丝蒂尔，如果你改变心意，\n',
            '随时都可以把他换下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400983V这次我会负责\n',
            '好好照顾他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    Jump('loc_585B')

    def _loc_57CD(): pass

    label('loc_57CD')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0012,
        (
            '#0110400984V#270F艾丝蒂尔，如果你改变心意，\n',
            '随时都可以把奥利维尔换下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110400985V我必须让那家伙亲身\n',
            '体验一下劳动的价值才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_585B(): pass

    label('loc_585B')

    Jump('loc_5865')

    def _loc_585E(): pass

    label('loc_585E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_5865',
    )

    def _loc_5865(): pass

    label('loc_5865')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x5869
@scena.Code('func_11_5869')
def func_11_5869():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_5977',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_590E',
    )

    ChrTalk(
        0x00FE,
        (
            '舰内马上就要开始进行\n',
            '飞翔引擎的最终检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调整应该是完美无缺才对，\n',
            '不过心中还是有些许的不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我才跑到\n',
            '外面来看看情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    Jump('loc_5974')

    def _loc_590E(): pass

    label('loc_590E')

    ChrTalk(
        0x00FE,
        (
            '舰内马上就要开始进行\n',
            '飞翔引擎的最终检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接着只要能回收左舷部的话，\n',
            '飞行准备就完成了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5974(): pass

    label('loc_5974')

    Jump('loc_5D76')

    def _loc_5977(): pass

    label('loc_5977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_5A98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A2E',
    )

    ChrTalk(
        0x00FE,
        (
            '不过飞翔引擎的调节是马虎不得的，\n',
            '所以得跟舵手好好讨论一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为最后操纵飞船的是他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从直接责任这个意义上来说，\n',
            '他们的工作比舰长更有压力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    Jump('loc_5A95')

    def _loc_5A2E(): pass

    label('loc_5A2E')

    ChrTalk(
        0x00FE,
        (
            '不过飞翔引擎的调节是马虎不得的，\n',
            '所以得跟舵手好好讨论一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为实际操纵飞船的是他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A95(): pass

    label('loc_5A95')

    Jump('loc_5D76')

    def _loc_5A98(): pass

    label('loc_5A98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_5BF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B7F',
    )

    ChrTalk(
        0x00FE,
        (
            '这突出在舷外的部分\n',
            '称为支架……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是搭载着辅助\n',
            '飞翔引擎的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来的话是左右各有一组，\n',
            '用以保持舰体平衡\n',
            '的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不巧的是左舷\n',
            '被切断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了预防最坏的情况，\n',
            '必须尽可能事先做些准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    Jump('loc_5BEE')

    def _loc_5B7F(): pass

    label('loc_5B7F')

    ChrTalk(
        0x00FE,
        (
            '总之我决定开始\n',
            '调整右舷的辅助引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '的确是项很难的工作，\n',
            '不过接下来也正好可以\n',
            '展示出我维修员的实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BEE(): pass

    label('loc_5BEE')

    Jump('loc_5D76')

    def _loc_5BF1(): pass

    label('loc_5BF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CE0',
    )

    ChrTalk(
        0x00FE,
        (
            '看来这个安定翼\n',
            '好像没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还真能承受住冲击呢。\n',
            '也因此省下了修理的功夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来要去\n',
            '检查支架才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……所谓的支架，\n',
            '就是突出在舷外的舰体部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它收纳了各种辅助飞翔引擎，\n',
            '是个很重要的部位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    Jump('loc_5D76')

    def _loc_5CE0(): pass

    label('loc_5CE0')

    ChrTalk(
        0x00FE,
        (
            '所谓的支架，\n',
            '就是突出在舷外的舰体部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它收纳了各种辅助飞翔引擎，\n',
            '是个很重要的部位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次左舷的支架\n',
            '整个都脱落了呢。\n',
            '难怪会坠落下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D76(): pass

    label('loc_5D76')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x5D7A
@scena.Code('func_12_5D7A')
def func_12_5D7A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DA9',
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

    Jump('loc_5DEB')

    def _loc_5DA9(): pass

    label('loc_5DA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_5DD0',
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

    Jump('loc_5DEB')

    def _loc_5DD0(): pass

    label('loc_5DD0')

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

    def _loc_5DEB(): pass

    label('loc_5DEB')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E86',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5E3D',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -17120, 3500, 23510, 135)

    def _loc_5E3D(): pass

    label('loc_5E3D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5E60',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -20610, 0, 16960, 315)

    def _loc_5E60(): pass

    label('loc_5E60')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5E83',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -23120, 0, 16149, 0)

    def _loc_5E83(): pass

    label('loc_5E83')

    Jump('loc_5FD1')

    def _loc_5E86(): pass

    label('loc_5E86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F0C',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5EB1',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 4310, -4000, 22130, 315)

    def _loc_5EB1(): pass

    label('loc_5EB1')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5EC3',
    )

    ClearChrFlags(0x0017, 0x0080)

    def _loc_5EC3(): pass

    label('loc_5EC3')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5EE6',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 5070, -3880, 23930, 270)

    def _loc_5EE6(): pass

    label('loc_5EE6')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5F09',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 11730, -4000, 18510, 90)

    def _loc_5F09(): pass

    label('loc_5F09')

    Jump('loc_5FD1')

    def _loc_5F0C(): pass

    label('loc_5F0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F5D',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5F37',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 34850, -4000, 16079, 225)

    def _loc_5F37(): pass

    label('loc_5F37')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5F5A',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 11730, -4000, 18510, 90)

    def _loc_5F5A(): pass

    label('loc_5F5A')

    Jump('loc_5FD1')

    def _loc_5F5D(): pass

    label('loc_5F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5FA3',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5FA3',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -18510, 3500, 22430, 180)
    CreateThread(0x0008, 0x00, 0x06, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 1, 0x22A1)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5FA3',
    )

    SetChrFlags(0x0008, 0x0010)

    def _loc_5FA3(): pass

    label('loc_5FA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5FD1',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5FD1',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -43550, 5000, 31240, 225)

    def _loc_5FD1(): pass

    label('loc_5FD1')

    OP_0D()

    Return()

# id: 0x0013 offset: 0x5FD3
@scena.Code('func_13_5FD3')
def func_13_5FD3():
    EventBegin(0x00)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000B, 255)
    OP_D2(0x00260222, 0x00260227, 0x15)
    OP_D2(0x0006007C, 0x00060081, 0x16)
    OP_D2(0x00260068, 0x0026006D, 0x17)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    OP_6D(58350, -4000, 15070, 0)
    OP_67(0, 9860, -10000, 0)
    OP_6B(4650, 0)
    OP_6C(310000, 0)
    OP_6E(684, 0)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0101, -20700, 3500, 24660, 180)
    SetChrPos(0x000C, -22360, 3500, 24090, 225)
    SetChrPos(0x000B, -22990, 3500, 24700, 180)
    SetChrPos(0x000D, -22150, 3500, 28290, 90)
    SetChrPos(0x0102, -21110, 3500, 26540, 135)
    SetChrPos(0x000A, -19850, 3500, 23160, 180)
    SetChrPos(0x0008, -18490, 3500, 26100, 135)
    SetChrPos(0x0009, -17510, 3500, 28380, 45)
    SetChrPos(0x000E, -19700, 3500, 25650, 90)
    SetChrPos(0x000F, -22180, 3500, 25600, 0)
    SetChrPos(0x0013, -18800, 3500, 23370, 0)
    SetChrPos(0x0012, -18590, 3500, 27820, 0)
    SetChrPos(0x0010, -20780, 3500, 28750, 0)
    SetChrPos(0x0011, -19600, 3500, 28870, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    FadeIn(2000, 0)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 30)

    @scena.Lambda('lambda_61C5')
    def lambda_61C5():
        OP_6D(-55380, -4000, 35510, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_61C5)

    @scena.Lambda('lambda_61DD')
    def lambda_61DD():
        OP_67(0, 8530, -10000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_61DD)

    @scena.Lambda('lambda_61F5')
    def lambda_61F5():
        OP_6E(662, 11000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_61F5)

    OP_A2(0x0000)
    CreateThread(0x0101, 0x01, 0x00, 0x0014)
    CreateThread(0x0011, 0x01, 0x00, 0x001A)
    Sleep(100)

    CreateThread(0x0102, 0x01, 0x00, 0x001A)
    CreateThread(0x000D, 0x01, 0x00, 0x0018)
    CreateThread(0x000A, 0x01, 0x00, 0x0014)
    Sleep(100)

    CreateThread(0x000F, 0x01, 0x00, 0x001A)
    CreateThread(0x0010, 0x01, 0x00, 0x001B)
    CreateThread(0x0008, 0x01, 0x00, 0x0017)
    CreateThread(0x0012, 0x01, 0x00, 0x0018)
    Sleep(100)

    CreateThread(0x000B, 0x01, 0x00, 0x0015)
    CreateThread(0x0013, 0x01, 0x00, 0x0016)
    CreateThread(0x000E, 0x01, 0x00, 0x0017)
    Sleep(100)

    CreateThread(0x000C, 0x01, 0x00, 0x0014)
    CreateThread(0x0009, 0x01, 0x00, 0x0019)
    OP_C8(0x0080, 0x0172, 'C_PLAC25._CH', 0x01, 0x09C4)
    Sleep(8000)

    OP_A3(0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)
    Fade(500)
    OP_6D(-20600, 3500, 26640, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(339000, 0)
    OP_6E(392, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010390165V#1020F#5P这、这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070390166V#560F#5P哇……好漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0280390167V#151F#5P这、这回一定要\n',
            '拍啊拍啊拍个够～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    SetChrSubChip(0x0011, 0)
    SetChrChipByIndex(0x0011, 22)
    OP_0D()
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_8C(0x0011, 225, 400)
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_8C(0x0011, 90, 400)
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_8C(0x0011, 0, 400)
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_8C(0x0010, 135, 400)
    Sleep(300)

    ChrTalk(
        0x0010,
        (
            '#0270390168V#142F#5P喂喂……\n',
            '别用完感光结晶回路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180390169V#1063F#5P不过这里……\n',
            '还真是个不得了的世外桃源呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390170V与其说是城市\n',
            '不如称为庭园比较恰当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390171V#1043F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390172V#1042F可能是大城市里\n',
            '类似公园之类的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390173V#1007F#6P确、确实有这种感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390174V#1019F而且，同样的景致\n',
            '还一直延续到远处……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390175V#035F#6P哟哟……\n',
            '真是令人无法想象的规模呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)
    OP_22(0x0197, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010390176V#1004F#5P基库！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_66C9')
    def lambda_66C9():
        OP_6D(-23900, 3500, 19660, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_66C9)

    SetChrPos(0x0014, -28880, 6500, 7610, 45)
    ClearChrFlags(0x0014, 0x0080)

    @scena.Lambda('lambda_66F7')
    def lambda_66F7():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_66F7')

    DispatchAsync2(0x000A, 0x0001, lambda_66F7)

    Sleep(50)

    @scena.Lambda('lambda_670D')
    def lambda_670D():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_670D')

    DispatchAsync2(0x0102, 0x0001, lambda_670D)

    @scena.Lambda('lambda_671E')
    def lambda_671E():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_671E')

    DispatchAsync2(0x0008, 0x0001, lambda_671E)

    Sleep(50)

    @scena.Lambda('lambda_6734')
    def lambda_6734():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_6734')

    DispatchAsync2(0x0101, 0x0001, lambda_6734)

    @scena.Lambda('lambda_6745')
    def lambda_6745():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_6745')

    DispatchAsync2(0x0009, 0x0001, lambda_6745)

    Sleep(50)

    @scena.Lambda('lambda_675B')
    def lambda_675B():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_675B')

    DispatchAsync2(0x000C, 0x0001, lambda_675B)

    @scena.Lambda('lambda_676C')
    def lambda_676C():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_676C')

    DispatchAsync2(0x000E, 0x0001, lambda_676C)

    @scena.Lambda('lambda_677D')
    def lambda_677D():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_677D')

    DispatchAsync2(0x0012, 0x0001, lambda_677D)

    Sleep(50)

    @scena.Lambda('lambda_6793')
    def lambda_6793():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_6793')

    DispatchAsync2(0x000B, 0x0001, lambda_6793)

    @scena.Lambda('lambda_67A4')
    def lambda_67A4():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_67A4')

    DispatchAsync2(0x000F, 0x0001, lambda_67A4)

    @scena.Lambda('lambda_67B5')
    def lambda_67B5():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_67B5')

    DispatchAsync2(0x0010, 0x0001, lambda_67B5)

    Sleep(50)

    @scena.Lambda('lambda_67CB')
    def lambda_67CB():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_67CB')

    DispatchAsync2(0x000D, 0x0001, lambda_67CB)

    @scena.Lambda('lambda_67DC')
    def lambda_67DC():
        OP_8C(0x00FE, 225, 400)
        Yield()

        Jump('lambda_67DC')

    DispatchAsync2(0x0013, 0x0001, lambda_67DC)

    SetChrSubChip(0x0011, 0)
    SetChrChipByIndex(0x0011, 9)

    @scena.Lambda('lambda_67F7')
    def lambda_67F7():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_67F7')

    DispatchAsync2(0x0011, 0x0001, lambda_67F7)

    WaitForThreadExit(0x0101, 0x0002)
    OP_22(0x008C, 0x00, 0x64)

    @scena.Lambda('lambda_6812')
    def lambda_6812():
        OP_8E(0x00FE, -20360, 5500, 21090, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_6812)

    Sleep(500)

    @scena.Lambda('lambda_6832')
    def lambda_6832():
        OP_6D(-20680, 3500, 25150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6832)

    WaitForThreadExit(0x0014, 0x0001)
    CreateThread(0x0014, 0x01, 0x00, 0x001C)
    WaitForThreadExit(0x0101, 0x0002)
    OP_8E(0x0014, -20140, 4500, 22850, 3000, 0x00)
    OP_8C(0x0014, 180, 400)
    OP_8F(0x0014, -20140, 3700, 22850, 1000, 0x00)
    OP_A3(0x0001)
    Fade(500)
    TerminateThread(0x000A, 0x01)
    SetChrPos(0x0014, -19850, 3800, 23160, 0)
    SetChrFlags(0x0014, 0x0080)
    SetChrSubChip(0x000A, 5)
    SetChrChipByIndex(0x000A, 21)

    @scena.Lambda('lambda_68B6')
    def lambda_68B6():
        OP_8C(0x00FE, 315, 400)
        Yield()

        Jump('lambda_68B6')

    DispatchAsync2(0x0013, 0x0001, lambda_68B6)

    OP_0D()

    ChrTalk(
        0x0014,
        (
            '#0440390177V#311F#5P啾啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390178V#1165F#2P太好了……\n',
            '我还以为和你失散了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390179V#1168F不要紧……我们也没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0440390180V#311F#5P啾⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0440390181V#310F啾！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0440390182V啾啾啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390183V#1167F#2P是吗……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000A, 0x0020)
    SetChrSubChip(0x000A, 3)
    OP_8C(0x000A, 0, 400)
    ClearChrFlags(0x000A, 0x0020)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0060390184V#1162F#6P看来我们迫降到了\n',
            '浮游都市的最西面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390185V而且『古罗力亚斯』\n',
            '正好停泊在\n',
            '反方向的东边尽头呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x6A76
@scena.Code('func_14_6A76')
def func_14_6A76():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6A98',
    )

    OP_8C(0x00FE, 45, 400)
    Sleep(1200)

    OP_8C(0x00FE, 225, 400)
    Sleep(1200)

    Jump('func_14_6A76')

    def _loc_6A98(): pass

    label('loc_6A98')

    Return()

# id: 0x0015 offset: 0x6A99
@scena.Code('func_15_6A99')
def func_15_6A99():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6ABB',
    )

    OP_8C(0x00FE, 135, 400)
    Sleep(1500)

    OP_8C(0x00FE, 225, 400)
    Sleep(1500)

    Jump('func_15_6A99')

    def _loc_6ABB(): pass

    label('loc_6ABB')

    Return()

# id: 0x0016 offset: 0x6ABC
@scena.Code('func_16_6ABC')
def func_16_6ABC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6ADE',
    )

    OP_8C(0x00FE, 45, 400)
    Sleep(1300)

    OP_8C(0x00FE, 135, 400)
    Sleep(1300)

    Jump('func_16_6ABC')

    def _loc_6ADE(): pass

    label('loc_6ADE')

    Return()

# id: 0x0017 offset: 0x6ADF
@scena.Code('func_17_6ADF')
def func_17_6ADF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6B01',
    )

    OP_8C(0x00FE, 225, 400)
    Sleep(1800)

    OP_8C(0x00FE, 135, 400)
    Sleep(1800)

    Jump('func_17_6ADF')

    def _loc_6B01(): pass

    label('loc_6B01')

    Return()

# id: 0x0018 offset: 0x6B02
@scena.Code('func_18_6B02')
def func_18_6B02():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6B24',
    )

    OP_8C(0x00FE, 90, 400)
    Sleep(1500)

    OP_8C(0x00FE, 45, 400)
    Sleep(1500)

    Jump('func_18_6B02')

    def _loc_6B24(): pass

    label('loc_6B24')

    Return()

# id: 0x0019 offset: 0x6B25
@scena.Code('func_19_6B25')
def func_19_6B25():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6B47',
    )

    OP_8C(0x00FE, 180, 400)
    Sleep(1200)

    OP_8C(0x00FE, 45, 400)
    Sleep(1200)

    Jump('func_19_6B25')

    def _loc_6B47(): pass

    label('loc_6B47')

    Return()

# id: 0x001A offset: 0x6B48
@scena.Code('func_1A_6B48')
def func_1A_6B48():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6B6A',
    )

    OP_8C(0x00FE, 45, 400)
    Sleep(1300)

    OP_8C(0x00FE, 180, 400)
    Sleep(1300)

    Jump('func_1A_6B48')

    def _loc_6B6A(): pass

    label('loc_6B6A')

    Return()

# id: 0x001B offset: 0x6B6B
@scena.Code('func_1B_6B6B')
def func_1B_6B6B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6B8D',
    )

    OP_8C(0x00FE, 90, 400)
    Sleep(1200)

    OP_8C(0x00FE, 45, 400)
    Sleep(1200)

    Jump('func_1B_6B6B')

    def _loc_6B8D(): pass

    label('loc_6B8D')

    Return()

# id: 0x001C offset: 0x6B8E
@scena.Code('func_1C_6B8E')
def func_1C_6B8E():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 23)
    def _loc_6B98(): pass

    label('loc_6B98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_6BAB',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

    Jump('loc_6B98')

    def _loc_6BAB(): pass

    label('loc_6BAB')

    Return()

# id: 0x001D offset: 0x6BAC
@scena.Code('func_1D_6BAC')
def func_1D_6BAC():
    SetMapFlags(0x02000000)

    Return()

# id: 0x001E offset: 0x6BB2
@scena.Code('func_1E_6BB2')
def func_1E_6BB2():
    ClearMapFlags(0x02000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
