import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4101.x'
    header.mapIndex       = 1
    header.bgm            = 21
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
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
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

# id: 0x10001 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '修女艾伦',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '魔兽',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '卡露娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 16,
            chipIndex           = 16,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '庭园大道方向',
            x                   = 62880,
            z                   = 0,
            y                   = 55500,
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
            name                = '艾尔贝离宫方向',
            x                   = -25910,
            z                   = 0,
            y                   = 25290,
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
            name                = '庭园大道方向',
            x                   = -107380,
            z                   = 0,
            y                   = -10960,
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

# id: 0x10002 offset: 0x522
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '凶暴巨鳄3',
            x           = 54960,
            z           = 20,
            y           = 1810,
            word_0C     = 0x0000,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0264,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔2',
            x           = 39700,
            z           = 70,
            y           = -19490,
            word_0C     = 0x0000,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0263,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '贪婪鳄鱼4',
            x           = 18160,
            z           = 10,
            y           = -7650,
            word_0C     = 0x0000,
            word_0E     = 0x001B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0265,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀3',
            x           = -32450,
            z           = 20,
            y           = -19130,
            word_0C     = 0x0000,
            word_0E     = 0x001F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0267,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫3',
            x           = -30720,
            z           = -20,
            y           = -16340,
            word_0C     = 0x0000,
            word_0E     = 0x0021,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0268,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x5AE
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 32110,
            y           = -1000,
            z           = -45500,
            range       = 35850,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF84AE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = -88800,
            y           = -1000,
            z           = -3040,
            range       = -85900,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFB7EE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 70260,
            y           = -1000,
            z           = 32570,
            range       = 56300,
            dword_10    = 0x000007D0,
            dword_14    = 0x00007602,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x60E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -18470,
            triggerZ            = 0,
            triggerY            = -5070,
            triggerRange        = 1500,
            actorX              = -18470,
            actorZ              = 1700,
            actorY              = -5070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9670,
            triggerZ            = 500,
            triggerY            = -54320,
            triggerRange        = 1500,
            actorX              = 9670,
            actorZ              = 4000,
            actorY              = -54320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x656
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_664',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_2E11)

    def _loc_664(): pass

    label('loc_664')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_672',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_04_3604)

    def _loc_672(): pass

    label('loc_672')

    Return()

# id: 0x0001 offset: 0x673
@scena.Code('func_01_673')
def func_01_673():
    OP_16(0x02, 4000, -140000, -140000, 196708)

    Return()

# id: 0x0002 offset: 0x686
@scena.Code('func_02_686')
def func_02_686():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 5, 0x615)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E10',
    )

    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 14740, 0, -49400, 225)
    ChrSetPos(0x0009, 12040, 0, -49370, 90)
    ChrSetPos(0x000A, 12070, 0, -51990, 45)
    ChrSetPos(0x000B, 14800, 0, -52250, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_06F2')
    def lambda_06F2():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_06F2')

    DispatchAsync2(0x0009, 0x0001, lambda_06F2)

    @scena.Lambda('lambda_0705')
    def lambda_0705():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0705')

    DispatchAsync2(0x000A, 0x0001, lambda_0705)

    @scena.Lambda('lambda_0718')
    def lambda_0718():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0718')

    DispatchAsync2(0x000B, 0x0001, lambda_0718)

    SetScenaFlags(ScenaFlag(0x00C2, 6, 0x616))
    OP_28(0x0046, 0x01, 0x0020)
    OP_28(0x0046, 0x01, 0x0040)
    OP_20(0x000005DC)

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0100101363V……呀啊啊～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x013F, 0)
    ChrTurnDirection(0x0102, 0x013F, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(86)

    ChrTalk(
        0x0101,
        (
            '#0010101364V#005F是女人的惨叫！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101365V#016F在这里面，赶快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07FD')
    def lambda_07FD():
        CameraMove(13190, 0, -50600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07FD)

    @scena.Lambda('lambda_0815')
    def lambda_0815():
        CameraSetDistance(3070, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0815)

    @scena.Lambda('lambda_0825')
    def lambda_0825():
        OP_6C(241000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0825)

    WaitForThreadExit(0x0101, 0x0002)
    FormationAddMember(0x3E, 0xFF)
    ChrClearFlags(0x013F, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x013F, 14740, 0, -49400, 225)
    ChrSetPos(0x0101, 20850, 0, -44670, 0)
    ChrSetPos(0x0102, 19400, 0, -43210, 0)
    OP_62(0x013F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101366V呀啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101367V救命啊！\n',
            '谁来救救我啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_08E6')
    def lambda_08E6():
        OP_92(0x00FE, 0x013F, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_08E6)

    Sleep(50)

    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_0905')
    def lambda_0905():
        OP_92(0x00FE, 0x013F, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0905)

    Sleep(100)

    ChrSetChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_0924')
    def lambda_0924():
        OP_92(0x00FE, 0x013F, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0924)

    Sleep(500)

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_0948')
    def lambda_0948():
        ChrWalkTo(0x00FE, 17790, 0, -47730, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0948)

    Sleep(300)

    @scena.Lambda('lambda_0968')
    def lambda_0968():
        ChrWalkTo(0x00FE, 13790, 0, -48820, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0968)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_098D')
    def lambda_098D():
        ChrJumpTo(0x00FE, 15230, 0, -50290, 1500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_098D)

    Sleep(200)

    TerminateThread(0x0102, 0xFF)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetFlags(0x0101, 0x1000)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_09C3')
    def lambda_09C3():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09C3)

    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_09D8')
    def lambda_09D8():
        ChrJumpTo(0x00FE, 13790, 0, -48820, 1500, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09D8)

    Sleep(200)

    ChrSetFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0102, 10)

    @scena.Lambda('lambda_0A05')
    def lambda_0A05():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0A05)

    Sleep(150)

    PlaySE(501, 0x00, 0x64)
    ChrSetChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_0A24')
    def lambda_0A24():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0A24')

    DispatchAsync2(0x000B, 0x0002, lambda_0A24)

    @scena.Lambda('lambda_0A37')
    def lambda_0A37():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 2000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A37)

    Sleep(100)

    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0A5F')
    def lambda_0A5F():
        ChrJumpToRelative(0x00FE, -2000, 0, 0, 2500, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A5F)

    @scena.Lambda('lambda_0A7D')
    def lambda_0A7D():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0A7D')

    DispatchAsync2(0x0009, 0x0002, lambda_0A7D)

    ChrTurnDirection(0x0101, 0x000B, 0)
    Sleep(150)

    ChrSetChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_0AA1')
    def lambda_0AA1():
        ChrJumpToRelative(0x00FE, -700, 0, -700, 1700, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0AA1)

    @scena.Lambda('lambda_0ABF')
    def lambda_0ABF():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0ABF')

    DispatchAsync2(0x000A, 0x0002, lambda_0ABF)

    WaitForThreadExit(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 3)

    @scena.Lambda('lambda_0ADC')
    def lambda_0ADC():
        ChrMoveTo(0x00FE, 14510, 0, -50410, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0ADC)

    WaitForThreadExit(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_0B01')
    def lambda_0B01():
        ChrMoveTo(0x00FE, 13780, 0, -49680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B01)

    Sleep(150)

    ChrTurnDirection(0x0102, 0x0009, 0)
    WaitForThreadExit(0x0101, 0x0001)

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101368V哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101369V#006F修女小姐，已经没事了！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101370V#012F很危险！\n',
            '请快点退到后面去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0BB5')
    def lambda_0BB5():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BB5)

    Sleep(50)

    TerminateThread(0x000A, 0xFF)
    ChrSetChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_0BD9')
    def lambda_0BD9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BD9)

    Sleep(50)

    TerminateThread(0x000B, 0xFF)
    ChrSetChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_0BFD')
    def lambda_0BFD():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BFD)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0C18')
    def lambda_0C18():
        ChrJumpTo(0x00FE, 14740, 0, -49400, 2000, 2600)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C18)

    Sleep(50)

    @scena.Lambda('lambda_0C3B')
    def lambda_0C3B():
        ChrJumpTo(0x00FE, 14740, 0, -49400, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C3B)

    Sleep(50)

    @scena.Lambda('lambda_0C5E')
    def lambda_0C5E():
        ChrJumpTo(0x00FE, 14740, 0, -49400, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C5E)

    Sleep(500)

    Battle(0x000003A3, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_C94'),
        (-1, 'loc_C97'),
    )

    def _loc_C94(): pass

    label('loc_C94')

    OP_B4(0x00)

    Return()

    def _loc_C97(): pass

    label('loc_C97')

    ChrSetStatus(0x0007, 0x00, 33)
    OP_B5(0x0007, 0x00)
    OP_B5(0x0007, 0x01)
    OP_B5(0x0007, 0x02)
    OP_B5(0x0007, 0x03)
    OP_B5(0x0007, 0x04)
    OP_B5(0x0007, 0x05)
    EquipCmd(0x07, 0x00D4)
    EquipCmd(0x07, 0x00F5)
    EquipCmd(0x07, 0x0113)
    EquipCmd(0x07, 0x0262, 0x00)
    EquipCmd(0x07, 0x0259, 0x01)
    EquipCmd(0x07, 0x025F, 0x02)
    EquipCmd(0x07, 0x0274, 0x03)
    AddCraft(0x0007, 0x00DC)
    AddCraft(0x0007, 0x00DD)
    AddCraft(0x0007, 0x00DE)
    AddCraft(0x0007, 0x00DF)
    AddSCraft(0x0007, 0x0109)
    AddSCraft(0x0007, 0x010A)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0108, 22520, 0, -37100, 0)
    ChrSetFlags(0x0108, 0x0080)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0101, 14390, 0, -50980, 225)
    ChrSetPos(0x0102, 12920, 0, -49800, 225)
    ChrSetPos(0x013F, 14740, 0, -49400, 225)
    CameraMove(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3070, 0)
    OP_6C(241000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    EventBegin(0x00)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010101371V#007F呼……\n',
            '真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x013F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101372V#006F修女小姐，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_0E12')
    def lambda_0E12():
        ChrTurnDirection(0x00FE, 0x013F, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E12)

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101373V啊，没事……多亏了你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101374V嗯……你们到底是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101375V#010F我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101376V在找人的途中听到了你的呼叫声，\n',
            '所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101377V是……这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101378V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101379V#580F怎、怎么了？\n',
            '看起来好像很没精神的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101380V难道受伤了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101381V没有……\n',
            '多亏了你们，我才平安无事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x013F,
        '修女',
        (
            '#0100101382V我是王都大圣堂的修女，\n',
            '名叫艾伦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013F,
        (
            '#0100101383V真是太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101384V#001F啊哈哈，不用谢啦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101385V#012F不过，作为圣职者的女性，\n',
            '孤身一人来这种地方似乎有点……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101386V您没有和其他人一起来吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013F,
        (
            '#0100101387V是的，只有我一个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013F,
        (
            '#0100101388V其实是因为大圣堂里调药用的\n',
            '草药没有了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013F,
        (
            '#0100101389V商店里也卖完了，\n',
            '所以我才来这里采集的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101390V#007F这也太危险了，\n',
            '明明到处都是魔兽啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013F,
        (
            '#0100101391V不是的……\n',
            '以前这里没有这么多魔兽的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013F,
        (
            '#0100101392V好像是从最近\n',
            '才突然开始增多的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x013F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x000005DC)
    ChrSetDirection(0x013F, 45, 600)

    ChrTalk(
        0x013F,
        (
            '#0100101393V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    PlayBGM(86)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    Sleep(500)

    @scena.Lambda('lambda_12A6')
    def lambda_12A6():
        ChrWalkTo(0x00FE, 15570, 0, -49480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_12A6)

    Sleep(100)

    @scena.Lambda('lambda_12C6')
    def lambda_12C6():
        ChrWalkTo(0x00FE, 14280, 0, -48510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_12C6)

    @scena.Lambda('lambda_12E1')
    def lambda_12E1():
        ChrMoveTo(0x00FE, 14210, 0, -50140, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013F, 0x0003, lambda_12E1)

    ChrSetPos(0x0009, 19840, 0, -40400, 0)
    ChrSetPos(0x000A, 21100, 0, -41220, 0)
    ChrSetPos(0x000B, 21440, 0, -39410, 0)
    ChrSetPos(0x000C, 21420, 0, -38390, 0)
    ChrSetPos(0x000D, 23130, 0, -39910, 0)
    ChrSetPos(0x000E, 21460, 0, -36780, 0)
    ChrSetPos(0x000F, 23510, 0, -37150, 0)
    ChrSetPos(0x0010, 24560, 0, -39000, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_13AC')
    def lambda_13AC():
        ChrWalkTo(0x00FE, 15280, 0, -45500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_13AC)

    @scena.Lambda('lambda_13C7')
    def lambda_13C7():
        ChrWalkTo(0x00FE, 17370, 0, -46170, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_13C7)

    @scena.Lambda('lambda_13E2')
    def lambda_13E2():
        ChrWalkTo(0x00FE, 16610, 0, -44960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13E2)

    @scena.Lambda('lambda_13FD')
    def lambda_13FD():
        ChrWalkTo(0x00FE, 16300, 0, -43340, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13FD)

    @scena.Lambda('lambda_1418')
    def lambda_1418():
        ChrWalkTo(0x00FE, 18970, 0, -44750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1418)

    @scena.Lambda('lambda_1433')
    def lambda_1433():
        ChrWalkTo(0x00FE, 17210, 0, -42380, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1433)

    @scena.Lambda('lambda_144E')
    def lambda_144E():
        ChrWalkTo(0x00FE, 19190, 0, -42290, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_144E)

    @scena.Lambda('lambda_1469')
    def lambda_1469():
        ChrWalkTo(0x00FE, 19060, 0, -43530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1469)

    @scena.Lambda('lambda_1484')
    def lambda_1484():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1484')

    DispatchAsync2(0x0009, 0x0002, lambda_1484)

    @scena.Lambda('lambda_1497')
    def lambda_1497():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1497')

    DispatchAsync2(0x000A, 0x0002, lambda_1497)

    Sleep(100)

    @scena.Lambda('lambda_14AF')
    def lambda_14AF():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_14AF')

    DispatchAsync2(0x000B, 0x0002, lambda_14AF)

    @scena.Lambda('lambda_14C2')
    def lambda_14C2():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_14C2')

    DispatchAsync2(0x000C, 0x0002, lambda_14C2)

    Sleep(100)

    @scena.Lambda('lambda_14DA')
    def lambda_14DA():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_14DA')

    DispatchAsync2(0x000D, 0x0002, lambda_14DA)

    @scena.Lambda('lambda_14ED')
    def lambda_14ED():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_14ED')

    DispatchAsync2(0x000E, 0x0002, lambda_14ED)

    Sleep(100)

    @scena.Lambda('lambda_1505')
    def lambda_1505():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1505')

    DispatchAsync2(0x000F, 0x0002, lambda_1505)

    @scena.Lambda('lambda_1518')
    def lambda_1518():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1518')

    DispatchAsync2(0x0010, 0x0002, lambda_1518)

    @scena.Lambda('lambda_152B')
    def lambda_152B():
        CameraMove(19250, 0, -43570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_152B)

    @scena.Lambda('lambda_1543')
    def lambda_1543():
        OP_6C(0, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1543)

    Sleep(1500)

    @scena.Lambda('lambda_1558')
    def lambda_1558():
        CameraMove(17110, 0, -45970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1558)

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010101394V#005F怎么回事啊，这些家伙们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101395V#012F好像是因为听到骚动而聚集过来了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101396V有这么多，还真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101397V#002F嗯，以防万一，\n',
            '至少先让修女小姐逃出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0108,
        '男性的声音',
        (
            '#0080101398V#3P哦，看起来你们遇到麻烦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0108, 0x0080)
    ChrSetPos(0x0108, 23450, 0, -37300, 225)

    @scena.Lambda('lambda_169A')
    def lambda_169A():
        CameraMove(17970, 0, -45090, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_169A)

    ChrSetChipByIndex(0x0108, 8)
    ChrSetFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_16BC')
    def lambda_16BC():
        ChrWalkTo(0x00FE, 21130, 0, -40520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_16BC)

    WaitForThreadExit(0x0108, 0x0001)
    Sleep(60)

    ChrSetFlags(0x0108, 0x0020)
    ChrSetChipByIndex(0x0108, 18)
    ChrSetFlags(0x0108, 0x0020)
    ChrSetFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_16F5')
    def lambda_16F5():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_16F5)

    ChrWalkTo(0x0108, 19670, 0, -41930, 8500, 0x00)
    PlaySE(507, 0x00, 0x64)
    PlaySE(521, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, 19660, 1000, -41900, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1758')
    def lambda_1758():
        ChrMoveTo(0x00FE, 17370, 0, -43990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1758)

    @scena.Lambda('lambda_1773')
    def lambda_1773():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_1773)

    Sleep(500)

    ChrJumpTo(0x0108, 20380, 0, -41250, 500, 5000)

    @scena.Lambda('lambda_17A1')
    def lambda_17A1():
        OP_99(0x00FE, 0x04, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_17A1)

    @scena.Lambda('lambda_17B1')
    def lambda_17B1():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_17B1)

    @scena.Lambda('lambda_17BF')
    def lambda_17BF():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_17BF)

    @scena.Lambda('lambda_17CD')
    def lambda_17CD():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_17CD)

    @scena.Lambda('lambda_17DB')
    def lambda_17DB():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_17DB)

    @scena.Lambda('lambda_17E9')
    def lambda_17E9():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_17E9)

    WaitForThreadExit(0x0108, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010101399V#501F#5P啊，金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101400V#010F#5P太好了……\n',
            '终于找到您了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101401V#070F哈哈，我还以为是谁，\n',
            '原来是你们两个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101402V总之，有话一会儿再说，\n',
            '赶快把这些家伙收拾掉吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101403V#006F#5P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101404V#010F#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0108, 0x0020)
    ChrClearFlags(0x0108, 0x1000)
    ChrSetChipByIndex(0x0108, 7)

    @scena.Lambda('lambda_1921')
    def lambda_1921():
        ChrWalkTo(0x00FE, 16750, 0, -47000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1921)

    @scena.Lambda('lambda_193C')
    def lambda_193C():
        OP_92(0x00FE, 0x000B, 600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_193C)

    @scena.Lambda('lambda_1951')
    def lambda_1951():
        ChrWalkTo(0x00FE, 18730, 0, -42670, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0003, lambda_1951)

    Sleep(400)

    Battle(0x000003A4, 0x00000000, 0x00, 0x0000, 0xFF)
    FormationDelMember(0x3E, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1987'),
        (-1, 'loc_198A'),
    )

    def _loc_1987(): pass

    label('loc_1987')

    OP_B4(0x00)

    Return()

    def _loc_198A(): pass

    label('loc_198A')

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    EventBegin(0x00)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 16770, 0, -47500, 45)
    ChrSetPos(0x0102, 15050, 0, -45990, 45)
    ChrSetPos(0x0108, 17690, 0, -44440, 225)
    ChrSetPos(0x0008, 14650, 0, -48360, 45)
    CameraMove(15920, 0, -45970, 0)
    OP_67(0, 5450, -10000, 0)
    CameraSetDistance(3690, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0108, 0x1000)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrClearFlags(0x0108, 0x0020)
    ChrClearFlags(0x0108, 0x1000)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080101405V#074F哎呀哎呀……\n',
            '多亏了这些家伙，让我好好地出了一次汗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101406V#070F不过话说回来，\n',
            '真没想到能在这里见到你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101407V你们不是在蔡斯地区工作吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101408V#506F啊哈哈～～\n',
            '确实从那时候起就一直没有像这样见面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101409V#010F#3P其实我们已经从蔡斯支部\n',
            '转属到王都格兰赛尔支部来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101410V#070F哦，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101411V也就是说，\n',
            '那个绑架事件已经解决了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101412V#071F那个中毒的红发小哥现在还好吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101413V#006F嗯，已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101414V……请问…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101415V#073F哦，真是失礼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080101416V#072F…………啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D42')
    def lambda_1D42():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_1D42')

    DispatchAsync2(0x0101, 0x0001, lambda_1D42)

    @scena.Lambda('lambda_1D53')
    def lambda_1D53():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1D53')

    DispatchAsync2(0x0108, 0x0001, lambda_1D53)

    ChrMoveTo(0x0108, 15730, 0, -45650, 3000, 0x00)
    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x0108,
        (
            '#0080101417V#070F（喂喂……\n',
            '　真是个美人啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101418V（是你们的同伴吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101419V#014F（不是，\n',
            '　我们也是刚认识的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101420V#007F真是的，这么色迷迷的，\n',
            '也不知道什么叫害羞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101421V#507F小心我去告诉雾香姐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0108, 0xFF)
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080101422V#073F哎呀……\n',
            '我只是陈述客观的事实罢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101423V#072F喂，我说艾丝蒂尔，\n',
            '为什么要提到那女人的名字啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 15080, 0, -47780, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0100101424V那个……把我从危险的地方救出来，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101425V你们都是我的救命恩人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FA7')
    def lambda_1FA7():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1FA7')

    DispatchAsync2(0x0108, 0x0001, lambda_1FA7)

    @scena.Lambda('lambda_1FB8')
    def lambda_1FB8():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_1FB8')

    DispatchAsync2(0x0102, 0x0001, lambda_1FB8)

    ChrMoveTo(0x0108, 15810, 0, -46820, 3000, 0x00)

    ChrTalk(
        0x0108,
        (
            '#0080101426V#071F#2P没什么没什么，请别放在心上！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101427V作为男人，就应该贯彻武侠之道嘛！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101428V哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 600)
    ChrWalkTo(0x0101, 16770, 0, -46200, 4000, 0x00)
    ChrWalkTo(0x0101, 15500, 0, -45360, 4000, 0x00)
    ChrTurnDirection(0x0101, 0x0108, 600)

    ChrTalk(
        0x0101,
        (
            '#0010101429V#506F（嘿嘿，好像在装帅呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101430V（金先生其实对女性是没有办法的。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101431V#019F（哈哈……说得没错。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0011, 27890, 0, -33290, 0)
    ChrSetPos(0x0012, 26890, 0, -32290, 0)

    NpcTalk(
        0x0011,
        '男人的声音',
        (
            '#2620101432V#3P你们在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_218A')
    def lambda_218A():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_218A)

    @scena.Lambda('lambda_2198')
    def lambda_2198():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2198)

    @scena.Lambda('lambda_21A6')
    def lambda_21A6():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_21A6)

    @scena.Lambda('lambda_21B4')
    def lambda_21B4():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_21B4)

    @scena.Lambda('lambda_21C2')
    def lambda_21C2():
        ChrWalkTo(0x00FE, 17460, 0, -43540, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_21C2)

    Sleep(200)

    @scena.Lambda('lambda_21E2')
    def lambda_21E2():
        ChrWalkTo(0x00FE, 18650, 0, -44020, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_21E2)

    CameraMove(17010, 0, -44670, 3000)

    @scena.Lambda('lambda_220E')
    def lambda_220E():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_220E')

    DispatchAsync2(0x0108, 0x0002, lambda_220E)

    @scena.Lambda('lambda_221F')
    def lambda_221F():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_221F')

    DispatchAsync2(0x0101, 0x0002, lambda_221F)

    @scena.Lambda('lambda_2230')
    def lambda_2230():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2230')

    DispatchAsync2(0x0102, 0x0002, lambda_2230)

    @scena.Lambda('lambda_2241')
    def lambda_2241():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2241')

    DispatchAsync2(0x0008, 0x0002, lambda_2241)

    ChrTalk(
        0x0101,
        (
            '#0010101433V#580F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101434V#012F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0011, 0x0001)

    ChrTalk(
        0x0011,
        (
            '#2620101435V在这种没人的地方密谈，\n',
            '真是可疑的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101436V#5P难道……\n',
            '你们是恐怖分子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 16770, 0, -46090, 4000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010101437V#005F谁、谁是恐怖分子啊！？\n',
            '我们是——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 16170, 0, -46090, 4000, 0x00)

    @scena.Lambda('lambda_2370')
    def lambda_2370():
        ChrWalkTo(0x00FE, 17150, 0, -46640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2370)

    ChrMoveTo(0x0102, 16770, 0, -46090, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020101438V#019F……我们是游击士协会\n',
            '格兰赛尔支部所属的成员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101439V就在刚才，\n',
            '我们保护了这位修女免遭魔兽袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101440V什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101441V#5P你们是游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 14980, 0, -46240, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0100101442V那个……\n',
            '他们说的都是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101443V我来这里采摘草药，\n',
            '结果被魔兽袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101444V#070F顺便一说，我也是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101445V我记得和你们的同僚\n',
            '在预选赛中曾经碰过面对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101446V卡尔瓦德的武术家……\n',
            '那个一个人参赛的家伙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101447V#5P哼……\n',
            '身份好像可以确定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101448V这次就放过你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101449V不过，这里离艾尔贝离宫很近。\n',
            '没事不要在这边乱转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101450V#5P还有，修女小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101451V#5P如果可以的话，\n',
            '我们把你送回王都去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101452V#5P有我们在就行了，\n',
            '不要借助什么游击士的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101453V哎，但、但是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010101454V#005F可恶，等一下，你们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101455V真是的……\n',
            '从刚才就一直在说些过分的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101456V#013F艾丝蒂尔……算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0011, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101457V#010F以后我们一定会注意的。\n',
            '这次真感谢你们能如此宽大地处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101458V哼，算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620101459V你们到底只不过是普通市民。\n',
            '弄清楚自己的本分就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630101460V#5P那么，修女小姐，我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100101461V好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrWalkTo(0x0008, 16450, 0, -44450, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0100101462V那个，各位……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 51, 400)

    @scena.Lambda('lambda_28E2')
    def lambda_28E2():
        OP_6C(20000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28E2)

    @scena.Lambda('lambda_28F2')
    def lambda_28F2():
        CameraMove(18100, 0, -44370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28F2)

    @scena.Lambda('lambda_290A')
    def lambda_290A():
        ChrMoveTo(0x00FE, 27890, 0, -33290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_290A)

    ChrSetDirection(0x0012, 51, 400)

    @scena.Lambda('lambda_292C')
    def lambda_292C():
        ChrMoveTo(0x00FE, 27890, 0, -33290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_292C)

    Sleep(200)

    @scena.Lambda('lambda_294C')
    def lambda_294C():
        ChrWalkTo(0x00FE, 27890, 0, -33290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_294C)

    Sleep(4000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    CameraMove(16870, 0, -45560, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010101463V#582F#2P什、什、什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101464V#005F#2P什么呀！那些家伙！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080101465V#070F他们是王国军情报部所属的\n',
            '『特务部队』的人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101466V虽然很厉害，\n',
            '不过都是些很阴险的家伙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A8F')
    def lambda_2A8F():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2A8F)

    Sleep(200)

    @scena.Lambda('lambda_2AA2')
    def lambda_2AA2():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AA2)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101467V#009F#2P与其说阴险，\n',
            '倒不如说是品行恶劣呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101468V#505F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101469V为什么金先生会知道他们的事情呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101470V#070F啊，武术大会的预选赛，\n',
            '他们的队伍也出场了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101471V那时就是这样介绍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010101472V#580F#2P（那些家伙也有出场……！？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101473V（平时进行地下活动那些家伙\n',
            '　这样堂堂正正地被人看到……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101474V#012F#5P（大概是已经没有\n',
            '　再隐藏自己存在的必要了吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101475V#074F总之，在被他们再次发现之前，\n',
            '我们还是赶快回城里去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101476V#073F……对了，\n',
            '你们为什么会在这里的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101477V#506F#2P啊……都忘了重要的事情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101478V#006F其实，我们是来找金先生你的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101479V#073F嗯？找我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101480V#010F#5P其实有件事情想拜托金先生。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101481V是有关武术大会的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2E10(): pass

    label('loc_2E10')

    Return()

# id: 0x0003 offset: 0x2E11
@scena.Code('func_03_2E11')
def func_03_2E11():
    EventBegin(0x00)
    ChrSetPos(0x0101, 11690, 0, -52560, 225)
    ChrSetPos(0x0102, 11000, 0, -51680, 225)
    ChrSetPos(0x0108, 10930, 0, -50240, 196)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0013, 14410, 0, -53900, 257)
    ChrSetPos(0x0014, 14820, 0, -52280, 244)
    ChrSetPos(0x0015, 13050, 0, -51640, 207)
    ChrSetPos(0x0016, 13090, 0, -50260, 213)
    CameraMove(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeIn(3000, 0)

    @scena.Lambda('lambda_2EEA')
    def lambda_2EEA():
        OP_6C(249000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2EEA)

    OP_6E(309, 5000)

    ChrTalk(
        0x0101,
        (
            '#000F嗯……\n',
            '这里就是集合点吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F在琥耀石的石碑旁的休息场所，\n',
            '和这里完全符合。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '问题是，尤莉亚中尉\n',
            '他们还没来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x0017, 17080, 0, -45130, 225)
    ChrSetPos(0x0018, 17100, 0, -43830, 225)
    ChrSetPos(0x0019, 18380, 0, -45010, 225)
    ChrSetPos(0x001A, 17740, 0, -42700, 225)
    ChrSetPos(0x001B, 18600, 0, -43670, 225)
    ChrSetPos(0x001C, 19480, 0, -44620, 225)
    ChrSetPos(0x001D, 18580, 0, -41840, 225)
    ChrSetPos(0x001E, 19520, 0, -42690, 225)
    ChrSetPos(0x001F, 20400, 0, -43690, 225)

    ChrTalk(
        0x0017,
        (
            '#0101060001V……请不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_306C')
    def lambda_306C():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_306C)

    @scena.Lambda('lambda_307A')
    def lambda_307A():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_307A)

    @scena.Lambda('lambda_3088')
    def lambda_3088():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3088)

    @scena.Lambda('lambda_3096')
    def lambda_3096():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3096)

    @scena.Lambda('lambda_30A4')
    def lambda_30A4():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_30A4)

    @scena.Lambda('lambda_30B2')
    def lambda_30B2():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_30B2)

    @scena.Lambda('lambda_30C0')
    def lambda_30C0():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_30C0)

    @scena.Lambda('lambda_30CE')
    def lambda_30CE():
        OP_6C(335000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_30CE)

    @scena.Lambda('lambda_30DE')
    def lambda_30DE():
        CameraMove(14730, 0, -48030, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_30DE)

    @scena.Lambda('lambda_30F6')
    def lambda_30F6():
        OP_6E(332, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_30F6)

    Sleep(2000)

    @scena.Lambda('lambda_310B')
    def lambda_310B():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_310B)

    Sleep(100)

    @scena.Lambda('lambda_312B')
    def lambda_312B():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_312B)

    @scena.Lambda('lambda_3146')
    def lambda_3146():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3146)

    Sleep(100)

    @scena.Lambda('lambda_3166')
    def lambda_3166():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_3166)

    @scena.Lambda('lambda_3181')
    def lambda_3181():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_3181)

    @scena.Lambda('lambda_319C')
    def lambda_319C():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_319C)

    Sleep(100)

    @scena.Lambda('lambda_31BC')
    def lambda_31BC():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_31BC)

    @scena.Lambda('lambda_31D7')
    def lambda_31D7():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_31D7)

    @scena.Lambda('lambda_31F2')
    def lambda_31F2():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_31F2)

    CameraMove(13880, 0, -49890, 4000)

    ChrTalk(
        0x0101,
        (
            '#000F哇，什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，有这么多人\n',
            '都能够潜伏在王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#170F在支持我们人当中，\n',
            '市民也是占大多数的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们这边已经准备好了，\n',
            '随时可以开始作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0016, 0x0101, 400)

    ChrTalk(
        0x0016,
        (
            '艾丝蒂尔，\n',
            '请发号施令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_32F6')
    def lambda_32F6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_32F6)

    @scena.Lambda('lambda_3304')
    def lambda_3304():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3304)

    @scena.Lambda('lambda_3312')
    def lambda_3312():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3312)

    @scena.Lambda('lambda_3320')
    def lambda_3320():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3320)

    @scena.Lambda('lambda_332E')
    def lambda_332E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_332E)

    @scena.Lambda('lambda_333C')
    def lambda_333C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_333C)

    ChrTalk(
        0x0101,
        (
            '#000F咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130543V我、我来！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '因为是由你们\n',
            '接受女王委托的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '啊，由你来发号施令\n',
            '是理所当然的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F可、可是……\n',
            '我还只是个新人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '哈哈，没关系。\n',
            '由你来我们没有异议的哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '只是注意要\n',
            '大声一点，好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#170F我们是来帮忙的，\n',
            '绝对不会有半点异议呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔，要有自信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F不用再细想了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130553V这可是老规矩了，老规矩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_350D')
    def lambda_350D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_350D')

    DispatchAsync2(0x0102, 0x0001, lambda_350D)

    @scena.Lambda('lambda_351E')
    def lambda_351E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_351E')

    DispatchAsync2(0x0108, 0x0001, lambda_351E)

    @scena.Lambda('lambda_352F')
    def lambda_352F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_352F')

    DispatchAsync2(0x0013, 0x0001, lambda_352F)

    @scena.Lambda('lambda_3540')
    def lambda_3540():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3540')

    DispatchAsync2(0x0014, 0x0001, lambda_3540)

    @scena.Lambda('lambda_3551')
    def lambda_3551():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3551')

    DispatchAsync2(0x0015, 0x0001, lambda_3551)

    @scena.Lambda('lambda_3562')
    def lambda_3562():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3562')

    DispatchAsync2(0x0016, 0x0001, lambda_3562)

    @scena.Lambda('lambda_3573')
    def lambda_3573():
        OP_6C(0, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3573)

    ChrWalkTo(0x0101, 10610, 480, -53440, 600, 0x00)
    ChrSetDirection(0x0101, 45, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#000F我向全体作战成员宣布……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾尔贝离宫攻略战，\n',
            '暨人质解救作战现在开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x3604
@scena.Code('func_04_3604')
def func_04_3604():
    EventBegin(0x00)
    CameraMove(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x0018, -25890, 0, -4510, 180)
    ChrSetPos(0x0019, -27370, 0, -4510, 180)
    ChrSetPos(0x001A, -27240, 0, -2700, 180)
    ChrSetPos(0x001B, -25950, 0, -2920, 180)
    ChrSetPos(0x0101, -26570, 0, -6220, 0)
    ChrSetPos(0x0102, -28030, 0, -6250, 45)
    ChrSetPos(0x0108, -25360, 0, -6190, 313)

    ChrTalk(
        0x0108,
        (
            '#070F好，伏击组开始行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '我们先行一步，\n',
            '去引开前庭的残存兵力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '趁此机会，请你们\n',
            '突入离宫内部！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130994V#010F愿女神保佑你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3783')
    def lambda_3783():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_3783')

    DispatchAsync2(0x0101, 0x0001, lambda_3783)

    @scena.Lambda('lambda_3794')
    def lambda_3794():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_3794')

    DispatchAsync2(0x0102, 0x0001, lambda_3794)

    @scena.Lambda('lambda_37A5')
    def lambda_37A5():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_37A5')

    DispatchAsync2(0x0108, 0x0001, lambda_37A5)

    @scena.Lambda('lambda_37B6')
    def lambda_37B6():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_37B6)

    Sleep(100)

    @scena.Lambda('lambda_37D6')
    def lambda_37D6():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_37D6)

    Sleep(200)

    @scena.Lambda('lambda_37F6')
    def lambda_37F6():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_37F6)

    Sleep(100)

    @scena.Lambda('lambda_3816')
    def lambda_3816():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3816)

    Sleep(2000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    SetScenaFlags(ScenaFlag(0x00CA, 1, 0x651))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x3856
@scena.Code('func_05_3856')
def func_05_3856():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_39CD',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38CE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130520V#002F……在突击的时刻是不能退缩的。\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130521V立刻赶去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39B2')

    def _loc_38CE(): pass

    label('loc_38CE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3935',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130522V#012F要突击也只有趁现在了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130523V赶快去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39B2')

    def _loc_3935(): pass

    label('loc_3935')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39B2',
    )

    ChrTurnDirection(0x0108, 0x0001, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130524V#072F如果现在不行动的话，\n',
            '就没有突入离宫的机会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130525V……赶快去艾尔贝离宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39B2(): pass

    label('loc_39B2')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_39CD(): pass

    label('loc_39CD')

    Return()

# id: 0x0006 offset: 0x39CE
@scena.Code('func_06_39CE')
def func_06_39CE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B46',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A47',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130520V#002F……在突击的时刻是不能退缩的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130521V立刻赶去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B2B')

    def _loc_3A47(): pass

    label('loc_3A47')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AAE',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130522V#012F要突击也只有趁现在了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130523V赶快去艾尔贝离宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B2B')

    def _loc_3AAE(): pass

    label('loc_3AAE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B2B',
    )

    ChrTurnDirection(0x0108, 0x0001, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130524V#072F如果现在不行动的话，\n',
            '就没有突入离宫的机会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130525V……赶快去艾尔贝离宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B2B(): pass

    label('loc_3B2B')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3B46(): pass

    label('loc_3B46')

    Return()

# id: 0x0007 offset: 0x3B47
@scena.Code('func_07_3B47')
def func_07_3B47():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　艾尔贝离宫\n',
            '西　圣海姆门　　２２４塞尔矩\n',
            '东　格鲁纳门　　２５６塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x3BC2
@scena.Code('func_08_3BC2')
def func_08_3BC2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的琥耀石石碑。',
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
