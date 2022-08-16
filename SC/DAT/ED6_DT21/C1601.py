import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1601   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1601.x'
    header.mapIndex       = 250
    header.bgm            = 125
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
        ('ED6_DT29/CH12450._CH', 'ED6_DT29/CH12450P._CP'),
        ('ED6_DT29/CH12451._CH', 'ED6_DT29/CH12451P._CP'),
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
        ('ED6_DT29/CH12460._CH', 'ED6_DT29/CH12460P._CP'),
        ('ED6_DT29/CH12461._CH', 'ED6_DT29/CH12461P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT29/CH12500._CH', 'ED6_DT29/CH12500P._CP'),
        ('ED6_DT29/CH12501._CH', 'ED6_DT29/CH12501P._CP'),
        ('ED6_DT29/CH12560._CH', 'ED6_DT29/CH12560P._CP'),
        ('ED6_DT29/CH12561._CH', 'ED6_DT29/CH12561P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 53080,
            z           = 0,
            y           = 1650,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 24670,
            z           = 0,
            y           = 22960,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -8910,
            z           = 0,
            y           = 21050,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -20410,
            z           = -500,
            y           = 27460,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -41620,
            z           = 1000,
            y           = 45310,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -32180,
            z           = 0,
            y           = 61060,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -48200,
            z           = 0,
            y           = 5330,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -9720,
            z           = 0,
            y           = -137210,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 217380,
            z           = 0,
            y           = 12010,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03C7,
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
            triggerX            = -7780,
            triggerZ            = 0,
            triggerY            = -128550,
            triggerRange        = 1000,
            actorX              = -7780,
            actorZ              = 0,
            actorY              = -127890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 227170,
            triggerZ            = 0,
            triggerY            = 11830,
            triggerRange        = 1000,
            actorX              = 227870,
            actorZ              = 0,
            actorY              = 11830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -29260,
            triggerZ            = 0,
            triggerY            = 54810,
            triggerRange        = 1000,
            actorX              = -29260,
            actorZ              = 0,
            actorY              = 54110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -34020,
            triggerZ            = 0,
            triggerY            = 67570,
            triggerRange        = 1000,
            actorX              = -34020,
            actorZ              = 0,
            actorY              = 68190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -940,
            triggerZ            = 0,
            triggerY            = -135030,
            triggerRange        = 1000,
            actorX              = -180,
            actorZ              = 0,
            actorY              = -135030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 215690,
            triggerZ            = 0,
            triggerY            = 23150,
            triggerRange        = 1000,
            actorX              = 215690,
            actorZ              = 0,
            actorY              = 23810,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 206060,
            triggerZ            = 0,
            triggerY            = 12220,
            triggerRange        = 1000,
            actorX              = 205400,
            actorZ              = 0,
            actorY              = 12180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x302
@scena.Code('Init')
def Init():
    OP_11(0xFF, 0xFF, 0xFF, 40000, 74000, 0)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_31E'),
        (-1, 'loc_332'),
    )

    def _loc_31E(): pass

    label('loc_31E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 4, 0x1A84)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32F',
    )

    MapSetFlags(0x10000000)
    Event(0, func_09_C02)

    def _loc_32F(): pass

    label('loc_32F')

    Jump('loc_332')

    def _loc_332(): pass

    label('loc_332')

    Return()

# id: 0x0001 offset: 0x333
@scena.Code('func_01_333')
def func_01_333():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 0, 0x1B80)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_345',
    )

    OP_6F(0x0000, 0)

    Jump('loc_34C')

    def _loc_345(): pass

    label('loc_345')

    OP_6F(0x0000, 60)

    def _loc_34C(): pass

    label('loc_34C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 2, 0x1B82)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35E',
    )

    OP_6F(0x0001, 0)

    Jump('loc_365')

    def _loc_35E(): pass

    label('loc_35E')

    OP_6F(0x0001, 60)

    def _loc_365(): pass

    label('loc_365')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 4, 0x1B84)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_377',
    )

    OP_6F(0x0002, 0)

    Jump('loc_37E')

    def _loc_377(): pass

    label('loc_377')

    OP_6F(0x0002, 60)

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 6, 0x1B86)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_390',
    )

    OP_6F(0x0003, 0)

    Jump('loc_397')

    def _loc_390(): pass

    label('loc_390')

    OP_6F(0x0003, 60)

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 7, 0x1B87)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A9',
    )

    OP_6F(0x0004, 0)

    Jump('loc_3B0')

    def _loc_3A9(): pass

    label('loc_3A9')

    OP_6F(0x0004, 60)

    def _loc_3B0(): pass

    label('loc_3B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0371, 0, 0x1B88)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C2',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3C9')

    def _loc_3C2(): pass

    label('loc_3C2')

    OP_6F(0x0005, 60)

    def _loc_3C9(): pass

    label('loc_3C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0371, 1, 0x1B89)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DB',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3E2')

    def _loc_3DB(): pass

    label('loc_3DB')

    OP_6F(0x0006, 60)

    def _loc_3E2(): pass

    label('loc_3E2')

    OP_E0(0x04, 0x10, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x8A, 0xF0, 0xFD, 0xFF)

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
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
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
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
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x43E
@scena.Code('func_02_43E')
def func_02_43E():
    UnlockAchievement(0x02, 0x005C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 0, 0x1B80)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['导力靴'], 1)"),
            Expr.Return,
        ),
        'loc_4B2',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0370, 0, 0x1B80))

    Jump('loc_518')

    def _loc_4B2(): pass

    label('loc_4B2')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['导力靴']),
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

    def _loc_518(): pass

    label('loc_518')

    Jump('loc_54C')

    def _loc_51B(): pass

    label('loc_51B')

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
    def _loc_54C(): pass

    label('loc_54C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x55A
@scena.Code('func_03_55A')
def func_03_55A():
    UnlockAchievement(0x02, 0x005D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 2, 0x1B82)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_637',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['金耀晚礼服'], 1)"),
            Expr.Return,
        ),
        'loc_5CE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0370, 2, 0x1B82))

    Jump('loc_634')

    def _loc_5CE(): pass

    label('loc_5CE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
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

    def _loc_634(): pass

    label('loc_634')

    Jump('loc_668')

    def _loc_637(): pass

    label('loc_637')

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
    def _loc_668(): pass

    label('loc_668')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x676
@scena.Code('func_04_676')
def func_04_676():
    UnlockAchievement(0x02, 0x005E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 4, 0x1B84)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_753',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['光束粒子炮'], 1)"),
            Expr.Return,
        ),
        'loc_6EA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['光束粒子炮']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0370, 4, 0x1B84))

    Jump('loc_750')

    def _loc_6EA(): pass

    label('loc_6EA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['光束粒子炮']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['光束粒子炮']),
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

    def _loc_750(): pass

    label('loc_750')

    Jump('loc_784')

    def _loc_753(): pass

    label('loc_753')

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
    def _loc_784(): pass

    label('loc_784')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x792
@scena.Code('func_05_792')
def func_05_792():
    UnlockAchievement(0x02, 0x005F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 6, 0x1B86)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_806',
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
    SetScenaFlags(ScenaFlag(0x0370, 6, 0x1B86))

    Jump('loc_86C')

    def _loc_806(): pass

    label('loc_806')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_86C(): pass

    label('loc_86C')

    Jump('loc_8A0')

    def _loc_86F(): pass

    label('loc_86F')

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
    def _loc_8A0(): pass

    label('loc_8A0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8AE
@scena.Code('func_06_8AE')
def func_06_8AE():
    UnlockAchievement(0x02, 0x0060, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0370, 7, 0x1B87)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_922',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0370, 7, 0x1B87))

    Jump('loc_988')

    def _loc_922(): pass

    label('loc_922')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
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

    def _loc_988(): pass

    label('loc_988')

    Jump('loc_9BC')

    def _loc_98B(): pass

    label('loc_98B')

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
    def _loc_9BC(): pass

    label('loc_9BC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x9CA
@scena.Code('func_07_9CA')
def func_07_9CA():
    UnlockAchievement(0x02, 0x0061, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0371, 0, 0x1B88)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_A3E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0371, 0, 0x1B88))

    Jump('loc_AA4')

    def _loc_A3E(): pass

    label('loc_A3E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_AA4(): pass

    label('loc_AA4')

    Jump('loc_AD8')

    def _loc_AA7(): pass

    label('loc_AA7')

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
    def _loc_AD8(): pass

    label('loc_AD8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xAE6
@scena.Code('func_08_AE6')
def func_08_AE6():
    UnlockAchievement(0x02, 0x0062, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0371, 1, 0x1B89)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BC3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_B5A',
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
    SetScenaFlags(ScenaFlag(0x0371, 1, 0x1B89))

    Jump('loc_BC0')

    def _loc_B5A(): pass

    label('loc_B5A')

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
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_BC0(): pass

    label('loc_BC0')

    Jump('loc_BF4')

    def _loc_BC3(): pass

    label('loc_BC3')

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
    def _loc_BF4(): pass

    label('loc_BF4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC02
@scena.Code('func_09_C02')
def func_09_C02():
    OP_C8(0x0200, 0x0032, 'C_PLAC17._CH', 0x00, 0x03E8)
    ShowPlaceName('古龙的居所')
    SetScenaFlags(ScenaFlag(0x0350, 4, 0x1A84))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
