import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5511_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5511   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ' '),
    TXT(0x02, ' '),
    TXT(0x03, ' '),
    TXT(0x04, ' '),
    TXT(0x05, ' '),
    TXT(0x06, ' '),
    TXT(0x07, ' '),
    TXT(0x08, ' '),
    TXT(0x09, '猎兵'),
    TXT(0x0A, '卡露娜'),
    TXT(0x0B, '库拉茨'),
    TXT(0x0C, '菲莉斯管理员'),
    TXT(0x0D, '维修师罗伯特'),
    TXT(0x0E, ' '),
    TXT(0x0F, ''),
    TXT(0x10, ''),
    TXT(0x11, ''),
    TXT(0x12, ''),
    TXT(0x13, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5511.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0x000E
    header.importTable    = ['ED6_DT21/C5511._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x39DD
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
        ('ED6_DT29/CH12240._CH', 'ED6_DT29/CH12240P._CP'),
        ('ED6_DT29/CH12241._CH', 'ED6_DT29/CH12241P._CP'),
        ('ED6_DT29/CH12370._CH', 'ED6_DT29/CH12370P._CP'),
        ('ED6_DT29/CH12371._CH', 'ED6_DT29/CH12371P._CP'),
        ('ED6_DT29/CH12210._CH', 'ED6_DT29/CH12210P._CP'),
        ('ED6_DT29/CH12211._CH', 'ED6_DT29/CH12211P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
        ('ED6_DT27/CH03630._CH', 'ED6_DT27/CH03630P._CP'),
        ('ED6_DT27/CH03640._CH', 'ED6_DT27/CH03640P._CP'),
        ('ED6_DT07/CH00261._CH', 'ED6_DT07/CH00261P._CP'),
        ('ED6_DT27/CH03900._CH', 'ED6_DT27/CH03900P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT27/CH04632._CH', 'ED6_DT27/CH04632P._CP'),
        ('ED6_DT27/CH03820._CH', 'ED6_DT27/CH03820P._CP'),
        ('ED6_DT27/CH04821._CH', 'ED6_DT27/CH04821P._CP'),
        ('ED6_DT27/CH04640._CH', 'ED6_DT27/CH04640P._CP'),
        ('ED6_DT27/CH04641._CH', 'ED6_DT27/CH04641P._CP'),
        ('ED6_DT27/CH04630._CH', 'ED6_DT27/CH04630P._CP'),
        ('ED6_DT27/CH04634._CH', 'ED6_DT27/CH04634P._CP'),
        ('ED6_DT27/CH04631._CH', 'ED6_DT27/CH04631P._CP'),
        ('ED6_DT26/CH20200._CH', 'ED6_DT26/CH20200P._CP'),
        ('ED6_DT26/CH20201._CH', 'ED6_DT26/CH20201P._CP'),
        ('ED6_DT26/CH20202._CH', 'ED6_DT26/CH20202P._CP'),
    ]

# id: 0x10002 offset: 0x18A
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
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0000,
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
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 18,
            chipIndex           = 18,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x34A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 580,
            z           = 0,
            y           = -79030,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 2350,
            z           = 0,
            y           = 18010,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 122670,
            z           = 0,
            y           = 56060,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 122370,
            z           = 0,
            y           = -65990,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x3BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x3BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1900,
            triggerZ            = -500,
            triggerY            = -56200,
            triggerRange        = 1000,
            actorX              = -1900,
            actorZ              = 1000,
            actorY              = -56200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2470,
            triggerZ            = 0,
            triggerY            = -60170,
            triggerRange        = 1000,
            actorX              = 2470,
            actorZ              = 0,
            actorY              = -60170,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1930,
            triggerZ            = 0,
            triggerY            = -30370,
            triggerRange        = 1000,
            actorX              = -1930,
            actorZ              = 0,
            actorY              = -30370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1960,
            triggerZ            = 0,
            triggerY            = -26130,
            triggerRange        = 1500,
            actorX              = -1960,
            actorZ              = 1500,
            actorY              = -26130,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1870,
            triggerZ            = 0,
            triggerY            = -33850,
            triggerRange        = 1500,
            actorX              = -1870,
            actorZ              = 1500,
            actorY              = -33850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5920,
            triggerZ            = 0,
            triggerY            = -28120,
            triggerRange        = 1500,
            actorX              = -5920,
            actorZ              = 1500,
            actorY              = -28120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5990,
            triggerZ            = 0,
            triggerY            = -32009,
            triggerRange        = 1500,
            actorX              = -5990,
            actorZ              = 1500,
            actorY              = -32009,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1920,
            triggerZ            = 0,
            triggerY            = -28070,
            triggerRange        = 1500,
            actorX              = 1920,
            actorZ              = 1500,
            actorY              = -28070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1900,
            triggerZ            = 0,
            triggerY            = -32030,
            triggerRange        = 1500,
            actorX              = 1900,
            actorZ              = 1500,
            actorY              = -32030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0xFFFF,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 74740,
            triggerZ            = 0,
            triggerY            = 102630,
            triggerRange        = 1000,
            actorX              = 74740,
            actorZ              = 1000,
            actorY              = 102630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -80430,
            triggerZ            = 0,
            triggerY            = 17900,
            triggerRange        = 1000,
            actorX              = -80430,
            actorZ              = 1000,
            actorY              = 17900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = -28920,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 1000,
            actorY              = -28920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2000,
            triggerZ            = 0,
            triggerY            = -28000,
            triggerRange        = 1000,
            actorX              = -2000,
            actorZ              = 1200,
            actorY              = -28000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x58E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x7A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59E',
    )

    Event(0, 0x0009)

    def _loc_59E(): pass

    label('loc_59E')

    Return()

# id: 0x0001 offset: 0x59F
@scena.Code('Init')
def Init():
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)
    OP_82(0x83, 0x00)
    OP_82(0x84, 0x00)
    OP_82(0x85, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 7, 0x1067)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E6',
    )

    OP_6F(0x0002, 30)
    OP_6F(0x0003, 30)
    OP_6F(0x0004, 30)
    OP_6F(0x0005, 30)
    OP_79(0x0A, 0x0002)
    OP_79(0x0C, 0x0002)
    OP_79(0x20, 0x0002)
    OP_79(0x21, 0x0002)
    OP_7B()

    Jump('loc_602')

    def _loc_5E6(): pass

    label('loc_5E6')

    OP_6F(0x0002, 15)
    OP_6F(0x0003, 15)
    OP_6F(0x0004, 15)
    OP_6F(0x0005, 15)

    def _loc_602(): pass

    label('loc_602')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_64(0x07, 0x0001)
    OP_64(0x08, 0x0001)
    OP_72(0x000B, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 7, 0x1067)),
            Expr.Return,
        ),
        'loc_65D',
    )

    OP_64(0x0C, 0x0001)
    OP_7A(0x0A, 0x0002)
    OP_7A(0x0C, 0x0002)
    OP_7A(0x20, 0x0002)
    OP_7A(0x21, 0x0002)
    OP_7B()
    OP_6F(0x002E, 1)
    OP_6F(0x000B, 29)
    OP_71(0x000B, 0x0002)

    Jump('loc_65D')

    def _loc_65D(): pass

    label('loc_65D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 5, 0x1145)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66F',
    )

    OP_6F(0x002F, 0)

    Jump('loc_676')

    def _loc_66F(): pass

    label('loc_66F')

    OP_6F(0x002F, 60)

    def _loc_676(): pass

    label('loc_676')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E1',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 74740, 1000, 102630, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 0x00000000)

    Jump('loc_6F4')

    def _loc_6E1(): pass

    label('loc_6E1')

    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 0x00000000)

    def _loc_6F4(): pass

    label('loc_6F4')

    Return()

# id: 0x0002 offset: 0x6F5
@scena.Code('ReInit')
def ReInit():
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x6F9
@scena.Code('func_03_6F9')
def func_03_6F9():
    TalkBegin(0x00FF)

    Talk(
        (
            '开始',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x00, 0x00, 0x0004)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x70F
@scena.Code('func_04_70F')
def func_04_70F():
    Return()

# id: 0x0005 offset: 0x710
@scena.Code('func_05_710')
def func_05_710():
    Return()

# id: 0x0006 offset: 0x711
@scena.Code('func_06_711')
def func_06_711():
    TalkBegin(0x00FF)

    Talk(
        (
            '开始',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x00, 0x00, 0x0007)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x727
@scena.Code('func_07_727')
def func_07_727():
    Return()

# id: 0x0008 offset: 0x728
@scena.Code('func_08_728')
def func_08_728():
    Return()

# id: 0x0009 offset: 0x729
@scena.Code('func_09_729')
def func_09_729():
    Call(0, 0x000A)
    Call(0, 0x000B)

    Return()

# id: 0x000A offset: 0x732
@scena.Code('func_0A_732')
def func_0A_732():
    EventBegin(0x00)
    OP_6D(71250, 0, -31120, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 70500, 0, -30340, 0)
    SetChrPos(0x010A, 72480, 0, -30340, 0)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x10A, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x10A, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x10A, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0010, 22)
    SetChrPos(0x0010, 71440, 2000, -19470, 178)
    ClearChrFlags(0x0010, 0x0080)
    OP_20(0x000005DC)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0010,
        '男人的声音',
        (
            '#0330191528V呵呵，终于来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_1D(0x56)
    Sleep(500)

    @scena.Lambda('lambda_086A')
    def lambda_086A():
        OP_6D(71640, 1000, -22120, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_086A)

    @scena.Lambda('lambda_0882')
    def lambda_0882():
        OP_67(0, 5140, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0882)

    @scena.Lambda('lambda_089A')
    def lambda_089A():
        OP_6C(57000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_089A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010191529V#1P#1005F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191530V#1P#812F总算出现了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0906')
    def lambda_0906():
        OP_6B(3700, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0906)

    SetChrChipByIndex(0x0101, 13)

    @scena.Lambda('lambda_091B')
    def lambda_091B():
        OP_94(0x00, 0x0101, 0x0000, 0x00001388, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_091B)

    Sleep(200)

    SetChrChipByIndex(0x010A, 15)

    @scena.Lambda('lambda_093B')
    def lambda_093B():
        OP_94(0x00, 0x010A, 0x0000, 0x00001388, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_093B)

    WaitForThreadExit(0x0101, 0x0000)
    SetChrChipByIndex(0x0101, 13)
    WaitForThreadExit(0x010A, 0x0000)
    SetChrChipByIndex(0x010A, 15)

    ChrTalk(
        0x0010,
        (
            '#0330191531V#5P来得正好。\n',
            '欢迎光临我们的新据点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191532V#5P装置还有趣吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191533V#6P#1007F嗯～托你的福呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191534V#1002F话说回来，克鲁茨前辈他们\n',
            '好像在那个门的另一边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191535V#816F#4P不想吃苦头的话\n',
            '最好快放了他们哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191536V#5P呵，两个小丫头\n',
            '还挺嚣张的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191537V#5P不知这里是死路一条，\n',
            '竟然毫不在乎地就跑了进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191538V#6P#1006F哼，这么说的话\n',
            '你们也是一样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191539V虽然不知道你们有什么目的，\n',
            '不过你们已经是瓮中之鳖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191540V#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191541V#816F#4P协会的支援很快就会过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191542V这样一来，你们\n',
            '可是没有胜算的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191543V#5P哼……\n',
            '宿舍的通讯器已经完全被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191544V#5P你要怎么跟他们联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191545V#6P#1015F唔、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191546V（有没有什么虚张声势的好方法……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '要如何虚张声势？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【已经升起狼烟联络了】\n'),
            TXT(0x01, '【不需要联络】\n'),
            TXT(0x02, '【预定有其它的训练志愿者会来】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D4E'),
        (0x00000001, 'loc_E7A'),
        (0x00000002, 'loc_FD8'),
        (-1, 'loc_115E'),
    )

    def _loc_D4E(): pass

    label('loc_D4E')

    ChrTalk(
        0x0101,
        (
            '#0010191547V#6P#1009F……我们已经升起狼烟\n',
            '联络山下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191548V这是紧急时候的联络手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191549V#1317F#4P艾、艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191550V#5P哈哈哈！\n',
            '好可爱的借口！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191551V#5P我刚刚才上过屋顶，\n',
            '可没看到那种东西哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191552V#6P#1019F呜……\n',
            '（好像太简单了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115E')

    def _loc_E7A(): pass

    label('loc_E7A')

    OP_2B(0x007E, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010191553V#6P#1006F哼，根本就\n',
            '不需要联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191554V没有收到定时联络，\n',
            '协会应该就会知道\n',
            '我们这边发生了异状。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191555V#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x010A,
        (
            '#0120191556V#814F#4P的确，今天早上\n',
            '应该已经注意到了异状才对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191557V#811F嗯，支援或许快要到了吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191558V#5P……可恶。\n',
            '最后的关头看来太大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115E')

    def _loc_FD8(): pass

    label('loc_FD8')

    ChrTalk(
        0x0101,
        (
            '#0010191559V#6P#1002F……今天刚好\n',
            '有其它的训练志愿者会来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191560V而且人数相当多，\n',
            '你们这些人根本不算什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191549V#1317F#4P艾、艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191562V#5P呵……\n',
            '你倒告诉了我一件好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191563V#5P那么，就在峡谷入口\n',
            '设下埋伏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191564V#5P如果他们没有戒备的话，\n',
            '速攻就能够全部歼灭了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191565V#6P#1019F呜……\n',
            '（没办法虚张声势了吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_115E(): pass

    label('loc_115E')

    ChrTalk(
        0x0010,
        (
            '#0330191566V#5P算了。\n',
            '总之你们太碍眼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x01FD, 0x00, 0x64)
    SetChrChipByIndex(0x0010, 17)
    OP_99(0x0010, 0x00, 0x05, 0x000007D0)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0330191567V#5P赶快让我统统都收拾掉吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191568V#6P#1005F正合我意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191569V#815F#4P现在就决一胜负吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x0010, 0xFF)
    Battle(0x00000395, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Return()

# id: 0x000B offset: 0x1263
@scena.Code('func_0B_1263')
def func_0B_1263():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x00)
    TerminateThread(0x0010, 0x00)
    OP_6D(72290, 1500, -21120, 0)
    SetChrPos(0x0101, 70540, 1500, -21200, 78)
    SetChrChipByIndex(0x0101, 13)
    SetChrPos(0x010A, 73110, 1000, -22200, 17)
    SetChrChipByIndex(0x010A, 15)
    SetChrPos(0x0010, 73240, 2000, -19780, 225)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0010, 23)
    SetChrSubChip(0x0010, 3)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0330191570V#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191571V#1006F#6P呼呼……赢、赢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191572V#1015F不、不过这个反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191573V#1317F嗯，嗯……\n',
            '艾丝蒂尔也发现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0011, 71420, 2000, -15600, 180)
    SetChrPos(0x0012, 71420, 2000, -15600, 180)

    NpcTalk(
        0x0011,
        '女人的声音',
        (
            '#0320191574V#2P呵呵……\n',
            '好像完全被骗了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    NpcTalk(
        0x0012,
        '男人的声音',
        (
            '#0310191575V#2P哈哈哈。\n',
            '完全上当了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x000007D0)

    @scena.Lambda('lambda_147E')
    def lambda_147E():
        OP_6D(72300, 2000, -18490, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_147E)

    @scena.Lambda('lambda_1496')
    def lambda_1496():
        OP_6B(3600, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1496)

    OP_8C(0x0101, 3, 1000)
    Sleep(100)

    OP_8C(0x010A, 3, 1000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrPos(0x0011, 71480, 2000, -12880, 180)
    SetChrPos(0x0012, 71480, 2000, -11880, 180)
    OP_22(0x006D, 0x00, 0x64)
    OP_72(0x000D, 0x0010)
    OP_6F(0x000D, 0)
    OP_70(0x000D, 0x0000001D)
    OP_73(0x000D)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_150A')
    def lambda_150A():
        OP_8E(0x0011, 72420, 2000, -18180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_150A)

    @scena.Lambda('lambda_1525')
    def lambda_1525():
        OP_8E(0x0012, 71480, 2000, -15540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1525)

    WaitForThreadExit(0x0012, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010191576V#1020F#6P啊！',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_1563')
    def lambda_1563():
        OP_8E(0x0012, 71320, 2000, -17970, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1563)

    WaitForThreadExit(0x0011, 0x0001)
    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191577V#812F#4P增、增援！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0012, 0x0001)
    ChrTurnDirection(0x0012, 0x0101, 400)

    NpcTalk(
        0x0011,
        '女猎兵',
        (
            '#0320191578V#5P哈哈，不是啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '女猎兵',
        (
            '#0320191579V#5P虽然口气没变，\n',
            '但你们也该明白了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191580V#1015F#6P这个大姐口气……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191581V#1004F……难、难道是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191582V#1317F#3S#4P卡、卡露娜前辈！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '女猎兵',
        (
            '#0320191583V#5P答对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00D5, 0x00, 0x64)
    Fade(500)
    SetChrChipByIndex(0x0011, 25)
    OP_0D()
    OP_1D(0x01)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0320191584V#1201F#5P亚妮拉丝、艾丝蒂尔。\n',
            '实在是好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x010A, 0)
    SetChrChipByIndex(0x010A, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191585V#1020F#6P好久不见……\n',
            '#1005F到底怎么回事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191586V那、那这位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191587V#815F库拉茨前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '猎兵',
        (
            '#0310191588V#5P对啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00D5, 0x00, 0x64)
    Fade(500)
    SetChrChipByIndex(0x0012, 27)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0310191589V#1191F#5P哟，你们两位\n',
            '辛苦啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191590V#1015F#6P辛、辛苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191591V……难道这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0330191592V呵呵，就是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0010, 0x03, 0x00, 0x000005DC)
    Sleep(500)

    OP_22(0x00D5, 0x00, 0x64)
    Fade(500)
    SetChrChipByIndex(0x0010, 26)
    OP_0D()
    OP_8C(0x0101, 78, 500)

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191593V#1211F艾丝蒂尔、亚妮拉丝。\n',
            '最终的训练，辛苦你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191594V#1004F#6P最、最终训练……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191595V#1317F这、这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191596V从昨天的袭击开始，\n',
            '一切都是在演戏吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191597V#1210F呵呵，这是本训练场\n',
            '的惯例。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191598V最终训练的用意是欺骗训练人员，\n',
            '让他们体验到危机的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191599V#1019F#6P什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0310191600V#1190F#5P而我们就是为了帮忙，\n',
            '特地从利贝尔赶过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0320191601V#1201F#5P呵呵……\n',
            '真是相当有趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191602V#1316F呜～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191603V#812F前辈们真是的，\n',
            '太欺负人啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191604V#1009F#6P就、就是呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191605V我们还以为\n',
            '真的碰到危机了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191606V#1213F嗯，这就是这次训练的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191607V#1212F顺带提醒你们……\n',
            '真正的猎兵可没这么天真哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191608V#1003F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191609V#813F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0320191610V#1200F#5P在利贝尔，\n',
            '使用猎兵团是被禁止的，\n',
            '因此不太容易想象得到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320191611V但在其它国家的话，游击士协会\n',
            '和猎兵团的较量可是家常便饭的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320191612V#1202F自然而然，游击士们大多\n',
            '也会对危机的状况有所戒备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0310191613V#1192F#5P所以，我们希望利贝尔的游击士\n',
            '也能体验一次危机的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310191614V就当这是一种父母心的表现吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191615V#1007F#6P唉……真狡猾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191616V#1019F被这么一说，\n',
            '想抱怨也没有办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191617V#812F嗯嗯，真狡猾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0013, 71480, 2000, -12880, 180)

    NpcTalk(
        0x0013,
        '女性的声音',
        (
            '#2750191618V#2P哎呀哎呀。\n',
            '已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0012, 500)

    @scena.Lambda('lambda_1E7C')
    def lambda_1E7C():
        OP_6D(71800, 2000, -18000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E7C)

    ClearChrFlags(0x0013, 0x0080)
    OP_8E(0x0013, 71410, 2000, -15260, 2000, 0x00)
    OP_8F(0x0013, 70140, 2000, -18290, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010191619V#1004F#6P啊，管理员小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191620V#812F唔～管理员小姐\n',
            '也是共犯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2750191621V#5P哎呀，别说成共犯那么难听嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2750191622V#5P因为要演戏，\n',
            '我也是拚命在背台词的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2750191623V#5P嘻嘻，很逼真的演技吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191624V#1019F#6P嗯嗯～\n',
            '完全被你骗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0014, 71310, 0, -31680, 358)

    NpcTalk(
        0x0014,
        '男人的声音',
        (
            '#2760191625V#1P哈哈哈。\n',
            '你们两个都辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0014, 0x0080)

    @scena.Lambda('lambda_2035')
    def lambda_2035():
        OP_94(0x00, 0x00FE, 0x0000, 0x00001C84, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2035)

    @scena.Lambda('lambda_204B')
    def lambda_204B():
        OP_6D(72580, 1500, -21110, 2500)

        ExitThread()

    DispatchAsync(0x0014, 0x0003, lambda_204B)

    @scena.Lambda('lambda_2063')
    def lambda_2063():
        ChrTurnDirection(0x00FE, 0x0014, 500)
        Yield()

        Jump('lambda_2063')

    DispatchAsync2(0x0101, 0x0001, lambda_2063)

    @scena.Lambda('lambda_2074')
    def lambda_2074():
        ChrTurnDirection(0x00FE, 0x0014, 500)
        Yield()

        Jump('lambda_2074')

    DispatchAsync2(0x010A, 0x0001, lambda_2074)

    WaitForThreadExit(0x0014, 0x0001)
    WaitForThreadExit(0x0014, 0x0003)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)

    ChrTalk(
        0x010A,
        (
            '#0120191626V#2P#815F啊～大骗子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191627V#1007F#5P结果，\n',
            '全部的人都是共犯啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191628V#1004F啊，这么说的话，\n',
            '宿舍的通讯器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2760191629V嗯，那是报废零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2760191630V真正的通讯器被保管在\n',
            '其它地方，不必担心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2760191631V其实我本来预定要当人质，\n',
            '就这样一直躲藏到最后的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2760191632V不过因为你们想知道\n',
            '怎么样运用新导力器，\n',
            '我才会在那个时机出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191633V#2P#1316F真是的……\n',
            '大家准备得都太周到了啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191634V#1314F但是，结果算是\n',
            '我们上了当吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191635V#1007F#5P嗯～虽然不甘心但确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191636V#1025F冷静下来思考的话，\n',
            '的确还有很多不自然的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191637V我们的修练毕竟还是不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191638V#1211F呵呵，别这么沮丧嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2360')
    def lambda_2360():
        ChrTurnDirection(0x00FE, 0x0010, 500)
        Yield()

        Jump('lambda_2360')

    DispatchAsync2(0x0101, 0x0001, lambda_2360)

    @scena.Lambda('lambda_2371')
    def lambda_2371():
        ChrTurnDirection(0x00FE, 0x0010, 500)
        Yield()

        Jump('lambda_2371')

    DispatchAsync2(0x010A, 0x0001, lambda_2371)

    OP_6D(72500, 1750, -20000, 800)

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191639V#1213F库拉茨也说了，\n',
            '此次与其说是测试你们的实力，\n',
            '不如说是希望你们能体验危机的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191640V从这个意义上来说，演习是相当成功的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191641V#1210F那么接下来……\n',
            '亚妮拉丝·艾尔菲德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191642V#814F啊，是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191643V#1210F艾丝蒂尔·布莱德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191644V#1002F#6P……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191645V#1210F至此，本训练场的\n',
            '综合强化训练全部结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191646V这３周，真的是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191647V#1004F#6P这、这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191648V#1310F明天就可以……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '克鲁茨',
        (
            '#0330191649V#1211F我已经帮你们订了\n',
            '往利贝尔的定期船票。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191650V今晚什么也不会发生了，\n',
            '你们两人都好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2750191651V#5P嘻嘻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2750191652V#5P作为庆功宴和送别会，\n',
            '今晚可要大吃一顿哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    RemoveItem(ItemTable['认证装置'], 1)
    NewScene('ED6_DT21/C5600._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x2694
@scena.Code('func_0C_2694')
def func_0C_2694():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26E5',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_28A0')

    def _loc_26E5(): pass

    label('loc_26E5')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2885',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 74740, 1000, 102630, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 0x00000032)
    OP_73(0x0007)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 74740, 1000, 102630, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 74740, 1000, 102630, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0007, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_2885(): pass

    label('loc_2885')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_289F',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_289F(): pass

    label('loc_289F')

    Return()

    def _loc_28A0(): pass

    label('loc_28A0')

    Return()

# id: 0x000D offset: 0x28A1
@scena.Code('func_0D_28A1')
def func_0D_28A1():
    UnlockAchievement(0x02, 0x9B, 0x01, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 5, 0x1065)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2915',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -81450, 0, 18230, 90)
    SetChrPos(0x010A, -81380, 0, 17370, 90)
    OP_6D(-80680, 0, 18040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def _loc_2915(): pass

    label('loc_2915')

    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 5, 0x1145)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29ED',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x002F, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['认证装置'], 1)"),
            Expr.Return,
        ),
        'loc_2984',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['认证装置']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1145)

    Jump('loc_29EA')

    def _loc_2984(): pass

    label('loc_2984')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['认证装置']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['认证装置']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x002F, 60)
    OP_70(0x002F, 0x00000000)

    def _loc_29EA(): pass

    label('loc_29EA')

    Jump('loc_2A1E')

    def _loc_29ED(): pass

    label('loc_29ED')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2A1E(): pass

    label('loc_2A1E')

    Sleep(30)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 5, 0x1065)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D1E',
    )

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010191460V#1015F#1P这是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191461V#818F#4P嗯～好像是什么装置呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191462V而且还能看见\n',
            '导力器装置的开关……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191463V#810F#4P嗯，总之\n',
            '还是先拿着比较好吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191464V这里是训练设施，\n',
            '说不定能用来解除哪里的机关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010191465V#1011F#1P的确有这个可能呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191466V#1015F自从来到这里之后，\n',
            '像是机关门啦、漆黑的房间啦等等的\n',
            '也都碰到过了不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191467V#1310F#4P有备无患，对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191468V那么，继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191469V#1006F#1P嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※得到『#15I使用事件道具』。\n',
            '  在游戏途中，某些场面要直接使用\n',
            '  这些关键道具来继续向前推进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※利用使用事件道具时，\n',
            '  从Camp画面选择[Items]页\n',
            '  直接单击想使用的道具名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_A2(0x1065)
    EventEnd(0x00)

    def _loc_2D1E(): pass

    label('loc_2D1E')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x2D27
@scena.Code('func_0E_2D27')
def func_0E_2D27():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x416),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D34',
    )

    Return()

    def _loc_2D34(): pass

    label('loc_2D34')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 7, 0x1067)),
            Expr.Return,
        ),
        'loc_2DCA',
    )

    TalkBegin(0x00FF)
    OP_22(0x009D, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证组件已经启动了……\n',
            '但好像没什么特别的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_3409')

    def _loc_2DCA(): pass

    label('loc_2DCA')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3113',
    )

    EventBegin(0x00)
    OP_22(0x009D, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证组件已经启动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    SetChrPos(0x0015, -1980, 0, -27750, 201)

    @scena.Lambda('lambda_2E3C')
    def lambda_2E3C():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E3C)

    @scena.Lambda('lambda_2E4A')
    def lambda_2E4A():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2E4A)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010191490V#1004F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(-1890, 0, -32890, 1000)
    OP_64(0x0C, 0x0001)
    OP_6F(0x0002, 30)
    OP_70(0x0002, 0x0000000F)
    OP_22(0x006B, 0x00, 0x64)
    OP_73(0x0002)
    SetChrPos(0x0015, -5940, 0, -29460, 201)

    @scena.Lambda('lambda_2ED2')
    def lambda_2ED2():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ED2)

    @scena.Lambda('lambda_2EE0')
    def lambda_2EE0():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2EE0)

    OP_7A(0x0A, 0x0002)
    OP_7B()
    Sleep(400)

    OP_6F(0x0003, 30)
    OP_70(0x0003, 0x0000000F)
    OP_22(0x006B, 0x00, 0x64)
    OP_73(0x0003)
    SetChrPos(0x0015, -5900, 0, -37010, 225)

    @scena.Lambda('lambda_2F1F')
    def lambda_2F1F():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F1F)

    @scena.Lambda('lambda_2F2D')
    def lambda_2F2D():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2F2D)

    OP_7A(0x20, 0x0002)
    OP_7B()
    Sleep(400)

    OP_6F(0x0005, 30)
    OP_70(0x0005, 0x0000000F)
    OP_22(0x006B, 0x00, 0x64)
    OP_73(0x0005)
    SetChrPos(0x0015, 1660, 0, -36980, 45)

    @scena.Lambda('lambda_2F6C')
    def lambda_2F6C():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F6C)

    @scena.Lambda('lambda_2F7A')
    def lambda_2F7A():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2F7A)

    OP_7A(0x21, 0x0002)
    OP_7B()
    Sleep(400)

    OP_6F(0x0004, 30)
    OP_70(0x0004, 0x0000000F)
    OP_22(0x006B, 0x00, 0x64)
    OP_73(0x0004)
    SetChrPos(0x0015, 1670, 0, -29260, 45)

    @scena.Lambda('lambda_2FB9')
    def lambda_2FB9():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FB9)

    @scena.Lambda('lambda_2FC7')
    def lambda_2FC7():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2FC7)

    OP_7A(0x0C, 0x0002)
    OP_7B()
    Sleep(1000)

    OP_22(0x0073, 0x00, 0x64)
    OP_6F(0x000B, 0)
    OP_70(0x000B, 0x0000001D)
    OP_73(0x000B)
    SetChrPos(0x0015, -1980, 0, -27750, 201)

    @scena.Lambda('lambda_3006')
    def lambda_3006():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3006)

    @scena.Lambda('lambda_3014')
    def lambda_3014():
        ChrTurnDirection(0x00FE, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_3014)

    OP_22(0x009D, 0x00, 0x64)
    OP_6F(0x002E, 1)
    OP_70(0x002E, 0x00000001)
    OP_73(0x002E)
    OP_71(0x000B, 0x0002)
    OP_A2(0x1067)
    Sleep(1000)

    Fade(1000)
    OP_69(0x0000, 0x00000000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010191491V#1008F啊哈哈……\n',
            '真、真的打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120191492V#811F嘿嘿，正义必胜！对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191493V#816F好，艾丝蒂尔。\n',
            '接下来也谨慎地前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010191494V#1006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_3409')

    def _loc_3113(): pass

    label('loc_3113')

    TalkBegin(0x00FF)
    OP_22(0x009D, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证组件已经启动了……\n',
            '但这个地方好像没什么特别的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_31DA',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191470V#814F艾丝蒂尔。\n',
            '好像不是这里哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191471V先往前走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0000)

    Jump('loc_3406')

    def _loc_31DA(): pass

    label('loc_31DA')

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_322C',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191472V#812F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_322C(): pass

    label('loc_322C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3272',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191473V#813F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_3272(): pass

    label('loc_3272')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32B6',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191474V#814F这里好像\n',
            '没什么可用的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_32B6(): pass

    label('loc_32B6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32FC',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191475V#817F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_32FC(): pass

    label('loc_32FC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3342',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191476V#818F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_3342(): pass

    label('loc_3342')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3380',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191477V#819F嗯～看来\n',
            '没找对地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_3380(): pass

    label('loc_3380')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C3',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191478V#1315F这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3403')

    def _loc_33C3(): pass

    label('loc_33C3')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3403',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191479V#1316F这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3403(): pass

    label('loc_3403')

    OP_A2(0x0000)

    def _loc_3406(): pass

    label('loc_3406')

    TalkEnd(0x00FF)

    def _loc_3409(): pass

    label('loc_3409')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x000F offset: 0x340F
@scena.Code('func_0F_340F')
def func_0F_340F():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是门锁机关，\n',
            '但没看到什么拉杆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 7, 0x1067)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_396F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3545',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 5, 0x1145)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34CE',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191505V#813F说不定，在某处\n',
            '会有控制这个的装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191506V#1316F只好返回通道\n',
            '去寻找了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3542')

    def _loc_34CE(): pass

    label('loc_34CE')

    ChrTalk(
        0x010A,
        (
            '#0120191507V#812F刚才捡到的装置，\n',
            '是不是应该用在这里呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191508V#812F对了，艾丝蒂尔。\n',
            '我们就稍微试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3542(): pass

    label('loc_3542')

    Jump('loc_396F')

    def _loc_3545(): pass

    label('loc_3545')

    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010191509V#1002F对了，亚妮拉丝……\n',
            '这个装置……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191510V#812F嗯，好像是控制\n',
            '门锁的机械呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191511V如果能启动这个的话，\n',
            '我想门就会打开了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191512V#1007F不过很可惜，\n',
            '我们不知道启动的方法呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191513V#1003F这里也找不到\n',
            '和那时候大门一样的拉杆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 5, 0x1145)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36FB',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191514V#813F说不定，在某处\n',
            '可能有东西能解除这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191515V#812F艾丝蒂尔。\n',
            '回去找找看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190892V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_396D')

    def _loc_36FB(): pass

    label('loc_36FB')

    ChrTalk(
        0x010A,
        (
            '#0120191514V#813F说不定，在某处\n',
            '可能有东西能解除这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191518V#812F艾丝蒂尔。\n',
            '回去找找看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010A, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x010A,
        (
            '#0120191519V#814F啊，对了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010191520V#1004F想起什么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120191521V#812F艾丝蒂尔。\n',
            '还记得刚才捡到的装置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191522V你想想，就是在楼梯那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191523V#1011F啊，那个古怪的机械？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191524V#810F嗯，说不定\n',
            '要使用那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191525V……怎么样，不试试看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191526V#1015F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191527V嗯，试试也好，\n',
            '不过应该没这么顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※利用使用事件道具时，\n',
            '  从Camp画面选择[Items]页\n',
            '  直接单击想使用的道具名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_A2(0x0001)

    def _loc_396D(): pass

    label('loc_396D')

    EventEnd(0x01)

    def _loc_396F(): pass

    label('loc_396F')

    TalkEnd(0x00FF)

    Return()

# id: 0x0010 offset: 0x3973
@scena.Code('func_10_3973')
def func_10_3973():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
