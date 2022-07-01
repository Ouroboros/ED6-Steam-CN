import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5509_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5509   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '匪兔'),
    TXT(0x02, '目标'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5509.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0x0010
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1879
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT29/CH12240._CH', 'ED6_DT29/CH12240P._CP'),
        ('ED6_DT29/CH12241._CH', 'ED6_DT29/CH12241P._CP'),
        ('ED6_DT29/CH12370._CH', 'ED6_DT29/CH12370P._CP'),
        ('ED6_DT29/CH12371._CH', 'ED6_DT29/CH12371P._CP'),
        ('ED6_DT29/CH12210._CH', 'ED6_DT29/CH12210P._CP'),
        ('ED6_DT29/CH12211._CH', 'ED6_DT29/CH12211P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
        ('ED6_DT29/CH12372._CH', 'ED6_DT29/CH12372P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT27/CH03095._CH', 'ED6_DT27/CH03095P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 45840,
            z                   = 0,
            y                   = 183500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 60000,
            z                   = 500,
            y                   = 183500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01EC,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -5380,
            z           = 0,
            y           = 37760,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 92320,
            z           = 0,
            y           = 33830,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 92630,
            z           = 0,
            y           = 185930,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1B6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 52700,
            y           = -1000,
            z           = 180050,
            range       = 54740,
            dword_10    = 0x000007D0,
            dword_14    = 0x0002D6A4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10005 offset: 0x1D6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -37300,
            triggerZ            = 0,
            triggerY            = 61450,
            triggerRange        = 1000,
            actorX              = -37910,
            actorZ              = 0,
            actorY              = 61450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20470,
            triggerZ            = 0,
            triggerY            = 67000,
            triggerRange        = 1000,
            actorX              = 20470,
            actorZ              = 0,
            actorY              = 67660,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 63940,
            triggerZ            = 0,
            triggerY            = 115470,
            triggerRange        = 1000,
            actorX              = 63940,
            actorZ              = 0,
            actorY              = 116130,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 63700,
            triggerZ            = 0,
            triggerY            = 77700,
            triggerRange        = 1000,
            actorX              = 63700,
            actorZ              = 1300,
            actorY              = 77700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 119240,
            triggerZ            = 250,
            triggerY            = 123450,
            triggerRange        = 1000,
            actorX              = 119240,
            actorZ              = 1550,
            actorY              = 123450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 64050,
            triggerZ            = 0,
            triggerY            = 146260,
            triggerRange        = 1000,
            actorX              = 64050,
            actorZ              = 1300,
            actorY              = 146260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022A, 0, 0x1150)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CC',
    )

    SetChrPos(0x0008, 45840, 0, 183500, 90)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_2CC(): pass

    label('loc_2CC')

    Return()

# id: 0x0001 offset: 0x2CD
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0010, 0x0020)
    OP_72(0x0011, 0x0020)
    OP_72(0x0012, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 4, 0x1024)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_306',
    )

    OP_6F(0x0011, 0)
    OP_70(0x0011, 0x00000000)
    OP_6F(0x0000, 0)

    Jump('loc_329')

    def _loc_306(): pass

    label('loc_306')

    OP_6F(0x0011, 1)
    OP_70(0x0011, 0x00000001)
    OP_6F(0x0015, 30)
    OP_70(0x0015, 0x0000001E)
    OP_6F(0x0000, 30)

    def _loc_329(): pass

    label('loc_329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 6, 0x10AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_342',
    )

    OP_6F(0x0012, 0)
    OP_70(0x0012, 0x00000000)

    Jump('loc_35E')

    def _loc_342(): pass

    label('loc_342')

    OP_6F(0x0012, 1)
    OP_70(0x0012, 0x00000001)
    OP_6F(0x0013, 30)
    OP_70(0x0013, 0x0000001E)

    def _loc_35E(): pass

    label('loc_35E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 7, 0x10AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_377',
    )

    OP_6F(0x0010, 0)
    OP_70(0x0010, 0x00000000)

    Jump('loc_393')

    def _loc_377(): pass

    label('loc_377')

    OP_6F(0x0010, 1)
    OP_70(0x0010, 0x00000001)
    OP_6F(0x0014, 30)
    OP_70(0x0014, 0x0000001E)

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 5, 0x1025)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A5',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3AC')

    def _loc_3A5(): pass

    label('loc_3A5')

    OP_6F(0x0001, 30)

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 0, 0x1140)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BE',
    )

    OP_6F(0x0016, 0)

    Jump('loc_3C5')

    def _loc_3BE(): pass

    label('loc_3BE')

    OP_6F(0x0016, 60)

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 1, 0x1141)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D7',
    )

    OP_6F(0x0017, 0)

    Jump('loc_3DE')

    def _loc_3D7(): pass

    label('loc_3D7')

    OP_6F(0x0017, 60)

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 2, 0x1142)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F0',
    )

    OP_6F(0x0018, 0)

    Jump('loc_3F7')

    def _loc_3F0(): pass

    label('loc_3F0')

    OP_6F(0x0018, 60)

    def _loc_3F7(): pass

    label('loc_3F7')

    Return()

# id: 0x0002 offset: 0x3F8
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_40D',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_40D(): pass

    label('loc_40D')

    Return()

# id: 0x0003 offset: 0x40E
@scena.Code('func_03_40E')
def func_03_40E():
    UnlockAchievement(0x02, 0x96, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 0, 0x1140)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EB',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0016, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_482',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1140)

    Jump('loc_4E8')

    def _loc_482(): pass

    label('loc_482')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0016, 60)
    OP_70(0x0016, 0x00000000)

    def _loc_4E8(): pass

    label('loc_4E8')

    Jump('loc_51C')

    def _loc_4EB(): pass

    label('loc_4EB')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_51C(): pass

    label('loc_51C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x52A
@scena.Code('func_04_52A')
def func_04_52A():
    UnlockAchievement(0x02, 0x97, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 1, 0x1141)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_607',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0017, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['ＥＰ１'], 1)"),
            Expr.Return,
        ),
        'loc_59E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['ＥＰ１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1141)

    Jump('loc_604')

    def _loc_59E(): pass

    label('loc_59E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['ＥＰ１']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['ＥＰ１']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0017, 60)
    OP_70(0x0017, 0x00000000)

    def _loc_604(): pass

    label('loc_604')

    Jump('loc_638')

    def _loc_607(): pass

    label('loc_607')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_638(): pass

    label('loc_638')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x646
@scena.Code('func_05_646')
def func_05_646():
    UnlockAchievement(0x02, 0x98, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0228, 2, 0x1142)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_723',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0018, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_6BA',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1142)

    Jump('loc_720')

    def _loc_6BA(): pass

    label('loc_6BA')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0018, 60)
    OP_70(0x0018, 0x00000000)

    def _loc_720(): pass

    label('loc_720')

    Jump('loc_754')

    def _loc_723(): pass

    label('loc_723')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_754(): pass

    label('loc_754')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x762
@scena.Code('func_06_762')
def func_06_762():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x022A, 0, 0x1150)),
            Expr.Return,
        ),
        'loc_76A',
    )

    Return()

    def _loc_76A(): pass

    label('loc_76A')

    EventBegin(0x00)
    LoadEffect(0x00, 'monster\\ms10180.eff')
    Fade(500)
    OP_6D(53680, 0, 184400, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 45840, 0, 183500, 90)
    ClearChrFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x0009, 58000, 500, 183500, 90)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, 58660, 0, 184000, 270)
    SetChrPos(0x010A, 58660, 0, 183000, 270)

    @scena.Lambda('lambda_081F')
    def lambda_081F():
        OP_91(0x00FE, -5000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_081F)

    Sleep(150)

    @scena.Lambda('lambda_083F')
    def lambda_083F():
        OP_91(0x00FE, -5000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_083F)

    OP_0D()

    @scena.Lambda('lambda_085B')
    def lambda_085B():
        OP_6D(50080, 0, 184400, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_085B)

    TerminateThread(0x0008, 0x00)
    SetChrChipByIndex(0x0008, 8)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_0881')
    def lambda_0881():
        OP_99(0x00FE, 0x00, 0x06, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0881)

    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000014, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000014, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0101, 11)
    SetChrSubChip(0x0101, 0)

    @scena.Lambda('lambda_08D8')
    def lambda_08D8():
        OP_96(0x00FE, 0x0000CDBE, 0x00000000, 0x0002D212, 0x000000C8, 0x00002710)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08D8)

    WaitForThreadExit(0x010A, 0x0001)
    SetChrChipByIndex(0x010A, 14)
    SetChrSubChip(0x010A, 0)

    @scena.Lambda('lambda_0905')
    def lambda_0905():
        OP_96(0x00FE, 0x0000CEAE, 0x00000000, 0x0002C70E, 0x000000C8, 0x00002710)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0905)

    PlayEffect(0x00, 0x01, 0x0008, 1500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x0009, 0, 0, 0, 0)

    @scena.Lambda('lambda_0958')
    def lambda_0958():
        OP_9E(0x00FE, 0x00000050, 0x00000000, 0x00000000, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0958)

    WaitForThreadExit(0x0101, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x010A, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_83(0x01, 0x02)
    TerminateThread(0x0008, 0x02)
    SetChrChipByIndex(0x0008, 8)
    SetChrSubChip(0x0008, 7)
    Sleep(200)

    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    Sleep(400)

    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 9)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x010A, 12)
    SetChrSubChip(0x010A, 0)
    Sleep(1000)

    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x010A, 13)
    SetChrSubChip(0x010A, 0)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x010A, 0x1000)

    @scena.Lambda('lambda_09EE')
    def lambda_09EE():
        OP_8F(0x00FE, 48080, 0, 183600, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09EE)

    @scena.Lambda('lambda_0A09')
    def lambda_0A09():
        OP_8F(0x00FE, 48080, 0, 183400, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0A09)

    TerminateThread(0x0008, 0x00)
    SetChrChipByIndex(0x0008, 3)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_0A32')
    def lambda_0A32():
        OP_8F(0x00FE, 50800, 0, 183500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A32)

    Sleep(400)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0008, 0x01)
    Battle(0x00000396, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_A79'),
        (0x00000000, 'loc_A7E'),
        (0x00000002, 'loc_A85'),
        (-1, 'loc_A8C'),
    )

    def _loc_A79(): pass

    label('loc_A79')

    OP_B4(0x00)

    Jump('loc_A8C')

    def _loc_A7E(): pass

    label('loc_A7E')

    Call(0, 0x0007)

    Jump('loc_A8C')

    def _loc_A85(): pass

    label('loc_A85')

    Call(0, 0x0008)

    Jump('loc_A8C')

    def _loc_A8C(): pass

    label('loc_A8C')

    Return()

# id: 0x0007 offset: 0xA8D
@scena.Code('func_07_A8D')
def func_07_A8D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x01)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_6D(48940, 0, 183500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    SetChrPos(0x0000, 48940, 0, 183500, 270)
    SetChrPos(0x0001, 48940, 0, 183500, 270)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x010A, 0x1000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    OP_A2(0x1150)
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0xB45
@scena.Code('func_08_B45')
def func_08_B45():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x01)
    SetChrPos(0x0008, 45840, 0, 183500, 90)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_6D(57100, 0, 183500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    SetChrPos(0x0000, 57100, 0, 183500, 90)
    SetChrPos(0x0001, 57100, 0, 183500, 90)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x010A, 0x1000)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x010A, 65535)
    SetChrSubChip(0x010A, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0xC06
@scena.Code('func_09_C06')
def func_09_C06():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 4, 0x1024)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C15',
    )

    Call(0, 0x000A)

    Jump('loc_C41')

    def _loc_C15(): pass

    label('loc_C15')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门已经被打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_C41(): pass

    label('loc_C41')

    Return()

# id: 0x000A offset: 0xC42
@scena.Code('func_0A_C42')
def func_0A_C42():
    EventBegin(0x00)
    Fade(1000)
    OP_6C(41000, 0)
    SetChrPos(0x0101, 64260, 0, 77280, 6)
    SetChrPos(0x010A, 63120, 0, 77280, 6)
    OP_69(0x0101, 0x00000000)
    OP_0D()
    Sleep(1000)

    OP_6F(0x0015, 0)
    OP_70(0x0015, 0x0000001E)
    OP_22(0x0064, 0x00, 0x64)
    Sleep(1000)

    OP_22(0x009D, 0x00, 0x64)
    OP_6F(0x0011, 1)
    OP_70(0x0011, 0x00000001)
    Fade(1000)
    OP_6D(89570, 0, 79810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(100)

    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000001E)
    Sleep(1500)

    OP_6D(64260, 0, 77280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_0D()
    Sleep(100)

    ChrTurnDirection(0x0101, 0x010A, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191433V#1019F什、什么啊，这个建筑……\n',
            '为什么会有这样的装置！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191434V#818F大概是假想军事施设的\n',
            '保安系统所制造而成的装置吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191435V潜入·逃出任务训练用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191436V#1007F好、好奇怪的训练内容啊。\n',
            '想起在雷斯顿要塞的时候了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191437V#1015F先不说这个……\n',
            '装置目前正在运作，\n',
            '就代表这也是猎兵团干的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191438V#817F嗯，我想没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191439V#816F但是敌人也不可能\n',
            '完全了解这个设施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191440V谨慎沉稳地前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191441V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191442V#814F嗯？\n',
            '怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191443V#1011F『谨慎沉稳』……\n',
            '雪拉姐也说过同样的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191444V#1315F嘿嘿……被你发现了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191445V#810F嗯，我这是跟雪拉前辈现学现卖的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191446V我在准游击士的时候\n',
            '承蒙前辈的关照……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191447V但我的个性太浮躁，\n',
            '所以经常被她像口头禅一样地念道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191448V#1016F啊哈哈……\n',
            '感觉特别亲切呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191449V不只雪拉姐，\n',
            '我也被约修亚这么说过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191450V#1025F不过……\n',
            '但现在只有我们两个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191451V#1314F嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191452V#1006F走吧，亚妮拉丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191453V『谨慎沉稳』地行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191454V#816F呵呵，明白啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1024)
    OP_28(0x0080, 0x01, 0x0800)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x11CF
@scena.Code('func_0B_11CF')
def func_0B_11CF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 4, 0x1024)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_127B',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010191455V#1000F◆嗯～\n',
            '这个光用手推\n',
            '好像打不开呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191319V#810F嗯，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191457V一定有什么打开的方法才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_127B(): pass

    label('loc_127B')

    Return()

# id: 0x000C offset: 0x127C
@scena.Code('func_0C_127C')
def func_0C_127C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 6, 0x10AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12BD',
    )

    Sleep(100)

    OP_6F(0x0013, 0)
    OP_70(0x0013, 0x0000001E)
    OP_22(0x0064, 0x00, 0x64)
    Sleep(1000)

    OP_22(0x009D, 0x00, 0x64)
    OP_6F(0x0012, 1)
    OP_70(0x0012, 0x00000001)
    OP_A2(0x10AE)
    TalkEnd(0x00FF)

    Jump('loc_12D6')

    def _loc_12BD(): pass

    label('loc_12BD')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '电源已经开启。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkEnd(0x00FF)

    def _loc_12D6(): pass

    label('loc_12D6')

    Return()

# id: 0x000D offset: 0x12D7
@scena.Code('func_0D_12D7')
def func_0D_12D7():
    Return()

# id: 0x000E offset: 0x12D8
@scena.Code('func_0E_12D8')
def func_0E_12D8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 7, 0x10AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_147A',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6C(41000, 0)
    SetChrPos(0x0101, 64050, 0, 145340, 7)
    SetChrPos(0x010A, 62870, 0, 144720, 345)
    OP_69(0x0101, 0x00000000)
    OP_0D()
    Sleep(1000)

    OP_6F(0x0014, 0)
    OP_70(0x0014, 0x0000001E)
    OP_22(0x0064, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0215, 6, 0x10AE)),
            Expr.Return,
        ),
        'loc_1430',
    )

    OP_22(0x009D, 0x00, 0x64)
    OP_6F(0x0010, 1)
    OP_70(0x0010, 0x00000001)
    OP_A2(0x10AF)
    Fade(1000)
    OP_6D(89800, 0, 147350, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(100)

    OP_22(0x006B, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000001E)
    Sleep(1500)

    OP_6D(64069, 0, 145340, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_0D()
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010191458V#1006F好，这样应该就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1025)
    EventEnd(0x00)

    Jump('loc_1477')

    def _loc_1430(): pass

    label('loc_1430')

    ChrTalk(
        0x0101,
        (
            '#0010191459V#1015F……咦？\n',
            '好像没反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6F(0x0014, 30)
    OP_70(0x0014, 0x00000000)
    OP_22(0x0064, 0x00, 0x64)
    Sleep(1000)

    EventEnd(0x00)

    def _loc_1477(): pass

    label('loc_1477')

    Jump('loc_14A6')

    def _loc_147A(): pass

    label('loc_147A')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门已经被打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_14A6(): pass

    label('loc_14A6')

    Return()

# id: 0x000F offset: 0x14A7
@scena.Code('func_0F_14A7')
def func_0F_14A7():
    EventBegin(0x00)
    Fade(1000)
    OP_6C(41000, 0)

    Return()

# id: 0x0010 offset: 0x14B8
@scena.Code('func_10_14B8')
def func_10_14B8():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x416),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14C5',
    )

    Return()

    def _loc_14C5(): pass

    label('loc_14C5')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x020C, 7, 0x1067)),
            Expr.Return,
        ),
        'loc_155B',
    )

    TalkBegin(0x00FF)
    OP_22(0x009D, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证组件已经启动了……\n',
            '但好像没什么特别的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_1851')

    def _loc_155B(): pass

    label('loc_155B')

    TalkBegin(0x00FF)
    OP_22(0x009D, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '认证单元已经启动了……\n',
            '但这个地方好像没什么特别的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1622',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191470V#814F艾丝蒂尔。\n',
            '好像不是这里哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191471V先往前走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0000)

    Jump('loc_184E')

    def _loc_1622(): pass

    label('loc_1622')

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1674',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191472V#812F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_1674(): pass

    label('loc_1674')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16BA',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191473V#813F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_16BA(): pass

    label('loc_16BA')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16FE',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191474V#814F这里好像\n',
            '没什么可用的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_16FE(): pass

    label('loc_16FE')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1744',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191475V#817F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_1744(): pass

    label('loc_1744')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_178A',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191476V#818F嗯～这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_178A(): pass

    label('loc_178A')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17C8',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191477V#819F嗯～看来\n',
            '没找对地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_17C8(): pass

    label('loc_17C8')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_180B',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191478V#1315F这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_180B(): pass

    label('loc_180B')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_184B',
    )

    ChrTalk(
        0x010A,
        (
            '#0120191479V#1316F这里好像\n',
            '没什么可用的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_184B(): pass

    label('loc_184B')

    OP_A2(0x0000)

    def _loc_184E(): pass

    label('loc_184E')

    TalkEnd(0x00FF)

    def _loc_1851(): pass

    label('loc_1851')

    ClearMapFlags(0x00000080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
