import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1704_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1704   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1704.x'
    header.mapIndex       = 1
    header.bgm            = 60
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

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -6050,
            z           = 400,
            y           = 21750,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E90,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5470,
            z           = 400,
            y           = 22210,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E91,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -340,
            z           = 400,
            y           = -13040,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1E92,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -59670,
            z           = 8400,
            y           = 86010,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E93,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -79990,
            z           = 4800,
            y           = 31890,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E94,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -68390,
            z           = 4800,
            y           = 31970,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1E95,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 79410,
            z           = 4800,
            y           = 31630,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E96,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 68430,
            z           = 4800,
            y           = 32280,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E97,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 58010,
            z           = 8400,
            y           = 90210,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1E98,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x216
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x216
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 10,
            triggerZ            = 0,
            triggerY            = 22700,
            triggerRange        = 1000,
            actorX              = 10,
            actorZ              = 0,
            actorY              = 21910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = 0,
            triggerY            = -7300,
            triggerRange        = 1000,
            actorX              = -20,
            actorZ              = 0,
            actorY              = -7870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -53290,
            triggerZ            = 8000,
            triggerY            = 86010,
            triggerRange        = 1000,
            actorX              = -54000,
            actorZ              = 8000,
            actorY              = 86010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -74010,
            triggerZ            = 4400,
            triggerY            = 32710,
            triggerRange        = 1000,
            actorX              = -74010,
            actorZ              = 4400,
            actorY              = 32049,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 74030,
            triggerZ            = 4400,
            triggerY            = 32710,
            triggerRange        = 1000,
            actorX              = 74030,
            actorZ              = 4400,
            actorY              = 32090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53290,
            triggerZ            = 8000,
            triggerY            = 86000,
            triggerRange        = 1000,
            actorX              = 53910,
            actorZ              = 8000,
            actorY              = 86000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = -7600,
            triggerY            = 5160,
            triggerRange        = 1000,
            actorX              = 40000,
            actorZ              = -7600,
            actorY              = 5160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -40000,
            triggerZ            = -7600,
            triggerY            = 4800,
            triggerRange        = 1000,
            actorX              = -40000,
            actorZ              = -7600,
            actorY              = 4800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 0,
            triggerY            = 66820,
            triggerRange        = 1000,
            actorX              = 40000,
            actorZ              = 0,
            actorY              = 66820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -39900,
            triggerZ            = 0,
            triggerY            = 67320,
            triggerRange        = 1000,
            actorX              = -39900,
            actorZ              = 0,
            actorY              = 67320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3860,
            triggerZ            = 4800,
            triggerY            = -34670,
            triggerRange        = 1200,
            actorX              = 3860,
            actorZ              = 6000,
            actorY              = -34670,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3A2
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3C2'),
        (0x00000065, 'loc_3C9'),
        (0x00000066, 'loc_3D0'),
        (0x00000067, 'loc_3D7'),
        (0x00000068, 'loc_3DE'),
        (0x00000069, 'loc_3E5'),
        (-1, 'loc_3EC'),
    )

    def _loc_3C2(): pass

    label('loc_3C2')

    Event(0, func_0D_22CB)

    Jump('loc_3EC')

    def _loc_3C9(): pass

    label('loc_3C9')

    Event(0, func_0F_2443)

    Jump('loc_3EC')

    def _loc_3D0(): pass

    label('loc_3D0')

    Event(0, func_11_25BB)

    Jump('loc_3EC')

    def _loc_3D7(): pass

    label('loc_3D7')

    Event(0, func_13_274E)

    Jump('loc_3EC')

    def _loc_3DE(): pass

    label('loc_3DE')

    Event(0, func_15_28E1)

    Jump('loc_3EC')

    def _loc_3E5(): pass

    label('loc_3E5')

    Event(0, func_17_2A59)

    Jump('loc_3EC')

    def _loc_3EC(): pass

    label('loc_3EC')

    Return()

# id: 0x0001 offset: 0x3ED
@scena.Code('func_01_3ED')
def func_01_3ED():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 2, 0x1FB2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FF',
    )

    OP_6F(0x0022, 0)

    Jump('loc_406')

    def _loc_3FF(): pass

    label('loc_3FF')

    OP_6F(0x0022, 60)

    def _loc_406(): pass

    label('loc_406')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 3, 0x1FB3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_418',
    )

    OP_6F(0x0023, 0)

    Jump('loc_41F')

    def _loc_418(): pass

    label('loc_418')

    OP_6F(0x0023, 60)

    def _loc_41F(): pass

    label('loc_41F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 4, 0x1FB4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_431',
    )

    OP_6F(0x0024, 0)

    Jump('loc_438')

    def _loc_431(): pass

    label('loc_431')

    OP_6F(0x0024, 60)

    def _loc_438(): pass

    label('loc_438')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 5, 0x1FB5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44A',
    )

    OP_6F(0x0025, 0)

    Jump('loc_451')

    def _loc_44A(): pass

    label('loc_44A')

    OP_6F(0x0025, 60)

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 6, 0x1FB6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_463',
    )

    OP_6F(0x0026, 0)

    Jump('loc_46A')

    def _loc_463(): pass

    label('loc_463')

    OP_6F(0x0026, 60)

    def _loc_46A(): pass

    label('loc_46A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 7, 0x1FB7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47C',
    )

    OP_6F(0x0027, 0)

    Jump('loc_483')

    def _loc_47C(): pass

    label('loc_47C')

    OP_6F(0x0027, 60)

    def _loc_483(): pass

    label('loc_483')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 0, 0x1E90)),
            Expr.Return,
        ),
        'loc_4B7',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_4B7(): pass

    label('loc_4B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 1, 0x1E91)),
            Expr.Return,
        ),
        'loc_4C3',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 2, 0x1E92)),
            Expr.Return,
        ),
        'loc_4CF',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_4CF(): pass

    label('loc_4CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 3, 0x1E93)),
            Expr.Return,
        ),
        'loc_4DB',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_4DB(): pass

    label('loc_4DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 4, 0x1E94)),
            Expr.Return,
        ),
        'loc_4E7',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_4E7(): pass

    label('loc_4E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 5, 0x1E95)),
            Expr.Return,
        ),
        'loc_4F3',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_4F3(): pass

    label('loc_4F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 6, 0x1E96)),
            Expr.Return,
        ),
        'loc_4FF',
    )

    ChrSetFlags(0x000E, 0x0080)

    def _loc_4FF(): pass

    label('loc_4FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D2, 7, 0x1E97)),
            Expr.Return,
        ),
        'loc_50B',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 0, 0x1E98)),
            Expr.Return,
        ),
        'loc_517',
    )

    ChrSetFlags(0x0010, 0x0080)

    def _loc_517(): pass

    label('loc_517')

    Call(0, 0x0008)
    OP_1B(0x00, 0x00, 0x000E)
    OP_1B(0x01, 0x00, 0x0010)
    OP_1B(0x02, 0x00, 0x0012)
    OP_1B(0x03, 0x00, 0x0014)
    OP_1B(0x04, 0x00, 0x0016)
    OP_1B(0x05, 0x00, 0x0018)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A4',
    )

    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 3860, 6000, -34670, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_71(0x002A, 0x0020)
    OP_6F(0x002A, 0)
    OP_70(0x002A, 250)

    Jump('loc_5B0')

    def _loc_5A4(): pass

    label('loc_5A4')

    OP_72(0x002A, 0x0020)
    OP_6F(0x002A, 250)

    def _loc_5B0(): pass

    label('loc_5B0')

    Return()

# id: 0x0002 offset: 0x5B1
@scena.Code('func_02_5B1')
def func_02_5B1():
    UnlockAchievement(0x02, 0x007F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 2, 0x1FB2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0022, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['翠耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_625',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['翠耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F6, 2, 0x1FB2))

    Jump('loc_68B')

    def _loc_625(): pass

    label('loc_625')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['翠耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['翠耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0022, 60)
    OP_70(0x0022, 0)

    def _loc_68B(): pass

    label('loc_68B')

    Jump('loc_6BF')

    def _loc_68E(): pass

    label('loc_68E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_6BF(): pass

    label('loc_6BF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x6CD
@scena.Code('func_03_6CD')
def func_03_6CD():
    UnlockAchievement(0x02, 0x0080, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 3, 0x1FB3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0023, 30)
    OP_73(0x0023)
    OP_6F(0x0023, 30)
    AddSepith(0x00, 300)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
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
    SetScenaFlags(ScenaFlag(0x03F6, 3, 0x1FB3))

    Jump('loc_7BC')

    def _loc_7A2(): pass

    label('loc_7A2')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_7BC(): pass

    label('loc_7BC')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x7CE
@scena.Code('func_04_7CE')
def func_04_7CE():
    UnlockAchievement(0x02, 0x0081, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 4, 0x1FB4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8AB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0024, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_842',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F6, 4, 0x1FB4))

    Jump('loc_8A8')

    def _loc_842(): pass

    label('loc_842')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0024, 60)
    OP_70(0x0024, 0)

    def _loc_8A8(): pass

    label('loc_8A8')

    Jump('loc_8DC')

    def _loc_8AB(): pass

    label('loc_8AB')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_8DC(): pass

    label('loc_8DC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x8EA
@scena.Code('func_05_8EA')
def func_05_8EA():
    UnlockAchievement(0x02, 0x0082, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 5, 0x1FB5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9C7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0025, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_95E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x03F6, 5, 0x1FB5))

    Jump('loc_9C4')

    def _loc_95E(): pass

    label('loc_95E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0025, 60)
    OP_70(0x0025, 0)

    def _loc_9C4(): pass

    label('loc_9C4')

    Jump('loc_9F8')

    def _loc_9C7(): pass

    label('loc_9C7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_9F8(): pass

    label('loc_9F8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xA06
@scena.Code('func_06_A06')
def func_06_A06():
    UnlockAchievement(0x02, 0x0083, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 6, 0x1FB6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AE3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0026, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['罗汉杖'], 1)"),
            Expr.Return,
        ),
        'loc_A7A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['罗汉杖']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F6, 6, 0x1FB6))

    Jump('loc_AE0')

    def _loc_A7A(): pass

    label('loc_A7A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['罗汉杖']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['罗汉杖']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0026, 60)
    OP_70(0x0026, 0)

    def _loc_AE0(): pass

    label('loc_AE0')

    Jump('loc_B14')

    def _loc_AE3(): pass

    label('loc_AE3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_B14(): pass

    label('loc_B14')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xB22
@scena.Code('func_07_B22')
def func_07_B22():
    UnlockAchievement(0x02, 0x0084, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 7, 0x1FB7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BFF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0027, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_B96',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x03F6, 7, 0x1FB7))

    Jump('loc_BFC')

    def _loc_B96(): pass

    label('loc_B96')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0027, 60)
    OP_70(0x0027, 0)

    def _loc_BFC(): pass

    label('loc_BFC')

    Jump('loc_C30')

    def _loc_BFF(): pass

    label('loc_BFF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_C30(): pass

    label('loc_C30')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xC3E
@scena.Code('func_08_C3E')
def func_08_C3E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 3, 0x1E23)),
            Expr.Return,
        ),
        'loc_CD0',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    Jump('loc_D58')

    def _loc_CD0(): pass

    label('loc_CD0')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    def _loc_D58(): pass

    label('loc_D58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 2, 0x1E32)),
            Expr.Return,
        ),
        'loc_DEA',
    )

    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_72(0x000A, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_72(0x000C, 0x0008)
    OP_72(0x000D, 0x0008)
    OP_72(0x000E, 0x0008)
    OP_72(0x000F, 0x0008)
    OP_6F(0x0008, 360)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6F(0x000F, 0)

    Jump('loc_E72')

    def _loc_DEA(): pass

    label('loc_DEA')

    OP_72(0x0008, 0x0020)
    OP_72(0x0009, 0x0020)
    OP_72(0x000A, 0x0020)
    OP_72(0x000B, 0x0020)
    OP_72(0x000C, 0x0020)
    OP_72(0x000D, 0x0020)
    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_72(0x0008, 0x0008)
    OP_72(0x0009, 0x0008)
    OP_72(0x000A, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_72(0x000C, 0x0008)
    OP_72(0x000D, 0x0008)
    OP_72(0x000E, 0x0008)
    OP_72(0x000F, 0x0008)
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6F(0x000F, 0)

    def _loc_E72(): pass

    label('loc_E72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 3, 0x1E33)),
            Expr.Return,
        ),
        'loc_F15',
    )

    OP_72(0x0019, 0x0020)
    OP_72(0x001A, 0x0020)
    OP_72(0x001B, 0x0020)
    OP_72(0x001C, 0x0020)
    OP_72(0x001D, 0x0020)
    OP_72(0x001E, 0x0020)
    OP_72(0x001F, 0x0020)
    OP_72(0x0020, 0x0020)
    OP_72(0x0021, 0x0020)
    OP_72(0x0019, 0x0008)
    OP_72(0x001A, 0x0008)
    OP_72(0x001B, 0x0008)
    OP_72(0x001C, 0x0008)
    OP_72(0x001D, 0x0008)
    OP_72(0x001E, 0x0008)
    OP_72(0x001F, 0x0008)
    OP_72(0x0020, 0x0008)
    OP_72(0x0021, 0x0008)
    OP_6F(0x0019, 360)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6F(0x0020, 0)
    OP_6F(0x0021, 0)

    Jump('loc_FAE')

    def _loc_F15(): pass

    label('loc_F15')

    OP_72(0x0019, 0x0020)
    OP_72(0x001A, 0x0020)
    OP_72(0x001B, 0x0020)
    OP_72(0x001C, 0x0020)
    OP_72(0x001D, 0x0020)
    OP_72(0x001E, 0x0020)
    OP_72(0x001F, 0x0020)
    OP_72(0x0020, 0x0020)
    OP_72(0x0021, 0x0020)
    OP_72(0x0019, 0x0008)
    OP_72(0x001A, 0x0008)
    OP_72(0x001B, 0x0008)
    OP_72(0x001C, 0x0008)
    OP_72(0x001D, 0x0008)
    OP_72(0x001E, 0x0008)
    OP_72(0x001F, 0x0008)
    OP_72(0x0020, 0x0008)
    OP_72(0x0021, 0x0008)
    OP_6F(0x0019, 0)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6F(0x0020, 0)
    OP_6F(0x0021, 0)

    def _loc_FAE(): pass

    label('loc_FAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 4, 0x1E34)),
            Expr.Return,
        ),
        'loc_1051',
    )

    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x0012, 0x0020)
    OP_72(0x0013, 0x0020)
    OP_72(0x0014, 0x0020)
    OP_72(0x0015, 0x0020)
    OP_72(0x0016, 0x0020)
    OP_72(0x0017, 0x0020)
    OP_72(0x0018, 0x0020)
    OP_72(0x0010, 0x0008)
    OP_72(0x0011, 0x0008)
    OP_72(0x0012, 0x0008)
    OP_72(0x0013, 0x0008)
    OP_72(0x0014, 0x0008)
    OP_72(0x0015, 0x0008)
    OP_72(0x0016, 0x0008)
    OP_72(0x0017, 0x0008)
    OP_72(0x0018, 0x0008)
    OP_6F(0x0010, 360)
    OP_6F(0x0011, 0)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6F(0x0018, 0)

    Jump('loc_10EA')

    def _loc_1051(): pass

    label('loc_1051')

    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x0012, 0x0020)
    OP_72(0x0013, 0x0020)
    OP_72(0x0014, 0x0020)
    OP_72(0x0015, 0x0020)
    OP_72(0x0016, 0x0020)
    OP_72(0x0017, 0x0020)
    OP_72(0x0018, 0x0020)
    OP_72(0x0010, 0x0008)
    OP_72(0x0011, 0x0008)
    OP_72(0x0012, 0x0008)
    OP_72(0x0013, 0x0008)
    OP_72(0x0014, 0x0008)
    OP_72(0x0015, 0x0008)
    OP_72(0x0016, 0x0008)
    OP_72(0x0017, 0x0008)
    OP_72(0x0018, 0x0008)
    OP_6F(0x0010, 0)
    OP_6F(0x0011, 0)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6F(0x0018, 0)

    def _loc_10EA(): pass

    label('loc_10EA')

    Return()

# id: 0x0009 offset: 0x10EB
@scena.Code('func_09_10EB')
def func_09_10EB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 3, 0x1E23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13BE',
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

    PlaySE(156, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_70(0x0000, 360)
    Sleep(2500)

    PlaySE(157, 0x00, 0x64)
    OP_B0(0x0004, 0x64)
    OP_B0(0x0005, 0x64)
    OP_B0(0x0006, 0x64)
    OP_B0(0x0007, 0x64)
    OP_70(0x0004, 240)
    Sleep(100)

    OP_70(0x0005, 240)
    Sleep(100)

    OP_70(0x0006, 240)
    Sleep(100)

    OP_70(0x0007, 240)
    Sleep(100)

    PlaySE(185, 0x00, 0x64)
    OP_B0(0x0001, 0x64)
    OP_B0(0x0002, 0x64)
    OP_B0(0x0003, 0x64)
    OP_70(0x0001, 360)
    OP_70(0x0002, 360)
    OP_70(0x0003, 360)
    OP_73(0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于设备塔（１／４）』\n',
            '　\n',
            '■第一■界』■■启■■，\n',
            '我们■■■■了\n',
            '在■■元里对■环■『■间冻结』。\n',
            '　\n',
            '但■，正如■■■示\n',
            '『■■计划』■■■■\n',
            '■止这■个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■封印计■』最后的■■■『■二■界■。\n',
            '　\n',
            '■■■■■\n',
            '■■■掌握着■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶１２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１２'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 3, 0x1E23))
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
    CameraMove(39870, -7400, 2790, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 39870, -7400, 2790, 0)
    ChrSetPos(0x0001, 39870, -7400, 2790, 0)
    ChrSetPos(0x0002, 39870, -7400, 2790, 0)
    ChrSetPos(0x0003, 39870, -7400, 2790, 0)
    OP_69(0x0000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_14F0')

    def _loc_13BE(): pass

    label('loc_13BE')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于设备塔（１／４）』\n',
            '　\n',
            '■第一■界』■■启■■，\n',
            '我们■■■■了\n',
            '在■■元里对■环■『■间冻结』。\n',
            '　\n',
            '但■，正如■■■示\n',
            '『■■计划』■■■■\n',
            '■止这■个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■封印计■』最后的■■■『■二■界■。\n',
            '　\n',
            '■■■■■\n',
            '■■■掌握着■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_14F0(): pass

    label('loc_14F0')

    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x14F4
@scena.Code('func_0A_14F4')
def func_0A_14F4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 2, 0x1E32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D7',
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

    PlaySE(156, 0x00, 0x64)
    OP_B0(0x0008, 0x78)
    OP_70(0x0008, 360)
    Sleep(2500)

    PlaySE(157, 0x00, 0x64)
    OP_B0(0x000C, 0x64)
    OP_B0(0x000D, 0x64)
    OP_B0(0x000E, 0x64)
    OP_B0(0x000F, 0x64)
    OP_70(0x000C, 240)
    Sleep(100)

    OP_70(0x000D, 240)
    Sleep(100)

    OP_70(0x000E, 240)
    Sleep(100)

    OP_70(0x000F, 240)
    Sleep(100)

    PlaySE(185, 0x00, 0x64)
    OP_B0(0x0009, 0x64)
    OP_B0(0x000A, 0x64)
    OP_B0(0x000B, 0x64)
    OP_B0(0x0009, 0x64)
    OP_B0(0x000A, 0x64)
    OP_B0(0x000B, 0x64)
    OP_70(0x0009, 360)
    OP_70(0x000A, 360)
    OP_70(0x000B, 360)
    OP_73(0x0009)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于设备塔（２／４）』\n',
            '　\n',
            '■■机■在『■■■■』被解除\n',
            '■环■的时间■■开始■■之时\n',
            '■动。\n',
            '　\n',
            '『■二■界』\n',
            '■■『重力结■』，\n',
            '有着在异■■中\n',
            '■■■■的机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S如果『环』■■活动\n',
            '它可以用■力之楔将其维在■次元，\n',
            '■■■■它在世■出现',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶１３']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１３'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 2, 0x1E32))
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0008, 360)
    OP_6F(0x0009, 0)
    OP_6F(0x000A, 0)
    OP_6F(0x000B, 0)
    OP_6F(0x000C, 0)
    OP_6F(0x000D, 0)
    OP_6F(0x000E, 0)
    OP_6F(0x000F, 0)
    CameraMove(-40200, -7400, 2800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -40200, -7400, 2800, 0)
    ChrSetPos(0x0001, -40200, -7400, 2800, 0)
    ChrSetPos(0x0002, -40200, -7400, 2800, 0)
    ChrSetPos(0x0003, -40200, -7400, 2800, 0)
    OP_69(0x0000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_190D')

    def _loc_17D7(): pass

    label('loc_17D7')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于设备塔（２／４）』\n',
            '　\n',
            '■■机■在『■■■■』被解除\n',
            '■环■的时间■■开始■■之时\n',
            '■动。\n',
            '　\n',
            '『■二■界』\n',
            '■■『重力结■』，\n',
            '有着在异■■中\n',
            '■■■■的机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S如果『环』■■活动\n',
            '它可以用■力之楔将其维在■次元，\n',
            '■■■■它在世■出现',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_190D(): pass

    label('loc_190D')

    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x1911
@scena.Code('func_0B_1911')
def func_0B_1911():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 3, 0x1E33)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C2C',
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

    PlaySE(156, 0x00, 0x64)
    OP_B0(0x0019, 0x78)
    OP_70(0x0019, 360)
    Sleep(2500)

    PlaySE(157, 0x00, 0x64)
    OP_B0(0x001D, 0x64)
    OP_B0(0x001E, 0x64)
    OP_B0(0x001F, 0x64)
    OP_B0(0x0020, 0x64)
    OP_B0(0x0021, 0x64)
    OP_70(0x001D, 240)
    Sleep(100)

    OP_70(0x001E, 240)
    Sleep(100)

    OP_70(0x001F, 240)
    Sleep(100)

    OP_70(0x0020, 240)
    Sleep(100)

    OP_70(0x0021, 240)
    Sleep(100)

    PlaySE(185, 0x00, 0x64)
    OP_B0(0x001A, 0x64)
    OP_B0(0x001B, 0x64)
    OP_B0(0x001C, 0x64)
    OP_70(0x001A, 360)
    OP_70(0x001B, 360)
    OP_70(0x001C, 360)
    OP_73(0x001A)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于数据塔（３／４）』\n',
            '　\n',
            '『第二结界■启动■时候，\n',
            '『■』已经■■■■转。\n',
            '　\n',
            '如果使用那个■为■■■■的■■，\n',
            '■■■随心所欲地■提取■■力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S残留在■■贝■＝■克』中的\n',
            '■■音』\n',
            '■■■■■■■印■。\n',
            '　\n',
            '但是，如果■■■现了\n',
            '相当于■■■■的东西，\n',
            '■环■的力量便会■■到■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶１４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１４'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 3, 0x1E33))
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0019, 360)
    OP_6F(0x001A, 0)
    OP_6F(0x001B, 0)
    OP_6F(0x001C, 0)
    OP_6F(0x001D, 0)
    OP_6F(0x001E, 0)
    OP_6F(0x001F, 0)
    OP_6F(0x0020, 0)
    OP_6F(0x0021, 0)
    CameraMove(39700, 200, 64819, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 39700, 200, 64819, 0)
    ChrSetPos(0x0001, 39700, 200, 64819, 0)
    ChrSetPos(0x0002, 39700, 200, 64819, 0)
    ChrSetPos(0x0003, 39700, 200, 64819, 0)
    OP_69(0x0000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_1D8F')

    def _loc_1C2C(): pass

    label('loc_1C2C')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于数据塔（３／４）』\n',
            '　\n',
            '『第二结界■启动■时候，\n',
            '『■』已经■■■■转。\n',
            '　\n',
            '如果使用那个■为■■■■的■■，\n',
            '■■■随心所欲地■提取■■力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S残留在■■贝■＝■克』中的\n',
            '■■音』\n',
            '■■■■■■■印■。\n',
            '　\n',
            '但是，如果■■■现了\n',
            '相当于■■■■的东西，\n',
            '■环■的力量便会■■到■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_1D8F(): pass

    label('loc_1D8F')

    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x1D93
@scena.Code('func_0C_1D93')
def func_0C_1D93():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C6, 4, 0x1E34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2109',
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

    PlaySE(156, 0x00, 0x64)
    OP_B0(0x0010, 0x78)
    OP_70(0x0010, 360)
    Sleep(2500)

    PlaySE(157, 0x00, 0x64)
    OP_B0(0x0014, 0x64)
    OP_B0(0x0015, 0x64)
    OP_B0(0x0016, 0x64)
    OP_B0(0x0017, 0x64)
    OP_B0(0x0018, 0x64)
    OP_70(0x0014, 240)
    Sleep(100)

    OP_70(0x0015, 240)
    Sleep(100)

    OP_70(0x0016, 240)
    Sleep(100)

    OP_70(0x0017, 240)
    Sleep(100)

    OP_70(0x0018, 240)
    Sleep(100)

    PlaySE(185, 0x00, 0x64)
    OP_B0(0x0011, 0x64)
    OP_B0(0x0012, 0x64)
    OP_B0(0x0013, 0x64)
    OP_70(0x0011, 360)
    OP_70(0x0012, 360)
    OP_70(0x0013, 360)
    OP_73(0x0013)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于数据塔（４／４）』\n',
            '　\n',
            '■■成功封印了『■』，\n',
            '但并没■■它的力量消失。\n',
            '　\n',
            '我■打算■根于此地，\n',
            '看守■■■。\n',
            '并且祈祷■■■■\n',
            '不被■■人看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■■此同时\n',
            '我们也■见，这是■■能的事。\n',
            '　\n',
            '『环■再次出■在世间■■■，\n',
            '生活于■世里的■■\n',
            '将做出■■■选择■－－\n',
            '　\n',
            '我们相信人类■不会■次■错，\n',
            '■■终有从■环■中■■■来的■■\n',
            '■■如此信念，■■将这些■■■付给■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶１５']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶１５'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 4, 0x1E34))
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0010, 360)
    OP_6F(0x0011, 0)
    OP_6F(0x0012, 0)
    OP_6F(0x0013, 0)
    OP_6F(0x0014, 0)
    OP_6F(0x0015, 0)
    OP_6F(0x0016, 0)
    OP_6F(0x0017, 0)
    OP_6F(0x0018, 0)
    CameraMove(-39880, 200, 64769, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -39880, 200, 64769, 0)
    ChrSetPos(0x0001, -39880, 200, 64769, 0)
    ChrSetPos(0x0002, -39880, 200, 64769, 0)
    ChrSetPos(0x0003, -39880, 200, 64769, 0)
    OP_69(0x0000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Jump('loc_22C7')

    def _loc_2109(): pass

    label('loc_2109')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『关于数据塔（４／４）』\n',
            '　\n',
            '■■成功封印了『■』，\n',
            '但并没■■它的力量消失。\n',
            '　\n',
            '我■打算■根于此地，\n',
            '看守■■■。\n',
            '并且祈祷■■■■\n',
            '不被■■人看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S■■■此同时\n',
            '我们也■见，这是■■能的事。\n',
            '　\n',
            '『环■再次出■在世间■■■，\n',
            '生活于■世里的■■\n',
            '将做出■■■选择■－－\n',
            '　\n',
            '我们相信人类■不会■次■错，\n',
            '■■终有从■环■中■■■来的■■\n',
            '■■如此信念，■■将这些■■■付给■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_22C7(): pass

    label('loc_22C7')

    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x22CB
@scena.Code('func_0D_22CB')
def func_0D_22CB():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 250, 52600, 0)
    ChrSetPos(0x0101, 500, 250, 52100, 180)
    ChrSetPos(0x0102, -500, 250, 52100, 180)
    ChrSetPos(0x00F8, 500, 250, 53100, 180)
    ChrSetPos(0x00F9, -500, 250, 53100, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    Fade(500)
    CameraMove(50, 250, 50650, 0)
    ChrSetPos(0x0000, 50, 250, 50650, 180)
    ChrSetPos(0x0001, 50, 250, 50650, 180)
    ChrSetPos(0x0002, 50, 250, 50650, 180)
    ChrSetPos(0x0003, 50, 250, 50650, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000E offset: 0x23CB
@scena.Code('func_0E_23CB')
def func_0E_23CB():
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
    CameraMove(0, 250, 52600, 0)
    ChrSetPos(0x0101, -500, 250, 53100, 0)
    ChrSetPos(0x0102, 500, 250, 53100, 0)
    ChrSetPos(0x00F8, -500, 250, 52100, 0)
    ChrSetPos(0x00F9, 500, 250, 52100, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001C)
    NewScene('ED6_DT21/C1703._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x2443
@scena.Code('func_0F_2443')
def func_0F_2443():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-15500, 250, 68000, 0)
    ChrSetPos(0x0101, -16000, 250, 67500, 270)
    ChrSetPos(0x0102, -16000, 250, 68500, 270)
    ChrSetPos(0x00F8, -15000, 250, 67500, 270)
    ChrSetPos(0x00F9, -15000, 250, 68500, 270)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    Fade(500)
    CameraMove(-17580, 250, 67930, 0)
    ChrSetPos(0x0000, -17580, 250, 67930, 270)
    ChrSetPos(0x0001, -17580, 250, 67930, 270)
    ChrSetPos(0x0002, -17580, 250, 67930, 270)
    ChrSetPos(0x0003, -17580, 250, 67930, 270)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0010 offset: 0x2543
@scena.Code('func_10_2543')
def func_10_2543():
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
    CameraMove(-15500, 250, 68000, 0)
    ChrSetPos(0x0101, -15000, 250, 68500, 90)
    ChrSetPos(0x0102, -15000, 250, 67500, 90)
    ChrSetPos(0x00F8, -16000, 250, 68500, 90)
    ChrSetPos(0x00F9, -16000, 250, 67500, 90)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001C)
    NewScene('ED6_DT21/C1703._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x25BB
@scena.Code('func_11_25BB')
def func_11_25BB():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(15500, 250, 68000, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 16000, 250, 68500, 90)
    ChrSetPos(0x0102, 16000, 250, 67500, 90)
    ChrSetPos(0x00F8, 15000, 250, 68500, 90)
    ChrSetPos(0x00F9, 15000, 250, 67500, 90)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    Fade(500)
    CameraMove(17480, 250, 68100, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, 17480, 250, 68100, 90)
    ChrSetPos(0x0001, 17480, 250, 68100, 90)
    ChrSetPos(0x0002, 17480, 250, 68100, 90)
    ChrSetPos(0x0003, 17480, 250, 68100, 90)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0012 offset: 0x26CD
@scena.Code('func_12_26CD')
def func_12_26CD():
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
    CameraMove(15500, 250, 68000, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 15000, 250, 67500, 270)
    ChrSetPos(0x0102, 15000, 250, 68500, 270)
    ChrSetPos(0x00F8, 16000, 250, 67500, 270)
    ChrSetPos(0x00F9, 16000, 250, 68500, 270)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001C)
    NewScene('ED6_DT21/C1703._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x274E
@scena.Code('func_13_274E')
def func_13_274E():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(21500, 8200, 86000, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 22000, 8200, 86500, 90)
    ChrSetPos(0x0102, 22000, 8200, 85500, 90)
    ChrSetPos(0x00F8, 21000, 8200, 86500, 90)
    ChrSetPos(0x00F9, 21000, 8200, 85500, 90)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    Fade(500)
    CameraMove(23620, 8200, 86140, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, 23620, 8200, 86140, 90)
    ChrSetPos(0x0001, 23620, 8200, 86140, 90)
    ChrSetPos(0x0002, 23620, 8200, 86140, 90)
    ChrSetPos(0x0003, 23620, 8200, 86140, 90)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0014 offset: 0x2860
@scena.Code('func_14_2860')
def func_14_2860():
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
    CameraMove(21500, 8200, 86000, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 21000, 8200, 85500, 270)
    ChrSetPos(0x0102, 21000, 8200, 86500, 270)
    ChrSetPos(0x00F8, 22000, 8200, 85500, 270)
    ChrSetPos(0x00F9, 22000, 8200, 86500, 270)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001C)
    NewScene('ED6_DT21/C1703._SN', 108, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x28E1
@scena.Code('func_15_28E1')
def func_15_28E1():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-21500, 8200, 86000, 0)
    ChrSetPos(0x0101, -22000, 8200, 85500, 270)
    ChrSetPos(0x0102, -22000, 8200, 86500, 270)
    ChrSetPos(0x00F8, -21000, 8200, 85500, 270)
    ChrSetPos(0x00F9, -21000, 8200, 86500, 270)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    Fade(500)
    CameraMove(-23480, 8200, 85910, 0)
    ChrSetPos(0x0000, -23480, 8200, 85910, 270)
    ChrSetPos(0x0001, -23480, 8200, 85910, 270)
    ChrSetPos(0x0002, -23480, 8200, 85910, 270)
    ChrSetPos(0x0003, -23480, 8200, 85910, 270)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0016 offset: 0x29E1
@scena.Code('func_16_29E1')
def func_16_29E1():
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
    CameraMove(-21500, 8200, 86000, 0)
    ChrSetPos(0x0101, -21000, 8200, 86500, 90)
    ChrSetPos(0x0102, -21000, 8200, 85500, 90)
    ChrSetPos(0x00F8, -22000, 8200, 86500, 90)
    ChrSetPos(0x00F9, -22000, 8200, 85500, 90)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001C)
    NewScene('ED6_DT21/C1703._SN', 109, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x2A59
@scena.Code('func_17_2A59')
def func_17_2A59():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 5550, -27800, 0)
    ChrSetPos(0x0101, 500, 5550, -28300, 180)
    ChrSetPos(0x0102, -500, 5550, -28300, 180)
    ChrSetPos(0x00F8, 500, 5550, -27300, 180)
    ChrSetPos(0x00F9, -500, 5550, -27300, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001B)
    Fade(500)
    CameraMove(20, 5200, -30080, 0)
    ChrSetPos(0x0000, 20, 5200, -30080, 180)
    ChrSetPos(0x0001, 20, 5200, -30080, 180)
    ChrSetPos(0x0002, 20, 5200, -30080, 180)
    ChrSetPos(0x0003, 20, 5200, -30080, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0018 offset: 0x2B59
@scena.Code('func_18_2B59')
def func_18_2B59():
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
    CameraMove(0, 5550, -27800, 0)
    ChrSetPos(0x0101, -500, 5550, -27300, 0)
    ChrSetPos(0x0102, 500, 5550, -27300, 0)
    ChrSetPos(0x00F8, -500, 5550, -28300, 0)
    ChrSetPos(0x00F9, 500, 5550, -28300, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001C)
    NewScene('ED6_DT21/C1705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x2BD1
@scena.Code('func_19_2BD1')
def func_19_2BD1():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001A offset: 0x2CB0
@scena.Code('func_1A_2CB0')
def func_1A_2CB0():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001B offset: 0x2D8F
@scena.Code('func_1B_2D8F')
def func_1B_2D8F():
    @scena.Lambda('lambda_2D95')
    def lambda_2D95():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2D95)

    @scena.Lambda('lambda_2DA7')
    def lambda_2DA7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2DA7)

    @scena.Lambda('lambda_2DB9')
    def lambda_2DB9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2DB9)

    @scena.Lambda('lambda_2DCB')
    def lambda_2DCB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2DCB)

    Sleep(2500)

    Return()

# id: 0x001C offset: 0x2DDD
@scena.Code('func_1C_2DDD')
def func_1C_2DDD():
    @scena.Lambda('lambda_2DE3')
    def lambda_2DE3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2DE3)

    @scena.Lambda('lambda_2DF5')
    def lambda_2DF5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2DF5)

    @scena.Lambda('lambda_2E07')
    def lambda_2E07():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2E07)

    @scena.Lambda('lambda_2E19')
    def lambda_2E19():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2E19)

    Sleep(2000)

    Return()

# id: 0x001D offset: 0x2E2B
@scena.Code('func_1D_2E2B')
def func_1D_2E2B():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E7E',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_3020')

    def _loc_2E7E(): pass

    label('loc_2E7E')

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
        'loc_3005',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x002A, 0x0020)
    OP_6F(0x002A, 300)
    OP_70(0x002A, 500)
    OP_73(0x002A)
    OP_6F(0x002A, 500)
    OP_70(0x002A, 700)
    OP_71(0x002A, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x03, 'map\\\\mp027_01.eff')
    PlayEffect(0x03, 0x03, 0x00FF, 3860, 6000, -34670, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x03, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, 3860, 6000, -34670, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x002A, 0)
    OP_70(0x002A, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_3005(): pass

    label('loc_3005')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_301F',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_301F(): pass

    label('loc_301F')

    Return()

    def _loc_3020(): pass

    label('loc_3020')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
