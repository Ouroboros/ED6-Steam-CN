import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1213_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1213   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1213.x'
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
    )

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -12480,
            z           = 0,
            y           = -20,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0090,
            word_18     = 0x1BA4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 12540,
            z           = 0,
            y           = 80,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0090,
            word_18     = 0x1BA5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -70,
            z           = 0,
            y           = 4810,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0090,
            word_18     = 0x1BA6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5870,
            z           = 0,
            y           = -210,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0090,
            word_18     = 0x1BA7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -5700,
            z           = 0,
            y           = -130,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0090,
            word_18     = 0x1BA8,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x176
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x176
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 4430,
            triggerZ            = 0,
            triggerY            = -22590,
            triggerRange        = 1000,
            actorX              = 4430,
            actorZ              = 0,
            actorY              = -23210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4600,
            triggerZ            = 0,
            triggerY            = -22590,
            triggerRange        = 1000,
            actorX              = -4690,
            actorZ              = 0,
            actorY              = -23250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -19260,
            triggerZ            = 0,
            triggerY            = 12750,
            triggerRange        = 1000,
            actorX              = -19730,
            actorZ              = 0,
            actorY              = 13160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12760,
            triggerZ            = 0,
            triggerY            = 19190,
            triggerRange        = 1000,
            actorX              = -13160,
            actorZ              = 0,
            actorY              = 19720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4500,
            triggerZ            = 0,
            triggerY            = 22580,
            triggerRange        = 1000,
            actorX              = -4590,
            actorZ              = 0,
            actorY              = 23200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4570,
            triggerZ            = 0,
            triggerY            = 22620,
            triggerRange        = 1000,
            actorX              = 4570,
            actorZ              = 0,
            actorY              = 23280,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12790,
            triggerZ            = 0,
            triggerY            = 19090,
            triggerRange        = 1000,
            actorX              = 13170,
            actorZ              = 0,
            actorY              = 19650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 19110,
            triggerZ            = 0,
            triggerY            = 12780,
            triggerRange        = 1000,
            actorX              = 19700,
            actorZ              = 0,
            actorY              = 13250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60,
            triggerZ            = 0,
            triggerY            = -700,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 0,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 5, 0x1B55)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2D4')

    def _loc_2CD(): pass

    label('loc_2CD')

    OP_6F(0x0000, 60)

    def _loc_2D4(): pass

    label('loc_2D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 6, 0x1B56)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2ED')

    def _loc_2E6(): pass

    label('loc_2E6')

    OP_6F(0x0001, 60)

    def _loc_2ED(): pass

    label('loc_2ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 7, 0x1B57)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FF',
    )

    OP_6F(0x0002, 0)

    Jump('loc_306')

    def _loc_2FF(): pass

    label('loc_2FF')

    OP_6F(0x0002, 60)

    def _loc_306(): pass

    label('loc_306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 0, 0x1B58)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_318',
    )

    OP_6F(0x0003, 0)

    Jump('loc_31F')

    def _loc_318(): pass

    label('loc_318')

    OP_6F(0x0003, 60)

    def _loc_31F(): pass

    label('loc_31F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 1, 0x1B59)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_331',
    )

    OP_6F(0x0004, 0)

    Jump('loc_338')

    def _loc_331(): pass

    label('loc_331')

    OP_6F(0x0004, 60)

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 2, 0x1B5A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34A',
    )

    OP_6F(0x0005, 0)

    Jump('loc_351')

    def _loc_34A(): pass

    label('loc_34A')

    OP_6F(0x0005, 60)

    def _loc_351(): pass

    label('loc_351')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 3, 0x1B5B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_363',
    )

    OP_6F(0x0006, 0)

    Jump('loc_36A')

    def _loc_363(): pass

    label('loc_363')

    OP_6F(0x0006, 60)

    def _loc_36A(): pass

    label('loc_36A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 4, 0x1B5C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37C',
    )

    OP_6F(0x0007, 0)

    Jump('loc_383')

    def _loc_37C(): pass

    label('loc_37C')

    OP_6F(0x0007, 60)

    def _loc_383(): pass

    label('loc_383')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 5, 0x1B5D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_395',
    )

    OP_6F(0x0008, 0)

    Jump('loc_39C')

    def _loc_395(): pass

    label('loc_395')

    OP_6F(0x0008, 60)

    def _loc_39C(): pass

    label('loc_39C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 4, 0x1BA4)),
            Expr.Return,
        ),
        'loc_3A8',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_3A8(): pass

    label('loc_3A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 5, 0x1BA5)),
            Expr.Return,
        ),
        'loc_3B4',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 6, 0x1BA6)),
            Expr.Return,
        ),
        'loc_3C0',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0374, 7, 0x1BA7)),
            Expr.Return,
        ),
        'loc_3CC',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0375, 0, 0x1BA8)),
            Expr.Return,
        ),
        'loc_3D8',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_3D8(): pass

    label('loc_3D8')

    Return()

# id: 0x0002 offset: 0x3D9
@scena.Code('func_02_3D9')
def func_02_3D9():
    UnlockAchievement(0x02, 0x0034, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 5, 0x1B55)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_44D',
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
    SetScenaFlags(ScenaFlag(0x036A, 5, 0x1B55))

    Jump('loc_4B3')

    def _loc_44D(): pass

    label('loc_44D')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_4B3(): pass

    label('loc_4B3')

    Jump('loc_4E7')

    def _loc_4B6(): pass

    label('loc_4B6')

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
    def _loc_4E7(): pass

    label('loc_4E7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4F5
@scena.Code('func_03_4F5')
def func_03_4F5():
    UnlockAchievement(0x02, 0x0035, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 6, 0x1B56)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_569',
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
    SetScenaFlags(ScenaFlag(0x036A, 6, 0x1B56))

    Jump('loc_5CF')

    def _loc_569(): pass

    label('loc_569')

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

    def _loc_5CF(): pass

    label('loc_5CF')

    Jump('loc_603')

    def _loc_5D2(): pass

    label('loc_5D2')

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
    def _loc_603(): pass

    label('loc_603')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x611
@scena.Code('func_04_611')
def func_04_611():
    UnlockAchievement(0x02, 0x0036, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036A, 7, 0x1B57)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_685',
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
    SetScenaFlags(ScenaFlag(0x036A, 7, 0x1B57))

    Jump('loc_6EB')

    def _loc_685(): pass

    label('loc_685')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_6EB(): pass

    label('loc_6EB')

    Jump('loc_71F')

    def _loc_6EE(): pass

    label('loc_6EE')

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
    def _loc_71F(): pass

    label('loc_71F')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x72D
@scena.Code('func_05_72D')
def func_05_72D():
    UnlockAchievement(0x02, 0x0037, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 0, 0x1B58)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_80A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['ＨＰ４'], 1)"),
            Expr.Return,
        ),
        'loc_7A1',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['ＨＰ４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036B, 0, 0x1B58))

    Jump('loc_807')

    def _loc_7A1(): pass

    label('loc_7A1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['ＨＰ４']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['ＨＰ４']),
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

    def _loc_807(): pass

    label('loc_807')

    Jump('loc_83B')

    def _loc_80A(): pass

    label('loc_80A')

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
    def _loc_83B(): pass

    label('loc_83B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x849
@scena.Code('func_06_849')
def func_06_849():
    UnlockAchievement(0x02, 0x0038, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 1, 0x1B59)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_926',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_8BD',
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
    SetScenaFlags(ScenaFlag(0x036B, 1, 0x1B59))

    Jump('loc_923')

    def _loc_8BD(): pass

    label('loc_8BD')

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

    def _loc_923(): pass

    label('loc_923')

    Jump('loc_957')

    def _loc_926(): pass

    label('loc_926')

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
    def _loc_957(): pass

    label('loc_957')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x965
@scena.Code('func_07_965')
def func_07_965():
    UnlockAchievement(0x02, 0x0039, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 2, 0x1B5A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A42',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_9D9',
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
    SetScenaFlags(ScenaFlag(0x036B, 2, 0x1B5A))

    Jump('loc_A3F')

    def _loc_9D9(): pass

    label('loc_9D9')

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

    def _loc_A3F(): pass

    label('loc_A3F')

    Jump('loc_A73')

    def _loc_A42(): pass

    label('loc_A42')

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
    def _loc_A73(): pass

    label('loc_A73')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xA81
@scena.Code('func_08_A81')
def func_08_A81():
    UnlockAchievement(0x02, 0x003A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 3, 0x1B5B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大吃一惊曲奇饼'], 1)"),
            Expr.Return,
        ),
        'loc_AF5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036B, 3, 0x1B5B))

    Jump('loc_B5B')

    def _loc_AF5(): pass

    label('loc_AF5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
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

    def _loc_B5B(): pass

    label('loc_B5B')

    Jump('loc_B8F')

    def _loc_B5E(): pass

    label('loc_B5E')

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
    def _loc_B8F(): pass

    label('loc_B8F')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE7',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0014)"),
            Expr.Return,
        ),
        'loc_BAE',
    )

    Jump('loc_BE7')

    def _loc_BAE(): pass

    label('loc_BAE')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE7(): pass

    label('loc_BE7')

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xBF0
@scena.Code('func_09_BF0')
def func_09_BF0():
    UnlockAchievement(0x02, 0x003B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 4, 0x1B5C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_C64',
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
    SetScenaFlags(ScenaFlag(0x036B, 4, 0x1B5C))

    Jump('loc_CCA')

    def _loc_C64(): pass

    label('loc_C64')

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
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_CCA(): pass

    label('loc_CCA')

    Jump('loc_CFE')

    def _loc_CCD(): pass

    label('loc_CCD')

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
    def _loc_CFE(): pass

    label('loc_CFE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xD0C
@scena.Code('func_0A_D0C')
def func_0A_D0C():
    UnlockAchievement(0x02, 0x003C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036B, 5, 0x1B5D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['琥耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_D80',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['琥耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036B, 5, 0x1B5D))

    Jump('loc_DE6')

    def _loc_D80(): pass

    label('loc_D80')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['琥耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['琥耀石护符']),
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

    def _loc_DE6(): pass

    label('loc_DE6')

    Jump('loc_E1A')

    def _loc_DE9(): pass

    label('loc_DE9')

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
    def _loc_E1A(): pass

    label('loc_E1A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
