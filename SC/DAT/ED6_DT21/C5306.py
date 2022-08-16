import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5306_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5306   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5306.x'
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
        ('ED6_DT29/CH12300._CH', 'ED6_DT29/CH12300P._CP'),
        ('ED6_DT29/CH12301._CH', 'ED6_DT29/CH12301P._CP'),
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
            x           = 91640,
            z           = 0,
            y           = -72910,
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
            x           = -76800,
            z           = 0,
            y           = -90840,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -94600,
            z           = 0,
            y           = -73000,
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
            x           = -87930,
            z           = 0,
            y           = 96320,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 100070,
            y           = -2000,
            z           = 9020,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = 5140,
            y           = -2000,
            z           = 110030,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10004 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -10520,
            triggerZ            = 0,
            triggerY            = -90700,
            triggerRange        = 1000,
            actorX              = -10490,
            actorZ              = 0,
            actorY              = -90090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9460,
            triggerZ            = 0,
            triggerY            = -90710,
            triggerRange        = 1000,
            actorX              = 9490,
            actorZ              = 0,
            actorY              = -90050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9550,
            triggerZ            = 0,
            triggerY            = -95300,
            triggerRange        = 1000,
            actorX              = 9520,
            actorZ              = 0,
            actorY              = -95870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10520,
            triggerZ            = 0,
            triggerY            = -95300,
            triggerRange        = 1000,
            actorX              = -10470,
            actorZ              = 0,
            actorY              = -96000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_27B',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_06_8A0)

    Jump('loc_2A4')

    def _loc_27B(): pass

    label('loc_27B')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_28F'),
        (0x0000007A, 'loc_296'),
        (0x0000006F, 'loc_29D'),
        (-1, 'loc_2A4'),
    )

    def _loc_28F(): pass

    label('loc_28F')

    Event(0, func_08_AE4)

    Jump('loc_2A4')

    def _loc_296(): pass

    label('loc_296')

    Event(0, func_0A_E6F)

    Jump('loc_2A4')

    def _loc_29D(): pass

    label('loc_29D')

    Event(0, func_0C_11B7)

    Jump('loc_2A4')

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 3, 0x223B)),
            Expr.Return,
        ),
        'loc_2EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_2EB(): pass

    label('loc_2EB')

    Return()

# id: 0x0001 offset: 0x2EC
@scena.Code('func_01_2EC')
def func_01_2EC():
    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xD7),
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
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 3, 0x238B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31F',
    )

    OP_6F(0x0003, 0)

    Jump('loc_326')

    def _loc_31F(): pass

    label('loc_31F')

    OP_6F(0x0003, 60)

    def _loc_326(): pass

    label('loc_326')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 5, 0x238D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_338',
    )

    OP_6F(0x0004, 0)

    Jump('loc_33F')

    def _loc_338(): pass

    label('loc_338')

    OP_6F(0x0004, 60)

    def _loc_33F(): pass

    label('loc_33F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 6, 0x238E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_351',
    )

    OP_6F(0x0005, 0)

    Jump('loc_358')

    def _loc_351(): pass

    label('loc_351')

    OP_6F(0x0005, 60)

    def _loc_358(): pass

    label('loc_358')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 7, 0x238F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36A',
    )

    OP_6F(0x0006, 0)

    Jump('loc_371')

    def _loc_36A(): pass

    label('loc_36A')

    OP_6F(0x0006, 60)

    def _loc_371(): pass

    label('loc_371')

    OP_10(0x00, 0x00)
    OP_10(0x16, 0x00)
    StopEffect(0x84, 0x00)
    StopEffect(0x88, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 3, 0x223B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39C',
    )

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_10(0x0B, 0x00)

    Jump('loc_3ED')

    def _loc_39C(): pass

    label('loc_39C')

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 600)
    OP_10(0x0B, 0x01)
    StopEffect(0x83, 0x00)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_1B(0x0B, 0x00, 0x000B)

    def _loc_3ED(): pass

    label('loc_3ED')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 0)
    OP_A1(0x0008, 0x0002)
    ChrSetPos(0x0008, 5140, -1750, 110030, 90)
    PlaySE(320, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x42B
@scena.Code('func_02_42B')
def func_02_42B():
    UnlockAchievement(0x02, 0x0148, 0x00)
    UnlockAchievement(0x02, 0x020F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 3, 0x238B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['男骑士机甲'], 1)"),
            Expr.Return,
        ),
        'loc_4A4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['男骑士机甲']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0471, 3, 0x238B))

    Jump('loc_50A')

    def _loc_4A4(): pass

    label('loc_4A4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['男骑士机甲']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['男骑士机甲']),
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

    def _loc_50A(): pass

    label('loc_50A')

    Jump('loc_53E')

    def _loc_50D(): pass

    label('loc_50D')

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
    def _loc_53E(): pass

    label('loc_53E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x54C
@scena.Code('func_03_54C')
def func_03_54C():
    UnlockAchievement(0x02, 0x0149, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 5, 0x238D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_629',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_5C0',
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
    SetScenaFlags(ScenaFlag(0x0471, 5, 0x238D))

    Jump('loc_626')

    def _loc_5C0(): pass

    label('loc_5C0')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_626(): pass

    label('loc_626')

    Jump('loc_65A')

    def _loc_629(): pass

    label('loc_629')

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
    def _loc_65A(): pass

    label('loc_65A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x668
@scena.Code('func_04_668')
def func_04_668():
    UnlockAchievement(0x02, 0x014A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 6, 0x238E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_745',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_6DC',
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
    SetScenaFlags(ScenaFlag(0x0471, 6, 0x238E))

    Jump('loc_742')

    def _loc_6DC(): pass

    label('loc_6DC')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_742(): pass

    label('loc_742')

    Jump('loc_776')

    def _loc_745(): pass

    label('loc_745')

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
    def _loc_776(): pass

    label('loc_776')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x784
@scena.Code('func_05_784')
def func_05_784():
    UnlockAchievement(0x02, 0x014B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 7, 0x238F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_861',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_7F8',
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
    SetScenaFlags(ScenaFlag(0x0471, 7, 0x238F))

    Jump('loc_85E')

    def _loc_7F8(): pass

    label('loc_7F8')

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
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_85E(): pass

    label('loc_85E')

    Jump('loc_892')

    def _loc_861(): pass

    label('loc_861')

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
    def _loc_892(): pass

    label('loc_892')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8A0
@scena.Code('func_06_8A0')
def func_06_8A0():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-97890, 0, 32369, 0)
    OP_67(0, 7020, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0001, 0)
    OP_70(0x0001, 600)
    Sleep(1500)

    PlaySE(225, 0x00, 0x64)
    Sleep(3000)

    PlaySE(112, 0x00, 0x64)
    OP_73(0x0001)

    @scena.Lambda('lambda_0928')
    def lambda_0928():
        CameraMove(-88930, 1090, 4140, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0928)

    @scena.Lambda('lambda_0940')
    def lambda_0940():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0940)

    OP_6C(315000, 5000)
    Fade(1000)
    PlaySE(215, 0x00, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x9B7
@scena.Code('func_07_9B7')
def func_07_9B7():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 100070, -1750, 9020, 0)
    Yield()
    Fade(1000)
    CameraMove(100070, 0, 9020, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 0, 10000, 0)
    OP_89(0x0001, 101000, 0, 9000, 90)
    OP_89(0x0002, 99000, 0, 9000, 270)
    OP_89(0x0003, 100000, 0, 8000, 180)
    OP_0D()
    Sleep(300)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0A6C')
    def lambda_0A6C():
        OP_67(0, 6500, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A6C)

    @scena.Lambda('lambda_0A84')
    def lambda_0A84():
        CameraSetDistance(3700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A84)

    @scena.Lambda('lambda_0A94')
    def lambda_0A94():
        ChrMoveToRelativeAsync(0x00FE, 0, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A94)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0451, 4, 0x228C))
    ClearScenaFlags(ScenaFlag(0x0451, 5, 0x228D))
    ClearScenaFlags(ScenaFlag(0x0451, 6, 0x228E))
    ClearScenaFlags(ScenaFlag(0x0451, 7, 0x228F))
    ClearScenaFlags(ScenaFlag(0x0452, 0, 0x2290))
    ClearScenaFlags(ScenaFlag(0x0452, 1, 0x2291))
    ClearScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    SetScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    ClearScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    ClearScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0xAE4
@scena.Code('func_08_AE4')
def func_08_AE4():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 100070, -11750, 9020, 0)
    Yield()
    CameraMove(100070, 0, 9020, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 0, 10000, 0)
    OP_89(0x0001, 101000, 0, 9000, 90)
    OP_89(0x0002, 99000, 0, 9000, 270)
    OP_89(0x0003, 100000, 0, 8000, 180)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0B93')
    def lambda_0B93():
        CameraSetDistance(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B93)

    FadeIn(1000, 0)
    OP_13(0x0120)

    @scena.Lambda('lambda_0BAF')
    def lambda_0BAF():
        ChrMoveToRelativeAsync(0x00FE, 0, 10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BAF)

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
    ChrSetPos(0x0000, 100080, 0, 4460, 180)
    ChrSetPos(0x0001, 100080, 0, 4460, 180)
    ChrSetPos(0x0002, 100080, 0, 4460, 180)
    ChrSetPos(0x0003, 100080, 0, 4460, 180)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0xC80
@scena.Code('func_09_C80')
def func_09_C80():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0002)
    ChrSetPos(0x0008, 5140, -1750, 110030, 90)
    Yield()
    Fade(1000)
    CameraMove(5140, 0, 110030, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 0, 111000, 0)
    OP_89(0x0001, 6000, 0, 110000, 90)
    OP_89(0x0002, 4000, 0, 110000, 270)
    OP_89(0x0003, 5000, 0, 109000, 180)
    OP_0D()
    MapSetFlags(0x00100000)
    PlaySE(235, 0x01, 0x64)

    @scena.Lambda('lambda_0D30')
    def lambda_0D30():
        ChrMoveTo(0x00FE, 5140, 65000, 110030, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D30)

    Sleep(500)

    @scena.Lambda('lambda_0D50')
    def lambda_0D50():
        CameraMove(5140, 35000, 110030, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D50)

    @scena.Lambda('lambda_0D68')
    def lambda_0D68():
        OP_67(0, 14000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D68)

    @scena.Lambda('lambda_0D80')
    def lambda_0D80():
        OP_6C(295000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D80)

    Sleep(500)

    @scena.Lambda('lambda_0D95')
    def lambda_0D95():
        ChrMoveTo(0x00FE, 5140, 65000, 110030, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D95)

    Sleep(500)

    @scena.Lambda('lambda_0DB5')
    def lambda_0DB5():
        ChrMoveTo(0x00FE, 5140, 65000, 110030, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DB5)

    Sleep(400)

    @scena.Lambda('lambda_0DD5')
    def lambda_0DD5():
        ChrMoveTo(0x00FE, 5140, 65000, 110030, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DD5)

    Sleep(200)

    @scena.Lambda('lambda_0DF5')
    def lambda_0DF5():
        ChrMoveTo(0x00FE, 5140, 65000, 110030, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0DF5)

    Sleep(100)

    @scena.Lambda('lambda_0E15')
    def lambda_0E15():
        ChrMoveTo(0x00FE, 5140, 65000, 110030, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E15)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0451, 4, 0x228C))
    ClearScenaFlags(ScenaFlag(0x0451, 5, 0x228D))
    ClearScenaFlags(ScenaFlag(0x0451, 6, 0x228E))
    ClearScenaFlags(ScenaFlag(0x0451, 7, 0x228F))
    ClearScenaFlags(ScenaFlag(0x0452, 0, 0x2290))
    ClearScenaFlags(ScenaFlag(0x0452, 1, 0x2291))
    ClearScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    ClearScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    SetScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    ClearScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0xE6F
@scena.Code('func_0A_E6F')
def func_0A_E6F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0002)
    ChrSetPos(0x0008, 5140, 66000, 110030, 90)
    Yield()
    CameraMove(5140, 48000, 110030, 0)
    OP_67(0, 16000, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(295000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 67000, 111000, 0)
    OP_89(0x0001, 6000, 67000, 110000, 90)
    OP_89(0x0002, 4000, 67000, 110000, 270)
    OP_89(0x0003, 5000, 67000, 109000, 180)
    PlaySE(235, 0x01, 0x64)

    @scena.Lambda('lambda_0F1E')
    def lambda_0F1E():
        CameraMove(5140, 0, 110030, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F1E)

    @scena.Lambda('lambda_0F36')
    def lambda_0F36():
        OP_67(0, 9500, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F36)

    @scena.Lambda('lambda_0F4E')
    def lambda_0F4E():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F4E)

    FadeIn(1000, 0)
    OP_13(0x0120)

    @scena.Lambda('lambda_0F6A')
    def lambda_0F6A():
        ChrMoveTo(0x00FE, 5140, -1750, 110030, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F6A)

    Sleep(7800)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        ChrMoveTo(0x00FE, 5140, -1750, 110030, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F8A)

    Sleep(700)

    @scena.Lambda('lambda_0FAA')
    def lambda_0FAA():
        ChrMoveTo(0x00FE, 5140, -1750, 110030, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FAA)

    Sleep(600)

    @scena.Lambda('lambda_0FCA')
    def lambda_0FCA():
        ChrMoveTo(0x00FE, 5140, -1750, 110030, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FCA)

    Sleep(100)

    @scena.Lambda('lambda_0FEA')
    def lambda_0FEA():
        ChrMoveTo(0x00FE, 5140, -1750, 110030, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FEA)

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
    ChrSetPos(0x0000, 160, 0, 109620, 270)
    ChrSetPos(0x0001, 160, 0, 109620, 270)
    ChrSetPos(0x0002, 160, 0, 109620, 270)
    ChrSetPos(0x0003, 160, 0, 109620, 270)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x10BB
@scena.Code('func_0B_10BB')
def func_0B_10BB():
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
    CameraMove(-89000, 1050, 4000, 0)
    ChrSetPos(0x0101, -88500, 1050, 4500, 90)
    ChrSetPos(0x0102, -88500, 1050, 3500, 90)
    ChrSetPos(0x00F8, -89500, 1050, 4500, 90)
    ChrSetPos(0x00F9, -89500, 1050, 3500, 90)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    @scena.Lambda('lambda_1166')
    def lambda_1166():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1166)

    @scena.Lambda('lambda_1178')
    def lambda_1178():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1178)

    @scena.Lambda('lambda_118A')
    def lambda_118A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_118A)

    @scena.Lambda('lambda_119C')
    def lambda_119C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_119C)

    Sleep(2000)

    NewScene('ED6_DT21/C5300._SN', 122, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x11B7
@scena.Code('func_0C_11B7')
def func_0C_11B7():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-89000, 1050, 4000, 0)
    ChrSetPos(0x0101, -89500, 1050, 3500, 270)
    ChrSetPos(0x0102, -89500, 1050, 4500, 270)
    ChrSetPos(0x00F8, -88500, 1050, 3500, 270)
    ChrSetPos(0x00F9, -88500, 1050, 4500, 270)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    @scena.Lambda('lambda_1292')
    def lambda_1292():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1292)

    @scena.Lambda('lambda_12A4')
    def lambda_12A4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_12A4)

    @scena.Lambda('lambda_12B6')
    def lambda_12B6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_12B6)

    @scena.Lambda('lambda_12C8')
    def lambda_12C8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_12C8)

    Sleep(2500)

    Fade(500)
    CameraMove(-92500, 0, 4000, 0)
    ChrSetPos(0x0000, -92500, 0, 4000, 270)
    ChrSetPos(0x0001, -92500, 0, 4000, 270)
    ChrSetPos(0x0002, -92500, 0, 4000, 270)
    ChrSetPos(0x0003, -92500, 0, 4000, 270)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
