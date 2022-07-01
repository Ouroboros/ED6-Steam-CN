import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2304_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2304   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2304.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1C98
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
        ('ED6_DT29/CH12730._CH', 'ED6_DT29/CH12730P._CP'),
        ('ED6_DT29/CH12731._CH', 'ED6_DT29/CH12731P._CP'),
        ('ED6_DT29/CH12740._CH', 'ED6_DT29/CH12740P._CP'),
        ('ED6_DT29/CH12741._CH', 'ED6_DT29/CH12741P._CP'),
        ('ED6_DT29/CH12750._CH', 'ED6_DT29/CH12750P._CP'),
        ('ED6_DT29/CH12751._CH', 'ED6_DT29/CH12751P._CP'),
        ('ED6_DT29/CH12760._CH', 'ED6_DT29/CH12760P._CP'),
        ('ED6_DT29/CH12761._CH', 'ED6_DT29/CH12761P._CP'),
        ('ED6_DT29/CH12770._CH', 'ED6_DT29/CH12770P._CP'),
        ('ED6_DT29/CH12771._CH', 'ED6_DT29/CH12771P._CP'),
        ('ED6_DT29/CH12780._CH', 'ED6_DT29/CH12780P._CP'),
        ('ED6_DT29/CH12781._CH', 'ED6_DT29/CH12781P._CP'),
        ('ED6_DT29/CH12790._CH', 'ED6_DT29/CH12790P._CP'),
        ('ED6_DT29/CH12791._CH', 'ED6_DT29/CH12791P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 290,
            z           = 0,
            y           = -40120,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EAF,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5500,
            z           = 400,
            y           = -9000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1EB0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5500,
            z           = 400,
            y           = -9000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EB1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5500,
            z           = 400,
            y           = 11000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EB2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5500,
            z           = 400,
            y           = 11000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1EB3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 140,
            z           = 0,
            y           = 660,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EB4,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -4870,
            triggerZ            = -3200,
            triggerY            = 64360,
            triggerRange        = 1000,
            actorX              = -5330,
            actorZ              = -3200,
            actorY              = 63890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -7290,
            triggerZ            = -3200,
            triggerY            = 69820,
            triggerRange        = 1000,
            actorX              = -7980,
            actorZ              = -3200,
            actorY              = 70010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4990,
            triggerZ            = -3200,
            triggerY            = 75520,
            triggerRange        = 1000,
            actorX              = -5420,
            actorZ              = -3200,
            actorY              = 75960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5070,
            triggerZ            = -3200,
            triggerY            = 75430,
            triggerRange        = 1000,
            actorX              = 5540,
            actorZ              = -3200,
            actorY              = 75890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7290,
            triggerZ            = -3200,
            triggerY            = 70200,
            triggerRange        = 1000,
            actorX              = 8070,
            actorZ              = -3200,
            actorY              = 70040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5010,
            triggerZ            = -3200,
            triggerY            = 64510,
            triggerRange        = 1000,
            actorX              = 5540,
            actorZ              = -3200,
            actorY              = 64120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 4400,
            triggerY            = 162290,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 4400,
            actorY              = 162970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 400,
            triggerY            = -74270,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 400,
            actorY              = -74900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 50,
            triggerZ            = 0,
            triggerY            = 39430,
            triggerRange        = 1000,
            actorX              = 50,
            actorZ              = 0,
            actorY              = 39430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3990,
            triggerZ            = 4400,
            triggerY            = 147040,
            triggerRange        = 1200,
            actorX              = -3990,
            actorZ              = 5600,
            actorY              = 147040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_33A'),
        (0x00000065, 'loc_341'),
        (-1, 'loc_348'),
    )

    def _loc_33A(): pass

    label('loc_33A')

    Event(0, 0x000B)

    Jump('loc_348')

    def _loc_341(): pass

    label('loc_341')

    Event(0, 0x000D)

    Jump('loc_348')

    def _loc_348(): pass

    label('loc_348')

    Return()

# id: 0x0001 offset: 0x349
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 2, 0x1F82)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35B',
    )

    OP_6F(0x000A, 0)

    Jump('loc_362')

    def _loc_35B(): pass

    label('loc_35B')

    OP_6F(0x000A, 60)

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 3, 0x1F83)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_374',
    )

    OP_6F(0x000B, 0)

    Jump('loc_37B')

    def _loc_374(): pass

    label('loc_374')

    OP_6F(0x000B, 60)

    def _loc_37B(): pass

    label('loc_37B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 4, 0x1F84)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38D',
    )

    OP_6F(0x000C, 0)

    Jump('loc_394')

    def _loc_38D(): pass

    label('loc_38D')

    OP_6F(0x000C, 60)

    def _loc_394(): pass

    label('loc_394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 5, 0x1F85)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A6',
    )

    OP_6F(0x000D, 0)

    Jump('loc_3AD')

    def _loc_3A6(): pass

    label('loc_3A6')

    OP_6F(0x000D, 60)

    def _loc_3AD(): pass

    label('loc_3AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 6, 0x1F86)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BF',
    )

    OP_6F(0x000E, 0)

    Jump('loc_3C6')

    def _loc_3BF(): pass

    label('loc_3BF')

    OP_6F(0x000E, 60)

    def _loc_3C6(): pass

    label('loc_3C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F1, 0, 0x1F88)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D8',
    )

    OP_6F(0x000F, 0)

    Jump('loc_3DF')

    def _loc_3D8(): pass

    label('loc_3D8')

    OP_6F(0x000F, 60)

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F1, 1, 0x1F89)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F1',
    )

    OP_6F(0x0011, 0)

    Jump('loc_3F8')

    def _loc_3F1(): pass

    label('loc_3F1')

    OP_6F(0x0011, 60)

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F1, 2, 0x1F8A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40A',
    )

    OP_6F(0x0012, 0)

    Jump('loc_411')

    def _loc_40A(): pass

    label('loc_40A')

    OP_6F(0x0012, 60)

    def _loc_411(): pass

    label('loc_411')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D5, 7, 0x1EAF)),
            Expr.Return,
        ),
        'loc_445',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_445(): pass

    label('loc_445')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 0, 0x1EB0)),
            Expr.Return,
        ),
        'loc_451',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 1, 0x1EB1)),
            Expr.Return,
        ),
        'loc_45D',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_45D(): pass

    label('loc_45D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 2, 0x1EB2)),
            Expr.Return,
        ),
        'loc_469',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 3, 0x1EB3)),
            Expr.Return,
        ),
        'loc_475',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 4, 0x1EB4)),
            Expr.Return,
        ),
        'loc_481',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_481(): pass

    label('loc_481')

    OP_10(0x01, 0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 2, 0x1E22)),
            Expr.Return,
        ),
        'loc_527',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)

    Jump('loc_5C0')

    def _loc_527(): pass

    label('loc_527')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)

    def _loc_5C0(): pass

    label('loc_5C0')

    OP_1B(0x00, 0x00, 0x000C)
    OP_1B(0x01, 0x00, 0x000E)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_635',
    )

    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, -3990, 5600, 147040, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0013, 0x0020)
    OP_6F(0x0013, 0)
    OP_70(0x0013, 0x000000FA)

    Jump('loc_641')

    def _loc_635(): pass

    label('loc_635')

    OP_72(0x0013, 0x0020)
    OP_6F(0x0013, 250)

    def _loc_641(): pass

    label('loc_641')

    Return()

# id: 0x0002 offset: 0x642
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 2, 0x1E22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A19',
    )

    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_70(0x0000, 0x00000168)
    Sleep(2500)

    OP_22(0x009D, 0x00, 0x64)
    OP_B0(0x0004, 0x64)
    OP_B0(0x0005, 0x64)
    OP_B0(0x0006, 0x64)
    OP_B0(0x0007, 0x64)
    OP_B0(0x0008, 0x64)
    OP_70(0x0004, 0x000000F0)
    Sleep(100)

    OP_70(0x0005, 0x000000F0)
    Sleep(100)

    OP_70(0x0006, 0x000000F0)
    Sleep(100)

    OP_70(0x0007, 0x000000F0)
    Sleep(100)

    OP_70(0x0008, 0x000000F0)
    Sleep(100)

    OP_22(0x00B9, 0x00, 0x64)
    OP_B0(0x0001, 0x64)
    OP_B0(0x0002, 0x64)
    OP_B0(0x0003, 0x64)
    OP_70(0x0001, 0x00000168)
    OP_70(0x0002, 0x00000168)
    OP_70(0x0003, 0x00000168)
    OP_73(0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于‘环’的封印（４／４）』\n',
            '　\n',
            '从设施■■■的光，\n',
            '经过长城『■■■』■内■折■\n',
            '■■■，并■■到了浮在■中的■■■。\n',
            '　\n',
            '■是，■环■\n',
            '■从我们■■消■■，\n',
            '『■■■梅拉■』■■■了运■。\n',
            '这样，『■■■■』\n',
            '的成功■行便被确认■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■环■是■■至宝■中\n',
            '■■空间的■■。\n',
            '■了让拥有对空间■■■■■力量■■■■无■■\n',
            '■■■■事就是■■\n',
            '■绝掉■■■对空间\n',
            '■至对时间的■■■■。\n',
            '　\n',
            '我们绞■■汁研■出的■■■■构』\n',
            '将■■■连同城■■■■进了■■元，\n',
            '成功地■■■■时■■结■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶１１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１１'], 1)
    OP_A2(0x1E22)
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_6F(0x0008, 0)
    OP_6D(520, 200, 36750, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 520, 200, 36750, 0)
    SetChrPos(0x0001, 520, 200, 36750, 0)
    SetChrPos(0x0002, 520, 200, 36750, 0)
    SetChrPos(0x0003, 520, 200, 36750, 0)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_C3D')

    def _loc_A19(): pass

    label('loc_A19')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x009C, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于‘环’的封印（４／４）』\n',
            '　\n',
            '从设施■■■的光，\n',
            '经过长城『■■■』■内■折■\n',
            '■■■，并■■到了浮在■中的■■■。\n',
            '　\n',
            '■是，■环■\n',
            '■从我们■■消■■，\n',
            '『■■■梅拉■』■■■了运■。\n',
            '这样，『■■■■』\n',
            '的成功■行便被确认■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■环■是■■至宝■中\n',
            '■■空间的■■。\n',
            '■了让拥有对空间■■■■■力量■■■■无■■\n',
            '■■■■事就是■■\n',
            '■绝掉■■■对空间\n',
            '■至对时间的■■■■。\n',
            '　\n',
            '我们绞■■汁研■出的■■■■构』\n',
            '将■■■连同城■■■■进了■■元，\n',
            '成功地■■■■时■■结■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_C3D(): pass

    label('loc_C3D')

    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0xC41
@scena.Code('func_03_C41')
def func_03_C41():
    UnlockAchievement(0x02, 0x9C, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 2, 0x1F82)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D1E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_CB5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F82)

    Jump('loc_D1B')

    def _loc_CB5(): pass

    label('loc_CB5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0x00000000)

    def _loc_D1B(): pass

    label('loc_D1B')

    Jump('loc_D4F')

    def _loc_D1E(): pass

    label('loc_D1E')

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
    def _loc_D4F(): pass

    label('loc_D4F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0xD5D
@scena.Code('func_04_D5D')
def func_04_D5D():
    UnlockAchievement(0x02, 0x9D, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 3, 0x1F83)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E3A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000B, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['苍耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_DD1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['苍耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F83)

    Jump('loc_E37')

    def _loc_DD1(): pass

    label('loc_DD1')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['苍耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['苍耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0x00000000)

    def _loc_E37(): pass

    label('loc_E37')

    Jump('loc_E6B')

    def _loc_E3A(): pass

    label('loc_E3A')

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
    def _loc_E6B(): pass

    label('loc_E6B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xE79
@scena.Code('func_05_E79')
def func_05_E79():
    UnlockAchievement(0x02, 0x9E, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 4, 0x1F84)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F56',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000C, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_EED',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F84)

    Jump('loc_F53')

    def _loc_EED(): pass

    label('loc_EED')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0x00000000)

    def _loc_F53(): pass

    label('loc_F53')

    Jump('loc_F87')

    def _loc_F56(): pass

    label('loc_F56')

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
    def _loc_F87(): pass

    label('loc_F87')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xF95
@scena.Code('func_06_F95')
def func_06_F95():
    UnlockAchievement(0x02, 0x9F, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 5, 0x1F85)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1072',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000D, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['活性之药'], 1)"),
            Expr.Return,
        ),
        'loc_1009',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F85)

    Jump('loc_106F')

    def _loc_1009(): pass

    label('loc_1009')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000D, 60)
    OP_70(0x000D, 0x00000000)

    def _loc_106F(): pass

    label('loc_106F')

    Jump('loc_10A3')

    def _loc_1072(): pass

    label('loc_1072')

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
    def _loc_10A3(): pass

    label('loc_10A3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x10B1
@scena.Code('func_07_10B1')
def func_07_10B1():
    UnlockAchievement(0x02, 0xA0, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F0, 6, 0x1F86)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_118E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000E, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['轻钢靴'], 1)"),
            Expr.Return,
        ),
        'loc_1125',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['轻钢靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F86)

    Jump('loc_118B')

    def _loc_1125(): pass

    label('loc_1125')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['轻钢靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['轻钢靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000E, 60)
    OP_70(0x000E, 0x00000000)

    def _loc_118B(): pass

    label('loc_118B')

    Jump('loc_11BF')

    def _loc_118E(): pass

    label('loc_118E')

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
    def _loc_11BF(): pass

    label('loc_11BF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x11CD
@scena.Code('func_08_11CD')
def func_08_11CD():
    UnlockAchievement(0x02, 0xA1, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F1, 0, 0x1F88)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12AA',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000F, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1241',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F88)

    Jump('loc_12A7')

    def _loc_1241(): pass

    label('loc_1241')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0x00000000)

    def _loc_12A7(): pass

    label('loc_12A7')

    Jump('loc_12DB')

    def _loc_12AA(): pass

    label('loc_12AA')

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
    def _loc_12DB(): pass

    label('loc_12DB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x12E9
@scena.Code('func_09_12E9')
def func_09_12E9():
    UnlockAchievement(0x02, 0xA2, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F1, 1, 0x1F89)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13C6',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0011, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['祭师之豆'], 1)"),
            Expr.Return,
        ),
        'loc_135D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['祭师之豆']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F89)

    Jump('loc_13C3')

    def _loc_135D(): pass

    label('loc_135D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['祭师之豆']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['祭师之豆']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0x00000000)

    def _loc_13C3(): pass

    label('loc_13C3')

    Jump('loc_13F7')

    def _loc_13C6(): pass

    label('loc_13C6')

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
    def _loc_13F7(): pass

    label('loc_13F7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x1405
@scena.Code('func_0A_1405')
def func_0A_1405():
    UnlockAchievement(0x02, 0xA3, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F1, 2, 0x1F8A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0012, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['红耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_1479',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['红耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F8A)

    Jump('loc_14DF')

    def _loc_1479(): pass

    label('loc_1479')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['红耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['红耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0012, 60)
    OP_70(0x0012, 0x00000000)

    def _loc_14DF(): pass

    label('loc_14DF')

    Jump('loc_1513')

    def _loc_14E2(): pass

    label('loc_14E2')

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
    def _loc_1513(): pass

    label('loc_1513')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x1521
@scena.Code('func_0B_1521')
def func_0B_1521():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 250, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -500, 250, -66000, 0)
    SetChrPos(0x0102, 500, 250, -66000, 0)
    SetChrPos(0x00F8, -500, 250, -67000, 0)
    SetChrPos(0x00F9, 500, 250, -67000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0011)
    Fade(500)
    OP_6D(-110, 250, -64580, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -110, 250, -64580, 0)
    SetChrPos(0x0001, -110, 250, -64580, 0)
    SetChrPos(0x0002, -110, 250, -64580, 0)
    SetChrPos(0x0003, -110, 250, -64580, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x162E
@scena.Code('func_0C_162E')
def func_0C_162E():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 250, -66500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 500, 250, -67000, 180)
    SetChrPos(0x0102, -500, 250, -67000, 180)
    SetChrPos(0x00F8, 500, 250, -66000, 180)
    SetChrPos(0x00F9, -500, 250, -66000, 180)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0012)
    NewScene('ED6_DT21/C2303._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x16AF
@scena.Code('func_0D_16AF')
def func_0D_16AF():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 5050, 154000, 0)
    SetChrPos(0x0101, 500, 5050, 153500, 180)
    SetChrPos(0x0102, -500, 5050, 153500, 180)
    SetChrPos(0x00F8, 500, 5050, 154500, 180)
    SetChrPos(0x00F9, -500, 5050, 154500, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0011)
    Fade(500)
    OP_6D(0, 4700, 151670, 0)
    SetChrPos(0x0000, 0, 4700, 151670, 180)
    SetChrPos(0x0001, 0, 4700, 151670, 180)
    SetChrPos(0x0002, 0, 4700, 151670, 180)
    SetChrPos(0x0003, 0, 4700, 151670, 180)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x17AA
@scena.Code('func_0E_17AA')
def func_0E_17AA():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 5050, 154000, 0)
    SetChrPos(0x0101, -500, 5050, 154500, 0)
    SetChrPos(0x0102, 500, 5050, 154500, 0)
    SetChrPos(0x00F8, -500, 5050, 153500, 0)
    SetChrPos(0x00F9, 500, 5050, 153500, 0)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0012)
    NewScene('ED6_DT21/C2305._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x1822
@scena.Code('func_0F_1822')
def func_0F_1822():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0010 offset: 0x1901
@scena.Code('func_10_1901')
def func_10_1901():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0011 offset: 0x19E0
@scena.Code('func_11_19E0')
def func_11_19E0():
    @scena.Lambda('lambda_19E6')
    def lambda_19E6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_19E6)

    @scena.Lambda('lambda_19F8')
    def lambda_19F8():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_19F8)

    @scena.Lambda('lambda_1A0A')
    def lambda_1A0A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1A0A)

    @scena.Lambda('lambda_1A1C')
    def lambda_1A1C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1A1C)

    Sleep(2500)

    Return()

# id: 0x0012 offset: 0x1A2E
@scena.Code('func_12_1A2E')
def func_12_1A2E():
    @scena.Lambda('lambda_1A34')
    def lambda_1A34():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1A34)

    @scena.Lambda('lambda_1A46')
    def lambda_1A46():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1A46)

    @scena.Lambda('lambda_1A58')
    def lambda_1A58():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1A58)

    @scena.Lambda('lambda_1A6A')
    def lambda_1A6A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1A6A)

    Sleep(2000)

    Return()

# id: 0x0013 offset: 0x1A7C
@scena.Code('func_13_1A7C')
def func_13_1A7C():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ACD',
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

    Jump('loc_1C6F')

    def _loc_1ACD(): pass

    label('loc_1ACD')

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
        'loc_1C54',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0013, 0x0020)
    OP_6F(0x0013, 300)
    OP_70(0x0013, 0x000001F4)
    OP_73(0x0013)
    OP_6F(0x0013, 500)
    OP_70(0x0013, 0x000002BC)
    OP_71(0x0013, 0x0020)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x02, 0x02)
    LoadEffect(0x03, 'map\\\\mp027_01.eff')
    PlayEffect(0x03, 0x03, 0x00FF, -3990, 5600, 147040, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x03, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, -3990, 5600, 147040, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0013, 0)
    OP_70(0x0013, 0x000000FA)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_1C54(): pass

    label('loc_1C54')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C6E',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_1C6E(): pass

    label('loc_1C6E')

    Return()

    def _loc_1C6F(): pass

    label('loc_1C6F')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
