import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1703_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1703   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1703.x'
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
        ScenaNpcData(
            name                = '',
            x                   = 32009,
            z                   = 2400,
            y                   = 30,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -16079,
            z           = 400,
            y           = 31920,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1E88,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -16020,
            z           = 400,
            y           = 16040,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E89,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -16010,
            z           = 400,
            y           = -40,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1E8A,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -16270,
            z           = 400,
            y           = -16340,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E8B,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 16040,
            z           = 400,
            y           = -15950,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1E8C,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 15850,
            z           = 400,
            y           = -200,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1E8D,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 15800,
            z           = 400,
            y           = 15870,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1E8E,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 16129,
            z           = 400,
            y           = 32250,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1E8F,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x21A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x21A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -31950,
            triggerZ            = 400,
            triggerY            = 31360,
            triggerRange        = 1000,
            actorX              = -31950,
            actorZ              = 400,
            actorY              = 31980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 32009,
            triggerZ            = 400,
            triggerY            = 820,
            triggerRange        = 1000,
            actorX              = 32009,
            actorZ              = 400,
            actorY              = 30,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60,
            triggerZ            = 400,
            triggerY            = 37280,
            triggerRange        = 1000,
            actorX              = 20,
            actorZ              = 400,
            actorY              = 37940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = 400,
            triggerY            = 11720,
            triggerRange        = 1000,
            actorX              = -20,
            actorZ              = 400,
            actorY              = 10980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20,
            triggerZ            = 400,
            triggerY            = 4280,
            triggerRange        = 1000,
            actorX              = 20,
            actorZ              = 400,
            actorY              = 4900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10,
            triggerZ            = 400,
            triggerY            = -21280,
            triggerRange        = 1000,
            actorX              = -10,
            actorZ              = 400,
            actorY              = -22070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2F2
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_322'),
        (0x00000065, 'loc_329'),
        (0x00000066, 'loc_330'),
        (0x00000067, 'loc_337'),
        (0x00000068, 'loc_33E'),
        (0x00000069, 'loc_345'),
        (0x0000006A, 'loc_34C'),
        (0x0000006B, 'loc_353'),
        (0x0000006C, 'loc_35A'),
        (0x0000006D, 'loc_361'),
        (-1, 'loc_368'),
    )

    def _loc_322(): pass

    label('loc_322')

    Event(0, func_09_C31)

    Jump('loc_368')

    def _loc_329(): pass

    label('loc_329')

    Event(0, func_0B_DA9)

    Jump('loc_368')

    def _loc_330(): pass

    label('loc_330')

    Event(0, func_0D_F3C)

    Jump('loc_368')

    def _loc_337(): pass

    label('loc_337')

    Event(0, func_0F_10B4)

    Jump('loc_368')

    def _loc_33E(): pass

    label('loc_33E')

    Event(0, func_11_1247)

    Jump('loc_368')

    def _loc_345(): pass

    label('loc_345')

    Event(0, func_13_13DA)

    Jump('loc_368')

    def _loc_34C(): pass

    label('loc_34C')

    Event(0, func_15_156D)

    Jump('loc_368')

    def _loc_353(): pass

    label('loc_353')

    Event(0, func_17_16E5)

    Jump('loc_368')

    def _loc_35A(): pass

    label('loc_35A')

    Event(0, func_19_185D)

    Jump('loc_368')

    def _loc_361(): pass

    label('loc_361')

    Event(0, func_1B_19F0)

    Jump('loc_368')

    def _loc_368(): pass

    label('loc_368')

    Return()

# id: 0x0001 offset: 0x369
@scena.Code('func_01_369')
def func_01_369():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 2, 0x1FAA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37B',
    )

    OP_6F(0x0000, 0)

    Jump('loc_382')

    def _loc_37B(): pass

    label('loc_37B')

    OP_6F(0x0000, 60)

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 4, 0x1FAC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_394',
    )

    OP_6F(0x0001, 0)

    Jump('loc_39B')

    def _loc_394(): pass

    label('loc_394')

    OP_6F(0x0001, 60)

    def _loc_39B(): pass

    label('loc_39B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 6, 0x1FAE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AD',
    )

    OP_6F(0x0002, 0)

    Jump('loc_3B4')

    def _loc_3AD(): pass

    label('loc_3AD')

    OP_6F(0x0002, 60)

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 7, 0x1FAF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C6',
    )

    OP_6F(0x0003, 0)

    Jump('loc_3CD')

    def _loc_3C6(): pass

    label('loc_3C6')

    OP_6F(0x0003, 60)

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 0, 0x1FB0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DF',
    )

    OP_6F(0x0004, 0)

    Jump('loc_3E6')

    def _loc_3DF(): pass

    label('loc_3DF')

    OP_6F(0x0004, 60)

    def _loc_3E6(): pass

    label('loc_3E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 1, 0x1FB1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F8',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3FF')

    def _loc_3F8(): pass

    label('loc_3F8')

    OP_6F(0x0005, 60)

    def _loc_3FF(): pass

    label('loc_3FF')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 0, 0x1E88)),
            Expr.Return,
        ),
        'loc_433',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_433(): pass

    label('loc_433')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 1, 0x1E89)),
            Expr.Return,
        ),
        'loc_43F',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_43F(): pass

    label('loc_43F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 2, 0x1E8A)),
            Expr.Return,
        ),
        'loc_44B',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 3, 0x1E8B)),
            Expr.Return,
        ),
        'loc_457',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_457(): pass

    label('loc_457')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 4, 0x1E8C)),
            Expr.Return,
        ),
        'loc_463',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_463(): pass

    label('loc_463')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 5, 0x1E8D)),
            Expr.Return,
        ),
        'loc_46F',
    )

    ChrSetFlags(0x000E, 0x0080)

    def _loc_46F(): pass

    label('loc_46F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 6, 0x1E8E)),
            Expr.Return,
        ),
        'loc_47B',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_47B(): pass

    label('loc_47B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D1, 7, 0x1E8F)),
            Expr.Return,
        ),
        'loc_487',
    )

    ChrSetFlags(0x0010, 0x0080)

    def _loc_487(): pass

    label('loc_487')

    OP_1B(0x00, 0x00, 0x000A)
    OP_1B(0x01, 0x00, 0x000C)
    OP_1B(0x02, 0x00, 0x000E)
    OP_1B(0x03, 0x00, 0x0010)
    OP_1B(0x04, 0x00, 0x0012)
    OP_1B(0x05, 0x00, 0x0014)
    OP_1B(0x06, 0x00, 0x0016)
    OP_1B(0x07, 0x00, 0x0018)
    OP_1B(0x08, 0x00, 0x001A)
    OP_1B(0x09, 0x00, 0x001C)

    Return()

# id: 0x0002 offset: 0x4BA
@scena.Code('func_02_4BA')
def func_02_4BA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4CF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4BA')

    def _loc_4CF(): pass

    label('loc_4CF')

    Return()

# id: 0x0003 offset: 0x4D0
@scena.Code('func_03_4D0')
def func_03_4D0():
    UnlockAchievement(0x02, 0x0079, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 2, 0x1FAA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['暴风加农炮'], 1)"),
            Expr.Return,
        ),
        'loc_544',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['暴风加农炮']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F5, 2, 0x1FAA))

    Jump('loc_5AA')

    def _loc_544(): pass

    label('loc_544')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['暴风加农炮']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['暴风加农炮']),
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

    def _loc_5AA(): pass

    label('loc_5AA')

    Jump('loc_5DE')

    def _loc_5AD(): pass

    label('loc_5AD')

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
    def _loc_5DE(): pass

    label('loc_5DE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5EC
@scena.Code('func_04_5EC')
def func_04_5EC():
    UnlockAchievement(0x02, 0x007A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 4, 0x1FAC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_784',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 5, 0x1FAD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D0',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0643')
    def lambda_0643():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0643)

    @scena.Lambda('lambda_065E')
    def lambda_065E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_065E)

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
    Battle(0x000003FC, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_6AB'),
        (0x00000002, 'loc_6BD'),
        (0x00000001, 'loc_6CD'),
        (-1, 'loc_6D0'),
    )

    def _loc_6AB(): pass

    label('loc_6AB')

    SetScenaFlags(ScenaFlag(0x03F5, 5, 0x1FAD))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_6D0')

    def _loc_6BD(): pass

    label('loc_6BD')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_6CD(): pass

    label('loc_6CD')

    OP_B4(0x00)

    Return()

    def _loc_6D0(): pass

    label('loc_6D0')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['洗礼圣瓶'], 1)"),
            Expr.Return,
        ),
        'loc_71F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['洗礼圣瓶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F5, 4, 0x1FAC))

    Jump('loc_781')

    def _loc_71F(): pass

    label('loc_71F')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['洗礼圣瓶']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['洗礼圣瓶']),
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

    def _loc_781(): pass

    label('loc_781')

    Jump('loc_7B3')

    def _loc_784(): pass

    label('loc_784')

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
    def _loc_7B3(): pass

    label('loc_7B3')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7C1
@scena.Code('func_05_7C1')
def func_05_7C1():
    UnlockAchievement(0x02, 0x007B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 6, 0x1FAE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_835',
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
    SetScenaFlags(ScenaFlag(0x03F5, 6, 0x1FAE))

    Jump('loc_89B')

    def _loc_835(): pass

    label('loc_835')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_89B(): pass

    label('loc_89B')

    Jump('loc_8CF')

    def _loc_89E(): pass

    label('loc_89E')

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
    def _loc_8CF(): pass

    label('loc_8CF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8DD
@scena.Code('func_06_8DD')
def func_06_8DD():
    UnlockAchievement(0x02, 0x007C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F5, 7, 0x1FAF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9BA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_951',
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
    SetScenaFlags(ScenaFlag(0x03F5, 7, 0x1FAF))

    Jump('loc_9B7')

    def _loc_951(): pass

    label('loc_951')

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

    def _loc_9B7(): pass

    label('loc_9B7')

    Jump('loc_9EB')

    def _loc_9BA(): pass

    label('loc_9BA')

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
    def _loc_9EB(): pass

    label('loc_9EB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x9F9
@scena.Code('func_07_9F9')
def func_07_9F9():
    UnlockAchievement(0x02, 0x007D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 0, 0x1FB0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AD6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_A6D',
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
    SetScenaFlags(ScenaFlag(0x03F6, 0, 0x1FB0))

    Jump('loc_AD3')

    def _loc_A6D(): pass

    label('loc_A6D')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_AD3(): pass

    label('loc_AD3')

    Jump('loc_B07')

    def _loc_AD6(): pass

    label('loc_AD6')

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
    def _loc_B07(): pass

    label('loc_B07')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xB15
@scena.Code('func_08_B15')
def func_08_B15():
    UnlockAchievement(0x02, 0x007E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F6, 1, 0x1FB1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['琥耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_B89',
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
    SetScenaFlags(ScenaFlag(0x03F6, 1, 0x1FB1))

    Jump('loc_BEF')

    def _loc_B89(): pass

    label('loc_B89')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_BEF(): pass

    label('loc_BEF')

    Jump('loc_C23')

    def _loc_BF2(): pass

    label('loc_BF2')

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
    def _loc_C23(): pass

    label('loc_C23')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC31
@scena.Code('func_09_C31')
def func_09_C31():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 200, 84600, 0)
    ChrSetPos(0x0101, 500, 200, 84100, 180)
    ChrSetPos(0x0102, -500, 200, 84100, 180)
    ChrSetPos(0x00F8, 500, 200, 85100, 180)
    ChrSetPos(0x00F9, -500, 200, 85100, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(120, 200, 82670, 0)
    ChrSetPos(0x0000, 120, 200, 82670, 180)
    ChrSetPos(0x0001, 120, 200, 82670, 180)
    ChrSetPos(0x0002, 120, 200, 82670, 180)
    ChrSetPos(0x0003, 120, 200, 82670, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000A offset: 0xD31
@scena.Code('func_0A_D31')
def func_0A_D31():
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
    CameraMove(0, 200, 84600, 0)
    ChrSetPos(0x0101, -500, 200, 85100, 0)
    ChrSetPos(0x0102, 500, 200, 85100, 0)
    ChrSetPos(0x00F8, -500, 200, 84100, 0)
    ChrSetPos(0x00F9, 500, 200, 84100, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1702._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0xDA9
@scena.Code('func_0B_DA9')
def func_0B_DA9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-43200, 8200, 98000, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, -42700, 8200, 98500, 90)
    ChrSetPos(0x0102, -42700, 8200, 97500, 90)
    ChrSetPos(0x00F8, -43700, 8200, 98500, 90)
    ChrSetPos(0x00F9, -43700, 8200, 97500, 90)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(-41260, 8200, 98030, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, -41260, 8200, 98030, 90)
    ChrSetPos(0x0001, -41260, 8200, 98030, 90)
    ChrSetPos(0x0002, -41260, 8200, 98030, 90)
    ChrSetPos(0x0003, -41260, 8200, 98030, 90)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000C offset: 0xEBB
@scena.Code('func_0C_EBB')
def func_0C_EBB():
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
    CameraMove(-43200, 8200, 98000, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, -43700, 8200, 97500, 270)
    ChrSetPos(0x0102, -43700, 8200, 98500, 270)
    ChrSetPos(0x00F8, -42700, 8200, 97500, 270)
    ChrSetPos(0x00F9, -42700, 8200, 98500, 270)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1702._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0xF3C
@scena.Code('func_0D_F3C')
def func_0D_F3C():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(43400, 8200, 98000, 0)
    ChrSetPos(0x0101, 42900, 8200, 97500, 270)
    ChrSetPos(0x0102, 42900, 8200, 98500, 270)
    ChrSetPos(0x00F8, 43900, 8200, 97500, 270)
    ChrSetPos(0x00F9, 43900, 8200, 98500, 270)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(41380, 8200, 97960, 0)
    ChrSetPos(0x0000, 41380, 8200, 97960, 270)
    ChrSetPos(0x0001, 41380, 8200, 97960, 270)
    ChrSetPos(0x0002, 41380, 8200, 97960, 270)
    ChrSetPos(0x0003, 41380, 8200, 97960, 270)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000E offset: 0x103C
@scena.Code('func_0E_103C')
def func_0E_103C():
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
    CameraMove(43400, 8200, 98000, 0)
    ChrSetPos(0x0101, 43900, 8200, 98500, 90)
    ChrSetPos(0x0102, 43900, 8200, 97500, 90)
    ChrSetPos(0x00F8, 42900, 8200, 98500, 90)
    ChrSetPos(0x00F9, 42900, 8200, 97500, 90)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1702._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x10B4
@scena.Code('func_0F_10B4')
def func_0F_10B4():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(32000, 200, -34400, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 31500, 200, -33900, 0)
    ChrSetPos(0x0102, 32500, 200, -33900, 0)
    ChrSetPos(0x00F8, 31500, 200, -34900, 0)
    ChrSetPos(0x00F9, 32500, 200, -34900, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(31900, 200, -32360, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, 31900, 200, -32360, 0)
    ChrSetPos(0x0001, 31900, 200, -32360, 0)
    ChrSetPos(0x0002, 31900, 200, -32360, 0)
    ChrSetPos(0x0003, 31900, 200, -32360, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0010 offset: 0x11C6
@scena.Code('func_10_11C6')
def func_10_11C6():
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
    CameraMove(32000, 200, -34400, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 32500, 200, -34900, 180)
    ChrSetPos(0x0102, 31500, 200, -34900, 180)
    ChrSetPos(0x00F8, 32500, 200, -33900, 180)
    ChrSetPos(0x00F9, 31500, 200, -33900, 180)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1702._SN', 108, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x1247
@scena.Code('func_11_1247')
def func_11_1247():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-32000, 200, -34400, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, -32500, 200, -33900, 0)
    ChrSetPos(0x0102, -31500, 200, -33900, 0)
    ChrSetPos(0x00F8, -32500, 200, -34900, 0)
    ChrSetPos(0x00F9, -31500, 200, -34900, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(-32100, 200, -32530, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, -32100, 200, -32530, 0)
    ChrSetPos(0x0001, -32100, 200, -32530, 0)
    ChrSetPos(0x0002, -32100, 200, -32530, 0)
    ChrSetPos(0x0003, -32100, 200, -32530, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0012 offset: 0x1359
@scena.Code('func_12_1359')
def func_12_1359():
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
    CameraMove(-32000, 200, -34400, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, -31500, 200, -34900, 180)
    ChrSetPos(0x0102, -32500, 200, -34900, 180)
    ChrSetPos(0x00F8, -31500, 200, -33900, 180)
    ChrSetPos(0x00F9, -32500, 200, -33900, 180)
    OP_0D()
    Call(0, 0x001D)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1702._SN', 109, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x13DA
@scena.Code('func_13_13DA')
def func_13_13DA():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 200, 51500, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, -500, 200, 52000, 0)
    ChrSetPos(0x0102, 500, 200, 52000, 0)
    ChrSetPos(0x00F8, -500, 200, 51000, 0)
    ChrSetPos(0x00F9, 500, 200, 51000, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(-100, 200, 53480, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, -100, 200, 53480, 0)
    ChrSetPos(0x0001, -100, 200, 53480, 0)
    ChrSetPos(0x0002, -100, 200, 53480, 0)
    ChrSetPos(0x0003, -100, 200, 53480, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0014 offset: 0x14EC
@scena.Code('func_14_14EC')
def func_14_14EC():
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
    CameraMove(0, 200, 51500, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 500, 200, 51000, 180)
    ChrSetPos(0x0102, -500, 200, 51000, 180)
    ChrSetPos(0x00F8, 500, 200, 52000, 180)
    ChrSetPos(0x00F9, -500, 200, 52000, 180)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1704._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x156D
@scena.Code('func_15_156D')
def func_15_156D():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-16000, 200, 68400, 0)
    ChrSetPos(0x0101, -15500, 200, 67900, 180)
    ChrSetPos(0x0102, -16500, 200, 67900, 180)
    ChrSetPos(0x00F8, -15500, 200, 68900, 180)
    ChrSetPos(0x00F9, -16500, 200, 68900, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(-15940, 200, 66450, 0)
    ChrSetPos(0x0000, -15940, 200, 66450, 180)
    ChrSetPos(0x0001, -15940, 200, 66450, 180)
    ChrSetPos(0x0002, -15940, 200, 66450, 180)
    ChrSetPos(0x0003, -15940, 200, 66450, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0016 offset: 0x166D
@scena.Code('func_16_166D')
def func_16_166D():
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
    CameraMove(-16000, 200, 68400, 0)
    ChrSetPos(0x0101, -16500, 200, 68900, 0)
    ChrSetPos(0x0102, -15500, 200, 68900, 0)
    ChrSetPos(0x00F8, -16500, 200, 67900, 0)
    ChrSetPos(0x00F9, -15500, 200, 67900, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1704._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x16E5
@scena.Code('func_17_16E5')
def func_17_16E5():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(16000, 200, 68400, 0)
    ChrSetPos(0x0101, 16500, 200, 67900, 180)
    ChrSetPos(0x0102, 15500, 200, 67900, 180)
    ChrSetPos(0x00F8, 16500, 200, 68900, 180)
    ChrSetPos(0x00F9, 15500, 200, 68900, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(16100, 200, 66510, 0)
    ChrSetPos(0x0000, 16100, 200, 66510, 180)
    ChrSetPos(0x0001, 16100, 200, 66510, 180)
    ChrSetPos(0x0002, 16100, 200, 66510, 180)
    ChrSetPos(0x0003, 16100, 200, 66510, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0018 offset: 0x17E5
@scena.Code('func_18_17E5')
def func_18_17E5():
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
    CameraMove(16000, 200, 68400, 0)
    ChrSetPos(0x0101, 15500, 200, 68900, 0)
    ChrSetPos(0x0102, 16500, 200, 68900, 0)
    ChrSetPos(0x00F8, 15500, 200, 67900, 0)
    ChrSetPos(0x00F9, 16500, 200, 67900, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1704._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x185D
@scena.Code('func_19_185D')
def func_19_185D():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(21600, 8200, 86100, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 22100, 8200, 86600, 90)
    ChrSetPos(0x0102, 22100, 8200, 85600, 90)
    ChrSetPos(0x00F8, 21100, 8200, 86600, 90)
    ChrSetPos(0x00F9, 21100, 8200, 85600, 90)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(23480, 8200, 86130, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, 23480, 8200, 86130, 90)
    ChrSetPos(0x0001, 23480, 8200, 86130, 90)
    ChrSetPos(0x0002, 23480, 8200, 86130, 90)
    ChrSetPos(0x0003, 23480, 8200, 86130, 90)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x001A offset: 0x196F
@scena.Code('func_1A_196F')
def func_1A_196F():
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
    CameraMove(21600, 8200, 86100, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 21100, 8200, 85600, 270)
    ChrSetPos(0x0102, 21100, 8200, 86600, 270)
    ChrSetPos(0x00F8, 22100, 8200, 85600, 270)
    ChrSetPos(0x00F9, 22100, 8200, 86600, 270)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1704._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x19F0
@scena.Code('func_1B_19F0')
def func_1B_19F0():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-21400, 8200, 86000, 0)
    ChrSetPos(0x0101, -21900, 8200, 85500, 270)
    ChrSetPos(0x0102, -21900, 8200, 86500, 270)
    ChrSetPos(0x00F8, -20900, 8200, 85500, 270)
    ChrSetPos(0x00F9, -20900, 8200, 86500, 270)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x001F)
    Fade(500)
    CameraMove(-23380, 8200, 85960, 0)
    ChrSetPos(0x0000, -23380, 8200, 85960, 270)
    ChrSetPos(0x0001, -23380, 8200, 85960, 270)
    ChrSetPos(0x0002, -23380, 8200, 85960, 270)
    ChrSetPos(0x0003, -23380, 8200, 85960, 270)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x001C offset: 0x1AF0
@scena.Code('func_1C_1AF0')
def func_1C_1AF0():
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
    CameraMove(-21400, 8200, 86000, 0)
    ChrSetPos(0x0101, -20900, 8200, 86500, 90)
    ChrSetPos(0x0102, -20900, 8200, 85500, 90)
    ChrSetPos(0x00F8, -21900, 8200, 86500, 90)
    ChrSetPos(0x00F9, -21900, 8200, 85500, 90)
    OP_0D()
    Call(0, 0x001E)
    Call(0, 0x0020)
    NewScene('ED6_DT21/C1704._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x1B68
@scena.Code('func_1D_1B68')
def func_1D_1B68():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001E offset: 0x1C47
@scena.Code('func_1E_1C47')
def func_1E_1C47():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001F offset: 0x1D26
@scena.Code('func_1F_1D26')
def func_1F_1D26():
    @scena.Lambda('lambda_1D2C')
    def lambda_1D2C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1D2C)

    @scena.Lambda('lambda_1D3E')
    def lambda_1D3E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1D3E)

    @scena.Lambda('lambda_1D50')
    def lambda_1D50():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1D50)

    @scena.Lambda('lambda_1D62')
    def lambda_1D62():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1D62)

    Sleep(2500)

    Return()

# id: 0x0020 offset: 0x1D74
@scena.Code('func_20_1D74')
def func_20_1D74():
    @scena.Lambda('lambda_1D7A')
    def lambda_1D7A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1D7A)

    @scena.Lambda('lambda_1D8C')
    def lambda_1D8C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1D8C)

    @scena.Lambda('lambda_1D9E')
    def lambda_1D9E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1D9E)

    @scena.Lambda('lambda_1DB0')
    def lambda_1DB0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1DB0)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
