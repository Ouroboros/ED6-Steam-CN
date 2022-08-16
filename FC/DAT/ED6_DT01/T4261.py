import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4261_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4261   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4261.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02623._CH', 'ED6_DT07/CH02623P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02033._CH', 'ED6_DT07/CH02033P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20133._CH', 'ED6_DT06/CH20133P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
    ]

# id: 0x10001 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '雷沃尔',
            x                   = 141250,
            z                   = 0,
            y                   = 7610,
            direction           = 278,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '妮舒',
            x                   = 78740,
            z                   = 0,
            y                   = -1880,
            direction           = 194,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 83700,
            z                   = 300,
            y                   = -52940,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '拉赛尔',
            x                   = 90160,
            z                   = 0,
            y                   = -56780,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458771,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524307,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589843,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655379,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 720915,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 786451,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '塔罗牌',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262163,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 86360,
            z                   = 200,
            y                   = -52990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 30310,
            z                   = 200,
            y                   = -53530,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 135100,
            z                   = 0,
            y                   = 9440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '玻璃杯',
            x                   = 134700,
            z                   = 700,
            y                   = 10040,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327699,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = 135400,
            z                   = 700,
            y                   = 10100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835032,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = 29400,
            z                   = 500,
            y                   = -53300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900568,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = 29400,
            z                   = 500,
            y                   = -53900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900568,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = 29000,
            z                   = 500,
            y                   = -53600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900568,
            chipIndex           = 24,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x472
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x472
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x472
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 139320,
            triggerZ            = 0,
            triggerY            = 7540,
            triggerRange        = 400,
            actorX              = 141250,
            actorZ              = 1500,
            actorY              = 7610,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x496
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_4A1',
    )

    Event(0, func_12_6751)

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_4B8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0D_2698)

    def _loc_4B8(): pass

    label('loc_4B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_4CF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_10_56CD)

    def _loc_4CF(): pass

    label('loc_4CF')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006A, 'loc_4DF'),
        (0x0000006C, 'loc_4F5'),
        (-1, 'loc_508'),
    )

    def _loc_4DF(): pass

    label('loc_4DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 5, 0x645)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F2',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 6, 0x646))
    Event(0, func_0F_3C50)

    def _loc_4F2(): pass

    label('loc_4F2')

    Jump('loc_508')

    def _loc_4F5(): pass

    label('loc_4F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_505',
    )

    Event(0, func_11_659A)

    def _loc_505(): pass

    label('loc_505')

    Jump('loc_508')

    def _loc_508(): pass

    label('loc_508')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_52A',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 38190, 200, -58050, 90)

    def _loc_52A(): pass

    label('loc_52A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_554',
    )

    ChrSetChipByIndex(0x0000, 2)
    ChrSetChipByIndex(0x0001, 3)
    ChrSetChipByIndex(0x0138, 4)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_638',
    )

    ChrClearFlags(0x000C, 0x0080)
    TerminateThread(0x000C, 0xFF)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetPos(0x000C, 30760, 200, 53020, 270)
    ChrSetPos(0x0017, 29800, 500, 53440, 0)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0012, 29750, 500, 53150, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0013, 29750, 500, 52650, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, 29300, 500, 53440, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0015, 29300, 500, 52920, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0016, 29300, 500, 52420, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x0019, 0x0080)

    Jump('loc_6F4')

    def _loc_638(): pass

    label('loc_638')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_65D',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 37840, 0, -58890, 90)

    Jump('loc_6F4')

    def _loc_65D(): pass

    label('loc_65D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_66C',
    )

    ChrSetFlags(0x000D, 0x0080)

    Jump('loc_6F4')

    def _loc_66C(): pass

    label('loc_66C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_69D',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetChipByIndex(0x0008, 16)
    CreateThread(0x0008, 0x00, 0x00, func_02_790)
    ChrSetPos(0x0008, 37860, 0, -59000, 90)
    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_6F4')

    def _loc_69D(): pass

    label('loc_69D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_6C9',
    )

    ChrSetChipByIndex(0x0008, 16)
    CreateThread(0x0008, 0x00, 0x00, func_02_790)
    ChrSetPos(0x0008, 37860, 0, -59000, 90)
    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_6F4')

    def _loc_6C9(): pass

    label('loc_6C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_6F4',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0008, 30330, 250, -53540, 270)

    def _loc_6F4(): pass

    label('loc_6F4')

    Return()

# id: 0x0001 offset: 0x6F5
@scena.Code('func_01_6F5')
def func_01_6F5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_711',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_12_6751)

    Jump('loc_739')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_729',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_739')

    def _loc_729(): pass

    label('loc_729')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_739',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_739(): pass

    label('loc_739')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_745',
    )

    OP_1B(0x00, 0x00, 0x0013)

    def _loc_745(): pass

    label('loc_745')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_74F',
    )

    Jump('loc_786')

    def _loc_74F(): pass

    label('loc_74F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_759',
    )

    Jump('loc_786')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_767',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_786')

    def _loc_767(): pass

    label('loc_767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_775',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_786')

    def _loc_775(): pass

    label('loc_775')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_77F',
    )

    Jump('loc_786')

    def _loc_77F(): pass

    label('loc_77F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_786',
    )

    def _loc_786(): pass

    label('loc_786')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x790
@scena.Code('func_02_790')
def func_02_790():
    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_8F7')

    def _loc_7B5(): pass

    label('loc_7B5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CE',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_8F7')

    def _loc_7CE(): pass

    label('loc_7CE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_8F7')

    def _loc_7E7(): pass

    label('loc_7E7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_800',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_8F7')

    def _loc_800(): pass

    label('loc_800')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_819',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_8F7')

    def _loc_819(): pass

    label('loc_819')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_832',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_8F7')

    def _loc_832(): pass

    label('loc_832')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_8F7')

    def _loc_84B(): pass

    label('loc_84B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_864',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_8F7')

    def _loc_864(): pass

    label('loc_864')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_8F7')

    def _loc_87D(): pass

    label('loc_87D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_896',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_8F7')

    def _loc_896(): pass

    label('loc_896')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8AF',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_8F7')

    def _loc_8AF(): pass

    label('loc_8AF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C8',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_8F7')

    def _loc_8C8(): pass

    label('loc_8C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_8F7')

    def _loc_8E1(): pass

    label('loc_8E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F7',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_8F7(): pass

    label('loc_8F7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_90C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_8F7')

    def _loc_90C(): pass

    label('loc_90C')

    Return()

# id: 0x0003 offset: 0x90D
@scena.Code('func_03_90D')
def func_03_90D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BE0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0010,
        (
            '#0540141261V#102F理查德上校使用的『福音』\n',
            '已经顺利回收了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540141262V等封印区域的调查结束了，\n',
            '回到蔡斯之后还得进行更彻底的相关调查。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141263V#007F嗯……确实让人很在意啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141264V#505F到最后还是没有弄清楚\n',
            '是谁制造了这个东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0540141265V#102F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540141266V只要能判定『福音』的真面目，\n',
            '那么在封印区域发生的事情\n',
            '所隐含的真正意义不也就清楚了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540141267V#101F嗯，充满干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141268V#006F充满干劲固然很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141269V不过还是要注意\n',
            '别在研究时被人绑架了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0540141270V#104F我知道了，\n',
            '以后我会小心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540141271V#100F顺便说一下，\n',
            '现在『福音』是由卡西乌斯那家伙保管的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540141272V没有比这更好的保管场所了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141273V#506F的确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5E')

    def _loc_BE0(): pass

    label('loc_BE0')

    ChrTalk(
        0x0010,
        (
            '#0540141274V#103F不过说起来，\n',
            '这个口琴的音色十分不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540141275V#101F呵呵，\n',
            '看来用导力器是无论如何也模仿不了的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5E(): pass

    label('loc_C5E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xC62
@scena.Code('func_04_C62')
def func_04_C62():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C87',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_CB8')

    def _loc_C87(): pass

    label('loc_C87')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C9D',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_CB8')

    def _loc_C9D(): pass

    label('loc_C9D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_CB3',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_CB8')

    def _loc_CB3(): pass

    label('loc_CB3')

    ChrSetSubChip(0x00FE, 1)

    def _loc_CB8(): pass

    label('loc_CB8')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E8A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000F,
        (
            '#0070141249V#560F好美的音色……\n',
            '是谁在吹呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141250V#501F啊，\n',
            '和提妲在一起的时候他没有吹过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141251V这是约修亚吹的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070141252V#064F约修亚哥哥！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070141253V#061F哇，\n',
            '原来哥哥他会吹口琴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070141254V吹得真好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141255V#006F嗯，还可以吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070141256V#067F我很笨，\n',
            '所以什么乐器都不会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070141257V我好羡慕他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141258V#506F（唔～如果说提妲都很笨，\n',
            '　那么我算是什么呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED8')

    def _loc_E8A(): pass

    label('loc_E8A')

    ChrTalk(
        0x000F,
        (
            '#0070141259V#061F原来约修亚哥哥会吹口琴啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070141254V吹得真好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ED8(): pass

    label('loc_ED8')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xEE1
@scena.Code('func_05_EE1')
def func_05_EE1():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F06',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_F37')

    def _loc_F06(): pass

    label('loc_F06')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F1C',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_F37')

    def _loc_F1C(): pass

    label('loc_F1C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F32',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_F37')

    def _loc_F32(): pass

    label('loc_F32')

    ChrSetSubChip(0x00FE, 2)

    def _loc_F37(): pass

    label('loc_F37')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1167',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0018,
        (
            '#0050141237V#053F这音色……\n',
            '怎么让人感觉如此怀念。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050141238V小的时候在村里好像听到过……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141239V#000F对了，\n',
            '阿加特是在拉文努村出生的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0050141240V#552F……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070141241V#061F嘿嘿，\n',
            '阿加特大哥哥在故乡有个妹妹呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070141242V是叫做米夏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0050141243V#055F喂、喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141244V#004F不会吧？\n',
            '你竟然还有妹妹！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0050141245V#551F你这是什么意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050141246V#552F的确，我很少回去看看，\n',
            '不是一个好哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050141247V#051F这次的事件总算解决了，\n',
            '隔了这么久，我也该回村里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B3')

    def _loc_1167(): pass

    label('loc_1167')

    ChrTalk(
        0x0018,
        (
            '#0050141247V#051F这次的事件总算解决了，\n',
            '隔了这么久，我也该回村里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B3(): pass

    label('loc_11B3')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x11BC
@scena.Code('func_06_11BC')
def func_06_11BC():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11E1',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_1212')

    def _loc_11E1(): pass

    label('loc_11E1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11F7',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_1212')

    def _loc_11F7(): pass

    label('loc_11F7')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_120D',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1212')

    def _loc_120D(): pass

    label('loc_120D')

    ChrSetSubChip(0x00FE, 2)

    def _loc_1212(): pass

    label('loc_1212')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1549',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0019,
        (
            '#0080141276V#070F哟，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080141277V卡西乌斯大人现在还在开会吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141278V#505F嗯，好像是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141279V凯诺娜上尉和洛伦斯少尉至今还没有抓到。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141280V军队指挥系统要重新改制，\n',
            '还有许许多多其他的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0080141281V#073F哦，我还说要请他喝酒，\n',
            '看来是不行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080141282V#075F不过，那个女的姑且不论，\n',
            '要想抓捕洛伦斯少尉，\n',
            '大人恐怕得费一番力气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080141283V我总觉得在武术大会上\n',
            '他根本没有用尽全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141284V#007F的确，第二次对决时，\n',
            '他的强大和之前简直就是天壤之别……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141285V#002F听说他原来是个猎兵，\n',
            '猎兵真的那么强吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0080141286V#072F是啊，\n',
            '身经百战的佣兵当然是很强的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080141287V而且那种强大远远不是\n',
            '这么简单就可以说清楚的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080141288V#074F修罗——\n',
            '这个词用在他身上是最合适的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141289V#003F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A4')

    def _loc_1549(): pass

    label('loc_1549')

    ChrTalk(
        0x0019,
        (
            '#0080141290V#070F话说回来，这首曲子很不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080141291V正好作为我晚上小酌的下酒菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A4(): pass

    label('loc_15A4')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x15AD
@scena.Code('func_07_15AD')
def func_07_15AD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1893',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x001A,
        (
            '#0040141292V#033F哦……\n',
            '这是约修亚君在演奏啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141293V#031F我当时在湖畔就听到过，\n',
            '的确不是一般的水准。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141294V应该经过了很久的练习吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141295V#006F的确，\n',
            '从很早以前他就一直在吹这首曲子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141296V虽然有时候也会吹其他的曲子，\n',
            '不过还是这首吹得最有感情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0040141297V#030F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141298V不过，据我对这首曲子的了解，\n',
            '约修亚君也确实是很厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141299V帝国的人姑且不论，就王国的人而言，\n',
            '知道这首曲子的人可谓寥寥无几。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141300V#004F哎……\n',
            '这是埃雷波尼亚的曲子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0040141301V#033F『星之所在』对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141302V#035F一首在帝国传唱了很久的曲子。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141303V帝都暂且不说，对于乡村的人们来说，\n',
            '至今都还非常的熟悉，一直都在流传着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141304V#505F哦～是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18FE')

    def _loc_1893(): pass

    label('loc_1893')

    ChrTalk(
        0x001A,
        (
            '#0040141305V#037F呵……\n',
            '不愧是约修亚君啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141306V婀娜多姿的旋律\n',
            '让我的心都在扑通扑通地跳动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18FE(): pass

    label('loc_18FE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1902
@scena.Code('func_08_1902')
def func_08_1902():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1927',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_1958')

    def _loc_1927(): pass

    label('loc_1927')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_193D',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_1958')

    def _loc_193D(): pass

    label('loc_193D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1953',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1958')

    def _loc_1953(): pass

    label('loc_1953')

    ChrSetSubChip(0x00FE, 2)

    def _loc_1958(): pass

    label('loc_1958')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A95',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000C,
        (
            '#0030141229V#021F哎呀，\n',
            '这不是约修亚的口琴声吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141230V从外面传来的声音来看，\n',
            '那孩子应该在空中庭园呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141231V#027F难得气氛这么好，\n',
            '现在就下定决心吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141232V#503F也、也许是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141233V#509F……不行！\n',
            '这次还没那个打算！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141234V#025F唉～遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF9')

    def _loc_1A95(): pass

    label('loc_1A95')

    ChrTalk(
        0x000C,
        (
            '#0030141235V#020F快呀快呀，去呀，\n',
            '快去空中庭园呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141236V这回只有你们两个，好好谈谈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF9(): pass

    label('loc_1AF9')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1B02
@scena.Code('func_09_1B02')
def func_09_1B02():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '这边是拉赛尔博士和\n',
            '提妲小姐的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1B39
@scena.Code('func_0A_1B39')
def func_0A_1B39():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x1B3E
@scena.Code('func_0B_1B3E')
def func_0B_1B3E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1B6D',
    )

    ChrTalk(
        0x000D,
        (
            '哟，今天怎么只有你一个人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D13')

    def _loc_1B6D(): pass

    label('loc_1B6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1C41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1BD2',
    )

    ChrTalk(
        0x000D,
        (
            '那位理查德上校竟然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我至今还认为\n',
            '他不应该是那种\n',
            '会反叛女王陛下的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3E')

    def _loc_1BD2(): pass

    label('loc_1BD2')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000D,
        (
            '理查德上校\n',
            '每晚都会到这里来\n',
            '向我打听一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '至今我还是觉得他不应该是\n',
            '会反叛女王陛下的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3E(): pass

    label('loc_1C3E')

    Jump('loc_1D13')

    def _loc_1C41(): pass

    label('loc_1C41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1C4B',
    )

    Jump('loc_1D13')

    def _loc_1C4B(): pass

    label('loc_1C4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1C55',
    )

    Jump('loc_1D13')

    def _loc_1C55(): pass

    label('loc_1C55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1CB9',
    )

    ChrTalk(
        0x000D,
        (
            '作为饭后的消遣，\n',
            '来一杯饮料如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '就算菜单上没有的种类\n',
            '也可以立刻调配出来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D13')

    def _loc_1CB9(): pass

    label('loc_1CB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1D13',
    )

    ChrTalk(
        0x000D,
        (
            '这里是谈话室。\n',
            '请在这里放松一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果客人\n',
            '需要酒水的话，\n',
            '请尽管吩咐我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D13(): pass

    label('loc_1D13')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x1D17
@scena.Code('func_0C_1D17')
def func_0C_1D17():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 4, 0x63C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2183',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 4, 0x63C))
    EventBegin(0x00)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 29590, 0, -55060, 0)
    ChrSetPos(0x0102, 28580, 0, -55120, 45)
    CameraMove(29870, 0, -54070, 0)
    ChrSetSubChip(0x00FE, 1)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0550120334V#802F哦哦……\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120335V#006F工房长先生！\n',
            '您果然也被邀请了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120336V#010F因为邀请的都是市长级别的人物，\n',
            '所以觉得工房长肯定也会来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550120337V#801F你们才是，\n',
            '真没想到能得到武术大会冠军，\n',
            '还被邀请来格兰赛尔城呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120338V哎呀～\n',
            '不愧是卡西乌斯先生的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120339V#008F嘿嘿……\n',
            '因为得到了很多人的帮助嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120340V#012F对了，最近这些天有什么动静吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550120341V#800F嗯……\n',
            '你们刚出发去王都，\n',
            '情报部的凯诺娜上尉就来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120342V虽然没办法拒绝出席晚宴，\n',
            '不过关于你们潜入要塞的事，\n',
            '不管怎么说还是瞒过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120343V逃走的拉赛尔博士他们，\n',
            '好像也没有被军队发现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120344V#803F不过，这种情况再持续下去，\n',
            '被抓住也只是时间上的问题了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120345V#003F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550120346V#800F刚才，我向凯诺娜上尉\n',
            '提出要探望女王陛下的要求，\n',
            '但话音刚落就被她一口拒绝了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120347V果然还是很难直接见面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120348V#007F好像是呢……\n',
            '#006F不过别担心，已经有办法了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120349V#012F不管怎么说，\n',
            '一定要把博士的传话带给女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)
    EventEnd(0x00)

    Jump('loc_2697')

    def _loc_2183(): pass

    label('loc_2183')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_2290',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_2205',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120363V#800F街上还是那么热闹啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120364V难得来一趟王都。\n',
            '回去之前就去酒馆里放松一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_228D')

    def _loc_2205(): pass

    label('loc_2205')

    ChrTalk(
        0x0008,
        (
            '#0550120365V#800F我和拉赛尔博士\n',
            '这么长时间不在中央工房，\n',
            '真是担心那边的情况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120366V我打算明天就乘『林德号』返回蔡斯。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_228D(): pass

    label('loc_228D')

    Jump('loc_2694')

    def _loc_2290(): pass

    label('loc_2290')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_229A',
    )

    Jump('loc_2694')

    def _loc_229A(): pass

    label('loc_229A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_22A4',
    )

    Jump('loc_2694')

    def _loc_22A4(): pass

    label('loc_22A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2562',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 1, 0x6F9)),
            Expr.Return,
        ),
        'loc_232C',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120367V#800F听说陛下的病情有了好转，\n',
            '让人松了一口气啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120368V只要知道这件事，\n',
            '来王都这一趟就值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255F')

    def _loc_232C(): pass

    label('loc_232C')

    SetScenaFlags(ScenaFlag(0x00DF, 1, 0x6F9))

    ChrTalk(
        0x0008,
        (
            '#0550120352V#800F希尔丹夫人，好久不见了。\n',
            '看到您这么有精神，真是太好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#0650120353V#711F玛多克工房长也没变呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120354V还是老样子，\n',
            '总是闲不下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550120355V#801F哈～哈，话说回来，\n',
            '中央工房优秀的新人辈出，\n',
            '让人甚感欣慰啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120356V#800F而且听说陛下的病情有了好转，\n',
            '让人松了一口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#0650120357V#710F……嗯，我想再过不久\n',
            '就可以和陛下见面了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120358V玛多克工房长，\n',
            '如果您有什么需要的话，\n',
            '请别客气，尽量提出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120359V我们会马上为您准备好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550120360V#800F……哦，让您费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_255F(): pass

    label('loc_255F')

    Jump('loc_2694')

    def _loc_2562(): pass

    label('loc_2562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_25C6',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120361V#800F哦，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120362V怎么样，\n',
            '和女王陛下见到面了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2694')

    def _loc_25C6(): pass

    label('loc_25C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_2694',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_25EF',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_2620')

    def _loc_25EF(): pass

    label('loc_25EF')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2605',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_2620')

    def _loc_2605(): pass

    label('loc_2605')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_261B',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_2620')

    def _loc_261B(): pass

    label('loc_261B')

    ChrSetSubChip(0x00FE, 2)

    def _loc_2620(): pass

    label('loc_2620')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0550120350V#800F情报部的那些人非常地狡猾。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120351V你们两个务必要\n',
            '谨慎小心地行动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    def _loc_2694(): pass

    label('loc_2694')

    TalkEnd(0x00FE)

    def _loc_2697(): pass

    label('loc_2697')

    Return()

# id: 0x000D offset: 0x2698
@scena.Code('func_0D_2698')
def func_0D_2698():
    EventBegin(0x00)
    CameraMove(132620, 4000, -1250, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0009, 13)
    ChrSetChipByIndex(0x0101, 14)
    ChrSetChipByIndex(0x0102, 15)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 149100, 4200, 7600, 270)
    ChrSetPos(0x0102, 146580, 4200, 8100, 90)
    ChrSetPos(0x0101, 146580, 4200, 7130, 90)
    FadeIn(1500, 0)
    CameraMove(147760, 4000, 7560, 5000)
    Fade(1000)
    CameraMove(148910, 4000, 7610, 0)
    OP_67(0, 5740, -10000, 0)
    CameraSetDistance(1090, 0)
    OP_6C(88000, 0)
    OP_6E(699, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0130120848V#110F……第一次见到卡西乌斯上校时\n',
            '我只是个刚从士官学校毕业的学生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120849V加入王国军之后，我就被分配到\n',
            '他所率领的独立机动部队去了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120850V从那以后，直到他引退的那段日子，\n',
            '我都在工作和生活各方面都受到他的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120851V#506F呵、呵～呵……\n',
            '是这样的啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120852V#501F嗯，当时我的老爸\n',
            '给上校您留下什么样的印象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120853V#115F用一个词形容，就是『英雄』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120854V称为『剑圣』也毫不为过的精湛技艺。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120855V面对任何战况都可以灵活应对，\n',
            '拥有立体的全方位指挥能力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120856V而且不仅仅是拥有各种战术，\n',
            '还拥有指挥部队的高超战略能力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120857V#110F不管哪一项都无人能及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120858V#509F听、听起来总觉得\n',
            '这么厉害的人不像是老爸呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120859V#010F父亲退役和那个『百日战役』\n',
            '是在同一时期吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120860V#116F嗯……\n',
            '我当时在卡西乌斯上校的麾下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120861V到现在我都还记得很清楚，\n',
            '他所部署的奇迹般的作战给我们\n',
            '军中将士所带来的热情与兴奋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120862V#115F一说起那个时候的事情，\n',
            '再有多少时间都不够用，\n',
            '以后有机会我会和你们慢慢道来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120863V但仅凭这些就可以断定一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120864V#112F那就是——如果那时没有一位\n',
            '叫做卡西乌斯·布莱特的男人，\n',
            '利贝尔就已经被埃雷波尼亚所吞并了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120865V#004F不、不会吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120866V的确有些难以置信……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120867V#110F呵呵，能将难以置信之事\n',
            '化为可能的就是『英雄』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120868V而且他在战争之后很快就退役了，\n',
            '更加拒绝了女王陛下授予的勋章，\n',
            '不让世人知道其威名……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120869V至今为止，在一部分军人之中还把\n',
            '卡西乌斯上校的名字作为英雄的代名词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120870V#009F唔～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120871V#582F那个小气的老爸，\n',
            '这些事情竟然一个字也没跟我提起过！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 2)

    ChrTalk(
        0x0102,
        (
            '#0020120872V#010F如果特地和女儿说这番话，\n',
            '也不见得她能听得进去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120873V若是责备父亲的话，他也太可怜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010120874V#005F可、可怜的是我们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120875V#509F……说起来，\n',
            '约修亚你似乎不是很吃惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120876V难道说……\n',
            '刚才那些事情你是都知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120877V#014F理查德上校是父亲的部下这一点\n',
            '的确不知道……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120878V#015F不过……其他的我是知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120879V#005F什、什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120880V这么说约修亚就是共犯了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120881V#019F太、太夸张了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120882V我是从别的地方得知的，\n',
            '父亲并没有亲口告诉过我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120883V而且父亲也没必要\n',
            '特地告诉我们这些事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120884V#509F唔～不太令人信服哦～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120885V#582F真是的……\n',
            '回去之后一定要好好教训他一顿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120886V#110F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010120887V#503F啊，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120888V#017F非、非常抱歉。\n',
            '中途打断了您说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120889V#115F哪里……\n',
            '看见你们这样我也稍感安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120890V卡西乌斯上校要退役的时候，\n',
            '我曾经打算用尽方法来挽留住他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120891V不过那样的选择，\n',
            '对他来说也许是最合适的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120892V#110F有你们陪伴在他身旁，\n',
            '失去夫人的悲痛一定会逐渐消去的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120893V#004F理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120894V#012F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(147760, 4000, 7560, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0009, 148530, 4000, 6210, 270)
    ChrClearFlags(0x0009, 0x0800)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0102, 2)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0130120895V#111F#2P那么……\n',
            '多谢你们能陪我聊一下天。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120896V因为公爵大人还在等着我过去，\n',
            '所以我就先告辞了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120897V#004F啊……好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120898V#010F抱歉，那个……\n',
            '我们完全是在听您的讲话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120899V#110F#2P不，没那回事。\n',
            '你们让我得知了我最想知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120900V#115F……这样一来我就没有什么可以遗憾的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111312V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120902V#012F这究竟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120903V#111F#2P哈哈，最近一段时间\n',
            '我们还会有机会见面的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120904V那时就可以和卡西乌斯上校\n',
            '还有你们一起好好聊聊了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)
    OP_62(0x0101, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    @scena.Lambda('lambda_357C')
    def lambda_357C():
        CameraMove(146770, 2000, -760, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_357C)

    CreateThread(0x0009, 0x01, 0x00, func_0E_3BF5)
    ChrSetSubChip(0x0101, 2)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_63(0x0101)
    OP_63(0x0102)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetPos(0x0102, 146580, 4000, 8100, 90)
    ChrSetPos(0x0101, 146580, 4000, 7130, 90)

    @scena.Lambda('lambda_35E9')
    def lambda_35E9():
        ChrWalkTo(0x00FE, 147560, 4000, 5300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35E9)

    Sleep(300)

    @scena.Lambda('lambda_3609')
    def lambda_3609():
        ChrWalkTo(0x00FE, 148500, 4000, 5300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3609)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_3629')
    def lambda_3629():
        CameraMove(148490, 4000, 5300, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3629)

    ChrSetDirection(0x0101, 225, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 225, 400)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010120905V#505F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120906V刚才那个人真的是理查德上校吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120907V#017F#2P我说……你睡迷糊了啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120908V#003F#6P可、可是他那样钦佩地\n',
            '说着老爸过去的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120909V怎么说好呢……\n',
            '和以往留下的印象不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120910V#015F#2P……的确。\n',
            '他并不是一个单纯的坏人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120911V#012F可是，抛开这个不提，\n',
            '他肯定是有什么企图的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120912V否则怎么会对父亲的事情\n',
            '了解得那么清楚明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120913V#007F#6P嗯……\n',
            '话是这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120914V#015F#2P丑话先说在前面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120915V把我们这么亲切地找来，\n',
            '也许是处于什么目的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120916V#012F像他那样的情报专家，\n',
            '要想欺骗我们这样的小孩，\n',
            '简直就是易如反掌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120917V#009F#6P你、你敢肯定刚才你说的那些话\n',
            '没有言过其实吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120918V#015F#2P嗯……肯定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120919V防人之心不可无。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120920V你只要相信你自己的直觉就可以了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120921V#004F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120922V#012F#2P要做好各种准备，\n',
            '对任何人都不可掉以轻心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120923V这一点也是游击士所要做到的……\n',
            '我认为就是这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120924V#500F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120925V#006F嗯，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120926V我会牢记在心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120927V#010F#2P……谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120928V#506F#6P什么～呀。\n',
            '约修亚你怎么和我讲起礼来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120929V#006F接下来我们要立刻\n',
            '赶到希尔丹夫人那里去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120930V她大概已经等得不耐烦了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120931V#010F#2P是啊……\n',
            '这就前去女佣的休息室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    SetScenaFlags(ScenaFlag(0x00C8, 1, 0x641))
    EventEnd(0x00)
    PlayBGM(17)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000E offset: 0x3BF5
@scena.Code('func_0E_3BF5')
def func_0E_3BF5():
    ChrWalkTo(0x00FE, 147940, 4000, 3800, 3000, 0x00)
    ChrClearFlags(0x0009, 0x0004)
    ChrWalkTo(0x00FE, 147920, 2000, -1500, 3000, 0x00)
    ChrWalkTo(0x00FE, 140850, 0, -1500, 3000, 0x00)
    ChrWalkTo(0x00FE, 132710, 0, 800, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000F offset: 0x3C50
@scena.Code('func_0F_3C50')
def func_0F_3C50():
    EventBegin(0x00)
    CameraMove(88650, 0, 6240, 0)
    OP_67(0, 5460, -10000, 0)
    CameraSetDistance(1940, 0)
    OP_6C(46000, 0)
    OP_6E(474, 0)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetPos(0x0138, 87950, 0, 4590, 0)
    ChrSetPos(0x0101, 87640, 0, 6230, 90)
    ChrSetPos(0x0102, 89210, 0, 6370, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010121368V#327F呼……\n',
            '约修亚你可真受欢迎啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121369V那个家伙一听到约修亚的名字，\n',
            '顿时就两眼放光呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121370V#337F#2P哪、哪有那样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121371V倒是你啊，装得还真像回事。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121372V#473F我那个时候对着那个家伙，\n',
            '可是一点紧张感都没有呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121373V#327F呼～不管怎么说～\n',
            '还是觉得有些不够自信啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121374V#332F#2P嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 93780, 0, 850, 90)
    ChrSetPos(0x000B, 93780, 0, 850, 90)
    OP_72(0x0024, 0x0010)
    OP_6F(0x0024, 0)
    OP_70(0x0024, 60)
    OP_73(0x0024)

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#0640121375V嗝……\n',
            '什么人在吵吵嚷嚷的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0040)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0138, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_3F12')
    def lambda_3F12():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F12)

    @scena.Lambda('lambda_3F20')
    def lambda_3F20():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3F20)

    @scena.Lambda('lambda_3F2E')
    def lambda_3F2E():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_3F2E)

    CameraMove(90380, 0, 5100, 1000)

    @scena.Lambda('lambda_3F4D')
    def lambda_3F4D():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3F4D')

    DispatchAsync2(0x0101, 0x0001, lambda_3F4D)

    @scena.Lambda('lambda_3F5E')
    def lambda_3F5E():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3F5E')

    DispatchAsync2(0x0102, 0x0001, lambda_3F5E)

    @scena.Lambda('lambda_3F6F')
    def lambda_3F6F():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3F6F')

    DispatchAsync2(0x0138, 0x0001, lambda_3F6F)

    @scena.Lambda('lambda_3F80')
    def lambda_3F80():
        CameraMove(89070, 0, 5570, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3F80)

    @scena.Lambda('lambda_3F98')
    def lambda_3F98():
        ChrWalkTo(0x00FE, 90890, 0, 1590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3F98)

    WaitForThreadExit(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_3FBD')
    def lambda_3FBD():
        ChrWalkTo(0x00FE, 89350, 0, 4440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3FBD)

    ChrWalkTo(0x000B, 91530, 0, 1210, 2000, 0x00)
    OP_72(0x0024, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0024, 60)
    OP_70(0x0024, 0)

    @scena.Lambda('lambda_4004')
    def lambda_4004():
        ChrWalkTo(0x00FE, 90890, 0, 1590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4004)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_4024')
    def lambda_4024():
        ChrWalkTo(0x00FE, 89760, 0, 3500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4024)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_4044')
    def lambda_4044():
        ChrTurnDirection(0x00FE, 0x0138, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4044)

    ChrTalk(
        0x0138,
        (
            '#0650121376V#712F公爵大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640121377V#227F我还以为是谁呢，这不是女管家吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0640121378V#481F哦……\n',
            '怎么，那两个侍女是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121379V嗝……\n',
            '以前没见过的小姑娘哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 6, 0x676)),
            Expr.Return,
        ),
        'loc_41A6',
    )

    ChrTalk(
        0x0138,
        (
            '#0650121380V#713F新来的实习侍女，\n',
            '莱娜和卡玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121381V因为她们对城里还不熟悉，\n',
            '所以我刚才带她们到处走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A3')

    def _loc_41A6(): pass

    label('loc_41A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 7, 0x677)),
            Expr.Return,
        ),
        'loc_4225',
    )

    ChrTalk(
        0x0138,
        (
            '#0650121382V#713F新来的实习侍女，\n',
            '雪拉和卡玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121381V因为她们对城里还不熟悉，\n',
            '所以我刚才带她们到处走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A3')

    def _loc_4225(): pass

    label('loc_4225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 0, 0x678)),
            Expr.Return,
        ),
        'loc_42A3',
    )

    ChrTalk(
        0x0138,
        (
            '#0650121384V#713F新来的实习侍女，\n',
            '朵洛希和卡玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121381V因为她们对城里还不熟悉，\n',
            '所以我刚才带她们到处走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42A3(): pass

    label('loc_42A3')

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0660121386V#722F哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000B, 90180, 0, 4270, 2000, 0x00)
    ChrWalkTo(0x000B, 89920, 0, 5310, 2000, 0x00)
    ChrTurnDirection(0x000B, 0x0102, 400)
    Sleep(500)

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0660121387V#721F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121388V#323F#1P（啊……注意到了？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121389V#335F（……糟糕了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121390V（毕竟和这个管家见过几次面，\n',
            '　所以被注意到也不奇怪……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640121391V#481F怎么了，菲利普。\n',
            '目不转睛的盯着看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121392V#229F哇哈哈，你这个正经古板的家伙，\n',
            '很少见你有这么出格的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660121393V#720F失礼了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121394V因为这位小姐和我的侄女很相似，\n',
            '所以不禁一下子就呆住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121395V两位小姐，刚才真是非常的抱歉。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121396V#474F#1P啊，没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121397V#331F请不要介意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640121398V#227F嘿嘿，仔细地再瞧一下，\n',
            '不管哪个都是精选的上等货色啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121399V尤其是棕色头发的那位，\n',
            '真是极具阳光女孩的气息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010121400V#476F#1P……（鄙视）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640121401V#227F至于黑色头发的那位嘛……\n',
            '要是再稍微把腰挺直点就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121402V#338F……惶、惶恐之至。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640121403V#483F呼，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 6, 0x676)),
            Expr.Return,
        ),
        'loc_4707',
    )

    ChrTalk(
        0x000A,
        (
            '#0640121404V#482F#3S莱娜！\n',
            '我命令你今晚来伺候我！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    Jump('loc_47AA')

    def _loc_4707(): pass

    label('loc_4707')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 7, 0x677)),
            Expr.Return,
        ),
        'loc_4759',
    )

    ChrTalk(
        0x000A,
        (
            '#0640121405V#482F#3S雪拉！\n',
            '我命令你今晚来伺候我！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    Jump('loc_47AA')

    def _loc_4759(): pass

    label('loc_4759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 0, 0x678)),
            Expr.Return,
        ),
        'loc_47AA',
    )

    ChrTalk(
        0x000A,
        (
            '#0640121406V#482F#3S朵洛希！\n',
            '我命令你今晚来伺候我！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    def _loc_47AA(): pass

    label('loc_47AA')

    ChrTalk(
        0x0102,
        (
            '#0020121407V#332F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121408V#324F#1P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#0660121409V#721F公、公爵大人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121410V#473F#1P（咦，什么叫伺候呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121411V#334F（唔，该怎么说好呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121412V#714F公爵大人，再怎么说，\n',
            '玩笑也开得有些过分了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121413V在这个格兰赛尔城工作的侍女\n',
            '全都是诚心服侍女王陛下的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121414V您难道忘记了这一点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0138, 400)

    ChrTalk(
        0x000A,
        (
            '#0640121415V#480F我知道、我知道……\n',
            '真是个连玩笑都受不起的大婶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121416V#483F嗝……\n',
            '反正一周之后这个王城就是我的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121417V嘿嘿嘿……\n',
            '到那时我再来好好享受这番乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121418V#714F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660121419V#723F公、公爵大人！\n',
            '请您说话适可而止！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121420V暴饮暴食姑且不论，\n',
            '沉溺女色简直就是岂有此理！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121421V我菲利普就算拼了老命，\n',
            '也会阻止大人您做出如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#0640121422V#482F刚才不是说了只是在开玩笑嘛！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121423V够了！\n',
            '今晚赶快回去休息吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660121424V#722F公、公爵大人所言极是。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121425V#720F大人您的房间就在前面，\n',
            '请您小心脚下慢慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4B9C')
    def lambda_4B9C():
        CameraMove(87270, 0, 5910, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4B9C)

    @scena.Lambda('lambda_4BB4')
    def lambda_4BB4():
        ChrWalkTo(0x00FE, 88470, 0, 5250, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4BB4)

    Sleep(600)

    @scena.Lambda('lambda_4BD4')
    def lambda_4BD4():
        ChrWalkTo(0x00FE, 86510, 0, 5570, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4BD4)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_4BF4')
    def lambda_4BF4():
        ChrWalkTo(0x00FE, 85560, 0, 5560, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4BF4)

    WaitForThreadExit(0x000A, 0x0001)
    Sleep(1000)

    @scena.Lambda('lambda_4C19')
    def lambda_4C19():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4C19')

    DispatchAsync2(0x000B, 0x0002, lambda_4C19)

    @scena.Lambda('lambda_4C2A')
    def lambda_4C2A():
        ChrTurnDirection(0x000A, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4C2A)

    ChrMoveTo(0x000A, 85650, 0, 6380, 1000, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 6, 0x676)),
            Expr.Return,
        ),
        'loc_4D0D',
    )

    ChrTalk(
        0x000A,
        (
            '#0640121426V#227F嗯～……\n',
            '对了，莱娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121427V#483F如果有什么感情上的问题的话，\n',
            '请不用客气，随时来找我商量哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121428V嘿嘿……身为下任国王的我\n',
            '一定会亲自帮你好好解决的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E9A')

    def _loc_4D0D(): pass

    label('loc_4D0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 7, 0x677)),
            Expr.Return,
        ),
        'loc_4DD4',
    )

    ChrTalk(
        0x000A,
        (
            '#0640121429V#227F嗯～……\n',
            '对了，雪拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121427V#483F如果有什么感情上的问题的话，\n',
            '请不用客气，随时来找我商量哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121428V嘿嘿……身为下任国王的我\n',
            '一定会亲自帮你好好解决的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E9A')

    def _loc_4DD4(): pass

    label('loc_4DD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 0, 0x678)),
            Expr.Return,
        ),
        'loc_4E9A',
    )

    ChrTalk(
        0x000A,
        (
            '#0640121432V#227F嗯～……\n',
            '对了，朵洛希。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121427V#483F如果有什么感情上的问题的话，\n',
            '请不用客气，随时来找我商量哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121428V嘿嘿……身为下任国王的我\n',
            '一定会亲自帮你好好解决的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E9A(): pass

    label('loc_4E9A')

    ChrTalk(
        0x0101,
        (
            '#0010121435V#476F啊哈……哈哈……\n',
            '在此先向您谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640121436V#229F哇哈哈，可爱的宝贝儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121437V#227F嗯……不错不错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 400)

    @scena.Lambda('lambda_4F31')
    def lambda_4F31():
        CameraMove(83810, 0, 6600, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4F31)

    ChrWalkTo(0x000A, 78870, 0, 6990, 1500, 0x00)
    ChrWalkTo(0x000A, 78920, 0, 7400, 1500, 0x00)
    OP_72(0x0021, 0x0010)
    OP_6F(0x0021, 0)
    OP_70(0x0021, 60)
    OP_73(0x0021)
    ChrWalkTo(0x000A, 78870, 0, 9590, 1500, 0x00)
    OP_72(0x0021, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0021, 60)
    OP_70(0x0021, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0138, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    @scena.Lambda('lambda_4FC7')
    def lambda_4FC7():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_4FC7')

    DispatchAsync2(0x0101, 0x0001, lambda_4FC7)

    @scena.Lambda('lambda_4FD8')
    def lambda_4FD8():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_4FD8')

    DispatchAsync2(0x0102, 0x0001, lambda_4FD8)

    @scena.Lambda('lambda_4FE9')
    def lambda_4FE9():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_4FE9')

    DispatchAsync2(0x0138, 0x0001, lambda_4FE9)

    @scena.Lambda('lambda_4FFA')
    def lambda_4FFA():
        CameraMove(88010, 0, 6080, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4FFA)

    ChrSetDirection(0x000B, 90, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#0660121438V#722F让你们受惊了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121439V大人明天一早起来的时候，\n',
            '就会什么也记不起来的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121440V请两位小姐放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121441V#714F……希望会是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660121442V#720F真是非常的抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121443V夫人、两位姑娘，\n',
            '那我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 400)
    ChrWalkTo(0x000B, 78950, 0, 5780, 3000, 0x00)
    ChrWalkTo(0x000B, 79030, 0, 9870, 3000, 0x00)
    PlaySE(6, 0x00, 0x64)
    Sleep(1500)

    PlaySE(7, 0x00, 0x64)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0138, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x0138,
        (
            '#0650121444V#716F唉，那个当管家的也够辛苦的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121445V几十年来都是那么辛苦地背负着\n',
            '杜南公爵那个累人的负担……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121446V#324F咦……\n',
            '希尔丹夫人和菲利普先生认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0138, 0x0101, 400)

    ChrTalk(
        0x0138,
        (
            '#0650121447V#715F在年幼的时候就认识了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121448V可是到了今天，不管在工作方面\n',
            '还是在立场方面都有了距离……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0138, 400)

    ChrTalk(
        0x0102,
        (
            '#0020121449V#330F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121450V#327F的确，菲利普先生看起来\n',
            '就是一副饱经沧桑的样子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121451V#473F他对公爵被上校唆使这件事\n',
            '好像非常担心的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020121452V#330F很有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121453V#338F对了，艾丝蒂尔，\n',
            '看来你也很受男性欢迎嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121454V公爵看来很喜欢你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121455V#476F哼……\n',
            '你好像是在幸灾乐祸啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121456V#471F啊，对了对了……\n',
            '到底那个『伺候』是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121457V#337F这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121458V#713F艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121459V向异性提出这种问题，\n',
            '会让对方很难为情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_54E6')
    def lambda_54E6():
        ChrTurnDirection(0x00FE, 0x0138, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_54E6)

    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121460V#324F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121461V#710F……把耳朵凑过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)
    ChrWalkTo(0x0138, 87590, 0, 5700, 2000, 0x00)
    ChrSetDirection(0x0101, 270, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '希尔丹夫人对艾丝蒂尔说了悄悄话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrMoveTo(0x0138, 87950, 0, 4590, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010121462V#472F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121463V#711F……明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121464V#472F啊，唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121465V#327F…………知道了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121466V#333F（果真是毫无防备啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4254._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x56CD
@scena.Code('func_10_56CD')
def func_10_56CD():
    EventBegin(0x00)
    FormationDelMember(0x01, 0xFF)
    ChrClearFlags(0x000C, 0x0080)
    TerminateThread(0x000C, 0xFF)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetPos(0x000C, 30760, 200, 53020, 270)
    ChrSetPos(0x0017, 29800, 500, 53440, 0)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0012, 29750, 500, 53150, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0013, 29750, 500, 52650, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, 29300, 500, 53440, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0015, 29300, 500, 52920, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0016, 29300, 500, 52420, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0101, 31390, 0, 55480, 270)
    CameraMove(29710, 0, 54720, 0)
    OP_67(0, 6900, -10000, 0)
    CameraSetDistance(2040, 0)
    OP_6C(45000, 0)
    OP_6E(401, 0)
    FadeIn(2000, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrWalkTo(0x0101, 29040, 0, 55000, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    ChrWalkTo(0x0101, 31390, 0, 55000, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 180, 400)
    ChrWalkTo(0x0101, 29040, 0, 55000, 2000, 0x00)
    Sleep(500)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010141160V#505F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141161V#020F怎么了，艾丝蒂尔。\n',
            '从刚才开始就静不下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141162V是不是有什么心事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010141163V#007F#5P嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_58F4')
    def lambda_58F4():
        CameraMove(30840, 0, 54690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58F4)

    ChrWalkTo(0x0101, 29910, 0, 54320, 1000, 0x00)
    ChrSetDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010141164V#002F#6P我说，雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141165V刚才一起吃饭的时候，\n',
            '觉不觉得约修亚的样子很奇怪啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141166V#023F#2P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141167V奇怪的是你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141168V那孩子不是和平时一样沉着冷静吗。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141169V#003F#6P话是这样说没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0030141170V#027F#2P哈哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141171V是吗，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141172V#004F#6P怎、怎么了，突然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141173V#021F#2P你瞒不住我的～⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141174V虽然看你平时总是呆呆的……\n',
            '不过到最后还是察觉出了自己的心意吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141175V#027F你啊……\n',
            '是不是喜欢上约修亚了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141176V#503F#6P………唔…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141177V#503F看、看得出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141178V#027F#2P不好意思哦～被我发现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141179V不过你这个样子，\n',
            '可没办法向约修亚表达真正的心意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141180V#503F#6P嗯……我也这样觉得……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141181V那个约修亚从以前开始，\n',
            '就对这方面的事情很迟钝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141182V#506F哎，我也没有资格说别人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141183V#520F#2P哎呀，真是单纯的想法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141184V那个不谙世事的艾丝蒂尔，\n',
            '也终于走到这一步了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141185V姐姐我真是感动啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141186V#509F#6P……真是的～再这样的话，\n',
            '我就不和雪拉姐说了哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141187V#020F#2P抱歉抱歉，我不开玩笑了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141188V#026F不过，也的确是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141189V仔细想想的话，\n',
            '你们在很小的时候就已经认识了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141190V所以没有注意到对方心意的变化\n',
            '也是没办法的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141191V#008F#6P是、是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141192V#503F我也是在旅行的途中，\n',
            '才开始慢慢意识到这种感觉的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141193V当、当我有一次非常在意他的时候，\n',
            '我就一下子意识到这种感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141194V#504F啊啊，真是的。\n',
            '这样根本不像我的性格啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141195V#027F#2P呵呵……\n',
            '世上没有不会绽放的花蕾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141196V女孩子都是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141197V#008F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141198V#020F#2P虽然表达心意不能太过轻率……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141199V不过，既然你已经下定决心的话，\n',
            '坦白地说出来不是更好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141200V如果觉得难以决定的话，\n',
            '不如姐姐我来为你占卜一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141201V#503F#6P不用了……\n',
            '其实，我已经下定决心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141202V而且也和他约好要听他说自己以前的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141203V#020F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141204V#520F好，这样才是我的妹妹嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141205V哎呀，真是的。\n',
            '姐姐我都要感动得想哭了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141206V#509F#6P就不能说多点建设性的话吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141207V#501F不过，谢谢你，雪拉姐。\n',
            '我觉得现在已经有点勇气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141208V我这就去约修亚那里看看。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x000C, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000C,
        (
            '#0030141209V#023F#2P哎……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141210V不、不会现在就要去告白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141211V#006F#6P不是啦，是其他的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141212V不知道是不是心理作用，\n',
            '总觉得刚才约修亚的样子有点奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141213V我先问问他是怎么回事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141214V#025F#2P是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141215V#020F不管怎样，\n',
            '你对他的事情还真是很了解啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141216V#021F你和约修亚一定会发展得很顺利的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141217V如果聊天的时候气氛不错，\n',
            '干脆就趁势向他告白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141218V#007F#6P唔……尽量吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141219V#006F那么，我走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 800)

    @scena.Lambda('lambda_6478')
    def lambda_6478():
        CameraMove(31870, 0, 54140, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6478)

    ChrWalkTo(0x0101, 33130, 0, 54320, 5000, 0x00)
    ChrSetSubChip(0x000C, 1)
    ChrWalkTo(0x0101, 35000, 0, 50320, 5000, 0x00)
    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_64C2')
    def lambda_64C2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_64C2)

    ChrWalkTo(0x0101, 35000, 0, 48980, 5000, 0x00)
    Sleep(1500)

    @scena.Lambda('lambda_64ED')
    def lambda_64ED():
        CameraMove(30840, 0, 54690, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_64ED)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    ChrSetChipByIndex(0x000C, 20)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetSubChip(0x000C, 0)
    OP_0D()
    Sleep(400)

    ChrSetSubChip(0x000C, 1)
    Sleep(400)

    OP_99(0x000C, 0x01, 0x03, 800)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0030141220V#026F#5P……初恋吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141221V#027F如果能顺利就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    Call(0, 0x0011)

    Return()

# id: 0x0011 offset: 0x659A
@scena.Code('func_11_659A')
def func_11_659A():
    EventBegin(0x00)
    CameraMove(89230, 0, 60740, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 79820, 0, 50600, 0)

    @scena.Lambda('lambda_65F0')
    def lambda_65F0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_65F0)

    FadeIn(1000, 0)
    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_6610')
    def lambda_6610():
        ChrWalkTo(0x00FE, 79700, 0, 55220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6610)

    CameraMove(81310, 0, 56390, 4000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010141224V#004F#6P咦……两个人都不在啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141225V#505F对了，老爸说过还要开会……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141226V可是，约修亚呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(74)
    OP_1F(0x50, 0x000000C8)
    Sleep(2000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010141227V#501F#6P约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141228V他在哪里吹口琴呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1B(0x00, 0x00, 0xFFFF)
    OP_1B(0x06, 0x00, 0xFFFF)
    SetScenaFlags(ScenaFlag(0x00CE, 0, 0x670))
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x6751
@scena.Code('func_12_6751')
def func_12_6751():
    OP_1F(0x50, 0x000000C8)

    Return()

# id: 0x0013 offset: 0x6758
@scena.Code('func_13_6758')
def func_13_6758():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67CB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x0101,
        (
            '#0010141330V#505F口琴声……\n',
            '好像是从外面传来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141331V也就是说，\n',
            '约修亚在空中庭园了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6803')

    def _loc_67CB(): pass

    label('loc_67CB')

    ChrTalk(
        0x0101,
        (
            '#0010141332V#006F总之到屋顶的空中庭园去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6803(): pass

    label('loc_6803')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    EventEnd(0x01)

    Return()

# id: 0x0014 offset: 0x681A
@scena.Code('func_14_681A')
def func_14_681A():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010141222V#007F哎呀，我真是的。\n',
            '这是往哪里走啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141223V#000F……不赶快去约修亚的房间的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
