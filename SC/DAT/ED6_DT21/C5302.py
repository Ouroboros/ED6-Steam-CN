import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5302.x'
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
        ('ED6_DT29/CH12340._CH', 'ED6_DT29/CH12340P._CP'),
        ('ED6_DT29/CH12341._CH', 'ED6_DT29/CH12341P._CP'),
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
            x           = -91600,
            z           = 2160,
            y           = 96970,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0530,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -98800,
            z           = 140,
            y           = 15500,
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
            x           = -99020,
            z           = 90,
            y           = 2280,
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
            x           = -71000,
            z           = 4240,
            y           = -78680,
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
            x           = 120,
            z           = 2000,
            y           = -94140,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0530,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 84070,
            z           = 2170,
            y           = -85430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 100070,
            y           = -2000,
            z           = 9050,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000A,
        ),
    )

# id: 0x10004 offset: 0x1F2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -107040,
            triggerZ            = 0,
            triggerY            = 5010,
            triggerRange        = 1000,
            actorX              = -107640,
            actorZ              = 0,
            actorY              = 4980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -107050,
            triggerZ            = 0,
            triggerY            = 7600,
            triggerRange        = 1000,
            actorX              = -107650,
            actorZ              = 0,
            actorY              = 7570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -107050,
            triggerZ            = 0,
            triggerY            = 10290,
            triggerRange        = 1000,
            actorX              = -107690,
            actorZ              = 0,
            actorY              = 10200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -107050,
            triggerZ            = 0,
            triggerY            = 12900,
            triggerRange        = 1000,
            actorX              = -107650,
            actorZ              = 0,
            actorY              = 12870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90700,
            triggerZ            = 0,
            triggerY            = 13070,
            triggerRange        = 1000,
            actorX              = -90030,
            actorZ              = 0,
            actorY              = 13100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90700,
            triggerZ            = 0,
            triggerY            = 10470,
            triggerRange        = 1000,
            actorX              = -90090,
            actorZ              = 0,
            actorY              = 10500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90700,
            triggerZ            = 0,
            triggerY            = 7650,
            triggerRange        = 1000,
            actorX              = -90010,
            actorZ              = 0,
            actorY              = 7690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90700,
            triggerZ            = 0,
            triggerY            = 5050,
            triggerRange        = 1000,
            actorX              = -90020,
            actorZ              = 0,
            actorY              = 4960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x312
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_322',
    )

    Event(0, func_0B_F2B)

    def _loc_322(): pass

    label('loc_322')

    Return()

# id: 0x0001 offset: 0x323
@scena.Code('func_01_323')
def func_01_323():
    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xD7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 4, 0x236C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_361',
    )

    OP_6F(0x0001, 0)

    Jump('loc_368')

    def _loc_361(): pass

    label('loc_361')

    OP_6F(0x0001, 60)

    def _loc_368(): pass

    label('loc_368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 5, 0x236D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_6F(0x0002, 0)

    Jump('loc_381')

    def _loc_37A(): pass

    label('loc_37A')

    OP_6F(0x0002, 60)

    def _loc_381(): pass

    label('loc_381')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 7, 0x236F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_393',
    )

    OP_6F(0x0003, 0)

    Jump('loc_39A')

    def _loc_393(): pass

    label('loc_393')

    OP_6F(0x0003, 60)

    def _loc_39A(): pass

    label('loc_39A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 0, 0x2370)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_6F(0x0004, 0)

    Jump('loc_3B3')

    def _loc_3AC(): pass

    label('loc_3AC')

    OP_6F(0x0004, 60)

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 1, 0x2371)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3CC')

    def _loc_3C5(): pass

    label('loc_3C5')

    OP_6F(0x0005, 60)

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 2, 0x2372)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3E5')

    def _loc_3DE(): pass

    label('loc_3DE')

    OP_6F(0x0006, 60)

    def _loc_3E5(): pass

    label('loc_3E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 4, 0x2374)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F7',
    )

    OP_6F(0x0007, 0)

    Jump('loc_3FE')

    def _loc_3F7(): pass

    label('loc_3F7')

    OP_6F(0x0007, 60)

    def _loc_3FE(): pass

    label('loc_3FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 5, 0x2375)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_410',
    )

    OP_6F(0x0008, 0)

    Jump('loc_417')

    def _loc_410(): pass

    label('loc_410')

    OP_6F(0x0008, 60)

    def _loc_417(): pass

    label('loc_417')

    OP_10(0x00, 0x00)
    PlaySE(320, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x420
@scena.Code('func_02_420')
def func_02_420():
    UnlockAchievement(0x02, 0x0130, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 4, 0x236C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_494',
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
    SetScenaFlags(ScenaFlag(0x046D, 4, 0x236C))

    Jump('loc_4FA')

    def _loc_494(): pass

    label('loc_494')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_4FA(): pass

    label('loc_4FA')

    Jump('loc_52E')

    def _loc_4FD(): pass

    label('loc_4FD')

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
    def _loc_52E(): pass

    label('loc_52E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x53C
@scena.Code('func_03_53C')
def func_03_53C():
    UnlockAchievement(0x02, 0x0131, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 5, 0x236D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_668',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 30)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
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
    SetScenaFlags(ScenaFlag(0x046D, 5, 0x236D))

    Jump('loc_682')

    def _loc_668(): pass

    label('loc_668')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_682(): pass

    label('loc_682')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x694
@scena.Code('func_04_694')
def func_04_694():
    UnlockAchievement(0x02, 0x0132, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046D, 7, 0x236F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_771',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['炮术师战甲'], 1)"),
            Expr.Return,
        ),
        'loc_708',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['炮术师战甲']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046D, 7, 0x236F))

    Jump('loc_76E')

    def _loc_708(): pass

    label('loc_708')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['炮术师战甲']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['炮术师战甲']),
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

    def _loc_76E(): pass

    label('loc_76E')

    Jump('loc_7A2')

    def _loc_771(): pass

    label('loc_771')

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
    def _loc_7A2(): pass

    label('loc_7A2')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7B0
@scena.Code('func_05_7B0')
def func_05_7B0():
    UnlockAchievement(0x02, 0x0133, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 0, 0x2370)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_824',
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
    SetScenaFlags(ScenaFlag(0x046E, 0, 0x2370))

    Jump('loc_88A')

    def _loc_824(): pass

    label('loc_824')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_88A(): pass

    label('loc_88A')

    Jump('loc_8BE')

    def _loc_88D(): pass

    label('loc_88D')

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
    def _loc_8BE(): pass

    label('loc_8BE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8CC
@scena.Code('func_06_8CC')
def func_06_8CC():
    UnlockAchievement(0x02, 0x0134, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 1, 0x2371)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9A9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_940',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x046E, 1, 0x2371))

    Jump('loc_9A6')

    def _loc_940(): pass

    label('loc_940')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_9A6(): pass

    label('loc_9A6')

    Jump('loc_9DA')

    def _loc_9A9(): pass

    label('loc_9A9')

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
    def _loc_9DA(): pass

    label('loc_9DA')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x9E8
@scena.Code('func_07_9E8')
def func_07_9E8():
    UnlockAchievement(0x02, 0x0135, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 2, 0x2372)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['猛虎之心'], 1)"),
            Expr.Return,
        ),
        'loc_A5C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['猛虎之心']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046E, 2, 0x2372))

    Jump('loc_AC2')

    def _loc_A5C(): pass

    label('loc_A5C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['猛虎之心']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['猛虎之心']),
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

    def _loc_AC2(): pass

    label('loc_AC2')

    Jump('loc_AF6')

    def _loc_AC5(): pass

    label('loc_AC5')

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
    def _loc_AF6(): pass

    label('loc_AF6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xB04
@scena.Code('func_08_B04')
def func_08_B04():
    UnlockAchievement(0x02, 0x0136, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 4, 0x2374)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BE1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_B78',
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
    SetScenaFlags(ScenaFlag(0x046E, 4, 0x2374))

    Jump('loc_BDE')

    def _loc_B78(): pass

    label('loc_B78')

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
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_BDE(): pass

    label('loc_BDE')

    Jump('loc_C12')

    def _loc_BE1(): pass

    label('loc_BE1')

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
    def _loc_C12(): pass

    label('loc_C12')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC20
@scena.Code('func_09_C20')
def func_09_C20():
    UnlockAchievement(0x02, 0x0137, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046E, 5, 0x2375)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_C94',
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
    SetScenaFlags(ScenaFlag(0x046E, 5, 0x2375))

    Jump('loc_CFA')

    def _loc_C94(): pass

    label('loc_C94')

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
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_CFA(): pass

    label('loc_CFA')

    Jump('loc_D2E')

    def _loc_CFD(): pass

    label('loc_CFD')

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
    def _loc_D2E(): pass

    label('loc_D2E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xD3C
@scena.Code('func_0A_D3C')
def func_0A_D3C():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 100070, -1750, 9050, 0)
    Yield()
    Fade(1000)
    CameraMove(100070, 0, 9050, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 14000, 10000, 0)
    OP_89(0x0001, 101000, 14000, 9000, 90)
    OP_89(0x0002, 99000, 14000, 9000, 270)
    OP_89(0x0003, 100000, 14000, 8000, 180)
    OP_0D()
    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0DEC')
    def lambda_0DEC():
        ChrMoveTo(0x00FE, 101980, 60000, 850, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DEC)

    Sleep(500)

    @scena.Lambda('lambda_0E0C')
    def lambda_0E0C():
        CameraMove(100070, 35000, 9050, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E0C)

    @scena.Lambda('lambda_0E24')
    def lambda_0E24():
        OP_67(0, 14000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E24)

    @scena.Lambda('lambda_0E3C')
    def lambda_0E3C():
        OP_6C(335000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E3C)

    Sleep(500)

    @scena.Lambda('lambda_0E51')
    def lambda_0E51():
        ChrMoveTo(0x00FE, 100070, 65000, 9050, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E51)

    Sleep(500)

    @scena.Lambda('lambda_0E71')
    def lambda_0E71():
        ChrMoveTo(0x00FE, 100070, 65000, 9050, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E71)

    Sleep(400)

    @scena.Lambda('lambda_0E91')
    def lambda_0E91():
        ChrMoveTo(0x00FE, 100070, 65000, 9050, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E91)

    Sleep(200)

    @scena.Lambda('lambda_0EB1')
    def lambda_0EB1():
        ChrMoveTo(0x00FE, 100070, 65000, 9050, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0EB1)

    Sleep(100)

    @scena.Lambda('lambda_0ED1')
    def lambda_0ED1():
        ChrMoveTo(0x00FE, 100070, 65000, 9050, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0ED1)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0451, 4, 0x228C))
    ClearScenaFlags(ScenaFlag(0x0451, 5, 0x228D))
    SetScenaFlags(ScenaFlag(0x0451, 6, 0x228E))
    ClearScenaFlags(ScenaFlag(0x0451, 7, 0x228F))
    ClearScenaFlags(ScenaFlag(0x0452, 0, 0x2290))
    ClearScenaFlags(ScenaFlag(0x0452, 1, 0x2291))
    ClearScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    ClearScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    ClearScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    ClearScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0xF2B
@scena.Code('func_0B_F2B')
def func_0B_F2B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 100070, 66000, 9050, 0)
    Yield()
    CameraMove(100070, 48000, 9050, 0)
    OP_67(0, 16000, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 67000, 10000, 0)
    OP_89(0x0001, 101000, 67000, 9000, 90)
    OP_89(0x0002, 99000, 67000, 9000, 270)
    OP_89(0x0003, 100000, 67000, 8000, 180)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0FDA')
    def lambda_0FDA():
        CameraMove(100070, 0, 9050, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FDA)

    @scena.Lambda('lambda_0FF2')
    def lambda_0FF2():
        OP_67(0, 9500, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FF2)

    @scena.Lambda('lambda_100A')
    def lambda_100A():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_100A)

    FadeIn(1000, 0)
    OP_13(0x011D)

    @scena.Lambda('lambda_1026')
    def lambda_1026():
        ChrMoveTo(0x00FE, 100070, -1750, 9050, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1026)

    Sleep(7800)

    @scena.Lambda('lambda_1046')
    def lambda_1046():
        ChrMoveTo(0x00FE, 100070, -1750, 9050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1046)

    Sleep(700)

    @scena.Lambda('lambda_1066')
    def lambda_1066():
        ChrMoveTo(0x00FE, 100070, -1750, 9050, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1066)

    Sleep(600)

    @scena.Lambda('lambda_1086')
    def lambda_1086():
        ChrMoveTo(0x00FE, 100070, -1750, 9050, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1086)

    Sleep(100)

    @scena.Lambda('lambda_10A6')
    def lambda_10A6():
        ChrMoveTo(0x00FE, 100070, -1750, 9050, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_10A6)

    Sleep(500)

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
    ChrSetPos(0x0000, 100420, 0, 4460, 180)
    ChrSetPos(0x0001, 100420, 0, 4460, 180)
    ChrSetPos(0x0002, 100420, 0, 4460, 180)
    ChrSetPos(0x0003, 100420, 0, 4460, 180)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
