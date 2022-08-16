import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5500   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5500.x'
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
    )

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -54250,
            z           = 0,
            y           = 61360,
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
            x           = -45920,
            z           = 0,
            y           = 60730,
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
            x           = -50020,
            z           = 0,
            y           = 99780,
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
            x           = -4000,
            z           = 0,
            y           = 54580,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0388,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -32900,
            triggerZ            = 0,
            triggerY            = 84900,
            triggerRange        = 1700,
            actorX              = -32900,
            actorZ              = 2500,
            actorY              = 84900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13900,
            triggerZ            = 0,
            triggerY            = 73100,
            triggerRange        = 1700,
            actorX              = -13900,
            actorZ              = 2500,
            actorY              = 73100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -44000,
            triggerZ            = 0,
            triggerY            = 52210,
            triggerRange        = 1000,
            actorX              = -44000,
            actorZ              = 0,
            actorY              = 51460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -49990,
            triggerZ            = 0,
            triggerY            = 52200,
            triggerRange        = 1000,
            actorX              = -49990,
            actorZ              = 0,
            actorY              = 51590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -55490,
            triggerZ            = 0,
            triggerY            = 52210,
            triggerRange        = 1000,
            actorX              = -55490,
            actorZ              = 0,
            actorY              = 51550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x20E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x20F
@scena.Code('func_01_20F')
def func_01_20F():
    PlaySE(455, 0x00, 0x64)
    OP_72(0x0000, 0x0028)
    OP_72(0x0001, 0x0028)
    OP_72(0x0002, 0x0028)
    OP_72(0x0003, 0x0028)
    OP_72(0x0004, 0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 1, 0x10A1)),
            Expr.Return,
        ),
        'loc_242',
    )

    OP_6F(0x0000, 120)
    OP_6F(0x0001, 60)

    def _loc_242(): pass

    label('loc_242')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 0, 0x10A0)),
            Expr.Return,
        ),
        'loc_257',
    )

    OP_6F(0x0000, 120)
    OP_6F(0x0001, 160)

    def _loc_257(): pass

    label('loc_257')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 3, 0x10A3)),
            Expr.Return,
        ),
        'loc_26C',
    )

    OP_6F(0x0003, 120)
    OP_6F(0x0004, 60)

    def _loc_26C(): pass

    label('loc_26C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 2, 0x10A2)),
            Expr.Return,
        ),
        'loc_281',
    )

    OP_6F(0x0002, 120)
    OP_6F(0x0004, 160)

    def _loc_281(): pass

    label('loc_281')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 0, 0x1100)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_293',
    )

    OP_6F(0x0005, 0)

    Jump('loc_29A')

    def _loc_293(): pass

    label('loc_293')

    OP_6F(0x0005, 60)

    def _loc_29A(): pass

    label('loc_29A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 1, 0x1101)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AC',
    )

    OP_6F(0x0006, 0)

    Jump('loc_2B3')

    def _loc_2AC(): pass

    label('loc_2AC')

    OP_6F(0x0006, 60)

    def _loc_2B3(): pass

    label('loc_2B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 2, 0x1102)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C5',
    )

    OP_6F(0x0007, 0)

    Jump('loc_2CC')

    def _loc_2C5(): pass

    label('loc_2C5')

    OP_6F(0x0007, 60)

    def _loc_2CC(): pass

    label('loc_2CC')

    Return()

# id: 0x0002 offset: 0x2CD
@scena.Code('func_02_2CD')
def func_02_2CD():
    UnlockAchievement(0x02, 0x0180, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 0, 0x1100)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['精神１'], 1)"),
            Expr.Return,
        ),
        'loc_341',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['精神１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0220, 0, 0x1100))

    Jump('loc_3A7')

    def _loc_341(): pass

    label('loc_341')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['精神１']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['精神１']),
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

    def _loc_3A7(): pass

    label('loc_3A7')

    Jump('loc_3DB')

    def _loc_3AA(): pass

    label('loc_3AA')

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
    def _loc_3DB(): pass

    label('loc_3DB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x3E9
@scena.Code('func_03_3E9')
def func_03_3E9():
    UnlockAchievement(0x02, 0x0181, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 1, 0x1101)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_45D',
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
    SetScenaFlags(ScenaFlag(0x0220, 1, 0x1101))

    Jump('loc_4C3')

    def _loc_45D(): pass

    label('loc_45D')

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

    def _loc_4C3(): pass

    label('loc_4C3')

    Jump('loc_4F7')

    def _loc_4C6(): pass

    label('loc_4C6')

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
    def _loc_4F7(): pass

    label('loc_4F7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x505
@scena.Code('func_04_505')
def func_04_505():
    UnlockAchievement(0x02, 0x0182, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0220, 2, 0x1102)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_579',
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
    SetScenaFlags(ScenaFlag(0x0220, 2, 0x1102))

    Jump('loc_5DF')

    def _loc_579(): pass

    label('loc_579')

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

    def _loc_5DF(): pass

    label('loc_5DF')

    Jump('loc_613')

    def _loc_5E2(): pass

    label('loc_5E2')

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
    def _loc_613(): pass

    label('loc_613')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x621
@scena.Code('func_05_621')
def func_05_621():
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
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 1, 0x10A1)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 0, 0x10A0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_75F',
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
        'loc_6F2',
    )

    OP_6F(0x0001, 0)
    OP_70(0x0001, 60)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0001)
    SetScenaFlags(ScenaFlag(0x0214, 1, 0x10A1))
    CameraMove(-32340, -60, 91590, 1200)
    Sleep(300)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 120)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    Jump('loc_755')

    def _loc_6F2(): pass

    label('loc_6F2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_755',
    )

    OP_6F(0x0001, 100)
    OP_70(0x0001, 160)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0001)
    SetScenaFlags(ScenaFlag(0x0214, 0, 0x10A0))
    CameraMove(-32340, -60, 91590, 1200)
    Sleep(300)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 120)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    def _loc_755(): pass

    label('loc_755')

    OP_69(0x0000, 600)

    Jump('loc_852')

    def _loc_75F(): pass

    label('loc_75F')

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
        'loc_852',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 1, 0x10A1)),
            Expr.Return,
        ),
        'loc_7F0',
    )

    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0001)
    ClearScenaFlags(ScenaFlag(0x0214, 1, 0x10A1))
    Sleep(500)

    CameraMove(-32340, -60, 91590, 1200)
    Sleep(300)

    OP_6F(0x0000, 120)
    OP_70(0x0000, 0)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    Jump('loc_852')

    def _loc_7F0(): pass

    label('loc_7F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 0, 0x10A0)),
            Expr.Return,
        ),
        'loc_852',
    )

    OP_6F(0x0001, 160)
    OP_70(0x0001, 100)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0001)
    ClearScenaFlags(ScenaFlag(0x0214, 0, 0x10A0))
    Sleep(500)

    CameraMove(-32340, -60, 91590, 1200)
    Sleep(300)

    OP_6F(0x0000, 120)
    OP_70(0x0000, 0)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(1000)

    Fade(500)
    OP_69(0x0000, 0)

    def _loc_852(): pass

    label('loc_852')

    MapSetFlags(0x00000001)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x85B
@scena.Code('func_06_85B')
def func_06_85B():
    TalkBegin(0x00FF)
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
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 3, 0x10A3)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 2, 0x10A2)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_93F',
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
        'loc_900',
    )

    OP_6F(0x0004, 0)
    OP_70(0x0004, 60)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0004)
    SetScenaFlags(ScenaFlag(0x0214, 3, 0x10A3))
    OP_6F(0x0003, 0)
    OP_70(0x0003, 120)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0003)

    Jump('loc_93C')

    def _loc_900(): pass

    label('loc_900')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93C',
    )

    OP_6F(0x0004, 100)
    OP_70(0x0004, 160)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0004)
    SetScenaFlags(ScenaFlag(0x0214, 2, 0x10A2))
    OP_6F(0x0002, 0)
    OP_70(0x0002, 120)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0002)

    def _loc_93C(): pass

    label('loc_93C')

    Jump('loc_9DA')

    def _loc_93F(): pass

    label('loc_93F')

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
        'loc_9DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 3, 0x10A3)),
            Expr.Return,
        ),
        'loc_9A4',
    )

    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0004)
    OP_6F(0x0003, 120)
    OP_70(0x0003, 0)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0003)
    ClearScenaFlags(ScenaFlag(0x0214, 3, 0x10A3))

    Jump('loc_9DA')

    def _loc_9A4(): pass

    label('loc_9A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0214, 2, 0x10A2)),
            Expr.Return,
        ),
        'loc_9DA',
    )

    OP_6F(0x0004, 160)
    OP_70(0x0004, 100)
    PlaySE(250, 0x00, 0x64)
    OP_73(0x0004)
    OP_6F(0x0002, 120)
    OP_70(0x0002, 0)
    PlaySE(251, 0x00, 0x64)
    OP_73(0x0002)
    ClearScenaFlags(ScenaFlag(0x0214, 2, 0x10A2))

    def _loc_9DA(): pass

    label('loc_9DA')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
