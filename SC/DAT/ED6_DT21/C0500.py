import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0500.x'
    header.mapIndex       = 20
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C0500_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x98C
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
        ('ED6_DT09/CH10110._CH', 'ED6_DT09/CH10110P._CP'),
        ('ED6_DT09/CH10111._CH', 'ED6_DT09/CH10111P._CP'),
        ('ED6_DT09/CH10270._CH', 'ED6_DT09/CH10270P._CP'),
        ('ED6_DT09/CH10271._CH', 'ED6_DT09/CH10271P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -28050,
            z                   = 1000,
            y                   = 56920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 11000,
            z           = 0,
            y           = 0,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -1000,
            z           = 0,
            y           = 14000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19000,
            z           = 0,
            y           = 29000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x13E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x13E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -28190,
            triggerZ            = 0,
            triggerY            = 56290,
            triggerRange        = 1000,
            actorX              = -28050,
            actorZ              = 0,
            actorY              = 56920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2210,
            triggerZ            = 0,
            triggerY            = 30060,
            triggerRange        = 1000,
            actorX              = -1530,
            actorZ              = 0,
            actorY              = 29870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3200,
            triggerZ            = 0,
            triggerY            = -17000,
            triggerRange        = 800,
            actorX              = 3200,
            actorZ              = 1000,
            actorY              = -17000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20000,
            triggerZ            = 0,
            triggerY            = 54040,
            triggerRange        = 600,
            actorX              = -20000,
            actorZ              = 600,
            actorY              = 54040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 15800,
            triggerZ            = 0,
            triggerY            = -160,
            triggerRange        = 1000,
            actorX              = 15800,
            actorZ              = 1000,
            actorY              = -160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -300,
            triggerZ            = 0,
            triggerY            = -10060,
            triggerRange        = 1000,
            actorX              = -2720,
            actorZ              = 0,
            actorY              = -9680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x216
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x217
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0080)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_232',
    )

    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)

    Jump('loc_236')

    def _loc_232(): pass

    label('loc_232')

    OP_64(0x03, 0x0001)

    def _loc_236(): pass

    label('loc_236')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0328, 0, 0x1940)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_248',
    )

    OP_6F(0x0001, 0)

    Jump('loc_24F')

    def _loc_248(): pass

    label('loc_248')

    OP_6F(0x0001, 60)

    def _loc_24F(): pass

    label('loc_24F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0328, 2, 0x1942)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_261',
    )

    OP_6F(0x0002, 0)

    Jump('loc_268')

    def _loc_261(): pass

    label('loc_261')

    OP_6F(0x0002, 60)

    def _loc_268(): pass

    label('loc_268')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BD',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_2BD(): pass

    label('loc_2BD')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x2C3
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2D8',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_2D8(): pass

    label('loc_2D8')

    Return()

# id: 0x0003 offset: 0x2D9
@scena.Code('func_03_2D9')
def func_03_2D9():
    UnlockAchievement(0x02, 0x09, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0328, 0, 0x1940)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_471',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0328, 1, 0x1941)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BD',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0330')
    def lambda_0330():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0330)

    @scena.Lambda('lambda_034B')
    def lambda_034B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_034B)

    ClearChrFlags(0x0008, 0x0080)

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
    Battle(0x0000002E, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_398'),
        (0x00000002, 'loc_3AA'),
        (0x00000001, 'loc_3BA'),
        (-1, 'loc_3BD'),
    )

    def _loc_398(): pass

    label('loc_398')

    OP_A2(0x1941)
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_3BD')

    def _loc_3AA(): pass

    label('loc_3AA')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_3BA(): pass

    label('loc_3BA')

    OP_B4(0x00)

    Return()

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['混沌之刃'], 1)"),
            Expr.Return,
        ),
        'loc_40C',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['混沌之刃']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1940)

    Jump('loc_46E')

    def _loc_40C(): pass

    label('loc_40C')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['混沌之刃']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['混沌之刃']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_46E(): pass

    label('loc_46E')

    Jump('loc_4A0')

    def _loc_471(): pass

    label('loc_471')

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
    def _loc_4A0(): pass

    label('loc_4A0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4AE
@scena.Code('func_04_4AE')
def func_04_4AE():
    UnlockAchievement(0x02, 0x13, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0328, 2, 0x1942)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_522',
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
    OP_A2(0x1942)

    Jump('loc_588')

    def _loc_522(): pass

    label('loc_522')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_588(): pass

    label('loc_588')

    Jump('loc_5BC')

    def _loc_58B(): pass

    label('loc_58B')

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
    def _loc_5BC(): pass

    label('loc_5BC')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5CA
@scena.Code('func_05_5CA')
def func_05_5CA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E2',
    )

    NewScene('ED6_DT21/T0101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5EB')

    def _loc_5E2(): pass

    label('loc_5E2')

    NewScene('ED6_DT21/T0100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_5EB(): pass

    label('loc_5EB')

    Return()

# id: 0x0006 offset: 0x5EC
@scena.Code('func_06_5EC')
def func_06_5EC():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_63D',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_7F8')

    def _loc_63D(): pass

    label('loc_63D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DD',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 15800, 1000, -160, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x00000032)
    OP_73(0x0003)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 15800, 1000, -160, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0003, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_7DD(): pass

    label('loc_7DD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F7',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_7F7(): pass

    label('loc_7F7')

    Return()

    def _loc_7F8(): pass

    label('loc_7F8')

    Return()

# id: 0x0007 offset: 0x7F9
@scena.Code('func_07_7F9')
def func_07_7F9():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0831')
    def lambda_0831():
        OP_6D(-1040, 0, -9430, 700)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0831)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_96C',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x0E, 0x00000004, 0x000001FE, 0x00000000, 0xFFFFD922, 0x0000010E, 0xFFFFF560, 0xFFFFFC18, 0xFFFFDA30)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_966',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_960',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0080)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_95D',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0080)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将在洛连特地下水路发现钓鱼场的事情\n',
            '记录在游击士手册上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_95D(): pass

    label('loc_95D')

    Jump('loc_966')

    def _loc_960(): pass

    label('loc_960')

    OP_28(0x0073, 0x01, 0x0200)

    def _loc_966(): pass

    label('loc_966')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_97B')

    def _loc_96C(): pass

    label('loc_96C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_97B',
    )

    EventEnd(0x01)

    def _loc_97B(): pass

    label('loc_97B')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
