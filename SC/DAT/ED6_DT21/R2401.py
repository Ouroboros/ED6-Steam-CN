import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2401.x'
    header.mapIndex       = 103
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1487
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
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT09/CH10340._CH', 'ED6_DT09/CH10340P._CP'),
        ('ED6_DT09/CH10341._CH', 'ED6_DT09/CH10341P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11070._CH', 'ED6_DT09/CH11070P._CP'),
        ('ED6_DT09/CH11071._CH', 'ED6_DT09/CH11071P._CP'),
        ('ED6_DT09/CH11080._CH', 'ED6_DT09/CH11080P._CP'),
        ('ED6_DT09/CH11081._CH', 'ED6_DT09/CH11081P._CP'),
        ('ED6_DT29/CH13010._CH', 'ED6_DT29/CH13010P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -3580,
            z                   = -30,
            y                   = 67370,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -12120,
            z           = 240,
            y           = 43840,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01A9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6530,
            z           = 270,
            y           = 30240,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01A8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x16A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -6700,
            y           = -2000,
            z           = 8900,
            range       = 8200,
            dword_10    = 0x00000BB8,
            dword_14    = 0x000026AC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -21190,
            y           = -3010,
            z           = 80310,
            range       = 20100,
            dword_10    = 0x00000BC2,
            dword_14    = 0x000148F2,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -5300,
            y           = 3000,
            z           = 95360,
            range       = 1100,
            dword_10    = 0x00001388,
            dword_14    = 0x000178F4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = -3580,
            y           = -500,
            z           = 67370,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 10960,
            triggerZ            = -50,
            triggerY            = 86080,
            triggerRange        = 1000,
            actorX              = 11490,
            actorZ              = 1000,
            actorY              = 86480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x20E
@scena.Code('PreInit')
def PreInit():
    OP_A3(0x1350)
    OP_A3(0x1351)
    OP_A3(0x1352)
    OP_A3(0x1353)
    OP_A3(0x1354)
    OP_A3(0x1355)
    OP_A3(0x1356)
    OP_A3(0x1357)
    OP_A3(0x1358)
    OP_A3(0x1359)
    OP_A3(0x1E99)
    OP_A3(0x1E9A)
    OP_A3(0x1E9B)
    OP_A3(0x1E9C)
    OP_A3(0x1E9D)
    OP_A3(0x1E9E)
    OP_A3(0x1E9F)
    OP_A3(0x1EA0)
    OP_A3(0x1EA1)
    OP_A3(0x1EA2)
    OP_A3(0x1EA3)
    OP_A3(0x1EA4)
    OP_A3(0x1EA5)
    OP_A3(0x1EA6)
    OP_A3(0x1EA7)
    OP_A3(0x1EA8)
    OP_A3(0x1EA9)
    OP_A3(0x1EAA)
    OP_A3(0x1EAB)
    OP_A3(0x1EAC)
    OP_A3(0x1EAD)
    OP_A3(0x1EAE)
    OP_A3(0x1EAF)
    OP_A3(0x1EB0)
    OP_A3(0x1EB1)
    OP_A3(0x1EB2)
    OP_A3(0x1EB3)
    OP_A3(0x1EB4)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_296',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    Jump('loc_2A6')

    def _loc_296(): pass

    label('loc_296')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A6',
    )

    Event(0, 0x000E)

    def _loc_2A6(): pass

    label('loc_2A6')

    Return()

# id: 0x0001 offset: 0x2A7
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0430, 0xFFFECB68, 0x00230024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D3',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D3(): pass

    label('loc_2D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 7, 0x130F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E5',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2EC')

    def _loc_2E5(): pass

    label('loc_2E5')

    OP_6F(0x0000, 60)

    def _loc_2EC(): pass

    label('loc_2EC')

    OP_E0(0x00, 0x14, 0x28, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x98, 0x4D, 0x01, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_309',
    )

    Jump('loc_359')

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_359',
    )

    LoadEffect(0x00, 'map\\\\mp086_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -2070, 6000, 96100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_359(): pass

    label('loc_359')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_372',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    Jump('loc_378')

    def _loc_372(): pass

    label('loc_372')

    OP_10(0x01, 0x01)
    OP_10(0x02, 0x00)

    def _loc_378(): pass

    label('loc_378')

    OP_B2(0x00, 0x03, 0x0080)
    SetChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 3, 0x20FB)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_398',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x03, 0x0080)

    def _loc_398(): pass

    label('loc_398')

    Return()

# id: 0x0002 offset: 0x399
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xE8, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 7, 0x130F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_476',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['省ＥＰ１'], 1)"),
            Expr.Return,
        ),
        'loc_40D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['省ＥＰ１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x130F)

    Jump('loc_473')

    def _loc_40D(): pass

    label('loc_40D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['省ＥＰ１']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['省ＥＰ１']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_473(): pass

    label('loc_473')

    Jump('loc_4A7')

    def _loc_476(): pass

    label('loc_476')

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
    def _loc_4A7(): pass

    label('loc_4A7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4B5
@scena.Code('func_03_4B5')
def func_03_4B5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 3, 0x20FB)),
            Expr.Return,
        ),
        'loc_4BD',
    )

    Return()

    def _loc_4BD(): pass

    label('loc_4BD')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_5A2'),
        (-1, 'loc_5C5'),
    )

    def _loc_5A2(): pass

    label('loc_5A2')

    Fade(500)
    OP_89(0x0000, -3140, -60, 60730, 357)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_5C5(): pass

    label('loc_5C5')

    Battle(0x00000EF2, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -3140, -60, 60730, 357)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_5FE'),
        (0x00000001, 'loc_601'),
        (-1, 'loc_604'),
    )

    def _loc_5FE(): pass

    label('loc_5FE')

    EventEnd(0x00)

    Return()

    def _loc_601(): pass

    label('loc_601')

    OP_B4(0x00)

    Return()

    def _loc_604(): pass

    label('loc_604')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x03, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x20FB)
    OP_28(0x00BA, 0x04, 0x10)
    OP_28(0x00BA, 0x04, 0x02)
    OP_28(0x00BA, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x670
@scena.Code('func_04_670')
def func_04_670():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_687',
    )

    Call(0, 0x0007)
    Call(0, 0x0008)

    def _loc_687(): pass

    label('loc_687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 2, 0x1E12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85E',
    )

    OP_6D(-1330, 20, 82650, 0)
    OP_67(0, 12040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(341, 0)
    SetChrPos(0x0101, 280, -30, 13880, 0)
    SetChrPos(0x0102, -1200, -10, 13760, 0)
    SetChrPos(0x0103, 280, 0, 12600, 0)
    SetChrPos(0x00F9, -1140, 20, 12330, 0)

    @scena.Lambda('lambda_0716')
    def lambda_0716():
        OP_6D(-450, 20, 21490, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0716)

    OP_C8(0x0200, 0x0046, 'C_PLAC20._CH', 0x01, 0x03E8)
    ShowPlaceName('绀碧之塔')
    FadeIn(1000, 0)
    OP_0D()
    Sleep(3000)

    @scena.Lambda('lambda_075C')
    def lambda_075C():
        OP_8E(0x00FE, 10, 20, 21400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_075C)

    @scena.Lambda('lambda_0777')
    def lambda_0777():
        OP_8E(0x00FE, -1220, 20, 21400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0777)

    @scena.Lambda('lambda_0792')
    def lambda_0792():
        OP_8E(0x00FE, -50, 20, 20190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_0792)

    @scena.Lambda('lambda_07AD')
    def lambda_07AD():
        OP_8E(0x00FE, -1470, 0, 20090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_07AD)

    WaitForThreadExit(0x0101, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(790, 50, 13670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    SetChrPos(0x0000, 790, 50, 11360, 0)
    SetChrPos(0x0001, 790, 50, 11360, 0)
    SetChrPos(0x0002, 790, 50, 11360, 0)
    SetChrPos(0x0003, 790, 50, 11360, 0)
    OP_A2(0x1E12)

    Jump('loc_8DF')

    def _loc_85E(): pass

    label('loc_85E')

    OP_6D(790, 50, 13670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 790, 50, 11360, 0)
    SetChrPos(0x0001, 790, 50, 11360, 0)
    SetChrPos(0x0002, 790, 50, 11360, 0)
    SetChrPos(0x0003, 790, 50, 11360, 0)

    def _loc_8DF(): pass

    label('loc_8DF')

    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0005 offset: 0x8F0
@scena.Code('func_05_8F0')
def func_05_8F0():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 2, 0x1E12)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_902',
    )

    Return()

    def _loc_902(): pass

    label('loc_902')

    EventBegin(0x01)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要回『埃尔赛尤』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【回船上】\n'),
            TXT(0x01, '【不回去】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_99E',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_9BE')

    def _loc_99E(): pass

    label('loc_99E')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_9BE(): pass

    label('loc_9BE')

    Return()

# id: 0x0006 offset: 0x9BF
@scena.Code('func_06_9BF')
def func_06_9BF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 2, 0x1E12)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 3, 0x1E13)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_9CC',
    )

    Return()

    def _loc_9CC(): pass

    label('loc_9CC')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9F1',
    )

    Call(0, 0x0007)
    Call(0, 0x0008)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_9F1(): pass

    label('loc_9F1')

    Fade(1000)
    OP_6D(-1000, 2600, 88570, 0)
    OP_67(0, 3330, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(9000, 0)
    OP_6E(437, 0)
    SetChrPos(0x0101, -1150, 400, 83690, 0)
    SetChrPos(0x0102, -2640, 400, 83590, 0)
    SetChrPos(0x0103, -1030, 20, 81750, 0)
    SetChrPos(0x00F9, -2430, 20, 81800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341296V#1015F#2P『绀碧』之塔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341297V这次会被传送到\n',
            '什么样的地方去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341298V#1035F#5P不进去的话\n',
            '是没有办法知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341299V#1042F和『表塔』不同，\n',
            '由于不受空间上的约制，\n',
            '因此内部构造似乎很不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341300V#053F哦……\n',
            '真令人不放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8A')

    def _loc_BA2(): pass

    label('loc_BA2')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BDF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341301V#074F嗯……\n',
            '真令人不安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8A')

    def _loc_BDF(): pass

    label('loc_BDF')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C1C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341302V#1068F唉～真令人不放心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8A')

    def _loc_C1C(): pass

    label('loc_C1C')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C50',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341303V#045F有点紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8A')

    def _loc_C50(): pass

    label('loc_C50')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C8A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341304V#561F呜……\n',
            '心脏跳得好快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C8A(): pass

    label('loc_C8A')

    ChrTalk(
        0x0103,
        (
            '#0030341305V#026F总之……\n',
            '只有进去看看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341306V#022F小心谨慎、一步一步地前进哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0CEF')
    def lambda_0CEF():
        OP_69(0x0000, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0CEF)

    @scena.Lambda('lambda_0CFD')
    def lambda_0CFD():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0CFD)

    @scena.Lambda('lambda_0D15')
    def lambda_0D15():
        OP_6B(3200, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0D15)

    @scena.Lambda('lambda_0D25')
    def lambda_0D25():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0D25)

    @scena.Lambda('lambda_0D35')
    def lambda_0D35():
        OP_6E(262, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0D35)

    OP_A2(0x1E13)
    WaitForThreadExit(0x0000, 0x0000)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xD4A
@scena.Code('func_07_D4A')
def func_07_D4A():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_DC4'),
        (0x00000001, 'loc_DCA'),
        (-1, 'loc_DD0'),
    )

    def _loc_DC4(): pass

    label('loc_DC4')

    OP_A2(0x1200)

    Jump('loc_DD0')

    def _loc_DCA(): pass

    label('loc_DCA')

    OP_A2(0x1201)

    Jump('loc_DD0')

    def _loc_DD0(): pass

    label('loc_DD0')

    Return()

# id: 0x0008 offset: 0xDD1
@scena.Code('func_08_DD1')
def func_08_DD1():
    FadeOut(0, 0, -1)
    OP_6D(-48940, 490, -13310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0009 offset: 0xE5E
@scena.Code('func_09_E5E')
def func_09_E5E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F41',
    )

    EventBegin(0x00)
    Fade(500)
    ClearMapFlags(0x00000001)
    OP_6D(-2080, 5220, 94860, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(14000, 0)
    OP_6E(376, 0)
    SetChrPos(0x0101, -2500, 4000, 94500, 0)
    SetChrPos(0x0102, -1500, 4000, 94500, 0)
    SetChrPos(0x00F8, -2500, 4000, 93500, 0)
    SetChrPos(0x00F9, -1500, 4000, 93500, 0)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, 0x000A)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, 0x000B)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, 0x000C)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, 0x000D)
    WaitForThreadExit(0x00F9, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x02000000)
    NewScene('ED6_DT21/C2300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_F41(): pass

    label('loc_F41')

    Return()

# id: 0x000A offset: 0xF42
@scena.Code('func_0A_F42')
def func_0A_F42():
    OP_91(0x00FE, 0, 0, 1800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0F87')
    def lambda_0F87():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F87)

    @scena.Lambda('lambda_0FA1')
    def lambda_0FA1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0FA1)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000B offset: 0xFC7
@scena.Code('func_0B_FC7')
def func_0B_FC7():
    OP_91(0x00FE, 0, 0, 1800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_100C')
    def lambda_100C():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_100C)

    @scena.Lambda('lambda_1026')
    def lambda_1026():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1026)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x104C
@scena.Code('func_0C_104C')
def func_0C_104C():
    OP_91(0x00FE, 0, 0, 2800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_1091')
    def lambda_1091():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1091)

    @scena.Lambda('lambda_10AB')
    def lambda_10AB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_10AB)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000D offset: 0x10D1
@scena.Code('func_0D_10D1')
def func_0D_10D1():
    OP_91(0x00FE, 0, 0, 2800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_1116')
    def lambda_1116():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1116)

    @scena.Lambda('lambda_1130')
    def lambda_1130():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1130)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000E offset: 0x1156
@scena.Code('func_0E_1156')
def func_0E_1156():
    EventBegin(0x00)
    OP_6D(-2080, 5220, 94860, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(14000, 0)
    OP_6E(376, 0)
    SetChrPos(0x0101, -1500, 4000, 96300, 180)
    SetChrPos(0x0102, -2500, 4000, 96300, 180)
    SetChrPos(0x00F8, -1500, 4000, 96300, 180)
    SetChrPos(0x00F9, -2500, 4000, 96300, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0101, 0x0001)
    ClearChrFlags(0x0102, 0x0001)
    ClearChrFlags(0x00F8, 0x0001)
    ClearChrFlags(0x00F9, 0x0001)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, 0x000F)
    Sleep(800)

    CreateThread(0x0102, 0x00, 0x00, 0x0010)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, 0x0011)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, 0x0012)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    OP_6D(-2150, 4000, 93840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -2150, 4000, 93840, 180)
    SetChrPos(0x0001, -2150, 4000, 93840, 180)
    SetChrPos(0x0002, -2150, 4000, 93840, 180)
    SetChrPos(0x0003, -2150, 4000, 93840, 180)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x12DD
@scena.Code('func_0F_12DD')
def func_0F_12DD():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_12E8')
    def lambda_12E8():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_12E8)

    @scena.Lambda('lambda_1302')
    def lambda_1302():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1302)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_1323')
    def lambda_1323():
        OP_8F(0x00FE, -1500, 3600, 93500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1323)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0010 offset: 0x133E
@scena.Code('func_10_133E')
def func_10_133E():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_1349')
    def lambda_1349():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1349)

    @scena.Lambda('lambda_1363')
    def lambda_1363():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1363)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_1384')
    def lambda_1384():
        OP_8F(0x00FE, -2500, 3600, 93500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1384)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0011 offset: 0x139F
@scena.Code('func_11_139F')
def func_11_139F():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_13AA')
    def lambda_13AA():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_13AA)

    @scena.Lambda('lambda_13C4')
    def lambda_13C4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_13C4)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_13E5')
    def lambda_13E5():
        OP_8F(0x00FE, -1500, 3600, 94500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_13E5)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0012 offset: 0x1400
@scena.Code('func_12_1400')
def func_12_1400():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_140B')
    def lambda_140B():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_140B)

    @scena.Lambda('lambda_1425')
    def lambda_1425():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1425)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_1446')
    def lambda_1446():
        OP_8F(0x00FE, -2500, 3600, 94500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1446)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
