import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1402.x'
    header.mapIndex       = 58
    header.bgm            = 29
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '安赛尔新道方向',
            x                   = 1070,
            z                   = -600,
            y                   = -32720,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3000,
            y           = -2000,
            z           = -22500,
            range       = 5000,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFFADF8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -16000,
            y           = -3500,
            z           = 5000,
            range       = 29380,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0000251C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -2200,
            y           = 3000,
            z           = 19000,
            range       = 4200,
            dword_10    = 0x00001388,
            dword_14    = 0x00004E20,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
    )

# id: 0x10004 offset: 0x128
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -13360,
            triggerZ            = 40,
            triggerY            = -930,
            triggerRange        = 1000,
            actorX              = -14080,
            actorZ              = 40,
            actorY              = -960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 26480,
            triggerZ            = -20,
            triggerY            = 8820,
            triggerRange        = 1000,
            actorX              = 27130,
            actorZ              = -20,
            actorY              = 8920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14820,
            triggerZ            = 40,
            triggerY            = -10480,
            triggerRange        = 1000,
            actorX              = 14240,
            actorZ              = 40,
            actorY              = -10750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x194
@scena.Code('Init')
def Init():
    ClearScenaFlags(ScenaFlag(0x0374, 0, 0x1BA0))
    ClearScenaFlags(ScenaFlag(0x0374, 1, 0x1BA1))
    ClearScenaFlags(ScenaFlag(0x0374, 2, 0x1BA2))
    ClearScenaFlags(ScenaFlag(0x0374, 3, 0x1BA3))
    ClearScenaFlags(ScenaFlag(0x0374, 4, 0x1BA4))
    ClearScenaFlags(ScenaFlag(0x0374, 5, 0x1BA5))
    ClearScenaFlags(ScenaFlag(0x0374, 6, 0x1BA6))
    ClearScenaFlags(ScenaFlag(0x0374, 7, 0x1BA7))
    ClearScenaFlags(ScenaFlag(0x0375, 0, 0x1BA8))
    ClearScenaFlags(ScenaFlag(0x0375, 1, 0x1BA9))
    ClearScenaFlags(ScenaFlag(0x0375, 2, 0x1BAA))
    ClearScenaFlags(ScenaFlag(0x0375, 3, 0x1BAB))
    ClearScenaFlags(ScenaFlag(0x0375, 4, 0x1BAC))
    ClearScenaFlags(ScenaFlag(0x03FB, 6, 0x1FDE))
    ClearScenaFlags(ScenaFlag(0x03FB, 7, 0x1FDF))
    ClearScenaFlags(ScenaFlag(0x03FC, 0, 0x1FE0))
    ClearScenaFlags(ScenaFlag(0x03FC, 1, 0x1FE1))
    ClearScenaFlags(ScenaFlag(0x03FC, 2, 0x1FE2))
    ClearScenaFlags(ScenaFlag(0x03FC, 3, 0x1FE3))
    ClearScenaFlags(ScenaFlag(0x03FC, 4, 0x1FE4))
    ClearScenaFlags(ScenaFlag(0x03FC, 5, 0x1FE5))
    ClearScenaFlags(ScenaFlag(0x03FC, 6, 0x1FE6))
    ClearScenaFlags(ScenaFlag(0x03FC, 7, 0x1FE7))
    ClearScenaFlags(ScenaFlag(0x03FD, 0, 0x1FE8))
    ClearScenaFlags(ScenaFlag(0x03FD, 1, 0x1FE9))
    ClearScenaFlags(ScenaFlag(0x03FD, 2, 0x1FEA))
    ClearScenaFlags(ScenaFlag(0x03FD, 3, 0x1FEB))
    ClearScenaFlags(ScenaFlag(0x03FD, 4, 0x1FEC))
    ClearScenaFlags(ScenaFlag(0x03FD, 5, 0x1FED))
    ClearScenaFlags(ScenaFlag(0x03FD, 6, 0x1FEE))
    ClearScenaFlags(ScenaFlag(0x03FD, 7, 0x1FEF))
    ClearScenaFlags(ScenaFlag(0x03FE, 0, 0x1FF0))
    ClearScenaFlags(ScenaFlag(0x03FE, 1, 0x1FF1))
    ClearScenaFlags(ScenaFlag(0x03FE, 2, 0x1FF2))
    ClearScenaFlags(ScenaFlag(0x03FE, 3, 0x1FF3))
    ClearScenaFlags(ScenaFlag(0x03FE, 4, 0x1FF4))
    ClearScenaFlags(ScenaFlag(0x03FE, 5, 0x1FF5))
    ClearScenaFlags(ScenaFlag(0x03FE, 6, 0x1FF6))
    ClearScenaFlags(ScenaFlag(0x03FE, 7, 0x1FF7))
    ClearScenaFlags(ScenaFlag(0x03FF, 0, 0x1FF8))
    ClearScenaFlags(ScenaFlag(0x03FF, 1, 0x1FF9))
    ClearScenaFlags(ScenaFlag(0x03FF, 2, 0x1FFA))
    ClearScenaFlags(ScenaFlag(0x03FF, 3, 0x1FFB))
    ClearScenaFlags(ScenaFlag(0x03FF, 4, 0x1FFC))
    ClearScenaFlags(ScenaFlag(0x03FF, 5, 0x1FFD))
    ClearScenaFlags(ScenaFlag(0x03FF, 6, 0x1FFE))
    ClearScenaFlags(ScenaFlag(0x03FF, 7, 0x1FFF))
    ClearScenaFlags(ScenaFlag(0x03D0, 0, 0x1E80))
    ClearScenaFlags(ScenaFlag(0x03D0, 1, 0x1E81))
    ClearScenaFlags(ScenaFlag(0x03D0, 2, 0x1E82))
    ClearScenaFlags(ScenaFlag(0x03D0, 3, 0x1E83))
    ClearScenaFlags(ScenaFlag(0x03D0, 4, 0x1E84))
    ClearScenaFlags(ScenaFlag(0x03D0, 5, 0x1E85))
    ClearScenaFlags(ScenaFlag(0x03D0, 6, 0x1E86))
    ClearScenaFlags(ScenaFlag(0x03D0, 7, 0x1E87))
    ClearScenaFlags(ScenaFlag(0x03D1, 0, 0x1E88))
    ClearScenaFlags(ScenaFlag(0x03D1, 1, 0x1E89))
    ClearScenaFlags(ScenaFlag(0x03D1, 2, 0x1E8A))
    ClearScenaFlags(ScenaFlag(0x03D1, 3, 0x1E8B))
    ClearScenaFlags(ScenaFlag(0x03D1, 4, 0x1E8C))
    ClearScenaFlags(ScenaFlag(0x03D1, 5, 0x1E8D))
    ClearScenaFlags(ScenaFlag(0x03D1, 6, 0x1E8E))
    ClearScenaFlags(ScenaFlag(0x03D1, 7, 0x1E8F))
    ClearScenaFlags(ScenaFlag(0x03D2, 0, 0x1E90))
    ClearScenaFlags(ScenaFlag(0x03D2, 1, 0x1E91))
    ClearScenaFlags(ScenaFlag(0x03D2, 2, 0x1E92))
    ClearScenaFlags(ScenaFlag(0x03D2, 3, 0x1E93))
    ClearScenaFlags(ScenaFlag(0x03D2, 4, 0x1E94))
    ClearScenaFlags(ScenaFlag(0x03D2, 5, 0x1E95))
    ClearScenaFlags(ScenaFlag(0x03D2, 6, 0x1E96))
    ClearScenaFlags(ScenaFlag(0x03D2, 7, 0x1E97))
    ClearScenaFlags(ScenaFlag(0x03D3, 0, 0x1E98))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_282',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_05_5B7)

    Jump('loc_292')

    def _loc_282(): pass

    label('loc_282')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_292',
    )

    Event(0, func_0F_10AD)

    def _loc_292(): pass

    label('loc_292')

    Return()

# id: 0x0001 offset: 0x293
@scena.Code('func_01_293')
def func_01_293():
    OP_16(0x02, 4000, -128000, -128000, 2293790)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0369, 0, 0x1B48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B7',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2BE')

    def _loc_2B7(): pass

    label('loc_2B7')

    OP_6F(0x0001, 60)

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0369, 1, 0x1B49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D0',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2D7')

    def _loc_2D0(): pass

    label('loc_2D0')

    OP_6F(0x0002, 60)

    def _loc_2D7(): pass

    label('loc_2D7')

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FF',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_30E',
    )

    Jump('loc_35E')

    def _loc_30E(): pass

    label('loc_30E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_35E',
    )

    LoadEffect(0x00, 'map\\\\mp086_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 1000, 6000, 19900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_35E(): pass

    label('loc_35E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_377',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    Jump('loc_37D')

    def _loc_377(): pass

    label('loc_377')

    OP_10(0x01, 0x01)
    OP_10(0x02, 0x00)

    def _loc_37D(): pass

    label('loc_37D')

    Return()

# id: 0x0002 offset: 0x37E
@scena.Code('func_02_37E')
def func_02_37E():
    Return()

# id: 0x0003 offset: 0x37F
@scena.Code('func_03_37F')
def func_03_37F():
    UnlockAchievement(0x02, 0x01D6, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0369, 0, 0x1B48)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_3F3',
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
    SetScenaFlags(ScenaFlag(0x0369, 0, 0x1B48))

    Jump('loc_459')

    def _loc_3F3(): pass

    label('loc_3F3')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_459(): pass

    label('loc_459')

    Jump('loc_48D')

    def _loc_45C(): pass

    label('loc_45C')

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
    def _loc_48D(): pass

    label('loc_48D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x49B
@scena.Code('func_04_49B')
def func_04_49B():
    UnlockAchievement(0x02, 0x01D7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0369, 1, 0x1B49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_578',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_50F',
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
    SetScenaFlags(ScenaFlag(0x0369, 1, 0x1B49))

    Jump('loc_575')

    def _loc_50F(): pass

    label('loc_50F')

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

    def _loc_575(): pass

    label('loc_575')

    Jump('loc_5A9')

    def _loc_578(): pass

    label('loc_578')

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
    def _loc_5A9(): pass

    label('loc_5A9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5B7
@scena.Code('func_05_5B7')
def func_05_5B7():
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
        'loc_5CE',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)

    def _loc_5CE(): pass

    label('loc_5CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 7, 0x1E1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7BF',
    )

    CameraMove(1390, 400, 7280, 0)
    OP_67(0, 15420, -10000, 0)
    CameraSetDistance(3020, 0)
    OP_6C(45000, 0)
    OP_6E(330, 0)
    OP_12(0x00008CA0, 0x00030D40, 0x00000000)
    ChrSetPos(0x0101, 2390, -280, -23110, 0)
    ChrSetPos(0x0102, 1220, -490, -23160, 0)
    ChrSetPos(0x00F8, 2400, -310, -24380, 0)
    ChrSetPos(0x00F9, 1020, -490, -24400, 0)

    @scena.Lambda('lambda_066A')
    def lambda_066A():
        CameraMove(950, -20, -15430, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_066A)

    OP_C8(0x0200, 0x0046, 'C_PLAC21._CH', 0x00, 0x03E8)
    ShowPlaceName('琥珀之塔')
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    @scena.Lambda('lambda_06B0')
    def lambda_06B0():
        ChrWalkTo(0x00FE, 1830, 10, -16460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06B0)

    @scena.Lambda('lambda_06CB')
    def lambda_06CB():
        ChrWalkTo(0x00FE, 500, -20, -16670, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_06CB)

    @scena.Lambda('lambda_06E6')
    def lambda_06E6():
        ChrWalkTo(0x00FE, 1980, 40, -17790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_06E6)

    @scena.Lambda('lambda_0701')
    def lambda_0701():
        ChrWalkTo(0x00FE, 450, 10, -18090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_0701)

    WaitForThreadExit(0x0101, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_12(0x00008CA0, 0x000186A0, 0x00000000)
    CameraMove(1350, -40, -18500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrSetPos(0x0000, 1350, -40, -20010, 0)
    ChrSetPos(0x0001, 1350, -40, -20010, 0)
    ChrSetPos(0x0002, 1350, -40, -20010, 0)
    ChrSetPos(0x0003, 1350, -40, -20010, 0)
    SetScenaFlags(ScenaFlag(0x03C3, 7, 0x1E1F))

    Jump('loc_840')

    def _loc_7BF(): pass

    label('loc_7BF')

    CameraMove(1350, -40, -18500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 1350, -40, -20010, 0)
    ChrSetPos(0x0001, 1350, -40, -20010, 0)
    ChrSetPos(0x0002, 1350, -40, -20010, 0)
    ChrSetPos(0x0003, 1350, -40, -20010, 0)

    def _loc_840(): pass

    label('loc_840')

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0006 offset: 0x851
@scena.Code('func_06_851')
def func_06_851():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 7, 0x1E1F)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_863',
    )

    Return()

    def _loc_863(): pass

    label('loc_863')

    EventBegin(0x01)
    TalkSetChrName('')

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
        'loc_8FF',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_91F')

    def _loc_8FF(): pass

    label('loc_8FF')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_91F(): pass

    label('loc_91F')

    Return()

# id: 0x0007 offset: 0x920
@scena.Code('func_07_920')
def func_07_920():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92D',
    )

    Return()

    def _loc_92D(): pass

    label('loc_92D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 0, 0x1E20)),
            Expr.Return,
        ),
        'loc_935',
    )

    Return()

    def _loc_935(): pass

    label('loc_935')

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
        'loc_95A',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_95A(): pass

    label('loc_95A')

    Fade(1000)
    CameraMove(1350, 2800, 13070, 0)
    OP_67(0, 2270, -10000, 0)
    CameraSetDistance(2850, 0)
    OP_6C(9000, 0)
    OP_6E(463, 0)
    ChrSetPos(0x0101, 1750, 400, 7850, 0)
    ChrSetPos(0x0102, 240, 400, 7460, 0)
    ChrSetPos(0x00F8, 2000, 50, 6000, 0)
    ChrSetPos(0x00F9, 590, 10, 6000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010341536V#1015F#2P终于到最后的塔了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341537V#1007F如果是和之前的塔一样\n',
            '只有一条路的话，就不会迷路了，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341538V#1035F#5P不过要是有强力的守卫\n',
            '挡路也很麻烦呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341539V#1042F很快就要天黑了……\n',
            '动作最好加快一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341540V#1003F#2P嗯，必须阻止玲才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341541V#1002F大家……\n',
            '打起精神来，继续前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341542V#062F嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B6B(): pass

    label('loc_B6B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B94',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341543V#042F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B94(): pass

    label('loc_B94')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BBF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341544V#022F嗯嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BBF(): pass

    label('loc_BBF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE9',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341545V#1063F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE9(): pass

    label('loc_BE9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C14',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341546V#057F哦哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C14(): pass

    label('loc_C14')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C3F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341547V#072F啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C3F(): pass

    label('loc_C3F')

    @scena.Lambda('lambda_0C45')
    def lambda_0C45():
        OP_69(0x0000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0C45)

    @scena.Lambda('lambda_0C53')
    def lambda_0C53():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C53)

    @scena.Lambda('lambda_0C6B')
    def lambda_0C6B():
        CameraSetDistance(3200, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0C6B)

    @scena.Lambda('lambda_0C7B')
    def lambda_0C7B():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0C7B)

    @scena.Lambda('lambda_0C8B')
    def lambda_0C8B():
        OP_6E(262, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0C8B)

    SetScenaFlags(ScenaFlag(0x03C4, 0, 0x1E20))
    WaitForThreadExit(0x0000, 0x0000)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0008 offset: 0xCA5
@scena.Code('func_08_CA5')
def func_08_CA5():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_D1F'),
        (0x00000001, 'loc_D25'),
        (-1, 'loc_D2B'),
    )

    def _loc_D1F(): pass

    label('loc_D1F')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_D2B')

    def _loc_D25(): pass

    label('loc_D25')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_D2B')

    def _loc_D2B(): pass

    label('loc_D2B')

    Return()

# id: 0x0009 offset: 0xD2C
@scena.Code('func_09_D2C')
def func_09_D2C():
    FadeOut(0, 0, -1)
    CameraMove(-31870, 10, -30550, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            ChrTable['凯文神父'],
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
    OP_69(0x0000, 0)

    Return()

# id: 0x000A offset: 0xDBB
@scena.Code('func_0A_DBB')
def func_0A_DBB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E98',
    )

    EventBegin(0x00)
    Fade(500)
    CameraMove(610, 4000, 21090, 0)
    OP_67(0, 4950, -10000, 0)
    CameraSetDistance(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    ChrSetPos(0x0101, 500, 4000, 18000, 0)
    ChrSetPos(0x0102, 1500, 4000, 18000, 0)
    ChrSetPos(0x00F8, 500, 4000, 17000, 0)
    ChrSetPos(0x00F9, 1500, 4000, 17000, 0)
    CreateThread(0x0101, 0x00, 0x00, func_0B_E99)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, func_0C_F1E)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, func_0D_FA3)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_0E_1028)
    WaitForThreadExit(0x00F9, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    NewScene('ED6_DT21/C1700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E98(): pass

    label('loc_E98')

    Return()

# id: 0x000B offset: 0xE99
@scena.Code('func_0B_E99')
def func_0B_E99():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 2500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0EDE')
    def lambda_0EDE():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0EDE)

    @scena.Lambda('lambda_0EF8')
    def lambda_0EF8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0EF8)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000C offset: 0xF1E
@scena.Code('func_0C_F1E')
def func_0C_F1E():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 2500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0F63')
    def lambda_0F63():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F63)

    @scena.Lambda('lambda_0F7D')
    def lambda_0F7D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0F7D)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000D offset: 0xFA3
@scena.Code('func_0D_FA3')
def func_0D_FA3():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 3500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0FE8')
    def lambda_0FE8():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0FE8)

    @scena.Lambda('lambda_1002')
    def lambda_1002():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1002)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000E offset: 0x1028
@scena.Code('func_0E_1028')
def func_0E_1028():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 3500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_106D')
    def lambda_106D():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_106D)

    @scena.Lambda('lambda_1087')
    def lambda_1087():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1087)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000F offset: 0x10AD
@scena.Code('func_0F_10AD')
def func_0F_10AD():
    EventBegin(0x00)
    CameraMove(610, 4000, 21090, 0)
    OP_67(0, 4950, -10000, 0)
    CameraSetDistance(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    ChrSetPos(0x0101, 1500, 4400, 20500, 180)
    ChrSetPos(0x0102, 500, 4400, 20500, 180)
    ChrSetPos(0x00F8, 1500, 4400, 20500, 180)
    ChrSetPos(0x00F9, 500, 4400, 20500, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, func_10_1239)
    Sleep(800)

    CreateThread(0x0102, 0x00, 0x00, func_11_129A)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, func_12_12FB)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, func_13_135C)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    CameraMove(1110, 4000, 17770, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 1110, 4000, 17770, 180)
    ChrSetPos(0x0001, 1110, 4000, 17770, 180)
    ChrSetPos(0x0002, 1110, 4000, 17770, 180)
    ChrSetPos(0x0003, 1110, 4000, 17770, 180)
    OP_0D()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0010 offset: 0x1239
@scena.Code('func_10_1239')
def func_10_1239():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_1244')
    def lambda_1244():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1244)

    @scena.Lambda('lambda_125E')
    def lambda_125E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_125E)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_127F')
    def lambda_127F():
        ChrMoveTo(0x00FE, 1500, 3600, 17000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_127F)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0011 offset: 0x129A
@scena.Code('func_11_129A')
def func_11_129A():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_12A5')
    def lambda_12A5():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_12A5)

    @scena.Lambda('lambda_12BF')
    def lambda_12BF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_12BF)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_12E0')
    def lambda_12E0():
        ChrMoveTo(0x00FE, 500, 3600, 17000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_12E0)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0012 offset: 0x12FB
@scena.Code('func_12_12FB')
def func_12_12FB():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_1306')
    def lambda_1306():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1306)

    @scena.Lambda('lambda_1320')
    def lambda_1320():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1320)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_1341')
    def lambda_1341():
        ChrMoveTo(0x00FE, 1500, 3600, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1341)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0013 offset: 0x135C
@scena.Code('func_13_135C')
def func_13_135C():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_1367')
    def lambda_1367():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1367)

    @scena.Lambda('lambda_1381')
    def lambda_1381():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1381)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_13A2')
    def lambda_13A2():
        ChrMoveTo(0x00FE, 500, 3600, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_13A2)

    WaitForThreadExit(0x00FE, 0x0002)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
