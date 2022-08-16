import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R4101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R4101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'R4101.x'
    header.mapIndex       = 1
    header.bgm            = 20
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
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
    ]

# id: 0x10001 offset: 0x192
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基库',
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
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '洛伦斯少尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '卡露娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亚妮拉丝',
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
            name                = '库拉茨',
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
            name                = '克鲁茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务艇影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '圣海姆门方向',
            x                   = -5160,
            z                   = -50,
            y                   = -7520,
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
        ScenaNpcData(
            name                = '王都格兰赛尔方向',
            x                   = -39160,
            z                   = 0,
            y                   = 152720,
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
        ScenaNpcData(
            name                = '格鲁纳门方向',
            x                   = 61180,
            z                   = 0,
            y                   = 83020,
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

# id: 0x10002 offset: 0x4D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = -6830,
            z           = 90,
            y           = 29510,
            word_0C     = 0x0000,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = 16290,
            z           = 70,
            y           = 76970,
            word_0C     = 0x0000,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫',
            x           = 31220,
            z           = 40,
            y           = 83060,
            word_0C     = 0x0000,
            word_0E     = 0x001B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫',
            x           = -33000,
            z           = 20,
            y           = 72240,
            word_0C     = 0x0000,
            word_0E     = 0x001B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = -17830,
            z           = 10,
            y           = 103860,
            word_0C     = 0x0000,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '剑齿吸血魔',
            x           = -58070,
            z           = 30,
            y           = 101390,
            word_0C     = 0x0000,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = -59820,
            z           = 0,
            y           = 105790,
            word_0C     = 0x0000,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫',
            x           = -61630,
            z           = 70,
            y           = 108700,
            word_0C     = 0x0000,
            word_0E     = 0x001B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x5B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x5B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -13540,
            triggerZ            = 0,
            triggerY            = 63650,
            triggerRange        = 1500,
            actorX              = -13540,
            actorZ              = 1700,
            actorY              = 63650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 130,
            triggerZ            = 0,
            triggerY            = 56450,
            triggerRange        = 1500,
            actorX              = 130,
            actorZ              = 1700,
            actorY              = 56450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1460,
            triggerZ            = 0,
            triggerY            = 53030,
            triggerRange        = 1500,
            actorX              = -1460,
            actorZ              = 1700,
            actorY              = 53030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x61E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_63D',
    )

    OP_26(121)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_679)

    def _loc_63D(): pass

    label('loc_63D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_654',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0B_14FF)

    def _loc_654(): pass

    label('loc_654')

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x666
@scena.Code('func_01_666')
def func_01_666():
    OP_16(0x02, 4000, -135000, -60000, 196668)

    Return()

# id: 0x0002 offset: 0x679
@scena.Code('func_02_679')
def func_02_679():
    OP_B6(0x00)
    MapClearFlags(0x02000000)
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    OP_77(0xC8, 0xC8, 0xC8, 0x00, 0x00000000)
    CameraMove(-38280, 0, 81580, 0)
    OP_67(0, 5320, -10000, 0)
    CameraSetDistance(3940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0008, 0x0080)
    OP_11(0x00, 0x00, 0x00, 38000, 130000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0008, -38320, 0, 69680, 270)
    ChrSetPos(0x0009, -39300, 6000, 86750, 270)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetChipByIndex(0x0008, 12)

    @scena.Lambda('lambda_072A')
    def lambda_072A():
        ChrWalkTo(0x00FE, -39860, 0, 104550, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_072A)

    Sleep(1000)

    @scena.Lambda('lambda_074A')
    def lambda_074A():
        CameraMove(-38720, 0, 104400, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_074A)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0060100032V#049F#5P呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0060100033V#043F#5P……基库，过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0080)
    OP_92(0x0009, 0x0008, 10000, 9000, 0x00)
    PlaySE(140, 0x00, 0x64)
    OP_92(0x0009, 0x0008, 5000, 8000, 0x00)
    OP_92(0x0009, 0x0008, 4000, 6000, 0x00)
    OP_92(0x0009, 0x0008, 3000, 4000, 0x00)
    OP_92(0x0009, 0x0008, 2000, 2000, 0x00)
    ChrWalkTo(0x0009, -40620, 1000, 104480, 1500, 0x00)
    TerminateThread(0x0008, 0xFF)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_0836')
    def lambda_0836():
        ChrSetDirection(0x00FE, 135, 200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0836)

    ChrMoveTo(0x0009, -40280, 200, 104530, 1000, 0x00)
    WaitForThreadExit(0x0009, 0x0003)
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Fade(250)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetSubChip(0x0008, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0440100034V#310F啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060100035V#043F#5P我已经没事了，\n',
            '你去尤莉亚那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100036V这样下去尤莉亚会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0440100037V#311F啾～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060100038V#048F#5P谢谢，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetSubChip(0x0008, 2)
    OP_0D()
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_094C')
    def lambda_094C():
        ChrWalkTo(0x00FE, -37200, 10000, 68710, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_094C)

    Sleep(400)

    @scena.Lambda('lambda_096C')
    def lambda_096C():
        ChrWalkTo(0x00FE, -37200, 10000, 68710, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_096C)

    Sleep(400)

    ChrSetChipByIndex(0x0008, 0)
    ChrClearFlags(0x0008, 0x0020)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_099B')
    def lambda_099B():
        ChrWalkTo(0x00FE, -37200, 10000, 68710, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_099B)

    @scena.Lambda('lambda_09B6')
    def lambda_09B6():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_09B6')

    DispatchAsync2(0x0008, 0x0001, lambda_09B6)

    Sleep(1800)

    TerminateThread(0x0008, 0xFF)
    ChrSetDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_09D7')
    def lambda_09D7():
        CameraMove(-39530, 0, 108060, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_09D7)

    ChrWalkTo(0x0008, -39530, 0, 108060, 2000, 0x00)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0060100039V#042F尤莉亚说得没错，\n',
            '这里的警戒果然比较薄弱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100040V不赶快去游击士协会的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp014_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -39360, 0, 108740, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0105, 0x03, 0x00, func_09_143B)
    Sleep(1500)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0060100041V#043F下雨了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100042V#047F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100043V#049F对了……\n',
            '艾丝蒂尔他们也应该快来到王都了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(121, 0x01, 0x50)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0019, 800)

    @scena.Lambda('lambda_0B93')
    def lambda_0B93():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_0B93')

    DispatchAsync2(0x0008, 0x0001, lambda_0B93)

    ChrTalk(
        0x0008,
        (
            '#0060100044V#044F……难道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_12(0x0000C350, 0x00030D40, 0x00000000)
    Fade(1000)
    OP_6C(134000, 0)
    CameraMove(-28620, 12200, 104390, 0)
    CameraSetDistance(4810, 0)
    OP_67(0, 8730, -10000, 0)
    OP_24(0x0079, 0x64)
    CreateThread(0x0019, 0x01, 0x00, func_03_F2D)
    Sleep(4000)

    @scena.Lambda('lambda_0C22')
    def lambda_0C22():
        CameraSetDistance(6420, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0C22)

    @scena.Lambda('lambda_0C32')
    def lambda_0C32():
        CameraMove(-38470, 6000, 118990, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C32)

    @scena.Lambda('lambda_0C4A')
    def lambda_0C4A():
        OP_6C(24000, 6000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0C4A)

    Sleep(8000)

    @scena.Lambda('lambda_0C5F')
    def lambda_0C5F():
        CameraMove(-38470, 0, 118990, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C5F)

    @scena.Lambda('lambda_0C77')
    def lambda_0C77():
        OP_67(0, 5740, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0C77)

    Sleep(3000)

    ChrMoveTo(0x0008, -39600, 0, 106290, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0060100045V#046F情报部的特务飞艇……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100046V怎么会……\n',
            '竟然在光天化日之下出现在王都前面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -38770, 0, 98180, 0)

    @scena.Lambda('lambda_0D2C')
    def lambda_0D2C():
        ChrWalkTo(0x00FE, -39420, 0, 103410, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D2C)

    Sleep(300)

    @scena.Lambda('lambda_0D4C')
    def lambda_0D4C():
        CameraSetDistance(5300, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0D4C)

    CameraMove(-39190, 0, 105060, 1000)

    ChrTalk(
        0x0008,
        (
            '#0060100047V#043F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140100048V#280F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DBC')
    def lambda_0DBC():
        CameraMove(-39940, 2250, 109870, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0DBC)

    @scena.Lambda('lambda_0DD4')
    def lambda_0DD4():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0DD4)

    @scena.Lambda('lambda_0DE4')
    def lambda_0DE4():
        CameraMove(-39940, 2250, 109870, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0DE4)

    WaitForThreadExit(0x0019, 0x0001)
    OP_73(0x0000)

    @scena.Lambda('lambda_0E04')
    def lambda_0E04():
        CameraMove(-39410, 0, 106900, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0E04)

    WaitForThreadExit(0x001E, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrClearFlags(0x000A, 0x0080)
    OP_89(0x000A, -38890, 3450, 120920, 180)
    WaitForThreadExit(0x0000, 0x0003)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0130100049V#4P啊，在这种地方相遇真是难得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000A, 0x01, 0x00, func_08_13E9)
    Sleep(300)

    ChrTurnDirection(0x0008, 0x000A, 400)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0130100050V#115F杰尼丝王立学院社会系的\n',
            '科洛丝·琳希小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130100051V#111F能和您稍微谈一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0105, 0x03, 0x00, func_0A_14A4)
    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    WaitForThreadExit(0x0105, 0x0003)
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xF2D
@scena.Code('func_03_F2D')
def func_03_F2D():
    ChrSetFlags(0x0019, 0x0004)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x001A, 0x0004)
    ChrSetFlags(0x001A, 0x0040)
    OP_A1(0x0019, 0x0000)
    OP_A1(0x001A, 0x0001)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 700)
    OP_70(0x0000, 780)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    ChrSetPos(0x0019, -13930, 20000, 76820, 324)
    ChrSetPos(0x001A, -13930, 0, 76820, 324)

    @scena.Lambda('lambda_0FA4')
    def lambda_0FA4():
        ChrMoveTo(0x00FE, -38820, 5000, 121000, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_0FA4)

    @scena.Lambda('lambda_0FBF')
    def lambda_0FBF():
        ChrMoveTo(0x00FE, -38820, 100, 121000, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0FBF)

    Sleep(3000)

    @scena.Lambda('lambda_0FDF')
    def lambda_0FDF():
        ChrMoveTo(0x00FE, -38820, 5000, 121000, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_0FDF)

    @scena.Lambda('lambda_0FFA')
    def lambda_0FFA():
        ChrMoveTo(0x00FE, -38820, 100, 121000, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0FFA)

    @scena.Lambda('lambda_1015')
    def lambda_1015():
        ChrSetDirection(0x0019, 0, 5)

        ExitThread()

    DispatchAsync(0x0019, 0x0000, lambda_1015)

    @scena.Lambda('lambda_1023')
    def lambda_1023():
        ChrSetDirection(0x001A, 0, 5)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_1023)

    Sleep(1000)

    PlayEffect(0x01, 0x01, 0x001A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_106B')
    def lambda_106B():
        ChrMoveTo(0x00FE, -38820, 5000, 121000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_106B)

    @scena.Lambda('lambda_1086')
    def lambda_1086():
        ChrMoveTo(0x00FE, -38820, 100, 121000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_1086)

    Sleep(1000)

    @scena.Lambda('lambda_10A6')
    def lambda_10A6():
        ChrMoveTo(0x00FE, -38820, 5000, 121000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_10A6)

    @scena.Lambda('lambda_10C1')
    def lambda_10C1():
        ChrMoveTo(0x00FE, -38820, 100, 121000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_10C1)

    Sleep(1000)

    @scena.Lambda('lambda_10E1')
    def lambda_10E1():
        ChrMoveTo(0x00FE, -38820, 5000, 121000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_10E1)

    @scena.Lambda('lambda_10FC')
    def lambda_10FC():
        ChrMoveTo(0x00FE, -38820, 100, 121000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_10FC)

    Sleep(1000)

    WaitForThreadExit(0x0019, 0x0002)
    OP_72(0x0000, 0x0020)
    PlayEffect(0x01, 0x02, 0x001A, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    OP_6F(0x0000, 1021)
    OP_70(0x0000, 1050)
    OP_73(0x0000)
    OP_6F(0x0000, 1051)
    OP_70(0x0000, 1110)
    ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 3000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, -1500, 0, 2500, 0x00)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    ChrMoveToRelativeAsync(0x00FE, 0, -2300, 0, 2000, 0x00)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    Sleep(1000)

    PlaySE(118, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_6F(0x0000, 61)
    OP_70(0x0000, 230)
    OP_73(0x0000)
    OP_B0(0x0000, 0x3C)
    OP_6F(0x0000, 231)
    OP_70(0x0000, 360)
    OP_73(0x0000)
    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0000, 1140)
    OP_70(0x0000, 1200)
    OP_73(0x0000)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0400)
    OP_71(0x0000, 0x0040)
    CreateThread(0x001B, 0x01, 0x00, func_04_1259)
    Sleep(300)

    CreateThread(0x001C, 0x01, 0x00, func_05_12BD)
    Sleep(300)

    CreateThread(0x001D, 0x01, 0x00, func_06_1321)
    Sleep(300)

    CreateThread(0x001E, 0x01, 0x00, func_07_1385)

    Return()

# id: 0x0004 offset: 0x1259
@scena.Code('func_04_1259')
def func_04_1259():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    OP_89(0x00FE, -38890, 3450, 120920, 180)
    ChrWalkTo(0x00FE, -38860, 3450, 117300, 5000, 0x00)
    ChrWalkTo(0x00FE, -38850, 0, 111640, 5000, 0x00)
    ChrWalkTo(0x00FE, -43120, 0, 105960, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0005 offset: 0x12BD
@scena.Code('func_05_12BD')
def func_05_12BD():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    OP_89(0x00FE, -38890, 3450, 120920, 180)
    ChrWalkTo(0x00FE, -38860, 3450, 117300, 5000, 0x00)
    ChrWalkTo(0x00FE, -38850, 0, 111640, 5000, 0x00)
    ChrWalkTo(0x00FE, -35560, 0, 105960, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0006 offset: 0x1321
@scena.Code('func_06_1321')
def func_06_1321():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    OP_89(0x00FE, -38890, 3450, 120920, 180)
    ChrWalkTo(0x00FE, -38860, 3450, 117300, 5000, 0x00)
    ChrWalkTo(0x00FE, -38850, 0, 111640, 5000, 0x00)
    ChrWalkTo(0x00FE, -41600, 0, 108320, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0007 offset: 0x1385
@scena.Code('func_07_1385')
def func_07_1385():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    OP_89(0x00FE, -38890, 3450, 120920, 180)
    ChrWalkTo(0x00FE, -38860, 3450, 117300, 5000, 0x00)
    ChrWalkTo(0x00FE, -38850, 0, 111640, 5000, 0x00)
    ChrWalkTo(0x00FE, -37390, 0, 108320, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0008 offset: 0x13E9
@scena.Code('func_08_13E9')
def func_08_13E9():
    ChrSetFlags(0x00FE, 0x0001)
    ChrWalkTo(0x00FE, -38860, 3450, 117300, 3000, 0x00)

    @scena.Lambda('lambda_1408')
    def lambda_1408():
        CameraSetDistance(4270, 2500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1408)

    ChrWalkTo(0x00FE, -38850, 0, 111640, 3000, 0x00)
    ChrWalkTo(0x00FE, -39500, 0, 107500, 3000, 0x00)

    Return()

# id: 0x0009 offset: 0x143B
@scena.Code('func_09_143B')
def func_09_143B():
    PlaySE(457, 0x01, 0x0A)
    Sleep(700)

    OP_24(0x01C9, 0x28)
    Sleep(300)

    OP_24(0x01C9, 0x32)
    Sleep(300)

    OP_24(0x01C9, 0x3C)
    Sleep(300)

    OP_24(0x01C9, 0x41)
    Sleep(300)

    OP_24(0x01C9, 0x46)
    Sleep(300)

    OP_24(0x01C9, 0x4B)
    Sleep(300)

    OP_24(0x01C9, 0x50)
    Sleep(300)

    OP_24(0x01C9, 0x55)
    Sleep(300)

    OP_24(0x01C9, 0x5A)
    Sleep(300)

    OP_24(0x01C9, 0x5F)
    Sleep(300)

    OP_24(0x01C9, 0x64)

    Return()

# id: 0x000A offset: 0x14A4
@scena.Code('func_0A_14A4')
def func_0A_14A4():
    Sleep(100)

    OP_24(0x01C9, 0x5F)
    Sleep(100)

    OP_24(0x01C9, 0x5A)
    Sleep(100)

    OP_24(0x01C9, 0x55)
    Sleep(100)

    OP_24(0x01C9, 0x50)
    Sleep(100)

    OP_24(0x01C9, 0x4B)
    Sleep(100)

    OP_24(0x01C9, 0x46)
    Sleep(100)

    OP_24(0x01C9, 0x3C)
    Sleep(100)

    OP_24(0x01C9, 0x32)
    Sleep(100)

    OP_24(0x01C9, 0x28)
    Sleep(100)

    OP_24(0x01C9, 0x01)

    Return()

# id: 0x000B offset: 0x14FF
@scena.Code('func_0B_14FF')
def func_0B_14FF():
    OP_B6(0x00)
    EventBegin(0x00)
    CameraMove(-38800, 0, 97110, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetPos(0x0010, -38880, 0, 82480, 0)
    ChrSetPos(0x000D, -38350, 0, 81550, 0)
    ChrSetPos(0x0011, -38350, 0, 80450, 0)
    ChrSetPos(0x0012, -38350, 0, 79350, 0)
    ChrSetPos(0x0013, -38350, 0, 78250, 0)
    ChrSetPos(0x0014, -38350, 0, 77150, 0)
    ChrSetPos(0x000E, -38350, 0, 76050, 0)
    ChrSetPos(0x000C, -39570, 0, 81550, 0)
    ChrSetPos(0x0015, -39570, 0, 80450, 0)
    ChrSetPos(0x0016, -39570, 0, 79350, 0)
    ChrSetPos(0x0017, -39570, 0, 78250, 0)
    ChrSetPos(0x0018, -39570, 0, 77150, 0)
    ChrSetPos(0x000F, -39570, 0, 76050, 0)
    FadeIn(2000, 0)
    CreateThread(0x0010, 0x01, 0x00, func_0C_17EC)
    CreateThread(0x000C, 0x01, 0x00, func_12_1924)
    CreateThread(0x000D, 0x01, 0x00, func_18_1A44)
    Sleep(100)

    CreateThread(0x0011, 0x01, 0x00, func_14_1984)
    CreateThread(0x0015, 0x01, 0x00, func_0E_1864)
    Sleep(100)

    CreateThread(0x0012, 0x01, 0x00, func_16_19E4)
    CreateThread(0x0016, 0x01, 0x00, func_10_18C4)
    Sleep(100)

    CreateThread(0x0013, 0x01, 0x00, func_15_19B4)
    CreateThread(0x0017, 0x01, 0x00, func_0F_1894)
    Sleep(100)

    CreateThread(0x0014, 0x01, 0x00, func_17_1A14)
    CreateThread(0x0018, 0x01, 0x00, func_11_18F4)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, func_13_1954)
    CreateThread(0x000F, 0x01, 0x00, func_0D_1834)

    @scena.Lambda('lambda_16EB')
    def lambda_16EB():
        CameraMove(-38550, 0, 106960, 6500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_16EB)

    @scena.Lambda('lambda_1703')
    def lambda_1703():
        OP_6E(405, 6500)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_1703)

    Sleep(2500)

    @scena.Lambda('lambda_1718')
    def lambda_1718():
        OP_67(0, 6530, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_1718)

    @scena.Lambda('lambda_1730')
    def lambda_1730():
        OP_6C(314000, 5000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1730)

    Sleep(5100)

    @scena.Lambda('lambda_1745')
    def lambda_1745():
        CameraMove(-36100, 0, 109830, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_1745)

    @scena.Lambda('lambda_175D')
    def lambda_175D():
        OP_67(0, 4320, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_175D)

    Sleep(4000)

    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x0010,
        (
            '#0100131052V#178F#5P好……\n',
            '各位，在此等候时机的到来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131053V正午钟响的同时就冲进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C4103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x17EC
@scena.Code('func_0C_17EC')
def func_0C_17EC():
    ChrWalkTo(0x00FE, -39060, 0, 99510, 4000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -32670, 0, 104380, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x1834
@scena.Code('func_0D_1834')
def func_0D_1834():
    ChrWalkTo(0x00FE, -39700, 0, 98070, 4000, 0x00)
    ChrWalkTo(0x00FE, -45260, 0, 107100, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x1864
@scena.Code('func_0E_1864')
def func_0E_1864():
    ChrWalkTo(0x00FE, -39700, 0, 98070, 4000, 0x00)
    ChrWalkTo(0x00FE, -46200, 0, 105950, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x1894
@scena.Code('func_0F_1894')
def func_0F_1894():
    ChrWalkTo(0x00FE, -39700, 0, 98070, 4000, 0x00)
    ChrWalkTo(0x00FE, -47250, 0, 105020, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x18C4
@scena.Code('func_10_18C4')
def func_10_18C4():
    ChrWalkTo(0x00FE, -39700, 0, 98070, 4000, 0x00)
    ChrWalkTo(0x00FE, -48520, 0, 104650, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0011 offset: 0x18F4
@scena.Code('func_11_18F4')
def func_11_18F4():
    ChrWalkTo(0x00FE, -39700, 0, 98070, 4000, 0x00)
    ChrWalkTo(0x00FE, -49750, 0, 104550, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x1924
@scena.Code('func_12_1924')
def func_12_1924():
    ChrWalkTo(0x00FE, -39700, 0, 98070, 4000, 0x00)
    ChrWalkTo(0x00FE, -50860, 0, 104450, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x1954
@scena.Code('func_13_1954')
def func_13_1954():
    ChrWalkTo(0x00FE, -38540, 0, 98020, 4000, 0x00)
    ChrWalkTo(0x00FE, -33180, 0, 107330, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x1984
@scena.Code('func_14_1984')
def func_14_1984():
    ChrWalkTo(0x00FE, -38540, 0, 98020, 4000, 0x00)
    ChrWalkTo(0x00FE, -32040, 0, 106360, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0015 offset: 0x19B4
@scena.Code('func_15_19B4')
def func_15_19B4():
    ChrWalkTo(0x00FE, -38540, 0, 98020, 4000, 0x00)
    ChrWalkTo(0x00FE, -30700, 0, 105110, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0016 offset: 0x19E4
@scena.Code('func_16_19E4')
def func_16_19E4():
    ChrWalkTo(0x00FE, -38540, 0, 98020, 4000, 0x00)
    ChrWalkTo(0x00FE, -29400, 0, 104310, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0017 offset: 0x1A14
@scena.Code('func_17_1A14')
def func_17_1A14():
    ChrWalkTo(0x00FE, -38540, 0, 98020, 4000, 0x00)
    ChrWalkTo(0x00FE, -27990, 0, 104210, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0018 offset: 0x1A44
@scena.Code('func_18_1A44')
def func_18_1A44():
    ChrWalkTo(0x00FE, -38540, 0, 98020, 4000, 0x00)
    ChrWalkTo(0x00FE, -26790, 0, 104310, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0019 offset: 0x1A74
@scena.Code('func_19_1A74')
def func_19_1A74():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　王都格兰赛尔',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001A offset: 0x1AB7
@scena.Code('func_1A_1AB7')
def func_1A_1AB7():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　格鲁纳门　　　１６５塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001B offset: 0x1B08
@scena.Code('func_1B_1B08')
def func_1B_1B08():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　圣海姆门　　　２２８塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
