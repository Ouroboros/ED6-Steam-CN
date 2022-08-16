import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1214_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1214   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1214.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT09/CH10410._CH', 'ED6_DT09/CH10410P._CP'),
        ('ED6_DT09/CH10411._CH', 'ED6_DT09/CH10411P._CP'),
        ('ED6_DT09/CH10420._CH', 'ED6_DT09/CH10420P._CP'),
        ('ED6_DT09/CH10421._CH', 'ED6_DT09/CH10421P._CP'),
        ('ED6_DT09/CH10430._CH', 'ED6_DT09/CH10430P._CP'),
        ('ED6_DT09/CH10431._CH', 'ED6_DT09/CH10431P._CP'),
        ('ED6_DT09/CH10440._CH', 'ED6_DT09/CH10440P._CP'),
        ('ED6_DT09/CH10441._CH', 'ED6_DT09/CH10441P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 10,
            z                   = 1000,
            y                   = -18040,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            x           = -20,
            z           = 0,
            y           = 3950,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x008F,
            word_18     = 0x1BA9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -20,
            z           = 0,
            y           = -4200,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x008F,
            word_18     = 0x1BAA,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x142
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x142
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = -17250,
            triggerRange        = 1000,
            actorX              = 10,
            actorZ              = 0,
            actorY              = -18040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9320,
            triggerZ            = 0,
            triggerY            = 9340,
            triggerRange        = 1000,
            actorX              = 8670,
            actorZ              = 0,
            actorY              = 8680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9260,
            triggerZ            = 0,
            triggerY            = -9330,
            triggerRange        = 1000,
            actorX              = -8820,
            actorZ              = 0,
            actorY              = -8890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9370,
            triggerZ            = 0,
            triggerY            = -9350,
            triggerRange        = 1000,
            actorX              = 8910,
            actorZ              = 0,
            actorY              = -8880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9360,
            triggerZ            = 0,
            triggerY            = 9260,
            triggerRange        = 1000,
            actorX              = -8830,
            actorZ              = 0,
            actorY              = 8860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4530,
            triggerZ            = 0,
            triggerY            = -22520,
            triggerRange        = 1000,
            actorX              = 4610,
            actorZ              = 0,
            actorY              = -23140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4490,
            triggerZ            = 0,
            triggerY            = -22490,
            triggerRange        = 1000,
            actorX              = -4490,
            actorZ              = 0,
            actorY              = -23150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x23E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x23F
@scena.Code('func_01_23F')
def func_01_23F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 7, 0x1B5F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_251',
    )

    OP_6F(0x0000, 0)

    Jump('loc_258')

    def _loc_251(): pass

    label('loc_251')

    OP_6F(0x0000, 60)

    def _loc_258(): pass

    label('loc_258')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 1, 0x1B61)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26A',
    )

    OP_6F(0x0001, 0)

    Jump('loc_271')

    def _loc_26A(): pass

    label('loc_26A')

    OP_6F(0x0001, 60)

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 2, 0x1B62)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_283',
    )

    OP_6F(0x0002, 0)

    Jump('loc_28A')

    def _loc_283(): pass

    label('loc_283')

    OP_6F(0x0002, 60)

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 3, 0x1B63)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29C',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2A3')

    def _loc_29C(): pass

    label('loc_29C')

    OP_6F(0x0003, 60)

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 4, 0x1B64)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B5',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2BC')

    def _loc_2B5(): pass

    label('loc_2B5')

    OP_6F(0x0004, 60)

    def _loc_2BC(): pass

    label('loc_2BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 5, 0x1B65)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_6F(0x0005, 0)

    Jump('loc_2D5')

    def _loc_2CE(): pass

    label('loc_2CE')

    OP_6F(0x0005, 60)

    def _loc_2D5(): pass

    label('loc_2D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 6, 0x1B66)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E7',
    )

    OP_6F(0x0006, 0)

    Jump('loc_2EE')

    def _loc_2E7(): pass

    label('loc_2E7')

    OP_6F(0x0006, 60)

    def _loc_2EE(): pass

    label('loc_2EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0375, 1, 0x1BA9)),
            Expr.Return,
        ),
        'loc_2FA',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_2FA(): pass

    label('loc_2FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0375, 2, 0x1BAA)),
            Expr.Return,
        ),
        'loc_306',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_306(): pass

    label('loc_306')

    Return()

# id: 0x0002 offset: 0x307
@scena.Code('func_02_307')
def func_02_307():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_31C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_307')

    def _loc_31C(): pass

    label('loc_31C')

    Return()

# id: 0x0003 offset: 0x31D
@scena.Code('func_03_31D')
def func_03_31D():
    UnlockAchievement(0x02, 0x000A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 7, 0x1B5F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 0, 0x1B60)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_401',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0374')
    def lambda_0374():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0374)

    @scena.Lambda('lambda_038F')
    def lambda_038F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_038F)

    ChrClearFlags(0x0008, 0x0080)

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
    Battle(0x00000092, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_3DC'),
        (0x00000002, 'loc_3EE'),
        (0x00000001, 'loc_3FE'),
        (-1, 'loc_401'),
    )

    def _loc_3DC(): pass

    label('loc_3DC')

    SetScenaFlags(ScenaFlag(0x036C, 0, 0x1B60))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_401')

    def _loc_3EE(): pass

    label('loc_3EE')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_3FE(): pass

    label('loc_3FE')

    OP_B4(0x00)

    Return()

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['幻影Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_450',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['幻影Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036B, 7, 0x1B5F))

    Jump('loc_4B2')

    def _loc_450(): pass

    label('loc_450')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['幻影Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['幻影Ⅱ']),
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

    def _loc_4B2(): pass

    label('loc_4B2')

    Jump('loc_4E4')

    def _loc_4B5(): pass

    label('loc_4B5')

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
    def _loc_4E4(): pass

    label('loc_4E4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4F2
@scena.Code('func_04_4F2')
def func_04_4F2():
    UnlockAchievement(0x02, 0x003D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 1, 0x1B61)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_566',
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
    SetScenaFlags(ScenaFlag(0x036C, 1, 0x1B61))

    Jump('loc_5CC')

    def _loc_566(): pass

    label('loc_566')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_5CC(): pass

    label('loc_5CC')

    Jump('loc_600')

    def _loc_5CF(): pass

    label('loc_5CF')

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
    def _loc_600(): pass

    label('loc_600')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x60E
@scena.Code('func_05_60E')
def func_05_60E():
    UnlockAchievement(0x02, 0x003E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 2, 0x1B62)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_682',
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
    SetScenaFlags(ScenaFlag(0x036C, 2, 0x1B62))

    Jump('loc_6E8')

    def _loc_682(): pass

    label('loc_682')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_6E8(): pass

    label('loc_6E8')

    Jump('loc_71C')

    def _loc_6EB(): pass

    label('loc_6EB')

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
    def _loc_71C(): pass

    label('loc_71C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x72A
@scena.Code('func_06_72A')
def func_06_72A():
    UnlockAchievement(0x02, 0x003F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 3, 0x1B63)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_807',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['斗魂扎头巾'], 1)"),
            Expr.Return,
        ),
        'loc_79E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['斗魂扎头巾']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036C, 3, 0x1B63))

    Jump('loc_804')

    def _loc_79E(): pass

    label('loc_79E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['斗魂扎头巾']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['斗魂扎头巾']),
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

    def _loc_804(): pass

    label('loc_804')

    Jump('loc_838')

    def _loc_807(): pass

    label('loc_807')

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
    def _loc_838(): pass

    label('loc_838')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x846
@scena.Code('func_07_846')
def func_07_846():
    UnlockAchievement(0x02, 0x0040, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 4, 0x1B64)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_923',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_8BA',
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
    SetScenaFlags(ScenaFlag(0x036C, 4, 0x1B64))

    Jump('loc_920')

    def _loc_8BA(): pass

    label('loc_8BA')

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

    def _loc_920(): pass

    label('loc_920')

    Jump('loc_954')

    def _loc_923(): pass

    label('loc_923')

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
    def _loc_954(): pass

    label('loc_954')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x962
@scena.Code('func_08_962')
def func_08_962():
    UnlockAchievement(0x02, 0x0041, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 5, 0x1B65)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_9D6',
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
    SetScenaFlags(ScenaFlag(0x036C, 5, 0x1B65))

    Jump('loc_A3C')

    def _loc_9D6(): pass

    label('loc_9D6')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_A3C(): pass

    label('loc_A3C')

    Jump('loc_A70')

    def _loc_A3F(): pass

    label('loc_A3F')

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
    def _loc_A70(): pass

    label('loc_A70')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xA7E
@scena.Code('func_09_A7E')
def func_09_A7E():
    UnlockAchievement(0x02, 0x0042, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 6, 0x1B66)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['提神果冻'], 1)"),
            Expr.Return,
        ),
        'loc_AF2',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['提神果冻']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036C, 6, 0x1B66))

    Jump('loc_B58')

    def _loc_AF2(): pass

    label('loc_AF2')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['提神果冻']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['提神果冻']),
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

    def _loc_B58(): pass

    label('loc_B58')

    Jump('loc_B8C')

    def _loc_B5B(): pass

    label('loc_B5B')

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
    def _loc_B8C(): pass

    label('loc_B8C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
