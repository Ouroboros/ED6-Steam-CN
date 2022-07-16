import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '修女艾伦'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '魔兽'),
    TXT(0x07, '魔兽'),
    TXT(0x08, '魔兽'),
    TXT(0x09, '魔兽'),
    TXT(0x0A, '特务兵'),
    TXT(0x0B, '特务兵'),
    TXT(0x0C, '卡露娜'),
    TXT(0x0D, '亚妮拉丝'),
    TXT(0x0E, '库拉茨'),
    TXT(0x0F, '克鲁茨'),
    TXT(0x10, '尤莉亚中尉'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '亲卫队员'),
    TXT(0x15, '亲卫队员'),
    TXT(0x16, '亲卫队员'),
    TXT(0x17, '亲卫队员'),
    TXT(0x18, '亲卫队员'),
    TXT(0x19, '庭园大道方向'),
    TXT(0x1A, '艾尔贝离宫方向'),
    TXT(0x1B, '庭园大道方向'),
    TXT(0x1C, '凶暴巨鳄3'),
    TXT(0x1D, '沼泽剑齿吸血魔2'),
    TXT(0x1E, '贪婪鳄鱼4'),
    TXT(0x1F, '地狱火爆麻雀3'),
    TXT(0x20, '迅猛小鹫3'),
    TXT(0x21, ''),
]

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

# id: 0xFFFF offset: 0x3973
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

# id: 0x10002 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x522
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
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

# id: 0x10004 offset: 0x5AE
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

# id: 0x10005 offset: 0x60E
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
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_664',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

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
    Event(0, 0x0004)

    def _loc_672(): pass

    label('loc_672')

    Return()

# id: 0x0001 offset: 0x673
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -140000, -140000, 196708)

    Return()

# id: 0x0002 offset: 0x686
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 5, 0x615)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2BBD',
    )

    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 14740, 0, -49400, 225)
    SetChrPos(0x0009, 12040, 0, -49370, 90)
    SetChrPos(0x000A, 12070, 0, -51990, 45)
    SetChrPos(0x000B, 14800, 0, -52250, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

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

    @scena.Lambda('lambda_07EE')
    def lambda_07EE():
        CameraMove(13190, 0, -50600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07EE)

    @scena.Lambda('lambda_0806')
    def lambda_0806():
        CameraSetDistance(3070, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0806)

    @scena.Lambda('lambda_0816')
    def lambda_0816():
        OP_6C(241000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0816)

    WaitForThreadExit(0x0101, 0x0002)
    FormationAddMember(0x3E, 0xFF)
    ClearChrFlags(0x013F, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrPos(0x013F, 14740, 0, -49400, 225)
    SetChrPos(0x0101, 20850, 0, -44670, 0)
    SetChrPos(0x0102, 19400, 0, -43210, 0)
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
    SetChrChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_08CD')
    def lambda_08CD():
        OP_92(0x00FE, 0x013F, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_08CD)

    Sleep(50)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_08EC')
    def lambda_08EC():
        OP_92(0x00FE, 0x013F, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_08EC)

    Sleep(100)

    SetChrChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_090B')
    def lambda_090B():
        OP_92(0x00FE, 0x013F, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_090B)

    Sleep(500)

    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_092F')
    def lambda_092F():
        ChrWalkTo(0x00FE, 17790, 0, -47730, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_092F)

    Sleep(300)

    @scena.Lambda('lambda_094F')
    def lambda_094F():
        ChrWalkTo(0x00FE, 13790, 0, -48820, 8500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_094F)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0974')
    def lambda_0974():
        ChrJumpTo(0x00FE, 15230, 0, -50290, 1500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0974)

    Sleep(200)

    TerminateThread(0x0102, 0xFF)
    SetChrChipByIndex(0x0101, 10)
    SetChrFlags(0x0101, 0x1000)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_09AA')
    def lambda_09AA():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09AA)

    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_09BF')
    def lambda_09BF():
        ChrJumpTo(0x00FE, 13790, 0, -48820, 1500, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09BF)

    Sleep(200)

    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0102, 10)

    @scena.Lambda('lambda_09EC')
    def lambda_09EC():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_09EC)

    Sleep(150)

    PlaySE(501, 0x00, 0x64)
    SetChrChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_0A0B')
    def lambda_0A0B():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0A0B')

    DispatchAsync2(0x000B, 0x0002, lambda_0A0B)

    @scena.Lambda('lambda_0A1E')
    def lambda_0A1E():
        ChrJumpToRelative(0x00FE, 0, 0, -2000, 2000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A1E)

    Sleep(100)

    SetChrChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0A46')
    def lambda_0A46():
        ChrJumpToRelative(0x00FE, -2000, 0, 0, 2500, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A46)

    @scena.Lambda('lambda_0A64')
    def lambda_0A64():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0A64')

    DispatchAsync2(0x0009, 0x0002, lambda_0A64)

    ChrTurnDirection(0x0101, 0x000B, 0)
    Sleep(150)

    SetChrChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_0A88')
    def lambda_0A88():
        ChrJumpToRelative(0x00FE, -700, 0, -700, 1700, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A88)

    @scena.Lambda('lambda_0AA6')
    def lambda_0AA6():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0AA6')

    DispatchAsync2(0x000A, 0x0002, lambda_0AA6)

    WaitForThreadExit(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 3)

    @scena.Lambda('lambda_0AC3')
    def lambda_0AC3():
        ChrMoveTo(0x00FE, 14510, 0, -50410, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AC3)

    WaitForThreadExit(0x0102, 0x0002)
    SetChrChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_0AE8')
    def lambda_0AE8():
        ChrMoveTo(0x00FE, 13780, 0, -49680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0AE8)

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
    SetChrChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0B8D')
    def lambda_0B8D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B8D)

    Sleep(50)

    TerminateThread(0x000A, 0xFF)
    SetChrChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_0BB1')
    def lambda_0BB1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BB1)

    Sleep(50)

    TerminateThread(0x000B, 0xFF)
    SetChrChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_0BD5')
    def lambda_0BD5():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BD5)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0BF0')
    def lambda_0BF0():
        ChrJumpTo(0x00FE, 14740, 0, -49400, 2000, 2600)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BF0)

    Sleep(50)

    @scena.Lambda('lambda_0C13')
    def lambda_0C13():
        ChrJumpTo(0x00FE, 14740, 0, -49400, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C13)

    Sleep(50)

    @scena.Lambda('lambda_0C36')
    def lambda_0C36():
        ChrJumpTo(0x00FE, 14740, 0, -49400, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C36)

    Sleep(500)

    Battle(0x000003A3, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_C6C'),
        (-1, 'loc_C6F'),
    )

    def _loc_C6C(): pass

    label('loc_C6C')

    OP_B4(0x00)

    Return()

    def _loc_C6F(): pass

    label('loc_C6F')

    SetChrStatus(0x0007, 0x00, 33)
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
    SetChrPos(0x0108, 22520, 0, -37100, 0)
    SetChrFlags(0x0108, 0x0080)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0101, 14390, 0, -50980, 225)
    SetChrPos(0x0102, 12920, 0, -49800, 225)
    SetChrPos(0x013F, 14740, 0, -49400, 225)
    CameraMove(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3070, 0)
    OP_6C(241000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)
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
    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x013F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101372V#006F修女小姐，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_0DE0')
    def lambda_0DE0():
        ChrTurnDirection(0x00FE, 0x013F, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0DE0)

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
    SetChrDirection(0x013F, 45, 600)

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
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    Sleep(500)

    @scena.Lambda('lambda_120B')
    def lambda_120B():
        ChrWalkTo(0x00FE, 15570, 0, -49480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_120B)

    Sleep(100)

    @scena.Lambda('lambda_122B')
    def lambda_122B():
        ChrWalkTo(0x00FE, 14280, 0, -48510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_122B)

    @scena.Lambda('lambda_1246')
    def lambda_1246():
        ChrMoveTo(0x00FE, 14210, 0, -50140, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013F, 0x0003, lambda_1246)

    SetChrPos(0x0009, 19840, 0, -40400, 0)
    SetChrPos(0x000A, 21100, 0, -41220, 0)
    SetChrPos(0x000B, 21440, 0, -39410, 0)
    SetChrPos(0x000C, 21420, 0, -38390, 0)
    SetChrPos(0x000D, 23130, 0, -39910, 0)
    SetChrPos(0x000E, 21460, 0, -36780, 0)
    SetChrPos(0x000F, 23510, 0, -37150, 0)
    SetChrPos(0x0010, 24560, 0, -39000, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_1311')
    def lambda_1311():
        ChrWalkTo(0x00FE, 15280, 0, -45500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1311)

    @scena.Lambda('lambda_132C')
    def lambda_132C():
        ChrWalkTo(0x00FE, 17370, 0, -46170, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_132C)

    @scena.Lambda('lambda_1347')
    def lambda_1347():
        ChrWalkTo(0x00FE, 16610, 0, -44960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1347)

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        ChrWalkTo(0x00FE, 16300, 0, -43340, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1362)

    @scena.Lambda('lambda_137D')
    def lambda_137D():
        ChrWalkTo(0x00FE, 18970, 0, -44750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_137D)

    @scena.Lambda('lambda_1398')
    def lambda_1398():
        ChrWalkTo(0x00FE, 17210, 0, -42380, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1398)

    @scena.Lambda('lambda_13B3')
    def lambda_13B3():
        ChrWalkTo(0x00FE, 19190, 0, -42290, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_13B3)

    @scena.Lambda('lambda_13CE')
    def lambda_13CE():
        ChrWalkTo(0x00FE, 19060, 0, -43530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_13CE)

    @scena.Lambda('lambda_13E9')
    def lambda_13E9():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_13E9')

    DispatchAsync2(0x0009, 0x0002, lambda_13E9)

    @scena.Lambda('lambda_13FC')
    def lambda_13FC():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_13FC')

    DispatchAsync2(0x000A, 0x0002, lambda_13FC)

    Sleep(100)

    @scena.Lambda('lambda_1414')
    def lambda_1414():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1414')

    DispatchAsync2(0x000B, 0x0002, lambda_1414)

    @scena.Lambda('lambda_1427')
    def lambda_1427():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1427')

    DispatchAsync2(0x000C, 0x0002, lambda_1427)

    Sleep(100)

    @scena.Lambda('lambda_143F')
    def lambda_143F():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_143F')

    DispatchAsync2(0x000D, 0x0002, lambda_143F)

    @scena.Lambda('lambda_1452')
    def lambda_1452():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1452')

    DispatchAsync2(0x000E, 0x0002, lambda_1452)

    Sleep(100)

    @scena.Lambda('lambda_146A')
    def lambda_146A():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_146A')

    DispatchAsync2(0x000F, 0x0002, lambda_146A)

    @scena.Lambda('lambda_147D')
    def lambda_147D():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_147D')

    DispatchAsync2(0x0010, 0x0002, lambda_147D)

    @scena.Lambda('lambda_1490')
    def lambda_1490():
        CameraMove(19250, 0, -43570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1490)

    @scena.Lambda('lambda_14A8')
    def lambda_14A8():
        OP_6C(0, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_14A8)

    Sleep(1500)

    @scena.Lambda('lambda_14BD')
    def lambda_14BD():
        CameraMove(17110, 0, -45970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14BD)

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
    ClearChrFlags(0x0108, 0x0080)
    SetChrPos(0x0108, 23450, 0, -37300, 225)

    @scena.Lambda('lambda_15E6')
    def lambda_15E6():
        CameraMove(17970, 0, -45090, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15E6)

    SetChrChipByIndex(0x0108, 8)
    SetChrFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_1608')
    def lambda_1608():
        ChrWalkTo(0x00FE, 21130, 0, -40520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1608)

    WaitForThreadExit(0x0108, 0x0001)
    Sleep(60)

    SetChrFlags(0x0108, 0x0020)
    SetChrChipByIndex(0x0108, 18)
    SetChrFlags(0x0108, 0x0020)
    SetChrFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_1641')
    def lambda_1641():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1641)

    ChrWalkTo(0x0108, 19670, 0, -41930, 8500, 0x00)
    PlaySE(507, 0x00, 0x64)
    PlaySE(521, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, 19660, 1000, -41900, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_16A4')
    def lambda_16A4():
        ChrMoveTo(0x00FE, 17370, 0, -43990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_16A4)

    @scena.Lambda('lambda_16BF')
    def lambda_16BF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_16BF)

    Sleep(500)

    ChrJumpTo(0x0108, 20380, 0, -41250, 500, 5000)

    @scena.Lambda('lambda_16ED')
    def lambda_16ED():
        OP_99(0x00FE, 0x04, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_16ED)

    @scena.Lambda('lambda_16FD')
    def lambda_16FD():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_16FD)

    @scena.Lambda('lambda_170B')
    def lambda_170B():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_170B)

    @scena.Lambda('lambda_1719')
    def lambda_1719():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1719)

    @scena.Lambda('lambda_1727')
    def lambda_1727():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1727)

    @scena.Lambda('lambda_1735')
    def lambda_1735():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1735)

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
    ClearChrFlags(0x0108, 0x0020)
    ClearChrFlags(0x0108, 0x1000)
    SetChrChipByIndex(0x0108, 7)

    @scena.Lambda('lambda_184F')
    def lambda_184F():
        ChrWalkTo(0x00FE, 16750, 0, -47000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_184F)

    @scena.Lambda('lambda_186A')
    def lambda_186A():
        OP_92(0x00FE, 0x000B, 600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_186A)

    @scena.Lambda('lambda_187F')
    def lambda_187F():
        ChrWalkTo(0x00FE, 18730, 0, -42670, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0003, lambda_187F)

    Sleep(400)

    Battle(0x000003A4, 0x00000000, 0x00, 0x0000, 0xFF)
    FormationDelMember(0x3E, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_18B5'),
        (-1, 'loc_18B8'),
    )

    def _loc_18B5(): pass

    label('loc_18B5')

    OP_B4(0x00)

    Return()

    def _loc_18B8(): pass

    label('loc_18B8')

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
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0101, 16770, 0, -47500, 45)
    SetChrPos(0x0102, 15050, 0, -45990, 45)
    SetChrPos(0x0108, 17690, 0, -44440, 225)
    SetChrPos(0x0008, 14650, 0, -48360, 45)
    CameraMove(15920, 0, -45970, 0)
    OP_67(0, 5450, -10000, 0)
    CameraSetDistance(3690, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0108, 0x1000)

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

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    ClearChrFlags(0x0108, 0x0020)
    ClearChrFlags(0x0108, 0x1000)
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

    @scena.Lambda('lambda_1C34')
    def lambda_1C34():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_1C34')

    DispatchAsync2(0x0101, 0x0001, lambda_1C34)

    @scena.Lambda('lambda_1C45')
    def lambda_1C45():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1C45')

    DispatchAsync2(0x0108, 0x0001, lambda_1C45)

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

    @scena.Lambda('lambda_1E6C')
    def lambda_1E6C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1E6C')

    DispatchAsync2(0x0108, 0x0001, lambda_1E6C)

    @scena.Lambda('lambda_1E7D')
    def lambda_1E7D():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_1E7D')

    DispatchAsync2(0x0102, 0x0001, lambda_1E7D)

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
    SetChrDirection(0x0101, 0, 600)
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
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0011, 27890, 0, -33290, 0)
    SetChrPos(0x0012, 26890, 0, -32290, 0)

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

    @scena.Lambda('lambda_202C')
    def lambda_202C():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_202C)

    @scena.Lambda('lambda_203A')
    def lambda_203A():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_203A)

    @scena.Lambda('lambda_2048')
    def lambda_2048():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2048)

    @scena.Lambda('lambda_2056')
    def lambda_2056():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2056)

    @scena.Lambda('lambda_2064')
    def lambda_2064():
        ChrWalkTo(0x00FE, 17460, 0, -43540, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2064)

    Sleep(200)

    @scena.Lambda('lambda_2084')
    def lambda_2084():
        ChrWalkTo(0x00FE, 18650, 0, -44020, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2084)

    CameraMove(17010, 0, -44670, 3000)

    @scena.Lambda('lambda_20B0')
    def lambda_20B0():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_20B0')

    DispatchAsync2(0x0108, 0x0002, lambda_20B0)

    @scena.Lambda('lambda_20C1')
    def lambda_20C1():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_20C1')

    DispatchAsync2(0x0101, 0x0002, lambda_20C1)

    @scena.Lambda('lambda_20D2')
    def lambda_20D2():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_20D2')

    DispatchAsync2(0x0102, 0x0002, lambda_20D2)

    @scena.Lambda('lambda_20E3')
    def lambda_20E3():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_20E3')

    DispatchAsync2(0x0008, 0x0002, lambda_20E3)

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

    @scena.Lambda('lambda_21F9')
    def lambda_21F9():
        ChrWalkTo(0x00FE, 17150, 0, -46640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21F9)

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
    SetChrDirection(0x0011, 51, 400)

    @scena.Lambda('lambda_26EE')
    def lambda_26EE():
        OP_6C(20000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_26EE)

    @scena.Lambda('lambda_26FE')
    def lambda_26FE():
        CameraMove(18100, 0, -44370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_26FE)

    @scena.Lambda('lambda_2716')
    def lambda_2716():
        ChrMoveTo(0x00FE, 27890, 0, -33290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2716)

    SetChrDirection(0x0012, 51, 400)

    @scena.Lambda('lambda_2738')
    def lambda_2738():
        ChrMoveTo(0x00FE, 27890, 0, -33290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2738)

    Sleep(200)

    @scena.Lambda('lambda_2758')
    def lambda_2758():
        ChrWalkTo(0x00FE, 27890, 0, -33290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2758)

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

    @scena.Lambda('lambda_2887')
    def lambda_2887():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2887)

    Sleep(200)

    @scena.Lambda('lambda_289A')
    def lambda_289A():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_289A)

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

    def _loc_2BBD(): pass

    label('loc_2BBD')

    Return()

# id: 0x0003 offset: 0x2BBE
@scena.Code('func_03_2BBE')
def func_03_2BBE():
    EventBegin(0x00)
    SetChrPos(0x0101, 11690, 0, -52560, 225)
    SetChrPos(0x0102, 11000, 0, -51680, 225)
    SetChrPos(0x0108, 10930, 0, -50240, 196)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0013, 14410, 0, -53900, 257)
    SetChrPos(0x0014, 14820, 0, -52280, 244)
    SetChrPos(0x0015, 13050, 0, -51640, 207)
    SetChrPos(0x0016, 13090, 0, -50260, 213)
    CameraMove(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeIn(3000, 0)

    @scena.Lambda('lambda_2C97')
    def lambda_2C97():
        OP_6C(249000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C97)

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
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x0017, 17080, 0, -45130, 225)
    SetChrPos(0x0018, 17100, 0, -43830, 225)
    SetChrPos(0x0019, 18380, 0, -45010, 225)
    SetChrPos(0x001A, 17740, 0, -42700, 225)
    SetChrPos(0x001B, 18600, 0, -43670, 225)
    SetChrPos(0x001C, 19480, 0, -44620, 225)
    SetChrPos(0x001D, 18580, 0, -41840, 225)
    SetChrPos(0x001E, 19520, 0, -42690, 225)
    SetChrPos(0x001F, 20400, 0, -43690, 225)

    ChrTalk(
        0x0017,
        (
            '#0101060001V……请不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E14')
    def lambda_2E14():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E14)

    @scena.Lambda('lambda_2E22')
    def lambda_2E22():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E22)

    @scena.Lambda('lambda_2E30')
    def lambda_2E30():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2E30)

    @scena.Lambda('lambda_2E3E')
    def lambda_2E3E():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2E3E)

    @scena.Lambda('lambda_2E4C')
    def lambda_2E4C():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2E4C)

    @scena.Lambda('lambda_2E5A')
    def lambda_2E5A():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_2E5A)

    @scena.Lambda('lambda_2E68')
    def lambda_2E68():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_2E68)

    @scena.Lambda('lambda_2E76')
    def lambda_2E76():
        OP_6C(335000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2E76)

    @scena.Lambda('lambda_2E86')
    def lambda_2E86():
        CameraMove(14730, 0, -48030, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E86)

    @scena.Lambda('lambda_2E9E')
    def lambda_2E9E():
        OP_6E(332, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2E9E)

    Sleep(2000)

    @scena.Lambda('lambda_2EB3')
    def lambda_2EB3():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_2EB3)

    Sleep(100)

    @scena.Lambda('lambda_2ED3')
    def lambda_2ED3():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_2ED3)

    @scena.Lambda('lambda_2EEE')
    def lambda_2EEE():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_2EEE)

    Sleep(100)

    @scena.Lambda('lambda_2F0E')
    def lambda_2F0E():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_2F0E)

    @scena.Lambda('lambda_2F29')
    def lambda_2F29():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2F29)

    @scena.Lambda('lambda_2F44')
    def lambda_2F44():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2F44)

    Sleep(100)

    @scena.Lambda('lambda_2F64')
    def lambda_2F64():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_2F64)

    @scena.Lambda('lambda_2F7F')
    def lambda_2F7F():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_2F7F)

    @scena.Lambda('lambda_2F9A')
    def lambda_2F9A():
        ChrMoveToRelative(0x00FE, -2000, 0, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2F9A)

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

    @scena.Lambda('lambda_309E')
    def lambda_309E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_309E)

    @scena.Lambda('lambda_30AC')
    def lambda_30AC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_30AC)

    @scena.Lambda('lambda_30BA')
    def lambda_30BA():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_30BA)

    @scena.Lambda('lambda_30C8')
    def lambda_30C8():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_30C8)

    @scena.Lambda('lambda_30D6')
    def lambda_30D6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_30D6)

    @scena.Lambda('lambda_30E4')
    def lambda_30E4():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_30E4)

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

    @scena.Lambda('lambda_32AB')
    def lambda_32AB():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_32AB')

    DispatchAsync2(0x0102, 0x0001, lambda_32AB)

    @scena.Lambda('lambda_32BC')
    def lambda_32BC():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_32BC')

    DispatchAsync2(0x0108, 0x0001, lambda_32BC)

    @scena.Lambda('lambda_32CD')
    def lambda_32CD():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_32CD')

    DispatchAsync2(0x0013, 0x0001, lambda_32CD)

    @scena.Lambda('lambda_32DE')
    def lambda_32DE():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_32DE')

    DispatchAsync2(0x0014, 0x0001, lambda_32DE)

    @scena.Lambda('lambda_32EF')
    def lambda_32EF():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_32EF')

    DispatchAsync2(0x0015, 0x0001, lambda_32EF)

    @scena.Lambda('lambda_3300')
    def lambda_3300():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3300')

    DispatchAsync2(0x0016, 0x0001, lambda_3300)

    @scena.Lambda('lambda_3311')
    def lambda_3311():
        OP_6C(0, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3311)

    ChrWalkTo(0x0101, 10610, 480, -53440, 600, 0x00)
    SetChrDirection(0x0101, 45, 400)
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

# id: 0x0004 offset: 0x33A2
@scena.Code('func_04_33A2')
def func_04_33A2():
    EventBegin(0x00)
    CameraMove(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    SetChrPos(0x0018, -25890, 0, -4510, 180)
    SetChrPos(0x0019, -27370, 0, -4510, 180)
    SetChrPos(0x001A, -27240, 0, -2700, 180)
    SetChrPos(0x001B, -25950, 0, -2920, 180)
    SetChrPos(0x0101, -26570, 0, -6220, 0)
    SetChrPos(0x0102, -28030, 0, -6250, 45)
    SetChrPos(0x0108, -25360, 0, -6190, 313)

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

    @scena.Lambda('lambda_351C')
    def lambda_351C():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_351C')

    DispatchAsync2(0x0101, 0x0001, lambda_351C)

    @scena.Lambda('lambda_352D')
    def lambda_352D():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_352D')

    DispatchAsync2(0x0102, 0x0001, lambda_352D)

    @scena.Lambda('lambda_353E')
    def lambda_353E():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_353E')

    DispatchAsync2(0x0108, 0x0001, lambda_353E)

    @scena.Lambda('lambda_354F')
    def lambda_354F():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_354F)

    Sleep(100)

    @scena.Lambda('lambda_356F')
    def lambda_356F():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_356F)

    Sleep(200)

    @scena.Lambda('lambda_358F')
    def lambda_358F():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_358F)

    Sleep(100)

    @scena.Lambda('lambda_35AF')
    def lambda_35AF():
        ChrWalkTo(0x00FE, -25760, 0, 30390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_35AF)

    Sleep(2000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetScenaFlags(ScenaFlag(0x00CA, 1, 0x651))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x35EF
@scena.Code('func_05_35EF')
def func_05_35EF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3748',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_365D',
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

    Jump('loc_372D')

    def _loc_365D(): pass

    label('loc_365D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36BA',
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

    Jump('loc_372D')

    def _loc_36BA(): pass

    label('loc_36BA')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_372D',
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

    def _loc_372D(): pass

    label('loc_372D')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3748(): pass

    label('loc_3748')

    Return()

# id: 0x0006 offset: 0x3749
@scena.Code('func_06_3749')
def func_06_3749():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38A3',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37B8',
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

    Jump('loc_3888')

    def _loc_37B8(): pass

    label('loc_37B8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3815',
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

    Jump('loc_3888')

    def _loc_3815(): pass

    label('loc_3815')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3888',
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

    def _loc_3888(): pass

    label('loc_3888')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_38A3(): pass

    label('loc_38A3')

    Return()

# id: 0x0007 offset: 0x38A4
@scena.Code('func_07_38A4')
def func_07_38A4():
    FadeOut(300, 0, 100)
    SetChrName('')
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

# id: 0x0008 offset: 0x391F
@scena.Code('func_08_391F')
def func_08_391F():
    FadeOut(300, 0, 100)
    SetChrName('')

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
