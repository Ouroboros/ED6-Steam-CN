import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5506_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5506   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5506.x'
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
        ('ED6_DT29/CH12180._CH', 'ED6_DT29/CH12180P._CP'),
        ('ED6_DT29/CH12181._CH', 'ED6_DT29/CH12181P._CP'),
        ('ED6_DT29/CH12230._CH', 'ED6_DT29/CH12230P._CP'),
        ('ED6_DT29/CH12231._CH', 'ED6_DT29/CH12231P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
        ('ED6_DT29/CH12360._CH', 'ED6_DT29/CH12360P._CP'),
        ('ED6_DT29/CH12361._CH', 'ED6_DT29/CH12361P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 44320,
            z                   = 1000,
            y                   = -17010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 8170,
            z           = 0,
            y           = -15930,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 16960,
            z           = 0,
            y           = 5750,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 36290,
            z           = 0,
            y           = 35730,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 48370,
            z           = 0,
            y           = 5530,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -19010,
            z           = -4000,
            y           = -840,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -25740,
            z           = -4000,
            y           = -9090,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -29330,
            z           = 0,
            y           = 13340,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -40750,
            z           = 0,
            y           = -9890,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -57380,
            z           = 0,
            y           = 9430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x206
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x206
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 44320,
            triggerZ            = 0,
            triggerY            = -16350,
            triggerRange        = 1000,
            actorX              = 44320,
            actorZ              = 0,
            actorY              = -17010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 54110,
            triggerZ            = 0,
            triggerY            = 4910,
            triggerRange        = 1000,
            actorX              = 54770,
            actorZ              = 0,
            actorY              = 4960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45550,
            triggerZ            = 0,
            triggerY            = 37990,
            triggerRange        = 1000,
            actorX              = 46210,
            actorZ              = 0,
            actorY              = 37990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -57310,
            triggerZ            = 0,
            triggerY            = -9280,
            triggerRange        = 1000,
            actorX              = -57940,
            actorZ              = 0,
            actorY              = -9480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -22600,
            triggerZ            = -4000,
            triggerY            = 15420,
            triggerRange        = 1000,
            actorX              = -23170,
            actorZ              = -4000,
            actorY              = 15420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2BA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2BB
@scena.Code('func_01_2BB')
def func_01_2BB():
    OP_BE(0x00, 0x01, 0x0002, 0x0028, 0x0000, 0x02, -34850, -4400, -21210, -7610, -3350, 18110)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 0, 0x1130)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EF',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2F6')

    def _loc_2EF(): pass

    label('loc_2EF')

    OP_6F(0x0000, 60)

    def _loc_2F6(): pass

    label('loc_2F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 2, 0x1132)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_308',
    )

    OP_6F(0x0001, 0)

    Jump('loc_30F')

    def _loc_308(): pass

    label('loc_308')

    OP_6F(0x0001, 60)

    def _loc_30F(): pass

    label('loc_30F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 3, 0x1133)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_321',
    )

    OP_6F(0x0002, 0)

    Jump('loc_328')

    def _loc_321(): pass

    label('loc_321')

    OP_6F(0x0002, 60)

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 4, 0x1134)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33A',
    )

    OP_6F(0x0003, 0)

    Jump('loc_341')

    def _loc_33A(): pass

    label('loc_33A')

    OP_6F(0x0003, 60)

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 5, 0x1135)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_353',
    )

    OP_6F(0x0004, 0)

    Jump('loc_35A')

    def _loc_353(): pass

    label('loc_353')

    OP_6F(0x0004, 60)

    def _loc_35A(): pass

    label('loc_35A')

    Return()

# id: 0x0002 offset: 0x35B
@scena.Code('func_02_35B')
def func_02_35B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_370',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_35B')

    def _loc_370(): pass

    label('loc_370')

    Return()

# id: 0x0003 offset: 0x371
@scena.Code('func_03_371')
def func_03_371():
    UnlockAchievement(0x02, 0x0191, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 0, 0x1130)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['战斗用棍'], 1)"),
            Expr.Return,
        ),
        'loc_3E5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['战斗用棍']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0226, 0, 0x1130))

    Jump('loc_44B')

    def _loc_3E5(): pass

    label('loc_3E5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['战斗用棍']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['战斗用棍']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_44B(): pass

    label('loc_44B')

    Jump('loc_47F')

    def _loc_44E(): pass

    label('loc_44E')

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
    def _loc_47F(): pass

    label('loc_47F')

    Sleep(30)

    Call(0, 0x0008)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x491
@scena.Code('func_04_491')
def func_04_491():
    UnlockAchievement(0x02, 0x0192, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 2, 0x1132)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['直刃剑'], 1)"),
            Expr.Return,
        ),
        'loc_505',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['直刃剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0226, 2, 0x1132))

    Jump('loc_56B')

    def _loc_505(): pass

    label('loc_505')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['直刃剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['直刃剑']),
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

    def _loc_56B(): pass

    label('loc_56B')

    Jump('loc_59F')

    def _loc_56E(): pass

    label('loc_56E')

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
    def _loc_59F(): pass

    label('loc_59F')

    Sleep(30)

    Call(0, 0x0008)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5B1
@scena.Code('func_05_5B1')
def func_05_5B1():
    UnlockAchievement(0x02, 0x0193, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 3, 0x1133)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['强化皮靴'], 1)"),
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
            (TxtCtl.Item, ItemTable['强化皮靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0226, 3, 0x1133))

    Jump('loc_68B')

    def _loc_625(): pass

    label('loc_625')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['强化皮靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['强化皮靴']),
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

    Call(0, 0x0008)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x6D1
@scena.Code('func_06_6D1')
def func_06_6D1():
    UnlockAchievement(0x02, 0x0194, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 4, 0x1134)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7AE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_745',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0226, 4, 0x1134))

    Jump('loc_7AB')

    def _loc_745(): pass

    label('loc_745')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_7AB(): pass

    label('loc_7AB')

    Jump('loc_7DF')

    def _loc_7AE(): pass

    label('loc_7AE')

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
    def _loc_7DF(): pass

    label('loc_7DF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x7ED
@scena.Code('func_07_7ED')
def func_07_7ED():
    UnlockAchievement(0x02, 0x0195, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 5, 0x1135)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_861',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0226, 5, 0x1135))

    Jump('loc_8C7')

    def _loc_861(): pass

    label('loc_861')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_8C7(): pass

    label('loc_8C7')

    Jump('loc_8FB')

    def _loc_8CA(): pass

    label('loc_8CA')

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
    def _loc_8FB(): pass

    label('loc_8FB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x909
@scena.Code('func_08_909')
def func_08_909():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 7, 0x100F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A07',
    )

    ChrTalk(
        0x0101,
        (
            '#0010191230V#1004F啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191231V难不成，这个\n',
            '就是我们的装备？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191232V#811F嗯，似乎是呢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191233V#1310F说不定其它装备\n',
            '也被藏在什么地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191234V#1006F嗯～\n',
            '虽然想避开和魔兽的战斗，\n',
            '但似乎值得探索一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0201, 7, 0x100F))

    def _loc_A07(): pass

    label('loc_A07')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
