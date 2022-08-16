import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5305_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5305   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5305.x'
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
        ScenaNpcData(
            name                = '',
            x                   = 60,
            z                   = 3500,
            y                   = -94030,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -91910,
            z           = 2230,
            y           = 96640,
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
            x           = -98860,
            z           = 50,
            y           = 8530,
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
            x           = -79920,
            z           = 2350,
            y           = -72810,
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
            x           = 83880,
            z           = 2180,
            y           = -85080,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 100050,
            y           = -2000,
            z           = 9110,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10004 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -107300,
            triggerZ            = 0,
            triggerY            = 4900,
            triggerRange        = 1000,
            actorX              = -107910,
            actorZ              = 0,
            actorY              = 4870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -107300,
            triggerZ            = 0,
            triggerY            = 9030,
            triggerRange        = 1000,
            actorX              = -107910,
            actorZ              = 0,
            actorY              = 9000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -107290,
            triggerZ            = 0,
            triggerY            = 13070,
            triggerRange        = 1000,
            actorX              = -107980,
            actorZ              = 0,
            actorY              = 12940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90700,
            triggerZ            = 0,
            triggerY            = 13010,
            triggerRange        = 1000,
            actorX              = -90050,
            actorZ              = 0,
            actorY              = 13040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90710,
            triggerZ            = 0,
            triggerY            = 8940,
            triggerRange        = 1000,
            actorX              = -90060,
            actorZ              = 0,
            actorY              = 8980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -90710,
            triggerZ            = 0,
            triggerY            = 5000,
            triggerRange        = 1000,
            actorX              = -90020,
            actorZ              = 0,
            actorY              = 5030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -540,
            triggerZ            = 2000,
            triggerY            = -94060,
            triggerRange        = 1000,
            actorX              = 60,
            actorZ              = 2000,
            actorY              = -94030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2E7',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0A_D3C)

    Jump('loc_30A')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x72),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FA',
    )

    Event(0, func_0C_1054)

    Jump('loc_30A')

    def _loc_2FA(): pass

    label('loc_2FA')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x74),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30A',
    )

    Event(0, func_0E_139C)

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Return,
        ),
        'loc_351',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_351',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_351(): pass

    label('loc_351')

    Return()

# id: 0x0001 offset: 0x352
@scena.Code('func_01_352')
def func_01_352():
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
        0x000B,
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
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 3, 0x2383)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_385',
    )

    OP_6F(0x0003, 0)

    Jump('loc_38C')

    def _loc_385(): pass

    label('loc_385')

    OP_6F(0x0003, 60)

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 4, 0x2384)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_6F(0x0004, 0)

    Jump('loc_3A5')

    def _loc_39E(): pass

    label('loc_39E')

    OP_6F(0x0004, 60)

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 5, 0x2385)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3BE')

    def _loc_3B7(): pass

    label('loc_3B7')

    OP_6F(0x0005, 60)

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 6, 0x2386)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D0',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3D7')

    def _loc_3D0(): pass

    label('loc_3D0')

    OP_6F(0x0006, 60)

    def _loc_3D7(): pass

    label('loc_3D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 7, 0x2387)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E9',
    )

    OP_6F(0x0007, 0)

    Jump('loc_3F0')

    def _loc_3E9(): pass

    label('loc_3E9')

    OP_6F(0x0007, 60)

    def _loc_3F0(): pass

    label('loc_3F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 0, 0x2388)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_402',
    )

    OP_6F(0x0008, 0)

    Jump('loc_409')

    def _loc_402(): pass

    label('loc_402')

    OP_6F(0x0008, 60)

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 1, 0x2389)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41B',
    )

    OP_6F(0x0009, 0)

    Jump('loc_422')

    def _loc_41B(): pass

    label('loc_41B')

    OP_6F(0x0009, 60)

    def _loc_422(): pass

    label('loc_422')

    OP_10(0x0E, 0x00)
    OP_71(0x0001, 0x0004)
    StopEffect(0x84, 0x00)
    StopEffect(0x85, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_452',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_10(0x10, 0x00)
    StopEffect(0x83, 0x00)

    Jump('loc_4A3')

    def _loc_452(): pass

    label('loc_452')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 600)
    OP_10(0x10, 0x01)
    StopEffect(0x83, 0x00)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_1B(0x10, 0x00, 0x000D)

    def _loc_4A3(): pass

    label('loc_4A3')

    PlaySE(320, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x4A9
@scena.Code('func_02_4A9')
def func_02_4A9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4BE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4A9')

    def _loc_4BE(): pass

    label('loc_4BE')

    Return()

# id: 0x0003 offset: 0x4BF
@scena.Code('func_03_4BF')
def func_03_4BF():
    UnlockAchievement(0x02, 0x0142, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 3, 0x2383)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_533',
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
    SetScenaFlags(ScenaFlag(0x0470, 3, 0x2383))

    Jump('loc_599')

    def _loc_533(): pass

    label('loc_533')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_599(): pass

    label('loc_599')

    Jump('loc_5CD')

    def _loc_59C(): pass

    label('loc_59C')

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
    def _loc_5CD(): pass

    label('loc_5CD')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5DB
@scena.Code('func_04_5DB')
def func_04_5DB():
    UnlockAchievement(0x02, 0x0143, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 4, 0x2384)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_64F',
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
    SetScenaFlags(ScenaFlag(0x0470, 4, 0x2384))

    Jump('loc_6B5')

    def _loc_64F(): pass

    label('loc_64F')

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

    def _loc_6B5(): pass

    label('loc_6B5')

    Jump('loc_6E9')

    def _loc_6B8(): pass

    label('loc_6B8')

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
    def _loc_6E9(): pass

    label('loc_6E9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6F7
@scena.Code('func_05_6F7')
def func_05_6F7():
    UnlockAchievement(0x02, 0x0144, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 5, 0x2385)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_76B',
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
    SetScenaFlags(ScenaFlag(0x0470, 5, 0x2385))

    Jump('loc_7D1')

    def _loc_76B(): pass

    label('loc_76B')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_7D1(): pass

    label('loc_7D1')

    Jump('loc_805')

    def _loc_7D4(): pass

    label('loc_7D4')

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
    def _loc_805(): pass

    label('loc_805')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x813
@scena.Code('func_06_813')
def func_06_813():
    UnlockAchievement(0x02, 0x0145, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 6, 0x2386)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_887',
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
    SetScenaFlags(ScenaFlag(0x0470, 6, 0x2386))

    Jump('loc_8ED')

    def _loc_887(): pass

    label('loc_887')

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

    def _loc_8ED(): pass

    label('loc_8ED')

    Jump('loc_921')

    def _loc_8F0(): pass

    label('loc_8F0')

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
    def _loc_921(): pass

    label('loc_921')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x92F
@scena.Code('func_07_92F')
def func_07_92F():
    UnlockAchievement(0x02, 0x0146, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0470, 7, 0x2387)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A0C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_9A3',
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
    SetScenaFlags(ScenaFlag(0x0470, 7, 0x2387))

    Jump('loc_A09')

    def _loc_9A3(): pass

    label('loc_9A3')

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
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_A09(): pass

    label('loc_A09')

    Jump('loc_A3D')

    def _loc_A0C(): pass

    label('loc_A0C')

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
    def _loc_A3D(): pass

    label('loc_A3D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xA4B
@scena.Code('func_08_A4B')
def func_08_A4B():
    UnlockAchievement(0x02, 0x0147, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 0, 0x2388)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B28',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_ABF',
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
    SetScenaFlags(ScenaFlag(0x0471, 0, 0x2388))

    Jump('loc_B25')

    def _loc_ABF(): pass

    label('loc_ABF')

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
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_B25(): pass

    label('loc_B25')

    Jump('loc_B59')

    def _loc_B28(): pass

    label('loc_B28')

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
    def _loc_B59(): pass

    label('loc_B59')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xB67
@scena.Code('func_09_B67')
def func_09_B67():
    UnlockAchievement(0x02, 0x0148, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 1, 0x2389)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0471, 2, 0x238A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C4B',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0009, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0009, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0BBE')
    def lambda_0BBE():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BBE)

    @scena.Lambda('lambda_0BD9')
    def lambda_0BD9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0BD9)

    ChrClearFlags(0x0009, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000532, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_C26'),
        (0x00000002, 'loc_C38'),
        (0x00000001, 'loc_C48'),
        (-1, 'loc_C4B'),
    )

    def _loc_C26(): pass

    label('loc_C26')

    SetScenaFlags(ScenaFlag(0x0471, 2, 0x238A))
    OP_6F(0x0009, 60)
    Sleep(500)

    Jump('loc_C4B')

    def _loc_C38(): pass

    label('loc_C38')

    OP_6F(0x0009, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_C48(): pass

    label('loc_C48')

    OP_B4(0x00)

    Return()

    def _loc_C4B(): pass

    label('loc_C4B')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大地女神之服'], 1)"),
            Expr.Return,
        ),
        'loc_C9A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大地女神之服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0471, 1, 0x2389))

    Jump('loc_CFC')

    def _loc_C9A(): pass

    label('loc_C9A')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大地女神之服']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大地女神之服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_CFC(): pass

    label('loc_CFC')

    Jump('loc_D2E')

    def _loc_CFF(): pass

    label('loc_CFF')

    FadeOut(300, 0, 100)

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
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-28890, 80, 108700, 0)
    OP_67(0, 7020, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(301000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 600)
    Sleep(1500)

    PlaySE(225, 0x00, 0x64)
    Sleep(3000)

    PlaySE(112, 0x00, 0x64)
    OP_73(0x0000)

    @scena.Lambda('lambda_0DC4')
    def lambda_0DC4():
        CameraMove(-890, 1090, 98940, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DC4)

    @scena.Lambda('lambda_0DDC')
    def lambda_0DDC():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DDC)

    OP_6C(315000, 5000)
    CameraSetDistance(3500, 0)
    OP_6E(262, 0)
    Fade(1000)
    PlaySE(215, 0x00, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0xE65
@scena.Code('func_0B_E65')
def func_0B_E65():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0002)
    ChrSetPos(0x0008, 100050, -1750, 9110, 0)
    Yield()
    Fade(1000)
    CameraMove(100050, 0, 9110, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 0, 10000, 0)
    OP_89(0x0001, 101000, 0, 9000, 90)
    OP_89(0x0002, 99000, 0, 9000, 270)
    OP_89(0x0003, 100000, 0, 8000, 180)
    OP_0D()
    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0F15')
    def lambda_0F15():
        ChrMoveTo(0x00FE, 100050, 65000, 9110, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F15)

    Sleep(500)

    @scena.Lambda('lambda_0F35')
    def lambda_0F35():
        CameraMove(100050, 35000, 9110, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F35)

    @scena.Lambda('lambda_0F4D')
    def lambda_0F4D():
        OP_67(0, 14000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F4D)

    @scena.Lambda('lambda_0F65')
    def lambda_0F65():
        OP_6C(335000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F65)

    Sleep(500)

    @scena.Lambda('lambda_0F7A')
    def lambda_0F7A():
        ChrMoveTo(0x00FE, 100050, 65000, 9110, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F7A)

    Sleep(500)

    @scena.Lambda('lambda_0F9A')
    def lambda_0F9A():
        ChrMoveTo(0x00FE, 100050, 65000, 9110, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F9A)

    Sleep(400)

    @scena.Lambda('lambda_0FBA')
    def lambda_0FBA():
        ChrMoveTo(0x00FE, 100050, 65000, 9110, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FBA)

    Sleep(200)

    @scena.Lambda('lambda_0FDA')
    def lambda_0FDA():
        ChrMoveTo(0x00FE, 100050, 65000, 9110, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FDA)

    Sleep(100)

    @scena.Lambda('lambda_0FFA')
    def lambda_0FFA():
        ChrMoveTo(0x00FE, 100050, 65000, 9110, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FFA)

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
    SetScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    ClearScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    ClearScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    ClearScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x1054
@scena.Code('func_0C_1054')
def func_0C_1054():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0002)
    ChrSetPos(0x0008, 100050, 66000, 9110, 0)
    Yield()
    CameraMove(100050, 48000, 9110, 0)
    OP_67(0, 16000, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 67000, 10000, 0)
    OP_89(0x0001, 101000, 67000, 9000, 90)
    OP_89(0x0002, 99000, 67000, 9000, 270)
    OP_89(0x0003, 100000, 67000, 8000, 180)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_1103')
    def lambda_1103():
        CameraMove(100050, 0, 9110, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1103)

    @scena.Lambda('lambda_111B')
    def lambda_111B():
        OP_67(0, 9500, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_111B)

    @scena.Lambda('lambda_1133')
    def lambda_1133():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1133)

    FadeIn(1000, 0)
    OP_13(0x011F)

    @scena.Lambda('lambda_114F')
    def lambda_114F():
        ChrMoveTo(0x00FE, 100050, -1750, 9110, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_114F)

    Sleep(7800)

    @scena.Lambda('lambda_116F')
    def lambda_116F():
        ChrMoveTo(0x00FE, 100050, -1750, 9110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_116F)

    Sleep(700)

    @scena.Lambda('lambda_118F')
    def lambda_118F():
        ChrMoveTo(0x00FE, 100050, -1750, 9110, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_118F)

    Sleep(600)

    @scena.Lambda('lambda_11AF')
    def lambda_11AF():
        ChrMoveTo(0x00FE, 100050, -1750, 9110, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11AF)

    Sleep(100)

    @scena.Lambda('lambda_11CF')
    def lambda_11CF():
        ChrMoveTo(0x00FE, 100050, -1750, 9110, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11CF)

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
    ChrSetPos(0x0000, 99940, 0, 4350, 180)
    ChrSetPos(0x0001, 99940, 0, 4350, 180)
    ChrSetPos(0x0002, 99940, 0, 4350, 180)
    ChrSetPos(0x0003, 99940, 0, 4350, 180)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x12A0
@scena.Code('func_0D_12A0')
def func_0D_12A0():
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
    CameraMove(-1000, 1050, 99000, 0)
    ChrSetPos(0x0101, -500, 1050, 98500, 180)
    ChrSetPos(0x0102, -1500, 1050, 98500, 180)
    ChrSetPos(0x00F8, -500, 1050, 99500, 180)
    ChrSetPos(0x00F9, -1500, 1050, 99500, 180)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    @scena.Lambda('lambda_134B')
    def lambda_134B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_134B)

    @scena.Lambda('lambda_135D')
    def lambda_135D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_135D)

    @scena.Lambda('lambda_136F')
    def lambda_136F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_136F)

    @scena.Lambda('lambda_1381')
    def lambda_1381():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1381)

    Sleep(2000)

    NewScene('ED6_DT21/C5300._SN', 122, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x139C
@scena.Code('func_0E_139C')
def func_0E_139C():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-1000, 1050, 99000, 0)
    ChrSetPos(0x0101, -1500, 1050, 99500, 0)
    ChrSetPos(0x0102, -500, 1050, 99500, 0)
    ChrSetPos(0x00F8, -1500, 1050, 98500, 0)
    ChrSetPos(0x00F9, -500, 1050, 98500, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    @scena.Lambda('lambda_1477')
    def lambda_1477():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1477)

    @scena.Lambda('lambda_1489')
    def lambda_1489():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1489)

    @scena.Lambda('lambda_149B')
    def lambda_149B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_149B)

    @scena.Lambda('lambda_14AD')
    def lambda_14AD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_14AD)

    Sleep(2500)

    Fade(500)
    CameraMove(-1000, 0, 103000, 0)
    ChrSetPos(0x0000, -1000, 0, 103000, 0)
    ChrSetPos(0x0001, -1000, 0, 103000, 0)
    ChrSetPos(0x0002, -1000, 0, 103000, 0)
    ChrSetPos(0x0003, -1000, 0, 103000, 0)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
