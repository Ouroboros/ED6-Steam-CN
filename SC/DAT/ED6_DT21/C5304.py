import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5304_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5304   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5304.x'
    header.mapIndex       = 1
    header.bgm            = 64
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
        ('ED6_DT29/CH12010._CH', 'ED6_DT29/CH12010P._CP'),
        ('ED6_DT29/CH12010._CH', 'ED6_DT29/CH12010P._CP'),
        ('ED6_DT29/CH12080._CH', 'ED6_DT29/CH12080P._CP'),
        ('ED6_DT29/CH12081._CH', 'ED6_DT29/CH12081P._CP'),
        ('ED6_DT29/CH12050._CH', 'ED6_DT29/CH12050P._CP'),
        ('ED6_DT29/CH12051._CH', 'ED6_DT29/CH12051P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
        ('ED6_DT29/CH12290._CH', 'ED6_DT29/CH12290P._CP'),
        ('ED6_DT29/CH12291._CH', 'ED6_DT29/CH12291P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '升降梯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -91790,
            z           = 2180,
            y           = 96980,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -98940,
            z           = 0,
            y           = 9760,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0528,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -80420,
            z           = 2250,
            y           = -72330,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -60,
            z           = 2000,
            y           = -94200,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 84020,
            z           = 2160,
            y           = -85480,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0529,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 102120,
            z           = 50,
            y           = 1620,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 91490,
            z           = 2130,
            y           = 96710,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0529,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1EE
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 5110,
            y           = -2000,
            z           = 110000,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10004 offset: 0x20E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 93700,
            triggerZ            = 0,
            triggerY            = -1910,
            triggerRange        = 1000,
            actorX              = 93040,
            actorZ              = 0,
            actorY              = -1950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 93750,
            triggerZ            = 0,
            triggerY            = 2080,
            triggerRange        = 1000,
            actorX              = 93060,
            actorZ              = 0,
            actorY              = 2040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 93710,
            triggerZ            = 0,
            triggerY            = 6100,
            triggerRange        = 1000,
            actorX              = 93040,
            actorZ              = 0,
            actorY              = 6070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110200,
            triggerZ            = 0,
            triggerY            = 5990,
            triggerRange        = 1000,
            actorX              = 110810,
            actorZ              = 0,
            actorY              = 6030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110190,
            triggerZ            = 0,
            triggerY            = 2060,
            triggerRange        = 1000,
            actorX              = 110860,
            actorZ              = 0,
            actorY              = 2090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110200,
            triggerZ            = 0,
            triggerY            = -2060,
            triggerRange        = 1000,
            actorX              = 110900,
            actorZ              = 0,
            actorY              = -2100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2E6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F6',
    )

    Event(0, func_09_BE4)

    def _loc_2F6(): pass

    label('loc_2F6')

    Return()

# id: 0x0001 offset: 0x2F7
@scena.Code('func_01_2F7')
def func_01_2F7():
    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xD7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 3, 0x237B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_335',
    )

    OP_6F(0x0001, 0)

    Jump('loc_33C')

    def _loc_335(): pass

    label('loc_335')

    OP_6F(0x0001, 60)

    def _loc_33C(): pass

    label('loc_33C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 5, 0x237D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_6F(0x0002, 0)

    Jump('loc_355')

    def _loc_34E(): pass

    label('loc_34E')

    OP_6F(0x0002, 60)

    def _loc_355(): pass

    label('loc_355')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 6, 0x237E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_367',
    )

    OP_6F(0x0003, 0)

    Jump('loc_36E')

    def _loc_367(): pass

    label('loc_367')

    OP_6F(0x0003, 60)

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 7, 0x237F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_380',
    )

    OP_6F(0x0004, 0)

    Jump('loc_387')

    def _loc_380(): pass

    label('loc_380')

    OP_6F(0x0004, 60)

    def _loc_387(): pass

    label('loc_387')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 1, 0x2381)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_399',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3A0')

    def _loc_399(): pass

    label('loc_399')

    OP_6F(0x0005, 60)

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 2, 0x2382)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B2',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3B9')

    def _loc_3B2(): pass

    label('loc_3B2')

    OP_6F(0x0006, 60)

    def _loc_3B9(): pass

    label('loc_3B9')

    OP_10(0x00, 0x00)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    PlaySE(320, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x3D3
@scena.Code('func_02_3D3')
def func_02_3D3():
    UnlockAchievement(0x02, 0x013C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 3, 0x237B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['闪耀宝玉'], 1)"),
            Expr.Return,
        ),
        'loc_447',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['闪耀宝玉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046F, 3, 0x237B))

    Jump('loc_4AD')

    def _loc_447(): pass

    label('loc_447')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['闪耀宝玉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['闪耀宝玉']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_4AD(): pass

    label('loc_4AD')

    Jump('loc_4E1')

    def _loc_4B0(): pass

    label('loc_4B0')

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
    def _loc_4E1(): pass

    label('loc_4E1')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4EF
@scena.Code('func_03_4EF')
def func_03_4EF():
    UnlockAchievement(0x02, 0x013D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 5, 0x237D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['百合项链'], 1)"),
            Expr.Return,
        ),
        'loc_563',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['百合项链']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046F, 5, 0x237D))

    Jump('loc_5C9')

    def _loc_563(): pass

    label('loc_563')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['百合项链']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['百合项链']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_5C9(): pass

    label('loc_5C9')

    Jump('loc_5FD')

    def _loc_5CC(): pass

    label('loc_5CC')

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
    def _loc_5FD(): pass

    label('loc_5FD')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x60B
@scena.Code('func_04_60B')
def func_04_60B():
    UnlockAchievement(0x02, 0x013E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 6, 0x237E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_67F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046F, 6, 0x237E))

    Jump('loc_6E5')

    def _loc_67F(): pass

    label('loc_67F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_6E5(): pass

    label('loc_6E5')

    Jump('loc_719')

    def _loc_6E8(): pass

    label('loc_6E8')

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
    def _loc_719(): pass

    label('loc_719')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x727
@scena.Code('func_05_727')
def func_05_727():
    UnlockAchievement(0x02, 0x013F, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046F, 7, 0x237F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_853',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 30)
    OP_73(0x0004)
    OP_6F(0x0004, 30)
    AddSepith(0x00, 100)
    AddSepith(0x01, 100)
    AddSepith(0x02, 100)
    AddSepith(0x03, 100)
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
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
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
    SetScenaFlags(ScenaFlag(0x046F, 7, 0x237F))

    Jump('loc_86D')

    def _loc_853(): pass

    label('loc_853')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_86D(): pass

    label('loc_86D')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x87F
@scena.Code('func_06_87F')
def func_06_87F():
    UnlockAchievement(0x02, 0x0140, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 1, 0x2381)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_95C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_8F3',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0470, 1, 0x2381))

    Jump('loc_959')

    def _loc_8F3(): pass

    label('loc_8F3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_959(): pass

    label('loc_959')

    Jump('loc_98D')

    def _loc_95C(): pass

    label('loc_95C')

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
    def _loc_98D(): pass

    label('loc_98D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x99B
@scena.Code('func_07_99B')
def func_07_99B():
    UnlockAchievement(0x02, 0x0141, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 2, 0x2382)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A78',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_A0F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0470, 2, 0x2382))

    Jump('loc_A75')

    def _loc_A0F(): pass

    label('loc_A0F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_A75(): pass

    label('loc_A75')

    Jump('loc_AA9')

    def _loc_A78(): pass

    label('loc_A78')

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
    def _loc_AA9(): pass

    label('loc_AA9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xAB7
@scena.Code('func_08_AB7')
def func_08_AB7():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 5110, -1750, 110000, 90)
    Yield()
    Fade(1000)
    CameraMove(5110, 10, 110000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 0, 111000, 0)
    OP_89(0x0001, 6000, 0, 110000, 90)
    OP_89(0x0002, 4000, 0, 110000, 270)
    OP_89(0x0003, 5000, 0, 109000, 180)
    OP_0D()
    Sleep(300)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x01, 0x64)

    @scena.Lambda('lambda_0B6C')
    def lambda_0B6C():
        OP_67(0, 6500, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B6C)

    @scena.Lambda('lambda_0B84')
    def lambda_0B84():
        CameraSetDistance(3700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B84)

    @scena.Lambda('lambda_0B94')
    def lambda_0B94():
        ChrMoveToRelativeAsync(0x00FE, 0, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B94)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0451, 4, 0x228C))
    ClearScenaFlags(ScenaFlag(0x0451, 5, 0x228D))
    ClearScenaFlags(ScenaFlag(0x0451, 6, 0x228E))
    ClearScenaFlags(ScenaFlag(0x0451, 7, 0x228F))
    ClearScenaFlags(ScenaFlag(0x0452, 0, 0x2290))
    SetScenaFlags(ScenaFlag(0x0452, 1, 0x2291))
    ClearScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    ClearScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    ClearScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    ClearScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0xBE4
@scena.Code('func_09_BE4')
def func_09_BE4():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 5110, -11750, 110000, 90)
    Yield()
    CameraMove(5110, 10, 110000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 0, 111000, 0)
    OP_89(0x0001, 6000, 0, 110000, 90)
    OP_89(0x0002, 4000, 0, 110000, 270)
    OP_89(0x0003, 5000, 0, 109000, 180)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0C93')
    def lambda_0C93():
        CameraSetDistance(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C93)

    FadeIn(1000, 0)
    OP_13(0x011F)

    @scena.Lambda('lambda_0CAF')
    def lambda_0CAF():
        ChrMoveToRelativeAsync(0x00FE, 0, 10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CAF)

    Sleep(2200)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    Fade(1000)
    ChrSetPos(0x0000, -180, 0, 109780, 270)
    ChrSetPos(0x0001, -180, 0, 109780, 270)
    ChrSetPos(0x0002, -180, 0, 109780, 270)
    ChrSetPos(0x0003, -180, 0, 109780, 270)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
