import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1702_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1702   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1702.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1DC0
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
        ('ED6_DT29/CH12800._CH', 'ED6_DT29/CH12800P._CP'),
        ('ED6_DT29/CH12801._CH', 'ED6_DT29/CH12801P._CP'),
        ('ED6_DT29/CH12810._CH', 'ED6_DT29/CH12810P._CP'),
        ('ED6_DT29/CH12811._CH', 'ED6_DT29/CH12811P._CP'),
        ('ED6_DT29/CH12820._CH', 'ED6_DT29/CH12820P._CP'),
        ('ED6_DT29/CH12821._CH', 'ED6_DT29/CH12821P._CP'),
        ('ED6_DT29/CH12830._CH', 'ED6_DT29/CH12830P._CP'),
        ('ED6_DT29/CH12831._CH', 'ED6_DT29/CH12831P._CP'),
        ('ED6_DT29/CH12840._CH', 'ED6_DT29/CH12840P._CP'),
        ('ED6_DT29/CH12841._CH', 'ED6_DT29/CH12841P._CP'),
        ('ED6_DT29/CH12850._CH', 'ED6_DT29/CH12850P._CP'),
        ('ED6_DT29/CH12851._CH', 'ED6_DT29/CH12851P._CP'),
        ('ED6_DT29/CH12860._CH', 'ED6_DT29/CH12860P._CP'),
        ('ED6_DT29/CH12861._CH', 'ED6_DT29/CH12861P._CP'),
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
            x           = -6530,
            z           = 400,
            y           = -39740,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FFB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5460,
            z           = 400,
            y           = -40310,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FFC,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -60,
            z           = 400,
            y           = -1320,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1FFD,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6310,
            z           = 400,
            y           = 40240,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FFE,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5540,
            z           = 400,
            y           = 39770,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1FFF,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -66580,
            z           = 400,
            y           = 75070,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E80,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -74870,
            z           = 400,
            y           = 66550,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E81,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -76050,
            z           = 400,
            y           = -67860,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E82,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -67900,
            z           = 400,
            y           = -75980,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1E83,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 67970,
            z           = 400,
            y           = -75600,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E84,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 75900,
            z           = 400,
            y           = -67970,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1E85,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 66360,
            z           = 400,
            y           = 74560,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E86,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 74650,
            z           = 400,
            y           = 66690,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1E87,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x286
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x286
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 30,
            triggerZ            = -50,
            triggerY            = 39240,
            triggerRange        = 1000,
            actorX              = 30,
            actorZ              = -50,
            actorY              = 39940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 80,
            triggerZ            = -50,
            triggerY            = -40760,
            triggerRange        = 1000,
            actorX              = 80,
            actorZ              = -50,
            actorY              = -40050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -71270,
            triggerZ            = 0,
            triggerY            = 71150,
            triggerRange        = 1000,
            actorX              = -70740,
            actorZ              = 0,
            actorY              = 70800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -71480,
            triggerZ            = 0,
            triggerY            = -71470,
            triggerRange        = 1000,
            actorX              = -71860,
            actorZ              = 0,
            actorY              = -72030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71530,
            triggerZ            = 0,
            triggerY            = -71540,
            triggerRange        = 1000,
            actorX              = 71990,
            actorZ              = 0,
            actorY              = -72000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71140,
            triggerZ            = 0,
            triggerY            = 71150,
            triggerRange        = 1000,
            actorX              = 70730,
            actorZ              = 0,
            actorY              = 70630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x35E
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_38E'),
        (0x00000065, 'loc_395'),
        (0x00000066, 'loc_39C'),
        (0x00000067, 'loc_3A3'),
        (0x00000068, 'loc_3AA'),
        (0x00000069, 'loc_3B1'),
        (0x0000006A, 'loc_3B8'),
        (0x0000006B, 'loc_3BF'),
        (0x0000006C, 'loc_3C6'),
        (0x0000006D, 'loc_3CD'),
        (-1, 'loc_3D4'),
    )

    def _loc_38E(): pass

    label('loc_38E')

    Event(0, 0x0008)

    Jump('loc_3D4')

    def _loc_395(): pass

    label('loc_395')

    Event(0, 0x000A)

    Jump('loc_3D4')

    def _loc_39C(): pass

    label('loc_39C')

    Event(0, 0x000C)

    Jump('loc_3D4')

    def _loc_3A3(): pass

    label('loc_3A3')

    Event(0, 0x000E)

    Jump('loc_3D4')

    def _loc_3AA(): pass

    label('loc_3AA')

    Event(0, 0x0010)

    Jump('loc_3D4')

    def _loc_3B1(): pass

    label('loc_3B1')

    Event(0, 0x0012)

    Jump('loc_3D4')

    def _loc_3B8(): pass

    label('loc_3B8')

    Event(0, 0x0014)

    Jump('loc_3D4')

    def _loc_3BF(): pass

    label('loc_3BF')

    Event(0, 0x0016)

    Jump('loc_3D4')

    def _loc_3C6(): pass

    label('loc_3C6')

    Event(0, 0x0018)

    Jump('loc_3D4')

    def _loc_3CD(): pass

    label('loc_3CD')

    Event(0, 0x001A)

    Jump('loc_3D4')

    def _loc_3D4(): pass

    label('loc_3D4')

    Return()

# id: 0x0001 offset: 0x3D5
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 4, 0x1FA4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E7',
    )

    OP_6F(0x0000, 0)

    Jump('loc_3EE')

    def _loc_3E7(): pass

    label('loc_3E7')

    OP_6F(0x0000, 60)

    def _loc_3EE(): pass

    label('loc_3EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 5, 0x1FA5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_400',
    )

    OP_6F(0x0001, 0)

    Jump('loc_407')

    def _loc_400(): pass

    label('loc_400')

    OP_6F(0x0001, 60)

    def _loc_407(): pass

    label('loc_407')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 6, 0x1FA6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_419',
    )

    OP_6F(0x0002, 0)

    Jump('loc_420')

    def _loc_419(): pass

    label('loc_419')

    OP_6F(0x0002, 60)

    def _loc_420(): pass

    label('loc_420')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 7, 0x1FA7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_432',
    )

    OP_6F(0x0003, 0)

    Jump('loc_439')

    def _loc_432(): pass

    label('loc_432')

    OP_6F(0x0003, 60)

    def _loc_439(): pass

    label('loc_439')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 0, 0x1FA8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44B',
    )

    OP_6F(0x0004, 0)

    Jump('loc_452')

    def _loc_44B(): pass

    label('loc_44B')

    OP_6F(0x0004, 60)

    def _loc_452(): pass

    label('loc_452')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 1, 0x1FA9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_464',
    )

    OP_6F(0x0005, 0)

    Jump('loc_46B')

    def _loc_464(): pass

    label('loc_464')

    OP_6F(0x0005, 60)

    def _loc_46B(): pass

    label('loc_46B')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 3, 0x1FFB)),
            Expr.Return,
        ),
        'loc_49F',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_49F(): pass

    label('loc_49F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 4, 0x1FFC)),
            Expr.Return,
        ),
        'loc_4AB',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_4AB(): pass

    label('loc_4AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 5, 0x1FFD)),
            Expr.Return,
        ),
        'loc_4B7',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_4B7(): pass

    label('loc_4B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 6, 0x1FFE)),
            Expr.Return,
        ),
        'loc_4C3',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 7, 0x1FFF)),
            Expr.Return,
        ),
        'loc_4CF',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_4CF(): pass

    label('loc_4CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 0, 0x1E80)),
            Expr.Return,
        ),
        'loc_4DB',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_4DB(): pass

    label('loc_4DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 1, 0x1E81)),
            Expr.Return,
        ),
        'loc_4E7',
    )

    SetChrFlags(0x000E, 0x0080)

    def _loc_4E7(): pass

    label('loc_4E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 2, 0x1E82)),
            Expr.Return,
        ),
        'loc_4F3',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_4F3(): pass

    label('loc_4F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 3, 0x1E83)),
            Expr.Return,
        ),
        'loc_4FF',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_4FF(): pass

    label('loc_4FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 4, 0x1E84)),
            Expr.Return,
        ),
        'loc_50B',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 5, 0x1E85)),
            Expr.Return,
        ),
        'loc_517',
    )

    SetChrFlags(0x0012, 0x0080)

    def _loc_517(): pass

    label('loc_517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 6, 0x1E86)),
            Expr.Return,
        ),
        'loc_523',
    )

    SetChrFlags(0x0013, 0x0080)

    def _loc_523(): pass

    label('loc_523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D0, 7, 0x1E87)),
            Expr.Return,
        ),
        'loc_52F',
    )

    SetChrFlags(0x0014, 0x0080)

    def _loc_52F(): pass

    label('loc_52F')

    OP_1B(0x00, 0x00, 0x0009)
    OP_1B(0x01, 0x00, 0x000B)
    OP_1B(0x02, 0x00, 0x000D)
    OP_1B(0x03, 0x00, 0x000F)
    OP_1B(0x04, 0x00, 0x0011)
    OP_1B(0x05, 0x00, 0x0013)
    OP_1B(0x06, 0x00, 0x0015)
    OP_1B(0x07, 0x00, 0x0017)
    OP_1B(0x08, 0x00, 0x0019)
    OP_1B(0x09, 0x00, 0x001B)

    Return()

# id: 0x0002 offset: 0x562
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x73, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 4, 0x1FA4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_5D6',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1FA4)

    Jump('loc_63C')

    def _loc_5D6(): pass

    label('loc_5D6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_63C(): pass

    label('loc_63C')

    Jump('loc_670')

    def _loc_63F(): pass

    label('loc_63F')

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
    def _loc_670(): pass

    label('loc_670')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x67E
@scena.Code('func_03_67E')
def func_03_67E():
    UnlockAchievement(0x02, 0x74, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 5, 0x1FA5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_75B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['骷髅项链'], 1)"),
            Expr.Return,
        ),
        'loc_6F2',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['骷髅项链']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1FA5)

    Jump('loc_758')

    def _loc_6F2(): pass

    label('loc_6F2')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['骷髅项链']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['骷髅项链']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_758(): pass

    label('loc_758')

    Jump('loc_78C')

    def _loc_75B(): pass

    label('loc_75B')

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
    def _loc_78C(): pass

    label('loc_78C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x79A
@scena.Code('func_04_79A')
def func_04_79A():
    UnlockAchievement(0x02, 0x75, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 6, 0x1FA6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_877',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_80E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1FA6)

    Jump('loc_874')

    def _loc_80E(): pass

    label('loc_80E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_874(): pass

    label('loc_874')

    Jump('loc_8A8')

    def _loc_877(): pass

    label('loc_877')

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
    def _loc_8A8(): pass

    label('loc_8A8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x8B6
@scena.Code('func_05_8B6')
def func_05_8B6():
    UnlockAchievement(0x02, 0x76, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 7, 0x1FA7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_993',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['叶隐'], 1)"),
            Expr.Return,
        ),
        'loc_92A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['叶隐']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1FA7)

    Jump('loc_990')

    def _loc_92A(): pass

    label('loc_92A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['叶隐']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['叶隐']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_990(): pass

    label('loc_990')

    Jump('loc_9C4')

    def _loc_993(): pass

    label('loc_993')

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
    def _loc_9C4(): pass

    label('loc_9C4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x9D2
@scena.Code('func_06_9D2')
def func_06_9D2():
    UnlockAchievement(0x02, 0x77, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 0, 0x1FA8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA7',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000001E)
    OP_73(0x0004)
    OP_6F(0x0004, 30)
    AddSepith(0x00, 0x012C)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1FA8)

    Jump('loc_AC1')

    def _loc_AA7(): pass

    label('loc_AA7')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_AC1(): pass

    label('loc_AC1')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xAD3
@scena.Code('func_07_AD3')
def func_07_AD3():
    UnlockAchievement(0x02, 0x78, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 1, 0x1FA9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BB0',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_B47',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1FA9)

    Jump('loc_BAD')

    def _loc_B47(): pass

    label('loc_B47')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_BAD(): pass

    label('loc_BAD')

    Jump('loc_BE1')

    def _loc_BB0(): pass

    label('loc_BB0')

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
    def _loc_BE1(): pass

    label('loc_BE1')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xBEF
@scena.Code('func_08_BEF')
def func_08_BEF():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 200, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -500, 200, -66000, 0)
    SetChrPos(0x0102, 500, 200, -66000, 0)
    SetChrPos(0x00F8, -500, 200, -67000, 0)
    SetChrPos(0x00F9, 500, 200, -67000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(-60, 200, -64400, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, -60, 200, -64400, 0)
    SetChrPos(0x0001, -60, 200, -64400, 0)
    SetChrPos(0x0002, -60, 200, -64400, 0)
    SetChrPos(0x0003, -60, 200, -64400, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0009 offset: 0xD01
@scena.Code('func_09_D01')
def func_09_D01():
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
    OP_6D(0, 200, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 500, 200, -67000, 180)
    SetChrPos(0x0102, -500, 200, -67000, 180)
    SetChrPos(0x00F8, 500, 200, -66000, 180)
    SetChrPos(0x00F9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1701._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0xD82
@scena.Code('func_0A_D82')
def func_0A_D82():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-46700, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -47200, 200, 46700, 0)
    SetChrPos(0x0102, -46200, 200, 46700, 0)
    SetChrPos(0x00F8, -47200, 200, 45700, 0)
    SetChrPos(0x00F9, -46200, 200, 45700, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(-46770, 200, 48120, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, -46770, 200, 48120, 0)
    SetChrPos(0x0001, -46770, 200, 48120, 0)
    SetChrPos(0x0002, -46770, 200, 48120, 0)
    SetChrPos(0x0003, -46770, 200, 48120, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000B offset: 0xE94
@scena.Code('func_0B_E94')
def func_0B_E94():
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
    OP_6D(-46700, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -46200, 200, 45700, 180)
    SetChrPos(0x0102, -47200, 200, 45700, 180)
    SetChrPos(0x00F8, -46200, 200, 46700, 180)
    SetChrPos(0x00F9, -47200, 200, 46700, 180)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1701._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0xF15
@scena.Code('func_0C_F15')
def func_0C_F15():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(46600, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 46100, 200, 46700, 0)
    SetChrPos(0x0102, 47100, 200, 46700, 0)
    SetChrPos(0x00F8, 46100, 200, 45700, 0)
    SetChrPos(0x00F9, 47100, 200, 45700, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(46620, 200, 48180, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, 46620, 200, 48180, 0)
    SetChrPos(0x0001, 46620, 200, 48180, 0)
    SetChrPos(0x0002, 46620, 200, 48180, 0)
    SetChrPos(0x0003, 46620, 200, 48180, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000D offset: 0x1027
@scena.Code('func_0D_1027')
def func_0D_1027():
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
    OP_6D(46600, 200, 46200, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 47100, 200, 45700, 180)
    SetChrPos(0x0102, 46100, 200, 45700, 180)
    SetChrPos(0x00F8, 47100, 200, 46700, 180)
    SetChrPos(0x00F9, 46100, 200, 46700, 180)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1701._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x10A8
@scena.Code('func_0E_10A8')
def func_0E_10A8():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(46500, 200, -46100, 0)
    SetChrPos(0x0101, 47000, 200, -46600, 180)
    SetChrPos(0x0102, 46000, 200, -46600, 180)
    SetChrPos(0x00F8, 47000, 200, -45600, 180)
    SetChrPos(0x00F9, 46000, 200, -45600, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(46630, 200, -48040, 0)
    SetChrPos(0x0000, 46630, 200, -48040, 180)
    SetChrPos(0x0001, 46630, 200, -48040, 180)
    SetChrPos(0x0002, 46630, 200, -48040, 180)
    SetChrPos(0x0003, 46630, 200, -48040, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000F offset: 0x11A8
@scena.Code('func_0F_11A8')
def func_0F_11A8():
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
    OP_6D(46500, 200, -46100, 0)
    SetChrPos(0x0101, 46000, 200, -45600, 0)
    SetChrPos(0x0102, 47000, 200, -45600, 0)
    SetChrPos(0x00F8, 46000, 200, -46600, 0)
    SetChrPos(0x00F9, 47000, 200, -46600, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1701._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x1220
@scena.Code('func_10_1220')
def func_10_1220():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-46500, 200, -46000, 0)
    SetChrPos(0x0101, -46000, 200, -46500, 180)
    SetChrPos(0x0102, -47000, 200, -46500, 180)
    SetChrPos(0x00F8, -46000, 200, -45500, 180)
    SetChrPos(0x00F9, -47000, 200, -45500, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(-46470, 200, -47980, 0)
    SetChrPos(0x0000, -46470, 200, -47980, 180)
    SetChrPos(0x0001, -46470, 200, -47980, 180)
    SetChrPos(0x0002, -46470, 200, -47980, 180)
    SetChrPos(0x0003, -46470, 200, -47980, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0011 offset: 0x1320
@scena.Code('func_11_1320')
def func_11_1320():
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
    OP_6D(-46500, 200, -46000, 0)
    SetChrPos(0x0101, -47000, 200, -45500, 0)
    SetChrPos(0x0102, -46000, 200, -45500, 0)
    SetChrPos(0x00F8, -47000, 200, -46500, 0)
    SetChrPos(0x00F9, -46000, 200, -46500, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1701._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x1398
@scena.Code('func_12_1398')
def func_12_1398():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x0101, 500, 200, 66000, 180)
    SetChrPos(0x0102, -500, 200, 66000, 180)
    SetChrPos(0x00F8, 500, 200, 67000, 180)
    SetChrPos(0x00F9, -500, 200, 67000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(130, 200, 64560, 0)
    SetChrPos(0x0000, 130, 200, 64560, 180)
    SetChrPos(0x0001, 130, 200, 64560, 180)
    SetChrPos(0x0002, 130, 200, 64560, 180)
    SetChrPos(0x0003, 130, 200, 64560, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0013 offset: 0x1498
@scena.Code('func_13_1498')
def func_13_1498():
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
    OP_6D(0, 200, 66500, 0)
    SetChrPos(0x0101, -500, 200, 67000, 0)
    SetChrPos(0x0102, 500, 200, 67000, 0)
    SetChrPos(0x00F8, -500, 200, 66000, 0)
    SetChrPos(0x00F9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1703._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x1510
@scena.Code('func_14_1510')
def func_14_1510():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-96100, 200, 96700, 0)
    SetChrPos(0x0101, -95600, 200, 96200, 180)
    SetChrPos(0x0102, -96600, 200, 96200, 180)
    SetChrPos(0x00F8, -95600, 200, 97200, 180)
    SetChrPos(0x00F9, -96600, 200, 97200, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(-96090, 200, 94660, 0)
    SetChrPos(0x0000, -96090, 200, 94660, 180)
    SetChrPos(0x0001, -96090, 200, 94660, 180)
    SetChrPos(0x0002, -96090, 200, 94660, 180)
    SetChrPos(0x0003, -96090, 200, 94660, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0015 offset: 0x1610
@scena.Code('func_15_1610')
def func_15_1610():
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
    OP_6D(-96100, 200, 96700, 0)
    SetChrPos(0x0101, -96600, 200, 97200, 0)
    SetChrPos(0x0102, -95600, 200, 97200, 0)
    SetChrPos(0x00F8, -96600, 200, 96200, 0)
    SetChrPos(0x00F9, -95600, 200, 96200, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1703._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x1688
@scena.Code('func_16_1688')
def func_16_1688():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(96200, 200, 96700, 0)
    SetChrPos(0x0101, 96700, 200, 96200, 180)
    SetChrPos(0x0102, 95700, 200, 96200, 180)
    SetChrPos(0x00F8, 96700, 200, 97200, 180)
    SetChrPos(0x00F9, 95700, 200, 97200, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(96270, 200, 94740, 0)
    SetChrPos(0x0000, 96270, 200, 94740, 180)
    SetChrPos(0x0001, 96270, 200, 94740, 180)
    SetChrPos(0x0002, 96270, 200, 94740, 180)
    SetChrPos(0x0003, 96270, 200, 94740, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0017 offset: 0x1788
@scena.Code('func_17_1788')
def func_17_1788():
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
    OP_6D(96200, 200, 96700, 0)
    SetChrPos(0x0101, 95700, 200, 97200, 0)
    SetChrPos(0x0102, 96700, 200, 97200, 0)
    SetChrPos(0x00F8, 95700, 200, 96200, 0)
    SetChrPos(0x00F9, 96700, 200, 96200, 0)
    OP_0D()
    Call(0, 0x001C)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1703._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x1800
@scena.Code('func_18_1800')
def func_18_1800():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 95500, 200, -96000, 0)
    SetChrPos(0x0102, 96500, 200, -96000, 0)
    SetChrPos(0x00F8, 95500, 200, -97000, 0)
    SetChrPos(0x00F9, 96500, 200, -97000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(95950, 200, -94510, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, 95950, 200, -94510, 0)
    SetChrPos(0x0001, 95950, 200, -94510, 0)
    SetChrPos(0x0002, 95950, 200, -94510, 0)
    SetChrPos(0x0003, 95950, 200, -94510, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0019 offset: 0x1912
@scena.Code('func_19_1912')
def func_19_1912():
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
    OP_6D(96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 96500, 200, -97000, 180)
    SetChrPos(0x0102, 95500, 200, -97000, 180)
    SetChrPos(0x00F8, 96500, 200, -96000, 180)
    SetChrPos(0x00F9, 95500, 200, -96000, 180)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1703._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x1993
@scena.Code('func_1A_1993')
def func_1A_1993():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -96500, 200, -96000, 0)
    SetChrPos(0x0102, -95500, 200, -96000, 0)
    SetChrPos(0x00F8, -96500, 200, -97000, 0)
    SetChrPos(0x00F9, -95500, 200, -97000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001E)
    Fade(500)
    OP_6D(-96080, 200, -94480, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, -96080, 200, -94480, 0)
    SetChrPos(0x0001, -96080, 200, -94480, 0)
    SetChrPos(0x0002, -96080, 200, -94480, 0)
    SetChrPos(0x0003, -96080, 200, -94480, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x001B offset: 0x1AA5
@scena.Code('func_1B_1AA5')
def func_1B_1AA5():
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
    OP_6D(-96000, 200, -96500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -95500, 200, -97000, 180)
    SetChrPos(0x0102, -96500, 200, -97000, 180)
    SetChrPos(0x00F8, -95500, 200, -96000, 180)
    SetChrPos(0x00F9, -96500, 200, -96000, 180)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    NewScene('ED6_DT21/C1703._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x1B26
@scena.Code('func_1C_1B26')
def func_1C_1B26():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x001D offset: 0x1C05
@scena.Code('func_1D_1C05')
def func_1D_1C05():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x001E offset: 0x1CE4
@scena.Code('func_1E_1CE4')
def func_1E_1CE4():
    @scena.Lambda('lambda_1CEA')
    def lambda_1CEA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1CEA)

    @scena.Lambda('lambda_1CFC')
    def lambda_1CFC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1CFC)

    @scena.Lambda('lambda_1D0E')
    def lambda_1D0E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1D0E)

    @scena.Lambda('lambda_1D20')
    def lambda_1D20():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1D20)

    Sleep(2500)

    Return()

# id: 0x001F offset: 0x1D32
@scena.Code('func_1F_1D32')
def func_1F_1D32():
    @scena.Lambda('lambda_1D38')
    def lambda_1D38():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1D38)

    @scena.Lambda('lambda_1D4A')
    def lambda_1D4A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1D4A)

    @scena.Lambda('lambda_1D5C')
    def lambda_1D5C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1D5C)

    @scena.Lambda('lambda_1D6E')
    def lambda_1D6E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1D6E)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
