import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5501_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5501   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5501.x'
    header.mapIndex       = 1
    header.bgm            = 31
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
        ('ED6_DT29/CH12190._CH', 'ED6_DT29/CH12190P._CP'),
        ('ED6_DT29/CH12191._CH', 'ED6_DT29/CH12191P._CP'),
        ('ED6_DT29/CH12200._CH', 'ED6_DT29/CH12200P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
        ('ED6_DT29/CH12210._CH', 'ED6_DT29/CH12210P._CP'),
        ('ED6_DT29/CH12211._CH', 'ED6_DT29/CH12211P._CP'),
        ('ED6_DT29/CH12220._CH', 'ED6_DT29/CH12220P._CP'),
        ('ED6_DT29/CH12221._CH', 'ED6_DT29/CH12221P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 53280,
            z                   = -1000,
            y                   = 81930,
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
            x           = 15760,
            z           = 0,
            y           = 94290,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 64760,
            z           = 0,
            y           = 102650,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0388,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 48300,
            z           = 0,
            y           = 54110,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 56540,
            z           = 0,
            y           = 54200,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0388,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 26440,
            z           = -2000,
            y           = 80620,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 45680,
            z           = -2000,
            y           = 78160,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0387,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 16750,
            triggerZ            = 0,
            triggerY            = 57710,
            triggerRange        = 1700,
            actorX              = 16750,
            actorZ              = 2500,
            actorY              = 57710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 46510,
            triggerZ            = 0,
            triggerY            = 67900,
            triggerRange        = 1700,
            actorX              = 46510,
            actorZ              = 2500,
            actorY              = 67900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53050,
            triggerZ            = 0,
            triggerY            = 92420,
            triggerRange        = 1700,
            actorX              = 53050,
            actorZ              = 2500,
            actorY              = 92420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 52570,
            triggerZ            = -2000,
            triggerY            = 81930,
            triggerRange        = 1000,
            actorX              = 53280,
            actorZ              = -2000,
            actorY              = 81930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57950,
            triggerZ            = 0,
            triggerY            = 48100,
            triggerRange        = 1000,
            actorX              = 58010,
            actorZ              = 0,
            actorY              = 47400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 52950,
            triggerZ            = 0,
            triggerY            = 48100,
            triggerRange        = 1000,
            actorX              = 52990,
            actorZ              = 0,
            actorY              = 47400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 47460,
            triggerZ            = 0,
            triggerY            = 48100,
            triggerRange        = 1000,
            actorX              = 47460,
            actorZ              = 0,
            actorY              = 47440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AE
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2AF
@scena.Code('func_01_2AF')
def func_01_2AF():
    PlaySE(455, 0x00, 0x64)
    OP_72(0x0000, 0x0028)
    OP_72(0x0001, 0x0028)
    OP_72(0x0002, 0x0028)
    OP_72(0x0003, 0x0028)
    OP_72(0x0004, 0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 4, 0x10A4)),
            Expr.Return,
        ),
        'loc_2E2',
    )

    OP_6F(0x0001, 120)
    OP_6F(0x0002, 60)

    def _loc_2E2(): pass

    label('loc_2E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 5, 0x10A5)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    OP_6F(0x0001, 120)
    OP_6F(0x0002, 160)

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 6, 0x10A6)),
            Expr.Return,
        ),
        'loc_30C',
    )

    OP_6F(0x0000, 60)
    OP_6F(0x0004, 260)

    def _loc_30C(): pass

    label('loc_30C')

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x6D6),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 3, 0x1103)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    OP_6F(0x0005, 0)

    Jump('loc_32F')

    def _loc_328(): pass

    label('loc_328')

    OP_6F(0x0005, 60)

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 5, 0x1105)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_6F(0x0006, 0)

    Jump('loc_348')

    def _loc_341(): pass

    label('loc_341')

    OP_6F(0x0006, 60)

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 6, 0x1106)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_6F(0x0007, 0)

    Jump('loc_361')

    def _loc_35A(): pass

    label('loc_35A')

    OP_6F(0x0007, 60)

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 7, 0x1107)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_373',
    )

    OP_6F(0x0008, 0)

    Jump('loc_37A')

    def _loc_373(): pass

    label('loc_373')

    OP_6F(0x0008, 60)

    def _loc_37A(): pass

    label('loc_37A')

    OP_E0(0x06, 0x90, 0xE2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xBB, 0x00, 0x00)
    OP_E0(0x07, 0x08, 0xCF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xBB, 0x00, 0x00)
    OP_E0(0x08, 0x80, 0xBB, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xBB, 0x00, 0x00)

    Return()

# id: 0x0002 offset: 0x3A5
@scena.Code('func_02_3A5')
def func_02_3A5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3A5')

    def _loc_3BA(): pass

    label('loc_3BA')

    Return()

# id: 0x0003 offset: 0x3BB
@scena.Code('func_03_3BB')
def func_03_3BB():
    UnlockAchievement(0x02, 0x0183, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 3, 0x1103)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_553',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 4, 0x1104)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49F',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0412')
    def lambda_0412():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0412)

    @scena.Lambda('lambda_042D')
    def lambda_042D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_042D)

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
    Battle(0x00000391, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_47A'),
        (0x00000002, 'loc_48C'),
        (0x00000001, 'loc_49C'),
        (-1, 'loc_49F'),
    )

    def _loc_47A(): pass

    label('loc_47A')

    SetScenaFlags(ScenaFlag(0x0220, 4, 0x1104))
    OP_6F(0x0005, 60)
    Sleep(500)

    Jump('loc_49F')

    def _loc_48C(): pass

    label('loc_48C')

    OP_6F(0x0005, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_49C(): pass

    label('loc_49C')

    OP_B4(0x00)

    Return()

    def _loc_49F(): pass

    label('loc_49F')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['替身木偶'], 1)"),
            Expr.Return,
        ),
        'loc_4EE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0220, 3, 0x1103))

    Jump('loc_550')

    def _loc_4EE(): pass

    label('loc_4EE')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['替身木偶']),
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

    def _loc_550(): pass

    label('loc_550')

    Jump('loc_582')

    def _loc_553(): pass

    label('loc_553')

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
    def _loc_582(): pass

    label('loc_582')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x590
@scena.Code('func_04_590')
def func_04_590():
    UnlockAchievement(0x02, 0x0184, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 5, 0x1105)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_604',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0220, 5, 0x1105))

    Jump('loc_66A')

    def _loc_604(): pass

    label('loc_604')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回复药']),
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

    def _loc_66A(): pass

    label('loc_66A')

    Jump('loc_69E')

    def _loc_66D(): pass

    label('loc_66D')

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
    def _loc_69E(): pass

    label('loc_69E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6AC
@scena.Code('func_05_6AC')
def func_05_6AC():
    UnlockAchievement(0x02, 0x0185, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 6, 0x1106)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_789',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_720',
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
    SetScenaFlags(ScenaFlag(0x0220, 6, 0x1106))

    Jump('loc_786')

    def _loc_720(): pass

    label('loc_720')

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
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_786(): pass

    label('loc_786')

    Jump('loc_7BA')

    def _loc_789(): pass

    label('loc_789')

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
    def _loc_7BA(): pass

    label('loc_7BA')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x7C8
@scena.Code('func_06_7C8')
def func_06_7C8():
    UnlockAchievement(0x02, 0x0186, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 7, 0x1107)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8A5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_83C',
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
    SetScenaFlags(ScenaFlag(0x0220, 7, 0x1107))

    Jump('loc_8A2')

    def _loc_83C(): pass

    label('loc_83C')

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
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_8A2(): pass

    label('loc_8A2')

    Jump('loc_8D6')

    def _loc_8A5(): pass

    label('loc_8A5')

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
    def _loc_8D6(): pass

    label('loc_8D6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x8E4
@scena.Code('func_07_8E4')
def func_07_8E4():
    TalkBegin(0x00FF)
    MapClearFlags(0x00000001)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有拉杆。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 4, 0x10A4)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 5, 0x10A5)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A1B',
    )

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '拉到右边\n'),
            TXT(0x01, '拉到左边\n'),
            TXT(0x02, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9B5',
    )

    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0214, 4, 0x10A4))
    Sleep(500)

    CameraMove(52660, -60, 67850, 1200)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 120)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    Jump('loc_A18')

    def _loc_9B5(): pass

    label('loc_9B5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A18',
    )

    OP_6F(0x0002, 100)
    OP_70(0x0002, 160)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0002)
    SetScenaFlags(ScenaFlag(0x0214, 5, 0x10A5))
    Sleep(500)

    CameraMove(52660, -60, 67850, 1200)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 120)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    def _loc_A18(): pass

    label('loc_A18')

    Jump('loc_AC7')

    def _loc_A1B(): pass

    label('loc_A1B')

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '恢复原状\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 4, 0x10A4)),
            Expr.Return,
        ),
        'loc_A6A',
    )

    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0214, 4, 0x10A4))

    Jump('loc_A8A')

    def _loc_A6A(): pass

    label('loc_A6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 5, 0x10A5)),
            Expr.Return,
        ),
        'loc_A8A',
    )

    OP_6F(0x0002, 160)
    OP_70(0x0002, 100)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0214, 5, 0x10A5))

    def _loc_A8A(): pass

    label('loc_A8A')

    Sleep(500)

    CameraMove(52660, -60, 67850, 1200)
    OP_6F(0x0001, 120)
    OP_70(0x0001, 0)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    def _loc_AC7(): pass

    label('loc_AC7')

    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xAD0
@scena.Code('func_08_AD0')
def func_08_AD0():
    TalkBegin(0x00FF)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '生锈了，好像不能扳动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xAF3
@scena.Code('func_09_AF3')
def func_09_AF3():
    MapSetFlags(0x00000080)
    MapClearFlags(0x00000001)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有拉杆。是否扳动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 6, 0x10A6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B97',
    )

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '降下\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B94',
    )

    EventBegin(0x00)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0000)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 250)
    PlaySE(252, 0x00, 0x64)
    OP_73(0x0004)
    SetScenaFlags(ScenaFlag(0x0214, 6, 0x10A6))
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

    def _loc_B94(): pass

    label('loc_B94')

    Jump('loc_BF8')

    def _loc_B97(): pass

    label('loc_B97')

    Menu(
        0,
        260,
        200,
        1,
        (
            TXT(0x00, '拉起\n'),
            TXT(0x01, '不动\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF8',
    )

    EventBegin(0x00)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0000)
    OP_6F(0x0004, 250)
    OP_70(0x0004, 0)
    PlaySE(252, 0x00, 0x64)
    OP_73(0x0004)
    ClearScenaFlags(ScenaFlag(0x0214, 6, 0x10A6))
    MapSetFlags(0x00000001)
    EventEnd(0x03)

    Return()

    def _loc_BF8(): pass

    label('loc_BF8')

    OP_69(0x0000, 600)
    MapClearFlags(0x00000080)
    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
