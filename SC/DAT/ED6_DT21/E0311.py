import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0311   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉扎德'),
    TXT(0x02, '奥利维尔'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '金'),
    TXT(0x05, '尤莉亚上尉'),
    TXT(0x06, '摩尔根将军'),
    TXT(0x07, '奈尔'),
    TXT(0x08, '朵洛希'),
    TXT(0x09, '阿加特'),
    TXT(0x0A, '提妲'),
    TXT(0x0B, '凯文神父'),
    TXT(0x0C, '拉赛尔博士'),
    TXT(0x0D, '福音'),
    TXT(0x0E, '零力场发生器'),
    TXT(0x0F, '艾丝蒂尔'),
    TXT(0x10, '约修亚'),
    TXT(0x11, '穆拉少校'),
    TXT(0x12, '酒杯'),
    TXT(0x13, '酒瓶'),
    TXT(0x14, '酒瓶'),
    TXT(0x15, '烹调师凯西'),
    TXT(0x16, '亲卫队队员'),
    TXT(0x17, '雷伊'),
    TXT(0x18, '亲卫队队员'),
    TXT(0x19, '亲卫队队员'),
    TXT(0x1A, '酒杯'),
    TXT(0x1B, '岩穴鱼'),
    TXT(0x1C, '岩穴鱼'),
    TXT(0x1D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0311.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/E0311_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9511
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT26/CH20352._CH', 'ED6_DT26/CH20352P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH02093._CH', 'ED6_DT07/CH02093P._CP'),
        ('ED6_DT07/CH02083._CH', 'ED6_DT07/CH02083P._CP'),
        ('ED6_DT27/CH03013._CH', 'ED6_DT27/CH03013P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
        ('ED6_DT07/CH02023._CH', 'ED6_DT07/CH02023P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT07/CH01323._CH', 'ED6_DT07/CH01323P._CP'),
        ('ED6_DT27/CH03210._CH', 'ED6_DT27/CH03210P._CP'),
    ]

# id: 0x10002 offset: 0x1D2
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0001,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 458766,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            dword_10            = 458766,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2370,
            z                   = 500,
            y                   = -40540,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327694,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2070,
            z                   = 500,
            y                   = -44670,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835023,
            chipIndex           = 15,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2500,
            z                   = 500,
            y                   = -44770,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966095,
            chipIndex           = 15,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 3760,
            z                   = 0,
            y                   = -38100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 1420,
            z                   = 0,
            y                   = -41460,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 1410,
            z                   = 0,
            y                   = -41580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -2370,
            z                   = 200,
            y                   = -46010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -2370,
            z                   = 200,
            y                   = -39890,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -650,
            z                   = 600,
            y                   = -48810,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327694,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -650,
            z                   = 650,
            y                   = -49330,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262158,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2340,
            z                   = 650,
            y                   = -48700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262158,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x552
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x552
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x552
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1410,
            triggerZ            = 0,
            triggerY            = -38950,
            triggerRange        = 800,
            actorX              = 3330,
            actorZ              = 1500,
            actorY              = -38950,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x576
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 0, 0x2200)),
            Expr.Return,
        ),
        'loc_70D',
    )

    SetChrPos(0x001C, 3330, 0, -38950, 270)
    ClearChrFlags(0x001C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59E',
    )

    Jump('loc_70A')

    def _loc_59E(): pass

    label('loc_59E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AE',
    )

    ClearChrFlags(0x0020, 0x0080)

    Jump('loc_70A')

    def _loc_5AE(): pass

    label('loc_5AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F2',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5EA',
    )

    SetChrFlags(0x0009, 0x0010)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 2020, 0, -43620, 270)
    SetChrChipByIndex(0x0009, 34)
    CreateThread(0x0009, 0x00, 0x00, 0x0003)

    def _loc_5EA(): pass

    label('loc_5EA')

    ClearChrFlags(0x001F, 0x0080)

    Jump('loc_70A')

    def _loc_5F2(): pass

    label('loc_5F2')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Or,
            Expr.Return,
        ),
        'loc_635',
    )

    SetChrPos(0x001A, -180, 750, -48810, 180)
    SetChrPos(0x001B, -200, 750, -49380, 180)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_635(): pass

    label('loc_635')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_670',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -420, 200, -48050, 180)
    SetChrFlags(0x0009, 0x0004)
    SetChrChipByIndex(0x0009, 21)
    SetChrSubChip(0x0009, 0)
    TerminateThread(0x0009, 0x00)
    ClearChrFlags(0x0021, 0x0080)

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6BD',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6BD',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -420, 200, -50170, 0)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    ClearChrFlags(0x0022, 0x0080)

    def _loc_6BD(): pass

    label('loc_6BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_70A',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -2370, 200, -48050, 180)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 0)
    TerminateThread(0x0008, 0x00)
    ClearChrFlags(0x0023, 0x0080)

    def _loc_70A(): pass

    label('loc_70A')

    Jump('loc_9F3')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_7CF',
    )

    SetChrPos(0x001C, 3330, 0, -38950, 270)
    ClearChrFlags(0x001C, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_765',
    )

    SetChrPos(0x0008, -2370, 200, -39890, 180)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 0)
    TerminateThread(0x0008, 0x00)
    ClearChrFlags(0x0019, 0x0080)

    def _loc_765(): pass

    label('loc_765')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7CC',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2370, 50, -42000, 0)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    SetChrPos(0x001A, -2070, 750, -41180, 180)
    SetChrPos(0x001B, -2500, 750, -41080, 180)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_7CC(): pass

    label('loc_7CC')

    Jump('loc_9F3')

    def _loc_7CF(): pass

    label('loc_7CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_88A',
    )

    SetChrPos(0x001C, 3330, 0, -38950, 270)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001E, 4990, 0, -39510, 45)
    SetChrFlags(0x001E, 0x0010)
    ClearChrFlags(0x001E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_842',
    )

    SetChrPos(0x0010, -2370, 200, -46010, 0)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0010, 27)
    SetChrSubChip(0x0010, 0)
    TerminateThread(0x0010, 0x00)

    def _loc_842(): pass

    label('loc_842')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_887',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2370, 200, -44020, 180)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_887(): pass

    label('loc_887')

    Jump('loc_9F3')

    def _loc_88A(): pass

    label('loc_88A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_91E',
    )

    SetChrPos(0x001C, 3330, 0, -38950, 270)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8E0',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -2370, 200, -41880, 0)
    SetChrPos(0x0010, 4600, 0, -47630, 270)

    def _loc_8E0(): pass

    label('loc_8E0')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_91B',
    )

    SetChrPos(0x0008, -2370, 200, -39890, 180)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 0)
    TerminateThread(0x0008, 0x00)
    ClearChrFlags(0x0019, 0x0080)

    def _loc_91B(): pass

    label('loc_91B')

    Jump('loc_9F3')

    def _loc_91E(): pass

    label('loc_91E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_97E',
    )

    SetChrPos(0x001C, 3330, 0, -38950, 270)
    ClearChrFlags(0x001C, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_97B',
    )

    SetChrPos(0x000B, -2370, 200, -44020, 180)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_97B(): pass

    label('loc_97B')

    Jump('loc_9F3')

    def _loc_97E(): pass

    label('loc_97E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_992',
    )

    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)

    Jump('loc_9F3')

    def _loc_992(): pass

    label('loc_992')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9F3',
    )

    SetChrPos(0x000D, 1730, 0, 53900, 0)
    ClearChrFlags(0x000D, 0x0080)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    SetChrPos(0x0009, -2370, 200, -39890, 180)
    SetChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 21)
    SetChrSubChip(0x0009, 0)
    TerminateThread(0x0009, 0x00)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)

    def _loc_9F3(): pass

    label('loc_9F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_A12',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0006)

    Jump('loc_ABC')

    def _loc_A12(): pass

    label('loc_A12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_A31',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x0008)

    Jump('loc_ABC')

    def _loc_A31(): pass

    label('loc_A31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_A47',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 0x000D)

    Jump('loc_ABC')

    def _loc_A47(): pass

    label('loc_A47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_A5D',
    )

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 0x000E)

    Jump('loc_ABC')

    def _loc_A5D(): pass

    label('loc_A5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_A7C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 0x000F)

    Jump('loc_ABC')

    def _loc_A7C(): pass

    label('loc_A7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_A9B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 0x0010)

    Jump('loc_ABC')

    def _loc_A9B(): pass

    label('loc_A9B')

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
        'loc_ABC',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0007)

    def _loc_ABC(): pass

    label('loc_ABC')

    Return()

# id: 0x0001 offset: 0xABD
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ADB',
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

    def _loc_ADB(): pass

    label('loc_ADB')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_AFA',
    )

    OP_B1('E0311_1')

    Jump('loc_B03')

    def _loc_AFA(): pass

    label('loc_AFA')

    OP_B1('E0311_2')

    def _loc_B03(): pass

    label('loc_B03')

    Jump('loc_B27')

    def _loc_B06(): pass

    label('loc_B06')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1E',
    )

    OP_B1('E0311_2')

    Jump('loc_B27')

    def _loc_B1E(): pass

    label('loc_B1E')

    OP_B1('E0311_1')

    def _loc_B27(): pass

    label('loc_B27')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B50',
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

    Jump('loc_B5D')

    def _loc_B50(): pass

    label('loc_B50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5D',
    )

    OP_22(0x007A, 0x01, 0x46)

    def _loc_B5D(): pass

    label('loc_B5D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 4, 0x1E24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B88',
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

    def _loc_B88(): pass

    label('loc_B88')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_BB6',
    )

    SetMapFlags(0x02000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_BAD',
    )

    OP_A3(0x000F)

    Jump('loc_BB6')

    def _loc_BAD(): pass

    label('loc_BAD')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BB6(): pass

    label('loc_BB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BFB',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDF',
    )

    Call(0, 0x0021)

    Jump('loc_BFB')

    def _loc_BDF(): pass

    label('loc_BDF')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFB',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x1),
            (Expr.PushLong, 0x49),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFB',
    )

    Call(0, 0x0022)

    def _loc_BFB(): pass

    label('loc_BFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_C05',
    )

    Jump('loc_C24')

    def _loc_C05(): pass

    label('loc_C05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_C0F',
    )

    Jump('loc_C24')

    def _loc_C0F(): pass

    label('loc_C0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C24',
    )

    OP_74(0x00FF, 0x00000010, 0x0001)

    def _loc_C24(): pass

    label('loc_C24')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_C33',
    )

    OP_65(0x00, 0x0001)

    def _loc_C33(): pass

    label('loc_C33')

    Return()

# id: 0x0002 offset: 0xC34
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
        'loc_C59',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_D9B')

    def _loc_C59(): pass

    label('loc_C59')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C72',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_D9B')

    def _loc_C72(): pass

    label('loc_C72')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C8B',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_D9B')

    def _loc_C8B(): pass

    label('loc_C8B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA4',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_D9B')

    def _loc_CA4(): pass

    label('loc_CA4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBD',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_D9B')

    def _loc_CBD(): pass

    label('loc_CBD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CD6',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_D9B')

    def _loc_CD6(): pass

    label('loc_CD6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CEF',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_D9B')

    def _loc_CEF(): pass

    label('loc_CEF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D08',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_D9B')

    def _loc_D08(): pass

    label('loc_D08')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D21',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_D9B')

    def _loc_D21(): pass

    label('loc_D21')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D3A',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_D9B')

    def _loc_D3A(): pass

    label('loc_D3A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D53',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_D9B')

    def _loc_D53(): pass

    label('loc_D53')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D6C',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_D9B')

    def _loc_D6C(): pass

    label('loc_D6C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D85',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_D9B')

    def _loc_D85(): pass

    label('loc_D85')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D9B',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_D9B(): pass

    label('loc_D9B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DB0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_D9B')

    def _loc_DB0(): pass

    label('loc_DB0')

    Return()

# id: 0x0003 offset: 0xDB1
@scena.Code('func_03_DB1')
def func_03_DB1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E83',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_DE7',
    )

    SetChrSubChip(0x00FE, 0)
    Sleep(50)

    SetChrSubChip(0x00FE, 1)
    Sleep(50)

    SetChrSubChip(0x00FE, 2)

    Jump('loc_E00')

    def _loc_DE7(): pass

    label('loc_DE7')

    SetChrSubChip(0x00FE, 0)
    Sleep(150)

    SetChrSubChip(0x00FE, 1)
    Sleep(150)

    SetChrSubChip(0x00FE, 2)

    def _loc_E00(): pass

    label('loc_E00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_E0D',
    )

    OP_A3(0x000E)

    Jump('loc_E49')

    def _loc_E0D(): pass

    label('loc_E0D')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x5),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_E49',
    )

    Sleep(80)

    SetChrSubChip(0x00FE, 3)
    Sleep(100)

    SetChrSubChip(0x00FE, 4)
    Sleep(150)

    SetChrSubChip(0x00FE, 3)
    Sleep(100)

    SetChrSubChip(0x00FE, 2)
    OP_A2(0x000E)

    def _loc_E49(): pass

    label('loc_E49')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_E6C',
    )

    Sleep(50)

    SetChrSubChip(0x00FE, 1)
    Sleep(50)

    Jump('loc_E80')

    def _loc_E6C(): pass

    label('loc_E6C')

    SetChrSubChip(0x00FE, 2)
    Sleep(150)

    SetChrSubChip(0x00FE, 1)
    Sleep(150)

    def _loc_E80(): pass

    label('loc_E80')

    Jump('func_03_DB1')

    def _loc_E83(): pass

    label('loc_E83')

    Return()

# id: 0x0004 offset: 0xE84
@scena.Code('func_04_E84')
def func_04_E84():
    Call(1, 0x0006)

    Return()

# id: 0x0005 offset: 0xE89
@scena.Code('func_05_E89')
def func_05_E89():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_F00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Return,
        ),
        'loc_EBB',
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

    Jump('loc_EFD')

    def _loc_EBB(): pass

    label('loc_EBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_EE2',
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

    Jump('loc_EFD')

    def _loc_EE2(): pass

    label('loc_EE2')

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

    def _loc_EFD(): pass

    label('loc_EFD')

    Jump('loc_F7E')

    def _loc_F00(): pass

    label('loc_F00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_F23',
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

    Jump('loc_F7E')

    def _loc_F23(): pass

    label('loc_F23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_F44',
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

    Jump('loc_F7E')

    def _loc_F44(): pass

    label('loc_F44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_F65',
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

    Jump('loc_F7E')

    def _loc_F65(): pass

    label('loc_F65')

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

    def _loc_F7E(): pass

    label('loc_F7E')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_114F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FDF',
    )

    Jump('loc_114C')

    def _loc_FDF(): pass

    label('loc_FDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FEA',
    )

    Jump('loc_114C')

    def _loc_FEA(): pass

    label('loc_FEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1034',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_102D',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 2020, 0, -43620, 270)
    SetChrChipByIndex(0x0009, 34)

    If(
        (
            (Expr.PushValueByIndex, 0x1),
            (Expr.PushLong, 0x49),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_102A',
    )

    Call(0, 0x0021)

    def _loc_102A(): pass

    label('loc_102A')

    Jump('loc_1031')

    def _loc_102D(): pass

    label('loc_102D')

    Call(0, 0x0022)
    def _loc_1031(): pass

    label('loc_1031')

    Jump('loc_114C')

    def _loc_1034(): pass

    label('loc_1034')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1077',
    )

    SetChrPos(0x001A, -180, 750, -48810, 180)
    SetChrPos(0x001B, -200, 750, -49380, 180)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_1077(): pass

    label('loc_1077')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_10B2',
    )

    SetChrPos(0x0009, -420, 200, -48050, 180)
    SetChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 21)
    SetChrSubChip(0x0009, 0)
    TerminateThread(0x0009, 0x00)
    ClearChrFlags(0x0021, 0x0080)

    def _loc_10B2(): pass

    label('loc_10B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10FF',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_10FF',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -420, 200, -50170, 0)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    ClearChrFlags(0x0022, 0x0080)

    def _loc_10FF(): pass

    label('loc_10FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_114C',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_114C',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -2370, 200, -48050, 180)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 0)
    TerminateThread(0x0008, 0x00)
    ClearChrFlags(0x0023, 0x0080)

    def _loc_114C(): pass

    label('loc_114C')

    Jump('loc_134A')

    def _loc_114F(): pass

    label('loc_114F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_1200',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1196',
    )

    SetChrPos(0x0008, -2370, 200, -39890, 180)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 0)
    TerminateThread(0x0008, 0x00)
    ClearChrFlags(0x0019, 0x0080)

    def _loc_1196(): pass

    label('loc_1196')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11FD',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2370, 50, -42000, 0)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    SetChrPos(0x001A, -2070, 750, -41180, 180)
    SetChrPos(0x001B, -2500, 750, -41080, 180)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_11FD(): pass

    label('loc_11FD')

    Jump('loc_134A')

    def _loc_1200(): pass

    label('loc_1200')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_128A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1242',
    )

    SetChrPos(0x0010, -2370, 200, -46010, 0)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0010, 27)
    SetChrSubChip(0x0010, 0)
    TerminateThread(0x0010, 0x00)

    def _loc_1242(): pass

    label('loc_1242')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1287',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2370, 200, -44020, 180)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000B, 0x00)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)

    def _loc_1287(): pass

    label('loc_1287')

    Jump('loc_134A')

    def _loc_128A(): pass

    label('loc_128A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_1308',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12C5',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -2370, 200, -41880, 0)
    SetChrPos(0x0010, 4600, 0, -47630, 270)

    def _loc_12C5(): pass

    label('loc_12C5')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1305',
    )

    SetChrPos(0x0008, -2370, 200, -39890, 180)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 0)
    TerminateThread(0x0008, 0x00)
    ClearChrFlags(0x0019, 0x0080)

    def _loc_1305(): pass

    label('loc_1305')

    Jump('loc_134A')

    def _loc_1308(): pass

    label('loc_1308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_134A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_134A',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2370, 200, -44020, 180)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 0)
    TerminateThread(0x0008, 0x00)

    def _loc_134A(): pass

    label('loc_134A')

    OP_0D()

    Return()

# id: 0x0006 offset: 0x134C
@scena.Code('func_06_134C')
def func_06_134C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrPos(0x000D, 1070, 200, 53790, 180)
    SetChrPos(0x000C, 2370, 0, 54390, 180)
    SetChrPos(0x0101, -1140, 100, 52380, 90)
    SetChrPos(0x0008, -1140, 100, 51220, 90)
    SetChrPos(0x000B, -1140, 100, 49960, 90)
    SetChrPos(0x000A, 2880, 200, 52400, 270)
    SetChrPos(0x0009, 2880, 200, 51200, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrChipByIndex(0x0101, 19)
    SetChrSubChip(0x0101, 1)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 1)
    SetChrChipByIndex(0x0009, 21)
    SetChrSubChip(0x0009, 2)
    SetChrChipByIndex(0x000A, 22)
    SetChrSubChip(0x000A, 2)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 1)
    SetChrChipByIndex(0x000D, 25)
    SetChrSubChip(0x000D, 0)
    OP_6D(1690, 0, 46880, 0)
    OP_67(0, 7340, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310179V──那么，开始介绍由王国军\n',
            '执行的『古龙捕获作战』计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_1504')
    def lambda_1504():
        OP_6D(2029, 100, 52820, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1504)

    @scena.Lambda('lambda_151C')
    def lambda_151C():
        OP_67(0, 6340, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_151C)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0600310180V#163F#5P本次作战将由\n',
            '飞行舰队来完成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310181V地面部队只负责利贝尔各地\n',
            '的警戒和防卫工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310182V#1015F利贝尔各地？就是说\n',
            '不只是柏斯地区吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310183V#160F#5P根据的昨天的情况来看，\n',
            '龙的飞行能力相当惊人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310184V不知其它地方何时又会遭受袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310185V#1003F嗯，的确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310186V#160F#5P所以在本次的作战里，\n',
            '除了这艘『埃尔赛尤』之外，\n',
            '又投入了警备飞艇１２艘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310187V这相当于所有\n',
            '警备艇数量的五分之二。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030310188V#023F#6P那种警备艇有１２艘啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310189V#030F#2P这下可真是大张旗鼓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310190V#163F#5P──尤莉亚上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310191V#178F#5P是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17CD')
    def lambda_17CD():
        OP_6D(2029, 100, 53820, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17CD)

    OP_8C(0x000C, 270, 400)
    OP_8C(0x000C, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_22(0x009C, 0x00, 0x64)
    Sleep(500)

    OP_22(0x009D, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    OP_74(0x00FF, 0x00000010, 0x0001)
    OP_0D()
    Sleep(500)

    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS136._CH')
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS210._CH')
    OP_C5(0x02, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS211._CH')
    OP_C5(0x03, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS212._CH')
    OP_C5(0x04, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS213._CH')
    OP_C5(0x05, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS214._CH')
    OP_C5(0x06, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS215._CH')
    OP_C5(0x07, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS216._CH')
    OP_C5(0x08, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS217._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1000)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010310192V#1004F哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080310193V#073F这个是……\n',
            '本次的作战行动图呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310194V#163F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310195V#160F现在，这艘『埃尔赛尤』\n',
            '正在柏斯上空进行巡航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310196V#160F在本次作战中，『埃尔赛尤』\n',
            '将担当作战司令部的功能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310197V至于实际的巡逻任务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310198V#163F就由装载了广域雷达的\n',
            '８艘警备艇负责。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310199V如果龙出现在上空，\n',
            '应该能成功捕捉到方位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310200V#160F然后一旦发现了龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310201V#160F警备艇将迅速前往，\n',
            '用机关炮进行牵制，\n',
            '并把龙诱导至瓦雷利亚湖上空。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x05, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310202V#163F而在发现龙的同时，\n',
            '装载了麻醉弹的警备艇\n',
            '就会从雷斯顿要塞紧急起飞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600310203V#163F──前去迎击被围追堵截的龙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310204V用飞船上所有的\n',
            '麻醉弹使龙昏睡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x03, -1, 500, 0)
    Sleep(2000)

    SetMessageWindowPos(72, 320, 56, 3)

    @scena.Lambda('lambda_1E81')
    def lambda_1E81():
        OP_6D(2029, 100, 52820, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E81)

    OP_8C(0x000C, 180, 0)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 0, 0)
    OP_C6(0x04, 0x03, 16777215, 0, 0)
    OP_C6(0x05, 0x03, 16777215, 0, 0)
    OP_C6(0x06, 0x03, 16777215, 0, 0)
    OP_C6(0x07, 0x03, 16777215, 0, 0)
    OP_C6(0x08, 0x03, 16777215, 1000, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)

    ChrTalk(
        0x000D,
        (
            '#0600310205V#160F#5P这就是『古龙捕获作战』的概要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310206V#1004F哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030310207V#025F#6P果然和协会的\n',
            '作战规模不同……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310208V#022F如果龙没有被麻醉弹迷昏，\n',
            '是不是会从捕获转换为剿灭呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310209V#163F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310210V只能集中整个舰队的火力\n',
            '来消灭它了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310211V虽然女王陛下希望我们\n',
            '优先考虑捕获而非剿灭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310212V#1015F咦……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310213V#160F#5P毕竟龙是传说中的\n',
            '极为珍贵的生物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310214V女王表示不忍心进行剿灭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310215V#043F#2P说得也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310216V而且它很有可能是被\n',
            '『结社』操控了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310217V#1007F这样啊……的确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310218V#1020F说、说到这个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310219V操纵龙的那个叫莱维的男人\n',
            '不是持有『福音』吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310220V#163F#5P嗯……\n',
            '你是说有导力停止现象的危险吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310221V#160F据拉赛尔博士所言，\n',
            '导力停止现象的连锁范围\n',
            '大约是５亚矩左右。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310222V所以各舰艇将会和龙\n',
            '保持10亚矩以上的距离。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310223V这样一来应该没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310224V#1025F原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310225V#031F#2P嗯，真令人佩服。\n',
            '这可以说是万全的对策了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310226V#163F我们的『百日战役』经验\n',
            '也不是毫无意义的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310227V#160F不过这次作战如果失败的话，\n',
            '就真的一筹莫展了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310228V到时候就要拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310229V#1007F话说得这么好听……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310230V#1019F其实你根本不认为\n',
            '作战会失败吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310231V#163F哼哼，那是自然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310232V这个计划唯一的问题\n',
            '就是要在发现龙之前\n',
            '耐心地等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310233V#1015F的确……\n',
            '不过如果这是白费功夫怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080310234V#074F#6P不，稍微分析一下『结社』\n',
            '至今为止的作法就知道那不可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310235V#072F他们一定会利用那头龙\n',
            '做出一些事情来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310236V#1002F嗯……的确是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 225, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100310237V#170F#5P那么各位游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310238V一旦发现龙之后，\n',
            '我们会用广播告知的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310239V在此之前，\n',
            '你们就在舰内轻松休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(870, 0, 3010, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrPos(0x0101, 870, 0, 3010, 180)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x1A1E)
    OP_28(0x0095, 0x01, 0x0002)
    OP_28(0x0095, 0x01, 0x0004)
    OP_28(0x0095, 0x01, 0x0008)
    OP_28(0x0095, 0x01, 0x0010)
    Sleep(1000)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x279D
@scena.Code('func_07_279D')
def func_07_279D():
    EventBegin(0x00)
    OP_22(0x00A6, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('尤莉亚的声音')

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

# id: 0x0008 offset: 0x28D5
@scena.Code('func_08_28D5')
def func_08_28D5():
    EventBegin(0x00)
    OP_6D(940, 950, 48420, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1010, 100, 48750, 90)
    SetChrPos(0x0103, -1060, 100, 47520, 90)
    SetChrPos(0x0104, -1040, 100, 46300, 90)
    SetChrPos(0x0108, -1140, 100, 49960, 90)
    SetChrPos(0x000D, 2900, 250, 48750, 270)
    SetChrPos(0x000C, 2950, 230, 47470, 270)
    SetChrPos(0x0105, 2900, 200, 49900, 270)
    ClearChrFlags(0x0103, 0x0080)
    ClearChrFlags(0x0104, 0x0080)
    ClearChrFlags(0x0108, 0x0080)
    ClearChrFlags(0x0105, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_4A(0x0103, 255)
    OP_4A(0x0104, 255)
    OP_4A(0x0108, 255)
    OP_4A(0x0105, 255)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0104, 0x0004)
    SetChrFlags(0x0105, 0x0004)
    SetChrFlags(0x0108, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrChipByIndex(0x0101, 19)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0103, 20)
    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0104, 21)
    SetChrSubChip(0x0104, 0)
    SetChrChipByIndex(0x0105, 22)
    SetChrSubChip(0x0105, 0)
    SetChrChipByIndex(0x0108, 23)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x000C, 24)
    SetChrSubChip(0x000C, 0)
    SetChrChipByIndex(0x000D, 25)
    SetChrSubChip(0x000D, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100310658V#176F#2P龙逃进了\n',
            '迷雾峡谷的西北部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310659V#178F那里是比空贼巢穴\n',
            '还要更深入的险处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0105, 1)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060310660V#042F#5P也就是说，用飞船\n',
            '很难进行搜索是吗？',
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
            '#0100310661V#176F#2P很遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310662V#175F或许只能从地面\n',
            '派遣搜索部队了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310663V#1020F#6P等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310664V如果派遣大批士兵过去，\n',
            '龙又会逃跑的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0105, 0)
    Sleep(100)

    SetChrSubChip(0x000C, 0)
    Sleep(300)

    ChrTalk(
        0x0103,
        (
            '#0030310665V#026F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310666V#020F最好由少数人进行搜索，\n',
            '并设法找出龙的破绽来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310667V#160F#2P也就是说，\n',
            '接下来交给你们是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080310668V#074F#6P对于险处的探索，\n',
            '我们比军人要更加熟悉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310669V#070F这也是择材而用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310670V#163F#2P……唔………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310671V#160F不过，你们有\n',
            '明确的搜索方向吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310672V我记得峡谷西北部\n',
            '应该没什么路可走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310673V如果漫无目的地乱找，\n',
            '几天时间都不够用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310674V#1015F#6P这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    SetChrPos(0x0010, 1000, 0, 40690, 0)

    NpcTalk(
        0x0010,
        '青年的声音',
        (
            '#0050310675V#1P……这你不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    OP_1D(0x01)
    Sleep(500)

    @scena.Lambda('lambda_2EBF')
    def lambda_2EBF():
        OP_6D(2800, 100, 48400, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2EBF)

    @scena.Lambda('lambda_2ED7')
    def lambda_2ED7():
        OP_67(0, 4370, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2ED7)

    @scena.Lambda('lambda_2EEF')
    def lambda_2EEF():
        OP_6E(311, 4000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_2EEF)

    @scena.Lambda('lambda_2EFF')
    def lambda_2EFF():
        OP_6C(52000, 4000)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_2EFF)

    @scena.Lambda('lambda_2F0F')
    def lambda_2F0F():
        OP_6B(2840, 4000)

        ExitThread()

    DispatchAsync(0x0104, 0x0003, lambda_2F0F)

    SetChrSubChip(0x0101, 2)
    SetChrSubChip(0x0103, 2)
    Sleep(50)

    SetChrSubChip(0x0104, 2)
    SetChrSubChip(0x0105, 1)
    Sleep(50)

    SetChrSubChip(0x0108, 2)
    SetChrSubChip(0x000C, 1)
    Sleep(50)

    SetChrSubChip(0x000D, 1)
    Sleep(800)

    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    CreateThread(0x0010, 0x01, 0x00, 0x0009)
    CreateThread(0x0011, 0x01, 0x00, 0x000A)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000D,
        (
            '#0600310676V#161F#5P你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310677V#1004F#5P阿加特、提妲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310678V#051F哟！打扰各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070310679V#560F#6P那个那个，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310680V#1008F#5P你们怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310681V#1020F而、而且你的伤…\n',
            '已经好了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310682V#053F伤口没问题了。\n',
            '只不过是一点擦伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310683V#1019F#5P……提妲，是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070310684V#066F#6P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310685V阿加特哥哥已经\n',
            '不会再勉强乱来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310686V#1006F#5P是吗……\n',
            '那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310687V#163F#5P哼，体力倒是\n',
            '永远用不完的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310688V#160F你叫我不用担心，\n',
            '不过作战的始末你知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310689V#050F嗯，卢格兰老爷子\n',
            '大致都跟我说过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310690V龙消失在\n',
            '迷雾峡谷西北部了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310691V#1015F#5P嗯，是没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310692V#053F关于迷雾峡谷，\n',
            '我知道有个人很熟悉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310693V如果去找他的话，应该可以\n',
            '前往龙所躲藏的西北部吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310694V#161F#5P喔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310695V#1004F#5P那、那是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310696V#051F就是住在峡谷东侧的\n',
            '维姆拉大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310697V据说他以前曾经去过\n',
            '没有道路的西北部。',
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
        'loc_3422',
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
            TXT(0x00, '【◇在后篇见过维姆拉】\n'),
            TXT(0x01, '【◇在后篇没见过维姆拉】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_3416'),
        (0x00000001, 'loc_341C'),
        (-1, 'loc_3422'),
    )

    def _loc_3416(): pass

    label('loc_3416')

    OP_A2(0x1A80)

    Jump('loc_3422')

    def _loc_341C(): pass

    label('loc_341C')

    OP_A3(0x1A80)

    Jump('loc_3422')

    def _loc_3422(): pass

    label('loc_3422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 0, 0x1A80)),
            Expr.Return,
        ),
        'loc_3469',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310698V#1011F#5P原来如此，是住在\n',
            '那间小屋里的大叔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3469(): pass

    label('loc_3469')

    ChrTalk(
        0x0104,
        (
            '#0040310699V#031F#5P呼，不愧是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310700V平时勤劳地收集情报，\n',
            '终于派上用场了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310701V#163F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310702V#160F不过，当你们\n',
            '找到龙之后又要怎么做？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310703V那可不是光靠你们几个\n',
            '就能轻易消灭的对手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310704V#050F龙的额头被嵌入了\n',
            '『福音』对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310705V当然是首先\n',
            '解决那个东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310706V#161F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030310707V#022F#5P仔细想想，龙很有可能是\n',
            '因为那个东西才会失去控制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310708V迄今为止，『福音』\n',
            '也已经引发了种种异常现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080310709V#074F#5P若能使『福音』失效的话，\n',
            '就可以让龙恢复正常吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310710V#070F嗯……道理是说得通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310711V#176F#5P说到使『福音』失效，\n',
            '我想起了凯文先生使用过的方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310712V#175F那时候是用古代遗物\n',
            '大力敲击『福音』，\n',
            '使其短路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310713V#051F用不着那么麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310714V只要连外壳一起\n',
            '把『福音』破坏就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100310715V#173F#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310716V#1004F#5P等、等等！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310717V要破坏『福音』\n',
            '有那么容易吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310718V我记得它的外壳\n',
            '是非常坚硬的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310719V#053F关于这一点\n',
            '也有办法解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310720V#050F……就是它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrFlags(0x0010, 0x0002)
    SetChrChipByIndex(0x0010, 10)
    SetChrSubChip(0x0010, 16)
    OP_0D()
    Sleep(1000)

    OP_AD(0x00240098, 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010310721V#1004F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030310722V#020F底部好像装着\n',
            '什么零件的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1500)

    ChrTalk(
        0x0010,
        (
            '#0050310723V#053F这是今早拉赛尔老爷子\n',
            '给我寄来的新发明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310724V#051F用来破坏『福音』\n',
            '外壳的零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310725V#1004F#1P#3S咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040310726V#033F#5P嗯……\n',
            '这东西究竟是什么构造？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070310727V#061F#6P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310728V#560F这个零件似乎可以\n',
            '使刀刃部位产生出只让\n',
            '外壳材质崩溃的高频振动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310729V由于振动的缘故，使用两三次后\n',
            '就会因承受不住而坏掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310730V#067F不过只要能够顺利融入刀身，\n',
            '据说就能够顺利破坏『福音』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310731V#1008F#5P虽、虽然我不太明白,\n',
            '不过似乎是相当厉害的发明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040310732V#035F#5P呵……\n',
            '真不愧是王国第一的天才学者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    ClearChrFlags(0x0010, 0x0002)
    SetChrChipByIndex(0x0010, 8)
    SetChrSubChip(0x0010, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0050310733V#053F虽然刚刚才\n',
            '请提妲帮我装上。\n',
            '但似乎可以毫无问题地正常运作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310734V接下来只要找到那条龙，\n',
            '攻击它的额头部位就可以了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310735V#051F怎么样，将军大人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310736V#163F#5P真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310737V#160F你们准备得这么齐全\n',
            '我不是只能点头同意了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0101, 0)
    Sleep(50)

    SetChrSubChip(0x0103, 0)
    Sleep(50)

    SetChrSubChip(0x0104, 0)
    Sleep(50)

    SetChrSubChip(0x0108, 0)
    Sleep(50)

    SetChrSubChip(0x000C, 2)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010310738V#1006F#6P那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310739V#050F这个任务可以交给我们了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310740V#163F#5P嗯……\n',
            '尽你们所能地去做吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310741V#160F不过为了以防万一\n',
            '我会在峡谷周围部署飞行舰队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310742V以便在龙逃走的时候，\n',
            '能及时采取应对措施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050310743V#051F很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310744V你们就别浪费子弹，\n',
            '还是看看我的厉害吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x3F6C
@scena.Code('func_09_3F6C')
def func_09_3F6C():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 1000, 0, 40690, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3F93')
    def lambda_3F93():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3F93)

    OP_8E(0x00FE, 1620, 0, 44510, 2000, 0x00)
    OP_8C(0x00FE, 0, 0)

    Return()

# id: 0x000A offset: 0x3FBB
@scena.Code('func_0A_3FBB')
def func_0A_3FBB():
    Sleep(500)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 1000, 0, 40690, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3FE7')
    def lambda_3FE7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3FE7)

    OP_8F(0x00FE, -90, 0, 44410, 2000, 0x00)
    OP_8C(0x00FE, 0, 0)

    Return()

# id: 0x000B offset: 0x400F
@scena.Code('func_0B_400F')
def func_0B_400F():
    OP_8E(0x00FE, -1210, 0, 43230, 2000, 0x00)
    OP_8E(0x00FE, -1210, 0, 47180, 2000, 0x00)
    OP_8C(0x00FE, 0, 0)

    Return()

# id: 0x000C offset: 0x403F
@scena.Code('func_0C_403F')
def func_0C_403F():
    Sleep(500)

    OP_8E(0x00FE, -1210, 0, 43230, 2000, 0x00)
    OP_8E(0x00FE, -1210, 0, 46360, 2000, 0x00)
    OP_8C(0x00FE, 0, 0)

    Return()

# id: 0x000D offset: 0x4074
@scena.Code('func_0D_4074')
def func_0D_4074():
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
        'loc_408B',
    )

    Call(0, 0x001D)
    Call(0, 0x001E)

    def _loc_408B(): pass

    label('loc_408B')

    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6D(2220, 100, 52500, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x0013, 1060, 150, 53910, 180)
    SetChrPos(0x000C, 2250, 0, 54450, 180)
    SetChrPos(0x0101, -1140, 100, 52380, 90)
    SetChrPos(0x0102, -1140, 100, 51220, 90)
    SetChrPos(0x0008, -1140, 100, 49960, 90)
    SetChrPos(0x000B, -1190, 100, 48660, 90)
    SetChrPos(0x000A, 2950, 200, 52400, 270)
    SetChrPos(0x0011, 2950, 200, 51200, 270)
    SetChrPos(0x0010, 2950, 200, 49840, 270)
    SetChrPos(0x0012, 2950, 200, 48620, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    OP_4A(0x0010, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x0012, 255)
    SetChrChipByIndex(0x0101, 19)
    SetChrSubChip(0x0101, 1)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 1)
    SetChrChipByIndex(0x000A, 22)
    SetChrSubChip(0x000A, 2)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 1)
    SetChrChipByIndex(0x0102, 26)
    SetChrSubChip(0x0102, 1)
    SetChrChipByIndex(0x0010, 27)
    SetChrSubChip(0x0010, 2)
    SetChrChipByIndex(0x0011, 28)
    SetChrSubChip(0x0011, 2)
    SetChrChipByIndex(0x0012, 29)
    SetChrSubChip(0x0012, 2)
    SetChrChipByIndex(0x0013, 30)
    SetChrSubChip(0x0013, 0)
    OP_72(0x0007, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0540340925V#104F#5P原来如此……\n',
            '竟然是这个样子的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340926V#1002F#6P总之\n',
            '那个『β』就先交给博士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340927V#1004F啊，我还在塔里\n',
            '发现了这种东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把在翡翠之塔得到的数据水晶交出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(ItemTable['数据水晶０'], 1)
    RemoveItem(ItemTable['数据水晶１'], 1)
    RemoveItem(ItemTable['数据水晶２'], 1)
    RemoveItem(ItemTable['数据水晶３'], 1)
    Sleep(100)

    SetChrSubChip(0x0013, 2)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0540340928V#103F#5P哦……\n',
            '古代导力文明时用来\n',
            '储存情报的记忆媒体吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340929V#1042F#6P内部数据\n',
            '已经损坏了，\n',
            '能想办法修复吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540340930V#104F#5P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340931V#100F它好像和结晶回路一样\n',
            '都是用七耀石材料制成的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340932V可能要花些时间，不过『卡佩尔』\n',
            '也许可以想办法分析出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340933V#1006F#6P可以帮我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540340934V#101F#5P嗯，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0013, 0)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0540340935V#102F#5P『里塔』似乎拥有着延伸到\n',
            '其他空间的特殊内部构造.....',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340936V#104F嗯嗯……\n',
            '要是我也能一起去就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070340937V#067F爷、爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340938V#1043F#6P恐怕那才是\n',
            '四轮之塔的真正形态吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340939V#1042F封印着『辉之环』\n',
            '的『设备塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180340940V#1067F既然它恢复了原状，\n',
            '应该可以放心了才对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340941V#1068F不过连塔顶的装置也停止了，\n',
            '这实在让人感到有些在意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540340942V#104F#5P嗯……的确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340943V#1002F#6P无论如何……\n',
            '我们不能就这样放任\n',
            '『结社』的那些家伙不管。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340944V#1005F必须赶紧前往下一座塔才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060340945V#042F尤莉亚。\n',
            '得到其它塔的情报了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100340946V#176F#5P刚才从蔡斯方面的\n',
            '侦察部队传来了后续报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340947V#178F出现在『红莲之塔』中的，\n',
            '似乎是一个戴着墨镜的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340948V#1026F#6P啊……',
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
        'loc_48B4',
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
        'loc_48B4',
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
        (0x00000000, 'loc_48A8'),
        (0x00000001, 'loc_48AE'),
        (-1, 'loc_48B4'),
    )

    def _loc_48A8(): pass

    label('loc_48A8')

    OP_A2(0x1201)

    Jump('loc_48B4')

    def _loc_48AE(): pass

    label('loc_48AE')

    OP_A3(0x1200)

    Jump('loc_48B4')

    def _loc_48B4(): pass

    label('loc_48B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_48E3',
    )

    ChrTalk(
        0x0010,
        (
            '#0050340949V#057F『瘦狼』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_490F')

    def _loc_48E3(): pass

    label('loc_48E3')

    ChrTalk(
        0x0008,
        (
            '#0030340950V#022F#6P『瘦狼』瓦鲁特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_490F(): pass

    label('loc_490F')

    ChrTalk(
        0x000B,
        (
            '#0080340951V#070F#6P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340952V#074F面对面一较高下的\n',
            '机会终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 2)
    SetChrSubChip(0x0102, 2)
    Sleep(100)

    SetChrSubChip(0x0008, 2)
    SetChrSubChip(0x000A, 1)
    Sleep(100)

    SetChrSubChip(0x0010, 0)
    SetChrSubChip(0x0011, 1)
    Sleep(100)

    SetChrSubChip(0x0012, 0)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010340953V#1026F#5P金先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080340954V#070F#6P艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340955V我也和你们一起\n',
            '去『红莲之塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x4A38
@scena.Code('func_0E_4A38')
def func_0E_4A38():
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
        'loc_4A4F',
    )

    Call(0, 0x001D)
    Call(0, 0x001F)

    def _loc_4A4F(): pass

    label('loc_4A4F')

    OP_6D(2220, 100, 52500, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x0013, 1060, 150, 53910, 180)
    SetChrPos(0x000C, 2250, 0, 54450, 180)
    SetChrPos(0x0101, -1140, 100, 52380, 90)
    SetChrPos(0x0102, -1140, 100, 51220, 90)
    SetChrPos(0x0008, -1140, 100, 49960, 90)
    SetChrPos(0x0108, -1190, 100, 48660, 90)
    SetChrPos(0x000A, 2950, 200, 52400, 270)
    SetChrPos(0x0011, 2950, 200, 51200, 270)
    SetChrPos(0x0010, 2950, 200, 49840, 270)
    SetChrPos(0x0012, 2950, 200, 48620, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0108, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0108, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    OP_4A(0x0010, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0108, 255)
    OP_4A(0x0012, 255)
    SetChrChipByIndex(0x0101, 19)
    SetChrSubChip(0x0101, 1)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 1)
    SetChrChipByIndex(0x000A, 22)
    SetChrSubChip(0x000A, 2)
    SetChrChipByIndex(0x0108, 23)
    SetChrSubChip(0x0108, 1)
    SetChrChipByIndex(0x0102, 26)
    SetChrSubChip(0x0102, 1)
    SetChrChipByIndex(0x0010, 27)
    SetChrSubChip(0x0010, 2)
    SetChrChipByIndex(0x0011, 28)
    SetChrSubChip(0x0011, 2)
    SetChrChipByIndex(0x0012, 29)
    SetChrSubChip(0x0012, 2)
    SetChrChipByIndex(0x0013, 30)
    SetChrSubChip(0x0013, 0)
    OP_72(0x0007, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0540341203V#103F#5P什么……\n',
            '居然只身一人闯入那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341204V#101F她本来就是个了不起的女孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100341205V#171F#5P说到蔡斯支部的雾香小姐，\n',
            '我听说是一位非常优秀的女性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341206V真想和她见一次面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341207V#1008F#6P（嗯……\n',
            '尤莉亚小姐和雾香小姐吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341208V#1040F#6P（在优秀程度方面，\n',
            '搞不好是难分伯仲呢。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341209V#074F#6P先不说这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341210V#072F这次也一样，虽然塔恢复原状了，\n',
            '可是塔顶上的装置却也停止运作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060341211V#047F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341212V#043F而且出现在塔顶的结界是什么，\n',
            '我们现在也仍然不得而知……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070341213V#063F问题是它为何会\n',
            '笼罩在塔顶上呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050341214V#053F算了，以后再操心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341215V#050F总之现在只能\n',
            '赶紧前往下一座塔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341216V#1015F#6P嗯……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341217V#1002F尤莉亚小姐。\n',
            '有来自其它的塔的后续情报吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100341218V#176F#5P嗯嗯……\n',
            '这次是『绀碧之塔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100341219V#178F据说出现在那里的是一位\n',
            '能响起铃音的黑衣女子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341220V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0101, 2)
    Sleep(50)

    SetChrSubChip(0x0011, 1)
    Sleep(50)

    SetChrSubChip(0x000A, 1)
    Sleep(50)

    SetChrSubChip(0x0010, 0)
    Sleep(50)

    SetChrSubChip(0x0012, 0)
    Sleep(50)

    SetChrSubChip(0x0102, 2)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020341221V#1043F#5P『幻惑之铃』露茜奥拉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341222V#1042F#5P我记得她是\n',
            '雪拉姐认识的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030341223V#026F#6P是啊，是老朋友呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341224V#524F接下来似乎该我出场了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341225V#1026F#5P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030341226V#021F#6P不要摆出那副表情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341227V#020F姐姐是姐姐，\n',
            '我是我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341228V我只是去完成\n',
            '身为游击士的使命而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/R2200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x51AF
@scena.Code('func_0F_51AF')
def func_0F_51AF():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(950, 0, 51430, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(67000, 0)
    OP_6E(291, 0)
    OP_77(0xCC, 0x84, 0x55, 0x00, 0x00000000)
    OP_6D(2220, 100, 52500, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x0013, 1060, 150, 53910, 180)
    SetChrPos(0x000C, 2250, 0, 54450, 180)
    SetChrPos(0x0016, -1140, 100, 52380, 90)
    SetChrPos(0x0017, -1140, 100, 51220, 90)
    SetChrPos(0x0008, -1140, 100, 49960, 90)
    SetChrPos(0x000B, -1190, 100, 48660, 90)
    SetChrPos(0x000A, 2950, 200, 52400, 270)
    SetChrPos(0x0011, 2950, 200, 51200, 270)
    SetChrPos(0x0010, 2950, 200, 49840, 270)
    SetChrPos(0x0012, 2950, 200, 48620, 270)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0016, 0x0004)
    SetChrFlags(0x0017, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    OP_4A(0x0010, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x0012, 255)
    SetChrChipByIndex(0x0016, 19)
    SetChrSubChip(0x0016, 1)
    SetChrChipByIndex(0x0008, 20)
    SetChrSubChip(0x0008, 1)
    SetChrChipByIndex(0x000A, 22)
    SetChrSubChip(0x000A, 2)
    SetChrChipByIndex(0x000B, 23)
    SetChrSubChip(0x000B, 1)
    SetChrChipByIndex(0x0017, 26)
    SetChrSubChip(0x0017, 1)
    SetChrChipByIndex(0x0010, 27)
    SetChrSubChip(0x0010, 2)
    SetChrChipByIndex(0x0011, 28)
    SetChrSubChip(0x0011, 2)
    SetChrChipByIndex(0x0012, 29)
    SetChrSubChip(0x0012, 2)
    SetChrChipByIndex(0x0013, 30)
    SetChrSubChip(0x0013, 0)
    OP_72(0x000B, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0540350072V#100F#5P──这是试制品\n',
            '『零力场发生器』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350073V#1004F#6P零力场……发生器？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350074V#104F#5P简单地说，\n',
            '『福音』能够产生\n',
            '特殊的波长的导力场……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350075V#100F而这种回路就是用来制造出\n',
            '与其产生的共振相互抵消的力场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350076V#1019F#6P听起来\n',
            '一点都不简单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0020350077V#1044F#6P难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350078V这种回路可以防止\n',
            '『导力停止现象』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000C, 0x0013, 400)

    ChrTalk(
        0x0016,
        (
            '#0010350079V#1004F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100350080V#173F#5P真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350081V#104F#5P嗯……是这样没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350082V#102F说到底，所谓『导力停止现象』\n',
            '就是导力器的导力\n',
            '通过『福音』被吸收的现象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350083V至于『吸往何处』一直都是个谜，\n',
            '不过到这个地步总算是明朗起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060350084V#043F#2P是因为那座浮游都市……\n',
            '『辉之环』，对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350085V#100F#5P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350086V#104F『辉之环』是从异次元\n',
            '通过『福音』这个小缺口\n',
            '引起了『导力停止现象』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350087V由于那个缺口太过狭小，\n',
            '所以只在小范围内造成了影响……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350088V但随着『辉之环』被解放出来，\n',
            '影响范围一口气扩大了许多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350089V#102F甚至扩大到\n',
            '席卷整个王国的程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350090V#1026F#6P整个王国……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0020350091V#1042F#6P这就是这次的现象吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350092V#104F#5P嗯，王国境内\n',
            '所有的导力器\n',
            '恐怕都无法运作了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350093V#100F但是，这个『零力场发生器』\n',
            '具有防止『环』的干涉的作用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350094V#101F──换句话说，\n',
            '在它这边的导力器\n',
            '可以正常地运作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070350095V#560F#2P哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350096V#1008F#6P太、太厉害了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050350097V#051F#2P哦，意思是只要用这个\n',
            '就万事ＯＫ了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350098V#102F#5P不……\n',
            '还没好用到那个程度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350099V#104F首先，这只是试制品，\n',
            '能保护的对象是有限制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350100V最多只能保护大小约为\n',
            '双手可以拿住的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070350101V#065F#2P双手可以拿住的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050350102V#555F#2P嗯，这么一来\n',
            '的确相当受限制啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350103V#102F#5P第二……\n',
            '数量是有限的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350104V虽说是受了卡西乌斯之托，\n',
            '但是也只做成了１６个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350105V#1015F#6P１６个……\n',
            '我觉得已经相当多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350106V#1004F这么说，是老爸拜托你的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350107V#100F#5P嗯……\n',
            '不久前他来过我这里，\n',
            '拜托我开发这个东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350108V#104F当时我根本没想到\n',
            '会出这样的大乱子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350109V#1016F#6P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080350110V#070F#6P不愧是大人。\n',
            '原来早已预料到了一切啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180350111V#1065F可是这么一来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180350112V#1060F这１６个要怎么运用，\n',
            '大致上都已经决定好了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350113V#103F#5P喔……\n',
            '你的观察力真是敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    SetChrSubChip(0x0016, 0)
    Sleep(75)

    SetChrSubChip(0x0016, 2)
    Sleep(300)

    ChrTalk(
        0x0016,
        (
            '#0010350114V#1004F#5P咦、咦，这话怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180350115V#1063F#2P在混乱当中最重要的，\n',
            '就是必须迅速获得正确的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180350116V无论是结社的那些家伙现身，\n',
            '还是运送必需品等等…\n',
            '都必须要先确保情报的准确传达。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180350117V#1062F也就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    SetChrSubChip(0x0017, 0)
    Sleep(75)

    SetChrSubChip(0x0017, 2)
    Sleep(300)

    ChrTalk(
        0x0017,
        (
            '#0020350118V#1035F#5P要把它们用在\n',
            '恢复各地的通信设置上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350119V#1040F是这样没有错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180350120V#1061F#2P答对⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350121V#1006F#5P是啊，的确如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 180, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100350122V#176F#5P对军队来说，导力枪和飞船\n',
            '无法使用纵然是相当致命的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100350123V#178F但司令部与各部队之间\n',
            '联系中断的后果则更为严重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100350124V特别是王城、哈肯大门、\n',
            '雷斯顿要塞之间的联络\n',
            '必须要尽快恢复才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    SetChrSubChip(0x0016, 0)
    Sleep(75)

    SetChrSubChip(0x0016, 1)
    Sleep(50)

    SetChrSubChip(0x0017, 0)
    Sleep(75)

    SetChrSubChip(0x0017, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0030350125V#026F#6P协会也是一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350126V#020F如果支部之间不能够取得联系，\n',
            '那么无论发生什么都无法采取应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540350127V#104F#5P嗯，看来大家都没有异议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0013, 1)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0540350128V#100F#6P那么尤莉亚上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350129V请把这１０个『零力场发生器』\n',
            '交给王国军吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350130V#101F只要有这些的话，埃尔赛尤号、\n',
            '王都、雷斯顿要塞、哈肯大门，\n',
            '以及各地关所都能保护到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0013, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100350131V#171F#5P……不胜感激。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100350132V我会马上派传令兵\n',
            '将它们安排送往各地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    SetChrSubChip(0x0013, 0)
    Sleep(75)

    SetChrSubChip(0x0013, 2)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0540350133V#100F#5P接下来，交给游击士协会\n',
            '６个『零力场发生器』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540350134V应该能够恢复\n',
            '各地协会的通讯器才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0010350135V#1006F#6P嗯……明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0020350136V#1040F#6P一定保证安全送达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F6)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x63CF
@scena.Code('func_10_63CF')
def func_10_63CF():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    OP_D2(0x00270003, 0x00270007, 0x13)
    OP_D2(0x00270013, 0x00270017, 0x14)
    OP_D2(0x00070023, 0x0007002B, 0x15)
    OP_D2(0x00070033, 0x0007003B, 0x16)
    OP_D2(0x0027039B, 0x0027039F, 0x17)
    OP_D2(0x00070053, 0x0007005B, 0x18)
    OP_D2(0x00070063, 0x0007006B, 0x19)
    OP_D2(0x00070073, 0x0007007B, 0x1A)
    OP_D2(0x00270083, 0x00270087, 0x1B)
    OP_D2(0x0007046C, 0x00070470, 0x1C)
    OP_D2(0x002703E0, 0x002703E5, 0x1D)
    OP_D2(0x0007047B, 0x0007047F, 0x1E)
    SetChrChipByIndex(0x0101, 19)
    SetChrChipByIndex(0x0102, 20)
    SetChrChipByIndex(0x0008, 21)
    SetChrChipByIndex(0x0009, 22)
    SetChrChipByIndex(0x000A, 23)
    SetChrChipByIndex(0x0010, 24)
    SetChrChipByIndex(0x0011, 25)
    SetChrChipByIndex(0x000B, 26)
    SetChrChipByIndex(0x0012, 27)
    SetChrChipByIndex(0x0013, 28)
    SetChrChipByIndex(0x0018, 29)
    SetChrChipByIndex(0x000C, 30)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x0018, 0x0004)
    OP_6D(2570, 100, 51210, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x000C, 1060, 200, 53910, 180)
    SetChrPos(0x000A, 2950, 200, 52420, 270)
    SetChrPos(0x0009, 2950, 200, 51220, 270)
    SetChrPos(0x0018, 2950, 300, 49990, 270)
    SetChrPos(0x0013, 2950, 200, 48730, 270)
    SetChrPos(0x0011, 2950, 200, 47540, 270)
    SetChrPos(0x0012, 2950, 200, 46360, 270)
    SetChrPos(0x0101, -1100, 100, 52380, 90)
    SetChrPos(0x0102, -1100, 100, 51220, 90)
    SetChrPos(0x0008, -1100, 100, 49960, 90)
    SetChrPos(0x0010, -1100, 100, 48660, 90)
    SetChrPos(0x000B, -1100, 100, 47570, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    OP_4A(0x0010, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x000B, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0540390186V#104F#2P──埃尔赛尤号的损伤\n',
            '并不算特别严重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390187V导力引擎几乎没有受到任何损害，\n',
            '反重力产生机关也只有轻微损伤。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390188V#102F可是，包括稳定装置在内\n',
            '的小型导力系统出了些问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390189V在这种状态下\n',
            '是无法正常浮上空中的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390190V#178F#5P是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0110390191V#272F#2P总之现在只有调集人手\n',
            '赶紧展开修理作业了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390192V#277F在下虽然驽钝，\n',
            '但也请允许我献上微薄之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390193V#176F#5P……不胜感激。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390194V#035F#2P就算埃尔赛尤号的问题可以解决，\n',
            '目前最大的问题还是存在于\n',
            '这个都市某处的『辉之环』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390195V#030F看来『结社』似乎\n',
            '正在一步步地进行准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000A, 1)
    Sleep(200)

    ChrTalk(
        0x000A,
        (
            '#0060390196V#1163F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390197V如果让『辉之环』落在他们手中\n',
            '无法想象事态会演变成什么样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390198V#025F#6P嗯，无论如何\n',
            '都不会有什么好事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390199V#022F我们只有从迄今为止发生的事来判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050390200V#555F#6P哎……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390201V看来马上采取\n',
            '行动会比较妥当吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080390202V#074F#6P但如果莽撞行动的话，\n',
            '反而有可能会导致更加混乱的结果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390203V#070F还是应该\n',
            '组织探索队才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390204V#1015F#6P的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390205V#1007F如果不先确保移动路线，\n',
            '接下来也无法寻找『辉之环』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390206V#1043F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x0101, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010390207V#1004F#5P怎么了、约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390208V#1035F#6P不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390209V#1042F──总而言之，我认为\n',
            '探索队也需要有后备人员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390210V返回埃尔赛尤号之后\n',
            '如果能马上轮替的话，\n',
            '那就再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390211V#176F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390212V<FIXME>私も探索に加わりたいところだが、\n',
            '今はアルセイユの修理が急務だ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390213V#178F我们尽快来商量一下\n',
            '各自的任务分工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    EquipCmd(ChrTable['科洛丝'], ItemTable['天琴'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['科洛丝'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    OP_37(0x04, 0x80, 0x02)
    EquipCmd(ChrTable['科洛丝'], ItemTable['ＨＰ４'], 0x00)
    EquipCmd(ChrTable['科洛丝'], ItemTable['精神３'], 0x01)
    EquipCmd(ChrTable['科洛丝'], ItemTable['ＥＰ３'], 0x02)
    EquipCmd(ChrTable['科洛丝'], ItemTable['省ＥＰ３'], 0x04)
    EquipCmd(ChrTable['科洛丝'], ItemTable['魔防３'], 0x05)
    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['幻影Ⅱ'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['树脂装甲'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['斯托雷加Ｇ'], 0xFF)
    OP_37(0x03, 0x80, 0x02)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['ＥＰ４'], 0x00)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['命中３'], 0x01)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['防御３'], 0x02)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['攻击３'], 0x03)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['回避３'], 0x04)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['移动３'], 0x05)
    SetChrStatus(ChrTable['凯文神父'], 0xFE, 0)
    EquipCmd(ChrTable['凯文神父'], ItemTable['导力弩'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['树脂装甲'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['斯托雷加Ｇ'], 0xFF)
    OP_37(0x08, 0x80, 0x02)
    OP_37(0x08, 0x81, 0x02)
    OP_37(0x08, 0x82, 0x02)
    OP_37(0x08, 0x83, 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['行动力３'], 0x00)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＥＰ３'], 0x01)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＨＰ４'], 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['精神４'], 0x03)
    EquipCmd(ChrTable['凯文神父'], ItemTable['防御３'], 0x04)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
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
        'loc_6DC4',
    )

    Call(0, 0x001D)

    def _loc_6DC4(): pass

    label('loc_6DC4')

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
            0x0004,
            0x0003,
            0x0006,
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
    Sleep(1000)

    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000C, 2)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0101, -1100, 100, 52380, 90)
    SetChrPos(0x0102, -1100, 100, 51220, 90)
    SetChrChipByIndex(0x0101, 19)
    SetChrChipByIndex(0x0102, 20)
    OP_6D(2570, 100, 51210, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100390214V#170F#5P那么请艾丝蒂尔等\n',
            '四名成员负责进行搜索的任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390215V由于不知道会发生什么事，\n',
            '请各位千万不要勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390216V#1006F#6P没问题，别担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390217V#1040F#6P我们会优先确保\n',
            '移动路线的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390218V#176F#5P拜托你们了。',
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
            '#0100390219V#178F#5P剩下的人在此待命\n',
            '请你们一起帮忙修理船体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_708C',
    )

    ChrTalk(
        0x0011,
        (
            '#0070390220V#560F#2P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70FB')

    def _loc_708C(): pass

    label('loc_708C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_70C8',
    )

    ChrTalk(
        0x0010,
        (
            '#0050390221V#051F#6P嗯，放心交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70FB')

    def _loc_70C8(): pass

    label('loc_70C8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_70FB',
    )

    ChrTalk(
        0x000B,
        (
            '#0080390222V#070F#6P啊，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70FB(): pass

    label('loc_70FB')

    ChrTalk(
        0x0013,
        (
            '#0540390223V#103F#2P……好了，那我们走了。\n',
            '顺便告诉大家一个好消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390224V#100F在浮游都市上面似乎\n',
            '并不会出现『导力停止现象』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390225V即使离开了埃尔赛尤号之后，\n',
            '战术导力器也应该可以使用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0018, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x0011, 2)
    SetChrSubChip(0x0101, 2)
    Sleep(50)

    SetChrSubChip(0x0102, 2)
    SetChrSubChip(0x0018, 1)
    Sleep(50)

    SetChrSubChip(0x0009, 1)
    Sleep(50)

    SetChrSubChip(0x0012, 2)
    Sleep(50)

    SetChrSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010390226V#1004F#5P真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070390227V#064F#4P你、你是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0540390228V#104F#2P其实，那个『零力场发生器』\n',
            '已经在迫降的冲击当中坏掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390229V#102F尽管如此，我们仍然可以\n',
            '让舰内的装置正常运作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390230V看来凯文神父的推测\n',
            '大概是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180390231V#1065F#4P『环』具有着排除\n',
            '外界异物的功能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390232V#1060F也就是只要在都市里，\n',
            '导力器就不会被\n',
            '判定为异物了对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0013, 1)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0540390233V#101F#5P嗯，就是这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390234V#1007F#5P呼～太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390235V#1008F毕竟在搜索的时候\n',
            '没有魔法的话会很困难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390236V#1040F#5P那么，舰内的\n',
            '工房设施也可以使用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0013, 0)
    Sleep(200)

    ChrTalk(
        0x0013,
        (
            '#0540390237V#100F#2P嗯，那个也没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390238V#101F导力器还可进行后续的改造，\n',
            '有空的话就过来一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390239V#1006F#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390240V#1040F#5P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['约修亚'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['提妲'], 0xFE, 0)
    SetChrStatus(ChrTable['金'], 0xFE, 0)
    SetChrStatus(ChrTable['凯文神父'], 0xFE, 0)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0010, 0x0004)
    ClearChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x000A, 0x0004)
    ClearChrFlags(0x0011, 0x0004)
    ClearChrFlags(0x0012, 0x0004)
    ClearChrFlags(0x0013, 0x0004)
    ClearChrFlags(0x000C, 0x0004)
    ClearChrFlags(0x0018, 0x0004)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0008, 0)
    SetChrChipByIndex(0x0009, 1)
    SetChrChipByIndex(0x000A, 36)
    SetChrChipByIndex(0x0010, 8)
    SetChrChipByIndex(0x0011, 9)
    SetChrChipByIndex(0x000B, 3)
    SetChrChipByIndex(0x0012, 12)
    SetChrChipByIndex(0x0013, 13)
    SetChrChipByIndex(0x0018, 18)
    SetChrChipByIndex(0x000C, 4)
    OP_6D(1490, 0, 2300, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_72(0x0007, 0x0010)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 0x0000000F)
    OP_73(0x0007)
    CreateThread(0x0013, 0x01, 0x00, 0x0011)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77DE',
    )

    Sleep(800)

    CreateThread(0x0011, 0x01, 0x00, 0x0011)

    def _loc_77DE(): pass

    label('loc_77DE')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77F7',
    )

    Sleep(800)

    CreateThread(0x0010, 0x01, 0x00, 0x0011)

    def _loc_77F7(): pass

    label('loc_77F7')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7810',
    )

    Sleep(800)

    CreateThread(0x0008, 0x01, 0x00, 0x0011)

    def _loc_7810(): pass

    label('loc_7810')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7829',
    )

    Sleep(800)

    CreateThread(0x000B, 0x01, 0x00, 0x0011)

    def _loc_7829(): pass

    label('loc_7829')

    Sleep(800)

    CreateThread(0x000C, 0x01, 0x00, 0x0012)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_784E',
    )

    Sleep(800)

    CreateThread(0x000A, 0x01, 0x00, 0x0012)

    def _loc_784E(): pass

    label('loc_784E')

    Sleep(800)

    CreateThread(0x0018, 0x01, 0x00, 0x0012)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7873',
    )

    Sleep(800)

    CreateThread(0x0009, 0x01, 0x00, 0x0012)

    def _loc_7873(): pass

    label('loc_7873')

    Sleep(2000)

    @scena.Lambda('lambda_787E')
    def lambda_787E():
        OP_6D(1700, 0, 810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_787E)

    @scena.Lambda('lambda_7896')
    def lambda_7896():
        OP_6B(2690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7896)

    CreateThread(0x0101, 0x01, 0x00, 0x0013)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, 0x0014)

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8004',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7904',
    )

    Sleep(800)

    CreateThread(0x0109, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x0016)
    Sleep(1500)

    OP_71(0x0007, 0x0010)
    OP_6F(0x0007, 15)
    OP_70(0x0007, 0x00000000)
    OP_73(0x0007)

    Jump('loc_7944')

    def _loc_7904(): pass

    label('loc_7904')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7944',
    )

    Sleep(800)

    CreateThread(0x0109, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, 0x0016)
    Sleep(1500)

    OP_71(0x0006, 0x0010)
    OP_6F(0x0007, 15)
    OP_70(0x0007, 0x00000000)
    OP_73(0x0007)

    def _loc_7944(): pass

    label('loc_7944')

    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010390241V#1015F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390242V我们现在赶紧到\n',
            '舰外展开搜索活动吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_79DE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390243V#1382F#5P嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF0')

    def _loc_79DE(): pass

    label('loc_79DE')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A13',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390244V#020F#5P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF0')

    def _loc_7A13(): pass

    label('loc_7A13')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A4E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390245V#035F#5P嗯，就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF0')

    def _loc_7A4E(): pass

    label('loc_7A4E')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A83',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390246V#051F#5P啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF0')

    def _loc_7A83(): pass

    label('loc_7A83')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AB8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390247V#560F#5P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AF0')

    def _loc_7AB8(): pass

    label('loc_7AB8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7AF0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390248V#070F#5P啊，要出发了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AF0(): pass

    label('loc_7AF0')

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020390249V#1035F#5P……抱歉，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390250V#1040F我许多装备都用完了，\n',
            '必须先去进行补充才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390251V可以稍微等我一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010390252V#1004F#6P哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180390253V#1062F#6P嗯嗯，既然如此\n',
            '我也得准备一下，一起去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390254V#1061F艾丝蒂尔你们就在\n',
            '那边的休息室等我们好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010390255V#1006F这样啊……我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CB3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390256V#1168F#5P那我们在这里等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DEC')

    def _loc_7CB3(): pass

    label('loc_7CB3')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CF4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390257V#021F#5P那么我们就在这里等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DEC')

    def _loc_7CF4(): pass

    label('loc_7CF4')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D3A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390258V#035F#5P呵……\n',
            '那么就等你们回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DEC')

    def _loc_7D3A(): pass

    label('loc_7D3A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D75',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390259V#051F#5P赶快弄好回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DEC')

    def _loc_7D75(): pass

    label('loc_7D75')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DB4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390260V#061F#5P那么，等你们回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DEC')

    def _loc_7DB4(): pass

    label('loc_7DB4')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DEC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390261V#071F#5P那么就等你们啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DEC(): pass

    label('loc_7DEC')

    CreateThread(0x0101, 0x01, 0x00, 0x0018)

    @scena.Lambda('lambda_7DF9')
    def lambda_7DF9():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_7DF9')

    DispatchAsync2(0x0102, 0x0001, lambda_7DF9)

    Sleep(100)

    @scena.Lambda('lambda_7E0F')
    def lambda_7E0F():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_7E0F')

    DispatchAsync2(0x0109, 0x0001, lambda_7E0F)

    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E3B',
    )

    CreateThread(0x00F9, 0x01, 0x00, 0x001A)
    WaitForThreadExit(0x00F9, 0x0001)

    Jump('loc_7E54')

    def _loc_7E3B(): pass

    label('loc_7E3B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E54',
    )

    CreateThread(0x00F8, 0x01, 0x00, 0x001A)
    WaitForThreadExit(0x00F8, 0x0001)

    def _loc_7E54(): pass

    label('loc_7E54')

    Sleep(1500)

    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0109, 0x01)
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180390262V#1067F#5P真是的……\n',
            '你可真是罪孽深重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0109, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020390263V#1043F……对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0109,
        (
            '#0180390264V#1065F#6P要道歉的话\n',
            '就去对艾丝蒂尔说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390265V#1063F……这样真的可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390266V#1035F我已经决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390267V#1040F凯文神父……\n',
            '这件事情就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180390268V#1068F#6P真是的，不管你了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390269V#1060F好了，时间所剩不多，\n',
            '赶快来医务室吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8724')

    def _loc_8004(): pass

    label('loc_8004')

    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x0016)
    Sleep(1500)

    OP_71(0x0007, 0x0010)
    OP_6F(0x0007, 15)
    OP_70(0x0007, 0x00000000)
    OP_73(0x0007)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010390241V#1015F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390242V我们现在赶紧到\n',
            '舰外展开搜索活动吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_80CE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390272V#1382F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81D5')

    def _loc_80CE(): pass

    label('loc_80CE')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8100',
    )

    ChrTalk(
        0x0103,
        (
            '#0030260343V#020F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81D5')

    def _loc_8100(): pass

    label('loc_8100')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8138',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390274V#035F呼，就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81D5')

    def _loc_8138(): pass

    label('loc_8138')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_816C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390275V#051F啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81D5')

    def _loc_816C(): pass

    label('loc_816C')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_81A0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390276V#560F嗯，是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81D5')

    def _loc_81A0(): pass

    label('loc_81A0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_81D5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390277V#070F啊，就这样做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_81D5(): pass

    label('loc_81D5')

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020390249V#1035F#5P……真对不起，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390250V#1040F我许多装备都用完了，\n',
            '必须先去进行补充才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390251V可以稍微等我一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010390281V#1004F#6P哦，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390282V#1015F既然如此\n',
            '我也跟你一起去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390283V#1049F#5P不，那倒不必。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390284V#1040F大约过３０分钟就回来,\n',
            '你们可以在休息室等我回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390285V#1006F#6P这样啊……我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83AA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390286V#071F那我们在这儿等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D3')

    def _loc_83AA(): pass

    label('loc_83AA')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83E4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390287V#061F那么，等你回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D3')

    def _loc_83E4(): pass

    label('loc_83E4')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_841C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390288V#051F赶快弄好回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D3')

    def _loc_841C(): pass

    label('loc_841C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_845F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390289V#035F呼……\n',
            '那么就等你们回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D3')

    def _loc_845F(): pass

    label('loc_845F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_849B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390290V#021F那么我们在这里等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D3')

    def _loc_849B(): pass

    label('loc_849B')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84D3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390291V#1168F那我们在这里等你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84D3(): pass

    label('loc_84D3')

    CreateThread(0x0101, 0x01, 0x00, 0x0018)

    @scena.Lambda('lambda_84E0')
    def lambda_84E0():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_84E0')

    DispatchAsync2(0x0102, 0x0001, lambda_84E0)

    Sleep(1000)

    CreateThread(0x00F8, 0x01, 0x00, 0x0019)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x001A)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(1500)

    OP_4A(0x0012, 255)
    SetChrPos(0x0012, 1020, 0, 5300, 180)
    OP_72(0x0007, 0x0010)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 0x0000000F)
    OP_73(0x0007)
    Sleep(500)

    NpcTalk(
        0x0012,
        '青年的声音',
        (
            '#0180390292V#4P哎呀呀……\n',
            '你可真是罪孽深重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8582')
    def lambda_8582():
        OP_6D(2490, 0, 1310, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8582)

    CreateThread(0x0012, 0x01, 0x00, 0x0017)

    @scena.Lambda('lambda_85A1')
    def lambda_85A1():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_85A1')

    DispatchAsync2(0x0102, 0x0001, lambda_85A1)

    Sleep(1500)

    OP_72(0x0007, 0x0010)
    OP_6F(0x0007, 15)
    OP_70(0x0007, 0x00000000)
    OP_73(0x0007)
    WaitForThreadExit(0x0012, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0102, 0x01)

    ChrTalk(
        0x0102,
        (
            '#0020390293V#1043F#6P……对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180390294V#1065F#5P要道歉的话\n',
            '就去对艾丝蒂尔说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390265V#1063F……这样真的可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390296V#1035F#6P我已经决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390267V#1040F凯文神父……\n',
            '这件事情就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0180390298V#1068F#5P真是的，不管你了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390269V#1060F好了，时间所剩不多，\n',
            '赶快来医务室吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8724(): pass

    label('loc_8724')

    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    OP_6D(-1470, 0, -49280, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_87EB'),
        (0x00000003, 'loc_87F8'),
        (0x00000004, 'loc_8805'),
        (0x00000005, 'loc_8812'),
        (0x00000006, 'loc_881F'),
        (0x00000007, 'loc_882C'),
        (-1, 'loc_8839'),
    )

    def _loc_87EB(): pass

    label('loc_87EB')

    OP_D2(0x00070023, 0x0007002B, 0x14)

    Jump('loc_8839')

    def _loc_87F8(): pass

    label('loc_87F8')

    OP_D2(0x00070033, 0x0007003B, 0x14)

    Jump('loc_8839')

    def _loc_8805(): pass

    label('loc_8805')

    OP_D2(0x0027039B, 0x0027039F, 0x14)

    Jump('loc_8839')

    def _loc_8812(): pass

    label('loc_8812')

    OP_D2(0x00070053, 0x0007005B, 0x14)

    Jump('loc_8839')

    def _loc_881F(): pass

    label('loc_881F')

    OP_D2(0x00070063, 0x0007006B, 0x14)

    Jump('loc_8839')

    def _loc_882C(): pass

    label('loc_882C')

    OP_D2(0x00070073, 0x0007007B, 0x14)

    Jump('loc_8839')

    def _loc_8839(): pass

    label('loc_8839')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_885A'),
        (0x00000003, 'loc_8867'),
        (0x00000004, 'loc_8874'),
        (0x00000005, 'loc_8881'),
        (0x00000006, 'loc_888E'),
        (0x00000007, 'loc_889B'),
        (-1, 'loc_88A8'),
    )

    def _loc_885A(): pass

    label('loc_885A')

    OP_D2(0x00070023, 0x0007002B, 0x15)

    Jump('loc_88A8')

    def _loc_8867(): pass

    label('loc_8867')

    OP_D2(0x00070033, 0x0007003B, 0x15)

    Jump('loc_88A8')

    def _loc_8874(): pass

    label('loc_8874')

    OP_D2(0x0027039B, 0x0027039F, 0x15)

    Jump('loc_88A8')

    def _loc_8881(): pass

    label('loc_8881')

    OP_D2(0x00070053, 0x0007005B, 0x15)

    Jump('loc_88A8')

    def _loc_888E(): pass

    label('loc_888E')

    OP_D2(0x00070063, 0x0007006B, 0x15)

    Jump('loc_88A8')

    def _loc_889B(): pass

    label('loc_889B')

    OP_D2(0x00070073, 0x0007007B, 0x15)

    Jump('loc_88A8')

    def _loc_88A8(): pass

    label('loc_88A8')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8916',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88E6',
    )

    SetChrFlags(0x00F8, 0x0004)
    SetChrChipByIndex(0x00F9, 21)
    SetChrPos(0x00F9, -2400, 200, -47940, 180)
    ClearChrFlags(0x00F9, 0x0080)

    Jump('loc_8913')

    def _loc_88E6(): pass

    label('loc_88E6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8913',
    )

    SetChrFlags(0x00F8, 0x0004)
    SetChrChipByIndex(0x00F8, 20)
    SetChrPos(0x00F8, -2400, 200, -47940, 180)
    ClearChrFlags(0x00F8, 0x0080)

    def _loc_8913(): pass

    label('loc_8913')

    Jump('loc_8956')

    def _loc_8916(): pass

    label('loc_8916')

    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    SetChrChipByIndex(0x00F8, 20)
    SetChrChipByIndex(0x00F9, 21)
    SetChrPos(0x00F8, -450, 200, -50200, 0)
    SetChrPos(0x00F9, -2400, 200, -47940, 180)
    ClearChrFlags(0x00F8, 0x0080)
    ClearChrFlags(0x00F9, 0x0080)
    def _loc_8956(): pass

    label('loc_8956')

    SetChrFlags(0x0101, 0x0004)
    SetChrChipByIndex(0x0101, 19)
    SetChrPos(0x0101, -2400, 200, -50200, 0)
    ClearChrFlags(0x0101, 0x0080)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C2E',
    )

    OP_22(0x006D, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89BC',
    )

    SetChrSubChip(0x00F9, 1)
    Sleep(100)

    SetChrSubChip(0x0101, 2)

    Jump('loc_89D8')

    def _loc_89BC(): pass

    label('loc_89BC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89D8',
    )

    SetChrSubChip(0x00F8, 1)
    Sleep(100)

    SetChrSubChip(0x0101, 2)

    def _loc_89D8(): pass

    label('loc_89D8')

    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x001B)
    Sleep(800)

    CreateThread(0x0109, 0x01, 0x00, 0x001C)

    @scena.Lambda('lambda_89F6')
    def lambda_89F6():
        OP_6D(-800, 200, -47820, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_89F6)

    WaitForThreadExit(0x0109, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010390300V#1004F#6P啊，约修亚、凯文神父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390301V#1040F#5P……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180390302V#1061F#5P啊，真不好意思。\n',
            '回来得晚了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390303V#1015F#6P这个倒无所谓……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390304V……只是你们两个，\n',
            '怎么都看上去满脸倦容啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180390305V#1064F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390306V#1035F#5P细部装备的补充\n',
            '耗费了相当多的工夫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390307V#1040F没关系，不妨碍搜索活动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180390308V#1066F#5P对、对对对！\n',
            '肯定会相当有帮助的～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390309V#1025F#6P那我就放心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390310V#1006F好～的。\n',
            '那么就出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DFF')

    def _loc_8C2E(): pass

    label('loc_8C2E')

    OP_22(0x006D, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x00F9, 1)
    Sleep(100)

    SetChrSubChip(0x0101, 2)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x001B)

    @scena.Lambda('lambda_8C59')
    def lambda_8C59():
        OP_6D(-540, 0, -48040, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8C59)

    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010390311V#1004F#6P啊、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390312V#1040F#5P……久等了。\n',
            '似乎稍微有点迟到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390303V#1015F#6P这个倒无所谓……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390314V……不过约修亚\n',
            '怎么都看上去满脸倦容啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390306V#1035F#5P细部装备的补充\n',
            '耗费了相当多的工夫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390316V#1040F不要紧。\n',
            '不会妨碍搜索活动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390309V#1025F#6P那我就放心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390310V#1006F好～的。\n',
            '那么就出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8DFF(): pass

    label('loc_8DFF')

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0000, 0x0004)
    ClearChrFlags(0x0001, 0x0004)
    ClearChrFlags(0x0002, 0x0004)
    ClearChrFlags(0x0003, 0x0004)
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    OP_6D(30, 0, -44840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 30, 0, -44840, 0)
    SetChrPos(0x0001, 30, 0, -44840, 0)
    SetChrPos(0x0002, 30, 0, -44840, 0)
    SetChrPos(0x0003, 30, 0, -44840, 0)
    Sleep(500)

    OP_71(0x0007, 0x0010)
    OP_A2(0x2201)
    OP_28(0x009C, 0x01, 0x0040)
    OP_28(0x009D, 0x04, 0x02)
    OP_28(0x009D, 0x04, 0x08)
    OP_28(0x009D, 0x01, 0x0001)
    OP_28(0x009D, 0x01, 0x0002)
    OP_28(0x009D, 0x01, 0x0004)
    OP_28(0x009D, 0x01, 0x0008)
    OP_C4(0x01, 0x00000008)
    OP_A2(0x1E0B)
    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0011 offset: 0x8F16
@scena.Code('func_11_8F16')
def func_11_8F16():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 1020, 0, 2150, 2000, 0x00)
    OP_8E(0x00FE, 5140, 0, 2150, 2000, 0x00)
    OP_8E(0x00FE, 5140, -1950, -1100, 2000, 0x00)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000000C8)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x8F79
@scena.Code('func_12_8F79')
def func_12_8F79():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 970, 0, 1840, 2000, 0x00)
    OP_8E(0x00FE, -880, 0, -100, 2000, 0x00)
    OP_8E(0x00FE, -3040, 0, 70, 2000, 0x00)

    @scena.Lambda('lambda_8FD1')
    def lambda_8FD1():
        OP_8E(0x00FE, -3110, 2400, 3400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_8FD1)

    Sleep(1800)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x8FFC
@scena.Code('func_13_8FFC')
def func_13_8FFC():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 930, 0, -910, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x902E
@scena.Code('func_14_902E')
def func_14_902E():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 1170, 0, 1480, 2000, 0x00)
    OP_8E(0x00FE, 2080, 0, 340, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0015 offset: 0x9074
@scena.Code('func_15_9074')
def func_15_9074():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 1190, 0, 2280, 2000, 0x00)
    OP_8E(0x00FE, -70, 0, 210, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0016 offset: 0x90BA
@scena.Code('func_16_90BA')
def func_16_90BA():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 1020, 0, 1580, 2000, 0x00)

    Return()

# id: 0x0017 offset: 0x90E5
@scena.Code('func_17_90E5')
def func_17_90E5():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1020, 0, 5300, 180)
    OP_8E(0x00FE, 1510, 0, 1970, 2000, 0x00)

    Return()

# id: 0x0018 offset: 0x9110
@scena.Code('func_18_9110')
def func_18_9110():
    OP_8E(0x00FE, 1020, 0, -1590, 2000, 0x00)
    OP_22(0x006D, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_9134')
    def lambda_9134():
        OP_8E(0x00FE, 1020, 0, -3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_9134)

    Sleep(500)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x0000012C)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0019 offset: 0x915F
@scena.Code('func_19_915F')
def func_19_915F():
    OP_8E(0x00FE, 990, 50, -1230, 2000, 0x00)

    @scena.Lambda('lambda_9179')
    def lambda_9179():
        OP_8E(0x00FE, 1020, 0, -3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_9179)

    Sleep(900)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x0000012C)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001A offset: 0x91A4
@scena.Code('func_1A_91A4')
def func_1A_91A4():
    @scena.Lambda('lambda_91AA')
    def lambda_91AA():
        OP_8E(0x00FE, 1020, 0, -3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_91AA)

    Sleep(2000)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x0000012C)
    OP_22(0x006D, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x91DA
@scena.Code('func_1B_91DA')
def func_1B_91DA():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 490, 0, -39390, 180)
    OP_8E(0x00FE, 390, 0, -44640, 2000, 0x00)
    OP_8E(0x00FE, -580, 0, -46900, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x001C offset: 0x9220
@scena.Code('func_1C_9220')
def func_1C_9220():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 490, 0, -39390, 180)
    OP_8E(0x00FE, 390, 0, -44640, 2000, 0x00)
    OP_8E(0x00FE, 380, 0, -47360, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x001D offset: 0x9266
@scena.Code('func_1D_9266')
def func_1D_9266():
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
        (0x00000000, 'loc_92E0'),
        (0x00000001, 'loc_92E6'),
        (-1, 'loc_92EC'),
    )

    def _loc_92E0(): pass

    label('loc_92E0')

    OP_A2(0x1200)

    Jump('loc_92EC')

    def _loc_92E6(): pass

    label('loc_92E6')

    OP_A2(0x1201)

    Jump('loc_92EC')

    def _loc_92EC(): pass

    label('loc_92EC')

    Return()

# id: 0x001E offset: 0x92ED
@scena.Code('func_1E_92ED')
def func_1E_92ED():
    FadeOut(0, 0, -1)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x001F offset: 0x937C
@scena.Code('func_1F_937C')
def func_1F_937C():
    FadeOut(0, 0, -1)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0020 offset: 0x9409
@scena.Code('func_20_9409')
def func_20_9409():
    FadeOut(0, 0, -1)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
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

# id: 0x0021 offset: 0x949A
@scena.Code('func_21_949A')
def func_21_949A():
    OP_A2(0x000F)
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x49),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x49)

    Return()

# id: 0x0022 offset: 0x94B4
@scena.Code('func_22_94B4')
def func_22_94B4():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x3E)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
